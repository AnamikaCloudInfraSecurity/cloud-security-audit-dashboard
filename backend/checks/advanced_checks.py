import boto3
from utils.report import add_finding
from datetime import datetime, timedelta

# 🔹 S3 Public Bucket Check
def check_s3_public():
    s3 = boto3.client('s3')
    buckets = s3.list_buckets()['Buckets']

    for bucket in buckets:
        bucket_name = bucket['Name']

        try:
            acl = s3.get_bucket_acl(Bucket=bucket_name)

            for grant in acl['Grants']:
                if 'URI' in grant['Grantee']:
                    if 'AllUsers' in grant['Grantee']['URI']:
                        add_finding(
                            "S3",
                            f"Public Bucket: {bucket_name}",
                            "HIGH",
                            bucket_name
                        )
        except Exception:
            pass


# 🔹 IAM Old Access Keys (>90 days)
def check_old_access_keys():
    iam = boto3.client('iam')
    users = iam.list_users()['Users']

    for user in users:
        username = user['UserName']
        keys = iam.list_access_keys(UserName=username)['AccessKeyMetadata']

        for key in keys:
            create_date = key['CreateDate'].replace(tzinfo=None)
            if datetime.now() - create_date > timedelta(days=90):
                add_finding(
                    "IAM",
                    f"Old Access Key (>90 days)",
                    "MEDIUM",
                    username
                )


# 🔹 EBS Encryption Check
def check_ebs_encryption():
    ec2 = boto3.client('ec2')
    volumes = ec2.describe_volumes()['Volumes']

    for vol in volumes:
        if not vol['Encrypted']:
            add_finding(
                "EC2",
                "Unencrypted EBS Volume",
                "HIGH",
                vol['VolumeId']
            )