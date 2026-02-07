import { useState } from "react";
import API from "../api";

function Login({ onLogin }) {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  const handleLogin = async (e) => {
    e.preventDefault();
    setError("");
    setLoading(true);

    try {
      const res = await API.post("login/", {
        username,
        password,
      });

      localStorage.setItem("token", res.data.token);
      onLogin();
    } catch {
      setError("❌ Invalid username or password");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="login-card">
      <h2>🔐 Login</h2>

      <form onSubmit={handleLogin}>
        <input
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          placeholder="Username"
          required
        />

        <input
          type="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          placeholder="Password"
          required
        />

        <button type="submit" disabled={loading}>
          {loading ? "Logging in..." : "Login"}
        </button>

        {error && (
          <p
            style={{
              marginTop: "12px",
              color: "#ff4b2b",
              textAlign: "center",
              fontWeight: 500,
            }}
          >
            {error}
          </p>
        )}
      </form>
    </div>
  );
}

export default Login;
