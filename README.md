![Logo](https://raw.githubusercontent.com/bmosoluciones/now-lms/main/now_lms/static/icons/logo/logo_small.png)

# NOW - Learning Management System
![PyPI - License](https://img.shields.io/pypi/l/now_lms?color=brightgreen&logo=apache&logoColor=white)
![PyPI](https://img.shields.io/pypi/v/now_lms?color=brightgreen&label=version&logo=python&logoColor=white)
![PyPI - Wheel](https://img.shields.io/pypi/wheel/now_lms?logo=python&logoColor=white)
[![Docker Repository on Quay](https://quay.io/repository/bmosoluciones/now-lms/status "Docker Repository on Quay")](https://quay.io/repository/bmosoluciones/now-lms)
[![codecov](https://codecov.io/gh/bmosoluciones/now-lms/branch/main/graph/badge.svg?token=SFVXF6Y3R3)](https://codecov.io/gh/bmosoluciones/now-lms)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=bmosoluciones_now-lms&metric=alert_status)](https://sonarcloud.io/dashboard?id=bmosoluciones_now-lms)

Simple to {install, use, configure, mantain} learning management system.

## Getting Started

### Dependencies

* Requires python >= 3.7
* Runs on Linux and Windows

### Quick Start

To star a local server just execute:

```
python3 -m venv venv
# Linux:
source venv/bin/activate
# Windows
venv\Scripts\activate.bat
python -m pip install now_lms
python -m now_lms
```

Visit http://127.0.0.1:8080/ in your browser, defaul user and password are `lms-admin`, note that the default server is olny bind to the localhost.

### OCI Image

There is also a OCI image disponible if you prefer to user containers, in this example we use [podman](https://podman.io/):

```
# Install the podman command line tool.
# Fedora, CentOS ...
sudo dnf -y install podman

# Debian, Ubuntu ...
sudo apt install -y podman

# OpenSUSE
sudo zypper in podman

# Create a new pod:
podman pod create --name now-lms -p 8080:8080

# Database:
podman run --pod now-lms --rm --name now-lms-db \
    --volume now-lms-postgresql-backup:/var/lib/postgresql/data \
    -e POSTGRES_DB=nowlearning \
    -e POSTGRES_USER=nowlearning \
    -e POSTGRES_PASSWORD=nowlearning \
    -d postgres:13

# App:
podman run --pod now-lms --rm --init --name now-lms-app \
    -e LMS_KEY=nsjksldknsdlkdsljdnsdjñasññqldñaas554dlkallas \ # Set you own secret and secure key.
    -e LMS_DB=postgresql+pg8000://nowlearning:nowlearning@localhost:5432/nowlearning \ # Set according the database container credentials
    -e LMS_USER=administrator \ # Set your own admin user.
    -e LMS_PSWD=administrator \ # Set your own admin user. 
    -d quay.io/bmosoluciones/now-lms

```

NOW-LMS also will work with MySQL or MariaDB just change the image of the database container and set the correct connect string.
