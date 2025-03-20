pipeline {
    agent any
    stages {
        stage('Install Dependencies') {
            steps {
                script {
                    sh """
                    set -e
                    set -x
                    bash -c 'python3 -m venv venv && source venv\Scripts\activate'
                    bash -c  'pip install pandas scikit-learn joblib'
                    """
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