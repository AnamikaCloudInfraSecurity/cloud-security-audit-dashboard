import boto3
from utils.report import add_finding

def check_rds_public():
    try:
        rds = boto3.client('rds')

        dbs = rds.describe_db_instances()['DBInstances']

        for db in dbs:
            if db['PubliclyAccessible']:
                add_finding(
                    "RDS",
                    "Publicly Accessible DB",
                    "HIGH",
                    db['DBInstanceIdentifier']
                )
    except Exception:
        pass