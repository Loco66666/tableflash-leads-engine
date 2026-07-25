import { useNavigate } from 'react-router-dom'

import { useAuth } from '../auth/AuthContext'

export function DashboardPage() {
  const { logout, user } = useAuth()
  const navigate = useNavigate()
  function handleLogout() {
    logout()
    navigate('/login', { replace: true })
  }

  return (
    <main className="app-shell">
      <header className="dashboard-header">
        <div><p className="eyebrow">TFLE — accès sécurisé</p><h1>TableFlash Leads Engine</h1><p>Bonjour {user?.full_name}.</p></div>
        <button type="button" onClick={handleLogout}>Se déconnecter</button>
      </header>
      <section className="dashboard-placeholder"><h2>Dashboard MVP</h2><p>Les fonctionnalités métier seront ajoutées dans les étapes suivantes.</p></section>
    </main>
  )
}
