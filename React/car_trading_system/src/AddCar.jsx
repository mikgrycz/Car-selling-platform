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
        BodyType: '',
        NumberOfReviews: 0,
        EngineSize: 2000,
        Transmission: 'Automatic',
        FuelType: 'Gasoline',
        DriveType: 'RWD',
        Power: 250,
    });
    const [selectedFile, setSelectedFile] = useState(null);
    const [estimate, setEstimate] = useState(null);
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

    const handleEstimate = async () => {
      const newCar =  {
        Make: car.Make,
        Model: car.Model,
        Year: parseInt(car.Year),
        Price: parseInt(car.Price),
        Mileage: parseInt(car.Mileage),
        Description: car.Description,
        BodyType: car.BodyType,
        Seller: 1,
        Transmission: car.Transmission,
        FuelType: car.FuelType,
        DriveType: car.DriveType,
        EngineSize: car.EngineSize,
        Power: car.Power

      };
      try {
          const response = await axios.post('http://localhost:8000/estimate/', newCar);
          console.log('Response data:', response.data);
          const estimatedCar = response.data;
          ///setCar(estimatedCar);
          setEstimate(estimatedCar.estimate);

      }
      catch (error) {
          console.error(error);
      }
  };


    const handleSubmit = async (event) => {
      event.preventDefault();
    
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
          EngineSize: car.EngineSize,
          Transmission: car.Transmission,
          FuelType: car.FuelType,
          DriveType: car.DriveType,
          Power: car.Power

      };
    
      try {
          // Post the new car to the database and get the response
          const response = await axios.post('http://localhost:8000/cars/', newCar);
      
          // Log the response data
          console.log('Response data:', response.data);
    
          // The response should include the posted car with its assigned ID
          const postedCar = response.data;
      
          // Create the directory for the car
          await axios.post('http://localhost:8000/create-dir/', { dir: `c${postedCar.CarID}` });
      
          // Upload the picture
          if (selectedFile) {
              const formData = new FormData();
              formData.append('photo', selectedFile);
      
              await axios.post(`http://localhost:8000/cars/${postedCar.CarID}/upload_photo/`, formData, {
                  headers: {
                      'Content-Type': 'multipart/form-data'
                  }
              });
      
              // Update the PictureLink in the car object
              postedCar.PictureLink = `\\CarData\\c${postedCar.CarID}\\c${postedCar.CarID}.png`;
              await axios.put(`http://localhost:8000/cars/${postedCar.CarID}/`, postedCar);
          }
      
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
      <div className="mb-3">
          <label className="form-label">Color</label>
          <input type="text" className="form-control" name="Color" value={car.Color} onChange={handleChange} />
      </div>
      <div className="mb-3">
          <label className="form-label">Transmission</label>
          <input type="text" className="form-control" name="Transmission" value={car.Transmission} onChange={handleChange} />
      </div>
      <div className="mb-3">
          <label className="form-label">Fuel Type</label>
          <input type="text" className="form-control" name="FuelType" value={car.FuelType} onChange={handleChange} />
      </div>
      <div className="mb-3">
          <label className="form-label">Engine Size</label>
          <input type="number" className="form-control" name="EngineSize" value={car.EngineSize} onChange={handleChange} />
      </div>
      <div className="mb-3">
          <label className="form-label">Drive Type</label>
          <input type="text" className="form-control" name="DriveType" value={car.DriveType} onChange={handleChange} />
      </div>
      <div className="mb-3">
          <label className="form-label">Power</label>
          <input type="number" className="form-control" name="Power" value={car.Power} onChange={handleChange} />
      </div>      
      <button type="button" className="btn btn-primary button-space" onClick={handleEstimate}>Estimate</button>
      
      <button type="submit" className="btn btn-primary">Submit</button>
        <div style={{ 
            backgroundColor: 'darkgrey', 
            color: 'white', 
            fontWeight: 'bold', 
            padding: '10px', 
            marginTop: '20px', 
            textAlign: 'center',
            borderRadius: '5px'
        }}>
            {estimate && `Estimated value: ${estimate}`}
        </div>        
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