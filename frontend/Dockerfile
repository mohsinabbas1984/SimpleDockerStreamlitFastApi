# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory in the container to /app/frontend
WORKDIR /app/frontend

# Copy the current directory contents into the container at /app/frontend
COPY . /app/frontend

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8501 available to the world outside this container
EXPOSE 8501

# Define environment variable (optional)
ENV NAME Frontend

# Run Streamlit (Corrected filename)
CMD ["streamlit", "run", "/app/frontend/streamlit_app.py"]  # Note the underscore
