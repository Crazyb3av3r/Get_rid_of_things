var elementPosition = $('.scroll-head').offset();

$(window).scroll(function(){
        if($(window).scrollTop() > elementPosition.top){
              $('.scroll-head').css('position','fixed').css('top','0');
        } else {
            $('.scroll-head').css('position','static');
        }
});