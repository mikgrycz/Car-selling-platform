import React, { useState, useEffect } from 'react';
import api from './api';
import axios from 'axios';
import { useSignIn } from 'react-auth-kit';
import './App.css';
function LoginForm() {
  return (
    <form className="login-form">
      <input className="input-field" type="text" placeholder="Username" />
      <input className="input-field" type="password" placeholder="Password" />
      <button className="login-button" type="submit">Login</button>
    </form>
  );
}

const App = () => {


  useEffect(() => {
    // Change the background color when the component mounts
    document.body.style.backgroundColor = '#27282c';

    // Reset the background color when the component unmounts
    return () => {
      document.body.style.backgroundColor = null;
    };
  }, []);
  const [cars, setCars] = useState([]);
  const [fromData, setFormData] = useState({
    name: '',
    year: '',
    model: '',
    price: '',
  });

  const fetchCars = async () => {
    const response = await api.get('/users');
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
    await api.post('/users', fromData);
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
<nav className="navbar navbar-custom">
  <div className="container-fluid">
    <a className="navbar-brand" href="#"></a>
    <LoginForm />
  </div>
</nav>
      <h1 className="logo">Car Trading System</h1>
      <ul>
        {/* {cars.map(car => (
          <li key={car.id}>{car.name}</li>
        ))} */}
      </ul>
    </div>
  );
};

export default App;
