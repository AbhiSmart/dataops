import boto3
import json
from datetime import date
from operations.ec2_data import fetch_instance_details
from operations.ebs_data import fetch_volume_details


def lambda_handler(event, context):

    ec2_client = boto3.client('ec2')

    # paginator to iterate over the results 
    paginator = ec2_client.get_paginator('describe_instances')
    page_iterator = paginator.paginate()
    ec2_result = {}
    for page in page_iterator:
        for reservation in page['Reservations']:
            for instance in reservation['Instances']:
                instance_id = instance.get('InstanceId')
                ec2_result[instance_id] = fetch_instance_details(instance)
    print(ec2_result)
                
    # paginator to iterate over the results 
    paginator = ec2_client.get_paginator('describe_volumes')
    page_iterator = paginator.paginate()
    ebs_result = {}
    for page in page_iterator:
        for volume in page['Volumes']:
            volume_id = volume.get('VolumeId')
            ebs_result[volume_id] = fetch_volume_details(volume)
    print(ebs_result)

if __name__ == '__main__':
    lambda_handler(None, None)
