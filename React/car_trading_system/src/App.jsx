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


function CarGrid() {
  const [cars, setCars] = useState([]);

  useEffect(() => {
    fetch('http://localhost:8000/cars')  // Update with your server's URL
      .then(response => response.json())
      .then(data => setCars(data.cars));
  }, []);

  return (
    <div className="centered-content">
      {cars.map(car => (
        <div key={car.CarID} className="car-details">
  <img className="car-image" src={car.PictureLink} alt={`${car.Make} ${car.Model}`} />
  <h2>{car.Make} {car.Model}</h2>
  <p>Year: {car.Year}</p>
  <p>Mileage: {car.Mileage + " KM"}</p>
  <p>Price: {car.Price + " PLN"}</p>
  <p>{car.Description}</p>
</div>
      ))}
    </div>
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
  useEffect(() => {
    fetch('http://localhost:8000/cars')  // Update with your server's URL
      .then(response => response.json())
      .then(data => setCars(data.cars));
  }, []);


  // return (
  //   <div>
  //     <nav className="navbar navbar-custom">
  //       <div className="container-fluid">
  //         <h1 className="logo">Car <br></br> Bazaar</h1>
  //         <a className="navbar-brand" href="#"></a>
  //         <LoginForm />
  //       </div>
  //     </nav>
  //     <div>
  //       <div>
  //         <CarGrid />
  //       </div>
  //       {cars.map(car => (
  //         <div key={car.CarID}>
  //           <img src={car.PictureLink} alt={car.Make} />
  //           <h2>{car.Make} {car.Model}</h2>
  //           <p>{car.Description}</p>
  //           {/* Add more car details here */}
  //         </div>
  //       ))}
  //     </div>
  //   </div>
  // );
  // };


//   return (
//     <div className="App">
//       {/* Other components here */}
//       <CarGrid />

//       <div className="container">
//         <div className="row">
//           <div className="col-md-12">
//             <h1 className="logo">Car <br></br> Bazaar</h1>
//             <LoginForm />
//           </div>
//         </div>

//         <div className="row">
//           <div className="col-md-12">
//             <CarGrid />
//           </div>
//     </div>
//   </div>
//     </div>
//   );
// };
return (
  <div>
    <nav className="navbar navbar-custom">
      <div className="container-fluid">
        <h1 className="logo">Car <br></br> Bazaar</h1>
        <a className="navbar-brand" href="#"></a>
        <LoginForm />
      </div>
    </nav>
    <div className="car-grid-container">
      <CarGrid />
    </div>
  </div>
);
};
export default App;
