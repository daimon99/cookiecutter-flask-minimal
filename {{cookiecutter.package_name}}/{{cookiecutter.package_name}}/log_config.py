# coding: utf-8


def set_logging(log_dir):
    from logging.config import dictConfig
    import os

    if not os.path.exists(log_dir):
        os.mkdir(log_dir)

    dictConfig({
        'version': 1,
        'formatters': {
            'default': {
                'format': '%(message)s',
            },
            'verbose': {
                'format': '%(asctime)s | %(levelname)s | %(filename)s:%(funcName)s:%(lineno)s '
                          '| %(process)d:%(thread)d | %(message)s'
            }
        },
        'handlers': {
            'stdout': {
                'class': 'logging.StreamHandler',
                'formatter': 'default',
            },
            'file': {
                'class': 'logging.handlers.WatchedFileHandler',
                'filename': os.path.join(log_dir, '{{cookiecutter.package_name}}.log'),
                'formatter': 'verbose'
            }
        },
        'loggers': {
            'flask.app': {
                'level': 'INFO',
                'handlers': ['stdout', 'file']
            }
        },

    })
