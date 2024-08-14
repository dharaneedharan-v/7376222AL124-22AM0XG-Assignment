# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /model-app

# Copy the current directory contents into the container at /app
COPY . /model-app/

# Install the necessary dependencies directly in the Dockerfile

RUN pip install --no-cache-dir numpy==1.21.4 scikit-learn==1.0.2 joblib==1.2.0


# Run the script when the container launches
CMD ["python", "app.py"]

EXPOSE 5001