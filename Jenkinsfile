pipeline {
    agent { docker { image 'golang:1.21.3-alpine3.18' } }
    stages {
        stage('build') {
            steps {
                sh 'go version'
                sh 'echo "hello"'
                sh 'mkdir direct'
                sh 'cd direct'
                sh 'pwd'
            }
        }
    }
}
