# dirclean
```
usage: dirclean.py [-h] [--delete] dir bytes

Recursively delete files until dir size is less than threshold size. Files
with oldest modification time are deleted first.

positional arguments:
  dir         root directory
  bytes       threshold size in bytes

optional arguments:
  -h, --help  show this help message and exit
  --delete    perform delete (default: print files to be deleted)
  ```
