$(document).ready(function () {
  $('DIV#add_item').on('click', function () {
    const content = '<li>Item</li>';
    $('UL.my_list').append(content);
  });
  $('DIV#remove_item').on('click', function () {
    $('UL.my_list li:last').remove();
  });
  $('DIV#clear_list').on('click', function () {
    $('UL.my_list li').remove();
  });
});
