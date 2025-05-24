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

from typing import Any
import boto3

def fetch_vpcs(region_name: str) -> list[dict[str, Any]]:
    """
    Fetches all VPCs in the given AWS region using Boto3.

    Args:
        region_name (str): The AWS region name (e.g., "us-east-1").

    Returns:
        list[dict[str, Any]]: A list of VPC dictionaries. Each dictionary contains
        'VpcId', 'CidrBlock', and optionally 'Tags'. If 'Tags' is empty or missing,
        a default name is assigned later during Terraform generation.

    Example:
        >>> vpcs = fetch_vpcs("us-east-1")
        >>> isinstance(vpcs, list)
        True
        >>> len(vpcs) == 0 or isinstance(vpcs[0].get("VpcId"), str)
        True
    """
    try:
        ec2 = boto3.client('ec2', region_name=region_name)
        response = ec2.describe_vpcs()
        vpcs = response.get('Vpcs', [])
        if not vpcs:
            print("No VPCs found in the specified region.")
        return vpcs
    except ImportError as e:
        print(f"Error fetching VPCs: {e}")
        return []
