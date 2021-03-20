//smooth scrolling for safari
$(document).ready(function () {
    $('a').on('click', function (event) {
        if (this.hash !== "") {
            event.preventDefault();
            var hash = this.hash;
            $('html, body').animate({
                scrollTop: $(hash).offset().top
            }, 800, function () {
                window.location.hash = hash;
            });
        }
    });

    /*
    $("#add-user-button").click(function(){
        $("#add-user-button").toggleClass('add-user-body');
        if($("#add-user-button").hasClass('add-user-body')){
            $("#add-user-button").text('show less').css('background-color', '#FFDDD2');
            $(".add-user-body").slideDown(200);
        } else {
            $("#add-user-button").text('New User').css('background-color', '#FFDDD2');
            $(".add-user-body").slideUp(200);
        }
    });
    */
});