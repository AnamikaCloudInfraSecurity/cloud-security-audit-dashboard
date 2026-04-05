from checks.s3_checks import check_s3
from checks.ec2_checks import check_ec2
from checks.iam_checks import check_iam
from checks.ebs_checks import check_ebs
from utils.report import generate_reports, print_summary
import sys
from checks.rds_checks import check_rds_public 
from checks.advanced_checks import check_s3_public, check_old_access_keys, check_ebs_encryption

def run_all():
    print("\n🔐 Running Cloud Security Audit...\n")

    check_s3()
    check_ec2()
    check_iam()
    check_ebs()
    
    check_s3_public()
    check_ebs_encryption()
    check_old_access_keys()
    check_rds_public()
    generate_reports()
    print_summary()
    
    

    


# ---------------- CLI SUPPORT ----------------
def run_service(service):
    print(f"\n🔍 Running check for: {service}\n")

    if service == "s3":
        check_s3()
    elif service == "ec2":
        check_ec2()
    elif service == "iam":
        check_iam()
    elif service == "ebs":
        check_ebs()
    else:
        print("❌ Invalid service name")

    generate_reports()
    print_summary()


# ---------------- MAIN ----------------
if __name__ == "__main__":
    if len(sys.argv) > 1:
        run_service(sys.argv[1])
    else:
        run_all()


# ---------------- LAMBDA HANDLER ----------------
def lambda_handler(event, context):
    run_all()
    return {
        "statusCode": 200,
        "body": "Audit Completed"
    }