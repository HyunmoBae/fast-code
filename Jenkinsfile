pipeline {
    agent any

    stages {
        stage('start') {
            steps {
                echo "hello Jenkins!!!"
            }
            post {
                failure {
                    sh "echo failed"
                }
                success {
                    sh "echo success"
                }
            }
        }
    }
}