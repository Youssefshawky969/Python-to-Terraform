"""
Main Module - AWS VPC Terraform Generator

This module serves as the entry point for the Terraform file generation process.
It utilizes functions to fetch VPC data from AWS and generate a Terraform configuration file
based on the fetched VPCs.

Dependencies:
- utils.vpc_fetcher (fetch_vpcs)
- utils.terraform_generator (generate_terraform_file)

"""

from utils.vpc_fetcher import fetch_vpcs
from utils.terraform_generator import generate_terraform_file


def main() -> None:
    """
        Main Module - AWS VPC Terraform Generator

    This module serves as the entry point for the Terraform file generation process.
    It utilizes functions to fetch VPC data from AWS and generate a Terraform configuration file
    based on the fetched VPCs.

    Dependencies:
    - utils.vpc_fetcher (fetch_vpcs)
    - utils.terraform_generator (generate_terraform_file)

    Example Usage:
        python main.py

    """
    region = "us-east-1"
    terraform_output_path = "terraform/vpc.tf"
    # Fetch VPCs
    vpcs = fetch_vpcs(region)
    if not vpcs:
        return
    # Generate Terraform file
    generate_terraform_file(vpcs, terraform_output_path)


if __name__ == "__main__":
    main()
