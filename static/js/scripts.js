
$(document).ready(function(){/* google maps -----------------------------------------------------*/
google.maps.event.addDomListener(window, 'load', initialize);

function initialize() {

  /* position Amsterdam */
  var latlng = new google.maps.LatLng(55.953251, -3.188267);

  var mapOptions = {
    center: latlng,
    scrollWheel: false,
    zoom: 13
  };

  var marker = new google.maps.Marker({
    position: latlng,
    url: '/',
    animation: google.maps.Animation.DROP
  });

  var map = new google.maps.Map(document.getElementById("map"), mapOptions);
  marker.setMap(map);
  //
  $.getJSON('/json-data/', function(data) {
//        marker = new google.maps.Marker({
//          position: new google.maps.LatLng(data[i].latitude, data[i].longitude),
//          map: map
//        });
        for (i=0; i < data.length; i++){
          $("#result").text(data[i].title);
        }
      });
};
/* end google maps -----------------------------------------------------*/
});