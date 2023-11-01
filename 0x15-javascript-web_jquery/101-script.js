$(document).ready(function () {
  let counter = 1;

  $('#add_item').click(function () {
    const newItem = $('<li>Item ' + counter + '</li>');
    $('ul.my_list').append(newItem);
    counter++;
  });

  $('#remove_item').click(function () {
    $('ul.my_list li:last-child').remove();
  });

  $('#clear_list').click(function () {
    $('ul.my_list').empty();
  });
});
