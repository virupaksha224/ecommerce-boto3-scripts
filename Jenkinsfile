pipeline {
    agent any

    environment {
        AWS_DEFAULT_REGION = 'us-east-1'
        AWS_ACCESS_KEY_ID     = credentials('aws-credentials').username
        AWS_SECRET_ACCESS_KEY = credentials('aws-credentials').password
    }

    stages {
        stage('Checkout Repo') {
            steps {
                git branch: 'main', url: 'https://github.com/virupaksha224/ecommerce-boto3-scripts.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip3 install --user boto3'
            }
        }

        stage('Run Upload.py') {
            steps {
                sh 'python3 upload.py'
            }
        }

        stage('Run Update.py') {
            steps {
                sh 'python3 update.py'
            }
        }

        stage('Run Delete.py') {
            steps {
                sh 'python3 delete.py'
            }
        }

        stage('Run Monitor.py') {
            steps {
                sh 'python3 monitor.py'
            }
        }
    }

}

