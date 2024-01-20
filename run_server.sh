#!/bin/bash

# Run FastAPI application in the background and redirect outputs to logs
nohup uvicorn src:main:app --log-level warning >> logs/fastapi.log 2>&1 &

# Set up log rotation
logrotate -s logs/logrotate.status -v logs/fastapi_logrotate.conf
