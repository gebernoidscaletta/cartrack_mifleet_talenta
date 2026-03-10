from enum import Enum

class ModuleName(Enum):
    FUEL = "fuel"
    TOLL = "toll"
    
    @classmethod
    def from_str(cls, module_name: str) -> 'ModuleName':
        for member in cls:
            if member.value == module_name:
                return member
        raise ValueError(f"Unknown module name: {module_name}")