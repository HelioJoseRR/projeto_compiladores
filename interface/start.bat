@echo off
REM Minipar Compiler Web Interface Launcher
REM Windows batch file to start the web interface

echo ============================================================
echo   Minipar Compiler - Web Interface Launcher
echo ============================================================
echo.

REM Check if Python is available
py --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python not found!
    echo Please install Python 3.7 or higher
    echo Download from: https://www.python.org/downloads/
    pause
    exit /b 1
)

echo [1/3] Checking Python installation...
py --version
echo.

REM Check if Gradio is installed
py -c "import gradio" >nul 2>&1
if errorlevel 1 (
    echo [2/3] Gradio not found. Installing...
    uv pip install gradio
    echo.
) else (
    echo [2/3] Gradio already installed
    echo.
)

REM Navigate to interface directory
cd /d "%~dp0"

echo [3/3] Starting web interface...
echo.
echo ============================================================
echo   The interface will open in your browser
echo   URL: http://localhost:7860
echo.
echo   Press Ctrl+C to stop the server
echo ============================================================
echo.

REM Start the interface
py app.py

pause
