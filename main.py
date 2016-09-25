import boto3


session = boto3.Session(profile_name='fc')
ec2 = session.resource('ec2', region_name='ap-southeast-2')


for status in ec2.meta.client.describe_instance_status()['InstanceStatuses']:
    print(status)



