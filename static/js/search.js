import {
    displayWarning
} from "./helpers.js";

// script dynamically displays search results
$(document).ready(function() {
    $('#search').on('input', async function(event) {
        let text = $('#search').val().trim();
        let response = await fetch('/words?q=' + text); //sending the query via fetch and saving the response
        let data = await response.json();
        // displaying a message if nothing was found
        if (data.length == 0) {
            $('#results').html('<tr><td colspan="5"> <h5>No results...</h5> </td></tr>')
        } else {
            let list_of_result = ''
            for (let i = 0; i < data.length; i++) {
                //adding to the results list:  row ordinal number, data, and buttons to edit and delete items
                list_of_result += `<tr>
                                        <th scope="row">${(i + 1)}</th>
                                        <td>${data[i].word}</td>
                                        <td>${data[i].definition}</td>
                                        <td><a class="btn btn-info btn-sm" role="button" href="/words/${data[i].id}">Edit</a></td>
                                        <td><button class="btn btn-secondary btn-sm" type="button" id=${data[i].id}>Delete</button></td>
                                  </tr>`;
            }
            $('#results').html(list_of_result);
        }
    });
});

// script that deletes a word/definition from the database
$(document).ready(function() {
    // button selector added as an additional parameter in on() - needed because data is added dynamically during the search
    $('#results').on('click', '.btn.btn-secondary.btn-sm', function(event) {
        let id = $(this).attr('id');
        //sending a deletion request
        $.ajax({
            type: 'delete',
            url: '/words/' + id,
            async: false
            //in AJAX requests, reading the code status from response is only possible with the third parameter
        }).always(function(response, textStatus, jqXHR) {
            if (jqXHR.status != 200) {
                displayWarning('Deletion failed!');
            } else {
                $('#search').trigger('input'); //if the item was successfully removed, the search list is refreshed
            }
        });
    });
});