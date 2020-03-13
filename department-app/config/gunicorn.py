"""Declares Gunicorn configuration."""

import multiprocessing

bind = 'localhost:8000'
backlog = 2048

workers = multiprocessing.cpu_count() * 2 + 1
worker_class = 'gthread'
timeout = 30
keepalive = 2

loglevel = 'debug'
errorlog = '-'
