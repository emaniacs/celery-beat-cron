from __future__ import absolute_import
from celery import Celery
import os
import sys
import imp
# import pdb

app = Celery('cron')
app.config_from_object('celeryconfig')

THIS_DIR = os.path.dirname(os.path.realpath(__file__))

@app.task
def run_crontab(jobname):
    """
    Run crontab berdasarkan jobname yang diberikan.
    <jobname> adalah module yang harus definisikan didalam folder ./jobs
    """

    name = str(jobname)
    filename = '{}/jobs/{}.py'.format(THIS_DIR, name)
    try:
        # pdb.set_trace()
        job = imp.load_source(name, filename)
        result = job.run()
    except Exception as e:
        raise e

    return result
