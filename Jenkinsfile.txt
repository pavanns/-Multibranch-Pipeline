pipeline {
    agent any

    options {
        timestamps()
        buildDiscarder(logRotator(numToKeepStr: '10'))
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
                echo "Branch: ${env.BRANCH_NAME}"
            }
        }

        stage('Environment Info') {
            steps {
                sh 'echo "Running on: $(hostname)"'
                sh 'docker --version || echo "docker not available on this agent"'
                sh 'pwd && ls -la'
            }
        }

        stage('Test') {
            steps {
                echo 'Placeholder test stage — replace with real test/build steps'
                sh 'echo "Pipeline is working for branch: ${BRANCH_NAME}"'
            }
        }
    }

    post {
        success {
            echo "✅ Build succeeded on branch ${env.BRANCH_NAME}"
        }
        failure {
            echo "❌ Build failed on branch ${env.BRANCH_NAME}"
        }
        always {
            cleanWs()
        }
    }
}