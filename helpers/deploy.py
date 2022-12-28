import subprocess

# Replace [YOUR_PROJECT_ID] with your Google Cloud project ID
project_id = "XXXX"

# Replace [YOUR_REGION] with the region where you want to deploy your Cloud Run service
region = "XXXX"

# Replace [YOUR_SERVICE_NAME] with the name of your Cloud Run service
service_name = "XXXX"

# Replace [YOUR_IMAGE_NAME] with the name of your Docker image
image_name = "XXXX"

# Build the Docker image
subprocess.run(["docker", "build", "-t", image_name, "."])

# Tag the Docker image with the name of your Google Container Registry repository
repository_url = f"gcr.io/{project_id}/{image_name}"
subprocess.run(["docker", "tag", image_name, repository_url])

# Push the Docker image to Google Container Registry
subprocess.run(["gcloud", "auth", "configure-docker"])
subprocess.run(["docker", "push", repository_url])

# Deploy the Docker image to Google Cloud Run
subprocess.run(["gcloud", "run", "deploy", service_name,
                "--image", repository_url,
                "--region", region])