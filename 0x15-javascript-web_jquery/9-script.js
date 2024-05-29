$(document).ready(function() {
  $.ajax({
    url: "https://fourtonfish.com/hellosalut/?lang=fr",
    method: "GET",
    dataType: "json",
    success: function(data) {
      $("DIV#hello").text(data.hello);
    },
    error: function(xhr, status, error) {
      console.error("Error fetching data:", error);
    }
  });
});
