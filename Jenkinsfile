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
                sh 'cd $WORKSPACE'
                sh 'echo ${URL}'
                sh 'python3 url_checker.py ${URL}'
            }
        }
    }
    post {
        always {
            emailext ( 
                to: "ferrum-ivanko@yandex.ru",
                from: "job@travelline.ru",
                subject: "Example",
                body: "111",
                attachLog: true,
            )
        }
    }
}