# Chrono Nexus Protocol - Quick Setup Script
# Run this script to set up the game quickly

Write-Host "🌌 CHRONO NEXUS PROTOCOL - Setup Script" -ForegroundColor Cyan
Write-Host "========================================`n" -ForegroundColor Cyan

# Check if Python is installed
Write-Host "Checking Python installation..." -ForegroundColor Yellow
try {
    $pythonVersion = python --version 2>&1
    Write-Host "✓ Python found: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "❌ Python is not installed or not in PATH" -ForegroundColor Red
    exit 1
}

# Create virtual environment
Write-Host "`nCreating virtual environment..." -ForegroundColor Yellow
if (Test-Path "venv") {
    Write-Host "⚠ Virtual environment already exists, skipping..." -ForegroundColor Yellow
} else {
    python -m venv venv
    Write-Host "✓ Virtual environment created" -ForegroundColor Green
}

# Activate virtual environment
Write-Host "`nActivating virtual environment..." -ForegroundColor Yellow
& ".\venv\Scripts\Activate.ps1"
Write-Host "✓ Virtual environment activated" -ForegroundColor Green

# Install dependencies
Write-Host "`nInstalling dependencies..." -ForegroundColor Yellow
pip install -r requirements.txt
Write-Host "✓ Dependencies installed" -ForegroundColor Green

# Run migrations
Write-Host "`nSetting up database..." -ForegroundColor Yellow
python manage.py makemigrations
python manage.py migrate
Write-Host "✓ Database initialized" -ForegroundColor Green

# Load challenges
Write-Host "`nLoading challenge data..." -ForegroundColor Yellow
python manage.py init_challenges
Write-Host "✓ Challenges loaded" -ForegroundColor Green

# Create superuser prompt
Write-Host "`n" -ForegroundColor White
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Setup complete! Now create an admin account:" -ForegroundColor Green
Write-Host "========================================`n" -ForegroundColor Cyan

python manage.py createsuperuser

Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "🚀 Setup Complete!" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "`nTo start the server, run:" -ForegroundColor Yellow
Write-Host "  python manage.py runserver`n" -ForegroundColor White
Write-Host "Then open: http://127.0.0.1:8000/`n" -ForegroundColor Cyan
