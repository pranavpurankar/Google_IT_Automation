#!/bin/bash

# This file contains the conditionals in the bash scripting, check localhost.

if grep "127.0.0.1" /etc/hosts; then
	echo "Everything ok"
else
	echo "ERROR! 127.0.0.1 is not in /etc/hosts"
fi
