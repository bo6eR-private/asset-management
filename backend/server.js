const express = require('express')
const path = require('path')

const app = express()
const PORT = process.env.PORT || 3001

app.use(express.json())

app.get('/api/health', (_req, res) => {
  res.json({ ok: true, service: 'asset-management' })
})

const dist = path.join(__dirname, 'dist')
if (require('fs').existsSync(dist)) {
  app.use(express.static(dist))
  app.get('*', (_req, res) => {
    res.sendFile(path.join(dist, 'index.html'))
  })
}

app.listen(PORT, () => {
  console.log(`API: http://localhost:${PORT}`)
})
