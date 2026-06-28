from dataclasses import dataclass, field


@dataclass
class Circuito:
    circuitId: int
    circuitRef: str
    name: str
    location: str
    country: str
    lat: int
    lng: int
    alt: int
    url: str
    risultati: dict = field(default_factory=dict)

    def __hash__(self):
        return hash(self.circuitId)

    def __eq__(self, other):
        return self.circuitId == other.circuitId

    def __str__(self):
        return f"{self.name} -- {self.circuitId}"