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
                    username: user,
                    check: 'username'
                },
                type: 'POST',
                url: '/register'
            })
                .done(function(response) { // receiving responses from the backend
                    // if the username can be registered, fields for creating a password are shown
                    if (response.username_status == 'ok') {
                        $('#usernameInput').prop("readonly", true).addClass('read-only-style'); // preventing editing of username and addin style
                        $('#warning').empty(); // hiding warnings if they were previously displayed
                        $('#checkUserButton').addClass('d-none'); // hiding button for check username
                        $('#passwordDiv').removeClass('d-none'); //showing inputs for password and it confirmation
                    } else {
                        displayWarning(response.message);
                    }
                });
        }
    });
});

// script checks the correctness of password entry and its confirmation
$(document).ready(function() {
    $('#submitRegistrationBtn').on('click', function(event) {
        console.log("test");
        let password = $('#password').val();
        let confirmation = $('#confirmation').val();
        if (password.length < 1) {
            displayWarning('Password can not be empty!');
        } else if ((new Set(password.split(""))).size < 5) {
            displayWarning('The password must contain at least 5 different characters!');
        } else if (confirmation.length < 1) {
            displayWarning('Password confirmation can not be empty!');
        } else if (password !== confirmation) {
            displayWarning('The password and its confirmation are not the same!');
        } else {
            $('#registration').submit();
        }
        event.preventDefault();
    });
});