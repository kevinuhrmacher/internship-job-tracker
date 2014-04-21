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
var map = L.mapbox.map('map', 'examples.map-9ijuk24y').setView([40, -74.50], 9)
	.featureLayer.setGeoJSON(geojson);

map.scrollWheelZoom.disable();