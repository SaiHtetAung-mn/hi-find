const socketIO = require('socket.io');
const socketEvent = require('./constants/socket-event');
const controller = require('./socket-controller');

exports.config = (server) => {
    const io = socketIO(server, {
        cors: {
          origin: "*",
          methods: "*"
        }
    });

    io.on('connection', (socket) => {
        // Client Events
        socket.on(socketEvent.REGISTER, (data) => controller.registerClient(socket, data));
    })
}