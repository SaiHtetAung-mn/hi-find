const http = require('http');
const dotEnv = require('dotenv');
dotEnv.config();

const PORT = process.env['PORT'] || 3000;
const server = http.createServer((req, res) => res.end('Hello! This is Socket Proxy server for Hi-Find'));
const socket = require('./socket');
socket.config(server);

server.listen(PORT, () => console.log(`Socket Server running at http://localhost:${PORT}`));