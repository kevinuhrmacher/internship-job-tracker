//expands user bio on profile page
$('.article').readmore({
	maxHeight: 100,
	heightMargin: 16,
	moreLink:'<a class="read-more" href="#">Read More</a>',
	lessLink:'<a class="read-more" href="#">Close</a>',
	afterToggle: function(trigger, element, expanded) {
	if(! expanded) { // The "Close" link was clicked
		$('html, body').animate( { scrollTop: element.offset().top }, {duration: 100 } );
		}
	}
});


//mapbox js

var map = L.mapbox.map('map', 'examples.map-9ijuk24y');

var myLayer = L.mapbox.featureLayer().addTo(map);

var geoJson = [
  {
    "type": "Feature",
    "geometry": {
      "type": "Point",
      "coordinates": [-77.035298,38.904292]
    },
    "properties": {
      "title": "The Washington Post",
      "url": "/city/0",
      "marker-color": "#fc4353",
      "marker-size": "large",
      "marker-symbol": "monument"
    }
  },
  {
    "type": "Feature",
    "geometry": {
      "type": "Point",
      "coordinates": [-76.289879,36.854752]
    },
    "properties": {
      "title": "The Virginian-Pilot",
      "url": "/city/1",
      "marker-color": "#fc4353",
      "marker-size": "large",
      "marker-symbol": "monument"
    }
  },
  {
    "type": "Feature",
    "geometry": {
      "type": "Point",
      "coordinates": [-104.988134,39.740854]
    },
    "properties": {
      "title": "The Denver Post",
      "url": "/city/2",
      "marker-color": "#fc4353",
      "marker-size": "large",
      "marker-symbol": "monument"
    }
  },
  {
    "type": "Feature",
    "geometry": {
      "type": "Point",
      "coordinates": [-78.641462,35.777523]
    },
    "properties": {
      "title": "The News and Observer",
      "url": "/city/3",
      "marker-color": "#fc4353",
      "marker-size": "large",
      "marker-symbol": "monument"
    }
  },
  {
    "type": "Feature",
    "geometry": {
      "type": "Point",
      "coordinates": [-80.344217, 25.806992]
    },
    "properties": {
      "title": "The Miami Herald",
      "url":"/city/4",
      "marker-color": "#fc4353",
      "marker-size": "large",
      "marker-symbol": "monument"
    }
  }
];



myLayer.on('layeradd', function(e) {
    var marker = e.layer,
        feature = marker.feature;

    // Create custom popup content
    var popupContent =  '<a target="_blank" class="popup" href="' + feature.properties.url + '">' +
                        '   <h2>' + feature.properties.title + '</h2>' +
                        '</a>';

    // http://leafletjs.com/reference.html#popup
    marker.bindPopup(popupContent,{
        closeButton: false,
        minWidth: 320
    });
});

myLayer.on('ready', function() {
    // featureLayer.getBounds() returns the corners of the furthest-out markers,
    // and map.fitBounds() makes sure that the map contains these.
    map.fitBounds(featureLayer.getBounds());
});

// Add features to the map
myLayer.setGeoJSON(geoJson);
map.scrollWheelZoom.disable();

map.setView([45.908, -78.525], 4);
//map.scrollWheelZoom.disable();