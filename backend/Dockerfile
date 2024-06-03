# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory in the container to /app/backend
WORKDIR /app/backend

# Copy the current directory contents into the container at /app
COPY . /app/backend

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port for FastAPI
EXPOSE 8000

# Set environment variable (optional)
ENV NAME Backend

# Run the FastAPI server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
