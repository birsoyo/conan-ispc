# -*- coding: utf-8 -*-

import io
from conans import ConanFile

class IspcTestConan(ConanFile):

    def build(self):
        pass # just silence the 'WARN: This conanfile has no build step'

    def test(self):
        output = io.StringIO()
        self.run('ispc --version', output=output)
        self.output.info(f'Installed:\n{str(output.getvalue())}')
        ver = str(self.requires['ispc_installer'].conan_reference.version)
        assert(ver in str(output.getvalue()))
