import { useState } from "react";
import API from "../api";

function UploadForm({ setSummary, onUploadSuccess }) {
  const [file, setFile] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleUpload = async (e) => {
    e.preventDefault();

    if (!file) {
      alert("Please select a CSV file");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    try {
      setLoading(true);

      const res = await API.post("upload-csv/", formData);
      setSummary(res.data.summary);

      if (onUploadSuccess) {
        onUploadSuccess();
      }
    } catch (err) {
      console.error(err.response?.data || err);
      alert("Upload failed. Please upload a valid CSV file.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="card upload">
      <h2>Upload CSV File</h2>

      <form onSubmit={handleUpload}>
        <input
          type="file"
          accept=".csv"
          onChange={(e) => setFile(e.target.files[0])}
          required
        />

        <button type="submit" disabled={loading}>
          {loading ? "Uploading..." : "Upload"}
        </button>
      </form>
    </div>
  );
}

export default UploadForm;
