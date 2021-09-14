pipeline {
    agent none 
    stages {
        stage("Fix the permission issue") {
            agent any
            steps {
                sh "sudo chown root:jenkins /run/docker.sock"
            }
        }
        stage('build') { 
            agent {
                docker {
                    image 'python:3.8.11' 
                }
            }
            steps {
                sh "ls"
                sh 'python -m venv venv'
                sh '. venv/bin/activate'
                sh 'pip  install -r api/requirements.txt ' 
                sh 'python tests/test.py'
                sh 'python app.py'
            }
        }
        
    }
}
