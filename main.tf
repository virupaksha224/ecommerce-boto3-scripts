# main.tf

provider "aws" {
  region = "us-east-1"
}

resource "aws_s3_bucket" "product_images" {
  bucket = "Products_Image_bucket_Casestudy"  # Replace with globally unique name
  versioning {
    enabled = true
  }
  lifecycle_rule {
    enabled = true
    expiration {
      days = 30
    }
  }
}

resource "aws_dynamodb_table" "products" {
  name           = "Products"
  billing_mode   = "PAY_PER_REQUEST"
  hash_key       = "ProductID"

  attribute {
    name = "ProductID"
    type = "S"
  }
}

resource "aws_instance" "app_server" {
  ami           = "ami-02b3c03c6fadb6e2c"  # Amazon Linux 2 AMI in us-east-1
  instance_type = "t3.micro"
  key_name      = "my-ec2-key"   # Replace with your EC2 key pair name

  tags = {
    Name = "EcommerceAppInstance"
  }
}

resource "aws_ebs_volume" "app_volume" {
  availability_zone = aws_instance.app_server.availability_zone
  size              = 8
  type              = "gp2"
  tags = {
    Name = "AppVolume"
  }
}

resource "aws_volume_attachment" "ebs_attach" {
  device_name = "/dev/xvdf"
  volume_id   = aws_ebs_volume.app_volume.id
  instance_id = aws_instance.app_server.id
}
