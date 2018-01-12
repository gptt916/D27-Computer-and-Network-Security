#!/usr/bin/env bash
echo 'nameserver 8.8.8.8' > /etc/resolv.conf  

iptables -F
iptables -F -t nat
iptables -F -t mangle

iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
iptables -A FORWARD -i eth0 -o eth1 -m state --state RELATED,ESTABLISHED -j ACCEPT
iptables -A FORWARD -i eth1 -o eth0 -j ACCEPT

iptables -t nat -A PREROUTING -p tcp -i eth1 -d 142.1.97.172 --dport 80 -j DNAT --to-destination 10.0.0.3:8080
python /shared/server.py
