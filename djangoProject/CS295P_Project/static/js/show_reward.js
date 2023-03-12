
    $(function () {
        //bindShowThread();
         ShowReward();

    })

    function AnswerReward(){
        $('button[id="answer_button"]').each(function () {
            $(this).click(function(){
               const answer_area=document.createElement('textarea');

            });

        });
    }
    function ShowReward(){
        $('header[id^="display_thread"]').each(function () {
            $(this).click(function () {
            var title = $(this).data("post_title");
            var date  = $(this).data("post_date");
            var content  = $(this).data("post_content");
            var category  = $(this).data("post_category");
            var reward_id = $(this).data("post_id");
            var user_id = $(this).data("post_user_id");
            var is_taken = $(this).data("post_is_taken");
            console.log($(this).data("post_is_taken"));
            console.log(title);
            const remove_div = document.querySelector('#card_content');
            const parent = remove_div.parentElement;
            parent.removeChild(remove_div);

            const card = document.createElement('div');
            card.classList.add('card'); card.classList.add('is-mobile');card.id='card_content';
            parent.appendChild(card);

            const card_header = document.createElement('header');
            card_header.classList.add('card-header');
            card.appendChild(card_header);

            const card_title = document.createElement('p');
            card_title.classList.add('card-header-title');
            card_title.innerText=title;
            card_header.appendChild(card_title);
                                    //  button to accept a reward
            const accept_button=document.createElement('button');card_header.appendChild(accept_button);
            accept_button.classList.add('card-header-icon');
            accept_button.id='accept_reward';
      //       accept_button.addEventListener('click', function() {
      //   alert('Button clicked!');
      // });
            accept_button.setAttribute('data-reward_id',reward_id);
            accept_button.setAttribute('data-is_taken',is_taken);
            accept_button.setAttribute('data-user_id',user_id);
            accept_button.setAttribute('data-header_id',$(this).attr('id'));
            //console.log($(this).attr('id'));
            // console.log(is_taken);
            if(accept_button.getAttribute('data-is_taken')==='True'){                       // if this reward is taken, then show it
                accept_button.style.color='orange';
            }
            accept_button.addEventListener('click',accept_reward);
            const i=document.createElement('i');   accept_button.appendChild(i);
            i.classList.add('fa-square-check');
            i.classList.add('fa-solid');
            i.style.fontSize = '1.5em';


            const accept_word=document.createElement('span');
            accept_button.appendChild(accept_word);

            const card_content = document.createElement('div');
            card_content.classList.add('card-content');
            card.appendChild(card_content);
            const card_content_p= document.createElement('p');
            card_content_p.innerText=content;
            card_content.appendChild(card_content_p);
            const card_content_date= document.createElement('time');
            card_content_date.innerText=date;
            card_content.appendChild(card_content_date);

            const card_footer = document.createElement('div');
            card_footer.classList.add('card-footer');
            card.appendChild(card_footer);



        });
        });
    }
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
                var mycoin_num = $(this).data("coin_num")
                var mywatches = $(this).data("mywatches")
                $.ajax({
                    url: '/show_reward/',
                    method: 'POST',
                    data: {
                        post_id: post_id,
                        title:title,
                        email:email,
                        date:date,
                        content:content,
                        category:category,
                        user_id:user_id,
                        coin_num:mycoin_num,
                        mywatches:mywatches,
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
                        var tag6 = document.getElementById("show_watches");
                         tag6.innerText = res["mywatches"]
                        console.log(res);
                    }
                });
            });
        });
    }

    function accept_reward(){
        const button = this;
         // var button=$(this);
        // console.log("fewwef") ;
        // var button = $(this);
        var reward_id = button.dataset.reward_id;
        var is_taken = button.dataset.is_taken;
        var user_id = button.dataset.user_id;
        if(is_taken==='False'){

            $.ajax({
                url:'/try_accept_reward/',
                method:'POST',
                data:{
                    reward_id:reward_id,
                    user_id:user_id,
                },
                dataType:"JSON",
                success: function (data){
                    if(data.status===1){        //if success accept reward
                        alert("You have accepted this reward!");
                         button.style.color='orange';                       //change color
                         var header_id = button.dataset.header_id;
                        console.log(header_id);
                        const header=document.getElementById(header_id);
                        console.log(header.getAttribute('data-post_is_taken'));
                        header.setAttribute('data-post_is_taken','True');
                        console.log(header.getAttribute('data-post_is_taken'));
                    }
                    else{
                        alert(data.error_msg);
                    }

                }
            });
        }




    }



