from .item import IniConfigItem
from configparser import SectionProxy
from dataclasses import dataclass
from typing import Optional


@dataclass(unsafe_hash=True)
class IniConfigSection:
    def __init__(
        self,
        item: SectionProxy,
        empty_to_none: Optional[bool] = False,
    ) -> None:
        """
        Generate config item from given config parser section

        :param SectionProxy item: config parser section
        :param Optional[bool] empty_to_none: use None for empty values. Default is false
        """
        for k, v in item.items():
            if k is None:
                continue

            setattr(self, k, IniConfigItem(v, empty_to_none))

    def __repr__(self) -> str:
        """
        Represent class content

        :return: content as text
        :rtype: str
        """
        kv = dict()

        for k in vars(self):
            kv[k] = getattr(self, k)

        return str(kv)
