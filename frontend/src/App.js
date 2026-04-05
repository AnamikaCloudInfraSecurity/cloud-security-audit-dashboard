import { useCallback, useEffect, useState } from "react";
import './App.css';
import { PieChart, Pie, Cell, ResponsiveContainer, Legend, Tooltip, LineChart, Line, CartesianGrid, XAxis, YAxis } from 'recharts';

function App() {
  const [findings, setFindings] = useState([]);
  const [filter, setFilter] = useState("ALL");
  const [serviceFilter, setServiceFilter] = useState("ALL");
  const [search, setSearch] = useState("");
  const [autoRefresh, setAutoRefresh] = useState(false);
  const [lastRefresh, setLastRefresh] = useState(null);

  const fetchData = useCallback(() => {
    fetch("https://aihuv81qb1.execute-api.ap-southeast-2.amazonaws.com/Prod/reports")
      .then(res => res.json())
      .then(data => {
        let parsed;

        if (data.body) {
          parsed = JSON.parse(data.body); // API Gateway format
        } else {
          parsed = data; // direct JSON format
        }

        // Ensure parsed is always an array
        let normalized = [];
        if (Array.isArray(parsed)) {
          normalized = parsed;
        } else if (parsed && typeof parsed === 'object') {
          const findingsArray = parsed.findings || parsed.data || Object.values(parsed)[0];
          normalized = Array.isArray(findingsArray) ? findingsArray : [];
        }

        setFindings(normalized);
        setLastRefresh(new Date());
      })
      .catch(err => console.error(err));
  }, []);

  useEffect(() => {
    fetchData();
  }, [fetchData]);

  useEffect(() => {
    if (!autoRefresh) return;

    const intervalId = setInterval(fetchData, 30000);
    return () => clearInterval(intervalId);
  }, [autoRefresh, fetchData]);

  const pieData = [
    { name: 'High', value: findings.filter(d => d.severity === 'HIGH').length, color: '#e74c3c' },
    { name: 'Medium', value: findings.filter(d => d.severity === 'MEDIUM').length, color: '#f39c12' },
    { name: 'Low', value: findings.filter(d => d.severity === 'LOW').length, color: '#27ae60' },
  ];

  const severityCounts = {
    high: findings.filter(d => d.severity === 'HIGH').length,
    medium: findings.filter(d => d.severity === 'MEDIUM').length,
    low: findings.filter(d => d.severity === 'LOW').length,
  };

  const totalFindings = findings.length;
  const riskScore = totalFindings
    ? Math.round(((severityCounts.high * 5 + severityCounts.medium * 3 + severityCounts.low * 1) / (totalFindings * 5)) * 100)
    : 0;

  const latestScanTime = findings.reduce((latest, item) => {
    const date = new Date(item.timestamp);
    return isNaN(date) ? latest : (latest === null || date > latest ? date : latest);
  }, null);

  const scanTime = latestScanTime || lastRefresh;
  const scanTimeLabel = scanTime
    ? scanTime.toLocaleString('en-AU', { day: '2-digit', month: 'short', year: 'numeric', hour: '2-digit', minute: '2-digit', hour12: true })
    : 'Updating...';

  const trendData = (() => {
    const days = Array.from({ length: 7 }).map((_, idx) => {
      const date = new Date();
      date.setHours(0, 0, 0, 0);
      date.setDate(date.getDate() - (6 - idx));
      return {
        key: date.toISOString().slice(0, 10),
        label: date.toLocaleDateString('en-US', { month: 'short', day: 'numeric' }),
        total: 0,
      };
    });

    const bucket = new Map(days.map(day => [day.key, day]));
    findings.forEach(item => {
      const date = new Date(item.timestamp);
      if (isNaN(date)) return;
      const key = date.toISOString().slice(0, 10);
      const row = bucket.get(key);
      if (row) row.total += 1;
    });

    return days;
  })();

  // Get unique services for filter
  const uniqueServices = ["ALL", ...new Set(findings.map(d => d.service))];

  // Filter and search logic
  const filteredData = findings
    .filter(item => {
      const severityMatch = filter === "ALL" || item.severity === filter;
      const serviceMatch = serviceFilter === "ALL" || item.service === serviceFilter;
      const searchMatch = 
        search === "" ||
        item.resource_id.toLowerCase().includes(search.toLowerCase()) ||
        item.issue.toLowerCase().includes(search.toLowerCase()) ||
        (item.compliance && item.compliance.toLowerCase().includes(search.toLowerCase()));
      return severityMatch && serviceMatch && searchMatch;
    })
    .sort((a, b) => new Date(b.timestamp) - new Date(a.timestamp));

  return (
    <div className="dashboard-container">
      <div className="top-panel">
        <div className="top-left">
          <div className="dashboard-header">
            <span className="dashboard-badge">Security Overview</span>
            <h1 className="dashboard-title">Cloud Security Dashboard</h1>
            <p className="dashboard-subtitle">Monitor findings, compliance, and severity in one modern control panel.</p>

            <div className="dashboard-meta">
              <div className="meta-item">
                <span>Last scan</span>
                <strong>{scanTimeLabel}</strong>
              </div>
              <div className="meta-item">
                <span>Risk score</span>
                <strong>{riskScore}/100</strong>
              </div>
              <button
                className={`live-toggle ${autoRefresh ? 'active' : ''}`}
                onClick={() => setAutoRefresh(prev => !prev)}
              >
                {autoRefresh ? 'Live mode on' : 'Live mode off'}
              </button>
            </div>
          </div>

          <div className="search-section">
            <input
              type="text"
              placeholder="Search by resource, issue, or compliance..."
              value={search}
              onChange={(e) => setSearch(e.target.value)}
              className="search-input"
            />
          </div>

          <div className="filter-bar">
            <div className="filter-group inline">
              <span>Severity</span>
              <div className="filter-buttons">
                <button className={`filter-btn ${filter === "ALL" ? "active" : ""}`} onClick={() => setFilter("ALL")}>All</button>
                <button className={`filter-btn ${filter === "HIGH" ? "active" : ""}`} onClick={() => setFilter("HIGH")}>High</button>
                <button className={`filter-btn ${filter === "MEDIUM" ? "active" : ""}`} onClick={() => setFilter("MEDIUM")}>Medium</button>
                <button className={`filter-btn ${filter === "LOW" ? "active" : ""}`} onClick={() => setFilter("LOW")}>Low</button>
              </div>
            </div>

            <div className="filter-group inline">
              <span>Service</span>
              <div className="filter-buttons">
                {uniqueServices.map(service => (
                  <button
                    key={service}
                    className={`filter-btn ${serviceFilter === service ? "active" : ""}`}
                    onClick={() => setServiceFilter(service)}
                  >
                    {service}
                  </button>
                ))}
              </div>
            </div>
          </div>
        </div>

        <div className="chart-panel">
          <div className="panel-header">
            <div>
              <h2>Severity Distribution</h2>
              <p>Live breakdown of findings by severity</p>
            </div>
          </div>
          <div className="chart-body">
            <div className="chart-block">
              <ResponsiveContainer width="100%" height={240}>
                <PieChart>
                  <Pie
                    data={pieData}
                    cx="50%"
                    cy="50%"
                    label={false}
                    outerRadius={90}
                    fill="#8884d8"
                    dataKey="value"
                  >
                    {pieData.map((entry, index) => (
                      <Cell key={`cell-${index}`} fill={entry.color} />
                    ))}
                  </Pie>
                  <Tooltip formatter={(value) => `${value} issue(s)`} />
                  <Legend verticalAlign="bottom" height={24} iconType="circle" />
                </PieChart>
              </ResponsiveContainer>
            </div>

            <div className="trend-chart">
              <div className="trend-chart-header">
                <h3>7-day findings trend</h3>
                <span>{trendData.reduce((sum, item) => sum + item.total, 0)} findings</span>
              </div>
              <ResponsiveContainer width="100%" height={150}>
                <LineChart data={trendData} margin={{ top: 8, right: 0, left: 0, bottom: 0 }}>
                  <CartesianGrid stroke="rgba(148,163,184,0.1)" strokeDasharray="3 3" />
                  <XAxis dataKey="label" axisLine={false} tickLine={false} tick={{ fill: '#94a3b8', fontSize: 12 }} />
                  <YAxis axisLine={false} tickLine={false} tick={{ fill: '#94a3b8', fontSize: 12 }} width={28} />
                  <Tooltip formatter={(value) => `${value} issues`} />
                  <Line type="monotone" dataKey="total" stroke="#60a5fa" strokeWidth={3} dot={{ r: 3, fill: '#60a5fa' }} activeDot={{ r: 5 }} />
                </LineChart>
              </ResponsiveContainer>
            </div>
          </div>
        </div>
      </div>

      <div className="summary-row">
        <div className="summary-card total">
          <h2>{findings.length}</h2>
          <p>Total Findings</p>
        </div>
        <div className="summary-card summary-high">
          <h2>{findings.filter(d => d.severity === "HIGH").length}</h2>
          <p>High</p>
        </div>
        <div className="summary-card summary-medium">
          <h2>{findings.filter(d => d.severity === "MEDIUM").length}</h2>
          <p>Medium</p>
        </div>
        <div className="summary-card summary-low">
          <h2>{findings.filter(d => d.severity === "LOW").length}</h2>
          <p>Low</p>
        </div>
      </div>

      {findings.length === 0 && <p className="loading">Loading findings...</p>}

      <div className="panel cards-panel">
        <ul className="cards-grid">
          {filteredData.map((item, index) => (
            <li
              key={index}
              className={`finding-card ${item.severity.toLowerCase()}`}
            >
              <div className="card-header">
                <div>
                  <h3>{item.issue}</h3>
                  <p className="card-meta">{item.service} · {item.resource_id}</p>
                </div>
                <span className={`severity-badge ${item.severity.toLowerCase()}`}>
                  {item.severity}
                </span>
              </div>
              <p className="card-detail">{item.description || item.issue}</p>
              <div className="card-footer">
                <span className="compliance-pill">{item.compliance || 'Compliance mapping unavailable'}</span>
                <span className="card-time">{item.timestamp}</span>
              </div>
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
}

export default App;