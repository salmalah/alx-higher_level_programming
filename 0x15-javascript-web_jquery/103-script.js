$(document).ready(function () {
  function fetchTranslation () {
    const languageCode = $('#language_code').val();
    const apiUrl = 'https://hellosalut.stefanbohacek.dev/?lang=' + languageCode;

    $.get(apiUrl, function (data) {
      $('#hello').text(data.hello);
    });
  }

  $('#btn_translate').click(fetchTranslation);

  $('#language_code').keypress(function (event) {
    if (event.keyCode === 13) {
      fetchTranslation();
    }
  });
});
