// Javascript updates the text colr of header element to red
// when the user clicks the tag DIV#read_heade

$(document).ready(function() {
  $('#red_header').click(function() {
    $('header').css('color', '#FF0000');
  });
});
