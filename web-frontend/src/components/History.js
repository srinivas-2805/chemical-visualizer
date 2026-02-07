import { useEffect, useState } from "react";
import API from "../api";

function History({ refreshKey }) {
  const [datasets, setDatasets] = useState([]);

  useEffect(() => {
    API.get("history/").then((res) => setDatasets(res.data));
  }, [refreshKey]); // 👈 re-run when upload happens

  const downloadPDF = async (id, name) => {
    const res = await API.get(`report/${id}/`, {
      responseType: "blob",
    });

    const url = window.URL.createObjectURL(new Blob([res.data]));
    const link = document.createElement("a");
    link.href = url;
    link.download = `${name}_report.pdf`;
    link.click();
  };

  return (
  <div className="card">
  <h2>Upload History</h2>
  <ul className="history-list">
    {datasets.map((d) => (
      <li key={d.id}>
        <span>{d.name}</span>
        <button onClick={() => downloadPDF(d.id, d.name)}>
          Download PDF
        </button>
      </li>
    ))}
  </ul>
</div>

);

}

export default History;
