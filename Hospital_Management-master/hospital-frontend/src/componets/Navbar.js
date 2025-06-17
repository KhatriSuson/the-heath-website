import React from 'react';
import { Link } from 'react-router-dom';

const Navbar = () => (
  <nav style={{ padding: '1rem', background: '#007bff', color: 'white' }}>
    <Link to="/" style={{ color: 'white', marginRight: '1rem' }}>Dashboard</Link>
    <Link to="/appointments" style={{ color: 'white', marginRight: '1rem' }}>Appointments</Link>
    <Link to="/reports" style={{ color: 'white', marginRight: '1rem' }}>Reports</Link>
    <Link to="/services" style={{ color: 'white' }}>Services</Link>
  </nav>
);

export default Navbar;
