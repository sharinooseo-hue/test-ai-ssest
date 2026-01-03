pipeline {
    agent any

    stages {
        stage('AI-Assisted Test Decision') {
            steps {
                echo 'Running AI-assisted regression test prioritization...'
                sh 'python3 scripts/ai_test_prioritizer.py'
            }
        }
    }
}
