# Base Image
FROM python:3-alpine3.15

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install Python dependencies specified in requirements.txt
RUN pip install -r requirements.txt

# Expose port 3003 to allow external access to this port from outside the container
EXPOSE 3003

# Define the command to run when the container starts, in this case, running app.py using Python
CMD python ./app.py