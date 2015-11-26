from celery.schedules import crontab
from datetime import timedelta

BROKER_URL = 'redis://localhost:6379/'
CELERY_RESULT_BACKEND = 'redis'

# http://docs.celeryproject.org/en/latest/userguide/periodic-tasks.html

CELERYBEAT_SCHEDULE = {
        'every-one-minute': {
            'task': 'cron.run_crontab',
            'schedule': crontab(minute='*/1'),
            'args': ('every_one_minute',),
        },
        'every-three-minute': {
            'task': 'cron.run_crontab',
            'schedule': crontab(minute='*/3'),
            'args': ('every_three_minute',),
        },
        'every-five-minute': {
            'task': 'cron.run_crontab',
            'schedule': crontab(minute='*/5'),
            'args': ('every_five_minute',),
        },
        'every-seven-minute': {
            'task': 'cron.run_crontab',
            'schedule': crontab(minute='*/7'),
            'args': ('every_seven_minute',),
        },
        'every-nine-minute': {
            'task': 'cron.run_crontab',
            'schedule': crontab(minute='*/9'),
            'args': ('every_nine_minute',),
        },
        'every-one-hour': {
            'task': 'cron.run_crontab',
            'schedule': crontab(minute=0, hour='*/1'),
            'args': ('every_one_hour',),
        },
    }
