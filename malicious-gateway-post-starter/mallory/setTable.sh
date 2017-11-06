#!/usr/bin/env bash

iptables -t nat -A PREROUTING -p tcp -i eth1 -d 142.1.97.172 --dport 80 -j DNAT --to-destination 10.0.0.3:8080