$(document).ready(function() {
  $.ajax({
    url: "https://swapi-api.alx-tools.com/api/films/?format=json",
    method: "GET",
    success: function(data) {
      data.results.forEach(function(film) {
        $("<li>").text(film.title).appendTo("ul#list_movies");
      });
    },
    error: function(xhr, status, error) {
      console.error("Error fetching movie data:", error);
    }
  });
});
