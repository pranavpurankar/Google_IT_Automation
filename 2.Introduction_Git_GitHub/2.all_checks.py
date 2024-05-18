#!/usr/bin/python3

import os

def check_reboot():
    '''Returns True if the computer has a pending reboot. '''
    return os.path.exists("/run/reboot-required")

def main():
    if check_reboot():
        print("Pending Reboot.")

main()
