// DOM
const button = document.getElementById("addBtn");
const lists = document.getElementById("lists");

function addList(todo) {
    const li = document.createElement("li");
    li.innerText = todo.title;
    lists.appendChild(li);
}

async function getUsers(){
    const url = "https://jsonplaceholder.typicode.com/todos";
    const res = await fetch(url);
    const todos = await res.json();
    return todos
}

async function ListUsers(){
    const todos = await getUsers();
    todos.forEach(addList);
}

window.addEventListener("load", ListUsers)
button.addEventListener("click", ListUsers)