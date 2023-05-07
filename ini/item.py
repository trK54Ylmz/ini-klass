import re

from configparser import SectionProxy
from dataclasses import dataclass
from typing import Any, List, Optional, Union


@dataclass(unsafe_hash=True)
class IniConfigItem:
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
        self.__set__(item, empty_to_none)

    def __set__(self, item: SectionProxy, empty_to_none: Optional[bool] = False) -> None:
        """
        Set configuration item by given configuration

        :param SectionProxy item: config parser section
        :param Optional[bool] empty_to_none: use None for empty values. Default is false
        """
        for k, v in item.items():
            if k is None:
                continue

            if not v.startswith('"') and not v.endswith('"') and ',' in v:
                tys = []
                for sv in v.split(','):
                    if len(sv.strip()) == 0 and not empty_to_none:
                        continue
                    tys.append(self.__cast__(sv.strip(), empty_to_none))

                setattr(self, k, tys)
            else:
                if len(v) == 0 and not empty_to_none:
                    continue
                setattr(self, k, self.__cast__(v, empty_to_none))

    def __cast__(
        self,
        value: str,
        empty_to_none: Optional[bool] = False,
    ) -> Optional[Union[str, float, bool, List[Any]]]:
        """
        Convert data type for suitable type

        :param str value: data value in text
        :param Optional[bool] empty_to_none: use None for empty values. Default is false
        :return: new data with updated type
        :rtype: Optional[Union[str, float, bool, List[Any]]]
        """
        if len(value) == 0 and empty_to_none:
            return None

        if value in ['true', 'false']:
            return value == 'true'

        if re.match(r'^[0-9]+[\\.]+[0-9]+$', value):
            return float(value)

        if value.isnumeric():
            return float(value) if '.' in value else int(value)

        return value

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
