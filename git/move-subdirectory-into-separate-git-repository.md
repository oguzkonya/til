# Move Subdirectory into Separate Git Repository

You have a directory in your project and you only realized now that it should be in a separate repository itself while keeping the history intact? Fear no more.

1. Prepare the old repo

    ```
    $ cd <big-repo>
    $ git subtree split -P <name-of-folder> -b <name-of-new-branch>
    ```

2. Create the new repo

    ```
    $ mkdir ~/<new-repo> && cd ~/<new-repo>
    $ git init
    $ git pull </path/to/big-repo> <name-of-new-branch>
    ```

3. Link the new repo to GitHub or wherever

    ```
    $ git remote add origin <git@github.com:user/new-repo.git>
    $ git push -u origin master
    ```

4. Cleanup inside <big-repo>, if desired

    ```
    $ git rm -rf <name-of-folder>
    ```
