"""
Breath host system abstraction
"""

from shutil import which
import platform
import distro

from .interactions import *
from .functions import *
from .errors import *


class BreathSystem:
    """
    The host system abstraction.
    """
    def __init__(self, system_passwd=None):
        self.system_passwd = system_passwd
        self.platform = platform.system()
        self.distro = distro.id()

        # Raise error if distro unsupported
        if self.distro not in ('arch', 'debian', 'fedora', 'ubuntu'):
            raise DistributionNotSupported(f'{self.distro} is not currently supported!')

        # Windows and Darwin unsupported
        elif self.platform in ('Windows', 'Darwin'):
            raise PlatformNotSupported(f'{self.platform} is not currently supported!')

        # Undetermined unsupported
        elif self.platform not in ('Windows', 'Darwin', 'Linux'):
            raise UndeterminedSystem(f'{self.platform} is an unsupported system!')

        # Yay aur helper needs to be installed on an arch-based host system
        elif self.distro == 'arch' and which('yay') is None:
            raise YayNotFound(f'Breath requires the yay aur helper to be installed!')

        # Ask user for root password for host system if system_passwd is None
        if system_passwd is None:
            pass # Disabled as this is properly working yet.
            #self.system_passwd = get_password()
            