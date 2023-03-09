
    $(function () {
        bindShowThread();
    })
    function bindShowThread() {
        $('header[id^="display_thread"]').each(function () {
            $(this).click(function () {
                var post_id = $(this).data("post_id")
                var title = $(this).data("post_title")
                var email = $(this).data("post_email")
                var date  = $(this).data("post_date")
                var content  = $(this).data("post_content")
                var category  = $(this).data("post_category")
                var user_id  = $(this).data("post_user_id")
                var coin_num = $(this).data("coin_num")
                $.ajax({
                    url: '/show_reward/',
                    method: 'POST',
                    data: {
                        post_id: post_id,
                        title:title,
                        emil:email,
                        date:date,
                        content:content,
                        category:category,
                        user_id:user_id,
                        coin_num:coin_num
                    },
                    dataType:"JSON",               // convert the data from POST and read as JSON
                    success: function (res) {
                        var tag1 = document.getElementById("show_post_title");
                        tag1.innerText = res["title"]
                        var tag2 = document.getElementById("show_post_category");
                         tag2.innerText = res["category"]
                        var tag3 = document.getElementById("show_post_content");
                         tag3.innerText = res["content"]
                        var tag4 = document.getElementById("show_post_time");
                         tag4.innerText = res["date"]
                        var tag5 = document.getElementById("show_coin_num");
                         tag5.innerText = res["coin_num"]
                        console.log(res);
                    }
                });
            });
        });
    }

