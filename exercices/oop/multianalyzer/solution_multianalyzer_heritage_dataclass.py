import functools
from dataclasses import dataclass


@dataclass
class Result:
    iocs: set[str]
    score: int = 0


@dataclass
class Report:
    results: list[Result] = None

    @property
    def score(self):
        return functools.reduce(lambda x, y: x + y, (r.score for r in self.results))

    @property
    def iocs(self):
        return sorted([ioc for r in self.results for ioc in r.iocs])

    def __str__(self) -> str:
        s = "Report :\n"
        s += f"- score = {self.score}\n"
        if self.iocs:
            s += f"- iocs :\n"
            for ioc in self.iocs:
                s += f"  - {ioc}\n"
        return s


class Service:
    name: str

    def run(self, filepath: str) -> Result:
        raise NotImplementedError


@dataclass
class Yara(Service):
    name: str = "Yara"

    def run(self, filepath: str) -> Result:
        return Result(score=500, iocs=["1.1.1.1"])


@dataclass
class ScanPDF(Service):
    name: str = "ScanPDF"

    def run(self, filepath: str) -> Result:
        return Result(iocs=["cestpasnous.com"])


@dataclass
class Antivirus(Service):
    name: str = "Antivirus"

    def run(self, filepath: str) -> Result:
        return Result(score=500, iocs={})


@dataclass
class MultiAnalyzer:
    services: list[Service]

    def get_service_by_name(self, name: str) -> Service:
        for service in self.services:
            if service.name == name:
                return service
        raise ValueError

    def analyze(self, filepath: str, services: list[str]) -> Report:
        results = []
        for service_name in services:
            service = self.get_service_by_name(service_name)
            results.append(service.run(filepath))
        return Report(results=results)


scanpdf = ScanPDF()
yara = Yara()
antivirus = Antivirus()
tool = MultiAnalyzer(services=[scanpdf, yara, antivirus])

report = tool.analyze(filepath="bizarre.pdf", services=["ScanPDF", "Yara", "Antivirus"])
print(report)
assert (
    str(report)
    == """Report :
- score = 1000
- iocs :
  - 1.1.1.1
  - cestpasnous.com
"""
)
