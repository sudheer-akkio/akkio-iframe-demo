# akkio-iframe-demo

Demo for showcasing iframe embedding

## Installation and Setup

### Dependencies

You can get these as follows.

```shell
brew install node
npm install express
```

## Getting Started

1. Start the server:

```shell
node server.js
```

2. Navigate to `http://localhost:3000/`

## Notes:

- Public Chat Explore, Public Dashboard, Public Insights Report, and Public Web App can be iframed.
- You can change the iframe src endpoint in `index.html`. Code is documented on how to do this.
- CSP header in `server.js` does not need to set, but included as an example
