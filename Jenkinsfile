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
        stage('Sending email') {
            node() {
                sh 'echo "Test Jenkins Pipeline job Email" | mail -s "Test" ferrum-ivanko@yandex.ru'
              }
        }
    }
    post {
        always {
            emailext ( 
                to: "ferrum-ivanko@yandex.ru",
                subject: "Jenkins Pipeline Job Result",
                body: "12345",
                attachLog: true,
            )
        }
    }
}