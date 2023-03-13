$(document).ready(function(){
    function start_tip(button){
         var tipboard=$('#tipboard')
       var html=`
            <input type="number" id="tip_quantity" min="0" step="any" style="width: 30%">
            <button id="tip_ok">OK</button>       
`;
        tipboard.html(html);
    }
    function end_tip(button){
        $('#tip_quantity').remove()
        $('#tip_ok').remove()
    }

   $(document).on('click','button[id="tip"]',function(){
       var button=$(this)
      // var thread_id=button.attr('data-thread_id')
        var ok=$('#tip_ok')
       if(ok.length===0)
           start_tip(button);
       else
           end_tip(button);

   });
    $(document).on('click','button[id="tip_ok"]',function(){
        var tip_quantity=$('#tip_quantity').val()
        var thread_id=$('#tip').attr('data-thread_id')
        var user_id=$('#parent').attr('data-user_id')
        $.ajax({
            url: '/tip_thread/',
            method: 'POST',
            data:{
                tip_quantity:tip_quantity,
                thread_id:thread_id,
                user_id:user_id
            },
            success(data){
                $('#tip_num').text(data.tip_num)
                $('#tip_quantity').remove()
                $('#tip_ok').remove()
            }

        })
    });

});