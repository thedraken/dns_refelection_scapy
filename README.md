# DNS reflection
A project that follows the guidelines [the project](https://infosecwriteups.com/mastering-scapy-for-network-security-a-hands-on-guide-to-scanning-and-dns-reflection-ce7fbf6f463f?sk=a7c72fafa6f6c31c9f4328b3933f63c1).

Uses python, docker, and installs all needed files inside the docker.

To start the system, you can use ./reset_docker.sh, to then open the relevant docker image bash, you can use ./openAttackerBash.sh and/or ./openTargetBash.sh

From inside the docker bashes, you can run the relevant python files to listen on the target, or test if the attacker can see what is going on from the attacker
