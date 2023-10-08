$(document).ready(function() {
  const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';

  $.getJSON(url, function(data) {
    const movies = data.results;
    for (let movie of movies) {
        $('#list_movies').append('<li>' + movie.title + '</li');
    }
  });
});
