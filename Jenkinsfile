pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'docker build -t myapp .'
            }
        }

        stage('Test') {
            steps {
                sh 'docker run -t myapp python -m unittest discover -s tests'
            }
        }

        stage('Deploy') {
            steps {
                sh 'docker tag myapp:latest myregistry.com/myapp:latest'
                sh 'docker push myregistry.com/myapp:latest'
            }
        }
    }
}