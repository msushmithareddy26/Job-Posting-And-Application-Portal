import React, { useState } from 'react';
import API from '../api';
import { render, screen } from '@testing-library/react';



export default function CandidateForm({ jobId, onApplied }) {
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [resume, setResume] = useState('');
  const [message, setMessage] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const cRes = await API.post('/candidates/', { name, email, resume });
      const candidateId = cRes.data.id;
      await API.post(`/jobs/${jobId}/apply/`, { candidate_id: candidateId }); // ✅ FIXED
      setMessage('✅ Applied successfully');
      onApplied && onApplied();
    } catch (err) {
      setMessage('❌ Error: ' + (err.response?.data?.detail || 'Try again'));
    }
  };

  return (
    <form onSubmit={handleSubmit} style={{ marginTop: '20px' }}>
      <h3>Apply Now</h3>
      <label>Name</label>
      <input
        value={name}
        onChange={e => setName(e.target.value)}
        required
      />
      <label>Email</label>
      <input
        type="email"
        value={email}
        onChange={e => setEmail(e.target.value)}
        required
      />
      <label>Resume (optional)</label>
      <textarea
        value={resume}
        onChange={e => setResume(e.target.value)}
      />
      <button type="submit" className="button">Apply</button>
      {message && <p>{message}</p>}
    </form>
  );
}
