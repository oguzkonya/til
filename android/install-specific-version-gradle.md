# Install a specific version of Gradle

Homebrew doesn't list different versions of Gradle, however SDKMAN! does. Install SDKMAN! with the following line:

    $ curl -s "https://get.sdkman.io" | bash

Then, either open a new terminal or run the following:

    $ source "$HOME/.sdkman/bin/sdkman-init.sh"

Then, run the following to ensure that installation succeeded:

    $ sdk version

List available Gradle versions:

    $ sdk list gradle

Install:

    $ sdk install gradle 5.1.1