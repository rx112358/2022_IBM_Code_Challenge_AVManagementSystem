
function get_location_data(location_list)
{
    let locations=[]
    function get_coord(c)
    {   let coords=c.toString().split(',')
        locations.push({'lat':parseFloat(coords[0]),'long':parseFloat(coords[1]) })
    }
    location_list.filter(get_coord)
    return JSON.stringify(locations)
}

/*
Creating a mission object from the values collected from form create-mission
*/

document.querySelector("#create-mission").onclick=function(event) {

    let data = {};

    let field_values={
    'mission_name'     : document.querySelector("#mission-name").value,
    'mission_loc_start': document.querySelector("#mission-loc-start").value,
    'mission_loc_end'  : document.querySelector("#mission-loc-end").value,
    'date'             : document.querySelector("#mission-date").value, 
    'time'             : document.querySelector("#mission-time").value
    }
    
    data={
             mission_name: field_values['mission_name']                     
            ,locations   : get_location_data([field_values['mission_loc_start'],field_values['mission_loc_end']])
            ,date        : field_values['date']            
            ,time        : field_values['time']                
        }

        console.log(data)
        
    let csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value
    var headers = new Headers();
    headers.append('X-CSRFToken', csrftoken);
    
    fetch("/mission/create-mission", {
        method: 'POST',
        body:  JSON.stringify(data),
        headers: headers,
        mode:'same-origin',
        credentials: 'include'
    })
    
    }
