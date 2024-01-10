

// Preloader
$.holdReady( true );

$('body').imagesLoaded({ background: ".background-holder" }, function(){
    $('#preloader').removeClass("loading");
    $.holdReady( false );
    setTimeout(function() {
        $('#preloader').remove();
    }, 800);
});

(function ($) {
	"use strict";
    $(document).ready(function() {
        var currentURL = window.location.href;
        var newURL = currentURL.replace(/\/(en|de)\//, '/de/');
        $('#switch-language').attr('href', newURL);
        
        $('.de').on('click', function(event) {
            event.preventDefault();  // Prevent the default link behavior
            var currentURL = window.location.href;
            var newURL = currentURL.replace(/\/(en|de)\//, '/de/');
            window.location.href = newURL;
        });

		$('.en').on('click', function(event) {
            event.preventDefault();  // Prevent the default link behavior
            var currentURL = window.location.href;
            var newURL = currentURL.replace(/\/(en|de)\//, '/en/');
            window.location.href = newURL;
        });
    });
})(jQuery);

console.log('Coded by: https://FarzinShams.com');