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
                sh 'echo ${params.URL}'
                sh 'python3 url_checker.py ${params.URL}'
            }
        }
    }
    post {
        always {
            mail to: "cyber.ernests@gmail.com",
            from: 'mariksafinator@gmail.com',
            subject: "Example",
            body: "111"
        }
    }
}