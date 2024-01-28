import {
    displayWarning
} from "./helpers.js";

// script checks whether both inputs have been filled correctly
$(document).ready(function () {
    $('#submitBtn').on('click', function (event) {
        let word = $('#word').val().trim();
        let definition = $('#def').val().trim();
        //getting the maximum length from the 'maxLength' attribute of the input
        let maxLength = $('#word').attr("maxlength");
        if (word.length < 1) {
            displayWarning('Word/concept can not be empty!');
        } else if (word.length > maxLength) {
            displayWarning(`Maximum word/concept length is ${maxLength} characters!`);
        } else if (definition.length < 1) {
            displayWarning('Definition/meaning can not be empty!');
        } else {
            $('form').submit();
        }
        event.preventDefault();
    });
});

// script prevents entering too long text into the input
$(document).ready(function () {
    $('#word').on('change', function (event) {
        //getting the maximum length from the 'maxLength' attribute of the input
        let maxLength = $(this).attr("maxlength");
        let text = $(this).val();
        if (text.length >= maxLength) {
            $(this).value = '';
        }
    });
});