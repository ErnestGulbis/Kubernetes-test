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
                script {
                    RESULT = sh(
                        script: 'python3 url_checker.py ${URL}',
                        returnStdout: true
                    ).trim()
                }
                sh 'echo RESULT'
                sh 'echo ${RESULT}'
            }
        }
        stage('Sending email') {
            steps {
                sh 'echo ${RESULT} | mail -s "Jenkins Pipeline Job Result" ferrum-ivanko@yandex.ru'
              }
        }
    }
}