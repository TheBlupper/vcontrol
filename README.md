# WinV
WinV is a package for controlling the sound volume in windows.
It takes use of the PyCaw library, which operates on a logarithmic
scale between 0 and -28, and converts it to a more readable, 0-100
scale using polynomial functions

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install WinV.

```bash
pip install winv
```

## Usage

```python
import winv

winv.set_volume(50) # sets the system volume to 50
winv.raise_volume(10) # increases the system volume by 10
winv.lower_volume(10) # decreases the system volume by 10
winv.get_volume() # returns the current volume
```

## Contributing
Due to the small size of this library i do not accept pull requests, but if any major issue arises, I will be able to fix it.

## License
[MIT](https://choosealicense.com/licenses/mit/)
