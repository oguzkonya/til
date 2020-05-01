# Create a Changelog From Git Commits

Not exactly a changelog, but you can generate a log of what changed since a specific commit with this:

    $ git shortlog <commit>..HEAD

Just replace `<commit>` with the hash of the commit you want your log to start from.