"""
AWS VPC Fetcher Module

This module provides a function to fetch VPCs in a specified AWS region using Boto3.
It retrieves all VPCs and returns a list of dictionaries containing VPC details.

Dependencies:
- boto3

Example Usage:
    from vpc_fetcher import fetch_vpcs

    vpcs = fetch_vpcs('us-east-1')
    print(vpcs)
"""

import boto3

def fetch_vpcs(region_name: str) -> list[dict[str, any]]:
    """
    Fetches all VPCs in the specified AWS region.

    This function connects to the AWS EC2 service using Boto3 and retrieves information
    about all VPCs in the specified region. It returns a list of VPC dictionaries, each 
    containing the VPC ID, CIDR block, and associated tags.

    Args:
        region_name (str): The AWS region to query (e.g., 'us-east-1').

    Returns:
        list[dict[str, any]]: A list of dictionaries, each representing a VPC. 
        Each dictionary contains information such as VpcId, CidrBlock, and Tags.

    Raises:
        boto3.exceptions.Boto3Error: If the Boto3 client fails to connect or retrieve data.

    Example:
        >>> vpcs = fetch_vpcs('us-east-1')
        >>> print(vpcs)
        [
            {
                'VpcId': 'vpc-12345678',
                'CidrBlock': '10.0.0.0/16',
                'Tags': [{'Key': 'Name', 'Value': 'Development'}]
            },
            {
                'VpcId': 'vpc-87654321',
                'CidrBlock': '192.168.0.0/24',
                'Tags': [{'Key': 'Environment', 'Value': 'Production'}]
            }
        ]
    """
    ec2 = boto3.client('ec2', region_name=region_name)
    response = ec2.describe_vpcs()
    vpcs = response.get('Vpcs', [])
    
    return vpcs
