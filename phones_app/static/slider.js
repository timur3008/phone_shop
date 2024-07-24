const screens = document.querySelectorAll('.phone__content-screen');
const mainImage = document.querySelector('.phone__main_image');
let index = 0;

screens.forEach(screen => {
    screen.addEventListener('click', event => {
        screens[index].classList.remove('screen__active');
        index = Number.parseInt(event.currentTarget.dataset.position);
        screens[index].classList.add('screen__active');
        mainImage.src = screens[index].src;
    })
})