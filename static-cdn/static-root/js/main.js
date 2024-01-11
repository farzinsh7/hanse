

// Preloader
$.holdReady(true);

$('body').imagesLoaded({ background: ".background-holder" }, function () {
    $('#preloader').removeClass("loading");
    $.holdReady(false);
    setTimeout(function () {
        $('#preloader').remove();
    }, 800);
});

(function ($) {
    "use strict";
    $(document).ready(function () {
        var currentURL = window.location.href;
        var newURL = currentURL.replace(/\/(en|de)\//, '/de/');
        $('#switch-language').attr('href', newURL);

        $('.de').on('click', function (event) {
            event.preventDefault();  // Prevent the default link behavior
            var currentURL = window.location.href;
            var newURL = currentURL.replace(/\/(en|de)\//, '/de/');
            window.location.href = newURL;
        });

        $('.en').on('click', function (event) {
            event.preventDefault();  // Prevent the default link behavior
            var currentURL = window.location.href;
            var newURL = currentURL.replace(/\/(en|de)\//, '/en/');
            window.location.href = newURL;
        });
    });
})(jQuery);

(function ($) {
    "use strict";
    $(document).on('submit', '#post-form', function (e) {
        e.preventDefault();

        var form = $(this);

        $.ajax({
            type: 'POST',
            url: '/en/create',
            data: {
                email: $('#email').val(),
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            },
            success: function (data) {
                // Display the success message
                $('#thanks').html('Thank You!')
                $('#success-message').html(data);

                // Hide the form
                form.hide();
                $('#title-1, #title-2').hide();
            }
        });
    });
})(jQuery);

console.log('Coded by: https://FarzinShams.com');