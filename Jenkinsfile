pipeline {
    agent any
    stages {
        stage('Install Dependencies') {
            steps {
                script {
                    sh 'python3 -m venv venv'
                    sh 'source venv/bin/activate && pip install pandas scikit-learn joblib'
                }
            }
        }
        stage('Train Model') {
            steps {
                script {
                    sh 'source venv/bin/activate && python model.py'
                }
            }
        }
    }
}