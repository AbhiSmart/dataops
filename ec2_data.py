from functools import reduce


def fetch_instance_details(instance):
    result = {}
    all_tags = {}
    result['image_id'] = instance.get('ImageId')
    result['instance_type'] = instance.get('InstanceType')
    result['instance_launch_time'] = instance.get('LaunchTime')
    result['instance_az'] = instance.get('Placement').get('AvailabilityZone')
    result['instance_private_dns_name'] = instance.get('PrivateDnsName')
    result['instance_private_ipv4'] = instance.get('PrivateIpAddress')
    result['instance_public_ipv4'] = instance.get('PublicIpAddress')
    result['instance_state'] = instance.get('State').get('Name')
    result['instance_subnet_id'] = instance.get('SubnetId')
    result['instance_vpc_id'] = instance.get('VpcId')
    if instance.get('Tags'):
        for tag in instance.get('Tags'):
                tag_key = tag['Key']
                tag_value = tag['Value']
                all_tags.update({tag_key:tag_value})
    result['instance_tags'] = all_tags
    result['instance_core_count'] = instance.get('CpuOptions').get('CoreCount')
    result['instance_threads_per_core'] = instance.get('CpuOptions').get('ThreadsPerCore')
    return result

    
    