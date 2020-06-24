# VControl
VControl is a package for controlling the sound volume in windows.
It takes use of the PyCaw library, which operates on a logarithmic
scale between 0 and -28, and converts it to a more readable, 0-100
scale using polynomial functions

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install vcontrol.

```bash
pip install vcontrol
```

## Usage

```python
import vcontrol

vcontrol.set_volume(50) # sets the system volume to 50
vcontrol.raise_volume(10) # increases the system volume by 10
vcontrol.lower_volume(10) # decreases the system volume by 10
```

## Contributing
Due to the small size of this library i do not accept pull requests, but if any major issue arises, I will be able to fix it.

## License
[MIT](https://choosealicense.com/licenses/mit/)
