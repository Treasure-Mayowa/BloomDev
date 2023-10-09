document.addEventListener("DOMContentLoaded", ()=> {
    const todoForm = document.querySelector("#todo-form")
    document.querySelector(".icon").addEventListener("click", ()=> {
        var x = document.querySelector("nav");
        if (x.className === "navbar shadow") {
            x.className += " responsive";
        } else {
            x.className = "navbar shadow";
        }
    })
    document.getElementById("new-todo").addEventListener("click", ()=> {
        if (todoForm.style.display === "none") {
            todoForm.style.display = "block"
        } else {
            todoForm.style.display = "none"
        }
    })
})