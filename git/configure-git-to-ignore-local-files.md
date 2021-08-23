# Configure Git to Ignore Local Files

If you need to ignore files without adding entries to the global `.gitignore` the `.git/info/exclude` file has the same format as any `.gitignore` file, but it's local only. If you already have unstaged changes you must run the following after editing your ignore-patterns:

    $ git update-index --assume-unchanged <file-list>