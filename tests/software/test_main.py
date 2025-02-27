# CHIPSEC: Platform Security Assessment Framework
# Copyright (c) 2017, Google
# Copyright (c) 2018-2021, Intel Corporation
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; Version 2.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
#
#

import unittest

import chipsec_main
from chipsec.testcase import ExitCode


class TestChipsecMain(unittest.TestCase):
    """Test the main entry point script."""

    def test_help(self):
        """Run chipsec_main --help"""
        # Basic test. This should run without loading the driver.
        m = chipsec_main.ChipsecMain(["--help"])
        self.assertEqual(ExitCode.OK, m.main())
