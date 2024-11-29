name: test
on:
  push:
    branches:
        - main

env: 
  KUBECONFIG: ${{ secrets.KUBECONFIG}}

jobs:
  deploy:
      runs-on: kubernetes
      steps:
      - name: Checkout code
        uses: actions/checkout@v2

      - name: Create Docker Image
        used: docker/build-push-action@v2
        with:
          context: .
          push: true

      - name: Deploy to k8s
      - uses: appleboy/kubectl-action@v1.0.0
        with: 
          args: apply -f deployment.yaml
          env:
            KUNECONFIG: ${{ env.KUBECONFIG }}
