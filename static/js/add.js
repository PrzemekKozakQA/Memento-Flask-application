import {
    displayWarning
} from "./helpers.js";

$(document).ready(function() {
    $('#submitAddBtn').on('click', function(event) {
        let word = $('#word').val().trim();
        let definition = $('#def').val().trim();

        if (word.length < 1) {
            displayWarning('Concept/word can not be empty!');
        } else if (word.length > 100) {
            displayWarning('Maximum Concept/word length is 50 characters!');
        } else if (definition.length < 1) {
            displayWarning('Definition/meaning can not be empty!');
        } else {
            $('#add_form').submit();
        }
        event.preventDefault();
    });
});