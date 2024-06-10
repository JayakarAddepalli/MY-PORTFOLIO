window.addEventListener('load', ()=>{
    const loader = document.querySelector(".loader")
    loader.classList.add("loader-hidden");

    loader.addEventListener('transitionend', ()=>{
        document.body.removeChild(loader);
    });
})

let mouse_pointer = document.getElementsByClassName('mouse-pointer')[0];

document.addEventListener('mousemove',(e)=>{
    ex = e.clientX
    ey = e.clientY
    
    mouse_pointer.style.top = ey
    mouse_pointer.style.left = ex
})


let menuburgur = document.getElementById('menuburgur');
let navbarsmlscr = document.getElementsByClassName('navbar-sml-scr')[0];
let crossimg = document.getElementById('crossimg');


menuburgur.addEventListener('click',()=>{
    navbarsmlscr.style.display = 'block';
})

crossimg.addEventListener('click',()=>{
    navbarsmlscr.style.display = 'none';
})
