import datetime
import os


def set_upload_path(instance, filename):
    return os.path.join(        # example: 'video/2015-02-01_22-00-17.jpg'
        instance.__class__.__name__.lower(),
        '{}.{}'.format(
            datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S'),
            filename.rsplit('.')[-1]
        )
    )
