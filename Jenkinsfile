pipeline {
    agent any
    
    stages {
        stage('Install Dependencies') {
            steps {
                script {
                    sh """
                    set -e
                    set -x
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install pandas scikit-learn joblib
                    """
                }
            }
        }
        
        stage('Train Model') {
            steps {
                script {
                    sh """
                    . venv/bin/activate
                    python model.py
                    """
                }
            }
        }
    }
}