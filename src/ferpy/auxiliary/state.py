from typing import List, Optional
from dataclasses import dataclass
from datetime import datetime

from ..main.quantity_values import QuantityValues

@dataclass
class State:
    """
    Represents a state in the system.
    """
    name: Optional[str] = None
    description: Optional[str] = None
    quantity_value: Optional[QuantityValues] = None

    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "quantity_value": self.quantity_value.to_dict() if self.quantity_value else None,
        }

    @classmethod
    def from_dict(cls, data: dict):
        """Creates a State instance from a dictionary."""
        return cls(
            name=data.get("name"),
            description=data.get("description"),
            quantity_value=QuantityValues.from_dict(data["quantity_value"]) if data.get("quantity_value") else None
        )