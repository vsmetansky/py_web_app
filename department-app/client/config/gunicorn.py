"""Declares Gunicorn configuration."""

import multiprocessing
import os

bind = 'localhost:7000'
backlog = 2048

workers = multiprocessing.cpu_count() * 2 + 1
worker_class = 'gthread'
timeout = 30
keepalive = 2

logconfig_dict = {
    'version': 1,
    'loggers': {
        'gunicorn.error': {
            'level': 'DEBUG',
            'handlers': ('file', 'console')
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout',
            'formatter': 'generic'
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.environ['LOG_DIR'],
            'formatter': 'generic'
        }
    }
}
