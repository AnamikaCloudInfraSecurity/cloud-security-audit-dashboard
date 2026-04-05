import smtplib
import requests
from email.mime.text import MIMEText

# ---------------- EMAIL ALERT ----------------
def send_email_alert(message):
    sender = "anamika00990@gmail.com"
    receiver = "anamika00990@gmail.com"
    password = "ddig safj uiew dfnb"

    msg = MIMEText(message)
    msg['Subject'] = "🚨 Cloud Security Alert"
    msg['From'] = sender
    msg['To'] = receiver

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(sender, password)
        server.sendmail(sender, receiver, msg.as_string())
        server.quit()
        print("📧 Email alert sent")
    except Exception as e:
        print("Email error:", e)


# ---------------- MICROSOFT TEAMS ALERT ----------------
#def send_teams_alert(message):
   # webhook_url = "YOUR_TEAMS_WEBHOOK_URL"

   # payload = {
    #    "text": message
   # }

#    try:
 #       requests.post(webhook_url, json=payload)
  #      print("💬 Teams alert sent")
   # except Exception as e:
    #    print("Teams error:", e)