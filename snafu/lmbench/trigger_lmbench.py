#!/usr/bin/env python
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

import datetime
import subprocess
import logging

import requests

logger = logging.getLogger("snafu")

class Trigger_lmbench:
    def __init__(self, args):
        self.uuid = args.uuid

        self.benchmarks = args.benchmarks #array of benchmarks to run
        self.fastmem = args.fastmem # boolean
        self.processors = args.processors # integer
        self.sched = args.sched #string, describes scheduler
        self.samples = args.samples #integer, number of times to run test

    def emit_actions(self):
        ts = datetime.datetime().utcnow()
        logger.info("Starting LMBench run")
