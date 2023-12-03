import {
    displayWarning
} from "./helpers.js";

$(document).ready(function () {
    $('#nextBtn').on('click', function (event) {
        if ($('#isWordMemorizedBox').is(':checked')) {
            $.ajax({
                    data: {
                        wordId: $('#wordHeader').attr('wordId'),
                    },
                    type: 'POST',
                    url: '/memorize',
                    async: false
                }).done(function () {
                    window.location.reload();
                })
                .fail(function () {
                    displayWarning('Marking as remembered failed! Please try again or uncheck and click Next.');
                });
        } else {
            window.location.reload();
        }

    });
});