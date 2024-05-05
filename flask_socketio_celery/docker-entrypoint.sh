#!/bin/bash

set -e

# activate our virtual environment here
# source venv/bin/activate

WORKERS=${WORKERS:-2}
LOG_LEVEL=${LOG_LEVEL:-DEBUG}

usage() {
  echo "Usage: $0 [celery|flask]"
  echo "  - flask: start the flask server"
  echo "  - celery: start the celery worker"
}

if [[ "$1" == "celery" ]]; then
  celery -A task_app.task worker --loglevel=$LOG_LEVEL #--concurrency=$WORKERS
elif [[ "$1" == "flask" ]]; then
  gunicorn --worker-class eventlet -w $WORKERS --bind 0.0.0.0:8080 app:app --log-level $LOG_LEVEL
else
  echo "Unknown or missing sub-command: '$1'"
  usage
  exit 1
fi
