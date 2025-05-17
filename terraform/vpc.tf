provider "aws" {
  region = "us-east-1"
}


resource "aws_vpc" "vpc_1" {
  cidr_block = "172.31.0.0/16"
  tags = {
    Name = "VPC_1"
  }
}
        