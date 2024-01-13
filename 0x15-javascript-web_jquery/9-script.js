$(document).ready(function () {
  const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
  $.getJSON(url,
    function (data, textStatus, jqXHR) {
      console.log(data);
      const content = data.hello;
      $('DIV#hello').text(content);
      // $('UL#list_movies').append(name);
    }
  );
});
