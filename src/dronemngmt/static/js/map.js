function getCoordinates(search_id)
{
    /*
    Convert the given user input into valid coordinates
    The user input is in the form of a string and can be of 3 kinds,
    Degrees, minutes, and seconds (DMS): 41°24'12.2"N 2°10'26.5"E
    Degrees and decimal minutes (DMM): 41 24.2028, 2 10.4418
    Decimal degrees (DD): 41.40338, 2.17403
    Use the degree symbol instead of "d".
    Use periods as decimals, not commas. Incorrect: 41,40338, 2,17403. Correct: 41.40338, 2.17403. 
    List latitude coordinates before longitude coordinates.
    first number in your latitude coordinate is between -90 and 90.
    first number in your longitude coordinate is between -180 and 180.
    */
    
    /*
    Check if the location coordinates given by user is valid
    */
    let search_coord_input=document.querySelector(search_id);
    let search_input=search_coord_input.value;

    if(search_input===undefined)
    {
        alert("Unable to identify your current location");
        return undefined
    }

    const dms_re= /-?\d+°\d+'[\d\.]+"[NSEW]*/g;
    const ddm_re= /-?\d+°*\s[\d\.]+'*[NSEW]/g;
    const dd_re = /-?[\d\.]+°*[NSEW]*/g;

    const wrong_input_message=`
                Please enter the input in the format of one of 3 kinds,
                Degrees, minutes, and seconds (DMS): 41°24'12.2"N 2°10'26.5"E or
                Degrees and decimal minutes (DMM): 41 24.2028, 2 10.4418 or
                Decimal degrees (DD): 41.40338, 2.17403`;

    let coordinates=[],lat=0.0,lon=0.0

    search_input=search_input.replace(/[,-]/g,'')
    search_input=search_input.replace(/\s\s+/g,' ')
    search_input=search_input.replace(/\s*°\s*/g,`°`)
    search_input=search_input.replace(/\s*'\s*/g,`'`)
    search_input=search_input.replace(/\s*"\s*/g,`"`)
    search_input=search_input.replace(/[A-Za-z]/g,'')

    switch(true)
    {
        case dms_re.test(search_input):
            search_input=search_input.replace(/[\s*°\s*|\s*'\s*|\s*"\s*]/g,` `)
            search_input=search_input.replace(/\s\s+/g,' ')
            coordinates=search_input.split(' ')

            lat=  parseFloat( coordinates[0] ) + 
                ( parseFloat( coordinates[1] ) /60 ) + 
                ( parseFloat( coordinates[2] ) /3600 )

            lon=  parseFloat( coordinates[3]) +
                ( parseFloat( coordinates[4]) /60 ) + 
                ( parseFloat( coordinates[5] ) /3600 )

            lat = parseFloat(lat.toFixed(5))
            lon = parseFloat(lon.toFixed(5))

            break

        case ddm_re.test(search_input):
            search_input=search_input.replace(/[\s*°\s*|\s*'\s*|\s*"\s*]/g,` `)
            search_input=search_input.replace(/\s\s+/g,' ')
            coordinates=search_input.split(' ')
            lat=( parseFloat( coordinates[0] ) + ( parseFloat( coordinates[1] ) / 60) )
            lon=( parseFloat( coordinates[2] ) + ( parseFloat( coordinates[3] ) / 60 ) )
            break

        case dd_re.test(search_input):
            search_input=search_input.replace(/[\s*°\s*|\s*'\s*|\s*"\s*]/g,' ')
            search_input=search_input.replace(/\s\s+/g,' ')
            coordinates=search_input.split(' ')
            lat=parseFloat(coordinates[0])
            lon=parseFloat(coordinates[1])
            break

        default:
            //alert(wrong_input_message);
            //alert("Unable to identify your current location");
            lat=undefined
            lon=undefined
    }

//console.log(lat,lon,coordinates)

let res=[]; 
res.push(lat); res.push(lon); 

if( isNaN(res[0])|| isNaN(res[1]) || res[0]==undefined || res[1]==undefined)
  {
  alert("Unable to identify your current location");
  res[0]=undefined
  res[1]=undefined
  }
else
    {

        if( lat==undefined || lon==undefined)
        {
            //console.log('Location not found')
            return undefined
        }

        else
        {
            return res
        }
    }
    return undefined
  
}

function get_drop_location(coord_id,search_loc_id)
{

    //let marker=undefined,marker_coord=[undefined,undefined];
    
    document.querySelector(search_loc_id).addEventListener('click',function()
        {
                let coord=getCoordinates(coord_id)
                if(coord!=undefined)
                {
                    marker_coord[0]=coord[0]
                    marker_coord[1]=coord[1]
                        // add marker to map
                    //marker=create_draggable_marker(marker_coord[0],marker_coord[1])
                }

        })

}

var key = 'pk.a786af1c5686dfc7212755d279ba275b';

let map_id=document.querySelector('#map');

var container = L.DomUtil.get(map_id);

if(container != null)
{
  container._leaflet_id = null;


  var map = L.map('map');
  
  map.setView([40.7259, -73.9805], 12);


  L.tileLayer(`https://{s}-tiles.locationiq.com/v2/obk/r/{z}/{x}/{y}.png?key=${key}`).addTo(map);

}