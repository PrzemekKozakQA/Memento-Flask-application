// function that displays an error message and hides it after 3 seconds

export function displayWarning(message) {
    $('#warning').html('<div class="alert alert-danger" role="alert">' + message + '</div>');
    $('html, body').scrollTop($("#warning").offset().top); //scroll to warning
    $('#warning > div').delay(5000).fadeOut(1000).queue(function() { //need to be added to the queue
        $(this).empty(); //removing the previously added div with the message
    });
};