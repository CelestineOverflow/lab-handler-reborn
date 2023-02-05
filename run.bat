@echo off
::start the api server in a new window
start cmd /k "title api && cd ./api && run_api.bat"

:: start webapp server in a new window
start cmd /k "title wewbapp &&cd ./webapp && npm run dev -- --port 5656"

:: start the chrome browser
start chrome http://localhost:5656