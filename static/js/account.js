// script checks the correctness of password entry and its confirmation
$(document).ready(function() {
    $('#change_pass_form').on('submit', function(event) {
        let oldPassword = $('#old_password').val();
        let newPassword = $('#new_password').val();
        let confirmation = $('#new_password_conf').val();

        if (oldPassword.length < 1) {
            displayWarning('Old password can not be empty!');
        } else if (newPassword.length < 1) {
            displayWarning('New password can not be empty!');
        } else if ((new Set(newPassword.split(""))).size < 5) {
            displayWarning('The new password must contain at least 5 different characters!');
        } else if (confirmation.length < 1) {
            displayWarning('New password confirmation can not be empty!');
        } else if (newPassword !== confirmation) {
            displayWarning('The new password and its confirmation are not the same!');
        } else {
            $('#change_pass_form').submit();
        }
        event.preventDefault();
    });
});

// function that displays an error message and hides it after 3 seconds
function displayWarning(message) {
    $('#warning').html('<div class="alert alert-danger" role="alert">' + message + '</div>');
    $('html, body').scrollTop($("#warning").offset().top); //scroll to warning
    $('#warning > div').delay(5000).fadeOut(1000).queue(function() { //need to be added to the queue
        $(this).empty(); //removing the previously added div with the message
    });
}