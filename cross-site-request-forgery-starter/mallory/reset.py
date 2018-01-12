import os, requests, urllib

PROTOCOL = "http"
HOST = "10.0.0.2"
PORT = "80"
BASE = PROTOCOL + "://" + HOST + ":" + PORT

# Mallory's credentials
mallory = {
    'email': 'mallory@example.com',
    'password': 'pass4mallory'
}

# reset the application
requests.get(BASE + '/reset.php')