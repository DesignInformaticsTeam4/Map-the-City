
$(document).ready(function(){/* google maps -----------------------------------------------------*/
    google.maps.event.addDomListener(window, 'load', initialize);

    function highlight_trigger(id) {
        var div = document.getElementById(id);
        div.style.backgroundColor='#EBEBEB';
    }
    alert(location.coords.latitude)
    console.log('here')
    /*
        gives us...
        location.coords.latitude
        location.coords.longitude
        location.coords.accuracy
    */

    function initialize() {                                                       // initialize the map
        var latlng = new google.maps.LatLng(55.953251, -3.188267);                // set map to edinburgh
//        console.log('map initialized to ')
        var mapOptions = {                                                        // setting up the map
            center: latlng,
            scrollWheel: false,
            zoom: 13
        };

    //    var map = new google.maps.Map(document.getElementById('map_canvas'), mapOptions);
    //    var GeoMarker = new GeolocationMarker(map);

        $.getJSON('/json-data/', function(data) {                                           // request the json data from flask app
            var myLatLng = null
            navigator.geolocation.getCurrentPosition(function(position) {
                    myLatLng = (position.coords.latitude, position.coords.longitude )
                };
            });
            var map = new google.maps.Map(document.getElementById("map"), mapOptions);      // map
            var markers = [];

            for (i=0; i < data.length; i++){
                var myLatLng = {lat: data[i].latitude, lng: data[i].longitude};      // add the lat and lang of a json loc

                var marker = new google.maps.Marker({
                    position: myLatLng,
                    map: map,
                    title: data[i].title                                              // get the memory title
                });                                                                   // end making marker

                marker.id = data[i].id
                markers.push(marker);
                marker.setMap(map);
                var id = data[i].id
            }   // end for
        }); // end marker adding
    };  // end ajax
/* end google maps -----------------------------------------------------*/
});