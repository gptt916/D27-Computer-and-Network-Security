#!/usr/bin/env bash

iptables -D FORWARD 1
iptables -D FORWARD 1

iptables -t nat -D PREROUTING 1
iptables -t nat -D POSTROUTING 2
