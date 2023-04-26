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
        var comment=comments[index]
        html+=`
            <div class="card-content">${comment.content}</div>
            <div style="background-color:white;height:30px">
                 <div style="float:right;"> author: ${comment.user_name}</div>   
            </div>
        `;
    }
    parent.html(html)

}
                                // show thread with comments
$(document).ready(function(){

    $(document).on('click', '[id^="display_thread"]', function(){
        var header=$(this)
        var thread_id=header.attr('data-post_id')
                                            // Update the displayed URL in the address bar without reloading the page
        var newURL="/main_page/"+thread_id
        history.pushState(null, null, newURL);
        window.history.replaceState({}, document.title, newURL);

        var parent=$('#parent')

        $.ajax({
           url: '/show_thread/',
            method:'POST',
            data:{
                thread_id:thread_id
            },
            success:function(data){
                // console.log(data.thread)
               createThread(parent,data)
            }
        });
      // $('[id^="display_thread"]').parent().parent().css('background-color','white');
      // header.parent().parent().css('background-color','#99e6ff');

    });

});
$(document).ready(function(){            // simulate click() when getting url to visit a thread
    var x=$('#thread_board').data('show_thread_id');   //if x is string like 1,25,100 it will be turned to integer by jquery automatically
    x=x.toString()
    if(x!=="-1"){
        $('header[data-post_id='+x+']').click();
    }
});
// $(document).ready(function() {
//   // Trigger click event on button with ID "myButton"
//
//   // Listen to click event on button with ID "myButton"
//   $('#myButton').on("click", function() {
//     alert("Button clicked!");
//   });
//   $('#myButton').click();
// });
