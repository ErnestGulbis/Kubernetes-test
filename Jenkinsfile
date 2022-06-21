pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps { 
                checkout scm
            }
        }
        stage('Build') {
            steps {
                sh 'cd $WORKSPACE'
                sh 'python3 url_checker.py ${URL}'
            }
        }
        stage('Sending email') {
            steps {
                sh 'cd $WORKSPACE'
                sh 'ls'
                script {
                    RESULT = readFile 'result.txt'
                    echo "${RESULT}"
                }
                script {
                    mail body: "${RESULT}",
                    subject: "Jenkins Pipeline Job Result",
                    to: "ferrum-ivanko@yandex.ru"
                }
              }
        }
    }
}