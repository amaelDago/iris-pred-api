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
                sh 'virtualvenv venv --distribute'
                sh '. venv/bin/activate'
                sh 'sudo -H pip  install -r api/requirements.txt ' 
                sh 'python app.py'
            }
        }
        
    }
}

