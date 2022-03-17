## ini config

ini file parser.

### Install

To install a wheel from PyPI,

```bash
pip install --upgrade ini-config
```

### Usage

Example ini file,

```ini
[example]
id = 12
name = John
status = true
salary = 100.50
group = car, book, phone
```

To parse ini file above,

```python
from ini import ConfigParser

# read from `CONFIG` environment
config = ConfigParser.load()

# read from file
config = ConfigParser.load('/tmp/file.ini')

# access configuration value
name = config.example.name
```
