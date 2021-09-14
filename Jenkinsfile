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
                sh "pip install virtualenv"
                sh 'virtualenv venv --distribute'
                sh '. venv/bin/activate'
                sh 'sudo -H pip  install -r api/requirements.txt ' 
                sh 'python tests/test.py'
                sh 'python app.py'
            }
        }
        
    }
}
