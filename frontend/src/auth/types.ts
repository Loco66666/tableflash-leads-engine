export type AuthUser = {
  id: string
  full_name: string
  email: string
  role: 'admin' | 'commercial' | 'analyst'
}

export type LoginResponse = {
  access_token: string
  token_type: string
  user: AuthUser
}
