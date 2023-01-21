$(document).ready(() => {
    // $('#image').on('click', () => {
    //     $('#upload').attr('disabled', 'disabled');
    //     $('#error').html('');
    //     $('#status').html('Please wait ....')
    //     $('form').submit();

    // });

    $('#image').on('click', () => {
        $('#error').html('');
        $('#status').html('')

    });

    $('#upload-image').on('click', ()=> {
        console.log('test')
        $('#image').click();
    });


    
    $('#select-city').on('change', function() {
       let city_id = $(this).find(':selected').val();

       let districts_list = '';
       Object.keys(districts).forEach((e) => {
        if (districts[e].city_id == city_id) {
            districts_list += `<option value="${districts[e].district_id}">${districts[e].name_en}</option>`;
        }
     });
     $('#select-district').html('');
     $('#select-district').append(districts_list);
    });

    let cities_list = '';
    Object.keys(cities).forEach((e) => {
       cities_list += `<option value="${cities[e].city_id}">${cities[e].name_en}</option>`;
    });

    $('#select-city').append(cities_list);




 


});

show_image = (src) => {
    let actual_image = '/static/images/uploads/' + src;
    let detected_image = '/static/images/detections/' + src;
    $('#actual-image').attr('src', actual_image );
    $('#detected-objects').attr('src', detected_image );
}