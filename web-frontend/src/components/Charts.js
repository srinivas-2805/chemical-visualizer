import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend,
} from "chart.js";
import { Bar } from "react-chartjs-2";

ChartJS.register(
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend
);

function Charts({ summary }) {
  const equipmentStats = summary?.type_distribution; // ✅ FIX HERE

  if (!equipmentStats) return null;

  const isDark = document.body.classList.contains("dark");

const chartColors = isDark
  ? ["#bb86fc", "#03dac6", "#cf6679", "#ffd166", "#4dd0e1"]  // dark theme
  : ["#ff6384", "#36a2eb", "#4bc0c0", "#ffcd56", "#9966ff"]; // light theme


  const data = {
    labels: Object.keys(equipmentStats),
    datasets: [
  {
    label: "Equipment Count",
    data: Object.values(equipmentStats),
    backgroundColor: chartColors,
    borderRadius: 8,
  },
],

  };

  const options = {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      legend: {
        position: "top",
      },
      title: {
        display: true,
        text: "Equipment Distribution",
      },
    },
  };

  return (
    <div className="card chart-card">
      <h2>Equipment Count</h2>
      <div style={{ height: "350px" }}>
        <Bar data={data} options={options} />
      </div>
    </div>
  );
}

export default Charts;
