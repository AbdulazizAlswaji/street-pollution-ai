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

show_image = (src) => {
    let actual_image = '/static/images/uploads/' + src;
    let detected_image = '/static/images/detections/' + src;
    $('#actual-image').attr('src', actual_image );
    $('#detected-objects').attr('src', detected_image );
}