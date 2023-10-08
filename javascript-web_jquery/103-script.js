$(document).ready(function () {
  function fetchTranslation() {
    const langCode = $('#language_code').val();
    const apiUrl = `https://www.fourtonfish.com/hellosalut/?lang=${langCode}`;

    $.get(apiUrl, function (response) {
      $('#hello').text(response.hello);
    });
  }

  $('#btn_translate').click(fetchTranslation);

  $('#language_code').keydown(function (e) {
    if (e.which === 13) {
      fetchTranslation();
    }
  });
});
