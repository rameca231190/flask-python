/*
    Helm install
 */
def helmInstall () {
    withCredentials([kubeconfigContent(credentialsId: "${KUBE_CREDENTIALS}", variable: 'KUBECONFIG_CONTENT')]){
    echo "Installing ${APP_NAME} in ${NAMESPACE}"
    script {
        release = "${APP_NAME}-${NAMESPACE}"
        sh """
            cat <<-EOF > kubeconfig
			${KUBECONFIG_CONTENT}
			EOF
        """
        sh """
            helm upgrade --install ${APP_NAME} -f helm-chart/values.yaml  helm-chart/. --namespace ${NAMESPACE} --kubeconfig=kubeconfig
            rm -rf kubeconfig
        """
        sh "sleep 5"
    }
 }
}

pipeline{
    agent{
        label "<SPECIFY_JENKINS_AGENT_HERE>"
    }
    environment {
        //be sure to replace env based on yours
        APP_NAME = "hello-world"
        VERSION = "v1"
        DOCKER_REGISTRY = "<SPECIFY_DOCKER_REGISTRY_HERE>"
        NAMESPACE = 'python-hello'
    }
    stages{
        stage("Build Docker Image"){
            steps{
                withCredentials([usernamePassword(credentialsId: 'docker-credentials', usernameVariable: 'username', passwordVariable: 'password')]){

                sh'''
                   docker login -u ${username} -p ${password} ${DOCKER_REGISTRY}
                   docker build -t ${APP_NAME} .
                '''
                }
            }
        }
        stage("Push Image"){
           steps{
               script{
                   env.IMAGE_TAG = "${VERSION}".trim() + "_" + "${env.BUILD_ID}".trim()
                   env.IMAGE_NAME = "${DOCKER_REGISTRY}/${APP_NAME}:${IMAGE_TAG}"
                   sh '''
                     docker tag ${APP_NAME} ${IMAGE_NAME}
                     docker push ${IMAGE_NAME}
                     docker rmi ${IMAGE_NAME}
                   '''
               }
               
           }
        }
        stage("Deploy to k8s"){
           environment{
               KUBE_CREDENTIALS = "<SPECIFY_KUBECONFIFG_CREDS_WHICH_IS_STORED_IN_JENKINS_HERE>"
               TARGET_ENV = "qa"
           }
          steps{
              script{
                  env.KUBE_NAMESPACE = "${NAMESPACE}".trim()+'-'+"${TARGET_ENV}".trim()
				  echo "Kube Namespace: ${NAMESPACE}"
                  echo "Deploying application ${APP_NAME} to ${NAMESPACE} namespace"
                  helmInstall()
              }
          }
        }
       
        } 
    }
