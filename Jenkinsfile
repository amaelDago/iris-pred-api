pipeline {
    agent { docker { image 'python:3.8.11', args:'-u root:root' } }
    stages {
        stage('build') { 
            steps {
                sh 'virtualvenv venv --distribute'
                sh 'source venv/bin/activate'
                sh 'pip --no-cache-dir  install --user -r api/requirements.txt ' 
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