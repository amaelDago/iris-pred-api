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
                sh "./build.sh"
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