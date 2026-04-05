import json
import boto3
from datetime import datetime
from utils.alerts import send_email_alert

findings = []

# ---------------- ADD FINDING ----------------
def add_finding(service, issue, severity, resource_id="N/A"):
    finding = {
        "service": service,
        "issue": issue,
        "severity": severity,
        "resource_id": resource_id,
        "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }

    findings.append(finding)

    # 🚨 Trigger alerts for HIGH severity
    if severity == "HIGH":
        alert_msg = f"""
🚨 CLOUD SECURITY ALERT

Service: {service}
Issue: {issue}
Resource: {resource_id}
Severity: {severity}
Time: {finding['timestamp']}
"""
        send_email_alert(alert_msg)


# ---------------- GENERATE REPORTS ----------------
def generate_reports():
    output_path = "/tmp"

    # JSON report
    json_path = f"{output_path}/report.json"
    with open(json_path, "w") as f:
        json.dump(findings, f, indent=4)

    # TXT report
    txt_path = f"{output_path}/report.txt"
    with open(txt_path, "w") as f:
        for item in findings:
            f.write(f"{item}\n")

    print("✅ Reports generated in /tmp folder")

    # 🚀 Upload to S3
    upload_to_s3(json_path, txt_path)


# ---------------- S3 UPLOAD ----------------
def upload_to_s3(json_path, txt_path):
    s3 = boto3.client('s3')

    bucket_name = "cloud-security-reports-anamika"  # 🔴 CHANGE THIS

    s3.upload_file(json_path, bucket_name, "reports/report.json")
    s3.upload_file(txt_path, bucket_name, "reports/report.txt")

    print("☁️ Reports uploaded to S3 successfully")


# ---------------- SUMMARY ----------------
def print_summary():
    severity_count = {"HIGH": 0, "MEDIUM": 0, "LOW": 0}

    for item in findings:
        severity_count[item["severity"]] += 1

    print("\n📊 Security Summary:")
    print("="*40)
    print(f"🔴 HIGH   : {severity_count['HIGH']}")
    print(f"🟠 MEDIUM : {severity_count['MEDIUM']}")
    print(f"🟢 LOW    : {severity_count['LOW']}")
    print("="*40)

    print(f"\nTotal Issues Found: {len(findings)}")

    # ✅ ADD THIS PART (VERY IMPORTANT)
    print("\n📋 Detailed Findings:")
    print("="*50)

    for item in findings:
        print(f"""
🔹 Service   : {item['service']}
🔹 Issue     : {item['issue']}
🔹 Resource  : {item['resource_id']}
🔹 Severity  : {item['severity']}
🔹 Compliance: {', '.join(item.get('compliance', []))}
🔹 Time      : {item['timestamp']}
----------------------------------------
""")

# Note: Do not execute report generation at import time. Use generate_reports() instead.

# Keep only the one upload_to_s3(json_path, txt_path) function defined above.
