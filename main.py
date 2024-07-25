#!/usr/bin/env python

import argparse
import logging
import string
import sys
import time
from random import choice, seed

import flask_bcrypt

DEFAULT_PASSWORD_LENGTH = 16
DEFAULT_LOG_LEVEL = "error"
PASSWORD_OUTPUT_KEY = "password"
PASSWORD_HASH_OUTPUT_KEY = "password-hash"


parser = argparse.ArgumentParser()

parser.add_argument(
    "-l",
    "--log-level",
    type=str,
    choices=["debug", "info", "warning", "error"],
    default=DEFAULT_LOG_LEVEL,
)
parser.add_argument("-L", "--length", type=int, default=DEFAULT_PASSWORD_LENGTH)
parser.add_argument("-p", "--password", type=str, default=None)


def get_default_password(length: int) -> str:
    return "".join(choice(string.ascii_letters + string.digits) for _ in range(length))


def hash_password(password: str) -> str:
    return flask_bcrypt.generate_password_hash(password).decode("utf-8")


def output_result(password: str, password_hash: str):
    print(
        f"::set-output name={PASSWORD_OUTPUT_KEY}::{password}",
        file=sys.stdout,
        flush=True,
    )
    print(
        f"::set-output name={PASSWORD_HASH_OUTPUT_KEY}::{password_hash}",
        file=sys.stdout,
        flush=True,
    )


if __name__ == "__main__":
    args = parser.parse_args(sys.argv[1:])

    seed(time.time())
    logging.basicConfig(level=args.log_level.upper())

    password = args.password or get_default_password(args.length)
    password_hash = hash_password(password)
    logging.debug(f"password-hash: {password_hash}")

    output_result(password, password_hash)
