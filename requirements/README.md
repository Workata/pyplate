# App requirements

Here you should have your all python requirments (libs) listed. It would be good to set precise version of specific libs (or at least version range). On top of that those requirements should be divided based on environment. For example you don't need testing libs (like pytest) on production env.

Example requirements structure:
```
├── requirements
    ├── base.txt
    ├── dev.txt     (for developing/testing; includes base)
    └── prod.txt    (for prod container; includes base)
```
