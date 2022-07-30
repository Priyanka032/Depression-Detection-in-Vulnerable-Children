const hero = document.querySelector(".hero");
const slider = document.querySelector(".slider");
const headline = document.querySelector(".headline");

const tl = new TimelineMax();

tl.fromTo(hero,1, {height:"0%"},{height:"80%"});

