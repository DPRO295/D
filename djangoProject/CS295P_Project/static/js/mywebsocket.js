var socket = new WebSocket("ws://localhost:8000/post_reward/1");

socket.onopen = function(event) {
    console.log("WebSocket Connected");
};

socket.onmessage = function(event) {
    var message = JSON.parse(event.data);
    console.log(message.type);
    if (message.type === "NewData" || message.type === "error") {
        var messageDiv = document.createElement("div");
        messageDiv.classList.add("message");

        var messageText = document.createElement("p");
        messageText.textContent = "New message arrived";

        messageDiv.appendChild(messageText);
        document.body.insertBefore(messageDiv, document.body.firstChild);
    }
};