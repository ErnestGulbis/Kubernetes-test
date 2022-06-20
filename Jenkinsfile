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
                sh 'script_output=$(python3 url_checker.py ${URL} 2>&1 > /dev/null)'
            }
        }
    }
    post {
        always {
            emailext ( 
                to: "ferrum-ivanko@yandex.ru",
                from: "cyber.ernests@gmail.com",
                subject: "Jenkins Pipeline Job Result",
                body: "12345",
                attachLog: true,
            )
        }
    }
}