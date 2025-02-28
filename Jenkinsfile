pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "gayathri731/calculator"
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/GayathriIIIT/miniproject.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Unit Tests') {
            steps {
                sh 'python3 -m unittest test_calculator.py'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $DOCKER_IMAGE .'
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withDockerRegistry([ credentialsId: 'docker-hub-credentials', url: 'https://index.docker.io/v1/' ]) {
    sh 'docker push gayathri731/calculator:latest'
}

                }
            }
        }

        stage('Deploy using Ansible') {
            steps {
                sh 'ansible-playbook deploy.yml'
            }
        }
    }
}

