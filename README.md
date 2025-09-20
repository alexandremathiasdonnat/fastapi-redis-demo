# FastAPI + Redis Demo (Docker & Kubernetes)

## Description
Bonjour, ceci est projet de démonstration simple :  
- Une API **FastAPI** qui incrémente un compteur.  
- Un **Redis** utilisé comme cache (stocke le compteur).  

---

## Arborescence

fastapi-redis-demo/
├─ app/
│ ├─ main.py # API FastAPI
│ ├─ requirements.txt # Dépendances Python
│ └─ Dockerfile # Image de l'API
├─ docker-compose.yml # Orchestration locale
├─ k8s/ # Manifests Kubernetes
│ ├─ namespace.yaml
│ ├─ redis-deployment.yaml
│ ├─ redis-service.yaml
│ ├─ api-deployment.yaml
│ └─ api-service.yaml
└─ README.md


---

## Exécution locale avec Docker Compose
```bash
docker compose up --build
```
Test : http://localhost:8000/ping

Chaque appel incrémente le compteur :
{"status": "ok", "hits": 1} 

## Build & Push de l’image Docker
```bash
docker build -t alexandremathiasdonnat/fastapi-redis-demo:latest ./app
docker push alexandremathiasdonnat/fastapi-redis-demo:latest
```
## Deploiement de Kubernetes
Activer Kubernetes (Docker Desktop ou Minikube)
Appliquer les manifests :
```bash
kubectl apply -f k8s/
kubectl -n demo get pods,svc
```

