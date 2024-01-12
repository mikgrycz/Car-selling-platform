import React, { useState, useEffect } from 'react';
import api from './api';
import axios from 'axios';
import { useSignIn } from 'react-auth-kit';
import './App.css';
import LoginForm from './login.jsx';
import { AuthProvider, useAuthState, useSignOut } from 'react-auth-kit';
import { Link, Route, useParams, Routes } from 'react-router-dom';
import { BrowserRouter as Router} from 'react-router-dom';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Dropdown, DropdownButton, FormControl } from 'react-bootstrap';
import { Button, Form } from 'react-bootstrap';
import { debounce } from 'lodash';

function CarSorterAndGrid() {
  const [cars, setCars] = useState([]);
  const [make, setMake] = useState('');
  const [model, setModel] = useState('');
  const [price, setPrice] = useState(10000000000);  // Set to a high number  const [cars, setCars] = useState([]);
  const [minPrice, setMinPrice] = useState(0);
  const [maxPrice, setMaxPrice] = useState(1000000000);
  const resetFilters = () => {
    setMake('');
    setModel('');
    setMaxPrice(10000000);
    setMinPrice(0);
  };
  
  const handleMakeChange = (eventKey) => {
    setMake(eventKey);
  };

  const handleModelChange = (eventKey) => {
    setModel(eventKey);
  };


  
  const handleMinPriceChange = (event) => {
    setMinPrice(event.target.value);
  };
  
  const handleMaxPriceChange = (event) => {
    setMaxPrice(event.target.value);
  };
  useEffect(() => {
    fetch('http://localhost:8000/cars')  // Update with your server's URL
      .then(response => response.json())
      .then(data => setCars(data.cars));
  }, []);

  const filteredCars = cars.filter(car => {
    return (make === '' || car.Make === make) &&
           (model === '' || car.Model === model) &&
           (car.Price >= minPrice && car.Price <= maxPrice);;
  });

  return (
    <div>
      
<br/>
<div>
<div className="d-flex justify-content-between">
  <div className="mb-3 flex-grow-1">
    <Dropdown onSelect={handleMakeChange}>
      <Dropdown.Toggle variant="success" id="dropdown-basic">
        {make || "Make"}
      </Dropdown.Toggle>

      <Dropdown.Menu>
        <Dropdown.Item eventKey="Porsche">Porsche</Dropdown.Item>
        <Dropdown.Item eventKey="Ferrari">Ferrari</Dropdown.Item>
        <Dropdown.Item eventKey="Lamborghini">Lamborghini</Dropdown.Item>
      </Dropdown.Menu>
    </Dropdown>
  </div>

  <div className="mb-3 flex-grow-1">
    <Dropdown onSelect={handleModelChange}>
      <Dropdown.Toggle variant="success" id="dropdown-basic">
        {model || "Model"}
      </Dropdown.Toggle>

      <Dropdown.Menu>
        <Dropdown.Item eventKey="911">911</Dropdown.Item>
        <Dropdown.Item eventKey="Huracan">Huracan</Dropdown.Item>
        <Dropdown.Item eventKey="Corvette">Corvette</Dropdown.Item>
      </Dropdown.Menu>
    </Dropdown>
  </div>

  <div className="mb-3 flex-grow-1" style={{ minWidth: '200px' }}>
  <label>Min Price: </label>
  <input className="input-field" type="number" min="0" max="1000000000" value={minPrice} onChange={handleMinPriceChange} />
</div>

<div className="mb-3 flex-grow-1" style={{ minWidth: '200px' }}>
  <label>Max Price: </label>
  <input className="input-field" type="number" min="0" max="1000000000" value={maxPrice} onChange={handleMaxPriceChange} />
</div>
  <div className="mb-3 flex-grow-1">
    <Button variant="primary" onClick={resetFilters}>Reset filters</Button>
  </div>
</div>
</div>


      <div className="centered-content">
        {filteredCars.map(car => (
          <Link key={car.CarID} to={`/car/${car.CarID}`}>
            <div key={car.CarID} className="car-details">
              <img className="car-image" src={car.PictureLink} alt={`${car.Make} ${car.Model}`} />
              <h2>{car.Make} {car.Model}</h2>
              <p>Year: {car.Year}</p>
              <p>Mileage: {car.Mileage + " KM"}</p>
              <p>Price: {car.Price + " PLN"}</p>
              <p>{car.Description}</p>
            </div>
          </Link>
        ))}
      </div>
    </div>
  );
}
function CarSorter() {
  const [make, setMake] = useState('');
  const [model, setModel] = useState('');
  const [price, setPrice] = useState(0);

  const handleMakeChange = (eventKey) => {
    setMake(eventKey);
    // Add your sorting logic here
  };

  const handleModelChange = (eventKey) => {
    setModel(eventKey);
    // Add your sorting logic here
  };

  const handlePriceChange = (event) => {
    setPrice(event.target.value);
    // Add your sorting logic here
  };

  return (
    <div>
<div className="login-button">
  <DropdownButton id="dropdown-basic-button" title="Make" onSelect={handleMakeChange}>
    <Dropdown.Item eventKey="Make1">Make1</Dropdown.Item>
    <Dropdown.Item eventKey="Make2">Make2</Dropdown.Item>
  </DropdownButton>
</div>

<div className="login-button">
  <DropdownButton id="dropdown-basic-button" title="Model" onSelect={handleModelChange}>
    <Dropdown.Item eventKey="Model1">Model1</Dropdown.Item>
    <Dropdown.Item eventKey="Model2">Model2</Dropdown.Item>
  </DropdownButton>
</div>

<FormControl type="range" min="0" max="1000000000" step="10000" value={price} onChange={handlePriceChange} />    
</div>
  );
}

function AddReview() {
  const [review, setReview] = useState('');
  const [rating, setRating] = useState(0);

  const handleSubmit = async (event) => {
    event.preventDefault();

    const response = await axios.post('http://localhost:8000/reviews/2', {
      review,
      rating,
    });

    console.log(response.data);
  };

  return (
    <form className="container" onSubmit={handleSubmit}>
      <div className="form-group">
        <div><br/></div>
        <label htmlFor="review">Please write your review here:</label>
        <div><br/></div>
        <textarea className="form-control" id="review" value={review} onChange={(e) => setReview(e.target.value)} />
      </div>
      <div className="form-group">
        <div><br/></div>
        <label htmlFor="rating">Rating (1 - 10):<br /> </label>
        <div><br/></div>
        <input className="form-control" type="number" min="1" max="10" id="rating" value={rating} onChange={(e) => setRating(e.target.value)} />
      </div>
      <br />
      <button className="btn btn-primary" type="submit">Submit</button>
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
        <Link key={car.CarID} to={`/car/${car.CarID}`}>
        <div key={car.CarID} className="car-details">
  <img className="car-image" src={car.PictureLink} alt={`${car.Make} ${car.Model}`} />
  <h2>{car.Make} {car.Model}</h2>
  <p>Year: {car.Year}</p>
  <p>Mileage: {car.Mileage + " KM"}</p>
  <p>Price: {car.Price + " PLN"}</p>
  <p>{car.Description}</p>
</div>
</Link>
      ))}
    </div>
  );
}



function CarDetails() {
  const [car, setCar] = useState(null);
  const { id } = useParams();
  useEffect(() => {
    fetch(`http://localhost:8000/car/${id}`)  // Update with your server's URL
      .then(response => response.json())
      .then(data => setCar(data));
  }, [id]);

  // Define handleAddReview inside CarDetails
  function handleAddReview() {
    // Navigate to the add review page
    window.location.href = `/add-review/${id}`; // Add this line
  }

  function handleBuy() {
    // Navigate to the add review page
    window.location.href = `/buy/${id}`; // Add this line
  }

  function handleShare() {
    // Navigate to the add review page
    window.location.href = `/share/${id}`; // Add this line
  }
  if (!car) return <div>Loading...</div>;

  return (
    <div className="car-details-one">
      <div className="car-image-container">
        <img className="car-image-one" src={car.PictureLink} alt={`${car.Make} ${car.Model}`} />
      </div>
      <div className="car-details-container">
        <br />
        <h2>{car.Make} {car.Model}</h2>
        <p><span className="field-name">Year:</span> {car.Year}</p>
        <p><span className="field-name">Mileage:</span> {car.Mileage + " KM"}</p>
        <p><span className="field-name">Price:</span> {car.Price + " PLN"}</p>
        <p><span className="field-name">Body Type:</span> {car.BodyType}</p>
        <p><span className="field-name">Seller ID:</span> {car.SellerID}</p>
        <p>{car.Description}</p>
          <div className="button-container">
            <button className="login-button" onClick={handleAddReview}>Add Review</button> {/* Add this line */}
            <button className="login-button" onClick={handleBuy}>Buy</button> {/* Add this line */}
            <button className="login-button" onClick={handleShare}>Share</button> {/* Add this line */}
          </div>
      </div>
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


const [user, setUser] = useState(null)
const [errorMessage, setErrorMessage] = useState(null);
return (
  <Router>
    <div>
      <nav className="navbar navbar-custom">
        <div className="container-fluid">
          <h1 className="logo">Car <br></br> Bazaar</h1>
          <a className="navbar-brand" href="#"></a>
          <LoginForm user={user} setUser={setUser} />

        </div>
      </nav>
      {/* {user && <p style={{ fontWeight: 'bold', color: 'white' }}>Welcome, {user.UserName}!</p>} */}
      <div className="car-grid-container">
        <Routes>
          <Route exact path="/"element={<CarSorterAndGrid />} />
          
            <Route exact path="/cars/"/>      
          <Route path="/car/:id" element={<CarDetails />} />
          <Route exact path="/add-review/:id" element={<AddReview />} />
        </Routes>
      </div>
      
    </div>
  </Router>
);
};
export default App;
