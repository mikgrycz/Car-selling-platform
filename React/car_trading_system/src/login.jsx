import React, { useState, useEffect } from 'react';
import axios from 'axios';

function LoginForm() {
  const [username, setusername] = useState('');
  const [password, setPassword] = useState('');
  const [user, setUser] = useState(null);

  const handleLogin = () => { 
   // window.location.reload();
  };
  const handleLogout = () => {
    setUser(null); // Clear the user's information from state
    localStorage.removeItem('user'); // Clear the user's information from local storage
    localStorage.removeItem('token'); // Clear the token from local storage
      window.location.reload();

  };
  useEffect(() => {
    const loggedInUser = localStorage.getItem('user');
    if (loggedInUser) {
      const foundUser = JSON.parse(loggedInUser);
      setUser(foundUser);
    }
  }, []);

  const handleSubmit = async (event) => {
    event.preventDefault();

    try {
      const response = await axios.post('http://localhost:8000/api/login/', {
        username,
        password,
      }, {
        headers: {
          'Content-Type': 'application/json',
        },
      });

      if (response.status === 200) {
        console.log('Login successful');
        setUser(response.data); // Store the user's information
        console.log(response.data); // Log the user's information
        localStorage.setItem('user', JSON.stringify(response.data)); // Store the user's information in local storage
        localStorage.setItem('token', response.data.token); // Store the token in local storage
        window.location.reload();
      } else {
        console.error('Login failed');
      }
    } catch (error) {
      console.error('A login error occurred:', error);
    }
  };

  return (
    <form className="login-form" onSubmit={handleSubmit}>
      <input
        className="input-field"
        type="text"
        value={username}
        onChange={(e) => setusername(e.target.value)}
        placeholder="username"
      />
      <input
        className="input-field"
        type="password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
        placeholder="password"
      />
      <button className="login-button" type="submit" onClick={handleLogin}>Login</button>
      {user && <button className="login-button" onClick={handleLogout}>Logout</button>}
      <div className="login-message">
      <div className='login-button'>
      {user ? `Welcome, ${user.UserName}!`:"Hello, Guest!"}
      </div>
      
      </div>
    </form>
  );
}


export default LoginForm;