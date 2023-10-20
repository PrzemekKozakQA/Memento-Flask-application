import {
    displayWarning
} from "./helpers.js";

$(document).ready(function() {
    $('#search').on('input', async function(event) {
        let text = $('#search').val().trim();
        let response = await fetch('/words?q=' + text, {
            method: "get"
        });
        let rows = await response.json();
        if (rows.length == 0) {
            $('#results').html('<tr><td colspan="4"> <h5>No results...</h5> </td></tr>')
        } else {
            let list_of_result = ''
            for (let i = 0; i < rows.length; i++) {
                list_of_result += `<tr>
                                        <th scope="row">${(i + 1)}</th>
                                        <td>${rows[i].word}</td>
                                        <td>${rows[i].definition}</td>
                                        <td><a class="btn btn-info btn-sm" role="button" href="/words/${rows[i].id}">Edit</a></td>
                                        <td><input class="btn btn-secondary btn-sm" type="button" value="Delete" id=${rows[i].id}></td>
                                  </tr>`
            }
            $('#results').html(list_of_result);
        }
    });
});

$(document).ready(function() {
    $('#results').on('click', '.btn.btn-secondary.btn-sm', function(event) {
        let id = $(this).attr('id');
        $.ajax({
            type: 'delete',
            url: '/words/' + id,
            async: false
        }).always(function(response, textStatus, jqXHR) {
            if (jqXHR.status != 200) {
                displayWarning('Deletion failed!');
            } else {
                $('#search').trigger('input');
            }
        });
    });
});