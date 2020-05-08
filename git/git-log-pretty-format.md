# Git Log Pretty Format

A nicely formatted `git log` with a tree view:

    $ git log --topo-order --all --graph --pretty=format:"%C(green)%h%C(reset) %s%C(red)%d%C(reset) %C(yellow)(%cD)%C(reset) %C(blue)%cN%C(reset)%n"