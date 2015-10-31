var map;

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
        zoom: 8
    });
}

function initMap() {                    // this gets called by the thingy
   getLocation()
}
