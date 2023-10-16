# Project: AirBnB Clone Web Server Configuration

## Task 1: Setting Up Development Environment

### Requirements:
- Ensure completion of Task #3 in the SSH project for web-01.
- Install the net-tools package: `sudo apt install -y net-tools`
- Git clone AirBnB_clone_v2 on web-01.
- Configure `web_flask/0-hello_route.py` to serve content from `/airbnb-onepage/` on port 5000.
  - Flask application object must be named `app`.

## Task 2: Production Environment Setup with Gunicorn

### Requirements:
- Install Gunicorn and required libraries.
- Flask application object should be named `app`.
- Serve content from the same route as in Task 1 on port 5000.
- Checker will bind a Gunicorn instance to port 6000 for verification.

## Task 3: Configure Nginx for Task 2

### Requirements:
- Nginx must serve content locally and on public IP on port 80.
- Proxy requests to the process listening on port 5000.
- Include Nginx config file as `2-app_server-nginx_config`.
- Reboot server to make Nginx publicly accessible.

## Task 4: Handling Multiple Services with Gunicorn and Nginx

### Requirements:
- Git clone AirBnB_clone_v2.
- Configure Nginx to proxy requests to `/airbnb-dynamic/number_odd_or_even/(any integer)` to a Gunicorn instance on port 5001.
- Include Nginx config file as `3-app_server-nginx_config`.

## Task 5: Serve AirBnB Clone v3 - RESTful API

### Requirements:
- Git clone AirBnB_clone_v3.
- Setup Nginx to point /api/ to a Gunicorn instance on port 5002.
- Nginx must serve content both locally and on public IP on port 80.
- Gunicorn should be bound to `api/v1/app.py`.
- Upload Nginx config file as `4-app_server-nginx_config`.

## Task 6: Serve AirBnB Clone v4 - Web Dynamic

### Requirements:
- Git clone AirBnB_clone_v4.
- Gunicorn to serve content from `web_dynamic/2-hbnb.py` on port 5003.
- Configure Nginx to serve the route / and static assets properly.
- Ensure Nginx serves content both locally and on public IP on port 5003.
- Update IP in `web_dynamic/static/scripts/2-hbnb.js`.
- Upload Nginx config as `5-app_server-nginx_config`.

## Task 7: Systemd Script for Gunicorn

### Requirements:
- Write a systemd script for Gunicorn to serve content from `web_dynamic/2-hbnb.py`.
- Gunicorn should spawn 3 worker processes.
- Log errors in `/tmp/airbnb-error.log` and access in `/tmp/airbnb-access.log`.
- Bind to port 5003.
- Upload `gunicorn.service` to GitHub.

## Task 8: Bash Script for Graceful Gunicorn Reload

### Requirements:
- Write a Bash script to reload Gunicorn gracefully.

