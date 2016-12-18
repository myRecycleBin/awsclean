import boto3


class EC2Clean:
    def __init__(self, ec2_client=boto3.client('ec2'), auto_scaling_client=boto3.client('autoscaling')):
        self.ec2_client = ec2_client
        self.auto_scaling_client = auto_scaling_client

    def list(self):
        print("Your AutoScaling resources are as below: ")
        self._list_auto_scaling_groups()

    def destroy(self):
        print("Your EC2 resources are to be destroyed ")

    def _list_auto_scaling_groups(self):
        response = self.auto_scaling_client.describe_auto_scaling_groups()
        auto_scaling_groups = response.get('AutoScalingGroups')
        for ag in auto_scaling_groups:
            print(ag.get('AutoScalingGroupName'))


EC2Clean().list()
