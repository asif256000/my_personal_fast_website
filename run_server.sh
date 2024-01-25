#!/bin/bash

# Run FastAPI application in the background and redirect outputs to logs
nohup python3 -m uvicorn src.main:app >> logs/fastapi.log 2>&1 &

# Set up log rotation
logrotate -s logs/logrotate.status -v logs/fastapi_logrotate.conf
