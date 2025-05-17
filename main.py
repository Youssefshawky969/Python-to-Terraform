"""
Main Module - AWS VPC Terraform Generator

This module serves as the entry point for the Terraform file generation process.
It utilizes functions to fetch VPC data from AWS and generate a Terraform configuration file 
based on the fetched VPCs.

Dependencies:
- utils.function (fetch_vpcs)
- utils.function2 (generate_terraform_file)

Example Usage:
    python main.py
"""

from utils.function import fetch_vpcs
from utils.function2 import generate_terraform_file


def main() -> None:
    """
    Main function to orchestrate the VPC fetching and Terraform file generation process.

    This function performs the following steps:
    1. Fetches VPC data for the specified AWS region.
    2. Checks if VPC data is available.
    3. Generates a Terraform configuration file for the VPCs.

    Args:
        None

    Returns:
        None

    Example:
        >>> python main.py
        Terraform file generated at: terraform/vpc.tf

    Raises:
        FileNotFoundError: If the output directory for the Terraform file cannot be created.
        IOError: If there is an error writing to the output file.
    """
    region = "us-east-1"
    terraform_output_path = "terraform/vpc.tf"
    # Fetch VPCs
    vpcs = fetch_vpcs(region)
    # Check if VPCs are available
    if not vpcs:
        print("No VPCs found in the specified region.")
        return
    # Generate Terraform file
    generate_terraform_file(vpcs, terraform_output_path)


if __name__ == "__main__":
    main()
