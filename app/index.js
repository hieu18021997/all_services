const express = require('express')
const app = express()
const port = 3001 
const morgan = require('morgan')

app.use(morgan('dev'))

app.use('/', (req, res) => {
  res.send(`Number : ${Math.random()}`)
})

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})
