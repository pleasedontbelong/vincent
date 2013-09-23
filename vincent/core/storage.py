import urlparse

from django.conf import settings

from storages.backends.s3boto import S3BotoStorage

from django.contrib.staticfiles.storage import CachedFilesMixin

from pipeline.storage import PipelineMixin


class CachedS3BotoStorage(PipelineMixin, CachedFilesMixin, S3BotoStorage):
    pass


def domain(url):
    return urlparse.urlparse(url).hostname


class MediaFilesStorage(S3BotoStorage):
    def __init__(self, *args, **kwargs):
        kwargs['bucket'] = settings.MEDIA_AWS_STORAGE_BUCKET_NAME
        kwargs['custom_domain'] = domain(settings.MEDIA_URL)
        super(MediaFilesStorage, self).__init__(*args, **kwargs)


class StaticFilesStorage(CachedS3BotoStorage):
    def __init__(self, *args, **kwargs):
        kwargs['bucket'] = settings.STATIC_AWS_STORAGE_BUCKET_NAME
        kwargs['custom_domain'] = domain(settings.STATIC_URL)
        super(StaticFilesStorage, self).__init__(*args, **kwargs)
