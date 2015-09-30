
$(document).ready(function(){/* google maps -----------------------------------------------------*/
google.maps.event.addDomListener(window, 'load', initialize);


function toggleBounce(marker) {
    alert('hunch hunch');
    alert(marker.title);
}

function initialize() {                                                       // initialize the map
  var latlng = new google.maps.LatLng(55.953251, -3.188267);                  // set map to edinburgh

  var mapOptions = {
    center: latlng,
    scrollWheel: false,
    zoom: 13
  };

  $.getJSON('/json-data/', function(data) {                                      // request the json data from flask app
        var map = new google.maps.Map(document.getElementById("map"), mapOptions);     // map
        var markers = [];

        for (i=0; i < data.length; i++){
            var myLatLng = {lat: data[i].latitude, lng: data[i].longitude};      // add the lat and lang of a json loc

            var marker = new google.maps.Marker({
                position: myLatLng,
                map: map,
                title: data[i].title                                              // get the memory title
            });                                                                   // end making marker
            marker.name = data[i].title
            markers.push(marker);
            marker.setMap(map);

            marker.addListener('click', function(marker) {
                alert('yup');
                var div = document.getElementById('638');
                div.style.backgroundColor='#EBEBEB';
//                map.setZoom(8);
//                map.setCenter(marker.getPosition());
            });


//            markers[i].addListener('click', toggleBounce(markers[i]) {
//
//
//            });                          // add animation listener
        }   // end for
    }); // end marker adding
};  // end ajax

/* end google maps -----------------------------------------------------*/
});