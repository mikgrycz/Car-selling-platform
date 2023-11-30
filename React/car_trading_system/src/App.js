// import logo from './logo.svg';
// import './App.css';

// function App() {
//   return (
//     <h1>Car Trading System</h1>
//   );
// }
import React, {useState, useEffect} from 'react';
import api from './api'

const App = () => {
  const [cars, setCars] = useState([])
  const [fromData, setFormData] = useState({
    name: '',
    year: '',
    model: '',
    price: ''
  })
  const fetchCars = async() => {
      const response = await api.get('/Users/');

  }
  useEffect(() => {
   // api.get('/Users').then(response => {
   //   setCars(response.data)
   // })
    fetchCars()
  }, [])

  const handleInputChange = event => {
    const value = event.target.type === 'checkbox' ? event.target.checked : event.target.value;
    setFormData({
      ...fromData,
      [event.target.name]: value,
    });
  };
  const handleFormSubmit = async (event) => {
    event.preventDefault();
    await api.post('/Users/', fromData);
    fetchCars();
    setFormData({
      name: '',
      year: '',
      model: '',
      price: ''
    });
  };
  return (
    <div>
      <nav className='navbar navbar-dark bg-primary '>
        <div className='container-fluid'>
          <a className='navbar-brand' href='#'>
            </a>
        </div>
      </nav>
      <h1 style={{ textAlign: 'center' }}>Car Trading System</h1>
      <ul>
        {/* {cars.map(car => (
          <li key={car.id}>{car.name}</li>
        ))} */}
      </ul>
    </div>
  )
}
export default App;
