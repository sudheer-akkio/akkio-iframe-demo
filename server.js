const express = require('express');
const app = express();
const path = require('path');

// app.use((req, res, next) => {
//   res.setHeader('Content-Security-Policy', "frame-ancestors 'self' https://www.akkio.com https://lp.akkio.com");
//   next();
// });

// Serve the HTML file
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'index.html'));
});

// very simple server setup for testing

app.listen(3000, () => {
  console.log('Server is running on port 3000');
});
