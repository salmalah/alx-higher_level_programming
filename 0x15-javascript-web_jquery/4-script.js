$(document).ready(function () {
  $('#toggle_header').click(function () {
    const headerElement = $('header');

    if (headerElement.hasClass('red')) {
      headerElement.removeClass('red').addClass('green');
    } else if (headerElement.hasClass('green')) {
      headerElement.removeClass('green').addClass('red');
    } else {
      headerElement.addClass('red');
    }
  });
});
