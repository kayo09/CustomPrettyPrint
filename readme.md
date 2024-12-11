# Black-Style Pretty Printer

A Python utility for pretty-printing nested data structures in a style similar to the Black code formatter. This custom pretty printer ensures well-indented and readable output for dictionaries, lists, and other Python objects, while supporting non-JSON-serializable types like `datetime`.

## Features
- **Black-like formatting:** Prints Python objects in a style adhering to Black's standards.
- **Handles nested structures:** Supports deeply nested dictionaries and lists.
- **Custom formatting for special types:** Includes support for `datetime` and other non-serializable types.
- **Customizable indentation:** Allows you to adjust the number of spaces used for indentation.

## Usage

### Function Signature
```python
def black_style_pretty_print(data: Any, indent: int = 4, level: int = 0):
```

- **`data`**: The Python object to pretty-print (e.g., dictionaries, lists, `datetime`, etc.).
- **`indent`**: Number of spaces to use for indentation (default is 4).
- **`level`**: Current indentation level (used internally for recursion; you don't need to set this).

### Example
```python
from datetime import datetime

data = {
    "a": [
        {
            "123": datetime(2021, 11, 15, 0, 0),
            "456": "cillum dolore eu fugiat nulla pariatur. Excepteur sint...",
            "567": [
                1,
                2,
                "cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
            ],
        }
    ],
    "b": {"x": "yz"},
}

black_style_pretty_print(data)
```

### Output
```
{
    "a": [
        {
            "123": datetime.datetime(2021, 11, 15, 0, 0),
            "456": "cillum dolore eu fugiat nulla pariatur. Excepteur sint...",
            "567": [
                1,
                2,
                "cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
            ]
        }
    ],
    "b": {"x": "yz"}
}
```

## Installation
No installation is required. Just copy the `black_style_pretty_print` function into your project and start using it.

## Customization
You can modify the `indent` parameter to change the indentation width:
```python
black_style_pretty_print(data, indent=2)  # Use 2 spaces for indentation
```

## Limitations
- The function is designed for readability and Black-like formatting but is not a full replacement for Black.
- It does not handle all possible Python objects (e.g., sets, tuples, or custom classes) but can be extended easily.

## Contributing
If you'd like to improve this utility, feel free to submit a pull request or suggest changes.

## License
This project is licensed under the MIT License.
