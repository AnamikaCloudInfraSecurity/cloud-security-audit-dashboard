import json
import boto3

def get_reports(event, context):
    print("🔥 API HIT")   # <-- IMPORTANT (for debugging)

    s3 = boto3.client('s3')
    bucket = "cloud-security-reports-anamika"

    try:
        response = s3.get_object(Bucket=bucket, Key="reports/report.json")
        data = json.loads(response['Body'].read().decode('utf-8'))

        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Headers": "*",
                "Access-Control-Allow-Methods": "GET"
            },
            "body": json.dumps(data)
        }

    except Exception as e:
        print("❌ ERROR:", str(e))   # <-- IMPORTANT
        return {
            "statusCode": 500,
            "headers": {
                "Access-Control-Allow-Origin": "*"
            },
            "body": str(e)
        }