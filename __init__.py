"""VControl is a package for controlling the sound volume in windows.
It takes use of the PyCaw library, which operates on a logarithmic
scale between 0 and -28 , and converts it to a more readable, 0-100
scale using polynomial functions
"""


from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
import warnings
from pycaw.pycaw import IAudioEndpointVolume, AudioUtilities

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

ERROR_MESSAGE = 'System volume can only be set between 0 to 100, but {} was entered'


def scale(x):
    '''   Takes in a value between 0 and 100,
    and converts it to the systems logarithmic
    scale, between 0 and -28.
    '''
    if x < 0 or x > 100:
            warnings.warn(f'{x} is not between 0 and 100, and therefore is it possible for the output to be outside of the systems volume scale 0-(-28)')

    x4 = -3.20113 * (10 ** -7) * (x ** 4)
    x3 = 8.94101 * (10 ** -5) * (x ** 3)
    x2 = -1.00955 * (10 ** -2) * (x ** 2)
    x = 7.1527 * (10 ** -1) * x
    c = -28.1261
    return x4 + x3 + x2 + x + c


def unscale(x):
    '''   Takes in a value between 0 and -28 (in the systems logarithmic scale)
    and converts it to a float between 0 and 100.
    '''

    if x < -28 or x > 0:
         warnings.warn(f'{x} is not between -28 and 0 (the system volume scale) and therefore it is possible for the output to be outsideof the 0-100 range')

    x4 = 2.12815 * (10 ** -5) * (x ** 4)
    x3 = 3.71056 * (10 ** -3) * (x ** 3)
    x2 = 2.36278 * (10 ** -1) * (x ** 2)
    x = 7.76061 * x
    c = 1.00582 * (10 ** 2)
    return x4 + x3 + x2 + x + c


def set_volume(x):
    '''    Sets the system volume to a given value. Works on values between 0-100, 
    if any other value is given, a ValueError is raised.
    '''

    if x > 100 or x < 0:
        raise ValueError(ERROR_MESSAGE.format(x))

    volume.SetMasterVolumeLevel(scale(x), None)


def raise_volume(x):
    '''    Raises the system volume by a given value. If the desired volume is above 100, 
    the value is capped.
    '''

    current = get_volume()
    volume.SetMasterVolumeLevel(scale(max(min(current + x,100), 0)), None)


def lower_volume(x):
    '''    Lowers the system volume by a given value. If the desired volume is below 0, 
    the value is capped.
    '''

    current = get_volume()
    volume.SetMasterVolumeLevel(scale(current + x), None)


def get_volume(*, convert=True):
    '''    Returns an integer with the current system volume between 0 and 100.
    If the flag \"convert\" is set to false, it will instead return the volume
    in the systems logarithmic scale, between 0 and -28.
    '''

    v = volume.GetMasterVolumeLevel()
    if convert: v = unscale(v)
    return round(v)
