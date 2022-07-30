from __future__ import annotations

import os
import sys

from .section import IniConfigSection

from configparser import ConfigParser
from typing import Any, List, Optional, Union


class IniKlassException(Exception):
    pass


class IniConfig:
    config: IniConfigSection

    @staticmethod
    def read(file=None, empty_to_none=False) -> IniConfig:
        """
        Load configuration by given path, command line argument or
        `CONFIG` environment.

        :param Optional[str] file: the configuration file path
        :return: the configuration object
        :rtype: ini.IniConfig
        """
        c = ConfigParser(default_section=None)

        path = None
        if file is not None:
            path = file
        elif 'CONFIG' in os.environ:
            path = os.environ.get('CONFIG')
        elif len(sys.argv) > 1:
            path = sys.argv[1]
        else:
            raise IniKlassException('Configuration parameter must be set.')

        if path is None or len(path.strip()) == 0:
            raise IniKlassException('Configuration path is missing.')

        if not os.path.exists(path):
            raise IniKlassException(f'Configuration file does not exists "{path}".')

        # read configuration from local path
        c.read(path)

        # size of sections must be greater than one
        if len(c.sections()) == 0:
            raise IniKlassException('There are no any sections.')

        ini = IniConfig()
        ini.config = IniConfigSection(c, empty_to_none)

        return ini

    def __getattr__(self, key: str) -> Optional[Union[str, float, bool, List[Any]]]:
        """
        Get configuration parameter

        :param str key: class parameter of configuration
        :return: configuration value
        :rtype: Optional[Union[str, float, bool, List[Any]]]
        """
        if not hasattr(self.config, key):
            return None

        return getattr(self.config, key)

    def __repr__(self) -> str:
        """
        Represent class content

        :return: content as text
        :rtype: str
        """
        kv = dict()

        for k in vars(self.config):
            kv[k] = getattr(self, k)

        return str(kv)
