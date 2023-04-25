$(document).on('click','[id^="display_thread"]',function(){
   $('[id^="display_thread"]').parent().parent().css('background-color','#ffe699');
   var header=$(this);
   header.parent().parent().css('background-color','#99e6ff');
});