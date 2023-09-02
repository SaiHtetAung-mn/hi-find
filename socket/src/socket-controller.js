const userSocket = { };

exports.registerClient = async (clientSocket, data) => {
    const { userId } = data;

    console.log(`User connected with id: ${userId} and socket id: ${clientSocket.id}`);

    if(userSocket[userId]) {
        userSocket[userId].push(clientSocket.id);
        return;
    }

    userSocket[userId] = [clientSocket.id];
}