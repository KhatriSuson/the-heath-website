import React, { useEffect, useState } from 'react';
import { dummyAppointments } from '../data/dummyData';

const Appointments = () => {
  const [appointments, setAppointments] = useState([]);

  useEffect(() => {
    setAppointments(dummyAppointments);
  }, []);

  return (
    <div style={{ padding: '2rem' }}>
      <h2>Your Appointments</h2>
      <ul>
        {appointments.map((appt) => (
          <li key={appt.id}>
            <strong>Doctor:</strong> {appt.doctor} | <strong>Date:</strong> {appt.date} | <strong>Status:</strong> {appt.status}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Appointments;
