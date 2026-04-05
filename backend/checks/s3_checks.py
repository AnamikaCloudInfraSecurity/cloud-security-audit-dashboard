import boto3
from utils.report import add_finding

def check_s3():
    s3 = boto3.client('s3')
    buckets = s3.list_buckets()['Buckets']

    for bucket in buckets:
        name = bucket['Name']
        try:
            acl = s3.get_bucket_acl(Bucket=name)
            for grant in acl['Grants']:
                if 'AllUsers' in str(grant):
                    add_finding("S3", f"Public bucket: {name}", "HIGH")
        except:
            pass