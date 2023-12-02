import React, { useState, useEffect } from 'react';
import api from './api';
import axios from 'axios';
import { useSignIn } from 'react-auth-kit';

const LoginForm = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const signIn = useSignIn;

  const handleSubmit = async (event) => {
    event.preventDefault();

    const response = await axios.post('/token', {
      username: username,
      password: password,
    });

    if (response.data === null) {
      return false;
    }

    signIn({
      token: response.data.access_token,
      expiresIn: 3600, // replace with actual expiration time
      tokenType: response.data.token_type,
      authState: {}, // replace with actual auth state
    });
  };

  return (
    <form onSubmit={handleSubmit}>
      <label>
        <span style={{ display: 'inline-block', width: '100px', textAlign: 'right', color: 'grey' }}>Username:</span>
        <input
          type="text"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          style={{ width: '100px', marginLeft: '10px' }} // Adjusted width to 150px
        />
      </label>
      
      <label>
        <span style={{ display: 'inline-block', width: '100px', textAlign: 'right', color: 'grey' }}>Password:</span>
        <input
          type="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          style={{ width: '100px', marginLeft: '10px' }} // Adjusted width to 150px
        />
      </label>
      <br />
      <input type="submit" value="Log In" style={{ float: 'right' }} />
    </form>
  );
};

const App = () => {
  const [cars, setCars] = useState([]);
  const [fromData, setFormData] = useState({
    name: '',
    year: '',
    model: '',
    price: '',
  });

  const fetchCars = async () => {
    const response = await api.get('/users/');
    setCars(response.data);
  };

  useEffect(() => {
    fetchCars();
  }, []);

  const handleInputChange = (event) => {
    const value = event.target.type === 'checkbox' ? event.target.checked : event.target.value;
    setFormData({
      ...fromData,
      [event.target.name]: value,
    });
  };

  const handleFormSubmit = async (event) => {
    event.preventDefault();
    await api.post('/users/', fromData);
    fetchCars();
    setFormData({
      name: '',
      year: '',
      model: '',
      price: '',
    });
  };

  return (
    <div>
      <nav className="navbar navbar-dark bg-dark ">
        <div className="container-fluid">
          <a className="navbar-brand" href="#"></a>
          <LoginForm />
        </div>
      </nav>
      <h1 style={{ textAlign: 'center' }}>Car Trading System</h1>
      <ul>
        {/* {cars.map(car => (
          <li key={car.id}>{car.name}</li>
        ))} */}
      </ul>
    </div>
  );
};

export default App;
