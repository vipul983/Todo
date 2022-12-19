import React, { useState, useEffect } from 'react';
import axios from 'axios';

const TodoList = () => {
  const [todos, setTodos] = useState([]);
  const [newTodo, setNewTodo] = useState('');

  useEffect(() => {
    const fetchTodos = async () => {
      try {
        const response = await axios.get('http://localhost:8000/todos');
        setTodos(response.data);
        console.log(response.data)
      } catch (error) {
        console.error(error);
      }
    };

    fetchTodos();
  }, []);

  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      console.log(newTodo)
      var data = {
        title: newTodo,
      }
      await axios.post('http://localhost:8000/todos/', data);
      setNewTodo('');
      setTodos([...todos, { text: newTodo, id: Date.now() }]);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div>
    <div>
      <form style={{marginTop: "10px"}} onSubmit={handleSubmit} >
        <label htmlFor="new-todo" style={{marginRight:"10px"}}>New Todo:</label>
        <input
          id="new-todo"
          value={newTodo}
          onChange={(event) => setNewTodo(event.target.value)}
        />
        <button type="submit" style={{marginLeft:"10px"}}>Add Todo</button>
      </form>
      <ul style={{
    display: "flex",
    flexDirection: "column",
    alignItems: "center"
}}>
        {todos.map((todo) => (
          <li style= {{padding : "10px"}} key={todo.id}>{todo.text}</li>
        ))}
      </ul>
    </div>
    </div>
  );
};

export default TodoList;