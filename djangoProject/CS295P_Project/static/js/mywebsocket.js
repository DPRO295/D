var socket = new WebSocket("ws://localhost:8000/post_reward/1");

socket.onopen = function(event) {
    console.log("WebSocket Connected");
};

socket.onmessage = function(event) {
    var message = JSON.parse(event.data);
    console.log(message.type);
    if (message.type === "New_Reward") {

    }
    else if(message.type==="New_Watch_number"){   // update watches number
        var span=$('#watch-count'+message.reward_id);
        span.text(message.watches);
    }
    else if(message.type==="New_Answer"){      // update new answer
        if($('button[data-reward_id="'+message.reward_id+'"]').length>0){
            $('header[data-post_id='+message.reward_id+']').click();
        }
    }
    else if(message.type==="New_Accept_Reward"){      // update accept reward button
        if($('button[data-reward_id="'+message.reward_id+'"]').length>0){
            $('header[data-post_id='+message.reward_id+']').click();
        }
    }
};