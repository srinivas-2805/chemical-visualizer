function Summary({ summary }) {
  return (
    <div className="card">
      <h2>Summary</h2>

      <div className="summary-grid">
        {Object.entries(summary).map(([key, value]) => (
          <div className="summary-item" key={key}>
            <h3>{key.replaceAll("_", " ").toUpperCase()}</h3>

            
            {typeof value === "object" && value !== null ? (
              <ul style={{ listStyle: "none", padding: 0 }}>
                {Object.entries(value).map(([k, v]) => (
                  <li key={k}>
                    {k}: <strong>{v}</strong>
                  </li>
                ))}
              </ul>
            ) : (
              <p>{value}</p>
            )}
          </div>
        ))}
      </div>
    </div>
  );
}

export default Summary;
