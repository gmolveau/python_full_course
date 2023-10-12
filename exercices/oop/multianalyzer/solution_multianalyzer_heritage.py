import functools


class Result:
    def __init__(self, iocs: set[str], score: int = 0) -> None:
        self.iocs = iocs
        self.score = score


class Report:
    def __init__(self, results: list[Result] | None = None) -> None:
        self.results = results

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
            s += "- iocs :\n"
            for ioc in self.iocs:
                s += f"  - {ioc}\n"
        return s


class Service:
    def __init__(self, name: str) -> None:
        self.name = name

    def run(self, filepath: str) -> Result:
        raise NotImplementedError


class Yara(Service):
    def __init__(self) -> None:
        self.name: str = "Yara"

    def run(self, filepath: str) -> Result:
        return Result(score=500, iocs=["1.1.1.1"])


class ScanPDF(Service):
    def __init__(self) -> None:
        self.name: str = "ScanPDF"

    def run(self, filepath: str) -> Result:
        return Result(iocs=["cestpasnous.com"])


class Antivirus(Service):
    def __init__(self) -> None:
        self.name: str = "Antivirus"

    def run(self, filepath: str) -> Result:
        return Result(score=500, iocs={})


class MultiAnalyzer:
    def __init__(self, services: list[Service] | None = None) -> None:
        self.services = services or []

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
