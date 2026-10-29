variable "aws_region" {
  type        = string
  default     = "ap-south-2"
  description = "The AWS region to deploy resources into"
}

variable "instance_type" {
  type        = string
  default     = "t3.micro"
  description = "EC2 instance type"
}