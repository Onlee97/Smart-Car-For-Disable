$(document).ready(function() {
    setTimeout(function() {
        $(".inner").fadeOut(500);
    }, 3000);

    $('#btnReset').click(function() {
        $(".inner").show();
        setTimeout(function() {
            $(".inner").fadeOut(500);
        }, 3000);
    });
});