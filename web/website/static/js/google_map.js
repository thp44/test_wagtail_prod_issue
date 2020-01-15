var map;
var marker;

function placeMarker(location) {

    window.position = {
        lat: map.getCenter().lat().toFixed(6),
        lon: map.getCenter().lng().toFixed(6)
    }
  if (marker) {
    //if marker already was created change positon
    marker.setPosition(location);
    map.setCenter(location);
  } else {
    //create a marker
    marker = new google.maps.Marker({
      position: location,
      map: map,
      draggable: true,
      title: "Building"
    });
    map.setCenter(location);
    map.setZoom(11);
  }
}

function geocodeAddress(geocoder, resultsMap) {
  var address = document.getElementById("address").value;
  geocoder.geocode({ address: address }, function(results, status) {
    if (status === "OK") {
      resultsMap.setCenter(results[0].geometry.location);
      placeMarker(results[0].geometry.location);
    } else {
      alert("Geocode was not successful for the following reason: " + status);
    }
  });
}

function initialize() {
  var centerPosition = new google.maps.LatLng(54.526, 15.2551);
  var options = {
    zoom: 3,
    center: centerPosition,
    mapTypeId: google.maps.MapTypeId.ROADMAP
  };
  map = new google.maps.Map($("#map")[0], options);
  var geocoder = new google.maps.Geocoder();

  google.maps.event.addListener(map, "click", function(evt) {
    placeMarker(evt.latLng);
  });

  // intercept map and marker movements
  google.maps.event.addListener(map, "click", function() {
    marker.setPosition(map.getCenter());

    window.position = {
        lat: map.getCenter().lat().toFixed(6),
        lon: map.getCenter().lng().toFixed(6)
    }
  });

  document.getElementById("submit").addEventListener("click", function(evt) {
    geocodeAddress(geocoder, map);
  });
}
google.maps.event.addDomListener(window, "load", initialize);
© 2019 GitHub, Inc.




