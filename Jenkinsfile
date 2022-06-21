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
                sh 'script_output=$((python3 url_checker.py https://vk.com) 2>&1)'
                sh 'echo $script_output'
            }
        }
        stage('Sending email') {
            steps {
                sh 'echo ${URL}'
                sh 'echo ${URL} | mail -s "Test" ferrum-ivanko@yandex.ru'
              }
        }
    }
}