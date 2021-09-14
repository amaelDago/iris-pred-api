pipeline {
    agent none 
    stages {
        stage('build') { 
            agent {
                docker {
                    args "--network host -u root:root"
                    image 'python:3.8.11' 
                }
            }
            steps {
                sh 'ls'
                sh 'ls api/'
                sh 'python -m venv venv'
                sh '. venv/bin/activate'
                sh 'pip  install -r api/requirements.txt ' 
                sh 'python tests/test.py'
                sh 'python api/app.py'
            }
        }
        
    }
}
