import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import API from '../api';
import CandidateForm from '../components/CandidateForm';

export default function JobDetails() {
  const { id } = useParams();
  const [job, setJob] = useState(null);
  const [applicants, setApplicants] = useState([]);

  useEffect(() => {
    API.get(`/jobs/${id}/`).then(res => setJob(res.data));
    API.get(`/jobs/${id}/applicants/`).then(res => setApplicants(res.data));
  }, [id]);

  const handleApplied = () => {
    API.get(`/jobs/${id}/applicants/`).then(res => setApplicants(res.data));
    API.get(`/jobs/${id}/`).then(res => setJob(res.data));
  };

  if (!job) return <div>Loading...</div>;

  return (
    <div className="card">
      <h2 style={{ color: '#4f46e5' }}>{job.title}</h2>
      <p>{job.description}</p>
      <p><strong>Skills:</strong> {job.required_skills}</p>
      <p><strong>Recruiter:</strong> {job.recruiter?.name}</p>

      <CandidateForm jobId={id} onApplied={handleApplied} />

      <h3>Applicants ({applicants.length})</h3>
      <ul className="applicants">
        {applicants.map(a => (
          <li key={a.id}>
            {a.name} — <span style={{ color: '#555' }}>{a.email}</span>
          </li>
        ))}
      </ul>
    </div>
  );
}
