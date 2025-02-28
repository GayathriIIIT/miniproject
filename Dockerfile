# Use an official Python runtime as base image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy all files from the current directory to the container's /app directory
COPY . .

# Install dependencies (if any)
RUN pip install --no-cache-dir -r requirements.txt || true

# Run unit tests to ensure code correctness
RUN python -m unittest test_calculator.py

# Set the default command to run the calculator
CMD ["python", "calculator.py"]

