pipeline {
    agent any

    stages {
        stage('Checkout Repo') {
            steps {
                git branch: 'main', url: 'https://github.com/virupaksha224/ecommerce-boto3-scripts.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'pip3 install --user boto3'
            }
        }

        stage('Run Scripts') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'aws-credentials', 
                    usernameVariable: 'AWS_ACCESS_KEY_ID', passwordVariable: 'AWS_SECRET_ACCESS_KEY')]) {
                    
                    bat 'python3 Upload.py'
                    bat 'python3 Update.py'
                    bat 'python3 Delete.py'
                    bat 'python3 Monitor.py'
                }
            }
        }
    }
}



