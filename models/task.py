import dataclasses

@dataclasses.dataclass
class Task:
    id: int
    title: str
    description: str
    completed: bool = False
