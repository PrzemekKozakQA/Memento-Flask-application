// function that displays an error message and hides it after 5 seconds
export function displayWarning(message) {
    //adding an element with warning text
    $('#warning').html(`<div class="alert alert-danger" role="alert">${message}</div>`);
    //scroll to warning
    $('html, body').scrollTop($("#warning").offset().top);
    // element fading with delay. Important! Next step after fadeOut need to be added to the queue!
    $('#warning > div').delay(3500).fadeOut(1000).queue(function () {
        //removing the previously added div with the message
        $(this).empty();
    });
};