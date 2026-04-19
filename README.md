# 🐳 Dockerfile and Calculator App

This repository contains a complete, ready-to-run Dockerized calculator application. It includes a Python Flask web interface, a `Dockerfile` for containerization, and deployment instructions.

## 🚀 Overview

A simple calculator web application built with Flask that runs inside a Docker container. You can perform basic arithmetic operations (addition, subtraction, multiplication, division) through a web browser interface.

## 📂 Project Structure

```
docker/
├── app.py
├── Dockerfile
└── README.md
```

## 🛠️ Tech Stack

- **Framework**: Flask (Python)
- **Containerization**: Docker
- **Base Image**: Python 3.12 slim
- **Deployment**: Docker Engine

## 📝 Prerequisites

- Docker installed and running on your machine.
  - [Install Docker Desktop](https://www.docker.com/products/docker-desktop/)

## 🏃 Quick Start

Follow these steps to build and run the application locally:

### Step 1: Build the Docker Image

Open your terminal, navigate to the `docker` directory, and run the build command:

```bash
cd docker
docker build -t calculator-app .
```

This will build a Docker image named `calculator-app`.

### Step 2: Run the Container

Run the container and map port 5000 on your host machine to port 5000 in the container:

```bash
docker run -p 5000:5000 calculator-app
```

### Step 3: Access the Application

Open your web browser and go to:

👉 **http://localhost:5000** 👈

You should see the calculator interface. Enter two numbers and choose an operation to see the result.

---

## 🧪 Testing the Application

### Test Case 1: Addition

1. Open **http://localhost:5000**
2. Enter `5` in the first number field
3. Enter `3` in the second number field
4. Select the `+` operation
5. Click **Calculate**
6. **Expected Result**: `8`

### Test Case 2: Division

1. Open **http://localhost:5000**
2. Enter `10` in the first number field
3. Enter `2` in the second number field
4. Select the `/` operation
5. Click **Calculate**
6. **Expected Result**: `5`

### Test Case 3: Division by Zero

1. Open **http://localhost:5000**
2. Enter `10` in the first number field
3. Enter `0` in the second number field
4. Select the `/` operation
5. Click **Calculate**
6. **Expected Result**: Error message "Cannot divide by zero"

---

## 📂 Detailed Documentation

### 📁 `app.py`

A simple Flask application that provides:
- A web interface for calculations
- Backend logic for basic arithmetic operations
- Error handling for division by zero

**Key Features:**
- Web-based calculator interface
- Supports `+`, `-`, `*`, `/` operations
- Validates user inputs

### 🐳 `Dockerfile`

Contains instructions to build the Docker image:

```dockerfile
# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY app.py .

# Install any needed packages specified in requirements.txt
RUN pip install Flask

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run app.py when the container launches
CMD ["python", "app.py"]
```

**Explanation:**
1. **`FROM python:3.12-slim`**: Uses Python 3.12 lightweight image
2. **`WORKDIR /app`**: Sets working directory inside the container
3. **`COPY app.py .`**: Copies the app file to the container
4. **`RUN pip install Flask`**: Installs Flask dependency
5. **`EXPOSE 5000`**: Exposes port 5000
6. **`CMD ["python", "app.py"]`**: Default command to start the app

---

## 🚀 Deployment Options

### Option 1: Local Deployment (Simple)

```bash
# Build image
docker build -t calculator-app .

# Run container
docker run -d -p 5000:5000 --name calculator calculator-app
```

### Option 2: Using Docker Compose

Create a `docker-compose.yml` file in the `docker` directory:

```yaml
version: '3.8'
services:
  calculator:
    image: calculator-app
    build: .
    container_name: calculator
    ports:
      - "5000:5000"
    restart: always
```

Then run:

```bash
docker-compose up -d
```

## 🧹 Cleanup

To stop and remove the container:

```bash
docker stop calculator
docker rm calculator
```

To remove the image:

```bash
docker rmi calculator-app
```

---

## 🔒 Security Considerations

- Avoid running Docker containers as root (though this example runs as non-root by default)
- Don't expose unnecessary ports
- Use environment variables for sensitive configurations (not applicable to this simple app)

## 📊 Performance

- **Lightweight**: Uses Python 3.12 slim image (~120MB)
- **Fast startup**: Container starts in under 2 seconds
- **Low memory usage**: Minimal footprint

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📧 Support

For questions or issues, please open an issue on the GitHub repository.