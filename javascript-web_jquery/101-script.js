$(document).ready(function() {
  //kuadd kwa list
  $('#add_item').click(function() {
    $('UL.my_list').append('<li>Item</li>');
  });

  //kutoa item ya mwisho
  $('#remove_item').click(function() {
    $('UL.my_list li:last').remove();
  });

  //clear kila kitu
  $('#clear_list').click(function() {
    $('UL.my_list').empty();
  });
});
