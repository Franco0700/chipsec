# CHIPSEC: Platform Security Assessment Framework
# Copyright (c) 2021, Intel Corporation
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
# Contact information:
# chipsec@intel.com
#


"""
The mmcfg_base command displays PCIe MMCFG Base/Size.

Usage:

>>> chipsec_util mmcfg_base

Examples:

>>> chipsec_util mmcfg_base
"""

from chipsec.command import BaseCommand
from chipsec.hal import mmio


# Access to Memory Mapped PCIe Configuration Space (MMCFG)
class MMCfgBaseCommand(BaseCommand):

    def requires_driver(self):
        return True

    def run(self):
        _mmio = mmio.MMIO(self.cs)
        pciexbar, pciexbar_sz = _mmio.get_MMCFG_base_address()
        self.logger.log("[CHIPSEC] Memory Mapped Config Base: 0x{:016X}".format(pciexbar))
        self.logger.log("[CHIPSEC] Memory Mapped Config Size: 0x{:016X}".format(pciexbar_sz))
        self.logger.log('')


commands = {'mmcfg_base': MMCfgBaseCommand}
