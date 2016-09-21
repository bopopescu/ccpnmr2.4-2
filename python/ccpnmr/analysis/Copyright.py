
"""
======================COPYRIGHT/LICENSE START==========================

Copyright.py: Part of the CcpNmr Analysis program

Copyright (C) 2003-2010 Wayne Boucher and Tim Stevens (University of Cambridge)

=======================================================================

The CCPN license can be found in ../../../license/CCPN.license.

======================COPYRIGHT/LICENSE END============================

for further information, please contact :

- CCPN website (http://www.ccpn.ac.uk/)

- email: ccpn@bioc.cam.ac.uk

- contact the authors: wb104@bioc.cam.ac.uk, tjs23@cam.ac.uk
=======================================================================

If you are using this software for academic purposes, we suggest
quoting the following references:

===========================REFERENCE START=============================
R. Fogh, J. Ionides, E. Ulrich, W. Boucher, W. Vranken, J.P. Linge, M.
Habeck, W. Rieping, T.N. Bhat, J. Westbrook, K. Henrick, G. Gilliland,
H. Berman, J. Thornton, M. Nilges, J. Markley and E. Laue (2002). The
CCPN project: An interim report on a data model for the NMR community
(Progress report). Nature Struct. Biol. 9, 416-418.

Wim F. Vranken, Wayne Boucher, Tim J. Stevens, Rasmus
H. Fogh, Anne Pajon, Miguel Llinas, Eldon L. Ulrich, John L. Markley, John
Ionides and Ernest D. Laue (2005). The CCPN Data Model for NMR Spectroscopy:
Development of a Software Pipeline. Proteins 59, 687 - 696.

===========================REFERENCE END===============================

"""
from memops.general.Version import getVersion
from ccpnmr.analysis.Version import version, timestamp

from memops.universal.Util import isWindowsOS

if isWindowsOS():
  from ccpnmr.analysis.Version import build
else:
  build = ''

suite = 'CcpNmr'
program = 'Analysis'
copyright = 'Copyright 2003-2014 CCPN'
version = getVersion(version, timestamp, name=program)
vendorAddress = 'Department of Biochemistry, Cambridge CB2 1GA, UK'
vendorName = 'CCPN'
vendorWebAddress = 'http://www.ccpn.ac.uk'
details = 'The CCPN NMR assignment and data analysis application'
