@echo off 
echo ======================================== 
echo CI/CD Build Script 
echo ======================================== 
 
echo [1/4] Cleaning old builds... 
rmdir /s /q build 
rmdir /s /q dist 
rmdir /s /q *.egg-info 
 
echo [2/4] Running tests... 
pytest tests/ -v --cov=src --cov-report=term-missing 
if errorlevel 1 exit /b 1 
 
echo [3/4] Building package... 
python -m build 
 
echo [4/4] Build complete! 
dir dist\ 
