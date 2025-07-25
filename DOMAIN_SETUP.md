# Setup Instructions for nexus-bank.com.au

## Step 1: DNS Configuration
Make sure your domain nexus-bank.com.au points to your server's IP address:
- A record: nexus-bank.com.au -> YOUR_SERVER_IP
- A record: www.nexus-bank.com.au -> YOUR_SERVER_IP

## Step 2: Install Nginx
```bash
sudo apt update
sudo apt install nginx
```

## Step 3: Copy Nginx Configuration
```bash
# Copy the configuration file to Nginx sites-available
sudo cp nexus-bank.nginx.conf /etc/nginx/sites-available/nexus-bank.com.au

# Update the static files path in the config (replace with your actual path)
sudo nano /etc/nginx/sites-available/nexus-bank.com.au
# Change: /path/to/nexus-bank-app/src/bank/static
# To: /home/yourusername/nexus-bank-app/src/bank/static
# (This should be the same directory where your run_app.py file is located)

# Enable the site
sudo ln -s /etc/nginx/sites-available/nexus-bank.com.au /etc/nginx/sites-enabled/

# Remove default site (optional)
sudo rm -f /etc/nginx/sites-enabled/default

# Test Nginx configuration
sudo nginx -t

# Restart Nginx
sudo systemctl restart nginx
sudo systemctl enable nginx
```

## Step 3: Start Your Flask App
```bash
# Start in background using screen
screen -S bankapp
python run_app.py

# Detach from screen: Ctrl+A, then D
```

## Step 4: Test Your Setup
- Visit: http://nexus-bank.com.au
- Your Flask app should now be accessible via your domain!

## Step 5: Add SSL (Recommended)
```bash
# Install Certbot
sudo apt install certbot python3-certbot-nginx

# Get SSL certificate
sudo certbot --nginx -d nexus-bank.com.au -d www.nexus-bank.com.au

# Test auto-renewal
sudo certbot renew --dry-run
```

After SSL setup, your bank will be available at:
- https://nexus-bank.com.au (secure!)

## Troubleshooting
- Check Nginx status: `sudo systemctl status nginx`
- Check Nginx logs: `sudo tail -f /var/log/nginx/nexus-bank_error.log`
- Check if Flask is running: `curl http://localhost:5000`
- Check if port 5000 is open: `netstat -tulpn | grep :5000`
