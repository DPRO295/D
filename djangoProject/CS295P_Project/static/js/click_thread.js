// $(document).ready(function(){
$(document).on('click','[id^="display_thread"]',function(){
   $('[id^="display_thread"]').parent().parent().css('background-color','white');
   var header=$(this);
   header.parent().parent().css('background-color','#99e6ff');
});

// });