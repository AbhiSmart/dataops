def fetch_volume_details(volume):
    result = {}
    all_tags = {}
    attached_instance_ids = {}
    result['volume_type'] = volume.get('VolumeType')
    result['volume_throughput'] = volume.get('Throughput')
    result['volume_create_time'] = volume.get('CreateTime')
    result['volume_encryption'] = volume.get('Encrypted')
    result['volume_kms_key'] = volume.get('KmsKeyId')
    result['volume_size_gb'] = volume.get('Size')
    result['volume_state'] = volume.get('State')
    result['volume_iops'] = volume.get('Iops')
    result['volume_attached_var'] = 0
    if volume.get('Tags'):
        for tag in volume.get('Tags'):
                tag_key = tag['Key']
                tag_value = tag['Value']
                all_tags.update({tag_key:tag_value})
    result['volume_tags'] = all_tags
    if volume.get('Attachments'):
        for attachment in volume.get('Attachments'):
                if (attachment['State'] == "attached"):
                    result['volume_attached_var'] = 1
                result['attached_instance_id'] = attachment.get('InstanceId')
    return result