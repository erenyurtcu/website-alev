
var slider_img = document.querySelector('.sliderimg');
var images = ["{% static 'images/slider-img.jpg' %}","{% static 'images/slider-bg.jpg' %}","{% static 'images/slider-img.jpg' %}","{% static 'images/slider-bg.jpg' %}"]
var i = 0;

function prev(){
    if(i <= 0) i = images.length;
    i--;
    return setImg();
}

function next(){
    if( i >= images.length - 1) i = -1;
    i++;
    return setImg();
}

function setImg(){
    return slider_img.setAttribute('src', images[i]);
}