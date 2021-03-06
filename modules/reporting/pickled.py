# Copyright (C) 2010-2013 Cuckoo Sandbox Developers.
# This file is part of Cuckoo Sandbox - http://www.cuckoosandbox.org
# See the file 'docs/LICENSE' for copying permission.

import os
import pickle

from lib.dragon.common.abstracts import Report
from lib.dragon.common.exceptions import CuckooReportError

class Pickled(Report):
    """Stores report in python pickle format."""

    def run(self, results):
        """Writes report.
        @param results: Cuckoo results dict.
        @raise CuckooReportError: if fails to write report.
        """
        try:
            pickle.dump(results, open(os.path.join(self.reports_path, "report.pickle"), "w"), 2)
        except (pickle.PickleError, IOError) as e:
            raise CuckooReportError("Failed to generate Pickle report: %s" % e)
