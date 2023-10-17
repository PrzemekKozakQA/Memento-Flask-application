import {
    displayWarning
} from "./helpers.js";

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