$(document).ready(() => {
    // $('#image').on('click', () => {
    //     $('#upload').attr('disabled', 'disabled');
    //     $('#error').html('');
    //     $('#status').html('Please wait ....')
    //     $('form').submit();

    // });

$.ajax({
    type: 'GET',
            url: '/get_cities',  
            async: true,
            success: (data) => {
                var list_cities = '<option></option>';
                Object.keys(data.cities).forEach((e)=> {

                    list_cities += `<option value="${data.cities[e]}"> ${cities[data.cities[e] - 1].name_en}</option>`;
                });

                $('#av-city').append(list_cities)
            }
});


$('#av-city').on('change', function() {
    $('#av-district').html('');
    let city_id = $(this).find(':selected').val();

    $.ajax({
        type: 'GET',
                url: '/get_districts',  
                async: true,
                data: {'_id': city_id},
                success: (data) => {
                    var list_districts = '';
                    Object.keys(data.districts).forEach((e)=> {
                        Object.keys(districts).forEach((k) => {
                            if (districts[k].district_id == data.districts[e]) {
                                 dis = districts[k].name_en;
                                 list_districts += `<option value="${data.districts[e]}"> ${dis}</option>`;
                            }
                        })
    
                        
                    });
    
                    $('#av-district').html('');
  $('#av-district').append(list_districts);
                }
    });

   
  
 });


 $('#av-district').on('change', function()  {


    let g = Math.random().toFixed(2) ;
    $('#g_act').html( g * 100 + '%')
    g_t=(((0.35 - g ) / (0.35 - 0.1)) * 0.2).toFixed(2)
    $('#g_score').html(  g_t  + '%');

    let s = Math.random().toFixed(2) ;
    $('#s_act').html( s * 100 + '%')
    //((target - act ) / (target - amb)) * w
    s_t = (((0.25 - s ) / (0.25 - 0.1)) * 0.3).toFixed(2)
    $('#s_score').html(   s_t + '%');


    let p = Math.random().toFixed(2) ;
    $('#p_act').html( p * 100 )
    //((target - act ) / (target - amb)) * w
    p_t=(((7 - p ) / (7 - 2)) * 0.30).toFixed(2)
    $('#p_score').html( p_t   + '%');


    let e = Math.random().toFixed(2) ;
    $('#e_act').html( e * 100 )
    //((target - act ) / (target - amb)) * w
    e_t=(((50 - e ) / (50 - 250)) * .10).toFixed(2)
    $('#e_score').html( e_t   + '%');

    let c = Math.random().toFixed(2) ;
    $('#c_act').html( c * 100 )
    //((target - act ) / (target - amb)) * w
    c_t = (((15 - c ) / (15 - 20)) * .10).toFixed(2)
    $('#c_score').html(   c_t + '%');

    
score = ((parseFloat(g_t)+parseFloat(s_t)+parseFloat(p_t)+parseFloat(e_t)+parseFloat(c_t)) ).toFixed(2) 
$('#score').html(score + '%')
    

 })






    particlesJS.load('particles-js', '../static/js/effects.json');
    particlesJS.load('particles-js', '../../static/js/effects.json');



    $('.resolved').on('click', function() {
        var _id = this.value;
        if ($(this).is(':checked')) {
            var checked = 'resolved';
        } else {
            var checked = '';
        }

        $.ajax({
            type: 'GET',
            url: '/resolve_issue',            
            async: true,
            data: {
                _id: _id , resolved: checked
            },
            success: (data) => {
               alert('Status updated');
               location.reload();
            }
        })
    })



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