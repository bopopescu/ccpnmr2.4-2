
"""
======================COPYRIGHT/LICENSE START==========================

Io.py: code for CCPN data model and code generation framework

Copyright (C) 2011  (CCPN Project)

=======================================================================

This library is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 2.1 of the License, or (at your option) any later version.
 
A copy of this license can be found in ../../../license/LGPL.license
 
This library is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
Lesser General Public License for more details.
 
You should have received a copy of the GNU Lesser General Public
License along with this library; if not, write to the Free Software
Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA


======================COPYRIGHT/LICENSE END============================

for further information, please contact :

- CCPN website (http://www.ccpn.ac.uk/)

- email: ccpn@bioc.cam.ac.uk

=======================================================================

If you are using this software for academic purposes, we suggest
quoting the following references:

===========================REFERENCE START=============================
R. Fogh, J. Ionides, E. Ulrich, W. Boucher, W. Vranken, J.P. Linge, M.
Habeck, W. Rieping, T.N. Bhat, J. Westbrook, K. Henrick, G. Gilliland,
H. Berman, J. Thornton, M. Nilges, J. Markley and E. Laue (2002). The
CCPN project: An interim report on a data model for the NMR community
(Progress report). Nature Struct. Biol. 9, 416-418.

Rasmus H. Fogh, Wayne Boucher, Wim F. Vranken, Anne
Pajon, Tim J. Stevens, T.N. Bhat, John Westbrook, John M.C. Ionides and
Ernest D. Laue (2005). A framework for scientific data modeling and automated
software development. Bioinformatics 21, 1678-1684.

===========================REFERENCE END===============================

"""

import operator

#from ccpnmr.analysis.core import AssignmentBasic
#from ccp.util import Assignment as AssignmentUtil
from pdbe.nmrStar.IO import Ccpn2NmrStar

entryName = '_ccpn_temp'

class NmrStarWrapper:
  """ Adapter class to allow IO without explicit creation of Entry
  """
  
  def __init__(self, project):
    self.project = project
    self.IOkeywords = {}
  
  def writeShifts(self, filePath, measurementList, **kw):
    """ Write talos format shift list
    """
    
    # first make temporary entry
    entryStore = (self.project.findFirstNmrEntryStore(name=entryName) or
                  self.project.newNmrEntryStore(name=entryName))
    try:
      entry = entryStore.newEntry(name=entryName)
      entry.measurementLists = (measurementList,)
      entry.molSystem = getMolSystem(measurementList)
      Ccpn2NmrStar.writeNmrStarFile(entry, filePath, nmrStarVersion='3.0')
    finally:
      entryStore.delete()
    
def getMolSystem(measurementList):
  """ Get MolSystem the fits MeasurementList
  """
  for shift in measurementList.sortedMeasurements():
    resSet = shift.resonance.resonanceSet
    if resSet is not None:
      molSystem = resSet.findFirstAtomSet().findFirstAtom().topObject
      break
  else:
    molSystem = None
  
  #
  return molSystem
