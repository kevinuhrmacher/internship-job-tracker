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

<<<<<<< HEAD
$('.description').readmore({
	maxHeight: 40,
	heightMargin: 16,
	moreLink:'<a class="read-more link-font float-right" href="#">Read More</a>',
	lessLink:'<a class="read-more link-font float-right" href="#">Close</a>',
	afterToggle: function(trigger, element, expanded) {
	if(! expanded) { // The "Close" link was clicked
		$('html, body').animate( { scrollTop: element.offset().top }, {duration: 100 } );
		}
	}
});
=======

//mapbox js


>>>>>>> f76015c9c6dbf250cf452316df5cf2b0a937d1af
