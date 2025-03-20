pipeline {
    agent any
    stages {
        stage('Install Dependencies') {
            steps {
                script {
                    sh 'pip install pandas scikit-learn joblib'
                }
            }
        }
        stage('Train Model') {
            steps {
                script {
                    sh 'python model.py'
                }
            }
        }
    }
}