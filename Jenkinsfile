pipeline {
    agent none 
    stages {
        stage('build') { 
            agent {
                docker {
                    image 'python:3.8.11' 
                }
            }
            steps {
                sh 'virtualenv venv --distribute'
                sh '. venv/bin/activate'
                sh 'sudo -H pip install -r api/requirements.txt '
            }
        }
        stage('test') {
            steps {
                sh 'python tests/test.py'
            }
        }
        stage('app') {
            steps {
                sh 'python api/app.py'
            }
        }
        
    }
}