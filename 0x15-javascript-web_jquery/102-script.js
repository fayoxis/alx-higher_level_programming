$(document).ready(function() {
  const url = 'https://hellosalut.stefanbohacek.dev/?';

  $('input#btn_translate').click(function() {
    const languageCode = $('input#language_code').val();
    $.get(url + $.param({ lang: languageCode }), function(data) {
      $('div#hello').html(data.hello);
    });
  });
});
