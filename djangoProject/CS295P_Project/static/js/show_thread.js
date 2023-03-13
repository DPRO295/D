function createThread(parent,data){      //create a thread for homepage
    var thread=data.thread
    var comments=data.comments
    // console.log(comments)
    var now=new Date(thread.date)
    now=now.toLocaleString();

    var post_user_name=thread.post_user_name

    var html=` 
        <header class="card-header">
          <p style="height:54px" class="card-header-title" id="show_post_title">${thread.title}</p>
          </header>
          
          <header class="card-header" style="height:40px;background-color: white">
          <p style="font-size: 1em" class="card-header-title">poster: ${post_user_name}</p>
         
          <button class="card-header-icon" id="tip" data-thread_id="${thread.id}">
          Tip
          </button>
          
          <div  class="card-header-icon" style="padding: 0 0"  id="tipboard"></div>
          
          <button class="card-header-icon" style="color:green ;">
          <span style="padding-right: 10px; font-size: 1.5em" >
          <i class="fa-solid fa-circle-dollar-to-slot"></i>
          </span>
          <span id="tip_num">${thread.tip_num}</span>     
            </button>
            
          <br>
        </header>
        
        <div class="card-content">
        <div class="content">
            <p id="show_post_content"> ${thread.content}</p>
            <br>
            <time style="float:right" datetime="" id="show_post_time">${now}</time>
            <br>
        </div>
        </div>
        <div style="height:30px;background-color:white"></div>
    `;
    for(const index in comments){
        // console.log(comment.content)
        var comment=comments[index]
        // console.log(comment)
        html+=`
            <div class="card-content">${comment.content}</div>
            <div style="background-color:white;height:30px">
                 <div style="float:right;"> author: ${comment.user_name}</div>   
            </div>
        `;
    }
    parent.html(html)

}
//${comment.comment_user.username}
                                // show thread with comments
$(document).ready(function(){

    $(document).on('click', '[id^="display_thread"]', function(){
        // console.log('are you ok')
        var header=$(this)
        var thread_id=header.attr('data-post_id')
        var parent=$('#parent')

        $.ajax({
           url: '/show_thread/',
            method:'POST',
            data:{
                thread_id:thread_id
            },
            success:function(data){
                console.log(data.thread)
               createThread(parent,data)
            }
        });
    });

});
    // function bindShowThread() {
    //     $('header[id^="display_thread"]').each(function () {
    //         $(this).click(function () {
    //             var post_id = $(this).data("post_id")
    //             var title = $(this).data("post_title")
    //             var email = $(this).data("post_email")
    //             var date  = $(this).data("post_date")
    //             var content  = $(this).data("post_content")
    //             var category  = $(this).data("post_category")
    //             var user_id  = $(this).data("post_user_id")
    //             $.ajax({
    //                 url: '/show_thread/',
    //                 method: 'POST',
    //                 data: {
    //                     post_id: post_id,
    //                     title:title,
    //                     emil:email,
    //                     date:date,
    //                     content:content,
    //                     category:category,
    //                     user_id:user_id,
    //
    //                 },
    //                 dataType:"JSON",               // convert the data from POST and read as JSON
    //                 success: function (res) {
    //                     var tag1 = document.getElementById("show_post_title");
    //                     tag1.innerText = res["title"]
    //                     var tag2 = document.getElementById("show_post_category");
    //                      tag2.innerText = res["category"]
    //                     var tag3 = document.getElementById("show_post_content");
    //                      tag3.innerText = res["content"]
    //                     var tag4 = document.getElementById("show_post_time");
    //                      tag4.innerText = res["date"]
    //                     console.log(res);
    //                 }
    //             });
    //         });
    //     });
    // }

