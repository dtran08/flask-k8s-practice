Practice project to brush up on Docker/K8s knowledge, as well as learn how to create Flask endpoints.

Credits to auth0 blog (https://auth0.com/blog/developing-restful-apis-with-python-and-flask/) for source code.

Steps to run:
`docker build -t cashman .`\
`kubectl apply -f deployment.yml`\
`kubectl apply -f service.yml`\
In another terminal window: `minikube tunnel`\
`kubectl get service`\

Get the EXTERNAL-IP from `kubectl get service` and go to http://external_ip:5000/request_here to see GET results