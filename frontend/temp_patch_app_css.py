from pathlib import Path
path = Path(r'D:\Job\Cloud Security Audit Project\cloud-security-dashboard\src\App.css')
text = path.read_text(encoding='utf-8')
old = '''.cards-panel { padding: 24px !important; }

.cards-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 20px;
  margin-bottom: 0;
}

@media (max-width: 860px) {
  .cards-grid { grid-template-columns: 1fr; }
}

.finding-card {
  background: rgba(15, 23, 42, 0.92) !important;
  border-radius: 22px;
  padding: 24px;
  border: 1px solid rgba(148, 163, 184, 0.12) !important;
}

.finding-card:hover {
  transform: translateY(-6px);
  box-shadow: 0 30px 70px rgba(15, 23, 42, 0.26) !important;
}

.card-header {
  display: flex;
  justify-content: space-between;
  gap: 14px;
  align-items: flex-start;
  margin-bottom: 18px;
  padding-bottom: 16px;
  border-bottom: 1px solid rgba(148, 163, 184, 0.12) !important;
}

.card-header h3 {
  margin: 0;
  font-size: 1.1rem;
  color: #f8fafc;
}
'''
new = '''.cards-panel { padding: 18px !important; }

.cards-list {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.cards-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 20px;
  margin-bottom: 0;
}

@media (max-width: 860px) {
  .cards-grid { grid-template-columns: 1fr; }
}

.finding-card {
  background: rgba(15, 23, 42, 0.95) !important;
  border-radius: 18px;
  padding: 16px 18px;
  border: 1px solid rgba(148, 163, 184, 0.14) !important;
  box-shadow: 0 12px 28px rgba(15, 23, 42, 0.18);
}

.finding-card:hover {
  box-shadow: 0 18px 36px rgba(15, 23, 42, 0.22) !important;
}

.card-header {
  display: flex;
  justify-content: space-between;
  gap: 12px;
  align-items: flex-start;
  margin-bottom: 12px;
  padding-bottom: 12px;
  border-bottom: 1px solid rgba(148, 163, 184, 0.1) !important;
}

.card-header h3 {
  margin: 0;
  font-size: 1rem;
  color: #f8fafc;
}
'''
replaced = 0
if old in text:
    text = text.replace(old, new)
    replaced = 1
else:
    print('Old block not found')
path.write_text(text, encoding='utf-8')
print('Replaced', replaced)
