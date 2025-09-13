import React from 'react';
import { BrowserRouter, Routes, Route, Link } from 'react-router-dom';
import JobList from './pages/JobList';
import JobDetails from './pages/JobDetails';
import './App.css';

function App(){
  return (
    <BrowserRouter>
      <header>
        <div className="container" style={{display:'flex',justifyContent:'space-between',alignItems:'center'}}>
          <h1><Link to="/" style={{color:'white', textDecoration:'none'}}>Job Portal</Link></h1>
          <nav>
            <Link to="/">Jobs</Link>
          </nav>
        </div>
      </header>
      <main className="container">
        <Routes>
          <Route path='/' element={<JobList/>} />
          <Route path='/jobs/:id' element={<JobDetails/>} />
        </Routes>
      </main>
    </BrowserRouter>
  )
}

export default App;