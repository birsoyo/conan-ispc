#!/bin/bash

set -e
set -x

if [[ "$(uname -s)" == 'Darwin' ]]; then
    brew update
    brew install openssl readline
    brew outdated pyenv || brew upgrade pyenv
    brew install pyenv-virtualenv

    if which pyenv > /dev/null; then
        eval "$(pyenv init -)"
    fi

    pyenv install 3.6.6
    pyenv virtualenv 3.6.6 conan
    pyenv rehash
    pyenv activate conan
fi

pip install conan --upgrade
pip install sesame_package_tools conan_package_tools bincrafters_package_tools --upgrade

conan user
