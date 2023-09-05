import ApiRequest from '../apiRequest.js';
import { sendMessage } from '../socket.js';

const state = {
    currentChatMateId: null,
    isConversationOpen: false
}

export async function showIncomingMessage(chatMateId, message) {
    if(chatMateId != state.currentChatMateId || !state.isConversationOpen) {
        await renderChatList();
        return;
    }

    appendSingleMessage(message, "incoming");
}

export async function renderConversation(chatMateId, chatMateName) {
    // Clear chat history
    $("#message-list").html("");

    // Clear event handler
    $("#send").unbind('click');

    // Add evnet handler to send 
    $("#send").on('click', () => {
        const message = $("#message-box").val();
        if(!message.trim()) return;

        sendMessage(chatMateId, message);
        appendSingleMessage(message, "outcoming");
        $("#message-box").val("");
        $("#message-list").scrollTop(1000);
    })

    // Render Mate Name
    $("#chat-mate-name").text(chatMateName);
    state.currentChatMateId = chatMateId;

    // Get messages and render
    const messages = await getMessages(chatMateId) || [];
    messages.forEach(msg => {
        const messageType = msg.receiver_id == window.userId ? "incoming" : "outcoming";
        appendSingleMessage(msg.message, messageType);
        $("#message-list").scrollTop(1000);
    });
}

export async function renderChatList() {
    const listContainer = document.getElementById('chat_list');
    listContainer.innerHTML = '';
    const list = await getChatList();

    list.forEach(l => {
        const listItem = document.createElement('li');
        listItem.innerHTML = `
            <li class="block">
                <div class="imgBox">
                    <img src="/static/images/user.jpg" class="cover" alt="">
                </div>
                <div class="details">
                    <div class="listHead">
                        <h4>${l.name}</h4>
                        <p class="time">12:34</p>
                    </div>
                    <div class="message_p">
                        <p>${l.message}</p>
                    </div>
                </div>
            </li>
        `;

        listItem.addEventListener('click', async () => {
            closeChatList();
            openConversation();
            renderConversation(l.mate_id, l.name);
        });

        listContainer.appendChild(listItem);
    }) 
}

export function openChatList() {
    $("#chat-popup").fadeIn();
}

export function closeChatList() {
    $("#chat-popup").fadeOut();
}

export function openConversation() {
    $(".conversation").addClass("show-chatbot");
    state.isConversationOpen = true;
}

export function closeConversation() {
    $(".conversation").removeClass("show-chatbot");
    state.currentChatMateId = null;
    state.isConversationOpen = false;
}

async function getChatList() {
    const data = await ApiRequest(
        `/api/chat/messages/list?user_id=${window.userId}`, 
        { method: 'GET' }
    );

    return data;
}

async function getMessages(chatMateId) {
    const data = await ApiRequest(
        `/api/chat/messages?user_id=${window.userId}&chat_mate=${chatMateId}`,
        { method: 'GET' }
    );

    return data;
}

/**
 * ## Append single message
 * @param {String} message 
 * @param {("incoming"|"outcoming")} type 
 */
function appendSingleMessage(msg, type="outcoming") {
    const messageContainer = document.getElementById('message-list');
    const message = document.createElement('li');
    message.classList.add('chat');
    if(type == "incoming") {
        message.innerHTML = `<img src="/static/images/user.jpg" alt="image" class="msgimg">`;
    }
    message.innerHTML += `<p>${msg}</p>`;
    message.classList.add(type);
    messageContainer.appendChild(message);
}