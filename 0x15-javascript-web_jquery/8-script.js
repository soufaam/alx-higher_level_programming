$(document).ready(function () {
  const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
  $.getJSON(url,
    function (data, textStatus, jqXHR) {
      console.log(data.results);
      data.results.forEach(element => {
        const content = '<li>' + element.title + '</li>';
        $('UL#list_movies').append(content);
      });
    // $('UL#list_movies').append(name);
    }
  );
});
