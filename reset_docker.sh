#!/usr/bin/env bash
# Reset the DNS-reflection lab: tear everything down, then rebuild & start.
# from the project dir

# Stop/remove anything compose tracks (ignore errors)
docker compose down --remove-orphans 2>/dev/null

# Force-remove the containers by name — they may be attached to a network
# that compose didn't create, so `down` won't touch them.
docker rm -f mydns attacker target 2>/dev/null

# Now the network has no active endpoints and can be removed.
docker network rm scapy_network 2>/dev/null

# Rebuild and start fresh; compose recreates the network with the subnet.
docker compose up --build
