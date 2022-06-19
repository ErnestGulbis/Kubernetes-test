pipeline {
    agent any
    parameters {
        string(defaultValue: "https://www.travelline.ru/", description: 'What URL to check?', name: 'URL')
    }
    stages {
        stage('Checkout') {
            steps { 
                checkout scm
            }
        }
        stage('Build') {
            steps {
                sh 'python3 --version'
                sh 'echo ${params.URL}'
            }
        }
    }
    post {
        always {
            emailext body: "Success",
            to: "cyber.ernests@gmail.com",
            from: 'jenkins@example.com',
            subject: "Example Build: ${env.JOB_NAME} - Success", 
            body: "Success"
        }
    }
}