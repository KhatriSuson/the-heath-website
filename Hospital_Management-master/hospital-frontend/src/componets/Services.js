import React from 'react';
import { services } from '../data/dummyData';

const Services = () => (
  <div style={{ padding: '2rem' }}>
    <h2>Our Services</h2>
    <div style={{ display: 'flex', gap: '1rem', flexWrap: 'wrap' }}>
      {services.map((s) => (
        <div key={s.id} style={{ border: '1px solid #ccc', padding: '1rem', width: '200px' }}>
          <h3>{s.icon} {s.title}</h3>
          <p>{s.description}</p>
        </div>
      ))}
    </div>
  </div>
);

export default Services;
