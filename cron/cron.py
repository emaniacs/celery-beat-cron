from __future__ import absolute_import
from celery import Celery
import os
import sys
import imp
import stopit
# import pdb

app = Celery('cron')
app.config_from_object('celeryconfig')

THIS_DIR = os.path.dirname(os.path.realpath(__file__))

# default timeout 10 seconds
DEFAULT_TIMEOUT = 10

@app.task
def run_crontab(jobname):
    """
    Run crontab berdasarkan jobname yang diberikan.
    <jobname> adalah module yang harus definisikan didalam folder ./jobs
    """

    name = str(jobname)
    filename = '{}/jobs/{}.py'.format(THIS_DIR, name)
    log_it(":LOAD {}".format(jobname))

    try:
        # pdb.set_trace()
        job = imp.load_source(name, filename)

        # get timeout
        timeout = DEFAULT_TIMEOUT
        if 'TIMEOUT' in dir(job):
            timeout = job.TIMEOUT

        try:
            log_it(":RUN {}; TIMEOUT {}".format(jobname, timeout))
            with stopit.ThreadingTimeout(timeout) as tmt:
                result = job.run()
        except Exception as e:
            log_it(":END {}; TIMEOUT {}; STATE timeout; MSG {}".format(jobname, timeout, str(e)))
            result = 'TIMEOUT'
    except Exception as e:
        log_it(":END {}; TIMEOUT {}; STATE error".format(jobname, timeout))
        raise e

    log_it(":END {}; TIMEOUT {}; STATE success".format(jobname, timeout))
    return result


def log_it(msg):
    """
    @TODO: log to file
    """
    print(msg)
