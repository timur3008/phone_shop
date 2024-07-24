const filterBox = document.querySelector('.filter__box');
const filterList = document.querySelector('.filter__list');
const filterItems = document.querySelectorAll('.filter__item');


const brandFilter = document.querySelector('.brand__filter');
const memoryFilter = document.querySelector('.memory__filter');

const brandFilterText = document.querySelector('.brand__filter_text');
const memoryFilterText = document.querySelector('.memory__filter_text');

const brandFilterSvg = document.querySelector('.brand__filter_svg');
const memoryFilterSvg = document.querySelector('.memory__filter_svg');

const brandFilterTable = document.querySelector('.brand__filter_ul');
const memoryFilterTable = document.querySelector('.memory__filter_ul');

const brandFilterItems = document.querySelectorAll('.brand__filter_li');
const memoryFilterItems = document.querySelectorAll('.memory__filter_li');


brandFilter.addEventListener('click', event => {
    brandFilterSvg.classList.toggle('svg__active');
    brandFilterTable.classList.toggle('filter__none_active');
    console.log(brandFilterTable);
});

memoryFilter.addEventListener('click', event => {
    memoryFilterSvg.classList.toggle('svg__active');
    memoryFilterTable.classList.toggle('filter__none_active');
    console.log(memoryFilterTable);
});

filterBox.addEventListener('click', event => {
    filterBox.classList.toggle('filter__box_open');
    filterList.classList.toggle('filter__list_open');
});
// filterItems.forEach(item => {
//     item.addEventListener('click', event => {
//         event.preventDefault()
//         const query = event.currentTarget.innerText;
//         location.href = `${location.href}?order=${query}`
//     });
// })