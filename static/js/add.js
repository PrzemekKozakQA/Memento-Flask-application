import {
    displayWarning
} from "./helpers.js";

// script checks whether both inputs have been filled
$(document).ready(function() {
    $('#submitAddBtn').on('click', function(event) {
        let word = $('#word').val().trim();
        let definition = $('#def').val().trim();
        if (word.length < 1) {
            displayWarning('Concept/word can not be empty!');
        } else if (word.length > 100) {
            displayWarning('Maximum Concept/word length is 100 characters!');
        } else if (definition.length < 1) {
            displayWarning('Definition/meaning can not be empty!');
        } else {
            $('#addForm').submit();
        }
        event.preventDefault();
    });
});

// script prevents entering too long text into the input
$(document).ready(function() {
    $('#word').on('change', function(event) {
        let maxlength = $(this).attr("maxlength"); //getting the maximum length from the 'maxlength' attribute of the input
        let text = $(this).val();
        if (text.length >= maxlength) {
            $(this).value = '';
        }
    });
});