# AWS VPC Terraform Generator

This tool generates Terraform configuration files for AWS VPCs by fetching VPC data using Boto3. 
The generated file can be used to replicate or manage VPC resources through Terraform.

##  Dependencies

- Python 3.11+
- Boto3
- Black (optional for formatting)
- Pylint (optional for linting)

##  Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/Youssefshawky969/Python-to-Terraform.git
    cd project/
    ```

2. Install the dependencies:

    ```bash
    pip install boto3 black pylint
    ```

3. Configure AWS credentials:

    ```bash
    aws configure
    ```

4. Run the script:

    ```bash
    python main.py
    ```

##  Project Structure
```
project/
├── utils/
│ ├── vpc_fetcher                # VPC fetching logic
│ └── terraform_generator        # Terraform generation logic
├── terraform/
│ └── vpc.tf                     # Generated Terraform file
├── main.py                      # Main entry point
└── README.md                    # Project documentation
```

If VPCs are found, a Terraform file will be generated at `terraform/vpc.tf`.
