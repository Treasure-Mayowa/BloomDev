document.addEventListener("DOMContentLoaded", ()=> {
    const todoForm = document.querySelector("#todo-form")
    document.querySelector(".icon").addEventListener("click", () => {
        var x = document.getElementById("navbar");
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
    const checkboxs = document.getElementsByClassName("checkbox")
    for (let i = 0; i < checkboxs.length; i++) {
        checkboxs[i].addEventListener("change", () => {
            const id = checkboxs[i].getAttribute("data-id");
            if (checkboxs[i].checked) {
                fetch(`/todos/changed/checked/${id}`)
            
            } else {
                fetch(`/todos/changed/unchecked/${id}`)
            }    
    })
    const todosTrash = document.getElementsByClassName("bx bx-trash bx-sm todo")
    for (let i = 0; i < todosTrash.length; i++) {
        todosTrash[i].addEventListener("click", () => {
            const id = todosTrash[i].getAttribute("data-id");
            fetch(`/todos/changed/delete/${id}`)
            location.reload();
    })
    }
}})

// Journal entry delete
function confirmDelete(event, entryId) {
    event.preventDefault(); 

    const confirmed = confirm("Are you sure you want to delete this entry?");

    if (confirmed) {

        const deleteUrl = `/journal/delete/${entryId}`;
        window.location = deleteUrl;
    } else {
        // If the user cancels, do nothing
    }
}