```bash
#!/bin/bash

CONFIG="config/client.ovpn"
LOGFILE="/tmp/vpn.log"

if [ -f "$CONFIG" ]; then
    nohup openvpn --config "$CONFIG" > "$LOGFILE" 2>&1 &
else
    echo "Fichier de configuration VPN manquant : $CONFIG"
fi
```

Rends-le exécutable :
```bash
chmod +x vpn.sh
```


📄 allowed_hosts.txt (exemple)
```
192.168.1.42
mon-pc.local
