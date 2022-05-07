
function get_location_data(location_list)
{
    locations=[]
    function get_coord(c)
    {   coords=c.split(',')
        locations.push({'lat':parseFloat(coords[0]),'long':parseFloat(coords[1]) })
    }
    location_list.filter(get_coord)
    return JSON.stringify(locations)
}


document.querySelector("#create-mission").addEventListener('click', function(event) {

    let data = {},valid_fields=true;

    let field_values={
    'mission_name'     : document.querySelector("#mission-name"),
    'mission_loc_start': document.querySelector("#mission-loc-start"),
    'mission_loc_end'  : document.querySelector("#mission-loc-end"),
    'date'             : document.querySelector("#mission-date"),
    'time'             : document.querySelector("#mission-time")
    }

    if(valid_fields==true)
    {               
        data={
             mission_name: field_values['mission_name']                     
            ,locations   : get_location_data([field_values['mission_loc_start'],field_values['mission_loc_end']])
            ,date        : field_values['date']            
            ,time        : field_values['time']                
        }
    }
        // sending mission data
        $.ajax({
        type:   "POST", // GET or POST
        url:    "/mission/create-mission",
        data:  data, // get the form data
        
        // on success
        success: 
            function (response) {
                
                let mission_id=response['mission_d'];

                showAlert('<p>Your mission has been set’</p>')
                console.log(" Form data submitted ",mission_id);
            },
        // on error
        error: function (response) {
            //console.log(response.errors) 
        }
        });// end of ajax call
    
    })