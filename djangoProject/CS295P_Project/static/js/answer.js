// can be rewritten by Handlebars or template literal, which don't need to build html in js manually

function update_button(parent){         //add answer/ask button if satisfy condition


   var user_id=parent.attr('data-user_id')
   var post_user_id=parent.attr('data-post_user_id')
   var taken_user_id=parent.attr('data-taken_user_id')
    var text,color;
    if(user_id!==post_user_id && user_id !==taken_user_id)
        return;
    if(user_id===post_user_id){
        text="keep Asking";
        color="purple";
    }
    else if(user_id===taken_user_id){
        text="Answer"
        color="blue";
    }
    var html=`
    <button id="answer_reward" style="float:right; color:${color};background-color: #81F781"  class="card-header-icon">${text}</button>
    `;
    parent.append(html)
    // button.css('background-color','#81F781')
    // if(user_id===post_user_id){
    //     button.text('Keep Asking')
    //     button.css('color','purple')
    // }
    // else if(user_id===taken_user_id){
    //     button.text('Answer')
    //     button.css('color','blue')
    // }
    // else{
    //     button.remove()
    // }
}

                   //show button at the beginning and each time it is inserted
$(document).ready(function() {

  //  listen to button addition
  //   $(document).on('DOMNodeInserted', function(event) {
  //   var target = $(event.target);
  //   if (target.find('#parent_card').length>0 && $('#answer_reward').length===0) {
  //
  //     update_button($('#parent_card'));
  //
  //   }
  // });
     //when accept reward  may create a button
    // $(document).on('click','#accept_reward',function(){
    //     if($('#answer_reward').length===0)
    //         update_button($('#parent_card'));
    // });
});



$(document).ready(function() {          // build texting area while click the answer/ask button
   $(document).on('click','#answer_reward',function(){

      var parent=$(this).parent();
      var bu=$(this);
      bu.remove();
      var board=$('<div>');
      board.addClass('control');
      board.attr('id','board')
      parent.append(board);

      var answer_area=$('<textarea>')
      answer_area.addClass('textarea')
      answer_area.attr('id','answer_area')
      answer_area.attr('rows','10')
      board.append(answer_area)

      var submit_button=$('<button>')
      submit_button.addClass('card-header-icon')
      submit_button.css({'color':'red','float':'right'})
      submit_button.attr('id','submit_button')
      submit_button.text('Submit')
      parent.append(submit_button)

   });
});

$(document).ready(function() {
  // When the send button is clicked

    $(document).on('click','#submit_button',function(){   // build html while submit answer
        var button=$('#submit_button')
        var par=button.parent()
    // Get the text from the textarea
    var text = $('#answer_area').val();
    var reward_id=par.attr('data-reward_id')
      var user_id=par.attr('data-user_id')
        var username=par.attr('data-username')
    // Send the text to the backend using AJAX
    $.ajax({
      url: '/add_reward_answer/',
      type: 'POST',
      data: { text: text, reward_id:reward_id, user_id:user_id },
      success: function() {
        // Handle the response from the backend
            var submit=$('#submit_button')
            var parent=submit.parent()
            submit.remove()
            $('#board').remove()
            var answer=$('<div>')
          answer.addClass('card-content')
          answer.text(text)
          parent.append(answer)
          var bar=$('<div>')
          bar.css({'background-color':'white','height':'30px'})
          var author=$('<div>')
            author.text('author: '+username)
          author.css('float','right')
          // author.css('color','purple')
          bar.append(author)
          parent.append(bar)

      update_button(parent);      // after submit, add answer/ask button
      },
    });
  });
});