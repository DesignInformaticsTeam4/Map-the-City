var map;
var geo_marker;
var markers = [];

function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(makeMap);
    } else {
        x.innerHTML = "Geolocation is not supported by this browser.";
    }
}

function makeMap(position){
    map = new google.maps.Map(document.getElementById('map'), {
        center: {lat: position.coords.latitude, lng: position.coords.longitude},
        zoom: 15
    });
    geo_marker = new GeolocationMarker(map);

    add_point();
}

function initMap() {                    // this gets called by the thingy
   getLocation()
}

function add_point(){
    $.getJSON('/json-data/', function(data) {                                             // request the json data from flask app
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
        } // end for
    }); // end marker adding ajax
}

