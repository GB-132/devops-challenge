Set-Content -Path README.md -Value '# Atomity DevOps Take-Home Challenge

This repository contains the solution for the Cloud & DevOps Intern take-home challenge.

## Project Structure
- `intern-task-app/`: Flask web application and Docker configuration.
- `intern-task-terraform/`: Modular Terraform configuration for AWS infrastructure deployment (VPC, EC2, Security Groups).

## Deployment Instructions
1. Navigate to `intern-task-terraform/`.
2. Run `terraform init` to initialize modules and providers.
3. Run `terraform apply` to provision AWS infrastructure.'