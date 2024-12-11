from datetime import datetime
from typing import Any

def black_style_pretty_print(data: Any, indent: int = 4, level: int = 0):
    """
    Pretty print Python objects in a style similar to Black.

    Args:
        data (Any): The object to be pretty-printed.
        indent (int): Number of spaces for indentation.
        level (int): Current indentation level (used internally for recursion).

    Returns:
        None
    """
    space = " " * indent
    current_indent = space * level
    next_indent = space * (level + 1)

    if isinstance(data, dict):
        print("{")
        for i, (key, value) in enumerate(data.items()):
            comma = "," if i < len(data) - 1 else ""
            print(f"{next_indent}\"{key}\": ", end="")
            black_style_pretty_print(value, indent, level + 1)
            print(f"{comma}")
        print(f"{current_indent}}}", end="")

    elif isinstance(data, list):
        print("[")
        for i, item in enumerate(data):
            comma = "," if i < len(data) - 1 else ""
            print(next_indent, end="")
            black_style_pretty_print(item, indent, level + 1)
            print(f"{comma}")
        print(f"{current_indent}]", end="")

    elif isinstance(data, datetime):
        print(f"datetime.datetime({data.year}, {data.month}, {data.day}, {data.hour}, {data.minute})", end="")

    elif isinstance(data, str):
        print(f'"{data}"', end="")

    else:
        print(data, end="")

# Example usage
data = {
    "a": [
        {"123": datetime(2021, 11, 15, 0, 0),
            "456": "cillum dolore eu fugiat nulla pariatur. Excepteur sint...",
            "567": [
                1,
                2,
                "cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",    ],
        }
    ],
    "b": {"x": "yz"},
}

black_style_pretty_print(data)

