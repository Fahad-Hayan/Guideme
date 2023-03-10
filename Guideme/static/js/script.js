// hide navbar when scroll down using jQuery
$(document).ready(function () {
    var prevScrollpos = window.pageYOffset;
    window.onscroll = function () {
        var currentScrollPos = window.pageYOffset;
        if (prevScrollpos > currentScrollPos) {
            document.getElementById("navbar").style.top = "0";
        } else {
            document.getElementById("navbar").style.top = "-100%";
        }
        prevScrollpos = currentScrollPos;
    }
});

function toggleFavorite(cityName) {
    // get the image element of the favorite button
    var favIcon = document.getElementsByClassName(cityName + 'F-icon');
    for(var i=0; i<favIcon.length;i++)
    {
        if (favIcon.item(i).getAttribute('src') === "/static/img/Icons/Favorite-outlined.svg") {
            favIcon.item(i).setAttribute('src', "/static/img/Icons/Favorite-filled.svg");
        } else {
            favIcon.item(i).setAttribute('src', "/static/img/Icons/Favorite-outlined.svg");
        } 
    }
}

function passwordVisibility() {
    var element = document.getElementById("password");
    var eyeStatus = document.getElementById("pass-eye");
    if (element.type === "password") {
    element.type = "text";
    eyeStatus.setAttribute("src","/static/img/Icons/opend-eye.svg");
    } else {
    element.type = "password";
    eyeStatus.setAttribute("src","/static/img/Icons/closed-eye.svg");
    }
}

$(".owl-carousel").owlCarousel({
    items: 4,
    nav: true,
    loop:false,
    lazyLoad: true,
    dots: false,
    responsive:{
        0:{
            items:1,
        },
        500:{
            items:2
        },
        768:{
            items:3
        },
        992:{
            items:4
        },
    }
});






