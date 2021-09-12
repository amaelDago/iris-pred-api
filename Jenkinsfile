pipeline {
    agent none 
    stages {
        stage('Build') { 
            agent {
                docker {
                    image 'python:3.8-slim-buster' 
                }
            }
            steps {
                sh 'python tests/test.py' 
            }
        }
    }
}

