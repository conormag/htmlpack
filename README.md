# htmlpack
The htmlpack module can be used to help preprocess HTML files for production environments. It can be used to strip HTML comments, minify HTML,
and more.

```
usage: python -m htmlpack [-h] [-s] [-v] [-d] path

positional arguments:
  path                  Path to file or folder

optional arguments:
  -h, --help            show this help message and exit
  -s, --strip-comments  Whether to strip HTML comments (default: False)
  -v, --verbose         Verbose output (default: False)
  -d, --dry-run         Perform a dry run without modifying files (default: False)
```