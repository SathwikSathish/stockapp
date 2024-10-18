# Stock Data Fetching Flask App

This is a Flask-based web application that fetches stock data using the Stock Data API. It allows users to input a stock symbol and retrieve the latest stock information. The application is containerized using Docker for easy deployment.

## Features
- Fetch real-time stock data by providing a stock symbol.
- User-friendly front-end interface built with HTML and CSS.
- Flask backend for API integration.
- Dockerized application for ease of deployment.

## Requirements

To run this project locally, you will need the following installed:
- Python 3.x
- Flask
- Docker

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/SathwikSathish/stockapp
# This clones the project from the GitHub repository.

cd stockapp
# Changes the current directory to the project directory.

pip install -r requirements.txt
# Installs the required Python packages listed in requirements.txt.

python stock.py
# Starts the Flask server locally. The app will be available at http://127.0.0.1:5000.

- BUILDING WITH DOCKER

docker build -t stockdata-app .
# Builds a Docker image with the tag 'stockdata-app' using the Dockerfile in the current directory.

docker run -d -p 5000:5000 stockdata-app
# Runs the container in detached mode (-d), mapping port 5000 of the container to port 5000 of the host.

http://localhost:5000
#accessing the application










