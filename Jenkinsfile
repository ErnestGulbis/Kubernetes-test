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
            }
        }
        stage('Sending email') {
            steps {
                sh 'cd $WORKSPACE'
                sh 'ls'
                script {
                    currentBuild.result = readFile 'result.txt'
                    echo "${currentBuild.result}"
                }
                sh 'echo ${currentBuild.result} | mail -s "Jenkins Pipeline Job Result" ferrum-ivanko@yandex.ru'
              }
        }
    }
}