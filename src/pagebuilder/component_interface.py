import json
from abc import ABC, abstractmethod

# Base class for all components
class Component:
    @abstractmethod
    def to_html(self) -> str:
        pass

    def _repr_html_(self):
        return self.to_html()

    def to_json(self) -> str:
        return json.dumps(self, default=lambda o: o.__dict__,
            sort_keys=True, indent=4)

