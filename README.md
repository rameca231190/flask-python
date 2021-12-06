# flask-python

# Command to build docker image:
docker build -t hello-world:v1 .

# Command to run docker image:
docker run -dti --name hello-world -p 5000:5000 <image_id >

# Helm command to see the output as yaml file of manifests to be installed.
helm upgrade --install hello-world helm-chart -f helm-chart/vales.yaml -n python-hello --dry-run

# Tag docker image and push it to Dockerhub
docker image tag 0a958dec7556 rameca231190/hello-world:v1
docker push rameca231190/hello-world:v1