import React, {useEffect, useState} from 'react';
import API from '../api';
import { Link } from 'react-router-dom';

export default function JobList() {
  const [jobs, setJobs] = useState([]);

  useEffect(() => {
    API.get('/jobs/')
      .then(res => setJobs(res.data))
      .catch(console.error);
  }, []);

  return (
    <div>
      <h2>Open Jobs</h2>
      <ul className="job-list">
        {jobs.map(job => (
          <li key={job.id}>
            <div className="card">
              <h3 style={{ marginTop: 0, color: '#4f46e5' }}>{job.title}</h3>
              <p><strong>Recruiter:</strong> {job.recruiter?.name || 'Unknown'}</p>
              <p><strong>Applicants:</strong> {job.applicants_count}</p>
              <Link to={`/jobs/${job.id}`} className="button">View Details</Link>
            </div>
          </li>
        ))}
      </ul>
    </div>
  );
}
