$(document).ready(function () {
  $('DIV#add_item').on('click', function () {
    const content = '<li>Item</li>';
    $('UL.my_list').append(content);
  });
});
