$(document).ready(function() {
  $('input#btn_translate').click(function() {
    $('div#hello').empty();
    const languageCode = $('input#language_code').val();
    $.ajax({
      type: 'GET',
      url: 'https://fourtonfish.com/hellosalut/?lang=' + languageCode,
      success: function(response) {
        $('div#hello').append(response.hello);
      }
    });
  });
});
