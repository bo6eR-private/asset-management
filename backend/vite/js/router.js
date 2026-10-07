const ROUTES = {}

export function defineRoutes(definitions) {
  Object.assign(ROUTES, definitions)
}

export function route(name) {
  const target = ROUTES[name]
  if (!target) {
    console.warn(`Unknown route: ${name}`)
    return
  }

  window.history.pushState({ name }, '', target.path)
  render(name)
}

function matchPath(pathname) {
  return (
    Object.keys(ROUTES).find((name) => ROUTES[name].path === pathname) ||
    'dashboard'
  )
}

function render(name) {
  const target = ROUTES[name] || ROUTES.dashboard
  document.title = target.title
  document.getElementById('app').innerHTML = target.render()

  document.querySelectorAll('.sidebar .nav-link').forEach((el) => {
    el.classList.toggle('active', el.dataset.nav === target.nav)
  })
}

export function startRouter() {
  window.route = route

  window.addEventListener('popstate', () => {
    render(matchPath(window.location.pathname))
  })

  const name = matchPath(window.location.pathname)
  window.history.replaceState({ name }, '', ROUTES[name].path)
  render(name)
}
