pipeline {
    agent any
    environment {
        GITNAME = 'HyunmoBae'
        GITMAIL = 'tsi0520@naver.com'
        GITWEBADD = 'https://github.com/HyunmoBae/fast-code.git'
        GITSSHADD = 'git@github.com:HyunmoBae/fast-code.git'
        GITCREDENTIAL = 'git_cre'
        DOCKERHUB = 'bhm99/fast'
        DOCKERHUBCREDENTIAL = 'docker_cre'
    }

    stages {
        stage('checkout github') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/main']], extensions: [],
                userRemoteConfigs: [[credentialsId: GITCREDENTIAL, url: GITWEBADD]]])
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
        stage('docker image build') {
            steps {
                sh "docker build -t ${DOCKERHUB}:${currentBuild.number} ."
                sh "docker build -t ${DOCKERHUB}:latest ."
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