# 🔐 Cloud Security Audit & Monitoring System

A serverless cloud security platform that automates AWS audits and provides real-time visibility into misconfigurations through a web dashboard.

---

## 🚀 Architecture

CloudFront → S3 (Frontend)  
API Gateway → Lambda → S3 (Reports)  
EventBridge → Lambda (Scheduled scans)

---

## 🔍 Features

- Automated security audits for AWS resources (EC2, IAM, S3)
- Detects:
  - Open security groups
  - IAM users without MFA
  - Over-privileged roles
  - Old access keys
- Severity-based classification (HIGH / MEDIUM / LOW)
- Email alerts for critical issues
- React dashboard for visualization
- CDN-enabled deployment using CloudFront
- Secure architecture using private S3 + OAC

---

## 🛠 Tech Stack

- AWS Lambda  
- API Gateway  
- S3  
- EventBridge  
- CloudFront  
- React  

---

## 🔐 Security Highlights

- Private S3 bucket (no public access)
- CDN integration using Amazon CloudFront
- Origin Access Control (OAC) for secure access
- HTTPS enabled

---

## 📊 Dashboard Preview

![Dashboard](docs/dashboard.png)
---
## Live Demo

Cloudfront - https://dig0uirih7yz4.cloudfront.net
---

## ⚙️ Setup Instructions

### Backend
1. Deploy Lambda function
2. Configure IAM roles and permissions
3. Connect API Gateway
4. Enable EventBridge trigger

### Frontend
1. Run `npm install`
2. Run `npm start`
3. Build using `npm run build`
4. Deploy to S3 and serve via CloudFront

---

## 📈 Future Enhancements

- Real-time alerts (WebSocket)
- Compliance mapping (CIS, ISO)
- Multi-account support
- Cognito authentication
- WAF integration

---

## 👩‍💻 Author

Anamika Awasthi
