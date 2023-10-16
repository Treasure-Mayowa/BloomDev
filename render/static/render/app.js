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
})

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