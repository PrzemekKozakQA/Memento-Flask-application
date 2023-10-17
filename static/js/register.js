import {
    displayWarning
} from "./helpers.js";

//the script checks whether it is possible to register a user with the name given in the form
$(document).ready(function() {
    $('#check_user_button').on('click', function(event) {
        //I'm getting the username without spaces at the beginning and end
        let user = $('#username-input').val().trim();
        //I check if the name is empty
        if (user.length < 1) {
            displayWarning('Username can not be empty!')
        } else {
            //sending a POST request in JSON format with username to the backend
            $.ajax({
                    data: {
                        username: user,
                        check: 'username'
                    },
                    type: 'POST',
                    url: '/register'
                })
                .done(function(response) { //receiving responses from the backend
                    //if the username can be registered, fields for creating a password are shown
                    if (response.username_status == 'ok') {
                        $('#username-input').prop("readonly", true).addClass('read_only_style'); //preventing editing of username and addin style
                        $('#warning').empty(); //hiding messages
                        $('#check_user_button').addClass('d-none'); //Hiding the button to check username
                        $('#password_div').removeClass('d-none'); //showing inputs  for password and id confirmation
                    } else {
                        displayWarning(response.message);
                    }
                });
        }
        event.preventDefault();
    });
});

// script checks the correctness of password entry and its confirmation
$(document).ready(function() {
    $('form').on('submit', function(event) {
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
            $('form').submit();
        }
        event.preventDefault();
    });
});