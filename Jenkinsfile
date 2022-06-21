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
                sh 'python3 url_checker.py ${URL}'
                readResult('result.txt')
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
void readResult(String resultFile=""){
    RESULT=readFile(resultFile)
}