var socket = new WebSocket("ws://localhost:8000/post_reward/2");

socket.onopen = function(event) {
    console.log("WebSocket Connected");
};

socket.onmessage = function(event) {
    var message = JSON.parse(event.data);
    // console.log(message.type);
     if(message.type==="New_Like_number"){
        var xx=$('#like-count'+message.thread_id);
        xx.text(message.likes);
    }
      else if(message.type==="New_Tip"){
        var tip=$('#tip_num');

        tip.text(message.tip_num);
    }

};


var socket2 = new WebSocket("ws://localhost:8000/post_reward/3");

socket2.onmessage = function(event) {
    var message = JSON.parse(event.data);
    if(message.type==="New_DisLike_number"){
        var xx=$('#dislike-count'+message.thread_id);
        xx.text(message.dislikes);
    }
};