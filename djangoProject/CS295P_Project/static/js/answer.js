// can be rewritten by Handlebars or template literal, which don't need to build html in js manually

function update_button(button){
    var parent=button.parent()
   var user_id=parent.attr('data-user_id')
   var post_user_id=parent.attr('data-post_user_id')
   var taken_user_id=parent.attr('data-taken_user_id')
    // console.log(user_id,post_user_id,taken_user_id)
    button.css('background-color','#81F781')
    if(user_id===post_user_id){
        button.text('Keep Asking')
        button.css('color','purple')
    }
    else if(user_id===taken_user_id){
        button.text('Answer')
        button.css('color','blue')
    }
    else{
        button.remove()
    }
}
                   //show button at the beginning and each time it is inserted
$(document).ready(function() {
  // Find all existing buttons with the ID "answer_reward" and apply the updateButton function to them
  $('#answer_reward').each(function() {
    update_button($(this));
  });

  // Listen for changes to the DOM and apply the updateButton function to any newly added buttons with the ID "answer_reward"
  $(document).on('DOMNodeInserted', function(event) {
    var target = $(event.target);
    if (target.is('#answer_reward')) {
      update_button(target);
    }
  });
});



$(document).ready(function() {          // build html while click the answer button
   $(document).on('click','#answer_reward',function(){                     // build html while click answer button

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

      var new_button=$('<button>')
      new_button.addClass('card-header-icon')
      new_button.css({'color':'blue','float':'right'})
      new_button.attr('id','answer_reward')
      new_button.text('Answer')
      parent.append(new_button)

      },
    });
  });
});