pipeline {
    agent any
    environment {
        dockerImage = ''
        registry = 'nilamdhobale/pythonapp'
        registryCredential = 'dockerhub_id'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/NilamDhobale/simpledjangoproject.git']]])
            }
        }
    
        stage('Build docker image') {
            steps {
                script {
                    dockerImage = docker.build registry
                }
                
            }
        }
        
        stage('Upload Image') {
            steps {    
                script {
                    docker.withRegistry( '', registryCredential ) {
                    dockerImage.push()
                    }
                }
            }
        }
        //Stopping Docker containers for cleaner Docker run
        stage('docker stop container') {
            steps {
               sh 'docker ps -f name=pythonappContainer -q | xargs --no-run-if-empty docker container stop'
               sh 'docker container ls -a -fname=pythonappContainer -q | xargs -r docker container rm'
            }
        }
    
    
    // Running Docker container, make sure port 8096 is opened in 
        stage('Docker Run') {
            steps{
                script {
                    dockerImage.run("-p 3000:3000 --rm --name pythonappContainer")
                }
            }
        }
        
            //stage('Deploy App on k8s') {
                //steps {
                   // sshagent(['k8s']) {
                   // sh "scp -o StrictHostKeyChecking=no nodeconfig.yaml nilam@127.0.1.1:/home/nilam"
                   // script {
                    // try{
                       // sh "ssh nilam@127.0.1.1:/home/nilam kubectl apply -f ."
                   // }catch(error){
                       // sh "ssh nilam@127.0.1.1:/home/nilamkubectl create -f ."
                  //  }
                   // }
                 //}
      
             //}
            //}
    }
}
