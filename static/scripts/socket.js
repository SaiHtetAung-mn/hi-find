const SOCKET_URL = 'http://localhost:3000';

const socket = io.connect(SOCKET_URL);

// Register user socket
socket.on('connect', () => {
    if(window.userId == 'None' || !window.userId) return;

    socket.emit('register', { userId: window.userId });
});