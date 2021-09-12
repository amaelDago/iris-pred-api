pipeline {
    agent docker { image 'python:3.8-slim-buster'} 
    stages {
        stage('build') {
            steps {
                sh 'pip install -r api/requirements.txt'
            }
        stage('test') {
            steps {
                sh 'python test.py'
            }
        }
        }
    }
}