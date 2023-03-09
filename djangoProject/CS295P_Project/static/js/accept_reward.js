
$(document).ready(function() {
    $('button[id="accept_reward"]').each(function() {
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