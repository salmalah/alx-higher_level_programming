$(document).ready(function () {
  // the povided Url is not working so I used the working url
  const apiUrl = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

  $.get(apiUrl, function (data) {
    $('#hello').text(data.hello);
  });
});
