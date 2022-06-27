## ini klass

The ini file parser.

### Install

To install a wheel from PyPI,

```bash
pip install --upgrade ini-klass
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
from ini import IniConfig

# read from `CONFIG` environment
config = IniConfig.read()

# read from file
config = IniConfig.read('/tmp/file.ini')

# access configuration value
name = config.example.name
```
