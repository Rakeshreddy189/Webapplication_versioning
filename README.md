# Webapplication_versioning
Creating the GitHub repo for webapplication project
# My Web App

This is a simple web application with a frontend, backend, and database connectivity. It is containerized using Docker and deployed on a Kubernetes cluster.

## Project Structure

- `frontend/` - Contains HTML, CSS, and JavaScript files.
- `backend/` - Contains Python backend application.
- `deployment/` - Contains Docker and Kubernetes configuration files.
## Create a Dockerfile for frontend and backend
##Build Docker images and containers for frontend and backend:
# Build frontend image
cd frontend
docker build -t my-frontend .

# Build backend image
cd ../backend
docker build -t my-backend .

# Test frontend container
docker run -d -p 8080:80 my-frontend

# Test backend container
docker run -d -p 5000:5000 my-backend
