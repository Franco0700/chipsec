CHIPSEC: Platform Security Assessment Framework
===============================================

[![Build Status](https://travis-ci.org/chipsec/chipsec.svg?branch=master)](https://travis-ci.org/chipsec/chipsec)

CHIPSEC is a framework for analyzing the security of PC platforms including hardware, system firmware (BIOS/UEFI), and platform components. It includes a security test suite, tools for accessing various low level interfaces, and forensic capabilities. It can be run on Windows, Linux, Mac OS X and UEFI shell. Instructions for installing and using CHIPSEC can be found in the [manual](chipsec-manual.pdf).

NOTE: This software is for security testing purposes. Use at your own risk. Read [WARNING.txt](chipsec/WARNING.txt) before using.

First version of CHIPSEC was released in March 2014:
[Announcement at CanSecWest 2014](https://cansecwest.com/slides/2014/Platform%20Firmware%20Security%20Assessment%20wCHIPSEC-csw14-final.pdf)

Recent presentation on how to use CHIPSEC to find vulnerabilities in firmware, hypervisors and hardware configuration, explore low level system assets and even detect firmware implants:
[Exploring Your System Deeper](https://www.slideshare.net/CanSecWest/csw2017-bazhaniuk-exploringyoursystemdeeperupdated)

Driver Information
------------------

For instructions on building the driver please refer to our manual: 
  * [Linux Instructions](https://chipsec.github.io/installation/Install%20in%20Linux.html)
  * [Windows Instructions](https://chipsec.github.io/installation/Install%20in%20Windows.html)
  * [UEFI Shell Instructions](https://chipsec.github.io/installation/USB%20with%20UEFI%20Shell.html)

Alternatively you can see if you can find a driver that matches your setup [here](https://github.com/HackingThings/chipsec_drivers)

Release Convention
------------------

  * CHIPSEC uses a major.minor.patch release version number
  * Changes to the arguments or calling conventions will be held for a minor version update


Projects That Include CHIPSEC
-----------------------------

 * [Linux UEFI Validation (LUV)](https://01.org/linux-uefi-validation)
 
 * [ArchStrike](https://archstrike.org)
 
 * [BlackArch Linux](https://www.blackarch.org/index.html)

Contact Us
----------

For any questions or suggestions please contact us at: chipsec@intel.com

Mailing list:

 * [CHIPSEC discussion list on 01.org](https://lists.01.org/hyperkitty/list/chipsec@lists.01.org/)

Twitter:

 * For CHIPSEC release alerts: Follow us at [CHIPSEC Release](https://twitter.com/ChipsecR)
 * For general CHIPSEC info: Follow [CHIPSEC](https://twitter.com/Chipsec)

For AMD related questions or suggestions please contact Gabriel Kerneis at: Gabriel.Kerneis@ssi.gouv.fr
