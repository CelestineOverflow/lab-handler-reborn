@echo off
:: Open API Docs
start chrome http://localhost:6969/docs
:: Start API Server
python -m uvicorn main:app --reload --port 6969 --host localhost

