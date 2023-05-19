var marker = new google.maps.Marker({
  position: {lat: 40.7128, lng: -74.0060},
  map: map,
  icon: '/static/img/marker.png'
});

var places = [];

function initMap() {
  var lat = 40.7128;
  var lng = -74.0060;
  var map = new google.maps.Map(document.getElementById('map'), {
    mapTypeId: 'hybrid',
    center: {lat: lat, lng: lng},
    zoom: 12
  });


  google.maps.event.addListener(map, 'click', function(event) {
    placeMarker(event.latLng, map);
  });


  var infowindow = new google.maps.InfoWindow({
    content: 'Buradasınız!'
  });


  function placeMarker(location, map) {

    if (marker) {
      marker.setMap(null);
    }


    marker = new google.maps.Marker({
      position: location,
      map: map,
      icon: new google.maps.MarkerImage("/static/img/travel.png", null, null, null, new google.maps.Size(50, 50)) // Statik dosya yolunu doğrudan belirtin
    });

    var latitude = location.lat();
    var longitude = location.lng();
    document.getElementById("latitudeInput").value = latitude;
    document.getElementById("longitudeInput").value = longitude;


    infowindow.setContent('Destination');
    infowindow.open(map, marker);


    google.maps.event.addListener(marker, 'position_changed', function() {
      infowindow.setContent('Destination');
    });
  }
}