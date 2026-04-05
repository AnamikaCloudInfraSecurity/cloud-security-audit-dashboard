from pathlib import Path

css = """* {
  box-sizing: border-box;
}

body {
  margin: 0;
  min-height: 100vh;
  font-family: Inter, 'Segoe UI', sans-serif;
  background: radial-gradient(circle at top left, rgba(94, 129, 230, 0.18), transparent 20%),
              radial-gradient(circle at bottom right, rgba(106, 90, 230, 0.14), transparent 18%),
              #060914;
  color: #e2e8f0;
}

html {
  scroll-behavior: smooth;
}

.dashboard-container {
  max-width: 1400px;
  margin: 0 auto;
  padding: 22px 18px;
  display: grid;
  gap: 22px;
}

.top-panel {
  display: grid;
  grid-template-columns: minmax(0, 1.5fr) minmax(280px, 1fr);
  gap: 22px;
  align-items: start;
}

@media (max-width: 1040px) {
  .top-panel {
    grid-template-columns: 1fr;
  }
}

.dashboard-header {
  display: grid;
  gap: 12px;
}

.dashboard-badge {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 6px 12px;
  border-radius: 999px;
  background: rgba(92, 102, 255, 0.18);
  color: #dbeafe;
  font-size: 0.78rem;
  font-weight: 700;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  width: fit-content;
}

.dashboard-title {
  margin: 0;
  font-size: clamp(2rem, 3vw, 2.6rem);
  line-height: 1.05;
  font-weight: 700;
}

.dashboard-subtitle {
  margin: 0;
  max-width: 620px;
  color: #a6b3d6;
  font-size: 0.95rem;
  line-height: 1.6;
}

.search-section {
  width: 100%;
}

.search-input {
  width: 100%;
  padding: 12px 16px;
  border-radius: 14px;
  border: 1px solid rgba(148, 163, 184, 0.22);
  background: rgba(14, 24, 43, 0.95);
  color: #e2e8f0;
  font-size: 0.95rem;
  outline: none;
  box-shadow: inset 0 1px 2px rgba(15, 23, 42, 0.35);
  transition: border-color 0.2s ease, transform 0.2s ease;
}

.search-input::placeholder {
  color: #7b8ba9;
}

.search-input:focus {
  border-color: rgba(79, 70, 229, 0.9);
  transform: translateY(-1px);
}

.filter-bar {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
  align-items: center;
  background: rgba(14, 24, 43, 0.9);
  border: 1px solid rgba(148, 163, 184, 0.16);
  border-radius: 18px;
  padding: 12px 14px;
  margin-top: 8px;
}

.filter-group {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  align-items: center;
}

.filter-group.inline span {
  color: #94a3b8;
  font-size: 0.78rem;
  text-transform: uppercase;
  letter-spacing: 0.12em;
}

.filter-buttons {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}

.filter-btn {
  background: rgba(100, 116, 139, 0.14);
  color: #e2e8f0;
  border: 1px solid transparent;
  padding: 7px 12px;
  border-radius: 999px;
  font-size: 0.82rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s ease;
}

.filter-btn:hover {
  background: rgba(99, 102, 241, 0.18);
}

.filter-btn.active {
  background: linear-gradient(135deg, #5b63ff, #3b82f6);
  box-shadow: 0 10px 24px rgba(59, 130, 246, 0.22);
  color: #fff;
  border-color: rgba(147, 197, 253, 0.25);
}

.summary-row {
  display: grid;
  grid-template-columns: repeat(4, minmax(0, 1fr));
  gap: 14px;
}

@media (max-width: 860px) {
  .summary-row {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }
}

@media (max-width: 640px) {
  .summary-row {
    grid-template-columns: 1fr;
  }
}

.summary-card {
  background: rgba(14, 24, 43, 0.92);
  border: 1px solid rgba(148, 163, 184, 0.14);
  border-radius: 18px;
  padding: 16px 18px;
  box-shadow: 0 14px 32px rgba(0, 0, 0, 0.18);
  display: grid;
  gap: 6px;
}

.summary-card h2 {
  margin: 0;
  font-size: 1.55rem;
  line-height: 1;
}

.summary-card p {
  margin: 0;
  font-size: 0.86rem;
  color: #94a3b8;
}

.summary-card.total {
  background: linear-gradient(135deg, #4f46e5, #2563eb);
  border-color: transparent;
  color: #fff;
}

.chart-panel {
  background: rgba(14, 24, 43, 0.96);
  border: 1px solid rgba(148, 163, 184, 0.18);
  border-radius: 24px;
  padding: 18px;
  box-shadow: 0 24px 60px rgba(0, 0, 0, 0.2);
  display: flex;
  flex-direction: column;
  min-height: 310px;
}

.chart-panel .panel-header {
  gap: 10px;
  margin-bottom: 16px;
}

.chart-panel h2 {
  margin: 0;
  font-size: 1.18rem;
}

.chart-panel p {
  margin: 6px 0 0;
  color: #94a3b8;
  font-size: 0.9rem;
}

.chart-body {
  flex: 1;
}

.cards-panel {
  background: rgba(14, 24, 43, 0.94);
  border: 1px solid rgba(148, 163, 184, 0.16);
  border-radius: 24px;
  padding: 16px;
  box-shadow: 0 20px 50px rgba(0, 0, 0, 0.2);
}

.cards-list {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: 10px;
}

.finding-card {
  background: rgba(10, 16, 30, 0.95);
  border: 1px solid rgba(148, 163, 184, 0.12);
  border-left: 4px solid transparent;
  border-radius: 16px;
  padding: 12px 14px;
  box-shadow: 0 12px 24px rgba(0, 0, 0, 0.18);
  transition: transform 0.18s ease, box-shadow 0.18s ease;
}

.finding-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 16px 28px rgba(0, 0, 0, 0.22);
}

.finding-card.high {
  border-left-color: #ef4444;
}

.finding-card.medium {
  border-left-color: #f59e0b;
}

.finding-card.low {
  border-left-color: #22c55e;
}

.card-top {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  gap: 12px;
}

.card-top h3 {
  margin: 0;
  font-size: 1rem;
}

.card-meta {
  margin: 4px 0 0;
  font-size: 0.82rem;
  color: #7b8ba9;
}

.card-divider {
  height: 1px;
  background: rgba(148, 163, 184, 0.08);
  margin: 10px 0;
}

.card-detail {
  margin: 0;
  color: #d9e1ff;
  font-size: 0.88rem;
  line-height: 1.5;
}

.card-footer {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 10px;
  margin-top: 10px;
}

.card-time {
  font-size: 0.78rem;
  color: #7b8ba9;
}

.compliance-tag {
  padding: 4px 10px;
  border-radius: 999px;
  background: rgba(59, 130, 246, 0.18);
  color: #cbd5e1;
  font-size: 0.78rem;
  border: 1px solid rgba(59, 130, 246, 0.24);
}

.severity-badge {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 6px 12px;
  border-radius: 999px;
  color: #fff;
  font-size: 0.75rem;
  letter-spacing: 0.08em;
  text-transform: uppercase;
}

.severity-badge.high {
  background: linear-gradient(135deg, #ef4444, #dc2626);
}

.severity-badge.medium {
  background: linear-gradient(135deg, #f59e0b, #d97706);
}

.severity-badge.low {
  background: linear-gradient(135deg, #22c55e, #16a34a);
}

.loading {
  padding: 20px 0;
  color: #94a3b8;
  text-align: center;
  font-size: 0.95rem;
}
"""