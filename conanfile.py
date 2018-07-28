# -*- coding: utf-8 -*-

import os
from conans import ConanFile, tools

class IspcConan(ConanFile):
    name = 'ispc_installer'
    version = '1.9.2'
    description = 'ispc is a compiler for a variant of the C programming language, with extensions for "single program, multiple data" (SPMD) programming.'
    url = 'https://github.com/birsoyo/conan-ispc_installer'
    homepage = "https://ispc.github.io/"
    author = 'Orhun Birsoy <orhunbirsoy@gmail.com>'

    license = 'BSD'

    export = ["LICENSE.md"]

    settings = {'os_build': ['Windows', 'Linux', 'Macos'], 'arch_build': ['x86', 'x86_64']}

    def build(self):
        suffix, ext = self._download_suffix_ext()
        url = f'http://sourceforge.net/projects/ispcmirror/files/v{self.version}/ispc-v{self.version}-{suffix}.{ext}'
        tools.get(url, keep_permissions=True)
        os.rename(f'ispc-v{self.version}-{suffix}', 'ispc')

    def package(self):
        exe = 'ispc'
        if self.settings.os_build == 'Windows':
            exe += '.exe'
        self.copy(exe, dst='bin', src='ispc')

    def package_info(self):
        self.cpp_info.bindirs.append('bin')
        self.env_info.PATH.append(os.path.join(self.package_folder, 'bin'))

    def _download_suffix_ext(self):
        suffix = ''
        ext = ''
        if self.settings.os_build == 'Windows':
            suffix = 'windows'
            ext = 'zip'
        elif self.settings.os_build == 'macOS':
            suffix = 'osx'
            ext = 'tar.gz'
        elif self.settings.os_build == 'Linux':
            suffix = 'linux'
            ext = 'tar.gz'
        return suffix, ext
