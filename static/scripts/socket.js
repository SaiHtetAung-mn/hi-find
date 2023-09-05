import { showIncomingMessage } from './chat/chat.js';
const SOCKET_URL = 'http://52.65.64.46:3000';

const socket = io.connect(SOCKET_URL);

// Register user socket
socket.on('connect', () => {
    if(window.userId == 'None' || !window.userId) return;

    register(window.userId);
});

socket.on('receive_message', ({ message, sender_id }) => {
    showIncomingMessage(sender_id, message);
})

export function register(userId) {
    window.userId = userId;
    socket.emit('register', { user_id: window.userId });
}

export function sendMessage(chatMateId, message) {
    socket.emit('send_message', { sender_id: window.userId, receiver_id: chatMateId, message });
}