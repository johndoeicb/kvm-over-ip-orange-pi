```python
from flask import Flask, render_template, request
import subprocess
import socket

app = Flask(__name__)

# Lire la liste des hôtes autorisés (nom ou IP)
def is_authorized(hostname):
    with open("allowed_hosts.txt", "r") as f:
        allowed = [line.strip() for line in f.readlines() if line.strip()]
    return hostname in allowed or request.remote_addr in allowed

@app.route("/")
def index():
    hostname = socket.gethostname()
    client_ip = request.remote_addr
    show_button = is_authorized(client_ip)
    return render_template("index.html", show_button=show_button)

@app.route("/start_vpn", methods=["POST"])
def start_vpn():
    if is_authorized(request.remote_addr):
        subprocess.Popen(["bash", "vpn.sh"])
        return "VPN démarré."
    return "Accès refusé."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
