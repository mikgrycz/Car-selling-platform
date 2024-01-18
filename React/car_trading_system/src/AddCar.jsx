import { useState } from 'react';

    const AddCar = () => {
    const [car, setCar] = useState({
        CarID: '',
        Make: '',
        Model: '',
        Year: '',
        Price: '',
        Mileage: '',
        Description: '',
        SellerID: '',
        PictureLink: '',
        BodyType: ''
    });
    const handleFileChange = (event) => {
        if (event.target.files && event.target.files[0]) {
        const file = event.target.files[0];
        const reader = new FileReader();
        reader.onloadend = () => {
            setCar({ ...car, PictureLink: reader.result });
        };
        reader.readAsDataURL(file);
        }
    };
    const handleChange = (event) => {
        setCar({ ...car, [event.target.name]: event.target.value });
    };

    const handleSubmit = (event) => {
        event.preventDefault();
      
        // Construct a new CarModel object
        const newCar = {
            Make: car.Make,
            Model: car.Model,
            Year: parseInt(car.Year),
            Price: parseInt(car.Price),
            Mileage: parseInt(car.Mileage),
            Description: car.Description,
            SellerID: 1,
            BodyType: car.BodyType
          };
      
        // ... submit the form ...
    };

  return (
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
  );
};

export default AddCar;