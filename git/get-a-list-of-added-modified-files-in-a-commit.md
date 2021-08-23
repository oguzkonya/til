# Get a List of Added/Modified Files in a Commit

Need to run an automated script on added/modified files in the most recent commit? Replace `<commit>` with your commit's hash:

    $ git diff-tree --diff-filter=AM --no-commit-id -r <commit> --name-only