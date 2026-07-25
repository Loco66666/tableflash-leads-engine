import { createContext, useContext, useMemo, useState } from 'react'

import type { AuthUser, LoginResponse } from './types'

const STORAGE_KEY = 'tfle.auth'
const API_BASE_URL = import.meta.env.VITE_API_BASE_URL ?? 'http://localhost:8000/api/v1'

type AuthState = { token: string; user: AuthUser }

type AuthContextValue = {
  user: AuthUser | null
  token: string | null
  login: (email: string, password: string) => Promise<void>
  logout: () => void
}

const AuthContext = createContext<AuthContextValue | null>(null)

function readStoredState(): AuthState | null {
  const serializedState = localStorage.getItem(STORAGE_KEY)
  if (!serializedState) return null
  try {
    return JSON.parse(serializedState) as AuthState
  } catch {
    localStorage.removeItem(STORAGE_KEY)
    return null
  }
}

export function AuthProvider({ children }: { children: React.ReactNode }) {
  const [authState, setAuthState] = useState<AuthState | null>(readStoredState)
  const value = useMemo<AuthContextValue>(
    () => ({
      user: authState?.user ?? null,
      token: authState?.token ?? null,
      async login(email: string, password: string) {
        const response = await fetch(`${API_BASE_URL}/auth/login`, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ email, password }),
        })
        if (!response.ok) throw new Error('Email ou mot de passe incorrect.')
        const payload = (await response.json()) as LoginResponse
        const nextState = { token: payload.access_token, user: payload.user }
        localStorage.setItem(STORAGE_KEY, JSON.stringify(nextState))
        setAuthState(nextState)
      },
      logout() {
        localStorage.removeItem(STORAGE_KEY)
        setAuthState(null)
      },
    }),
    [authState],
  )
  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>
}

// This hook intentionally shares the provider state with route components.
// eslint-disable-next-line react-refresh/only-export-components
export function useAuth() {
  const context = useContext(AuthContext)
  if (!context) throw new Error('useAuth must be used within AuthProvider')
  return context
}
