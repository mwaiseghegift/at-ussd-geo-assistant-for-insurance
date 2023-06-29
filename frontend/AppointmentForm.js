import React, { useState, useEffect } from "react";
import axios from "axios";

const AppointmentForm = () => {
  const [name, setName] = useState("");
  const [doctor, setDoctor] = useState("");
  const [address, setAddress] = useState("");
  const [contact_no, setContactNo] = useState("");
  const [lat, setLat] = useState("");
  const [long, setLong] = useState("");

  const handleNameChange = (e) => {
    setName(e.target.value);
  };

  const handleDoctorChange = (e) => {
    setDoctor(e.target.value);
  };

  const handleLatChange = (e) => {
    setDate(e.target.value);
  };

  const handleLongChange = (e) => {
    setTime(e.target.value);
  };

  const handleMessageChange = (e) => {
    setMessage(e.target.value);
  };

  const handleAddressChange = (e) => {
    setEmail(e.target.value);
  };

  const handleContactNoChange = (e) => {
    setPhoneNo(e.target.value);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await axios.post(
        // "https://api.carepointphysiotherapy.com/api/appointments/add/",
        {
          doctor: parseInt(doctor),
          name,
          address,
          contact_no,
          lat,
          long,
          message,
        }
      );
      alert("Appointment booked successfully");
      // clear form
      setDoctor("");
      setName("");
      setAddress("");
      setContactNo("");
      setLat("");
      setLong("");
    } catch (error) {
      console.log(error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <div className="row">
        <div className="form-group col-12">
          <label htmlFor="name">Name</label>
          <input
            type="name"
            className="form-control"
            id="name"
            name="name"
            value={name}
            onChange={handleNameChange}
          />
        </div>
      </div>

      <div className="row">
        <div className="form-group col-6">
          <label htmlFor="address">Address</label>
          <input
            type="address"
            className="form-control"
            id="address"
            name="address"
            value={address}
            onChange={handleAddressChange}
          />
        </div>

        <div className="form-group col-6">
          <label htmlFor="contact_no">Contact No</label>
          <input
            type="text"
            className="form-control"
            id="contact_no"
            name="contact_no"
            value={contact_no}
            onChange={handleContactNoChange}
          />
        </div>
      </div>

      <div className="row">
        <div className="form-group col-6">
          <label htmlFor="date">Doctor</label>
          <input
            type="date"
            className="form-control"
            id="date"
            name="date"
            value={date}
            onChange={handleDoctorChange}
          />
        </div>

        <div className="form-group col-6">
          <label htmlFor="time">Latitude</label>
          <input
            type="latitude"
            className="form-control"
            id="latitude"
            name="latitude"
            value={lat}
            onChange={handleLatChange}
          />
        </div>

        <div className="form-group col-6">
          <label htmlFor="time">Longitude</label>
          <input
            type="longitude"
            className="form-control"
            id="longitude"
            name="longitude"
            value={long}
            onChange={handleLongChange}
          />
        </div>
      </div>

      <div className="form-group">
        <label htmlFor="message">Message</label>
        <textarea
          className="form-control"
          id="message"
          name="message"
          rows="3"
          value={message}
          onChange={handleMessageChange}
        ></textarea>
      </div>
      <button type="submit" className="btn btn-primary">
        Book Appointment
      </button>
    </form>
  );
};

export default AppointmentForm;
