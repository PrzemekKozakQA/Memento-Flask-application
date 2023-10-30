// function that displays an error message and hides it after 5 seconds

export function displayWarning(message) {
    $('#warning').html('<div class="alert alert-danger" role="alert">' + message + '</div>'); //adding an element with warning text
    $('html, body').scrollTop($("#warning").offset().top); //scroll to warning
    // element fading with delay
    $('#warning > div').delay(5000).fadeOut(1000).queue(function() { //next step need to be added to the queue
        $(this).empty(); //removing the previously added div with the message
    });
};