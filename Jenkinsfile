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
            }
            steps {
                sh 'python api/app.py'
            }
        }
    }
}

