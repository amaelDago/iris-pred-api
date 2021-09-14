pipeline {
    agent none 
    stages {
        stage('Build') { 
            agent {
                docker {
                    image 'python:3.8.11' 
                }
            }
            steps {
                sh 'python tests/test.py'
                sh "pip install --user -r api/requirements.txt"
                sh 'python app.py'
            }
        }
        
    }
}

