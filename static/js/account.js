import {
    displayWarning
} from "./helpers.js";

// script checks the correctness of data (old password, new and its confirmation) for changing the password
$(document).ready(function() {
    $('#submitChangePassBtn').on('click', function(event) {
        let oldPassword = $('#oldPassword').val();
        let newPassword = $('#newPassword').val();
        let confirmation = $('#newPasswordConf').val();

        if (oldPassword.length < 1) {
            displayWarning('Old password can not be empty!');
        } else if (newPassword.length < 1) {
            displayWarning('New password can not be empty!');
        //checking whether the new password has at least 5 unique characters
        } else if ((new Set(newPassword.split(""))).size < 5) {
            displayWarning('The new password must contain at least 5 different characters!');
        } else if (confirmation.length < 1) {
            displayWarning('New password confirmation can not be empty!');
        } else if (newPassword !== confirmation) {
            displayWarning('The new password and its confirmation are not the same!');
        } else {
            $('#changePassForm').submit();
        }
        event.preventDefault();
    });
});

// script displaying input and a button to delete a user account
$(document).ready(function() {
    $('#delUserBtn').on('click', function(event) {
        $('#confirmationDiv').removeClass('d-none');
    });
});

// script checks whether the entered username matches the name in the account header,
// if so it activates the button that deletes the account
$(document).ready(function() {
    $('#userConfirm').on('input', function(event) {
        let username = $('#userNameHeader').text();
        if ($(this).val() == username) {
            //removing an attribute from button to activate it
            $('#submitDelUserBtn').removeAttr("disabled");
        } else {
            //adding back an attribute from the button if only the beginning of the username matches
            $('#submitDelUserBtn').attr("disabled", "disabled");
        }
    });
});
