import boto3
from datetime import datetime, timezone
from utils.report import add_finding

def check_iam():
    try:
        iam = boto3.client('iam')

        users = iam.list_users()['Users']

        for user in users:
            username = user['UserName']

            # ---------------- MFA CHECK ----------------
            mfa_devices = iam.list_mfa_devices(UserName=username)['MFADevices']
            if len(mfa_devices) == 0:
                add_finding(
                    service="IAM",
                    issue="User without MFA",
                    severity="HIGH",
                    resource_id=username
                )

            # ---------------- ADMIN ACCESS CHECK ----------------
            attached_policies = iam.list_attached_user_policies(UserName=username)['AttachedPolicies']
            
            for policy in attached_policies:
                if policy['PolicyName'] == 'AdministratorAccess':
                    add_finding(
                        service="IAM",
                        issue="User has AdministratorAccess policy",
                        severity="HIGH",
                        resource_id=username
                    )

            # ---------------- ACCESS KEY AGE CHECK ----------------
            access_keys = iam.list_access_keys(UserName=username)['AccessKeyMetadata']
            
            for key in access_keys:
                create_date = key['CreateDate']
                age_days = (datetime.now(timezone.utc) - create_date).days

                if age_days > 90:
                    add_finding(
                        service="IAM",
                        issue=f"Old Access Key (>90 days)",
                        severity="MEDIUM",
                        resource_id=username
                    )
    except Exception:
        pass