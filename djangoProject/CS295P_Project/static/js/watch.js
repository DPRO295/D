
// Set the rel, type, and href attributes of the link element

// Append the link element to the head of the HTML document


$(document).ready(function() {
    $('button[id^="watch-button"]').each(function() {
        var button=$(this);
        button.click(function () {
            // var button = $(this);
            var postId = button.data('post-id');
            var iswatched = button.data('iswatched')
            var userid = button.data('userid');
            $.ajax({
                url: '/change_watch/' + postId + '/' + userid + '/' + iswatched + '/',      // if iswatched, change to  empty heart and reduce number and diswatchd
                method: 'POST',                                                      // else change to full heart and add number and liked
                success: function (data) {
                    $('#watch-count'+postId).text(data.watches);
                    if (iswatched === 'True') {
                        button.data('iswatched', 'False')
                        button.removeClass('watch')
                        button.addClass('unwatch')
                    } else {
                        button.data('iswatched', 'True')
                        button.removeClass('unwatch')
                        button.addClass('watch')
                    }
                }
            });
        });
    });
});


document.addEventListener("DOMContentLoaded", function(event) {
      // Get the value of x from the Django context and convert it to lower case
    var buttons = document.querySelectorAll('button[id^="watch-button"]');  // Get the button element
    for(var i=0;i<buttons.length;i++){
        button = buttons[i];
        var iswatched = button.getAttribute('data-iswatched');
        // console.log(iswatched);
        if (iswatched === "True") {
            button.classList.add("watch");  // Add class1 to the button class list
            button.classList.remove("unwatch");  // Remove the default class from the button class list

        } else {
            button.classList.add("unwatch");  // Add class2 to the button class list
            button.classList.remove("watch");  // Remove the default class from the button class list
        }
    }

});

