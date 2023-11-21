import {
    displayWarning
} from "./helpers.js";

// script verifies username and password during registration
$(document).ready(function() {
    $('#checkUserButton').on('click', function(event) {
        let user = $('#usernameInput').val().trim();
        if (user.length < 1) {
            displayWarning('Username can not be empty!')
        } else {
            //sending a POST request using AJAX in JSON format with username to the backend
            $.ajax({
                    data: {
                        ajaxCheckUsername: true,
                        username: user
                    },
                    type: 'POST',
                    url: '/register'
                })
                // receiving responses from the backend
                .done(function(response) {
                    // if the username can be registered, fields for creating a password are shown
                    // preventing editing of username and addin style
                    $('#usernameInput').prop("readonly", true).addClass('read-only-style');
                    // hiding warnings if they were previously displayed
                    $('#warning').empty();
                    // hiding button for check username
                    $('#checkUserButton').addClass('d-none');
                    //showing inputs for password and it confirmation
                    $('#passwordDiv').removeClass('d-none');
                })
                .fail(function(jqXHR) {
                    displayWarning(jqXHR.responseJSON.message);
                });
        }
    });
});

// script checks the correctness of password entry and its confirmation
$(document).ready(function() {
    $('#submitRegistrationBtn').on('click', function(event) {
        let password = $('#password').val();
        let confirmation = $('#confirmation').val();
        if (password.length < 1) {
            displayWarning('Password can not be empty!');
            //checking whether the password and its confirmation have at least 5 different characters
        } else if ((new Set(password.split(""))).size < 5) {
            displayWarning('The password must contain at least 5 different characters!');
        } else if (confirmation.length < 1) {
            displayWarning('Password confirmation can not be empty!');
        } else if (password !== confirmation) {
            displayWarning('The password and its confirmation are not the same!');
        } else {
            $('#registration').submit();
        }
        //preventing the button from working by default so that the script doesn't get into a loop
        event.preventDefault();
    });
});
