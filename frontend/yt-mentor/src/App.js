import React from 'react';
import './App.css';

const onSubmission = e => {
  e.preventDefault();
}

function App() {
  return (
    <div className='App'>
      <body>
        <a 
          href='https://github.com/cherman23/hackbeanpot2024'
          target='_blank'
          rel='noreferrer noopener'>
          <button className='about'>
            About
          </button>
        </a>
        <h1> YT Mentor </h1>
        <div>
          <form className='container'> 
            <input
              type="Text" 
              className="inputData"
              name='input'
              onClick={onSubmission}>
            </input>
          </form>
        </div>
        <div
          className='playlist'>
        </div>
      </body>
    </div>
  );
}

export default App;
