# encoding: utf-8

"""
.. codeauthor:: Tsuyoshi Hombashi <gogogo.vm@gmail.com>
"""

from __future__ import absolute_import
from __future__ import unicode_literals

import logbook
import subprocrunner


LOG_FORMAT_STRING = "[{record.level_name}] {record.channel}: {record.message}"


logger = logbook.Logger("tcconfig")
logger.disable()


def set_logger(log_level):
    """
    Set logging level of this module. The module using
    `logbook <http://logbook.readthedocs.io/en/stable/>`__ module for logging.

    :param int log_level:
        One of the log level of the
        `logbook <http://logbook.readthedocs.io/en/stable/api/base.html>`__.
        Disabled logging if the ``log_level`` is ``logbook.NOTSET``.
    """

    subprocrunner.set_logger(log_level)

    if log_level == logbook.NOTSET:
        logger.disable()
    else:
        logger.enable()
        logger.level = log_level