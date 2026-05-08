#!/bin/bash

# Simple script to run frontend and backend concurrently

# Function to kill child processes on exit
cleanup() {
    echo "Shutting down..."
    kill $BACKEND_PID $FRONTEND_PID
    exit
}

trap cleanup SIGINT SIGTERM

echo "Starting Backend..."
(cd backend && make run) &
BACKEND_PID=$!

echo "Starting Frontend..."
(cd frontend && npm run dev) &
FRONTEND_PID=$!

wait
