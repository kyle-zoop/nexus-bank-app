# PowerShell script to run the fake bank
Write-Host "=========================================" -ForegroundColor Cyan
Write-Host "Global Trust Bank - Fake Bank for Scam Baiting" -ForegroundColor Yellow
Write-Host "=========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "WARNING: This is a FAKE BANK for educational/scam baiting purposes only!" -ForegroundColor Red
Write-Host "Do not use for real financial transactions." -ForegroundColor Red
Write-Host ""
Write-Host "Demo Login Credentials:" -ForegroundColor Green
Write-Host "Username: demo123" -ForegroundColor White
Write-Host "Password: secure456" -ForegroundColor White
Write-Host ""
Write-Host "Starting server on http://localhost:5000" -ForegroundColor Yellow
Write-Host "Press Ctrl+C to stop the server" -ForegroundColor Yellow
Write-Host ""

# Set location to bank directory
Set-Location "c:\Projects\bank"

# Start the Flask application
python app.py
