from typing import Iterable
import jinja2
import os
import subprocess
import shlex

from snafu.benchmarks import Benchmark, BenchmarkResult
from snafu.process import sample_process

class LMBench(Benchmark):
    tool_name = "lmbench"

    def setup(self) -> bool:
        self.logger.info("Building LMBench config file")
        config_template = None
        script_pwd = os.path.dirname(os.path.realpath(__file__))
        with open(f"{script_pwd}/config_template.j2") as f:
            config = jinja2.Template("".join(f.readlines()))
        with open("CONFIG-lmbench", "w") as f:
            f.writelines(config.render())
        return True
    
    def collect(self) -> Iterable[BenchmarkResult]:
        samples = sample_process(shlex.split("/opt/lmbench/bin/lmbench ./CONFIG-lmbench"), self.logger)

        for sample_num, sample in enumerate(samples):
            self.logger.info(f"Starting LMBench sample number {sample_num}")
            if not sample.successful:
                self.logger.critical(f"Failed to run! Got error: {sample}")
            else:
                self.logger.info(sample)

        return []
    
    def cleanup(self):
        return True