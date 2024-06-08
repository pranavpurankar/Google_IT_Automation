#!/usr/bin/env python3


import logging


def user_login(username, password):
    logging.info(f"Attempting to log in user: {username}")
    # . . . (some code for authentication)
    if authentication_failed:
        logging.error(f"Login failed for user: {username}")
    else:
        logging.info(f"Successfully logged in user: {username}")

