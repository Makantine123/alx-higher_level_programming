// adds the class .red to header element when user clicks
// DIV#reed_header
$(document).ready(function() {
	$('#red_header').click(function() {
		$('header').addClass('red');
		});
	});
