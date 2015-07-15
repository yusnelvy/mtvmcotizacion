$(document).ready(main);

var contador = 1;

function main(){
    $('.ayuda_btn').click(function(){
        // $('nav').toggle();

        if(contador == 1){
            $('.ayuda').animate({
                right: '1%'
            });
            contador = 0;
        } else {
            contador = 1;
            $('.ayuda').animate({
                right: '-100%'
            });
        }

    });
            $('#page-wrap').click(function(){
        // $('nav').toggle();

        if(contador == 0){

            $('.ayuda').animate({
                right: '-100%'
            });
            contador = 1;
        }

    });
          $('#footer').click(function(){
        // $('nav').toggle();

        if(contador == 0){

            $('.ayuda').animate({
                right: '-100%'
            });
            contador = 1;
        }

    });

};

    $(window).scroll(function()
        {
            if ($(this).scrollTop()) $('nav2').addClass("navbar-fixed-top").fadeIn();
            if ($(this).scrollTop()) $('nav2').removeClass("navbar-fixed-top").fadeOut();
        });
