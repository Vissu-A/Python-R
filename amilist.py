import boto3
import sys
import pprint
ec2 = boto3.resource('ec2')
client = boto3.client('ec2')
response = client.describe_images(Owners=['self'])
print("response is: {}".format(response))
print("images: {}".format(response["Images"]))
# for ami in response['Images']:
#     if 'Tags' in ami:
#       name = [tag['Value'] for tag in ami['Tags'] if tag['Key'] == 'Name'][0]
#     else:
#       name = ''
#     print (name, ami['Name'], ami['ImageId'], ami['State'])