
// Set the rel, type, and href attributes of the link element

// Append the link element to the head of the HTML document


$(document).ready(function() {
    $('button[id^="like-button"]').each(function() {
        var button=$(this);
        button.click(function () {
            // var button = $(this);
            var postId = button.data('post-id');
            var isliked = button.data('isliked')
            var userid = button.data('userid');
            $.ajax({
                url: '/change_like/' + postId + '/' + userid + '/' + isliked + '/',      // if isliked, change to  empty heart and reduce number and disliked
                method: 'POST',                                                      // else change to full heart and add number and liked
                success: function (data) {
                    $('#like-count'+postId).text(data.likes);
                    if (isliked === 'True') {
                        button.data('isliked', 'False')
                        button.removeClass('like')
                        button.addClass('unlike')
                    } else {
                        button.data('isliked', 'True')
                        button.removeClass('unlike')
                        button.addClass('like')
                    }
                }
            });
        });
    });
});


document.addEventListener("DOMContentLoaded", function(event) {
      // Get the value of x from the Django context and convert it to lower case
    var buttons = document.querySelectorAll('button[id^="like-button"]');  // Get the button element
    for(var i=0;i<buttons.length;i++){
        button = buttons[i];
        var isliked = button.getAttribute('data-isliked');
        // console.log(isliked);
        if (isliked === "True") {
            button.classList.add("like");  // Add class1 to the button class list
            button.classList.remove("unlike");  // Remove the default class from the button class list

        } else {
            button.classList.add("unlike");  // Add class2 to the button class list
            button.classList.remove("like");  // Remove the default class from the button class list
        }
    }

});

