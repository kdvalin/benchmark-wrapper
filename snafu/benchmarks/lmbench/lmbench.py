from typing import Iterable
import jinja2
import os

from snafu.benchmarks import Benchmark, BenchmarkResult

class LMBench(Benchmark):
    tool_name = "lmbench"

    def setup(self) -> bool:
        self.logger.info("Building LMBench config file")
        config_template = None
        with open(f"{os.path.dirname(os.path.realpath(__file__))}/config_template.j2") as f:
            config = jinja2.Template("".join(f.readlines()))
        with open("CONFIG-lmbench", "w") as f:
            f.writelines(config.render())
        return True
    
    def collect(self) -> Iterable[BenchmarkResult]:
        return None
    
    def cleanup(self):
        return True