pipeline {
    agent any
    parameters {
        string(defaultValue: "https://www.travelline.ru/", description: 'What URL to check?', name: 'URL')
    }
    stages {
        stage('Checkout') {
            steps {
                // Вытягивавем скрипт средствами git 
                checkout scm
            }
        }
        stage('Build') {
            steps {
                // Переходим в рабочий каталог
                sh 'cd $WORKSPACE'
                // Запускаем python-скрипт, который сохраняет результат в текстовый файл result.txt (success или failure)
                sh 'python3 url_checker.py ${URL}'
            }
        }
        stage('Sending email') {
            steps {
                sh 'cd $WORKSPACE'
                // Читаем результат в переменную и выводим в консоль
                script {
                    RESULT = readFile 'result.txt'
                    echo "${RESULT}"
                }
                // Отправляем результат на почту
                script {
                    mail body: "${RESULT}",
                    subject: "Jenkins Pipeline Job Result",
                    to: "name@domain.com"
                }
              }
        }
    }
}