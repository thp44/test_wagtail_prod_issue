//sidebar

/*
$(window).scroll(function() {
    var currentScroll = $(window).scrollTop();
    /*var headerHeight = $('.header').height()
    if (currentScroll >= headerHeight) {
        $('.fixme').css({
            position: 'fixed',
            top: '5em',
        });
    } else {
        $('.fixme').css({
            position: 'static',
            top: '5em',
        });
    }
});*/

//change active state in menu
$(window).scroll(function() {
    var scrollDistance = $(window).scrollTop();
    var headerHeight = $('.header').height()
    var scrollPadding = 40
$('.page-section').each(function(i) {
    if ($(this).position().top <= scrollDistance + scrollPadding) {
        $('.nav a.active').removeClass('active');
        $('.nav a').eq(i).addClass('active');
    }
});
}).scroll();


//move side menu
$(function() {
    var offset = $("#sidebar").offset();
    var topPadding = 40;
    $(window).scroll(function() {
        if (offset && $(window).scrollTop() > offset.top) {
            $("#sidebar").stop().animate({
                marginTop: $(window).scrollTop() + topPadding
            });
        } else {
            $("#sidebar").stop().animate({
                marginTop: 0
            });
        };
    });
});
