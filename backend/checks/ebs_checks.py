import boto3
from utils.report import add_finding

def check_ebs():
    try:
        ec2 = boto3.client('ec2')
        volumes = ec2.describe_volumes()['Volumes']

        for vol in volumes:
            if not vol['Encrypted']:
               add_finding(
        "EBS",
        "Unencrypted Volume",
        "MEDIUM",
        vol['VolumeId']
    )
    except Exception:
        pass