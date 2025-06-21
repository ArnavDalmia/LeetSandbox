@echo off
echo Running database seed script...
python scripts/seed_neetcode.py
if %ERRORLEVEL% NEQ 0 (
    echo Error: Seeding failed
    exit /b %ERRORLEVEL%
)
echo Database seeding completed successfully