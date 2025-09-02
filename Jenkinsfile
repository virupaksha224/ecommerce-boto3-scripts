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
                sh 'pip3 install --user boto3'
            }
        }

        stage('Run Scripts') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'aws-credentials', 
                    usernameVariable: 'AWS_ACCESS_KEY_ID', passwordVariable: 'AWS_SECRET_ACCESS_KEY')]) {
                    
                    sh 'python3 Upload.py'
                    sh 'python3 Update.py'
                    sh 'python3 Delete.py'
                    sh 'python3 Monitor.py'
                }
            }
        }
    }
}


