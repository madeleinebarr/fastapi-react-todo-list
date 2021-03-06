import React, { Fragment, useState } from "react";

const InputTodo = ({ todos }) => {
    const [item, setItem] = useState("");

    // console.log(todos[todos.length-1].id + 1);

    const onSubmitForm = async (e) => {
        e.preventDefault();
    
        try {
            const body = { 
                "id": todos[todos.length-1].id + 1,
                "item": item
             };
            const response = await fetch("http://localhost:8000/todos", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(body),
            });

            window.location = "/";
            
        } catch (err) {
            console.error(err.message);
        }
    }

    return(
        <Fragment>
      <h1 className="text-center my-5">My todo list</h1>
      <form className="d-flex" onSubmit={onSubmitForm}>
        <input
          type="text"
          placeholder="add todo"
          className="form-control"
          value={item}
          onChange={(e) => setItem(e.target.value)}
        />
        <button className="btn btn-success">Add</button>
      </form>
    </Fragment>
    );
};

export default InputTodo;