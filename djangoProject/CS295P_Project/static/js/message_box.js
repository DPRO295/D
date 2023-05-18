
$(document).ready(function() {
    $.ajax({
        url: '/update_message_box/',      //
        method: 'POST',
        success: function (data) {
            if(data.read===false){
                $('#message_show').attr("src","/static/img/unread.png")
            }
        }
    });
});