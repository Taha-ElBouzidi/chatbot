function sendMessage() {
    var userInput = $("#user-input").val();
    if (userInput.trim() === "") {
        return;
    }

    $("#user-input").prop("disabled", true);
    $(".send-icon").css("pointer-events", "none");

    $("#chat-box").append("<div class='chat-message'><b>You:</b> " + userInput + "</div>");
    

    $("#chat-box").append("<div class='chat-message' id='typing-indicator'> <b>Bot: </b> <span class='typing-dot'></span><span class='typing-dot'></span><span class='typing-dot'></span></div>");
    scrollToBottom();
    
    setTimeout(function() {
        

        $.post("/get", { msg: userInput }, function(data) {
            $("#typing-indicator").remove();
            $("#chat-box").append("<div class='chat-message'><b>Bot:</b> " + data.response + "</div>");
            $("#user-input").val("");
            scrollToBottom();
            
 
            $("#user-input").prop("disabled", false);
            $(".send-icon").css("pointer-events", "auto");
        });
    }, 1000);
}

function scrollToBottom() {
    $("#chat-box").scrollTop($("#chat-box")[0].scrollHeight);
}
