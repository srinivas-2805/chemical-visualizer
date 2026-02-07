import "./index.css";
import { useEffect, useState } from "react";
import Login from "./components/Login";
import UploadForm from "./components/UploadForm";
import Summary from "./components/Summary";
import Charts from "./components/Charts";
import History from "./components/History";

function App() {
  const [loggedIn, setLoggedIn] = useState(false);
  const [authChecked, setAuthChecked] = useState(false);
  const [summary, setSummary] = useState(null);
  const [historyKey, setHistoryKey] = useState(0);

  
  const [darkMode, setDarkMode] = useState(
    localStorage.getItem("theme") === "dark"
  );

  
  const [toast, setToast] = useState("");

  useEffect(() => {
    const token = localStorage.getItem("token");
    if (token) setLoggedIn(true);
    setAuthChecked(true);
  }, []);

  useEffect(() => {
    document.body.className = darkMode ? "dark" : "light";
    localStorage.setItem("theme", darkMode ? "dark" : "light");
  }, [darkMode]);

  const handleLogout = () => {
    localStorage.removeItem("token");
    setLoggedIn(false);
    setSummary(null);
  };

  const triggerHistoryRefresh = () => {
    setHistoryKey((k) => k + 1);
  };

  if (!authChecked) {
    return <p style={{ textAlign: "center" }}>Loading...</p>;
  }

  if (!loggedIn) {
    return <Login onLogin={() => setLoggedIn(true)} />;
  }

  return (
    <div className="app-container">
      
      {toast && <div className="toast">{toast}</div>}

      
      <div className="app-header">
        <h1>⚗️ Chemical Equipment Parameter Visualizer</h1>

        <div style={{ display: "flex", gap: "10px" }}>
          <button onClick={() => setDarkMode(!darkMode)}>
            {darkMode ? "☀️ Light" : "🌙 Dark"}
          </button>

          <button className="logout" onClick={handleLogout}>
            Logout
          </button>
        </div>
      </div>

      
      <UploadForm
        setSummary={setSummary}
        onUploadSuccess={() => {
          triggerHistoryRefresh();
          setToast("✅ CSV uploaded successfully");
          setTimeout(() => setToast(""), 3000);
        }}
      />

      
      {summary && (
        <>
          <Summary summary={summary} />
          <Charts summary={summary} />
        </>
      )}

      <History refreshKey={historyKey} />
    </div>
  );
}

export default App;
