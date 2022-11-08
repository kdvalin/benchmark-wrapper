#!/usr/bin/env python

import os

class lmbench_wrapper:
    def __init__(self, parser):
        parser.add_argument("-u", "--uuid", nargs=1, help="Provide the uuid")
        self.args = parser.parse_args()

        self.args.benchmarks = []
        self.args.fastmem = False
        self.args.processors = 1
        self.args.sched = "DEFAULT"
        self.args.samples = 1

        if "benchmarks" in os.environ:
            self.args.benchmarks = os.environ["benchmarks"]
        if "processors" in os.environ:
            self.args.processors = os.environ["processors"]


