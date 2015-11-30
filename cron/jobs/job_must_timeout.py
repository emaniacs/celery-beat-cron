#!/usr/bin/env python

import time

__AUTHOR__ = 'ardi'
__VERSION__ = '0.1.0'

JOB_NAME = 'job_must_timeout'
TIMEOUT = 2

def run():
    # sleep
    time.sleep(3)
    return "THIS MUST NOT RETURN"
