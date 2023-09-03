export const handleSocketEvent = (socket) => {

}

export function sendMessage(socket, receiverId, message) {
    socket.emit('send_message', { receiver_id: receiverId, sender_id: window.userId, message });
}