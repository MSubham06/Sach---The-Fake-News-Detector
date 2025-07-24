import React, { useState } from 'react';
import './App.css';

function App() {
  const [text, setText] = useState('');
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const checkNews = async (e) => {
    e.preventDefault();
    if (!text.trim()) return;
    
    setLoading(true);
    setError(null);
    
    try {
      const response = await fetch('http://localhost:5000/predict', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text }),
      });

      if (!response.ok) {
        throw new Error('Server error');
      }

      const data = await response.json();
      setResult(data);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app">
      <header>
        <h1>SACH - Fake News Detector</h1>
        <p>Check if your news is likely real or fake using AI</p>
      </header>
      
      <main>
        <form onSubmit={checkNews} className="news-form">
          <textarea
            value={text}
            onChange={(e) => setText(e.target.value)}
            placeholder="Paste news headline or text here..."
            required
          />
          <button type="submit" disabled={loading}>
            {loading ? 'Analyzing...' : 'Check News'}
          </button>
        </form>

        {error && <div className="error">{error}</div>}

        {result && (
          <div className={`result ${result.prediction}`}>
            <h3>
              {result.prediction === 'real' ? (
                <>
                  <span>✅</span> Likely Real News
                </>
              ) : (
                <>
                  <span>❌</span> Likely Fake News
                </>
              )}
            </h3>
            <div className="confidence">
              Confidence: {Math.round(result.confidence * 100)}%
            </div>
            <div className="tips">
              <h4>Fact-Checking Tips:</h4>
              <ul>
                <li>Check the source reputation</li>
                <li>Look for corroborating reports</li>
                <li>Verify dates and author information</li>
                <li>Search for fact-checking articles</li>
              </ul>
            </div>
          </div>
        )}
      </main>

      <footer>
        <p>© 2023 SACH - Fake News Detector | Open Source Project</p>
      </footer>
    </div>
  );
}

export default App;
