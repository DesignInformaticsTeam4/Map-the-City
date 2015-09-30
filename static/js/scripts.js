
$(document).ready(function(){/* google maps -----------------------------------------------------*/
google.maps.event.addDomListener(window, 'load', initialize);

function initialize() {                                                       // initialize the map
  var latlng = new google.maps.LatLng(55.953251, -3.188267);                  // set map to edinburgh

  var mapOptions = {
    center: latlng,
    scrollWheel: false,
    zoom: 13
  };

//  var marker = new google.maps.Marker({                                       // add central marker
//    position: latlng,
//    url: '/',
//    animation: google.maps.Animation.DROP
//  });

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

            markers.push(marker);
            markers[i].setMap(map);

            function toggleBounce() {
                alert(marker.title);
            }

            marker.addListener('click', toggleBounce);                          // add animation listener
        }   // end for
    }); // end marker adding
};  // end ajax

/* end google maps -----------------------------------------------------*/
});