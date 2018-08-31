#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from bincrafters import build_template_installer
from bincrafters import build_shared

if __name__ == "__main__":
    builder = build_template_installer.get_builder()
    builder.add({}, {}, {}, {})
    builder.run()
