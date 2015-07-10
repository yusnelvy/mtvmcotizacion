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
            $('.row').click(function(){
        // $('nav').toggle();

        if(contador == 0){

            $('.ayuda').animate({
                right: '-100%'
            });
            contador = 1;
        }

    });

};

(function($) {
    var $window = $(window),
        $nav2 = $('nav');

    $window.resize(function resize() {
        if ($window.width() < 976) {
            return $nav.removeClass('navbar-fixed-top');
        }

        $nav.addClass('navbar-fixed-top');
    }).trigger('resize');
})(jQuery);


    $(window).scroll(function()
        {
            if ($(this).scrollTop()) $('nav2').addClass("navbar-fixed-top").fadeIn();
            if ($(this).scrollTop()) $('nav2').removeClass("navbar-fixed-top").fadeOut();
        });
