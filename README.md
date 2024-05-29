# Project Setup Guide

This guide will help you clone and run the project using Docker.

## Prerequisites

Ensure you have the following installed on your system:

- Git
- Docker

## Clone the Project

First, clone the project from GitHub:

```bash
git clone git@github.com:thancode99382/DoAnTKHDT.git
```

## Change Directory
```bash
cd DoAnTKHDT
```

## Build the Docker Image
```shell
docker build -t doantkhdt .
```

## Run the Docker Container
```shell
docker run -d -p 5000:5000 doantkhdt
```

## Access the Application
Open your browser and navigate to `http://localhost:8000` to access the application.