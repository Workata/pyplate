### App settings

Default settings should be located in `base.py` file. On top of that you may want to include additional settings for different environments. These additional settings should inherit from `Settings` class.

Example settings structure:
```
├── src
    └── settings
        ├── components
        |   ├── __init__.py
        |   └── logging.py
        ├── __init__.py
        ├── base.py
        ├── dev.py
        ├── staging.py
        └── prod.py
```
