const conversationContainer = document.querySelector(".conversation-container");
const textInput = document.getElementById("text");

function appendUserMessage(content) {
    const messageContainer = document.createElement("div");
    messageContainer.className = "message-container user";
    const messageElement = document.createElement("div");
    messageElement.className = "message user-message";
    // Replace newline characters with <br> tags
    messageElement.innerHTML = content.replace(/\n/g, '<br>');
    messageContainer.appendChild(messageElement);
    conversationContainer.appendChild(messageContainer);
}

function appendBotMessage(content) {
    const messageContainer = document.createElement("div");
    messageContainer.className = "message-container bot";
    const messageElement = document.createElement("div");
    messageElement.className = "message bot-message";
    messageElement.textContent = content;
    messageElement.innerHTML = content.replace(/\n/g, '<br>');
    messageContainer.appendChild(messageElement);
    conversationContainer.appendChild(messageContainer);
}
function handleEnter(event) {
    if (event.key === "Enter") {
        event.preventDefault(); // Prevent default behavior (new line)
        sendMessage(); // Call the sendMessage function
    }
}
function sendMessage() {
    const userInput = textInput.value;
    appendUserMessage(userInput);

    textInput.value = ""; // Clear input immediately
    
    fetch("/ask_achraf/", {
        method: "POST",
        body: new URLSearchParams({ text: userInput }),
        headers: {
            "Content-Type": "application/x-www-form-urlencoded"
        }
    })
    .then(response => response.json())
    .then(data => {
        const botResponse = data.modified_text;
        
        appendBotMessage(botResponse);
    });
}

function addBotWelcomeMessage() {
    const welcomeMessage = "Bonjour! Posez moi une question sur Achraf et je vous répondrai en se basant sur les informations dont je dispose.";
    appendBotMessage(welcomeMessage);
}

document.addEventListener("DOMContentLoaded", () => {
    addBotWelcomeMessage();
});