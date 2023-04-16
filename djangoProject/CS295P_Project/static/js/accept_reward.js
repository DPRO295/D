
function accept_reward_button_style(){          //change accept reward button's style
    const bu=document.getElementById('accept_reward');
    const i=document.getElementById('i');
    const accept_word=document.getElementById('accept_word');

    user_id=bu.dataset.user_id;
    is_taken=bu.dataset.is_taken;
    post_user_id=bu.dataset.post_user_id;
    taken_user_name=bu.dataset.taken_user_name;
    taken_user_id=bu.dataset.taken_user_id;
    // console.log(is_taken==='true')
    if( is_taken==='true'){
        if( taken_user_id===user_id){
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
}
$(document).ready(function() {

  //   $(document).on('DOMNodeInserted', function(event) {
  //
  //   var target = $(event.target);
  //
  //   if (target.find('#accept_reward').length>0) {
  //     accept_reward_button_style();
  //   }
  //
  // });
});

$(document).ready(function() {
    $(document).on('click', 'button[id="accept_reward"]', function(){
        var button = $(this);
        // var button = $(this);
        var reward_id = button.data('reward_id');
        var is_taken = button.attr('data-is_taken');   //button.data() only reads when DOM is loaded ,not changed
        var user_id = button.data('user_id');
        // console.log(is_taken)
        if (is_taken === 'false') {
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
                        // alert("You have accepted this reward!");
                        button.attr('data-taken_user_id',user_id)     //change stored data for changing style
                        button.attr('data-is_taken','true');
                        $('#parent_card').attr('data-taken_user_id',user_id);
                        accept_reward_button_style();               // accept reward, then button style change
                        update_button($('#parent_card'))            // answer button change
                        // console.log(button.data('is_taken'))
                    } else {
                        // alert(data.error_msg);
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