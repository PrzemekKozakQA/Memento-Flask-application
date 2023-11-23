import {
    displayWarning
} from "./helpers.js";

// script checks whether both inputs have been filled correctly
$(document).ready(function() {
    $('#submitBtn').on('click', function(event) {
        let word = $('#word').val().trim();
        let definition = $('#def').val().trim();
        //getting the maximum length from the 'maxlength' attribute of the input
        let maxlength = $('#word').attr("maxlength");
        if (word.length < 1) {
            displayWarning('Word/concept can not be empty!');
        } else if (word.length > maxlength) {
            displayWarning(`Maximum word/concept length is ${maxlength} characters!`);
        } else if (definition.length < 1) {
            displayWarning('Definition/meaning can not be empty!');
        } else {
            $('form').submit();
        }
        event.preventDefault();
    });
});

// script prevents entering too long text into the input
$(document).ready(function() {
    $('#word').on('change', function(event) {
        //getting the maximum length from the 'maxlength' attribute of the input
        let maxlength = $(this).attr("maxlength");
        let text = $(this).val();
        if (text.length >= maxlength) {
            $(this).value = '';
        }
    });
});
