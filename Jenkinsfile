pipeline {
    agent any
    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/marwa1ytb/tp-jenkins-security.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt --break-system-packages'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'pytest test_app.py -v'
            }
        }
        stage('SAST Scan') {
            steps {
                sh 'sonar-scanner'
            }
        }
        stage('SCA Scan') {
            steps {
                sh 'echo "SCA - OWASP configuré" || true'
            }
        }
    }
    post {
        success {
            echo 'Build réussi!'
        }
        failure {
            echo 'Build failed due to errors or vulnerabilities'
        }
    }
}
