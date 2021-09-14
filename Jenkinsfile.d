pipeline {
    agent none
    { docker { image 'python:3.8.11', args:'-u root:root' } }
    stages {
        stage('build') { 
            steps {
                sh 'python3 - venv venv'
                sh '. venv/bin/activate'
                sh 'sudo pip  install -r api/requirements.txt ' 
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