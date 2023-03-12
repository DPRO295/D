$(document).ready(function() {

    const bu=document.getElementById('accept_reward');
    const i=document.getElementById('i');
    const accept_word=document.getElementById('accept_word');

    user_id=bu.dataset.user_id;
    is_taken=bu.dataset.is_taken;
    post_user_id=bu.dataset.post_user_id;
    taken_user_name=bu.dataset.taken_user_name;
    taken_user_id=bu.dataset.taken_user_id;
    if(is_taken==='True'){
        if(taken_user_id===user_id){
            i.style.color='blue';
            accept_word.style.color='blue';
            accept_word.innerText='Accepted by You';
        }
        else if(post_user_id===user_id){
            i.style.color='green';
            accept_word.style.color='green';
            accept_word.innerText='Your reward Accepted by '+taken_user_name;
        }
        else{
            i.style.color='orange';
            accept_word.style.color='orange';
            accept_word.innerText='Accepted by others';
        }

    }
    else{
         if(post_user_id===user_id){
            accept_word.innerText='Your reward not Accepted';
        }
         else{
             accept_word.innerText='Not Accepted';
         }
    }
});

$(document).ready(function() {
    $('button[id="accept_reward"]').click(function () {
        var button = $(this);
        // console.log("fewwef");
        // var button = $(this);
        var reward_id = button.data('reward_id');
        var is_taken = button.data('is_taken');
        var user_id = button.data('user_id');
        if (is_taken === 'False') {

            $.ajax({
                url: '/try_accept_reward/',
                method: 'POST',
                data: {
                    reward_id: reward_id,
                    user_id: user_id,
                },
                dataType: "JSON",
                success: function (data) {
                    if (data.status === 1) {        //if success accept reward
                        alert("You have accepted this reward!");
                        //button.css( 'color','orange');                       //change color
                        // window.location.assign("/current_rewards/?reward_id="+reward_id);
                        location.reload();
                    } else {
                        alert(data.error_msg);
                    }

                }
            });
        }
    });
});
//
// });
// $(document).ready(function() {
//     const button = document.getElementById("accept_reward");
//     button.addEventListener('click',function(){
//          // var button=$(this);
//         console.log("fewwef") ;
//         // var button = $(this);
//         var reward_id = button.data('reward_id');
//         var is_taken = button.data('is_taken');
//         var user_id = button.data('user_id');
//         if(is_taken==='False'){
//
//             $.ajax({
//                 url:'/try_accept_reward/',
//                 method:'POST',
//                 data:{
//                     reward_id:reward_id,
//                     user_id:user_id,
//                 },
//                 dataType:"JSON",
//                 success: function (data){
//                     if(data.status===1){        //if success accept reward
//                         alert("You have accepted this reward!");
//                          button.style.color='orange';                       //change color
//                     }
//                     else{
//                         alert(data.error_msg);
//                     }
//
//                 }
//             });
//         }
//
//     });
//
// });