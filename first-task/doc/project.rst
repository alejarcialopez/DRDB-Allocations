Django project configuration
============================

The :py:mod:``first_task_project`` module contains top-level
configuration and URL routes for the entire web application.

Settings
--------

Django settings for |project|.

.. _settings:

Generic settings
````````````````

.. automodule:: first_task_project.settings
    :members:

.. _settings_testsuite:

Test-suite specific settings
````````````````````````````

.. automodule:: first_task_project.settings.tox
    :members:

.. _settings_developer:

Developer specific settings
```````````````````````````

.. automodule:: first_task_project.settings.developer
    :members:

Custom test suite runner
------------------------

The :any:`test suite settings <settings_testsuite>` overrides the
``TEST_RUNNER`` setting to point to
:py:class:`~first_task_project.test.runner.BufferedTextTestRunner`.
This runner captures output to stdout and stderr and only reports the output if
a test fails. This helps make our tests a little less noisy.

.. autoclass:: first_task_project.test.runner.BufferedDiscoverRunner

.. autoclass:: first_task_project.test.runner.BufferedTextTestRunner
