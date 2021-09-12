pipeline {
    agent { docker { image 'python:3.8.11' } 
    stages {
        stage('build') { 
            steps {
                sh 'pip install -r requirements.txt ' 
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

