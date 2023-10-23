FROM python:3.9.7-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt
# Make port 80 available to the world outside this container
EXPOSE 5000

# Define environment variable
# ENV DATABASE_URL=postgres://myuser:mypassword@db:5432/mydatabase

# Run app.py when the container launches
CMD ["python", "app.py"]
