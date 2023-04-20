function createReward(parent,data){      //show a reward

    var thread=data.thread
    var comments=data.comments
    var user_id=thread.user_id
    var user_name=thread.user_name
    var post_user_id=thread.post_user_id
    var post_user_name=thread.post_user_name
    var taken_user_name=thread.taken_user_name
    // console.log(thread.content)
    var now=new Date(thread.date)
    now=now.toLocaleString();



    var html=` 
        <header class="card-header">
          <p style="height:54px" class="card-header-title" id="show_post_title">${thread.title}</p>
          </header>
          
          <header class="card-header" style="height:40px;background-color: white">
          <p style="font-size: 1em" class="card-header-title">poster: ${post_user_name}</p>
        `;
    if(user_id===post_user_id && thread.taken_user_id!==0){
        html+=`
            <button id="finish_reward" class="card-header-icon">     
                <a href="/finish_reward/?reward_id=${ thread.id }" class="icon">
                    <i class="fa-solid fa-cannabis" style="font-size:1.5em"></i>
                </a>
            </button>
        `;
    }
    html+=`
            <button id="accept_reward" class="card-header-icon"
                    data-reward_id="${ thread.id }"
                    data-is_taken="${ thread.is_taken }"
                    data-user_id="${ user_id }"
                    data-post_user_id="${ post_user_id }"
                    data-taken_user_name="${ taken_user_name }"
                    data-taken_user_id="${thread.taken_user_id}"
            >
            <i id='i' class="fa-solid fa-square-check" style="font-size: 1.5em;"></i>
                <span id="accept_word" style="padding:0 5px;"></span>

            </button>
            <button class="card-header-icon">
                <span class="icon">
                    <i class="fa-solid fa-coins" style="color:#00b300;font-size:1.5em"></i>
                </span>
                <span style="padding:0 5px; color:#00b300;" id="show_coin_num">
                    ${ thread.coin_num }
                </span>
            </button>
        </header>
    
        <div class="card-content">
        <div class="content">
            <p id="show_post_content"> ${ thread.content }</p>
            <br>
            <time style="float:right" datetime="" id="show_post_time">${ now }</time>
            <br>
        </div>
        </div>
        <div class="card-footer">             
        </div>

        <div id='parent_card'
             data-reward_id=${ thread.id } data-post_user_id=${ post_user_id }
                data-taken_user_id=${ thread.taken_user_id }
             data-user_id=${ user_id } data-username=${ user_name }
              >
            <div style="height:30px;background-color:white"></div>    
    `;
    for(const index in comments){
        var comment=comments[index]
        html+=`
            <div class="card-content">${comment.content}</div>
            <div style="background-color:white;height:30px">
                 <div style="float:right;"> author: ${comment.user_name}</div>   
            </div>
        `;
    }
    html+=`</div>    
    `;
       // <button id="answer_reward" style="float:right; color:blue"  class="card-header-icon">Answer</button>



    parent.html(html)
    accept_reward_button_style()      //update accept button
    update_button($('#parent_card'))  //add answer/ask button
}

$(document).ready(function(){

    $(document).on('click', '[id^="display_thread"]', function(){

        var header=$(this)
        var thread_id=header.attr('data-post_id')
                                            // Update the displayed URL in the address bar without reloading the page
        var newURL="/current_rewards/"+thread_id
        history.pushState(null, null, newURL);
        window.history.replaceState({}, document.title, newURL);

        var parent=$('#parent')

        $.ajax({
           url: '/show_reward/',
            method:'POST',
            data:{
                thread_id:thread_id
            },
            success:function(data){
                // console.log(data.thread)
               createReward(parent,data)
            }
        });
    });

});

$(document).ready(function(){            // simulate click() when getting url to visit a reward
    var x=$('#directory').data('show_thread_id');   //if x is string like 1,25,100 it will be turned to integer by jquery automatically
    x=x.toString()
    if(x!=="-1"){
        $('header[data-post_id='+x+']').click();
    }
});

