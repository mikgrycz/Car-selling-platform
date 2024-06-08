import axios from 'axios';
import { useState } from 'react';
import './App.css';


    const AddCar = () => {
    const [car, setCar] = useState({
        CarID: 0,
        Make: '',
        Model: '',
        Year: 0,
        Price: 0,
        Mileage: 0,
        Description: '',
        SellerID: 0,
        PictureLink: '',
        BodyType: ''
    });
    const [selectedFile, setSelectedFile] = useState(null);

    const handleFileChange = (event) => {
        if (event.target.files && event.target.files[0]) {
        const file = event.target.files[0];
        const reader = new FileReader();
        reader.onloadend = () => {
            setCar({ ...car, PictureLink: reader.result });
        };
        reader.readAsDataURL(file);
        }
        setSelectedFile(event.target.files[0]);

    };
    const handleChange = (event) => {
        setCar({ ...car, [event.target.name]: event.target.value });
    };




    const handleSubmit = async (event) => {
        event.preventDefault();
      
        // Construct a new CarModel object
        /*
            CarID: Optional[int] = None
    Make: str
    Model: str
    Year: int
    Price: int
    Mileage: int
    Description: str
    SellerID: int
    PictureLink: str
    BodyType: str
        */
        const newCar =  {
            Make: car.Make,
            Model: car.Model,
            Year: parseInt(car.Year),
            Price: parseInt(car.Price),
            Mileage: parseInt(car.Mileage),
            Description: car.Description,
            Seller: 1,
            PictureLink: " ",
            BodyType: car.BodyType,
            NumberOfReviews: 0,
          };
      
          console.log(newCar.data);

          try {
            // Post the new car to the database and get the response
            const response = await axios.post('http://localhost:8000/cars/', newCar);
        
            // The response should include the posted car with its assigned ID
            const postedCar = response.data;
            postedCar.PictureLink = `\\CarData\\c${postedCar.CarID}\\c${postedCar.CarID}.png`;
            // Now you can use postedCar, which includes the assigned ID
            await axios.put(`http://localhost:8000/cars/${postedCar.CarID}/`, postedCar);
            
            await axios.post('http://localhost:8000/create-dir/', { dir: `c${postedCar.CarID}` });

            console.log(postedCar);
          } catch (error) {
            console.error(error);
          }

        
    };

  return (
    <div style={{ display: 'flex', justifyContent: 'space-between' }}>
    <form onSubmit={handleSubmit} style={{ padding: '100px' }}>
        <h1>Add a new car here: </h1>
        <div className="mb-3">
  <label className="form-label">Photo</label>
  <input type="file" className="form-control" name="PictureLink" onChange={handleFileChange} />
</div>
      <div className="mb-3">
        <label className="form-label">Make</label>
        <input type="text" className="form-control" name="Make" value={car.Make} onChange={handleChange} />
      </div>
      <div className="mb-3">
        <label className="form-label">Model</label>
        <input type="text" className="form-control" name="Model" value={car.Model} onChange={handleChange} />
      </div>
      <div className="mb-3">
        <label className="form-label">Year</label>
        <input type="number" className="form-control" name="Year" value={car.Year} onChange={handleChange} />
      </div>
      <div className="mb-3">
        <label className="form-label">Price</label>
        <input type="number" className="form-control" name="Price" value={car.Price} onChange={handleChange} />
      </div>
      <div className="mb-3">
        <label className="form-label">Mileage</label>
        <input type="number" className="form-control" name="Mileage" value={car.Mileage} onChange={handleChange} />
      </div>
      <div className="mb-3">
        <label className="form-label">Description</label>
        <input type="text" className="form-control" name="Description" value={car.Description} onChange={handleChange} />
      </div>
      <div className="mb-3">
        <label className="form-label">Body Type</label>
        <input type="text" className="form-control" name="BodyType" value={car.BodyType} onChange={handleChange} />
      </div>
      <button type="submit" className="btn btn-primary">Submit</button>
        <br />
        <br />
        <br />
        <br />
        <br />
    </form>
    <div className='car-image-container-2'>
      <br />
      <br />
      <br />
      <br />
      <br />
      <br />
      <br />
      <br/>
        <img className="car-image-two" src={process.env.PUBLIC_URL + '/Photos/garage.jpg'} alt="Garage" />
    </div>
    </div>
  );
};

export default AddCar;