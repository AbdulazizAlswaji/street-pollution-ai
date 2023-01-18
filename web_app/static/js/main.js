$(document).ready(() => {
    $('#upload').on('click', () => {
        $('#upload').attr('disabled', 'disabled');
        $('#error').html('');
        $('#status').html('Please wait ....')
        $('form').submit();

    });

    $('#image').on('click', () => {
        $('#error').html('');
        $('#status').html('')

    });
 







});