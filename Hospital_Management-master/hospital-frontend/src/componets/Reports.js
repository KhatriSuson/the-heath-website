import React, { useEffect, useState } from 'react';
import { dummyReports } from '../data/dummyData';

const Reports = () => {
  const [reports, setReports] = useState([]);

  useEffect(() => {
    setReports(dummyReports);
  }, []);

  return (
    <div style={{ padding: '2rem' }}>
      <h2>Your Reports</h2>
      <ul>
        {reports.map((report) => (
          <li key={report.id}>
            <p><strong>Result:</strong> {report.result}</p>
            <p><strong>Date:</strong> {report.date}</p>
            {report.image && <img src={report.image} alt="report" width="100" />}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Reports;
