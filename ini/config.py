import configparser
import os
import sys
from dataclasses import dataclass
from typing import Optional


def _is_float(val: str):
    try:
        float(val)
        return True
    except ValueError:
        return False
    return False


def _is_bool(val: str) -> bool:
    return val.upper() in ["TRUE", "FALSE"]


def _get_bool(val: str) -> bool:
    return val.upper() == "TRUE"


class ConfigParserException(Exception):
    pass


@dataclass
class Sections:
    raw_sections: configparser.ConfigParser

    def __post_init__(self):
        for section_key, section_value in self.raw_sections.items():
            setattr(self, section_key, SectionContent(section_value.items()))


@dataclass
class SectionContent:
    raw_section_content: configparser.ConfigParser

    def __post_init__(self):
        for section_content_k, section_content_v in self.raw_section_content:
            if _is_float(section_content_v):
                setattr(self, section_content_k, float(section_content_v))
            elif section_content_v.isnumeric():
                setattr(self, section_content_k, int(section_content_v))
            elif "," in section_content_v:
                setattr(
                    self,
                    section_content_k,
                    [_item.strip() for _item in section_content_v.split(",")],
                )
            elif _is_bool(section_content_v):
                setattr(self, section_content_k, _get_bool(section_content_v))
            else:
                setattr(self, section_content_k, section_content_v)


class ConfigParser(Sections):
    """Main Config Parser class.

    ATTENTION! python internal configparser module also has a class
    with the same name. (configparser.ConfigParser).
    Watch out for the shadowing.
    """

    def __init__(self, raw_config_parser: configparser.ConfigParser):
        """Initialize raw config."""
        Sections.__init__(self, raw_config_parser)

    @staticmethod
    def load(path: Optional[str] = None) -> "ConfigParser":
        """
        Load configuration by given path or `CONFIG` environment.

        The environment variable is primary lookup.

        :param str or None path: the configuration path
        :return: the configuration object
        :rtype: attrdict.AttrMap
        """
        if path is None:
            if "CONFIG" in os.environ:
                path = os.environ["CONFIG"]
            elif len(sys.argv) > 1:
                path = sys.argv[1]
            else:
                raise ConfigParserException("Configuration parameter must be set")

        if path is None or len(path.strip()) == 0:
            raise ConfigParserException("Configuration path is missing")

        if not os.path.exists(path):
            raise ConfigParserException(f'Configuration file does not exists "{path}"')

        config = configparser.ConfigParser()
        config.read(path)

        # size of sections must be greater than one
        if len(config.sections()) == 0:
            raise ConfigParserException("There are no any sections")

        config_dataclass = ConfigParser(config)
        return config_dataclass
