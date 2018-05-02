# coding: utf-8

def set_logging(log_dir):
    from logging.config import dictConfig
    import os

    dictConfig({
        'version': 1,
        'formatters': {
            'default': {
                'format': '%(message)s',
            },
            'verbose': {
                'format': '%(asctime)s - %(levelname)s - %(filename)s:%(funcName)s:%(lineno)s - %(process)d:%(thread)d '
                          '- %(message)s'
            }
        },
        'handlers': {
            # 'wsgi': {
            #     'class': 'logging.StreamHandler',
            #     'stream': 'ext://flask.logging.wsgi_errors_stream',
            #     'formatter': 'default'
            # },
            'stdout': {
                'class': 'logging.StreamHandler',
                'formatter': 'default',
            },
            'file': {
                'class': 'logging.WatchedFileHandler',
                'filename': os.path.join(log_dir, '{{cookiecutter.package_name}}'),
                'formatter': 'verbose'
            }
        },

        'root': {
            'level': 'INFO',
            'handlers': ['file', 'stdout']
        }
    })
