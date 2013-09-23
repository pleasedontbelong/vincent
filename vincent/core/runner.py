from django_nose import NoseTestSuiteRunner as BaseNoseTestSuiteRunner

from django.conf import settings


class NoseTestSuiteRunner(BaseNoseTestSuiteRunner):
    def setup_test_environment(self, *args, **kwargs):

        """
        Django test runner allowing testing of celery delayed tasks.
        All tasks are run locally, not in a worker.
        To use this runner set ``settings.TEST_RUNNER``::
            TEST_RUNNER = "celery.contrib.test_runner.CeleryTestSuiteRunner"
        """
        settings.CELERY_ALWAYS_EAGER = True
        settings.CELERY_EAGER_PROPAGATES_EXCEPTIONS = True  # Issue #75
        super(NoseTestSuiteRunner, self).setup_test_environment(*args,
                                                                **kwargs)
