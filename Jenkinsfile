pipeline {
    agent any
    stages {
        stage('Install Dependencies') {
            steps {
                script {
                    sh 'bash -c "python3 -m venv venv && source venv/bin/activate && pip install pandas scikit-learn joblib"'
                }
            }
        }
        stage('Train Model') {
            steps {
                script {
                    sh 'bash -c "source venv/bin/activate && python model.py"'
                }
            }
        }
    }
}