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
          <Route path="/car/:id" element={<CarDetails />} />
          <Route exact path="/" element={<CarGrid />} />
          <Route exact path="/cars/" element={<CarGrid />} />
          <Route exact path="/add-review/:id" element={<AddReview />} />
        </Routes>
      </div>
    </div>
  </Router>
);
};
export default App;
