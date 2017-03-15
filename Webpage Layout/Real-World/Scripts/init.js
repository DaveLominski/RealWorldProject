$(document).ready(function(){
    // Initial boot scripts to set-up sites functionality.
    $('body').scrollspy({
        target: ".navigation",
        offset: 30
    }); 
    
    $('.carousel').carousel({
        interval: 3000
    });
});

// Animated Scroll
$(".mainNav").find("a").click(function(e) {
    e.preventDefault();
    var section = $(this).attr("href");
    $("html, body").animate({
        scrollTop: ($(section).offset().top - 20),
    }, 700);
});

// Animated Scroll
$(".mobileNav").find("a").click(function(e) {
    e.preventDefault();
    var section = $(this).attr("href");
    $("html, body").animate({
        scrollTop: ($(section).offset().top - 60),
    }, 700);
});