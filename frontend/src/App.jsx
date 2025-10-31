import React, { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [file, setFile] = useState(null);
  const [analysis, setAnalysis] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleAnalyze = async (e) => {
    e && e.preventDefault();
    if (!file) return alert("Please choose a file first.");
    setLoading(true);
    const formData = new FormData();
    formData.append("file", file);
    try {
      const res = await axios.post("http://localhost:8000/api/requirements/upload", formData, {
        headers: { "Content-Type": "multipart/form-data" },
      });
      setAnalysis(res.data.analysis ?? res.data ?? "No analysis returned");
    } catch (err) {
      console.error(err);
      alert("Upload failed. Check backend logs.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app-root">
      <header className="app-header">
        <div className="brand">
          <div className="logo" aria-hidden>
            {/* simple inline SVG logo */}
            <svg width="36" height="36" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
              <rect width="24" height="24" rx="6" fill="url(#g)" />
              <defs>
                <linearGradient id="g" x1="0" x2="1">
                  <stop offset="0" stopColor="#6EE7B7" />
                  <stop offset="1" stopColor="#3B82F6" />
                </linearGradient>
              </defs>
            </svg>
          </div>
          <div>
            <h1 className="title">AI Requirements Reviewer</h1>
            <p className="tag">Quick automated review for requirement docs</p>
          </div>
        </div>

        <div className="controls">
          <label className="file-label">
            <input
              type="file"
              accept=".txt,.pdf,.docx"
              onChange={(e) => setFile(e.target.files[0])}
            />
            <span>Choose file</span>
          </label>

          <button className="btn primary" onClick={handleAnalyze} disabled={loading}>
            {loading ? <span className="spinner" /> : "Analyze"}
          </button>
        </div>
      </header>

      <main className="container">
        <section className="hero">
          <h2>Upload a requirements document</h2>
          <p>Supported: .txt, .pdf, .docx — we’ll analyze clarity, completeness and detect ambiguities.</p>
        </section>

        <section className="result-card">
          <h3>Analysis Result</h3>
          {!analysis && <div className="empty">No analysis yet. Upload a file and click Analyze.</div>}
          {analysis && (
            <div className="result-body">
              {/* If analysis is an object/renderable JSON show formatted, otherwise show string */}
              {typeof analysis === "object" ? (
                <pre className="json">{JSON.stringify(analysis, null, 2)}</pre>
              ) : (
                <div className="text">{analysis}</div>
              )}
            </div>
          )}
        </section>
      </main>
    </div>
  );
}

export default App;
