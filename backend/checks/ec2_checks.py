import boto3
from utils.report import add_finding

def check_ec2():
    try:
        ec2 = boto3.client('ec2')
        groups = ec2.describe_security_groups()['SecurityGroups']

        for sg in groups:
            for perm in sg['IpPermissions']:
                for ip in perm.get('IpRanges', []):
                    if ip.get('CidrIp') == '0.0.0.0/0':
                        add_finding("EC2", f"Open Security Group: {sg['GroupName']}", "HIGH")
    except Exception:
        pass