

// Preloader
$.holdReady( true );

$('body').imagesLoaded({ background: ".background-holder" }, function(){
    $('#preloader').removeClass("loading");
    $.holdReady( false );
    setTimeout(function() {
        $('#preloader').remove();
    }, 800);
});

// Zanimation
$(window).on('load', function(){
    $('*[data-inertia]').each(function(){
        $(this).inertia();
    });

});