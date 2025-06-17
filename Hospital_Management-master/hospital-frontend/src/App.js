import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Navbar from './componets/Navbar';
import Dashboard from './componets/Dashboard';
import Appointments from './componets/Appointments';
import Reports from './componets/Reports';
import Services from './componets/Services';

const App = () => (
  <Router>
    <Navbar />
    <Routes>
      <Route path="/" element={<Dashboard />} />
      <Route path="/appointments" element={<Appointments />} />
      <Route path="/reports" element={<Reports />} />
      <Route path="/services" element={<Services />} />
    </Routes>
  </Router>
);

export default App;
