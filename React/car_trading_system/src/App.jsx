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
import { Button, Form, Carousel } from 'react-bootstrap';
import { debounce } from 'lodash';
import { useHistory } from 'react-router-dom';
import AddCar from './AddCar.jsx';
function CarSorterAndGrid() {
  const [cars, setCars] = useState([]);
  const [make, setMake] = useState('');
  const [model, setModel] = useState('');
  const [price, setPrice] = useState(10000000000);  // Set to a high number  const [cars, setCars] = useState([]);
  const [minPrice, setMinPrice] = useState(0);
  const [maxPrice, setMaxPrice] = useState(1000000000);
  const [minMileage, setMinMileage] = useState(0);
  const [maxMileage, setMaxMileage] = useState(1000000000);
  const [BodyType, setBodyType] = useState('');
  const resetFilters = () => {
    setMake('');
    setModel('');
    setBodyType('');
    setMaxPrice(10000000);
    setMinPrice(0);
    setMinMileage(0);
    setMaxMileage(10000000);
  };
  
  const handleMakeChange = (eventKey) => {
    setMake(eventKey);
  };

  const handleModelChange = (eventKey) => {
    setModel(eventKey);
  };

  const handleBodyTypeChange = (eventKey) => {
    setBodyType(eventKey);
  };
  
  const handleMinPriceChange = (event) => {
    setMinPrice(event.target.value);
  };
  
  const handleMaxPriceChange = (event) => {
    setMaxPrice(event.target.value);
  };

  const handleMinMileageChange = (event) => {
    setMinPrice(event.target.value);
  };
  const handleMaxMileageChange = (event) => {
    setMaxPrice(event.target.value);
  };

  useEffect(() => {
    fetch('http://localhost:8000/cars')  // Update with your server's URL
      .then(response => response.json())
      .then(data => setCars(data.cars));
  }, []);

  const filteredCars = cars.filter(car => {
    const makeRegex = new RegExp(make, 'i');
    const modelRegex = new RegExp(model, 'i');
    const bodyTypeRegex = new RegExp(BodyType, 'i');
  
    return (make === '' || makeRegex.test(car.Make)) &&
           (model === '' || modelRegex.test(car.Model)) &&
           (BodyType === '' || bodyTypeRegex.test(car.BodyType)) &&
           (car.Price >= minPrice && car.Price <= maxPrice);
  });

  return (
    <div>
 <div className="carousel-container">
  <div className="centered-content">
    <Carousel>
      {cars.map(car => (
        <Carousel.Item key={car.CarID}>
          <Link to={`/car/${car.CarID}`}>
            <img className="d-block carousel-image" src={car.PictureLink} alt={`${car.Make} ${car.Model}`} />
            <Carousel.Caption>
              <h3>{car.Make} {car.Model}</h3>
              <p>Price: {car.Price + " PLN"}</p>
            </Carousel.Caption>
          </Link>
        </Carousel.Item>
      ))}
    </Carousel>
  </div>
</div>
<br/>
<br/> 
<br/>
<div>
<div className="d-flex justify-content-between" style={{paddingLeft:'30px'}}>
  <div className="mb-3 flex-grow-1">
    <Dropdown onSelect={handleMakeChange}>
      <Dropdown.Toggle variant="success" id="dropdown-basic">
        {make || "Make"}
      </Dropdown.Toggle>

      <Dropdown.Menu>
        <Dropdown.Item eventKey="Porsche">Porsche</Dropdown.Item>
        <Dropdown.Item eventKey="Ferrari">Ferrari</Dropdown.Item>
        <Dropdown.Item eventKey="Lamborghini">Lamborghini</Dropdown.Item>
        <Dropdown.Item eventKey="Chevrolet">Chevrolet</Dropdown.Item>
        <Dropdown.Item eventKey="Audi">Audi</Dropdown.Item>
        <Dropdown.Item eventKey="BMW">BMW</Dropdown.Item>
        <Dropdown.Item eventKey="Mercedes">Mercedes</Dropdown.Item>
        <Dropdown.Item eventKey="Ford">Ford</Dropdown.Item>
        <Dropdown.Item eventKey="Toyota">Toyota</Dropdown.Item>
        <Dropdown.Item eventKey="Honda">Honda</Dropdown.Item>
        <Dropdown.Item eventKey="Nissan">Nissan</Dropdown.Item>
        <Dropdown.Item eventKey="Mazda">Mazda</Dropdown.Item>
        <Dropdown.Item eventKey="Volkswagen">Volkswagen</Dropdown.Item>
        <Dropdown.Item eventKey="Volvo">Volvo</Dropdown.Item>
        <Dropdown.Item eventKey="Subaru">Subaru</Dropdown.Item>
        <Dropdown.Item eventKey="Mitsubishi">Mitsubishi</Dropdown.Item>
        <Dropdown.Item eventKey="Kia">Kia</Dropdown.Item>
        <Dropdown.Item eventKey="Hyundai">Hyundai</Dropdown.Item>
        <Dropdown.Item eventKey="Lexus">Lexus</Dropdown.Item>
        <Dropdown.Item eventKey="Infiniti">Infiniti</Dropdown.Item>
        <Dropdown.Item eventKey="Acura">Acura</Dropdown.Item>
        <Dropdown.Item eventKey="Alfa Romeo">Alfa Romeo</Dropdown.Item>
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
        <Dropdown.Item eventKey="488">488</Dropdown.Item>
        <Dropdown.Item eventKey="Aventador">Aventador</Dropdown.Item>
        <Dropdown.Item eventKey="Carrera">Carrera</Dropdown.Item>
        <Dropdown.Item eventKey="Cayman">Cayman</Dropdown.Item>
        <Dropdown.Item eventKey="F8">F8</Dropdown.Item>
        <Dropdown.Item eventKey="F12">F12</Dropdown.Item>
        <Dropdown.Item eventKey="Gallardo">Gallardo</Dropdown.Item>
        <Dropdown.Item eventKey="458">458</Dropdown.Item>
        <Dropdown.Item eventKey="488">488</Dropdown.Item>
        <Dropdown.Item eventKey="812">812</Dropdown.Item>
        <Dropdown.Item eventKey="SF90">SF90</Dropdown.Item>
        <Dropdown.Item eventKey="Portofino">Portofino</Dropdown.Item>
        <Dropdown.Item eventKey="812">812</Dropdown.Item>
        <Dropdown.Item eventKey="GTC4">GTC4</Dropdown.Item>
        <Dropdown.Item eventKey="488">488</Dropdown.Item>
        
      </Dropdown.Menu>
    </Dropdown>
  </div>


  <div className="mb-3 flex-grow-1">
    <Dropdown onSelect={handleBodyTypeChange}>
      <Dropdown.Toggle variant="success" id="dropdown-basic">
        {BodyType || "Body Type"}
      </Dropdown.Toggle>

      <Dropdown.Menu>
        <Dropdown.Item eventKey="convertible">convertible</Dropdown.Item>
        <Dropdown.Item eventKey="coupe">coupe</Dropdown.Item>
        <Dropdown.Item eventKey="roadster">roadster</Dropdown.Item>
        <Dropdown.Item eventKey="sedan">sedan</Dropdown.Item>
        <Dropdown.Item eventKey="suv">suv</Dropdown.Item>
        <Dropdown.Item eventKey="hatchback">hatchback</Dropdown.Item>
        <Dropdown.Item eventKey="pickup">pickup</Dropdown.Item>
        <Dropdown.Item eventKey="van">van</Dropdown.Item>
        <Dropdown.Item eventKey="wagon">wagon</Dropdown.Item>
        <Dropdown.Item eventKey="minivan">minivan</Dropdown.Item>
        <Dropdown.Item eventKey="bus">bus</Dropdown.Item>
        
      </Dropdown.Menu>
    </Dropdown>
  </div>

  <div className="mb-3 flex-grow-1" style={{ minWidth: '200px' }}>
  <label>Min Mileage: </label>
  <input className="input-field" type="number" min="0" max="1000000000" value={minPrice} onChange={handleMinMileageChange} />
</div>

<div className="mb-3 flex-grow-1" style={{ minWidth: '200px' }}>
  <label>Max Mileage: </label>
  <input className="input-field" type="number" min="0" max="1000000000" value={maxPrice} onChange={handleMaxMileageChange} />
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
  const [Mileage, setMileage] = useState(0);

  const handleMakeChange = (eventKey) => {
    setMake(eventKey);
    // Add your sorting logic here
  };

const handleMileageChange = (event) => {
  setMileage(event.target.value);
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

<div className="login-button">
  <DropdownButton id="dropdown-basic-button" title="Body style"  >
    <Dropdown.Item eventKey="Body1">Coupe</Dropdown.Item>
    <Dropdown.Item eventKey="Body2">Roadster</Dropdown.Item>
  </DropdownButton>
</div>
<FormControl type="range" min="0" max="1000000" step="1000" value={Mileage}  />    

<FormControl type="range" min="0" max="1000000000" step="10000" value={price} onChange={handleMileageChange} />    
</div>
  );
}

function AddReview() {
  const [review, setReview] = useState('');
  const [rating, setRating] = useState(0);
  const { id } = useParams();
  
  const handleSubmit = async (event) => {
    event.preventDefault();

    const response = await axios.post(`http://localhost:8000/reviews`, {
      Rating: rating,
      Comment: review,
      ReviewerID: 1,
      CarSoldID: id
    });

    console.log(response.data);
    // go to / 
    window.location.href = `/car/${id}`;
    
  };

  return (
    <form className="container" onSubmit={handleSubmit}>
      <br/>
      <div className="form-group">
        <label htmlFor="review">Please write your review here:</label>
        <div><br/></div>
        <textarea className="form-control" id="review" value={review} onChange={(e) => setReview(e.target.value)} />
      </div>
      <br/>
      <div className="form-group">
        <label htmlFor="rating">Rating (1 - 10):</label>
        <div><br/></div>
        <input className="form-control" type="number" min="1" max="10" id="rating" value={rating} onChange={(e) => setRating(e.target.value)} />
      </div>
      <br/>
      <button className="btn btn-primary" type="submit">Submit</button>
    </form>
  );
}

function EndOfTransaction() {
  const { id } = 1;
  //axios.post(`http://localhost:8000/buy/${id}`);
  return (
    <div className="container mt-5">
      <div className="jumbotron">
        <h1 className="display-4">Thank You for Your Interest!</h1>
        <hr className="my-4"/>
        <p className="lead">We appreciate doing business with you. Our team will contact you shortly.</p>
      </div>
      <div>
      <br />
      <br />
      <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', height: '100vh' }}>
  <img className="car-image-two" src={process.env.PUBLIC_URL + '/Photos/thankyou.jpg'} alt="Garage" />
</div>      
<br/>
      <br/>
      <br/>
    </div>
    </div>
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
  const [reviews, setReviews] = useState([]);
  const { id } = useParams();
  useEffect(() => {
    fetch(`http://localhost:8000/car/${id}`)  // Update with your server's URL
      .then(response => response.json())
      .then(data => setCar(data));

      fetch(`http://localhost:8000/reviews/${id}`)
      .then(response => response.json())
      .then(data => setReviews(data));
  }, [id]);

  // Define handleAddReview inside CarDetails
  function handleAddReview() {
    // Navigate to the add review page
    window.location.href = `/add-review/${id}`; // Add this line
  }

  function handleBuy() {
    // Navigate to the add review page
    window.location.href = `/buy/${id}`; // Add this line
    axios.post(`http://localhost:8000/buy/${id}`);

    // access endpoint to send email

  }

  function handleShare() {
    // Navigate to the add review page
    window.location.href = `https://www.facebook.com/`; // Add this line
  }
  if (!car) return <div>Loading...</div>;

  return (
    <div>
      <div className="car-details-one" style={{ paddingTop: '55px', paddingRight:'35px' }}>
        <br/>
        <br/>
        <div className="car-image-container">
          <img className="car-image-one" src={car.PictureLink} alt={`${car.Make} ${car.Model}`} />
        </div>
        <br/>
        <br/>
        <br/>
        <div className="car-details-container" style={{ padding: '30px' }}>
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
      <br/>
      <br/>
      <div className="reviews-container" style={{ overflowY: 'scroll', maxHeight: '200px' }}>
      <h2 className='component-class'>Reviews</h2> {/* Add this line */}
    <br/>
  {reviews.map((review) => (
    <div key={review.ReviewID} className="review">
      <p>Rating: {review.Rating}</p>
      <p>{review.Comment}</p>
      {/* Display other review fields as needed */}
    </div>
          ))}
        </div>
        <br/>
        <br/>
        <br/>
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
let storedUser = localStorage.getItem('user');
storedUser = storedUser ? JSON.parse(storedUser) : null;
return (
  <Router>
      <div className="main-content">
    <div>
      <nav className="navbar navbar-custom">
        <div className="container-fluid">
        <Link to="/">
          <h1 className="logo">Car <br></br> Bazaar</h1>
        </Link>
          <a className="navbar-brand" href="#"></a>
          <LoginForm user={user} setUser={setUser} />
          <Link to="/add-car">
          {storedUser && <button className="login-button">Add a new car</button>}
          </Link>
        </div>
      </nav>
      {/* {user && <p style={{ fontWeight: 'bold', color: 'white' }}>Welcome, {user.UserName}!</p>} */}
      <div className="car-grid-container">
        <Routes>
          <Route exact path="/"element={<CarSorterAndGrid />} />
          
            <Route exact path="/cars/"/>      
          <Route path="/car/:id" element={<CarDetails />} />
          <Route exact path="/add-review/:id" element={<AddReview />} />
          <Route exact path="/add-car" element={<AddCar />} />
          <Route exact path="/buy/:id" element={<EndOfTransaction />} />
        </Routes>
      </div>
      </div>
    </div>
    <br/>
    <br/>
    <br/>
    <br/>
<footer className="footer mt-auto py-1 bg-dark">
  <div className="container">
    <Link to="/">
      <span className="footer-text">© 2024 Car Bazaar. All rights reserved.</span>
    </Link>
  </div>
</footer>
  </Router>
);
};
export default App;
