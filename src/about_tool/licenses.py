#!/usr/bin/env python
# -*- coding: utf8 -*-

# ============================================================================
#  Copyright (c) 2013-2016 nexB Inc. http://www.nexb.com/ - All rights reserved.
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#      http://www.apache.org/licenses/LICENSE-2.0
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
# ============================================================================

from __future__ import print_function


# SPDX License Identifiers from http://spdx.org/licenses/
# based on SPDX License List version 1.18 released on 2013-04-10
SPDX_LICENSES = (
    'AFL-1.1',
    'AFL-1.2',
    'AFL-2.0',
    'AFL-2.1',
    'AFL-3.0',
    'APL-1.0',
    'Aladdin',
    'ANTLR-PD',
    'Apache-1.0',
    'Apache-1.1',
    'Apache-2.0',
    'APSL-1.0',
    'APSL-1.1',
    'APSL-1.2',
    'APSL-2.0',
    'Artistic-1.0',
    'Artistic-2.0',
    'AAL',
    'BitTorrent-1.0',
    'BitTorrent-1.1',
    'BSL-1.0',
    'BSD-2-Clause',
    'BSD-2-Clause-FreeBSD',
    'BSD-2-Clause-NetBSD',
    'BSD-3-Clause',
    'BSD-3-Clause-Clear',
    'BSD-4-Clause',
    'BSD-4-Clause-UC',
    'CECILL-1.0',
    'CECILL-1.1',
    'CECILL-2.0',
    'CECILL-B',
    'CECILL-C',
    'ClArtistic',
    'CNRI-Python',
    'CNRI-Python-GPL-Compatible',
    'CPOL-1.02',
    'CDDL-1.0',
    'CDDL-1.1',
    'CPAL-1.0',
    'CPL-1.0',
    'CATOSL-1.1',
    'Condor-1.1',
    'CC-BY-1.0',
    'CC-BY-2.0',
    'CC-BY-2.5',
    'CC-BY-3.0',
    'CC-BY-ND-1.0',
    'CC-BY-ND-2.0',
    'CC-BY-ND-2.5',
    'CC-BY-ND-3.0',
    'CC-BY-NC-1.0',
    'CC-BY-NC-2.0',
    'CC-BY-NC-2.5',
    'CC-BY-NC-3.0',
    'CC-BY-NC-ND-1.0',
    'CC-BY-NC-ND-2.0',
    'CC-BY-NC-ND-2.5',
    'CC-BY-NC-ND-3.0',
    'CC-BY-NC-SA-1.0',
    'CC-BY-NC-SA-2.0',
    'CC-BY-NC-SA-2.5',
    'CC-BY-NC-SA-3.0',
    'CC-BY-SA-1.0',
    'CC-BY-SA-2.0',
    'CC-BY-SA-2.5',
    'CC-BY-SA-3.0',
    'CC0-1.0',
    'CUA-OPL-1.0',
    'D-FSL-1.0',
    'WTFPL',
    'EPL-1.0',
    'eCos-2.0',
    'ECL-1.0',
    'ECL-2.0',
    'EFL-1.0',
    'EFL-2.0',
    'Entessa',
    'ErlPL-1.1',
    'EUDatagrid',
    'EUPL-1.0',
    'EUPL-1.1',
    'Fair',
    'Frameworx-1.0',
    'FTL',
    'AGPL-1.0',
    'AGPL-3.0',
    'GFDL-1.1',
    'GFDL-1.2',
    'GFDL-1.3',
    'GPL-1.0',
    'GPL-1.0+',
    'GPL-2.0',
    'GPL-2.0+',
    'GPL-2.0-with-autoconf-exception',
    'GPL-2.0-with-bison-exception',
    'GPL-2.0-with-classpath-exception',
    'GPL-2.0-with-font-exception',
    'GPL-2.0-with-GCC-exception',
    'GPL-3.0',
    'GPL-3.0+',
    'GPL-3.0-with-autoconf-exception',
    'GPL-3.0-with-GCC-exception',
    'LGPL-2.1',
    'LGPL-2.1+',
    'LGPL-3.0',
    'LGPL-3.0+',
    'LGPL-2.0',
    'LGPL-2.0+',
    'gSOAP-1.3b',
    'HPND',
    'IPL-1.0',
    'Imlib2',
    'IJG',
    'Intel',
    'IPA',
    'ISC',
    'JSON',
    'LPPL-1.3a',
    'LPPL-1.0',
    'LPPL-1.1',
    'LPPL-1.2',
    'LPPL-1.3c',
    'Libpng',
    'LPL-1.02',
    'LPL-1.0',
    'MS-PL',
    'MS-RL',
    'MirOS',
    'MIT',
    'Motosoto',
    'MPL-1.0',
    'MPL-1.1',
    'MPL-2.0',
    'MPL-2.0-no-copyleft-exception',
    'Multics',
    'NASA-1.3',
    'Naumen',
    'NBPL-1.0',
    'NGPL',
    'NOSL',
    'NPL-1.0',
    'NPL-1.1',
    'Nokia',
    'NPOSL-3.0',
    'NTP',
    'OCLC-2.0',
    'ODbL-1.0',
    'PDDL-1.0',
    'OGTSL',
    'OLDAP-2.2.2',
    'OLDAP-1.1',
    'OLDAP-1.2',
    'OLDAP-1.3',
    'OLDAP-1.4',
    'OLDAP-2.0',
    'OLDAP-2.0.1',
    'OLDAP-2.1',
    'OLDAP-2.2',
    'OLDAP-2.2.1',
    'OLDAP-2.3',
    'OLDAP-2.4',
    'OLDAP-2.5',
    'OLDAP-2.6',
    'OLDAP-2.7',
    'OPL-1.0',
    'OSL-1.0',
    'OSL-2.0',
    'OSL-2.1',
    'OSL-3.0',
    'OLDAP-2.8',
    'OpenSSL',
    'PHP-3.0',
    'PHP-3.01',
    'PostgreSQL',
    'Python-2.0',
    'QPL-1.0',
    'RPSL-1.0',
    'RPL-1.1',
    'RPL-1.5',
    'RHeCos-1.1',
    'RSCPL',
    'Ruby',
    'SAX-PD',
    'SGI-B-1.0',
    'SGI-B-1.1',
    'SGI-B-2.0',
    'OFL-1.0',
    'OFL-1.1',
    'SimPL-2.0',
    'Sleepycat',
    'SMLNJ',
    'SugarCRM-1.1.3',
    'SISSL',
    'SPL-1.0',
    'Watcom-1.0',
    'NCSA',
    'VSL-1.0',
    'W3C',
    'WXwindows',
    'Xnet',
    'X11',
    'XFree86-1.1',
    'YPL-1.0',
    'YPL-1.1',
    'Zimbra-1.3',
    'Zlib',
    'ZPL-1.1',
    'ZPL-2.0',
    'ZPL-2.1',
)


# Maps lowercase id to standard ids with official case
SPDX_LICENSE_IDS = dict((name.lower(), name) for name in SPDX_LICENSES)


# Use DJE License Name
COMMON_LICENSES = (
    'AES-128 v3.0 License',
    'Apache License 1.1',
    'Apache License 2.0',
    'Apple Attribution License 1997',
    'Apple Example Code License',
    'Apple Public Source License 2.0',
    'Arphic Public License',
    'Artistic License (Perl) 1.0',
    'Artistic License 2.0',
    'Bitstream Vera Font License',
    'Boost Software License 1.0',
    'Broadcom CFE License',
    'BSD-Modified',
    'BSD-Original',
    'BSD-Original-UC',
    'BSD-Simplified',
    'CMU Computing Services License',
    'Common Development and Distribution License 1.0',
    'Common Development and Distribution License 1.1',
    'Common Public License 1.0',
    'Creative Commons Attribution License 2.5',
    'Creative Commons Attribution Share Alike License 3.0',
    'Curl License',
    'FreeType Project License',
    'GNU General Public License 2.0',
    'GNU General Public License 2.0 with Bison exception',
    'GNU General Public License 2.0 with GLIBC  exception',
    'GNU General Public License 3.0',
    'GNU Lesser General Public License 2.1',
    'GNU Library General Public License 2.0',
    'GPL 2.0 or later with Linking exception',
    'GPL 2.0 with Broadcom Linking exception',
    'Independent JPEG Group License',
    'ISC License (ISCL)',
    'Larabie Fonts EULA',
    'Libpng License',
    'Microsoft Limited Public License',
    'Microsoft Public License',
    'Microsoft Reciprocal License',
    'Microsoft TrueType Fonts EULA',
    'MIT License',
    'Mozilla Public License 1.1',
    'Net SNMP License',
    'Netscape Public License 1.1',
    'NTP License',
    'OpenSSL/SSLeay License',
    'Original SSLeay License with Windows exception',
    'RSA Data Security MD4',
    'RSA Data Security MD5',
    'SFL License Agreement',
    'SGI Free Software License B v2.0',
    'Sun RPC License',
    'TCL/TK License',
    'Tidy License',
    'University of Illinois/NCSA Open Source License',
    'X11 License',
    'ZLIB License',
)