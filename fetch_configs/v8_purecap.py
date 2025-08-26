# Copyright 2014 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import sys

import config_util  # pylint: disable=import-error


# This class doesn't need an __init__ method, so we disable the warning
# pylint: disable=no-init
class V8(config_util.Config):
    """Basic Config class for V8."""
    @staticmethod
    def fetch_spec(props):
        url = 'https://github.com/CTSRD-CHERI/v8.git'
        solution = {
            'name': 'v8',
            'url': url,
            'deps_file': 'DEPS',
            'managed': False,
            'custom_deps': {
               "v8/build": "https://github.com/chromium-cheri/build.git@9a86e31a61f262071edd37ac24e05515c2764fd3",
               "v8/buildtools": "https://github.com/chromium-cheri/buildtools.git@8b16338d17cd71b04a6ba28da7322ab6739892c2",
               "v8/third_party/zlib": "https://github.com/chromium-cheri/zlib.git@05ca39ba1b282fc3ed9e5e3f0ebfadafaa25ef21",
            },
        }
        spec = {
            'solutions': [solution],
            'with_branch_heads': True,
        }
        return {
            'type': 'gclient_git',
            'gclient_git_spec': spec,
        }

    @staticmethod
    def expected_root(_props):
        return 'v8'


def main(argv=None):
    return V8().handle_args(argv)


if __name__ == '__main__':
    sys.exit(main(sys.argv))
