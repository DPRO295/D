
// Set the rel, type, and href attributes of the link element

// Append the link element to the head of the HTML document


$(document).ready(function() {
    $('header[id^="display_thread"]').each(function() {
        var header=$(this);
        header.click(function () {
            // var button = $(this);
            var button=$("#accept_reward");
            var postId = header.data('post_id');
            if(button.length===0 || parseInt(button.attr('data-reward_id'))!==parseInt(postId)){
                $.ajax({
                    url: '/change_watch/' + postId + '/' ,      //
                    method: 'POST',
                    success: function (data) {
                        $('#watch-count'+postId).text(data.watches);
                    }
                });
            }

        });
    });
});


// document.addEventListener("DOMContentLoaded", function(event) {
//       // Get the value of x from the Django context and convert it to lower case
//     var buttons = document.querySelectorAll('button[id^="watch-button"]');  // Get the button element
//     for(var i=0;i<buttons.length;i++){
//         button = buttons[i];
//         var iswatched = button.getAttribute('data-iswatched');
//         // console.log(iswatched);
//         if (iswatched === "True") {
//             button.classList.add("watch");  // Add class1 to the button class list
//             button.classList.remove("unwatch");  // Remove the default class from the button class list
//
//         } else {
//             button.classList.add("unwatch");  // Add class2 to the button class list
//             button.classList.remove("watch");  // Remove the default class from the button class list
//         }
//     }
//
// });

