"""
Terraform File Generator Module

This module provides a function to generate a Terraform configuration file for AWS VPCs.
It iterates through a list of VPC dictionaries and constructs Terraform `aws_vpc` resource blocks 
with relevant attributes such as CIDR block and tags.

Dependencies:
- os

Example Usage:
    from terraform_generator import generate_terraform_file

    vpcs = [
        {
            "VpcId": "vpc-12345678",
            "CidrBlock": "10.0.0.0/16",
            "Tags": [{"Key": "Name", "Value": "Development"}]
        }
    ]
    output_path = "terraform/vpc.tf"
    generate_terraform_file(vpcs, output_path)
"""

import os

def generate_terraform_file(vpcs: list[dict[str, any]], output_path: str) -> None:
    """
    Generates a Terraform configuration file for the provided VPCs.

    This function creates a Terraform file that defines `aws_vpc` resources based on 
    the provided VPC data. Each VPC is converted into a separate Terraform resource block, 
    with the CIDR block and tags being dynamically populated.

    Args:
        vpcs (list[dict[str, any]]): A list of dictionaries, each representing a VPC.
            Each dictionary should contain the keys:
                - 'VpcId' (str): The VPC ID.
                - 'CidrBlock' (str): The CIDR block of the VPC.
                - 'Tags' (list[dict[str, str]]): Optional list of tags for the VPC.

        output_path (str): The file path where the Terraform configuration will be saved.

    Returns:
        None

    Raises:
        FileNotFoundError: If the specified output directory does not exist and cannot be created.
        IOError: If there is an error writing to the output file.

    Example:
        >>> vpcs = [
        ...     {
        ...         "VpcId": "vpc-12345678",
        ...         "CidrBlock": "10.0.0.0/16",
        ...         "Tags": [{"Key": "Name", "Value": "Development"}]
        ...     }
        ... ]
        >>> generate_terraform_file(vpcs, "terraform/vpc.tf")
        Terraform file generated at: terraform/vpc.tf
    """
    # Initialize the Terraform content with the provider block
    terraform_content = 'provider "aws" {\n  region = "us-east-1"\n}\n\n'

    for idx, vpc in enumerate(vpcs):
        cidr_block = vpc.get('CidrBlock', '0.0.0.0/0')
        tags = vpc.get('Tags', [])
        name_tag = next((tag['Value'] for tag in tags if tag['Key'] == 'Name'), f"VPC_{idx + 1}")

        # Append the resource block to the Terraform content
        terraform_content += f"""
resource "aws_vpc" "vpc_{idx + 1}" {{
  cidr_block = "{cidr_block}"
  tags = {{
    Name = "{name_tag}"
  }}
}}
        """

    # Ensure the output directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Write the Terraform content to the output file
    with open(output_path, "w", encoding="utf-8") as tf_file:
        tf_file.write(terraform_content)

    print(f"Terraform file generated at: {output_path}")
