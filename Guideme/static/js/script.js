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

function iconChange(id){
    let iconId=document.getElementById(id)
    if(iconId.src.match('Assets/img/Icons/Favorite-outlined.svg')){
        iconId.src='Assets/img/Icons/Favorite-filled.svg'
    }else{
        iconId.src='Assets/img/Icons/Favorite-outlined.svg'
    }
};


// hide navbar when scroll down
var prevScrollpos = window.pageYOffset;
window.onscroll = function() {
var currentScrollPos = window.pageYOffset;
if (prevScrollpos > currentScrollPos) {
    document.getElementById("navbar").style.top = "0";
} else {
    document.getElementById("navbar").style.top = "-100%";
}
prevScrollpos = currentScrollPos;
};




