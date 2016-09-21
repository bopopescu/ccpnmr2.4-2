"""
#######################################################################

CCPN Data Model version 2.1.2

Autogenerated by PyXmlMapWrite revision 1.29 on Mon Mar  2 17:24:14 2015
  from data model element cambridge.Wms revision ?

#######################################################################
======================COPYRIGHT/LICENSE START==========================

Wms.py: python XML-I/O-mapping for CCPN data model, MetaPackage cambridge.Wms

Copyright (C) 2007  (CCPN Project)

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
Rasmus H. Fogh, Wayne Boucher, Wim F. Vranken, Anne
Pajon, Tim J. Stevens, T.N. Bhat, John Westbrook, John M.C. Ionides and
Ernest D. Laue (2005). A framework for scientific data modeling and automated
software development. Bioinformatics 21, 1678-1684.


This file was generated with the Memops software generation framework,
and contains original contributions embedded in the framework

===========================REFERENCE END===============================
"""
from memops.general.Constants import baseDataTypeModule as basicDataTypes
# 
#  Current package api
import cambridge.api.Wms

def makeMapping(globalMap):
  """
  generates XML I/O mapping for package WMS, adding it to globalMap
  """
  
  from memops.xml.Implementation import bool2str, str2bool

  # Set up top level dictionaries
  loadMaps = globalMap.get('loadMaps')
  mapsByGuid = globalMap.get('mapsByGuid')

  abstractTypes = globalMap.get('WMS').get('abstractTypes')
  exolinks = globalMap.get('WMS').get('exolinks')

  # Class Project
  currentMap = {}
  abstractTypes['Project'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2009-01-29-15:16:52_00005'] = currentMap
  loadMaps['WMS.Project'] = currentMap
  currentMap['tag'] = 'WMS.Project'
  currentMap['type'] = 'class'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2009-01-29-15:16:52_00005'
  currentMap['eType'] = 'cplx'
  currentMap['fromParent'] = 'projects'
  currentMap['objkey'] = 'name'
  currentMap['class'] = cambridge.api.Wms.Project
  contentMap = {}
  currentMap['content'] = contentMap

  # Attribute Project.applicationData
  contentMap['applicationData'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-09-14-18:48:27_00007')

  # Attribute Project.details
  currentMap = {}
  contentMap['details'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2009-01-29-15:16:56_00007'] = currentMap
  loadMaps['WMS.Project.details'] = currentMap
  currentMap['tag'] = 'WMS.Project.details'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2009-01-29-15:16:56_00007'
  currentMap['name'] = 'details'
  currentMap['hicard'] = 1
  currentMap['locard'] = 0
  currentMap['eType'] = 'cplx'
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00036')

  # Attribute Project.location
  currentMap = {}
  contentMap['location'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2009-01-29-15:16:56_00006'] = currentMap
  loadMaps['WMS.Project.location'] = currentMap
  currentMap['tag'] = 'WMS.Project.location'
  currentMap['type'] = 'dobj'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2009-01-29-15:16:56_00006'
  currentMap['name'] = 'location'
  currentMap['hicard'] = 1
  currentMap['locard'] = 1
  currentMap['eType'] = 'cplx'
  currentMap['content'] = globalMap.get('IMPL').get('abstractTypes')

  # Attribute Project.name
  currentMap = {}
  contentMap['name'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2009-01-29-15:16:56_00005'] = currentMap
  loadMaps['WMS.Project.name'] = currentMap
  currentMap['tag'] = 'WMS.Project.name'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2009-01-29-15:16:56_00005'
  currentMap['name'] = 'name'
  currentMap['hicard'] = 1
  currentMap['locard'] = 1
  currentMap['eType'] = 'cplx'
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00033')

  # Attribute Project.nmrCalcRunSerial
  currentMap = {}
  contentMap['nmrCalcRunSerial'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2010-05-06-12:26:56_00005'] = currentMap
  loadMaps['WMS.Project.nmrCalcRunSerial'] = currentMap
  currentMap['tag'] = 'WMS.Project.nmrCalcRunSerial'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2010-05-06-12:26:56_00005'
  currentMap['name'] = 'nmrCalcRunSerial'
  currentMap['hicard'] = 1
  currentMap['locard'] = 0
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:54_00001')

  # Attribute Project.nmrCalcStoreName
  currentMap = {}
  contentMap['nmrCalcStoreName'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2010-05-06-12:26:56_00004'] = currentMap
  loadMaps['WMS.Project.nmrCalcStoreName'] = currentMap
  currentMap['tag'] = 'WMS.Project.nmrCalcStoreName'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2010-05-06-12:26:56_00004'
  currentMap['name'] = 'nmrCalcStoreName'
  currentMap['hicard'] = 1
  currentMap['locard'] = 0
  currentMap['eType'] = 'cplx'
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00033')

  # Role Project.access
  contentMap['access'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-12-31-09:03:01_00014')

  # Role Project.nmrCalcInfo
  currentMap = {}
  contentMap['nmrCalcInfo'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2010-05-06-12:26:56_00003'] = currentMap
  loadMaps['WMS.Project.nmrCalcInfo'] = currentMap
  currentMap['tag'] = 'WMS.Project.nmrCalcInfo'
  currentMap['type'] = 'exolink'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2010-05-06-12:26:56_00003'
  currentMap['name'] = 'nmrCalcInfo'
  currentMap['hicard'] = 1
  currentMap['locard'] = 0
  currentMap['eType'] = 'cplx'
  currentMap['copyOverride'] = True
  currentMap['content'] = globalMap.get('CALC').get('exolinks')

  # Role Project.projectVersions
  currentMap = {}
  contentMap['projectVersions'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2009-01-29-15:16:56_00004'] = currentMap
  loadMaps['WMS.Project.projectVersions'] = currentMap
  currentMap['tag'] = 'WMS.Project.projectVersions'
  currentMap['type'] = 'child'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2009-01-29-15:16:56_00004'
  currentMap['name'] = 'projectVersions'
  currentMap['hicard'] = -1
  currentMap['locard'] = 0
  currentMap['eType'] = 'cplx'
  currentMap['content'] = globalMap.get('WMS').get('abstractTypes')

  # Role Project.rawFiles
  currentMap = {}
  contentMap['rawFiles'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2010-05-06-12:26:56_00002'] = currentMap
  loadMaps['WMS.Project.rawFiles'] = currentMap
  currentMap['tag'] = 'WMS.Project.rawFiles'
  currentMap['type'] = 'child'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2010-05-06-12:26:56_00002'
  currentMap['name'] = 'rawFiles'
  currentMap['hicard'] = -1
  currentMap['locard'] = 0
  currentMap['eType'] = 'cplx'
  currentMap['content'] = globalMap.get('WMS').get('abstractTypes')
  # End of Project

  currentMap = abstractTypes.get('Project')
  aList = ['nmrCalcRunSerial']
  currentMap['headerAttrs'] = aList
  aList = ['details', 'name', 'nmrCalcStoreName']
  currentMap['simpleAttrs'] = aList
  aList = ['rawFiles', 'projectVersions', 'access', 'location', 'applicationData']
  currentMap['cplxAttrs'] = aList
  aList = ['projectVersions', 'rawFiles']
  currentMap['children'] = aList

  # Class ProjectVersion
  currentMap = {}
  abstractTypes['ProjectVersion'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2009-01-29-15:16:52_00006'] = currentMap
  loadMaps['WMS.ProjectVersion'] = currentMap
  currentMap['tag'] = 'WMS.ProjectVersion'
  currentMap['type'] = 'class'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2009-01-29-15:16:52_00006'
  currentMap['eType'] = 'cplx'
  currentMap['fromParent'] = 'projectVersions'
  currentMap['objkey'] = 'versionTag'
  currentMap['class'] = cambridge.api.Wms.ProjectVersion
  contentMap = {}
  currentMap['content'] = contentMap

  # Attribute ProjectVersion.applicationData
  contentMap['applicationData'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-09-14-18:48:27_00007')

  # Attribute ProjectVersion.creationTime
  currentMap = {}
  contentMap['creationTime'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2009-01-29-15:16:56_00016'] = currentMap
  loadMaps['WMS.ProjectVersion.creationTime'] = currentMap
  currentMap['tag'] = 'WMS.ProjectVersion.creationTime'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2009-01-29-15:16:56_00016'
  currentMap['name'] = 'creationTime'
  currentMap['hicard'] = 1
  currentMap['locard'] = 1
  currentMap['eType'] = 'cplx'
  currentMap['proc'] = 'direct'
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00029')

  # Attribute ProjectVersion.status
  currentMap = {}
  contentMap['status'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2009-01-29-15:16:56_00015'] = currentMap
  loadMaps['WMS.ProjectVersion.status'] = currentMap
  currentMap['tag'] = 'WMS.ProjectVersion.status'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2009-01-29-15:16:56_00015'
  currentMap['name'] = 'status'
  currentMap['hicard'] = 1
  currentMap['locard'] = 0
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00037')

  # Attribute ProjectVersion.summary
  currentMap = {}
  contentMap['summary'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2010-05-06-12:26:56_00008'] = currentMap
  loadMaps['WMS.ProjectVersion.summary'] = currentMap
  currentMap['tag'] = 'WMS.ProjectVersion.summary'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2010-05-06-12:26:56_00008'
  currentMap['name'] = 'summary'
  currentMap['hicard'] = 1
  currentMap['locard'] = 0
  currentMap['eType'] = 'cplx'
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00033')

  # Attribute ProjectVersion.versionTag
  currentMap = {}
  contentMap['versionTag'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2009-01-29-15:16:56_00014'] = currentMap
  loadMaps['WMS.ProjectVersion.versionTag'] = currentMap
  currentMap['tag'] = 'WMS.ProjectVersion.versionTag'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2009-01-29-15:16:56_00014'
  currentMap['name'] = 'versionTag'
  currentMap['hicard'] = 1
  currentMap['locard'] = 1
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00037')

  # Role ProjectVersion.access
  contentMap['access'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-12-31-09:03:01_00014')

  # Role ProjectVersion.createdByTask
  currentMap = {}
  contentMap['createdByTask'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2009-03-09-12:00:17_00005'] = currentMap
  loadMaps['WMS.ProjectVersion.createdByTask'] = currentMap
  currentMap['tag'] = 'WMS.ProjectVersion.createdByTask'
  currentMap['type'] = 'link'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2009-03-09-12:00:17_00005'
  currentMap['name'] = 'createdByTask'
  currentMap['hicard'] = 1
  currentMap['locard'] = 0
  currentMap['copyOverride'] = False

  # Role ProjectVersion.outputTasks
  currentMap = {}
  contentMap['outputTasks'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2009-03-09-12:00:17_00007'] = currentMap
  loadMaps['WMS.ProjectVersion.outputTasks'] = currentMap
  currentMap['tag'] = 'WMS.ProjectVersion.outputTasks'
  currentMap['type'] = 'link'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2009-03-09-12:00:17_00007'
  currentMap['name'] = 'outputTasks'
  currentMap['hicard'] = -1
  currentMap['locard'] = 0
  currentMap['copyOverride'] = False
  # End of ProjectVersion

  currentMap = abstractTypes.get('ProjectVersion')
  aList = ['status', 'versionTag']
  currentMap['headerAttrs'] = aList
  aList = ['creationTime', 'summary', 'createdByTask', 'outputTasks']
  currentMap['simpleAttrs'] = aList
  aList = ['access', 'applicationData']
  currentMap['cplxAttrs'] = aList

  # Class RawFile
  currentMap = {}
  abstractTypes['RawFile'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2009-01-29-15:16:52_00004'] = currentMap
  loadMaps['WMS.RawFile'] = currentMap
  currentMap['tag'] = 'WMS.RawFile'
  currentMap['type'] = 'class'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2009-01-29-15:16:52_00004'
  currentMap['eType'] = 'cplx'
  currentMap['fromParent'] = 'rawFiles'
  currentMap['objkey'] = 'serial'
  currentMap['class'] = cambridge.api.Wms.RawFile
  contentMap = {}
  currentMap['content'] = contentMap

  # Attribute RawFile.applicationData
  contentMap['applicationData'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-09-14-18:48:27_00007')

  # Attribute RawFile.details
  currentMap = {}
  contentMap['details'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2009-01-29-15:16:56_00020'] = currentMap
  loadMaps['WMS.RawFile.details'] = currentMap
  currentMap['tag'] = 'WMS.RawFile.details'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2009-01-29-15:16:56_00020'
  currentMap['name'] = 'details'
  currentMap['hicard'] = 1
  currentMap['locard'] = 0
  currentMap['eType'] = 'cplx'
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00036')

  # Attribute RawFile.location
  currentMap = {}
  contentMap['location'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2009-01-29-15:16:56_00019'] = currentMap
  loadMaps['WMS.RawFile.location'] = currentMap
  currentMap['tag'] = 'WMS.RawFile.location'
  currentMap['type'] = 'dobj'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2009-01-29-15:16:56_00019'
  currentMap['name'] = 'location'
  currentMap['hicard'] = 1
  currentMap['locard'] = 1
  currentMap['eType'] = 'cplx'
  currentMap['content'] = globalMap.get('IMPL').get('abstractTypes')

  # Attribute RawFile.path
  currentMap = {}
  contentMap['path'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2009-01-29-15:16:56_00018'] = currentMap
  loadMaps['WMS.RawFile.path'] = currentMap
  currentMap['tag'] = 'WMS.RawFile.path'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2009-01-29-15:16:56_00018'
  currentMap['name'] = 'path'
  currentMap['hicard'] = 1
  currentMap['locard'] = 1
  currentMap['eType'] = 'cplx'
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:54_00003')

  # Attribute RawFile.serial
  currentMap = {}
  contentMap['serial'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2009-01-29-15:16:56_00017'] = currentMap
  loadMaps['WMS.RawFile.serial'] = currentMap
  currentMap['tag'] = 'WMS.RawFile.serial'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2009-01-29-15:16:56_00017'
  currentMap['name'] = 'serial'
  currentMap['hicard'] = 1
  currentMap['locard'] = 1
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00032')

  # Role RawFile.access
  contentMap['access'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-12-31-09:03:01_00014')
  # End of RawFile

  currentMap = abstractTypes.get('RawFile')
  aList = ['serial']
  currentMap['headerAttrs'] = aList
  aList = ['details', 'path']
  currentMap['simpleAttrs'] = aList
  aList = ['access', 'location', 'applicationData']
  currentMap['cplxAttrs'] = aList

  # Class Task
  currentMap = {}
  abstractTypes['Task'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2009-01-29-15:16:52_00007'] = currentMap
  loadMaps['WMS.Task'] = currentMap
  currentMap['tag'] = 'WMS.Task'
  currentMap['type'] = 'class'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2009-01-29-15:16:52_00007'
  currentMap['eType'] = 'cplx'
  currentMap['fromParent'] = 'tasks'
  currentMap['objkey'] = 'serial'
  currentMap['class'] = cambridge.api.Wms.Task
  contentMap = {}
  currentMap['content'] = contentMap

  # Attribute Task.applicationData
  contentMap['applicationData'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-09-14-18:48:27_00007')

  # Attribute Task.dateCompleted
  currentMap = {}
  contentMap['dateCompleted'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2009-03-09-12:00:17_00009'] = currentMap
  loadMaps['WMS.Task.dateCompleted'] = currentMap
  currentMap['tag'] = 'WMS.Task.dateCompleted'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2009-03-09-12:00:17_00009'
  currentMap['name'] = 'dateCompleted'
  currentMap['hicard'] = 1
  currentMap['locard'] = 0
  currentMap['eType'] = 'cplx'
  currentMap['proc'] = 'direct'
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00029')

  # Attribute Task.dateStarted
  currentMap = {}
  contentMap['dateStarted'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2009-03-09-12:00:17_00008'] = currentMap
  loadMaps['WMS.Task.dateStarted'] = currentMap
  currentMap['tag'] = 'WMS.Task.dateStarted'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2009-03-09-12:00:17_00008'
  currentMap['name'] = 'dateStarted'
  currentMap['hicard'] = 1
  currentMap['locard'] = 0
  currentMap['eType'] = 'cplx'
  currentMap['proc'] = 'direct'
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00029')

  # Attribute Task.nmrCalcRunSerial
  currentMap = {}
  contentMap['nmrCalcRunSerial'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2010-05-06-12:26:57_00005'] = currentMap
  loadMaps['WMS.Task.nmrCalcRunSerial'] = currentMap
  currentMap['tag'] = 'WMS.Task.nmrCalcRunSerial'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2010-05-06-12:26:57_00005'
  currentMap['name'] = 'nmrCalcRunSerial'
  currentMap['hicard'] = 1
  currentMap['locard'] = 0
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:54_00001')

  # Attribute Task.nmrCalcStoreName
  currentMap = {}
  contentMap['nmrCalcStoreName'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2010-05-06-12:26:57_00004'] = currentMap
  loadMaps['WMS.Task.nmrCalcStoreName'] = currentMap
  currentMap['tag'] = 'WMS.Task.nmrCalcStoreName'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2010-05-06-12:26:57_00004'
  currentMap['name'] = 'nmrCalcStoreName'
  currentMap['hicard'] = 1
  currentMap['locard'] = 0
  currentMap['eType'] = 'cplx'
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00033')

  # Attribute Task.operatorId
  currentMap = {}
  contentMap['operatorId'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2010-05-06-12:26:57_00002'] = currentMap
  loadMaps['WMS.Task.operatorId'] = currentMap
  currentMap['tag'] = 'WMS.Task.operatorId'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2010-05-06-12:26:57_00002'
  currentMap['name'] = 'operatorId'
  currentMap['hicard'] = 1
  currentMap['locard'] = 0
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00037')

  # Attribute Task.protocolName
  currentMap = {}
  contentMap['protocolName'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2010-05-10-13:46:55_00001'] = currentMap
  loadMaps['WMS.Task.protocolName'] = currentMap
  currentMap['tag'] = 'WMS.Task.protocolName'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2010-05-10-13:46:55_00001'
  currentMap['name'] = 'protocolName'
  currentMap['hicard'] = 1
  currentMap['locard'] = 0
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00037')

  # Attribute Task.serial
  currentMap = {}
  contentMap['serial'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2009-01-29-15:16:56_00001'] = currentMap
  loadMaps['WMS.Task.serial'] = currentMap
  currentMap['tag'] = 'WMS.Task.serial'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2009-01-29-15:16:56_00001'
  currentMap['name'] = 'serial'
  currentMap['hicard'] = 1
  currentMap['locard'] = 1
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00032')

  # Attribute Task.status
  currentMap = {}
  contentMap['status'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2009-01-29-15:16:56_00002'] = currentMap
  loadMaps['WMS.Task.status'] = currentMap
  currentMap['tag'] = 'WMS.Task.status'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2009-01-29-15:16:56_00002'
  currentMap['name'] = 'status'
  currentMap['hicard'] = 1
  currentMap['locard'] = 0
  currentMap['eType'] = 'cplx'
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00033')

  # Attribute Task.summary
  currentMap = {}
  contentMap['summary'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2010-05-06-12:26:57_00003'] = currentMap
  loadMaps['WMS.Task.summary'] = currentMap
  currentMap['tag'] = 'WMS.Task.summary'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2010-05-06-12:26:57_00003'
  currentMap['name'] = 'summary'
  currentMap['hicard'] = 1
  currentMap['locard'] = 0
  currentMap['eType'] = 'cplx'
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00033')

  # Role Task.access
  contentMap['access'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-12-31-09:03:01_00014')

  # Role Task.generatedVersion
  currentMap = {}
  contentMap['generatedVersion'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2009-03-09-12:00:17_00004'] = currentMap
  loadMaps['WMS.Task.generatedVersion'] = currentMap
  currentMap['tag'] = 'WMS.Task.generatedVersion'
  currentMap['type'] = 'link'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2009-03-09-12:00:17_00004'
  currentMap['name'] = 'generatedVersion'
  currentMap['hicard'] = 1
  currentMap['locard'] = 0
  currentMap['copyOverride'] = False

  # Role Task.inputVersion
  currentMap = {}
  contentMap['inputVersion'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2009-03-09-12:00:17_00006'] = currentMap
  loadMaps['WMS.Task.inputVersion'] = currentMap
  currentMap['tag'] = 'WMS.Task.inputVersion'
  currentMap['type'] = 'link'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2009-03-09-12:00:17_00006'
  currentMap['name'] = 'inputVersion'
  currentMap['hicard'] = 1
  currentMap['locard'] = 0
  currentMap['copyOverride'] = True

  # Role Task.nmrCalcRun
  currentMap = {}
  contentMap['nmrCalcRun'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2010-05-06-12:26:56_00010'] = currentMap
  loadMaps['WMS.Task.nmrCalcRun'] = currentMap
  currentMap['tag'] = 'WMS.Task.nmrCalcRun'
  currentMap['type'] = 'exolink'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2010-05-06-12:26:56_00010'
  currentMap['name'] = 'nmrCalcRun'
  currentMap['hicard'] = 1
  currentMap['locard'] = 0
  currentMap['eType'] = 'cplx'
  currentMap['copyOverride'] = True
  currentMap['content'] = globalMap.get('CALC').get('exolinks')
  # End of Task

  currentMap = abstractTypes.get('Task')
  aList = ['nmrCalcRunSerial', 'operatorId', 'protocolName', 'serial']
  currentMap['headerAttrs'] = aList
  aList = ['dateCompleted', 'dateStarted', 'nmrCalcStoreName', 'status', 'summary', 'generatedVersion']
  currentMap['simpleAttrs'] = aList
  aList = ['inputVersion']
  currentMap['optLinks'] = aList
  aList = ['access', 'applicationData']
  currentMap['cplxAttrs'] = aList

  # Class WmsSegment
  currentMap = {}
  abstractTypes['WmsSegment'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2009-01-29-15:16:52_00002'] = currentMap
  loadMaps['WMS.WmsSegment'] = currentMap
  currentMap['tag'] = 'WMS.WmsSegment'
  currentMap['type'] = 'class'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2009-01-29-15:16:52_00002'
  currentMap['eType'] = 'cplx'
  currentMap['fromParent'] = 'wmsSegments'
  currentMap['isTop'] = True
  currentMap['objkey'] = 'name'
  currentMap['class'] = cambridge.api.Wms.WmsSegment
  contentMap = {}
  currentMap['content'] = contentMap

  # Attribute WmsSegment.applicationData
  contentMap['applicationData'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-09-14-18:48:27_00007')

  # Attribute WmsSegment.createdBy
  contentMap['createdBy'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-12-31-09:00:59_00002__www.ccpn.ac.uk_Fogh_2007-10-03-14:53:27_00001__www.ccpn.ac.uk_Fogh_2006-09-14-16:28:57_00002')

  # Attribute WmsSegment.details
  currentMap = {}
  contentMap['details'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2010-05-06-12:26:57_00009'] = currentMap
  loadMaps['WMS.WmsSegment.details'] = currentMap
  currentMap['tag'] = 'WMS.WmsSegment.details'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2010-05-06-12:26:57_00009'
  currentMap['name'] = 'details'
  currentMap['hicard'] = 1
  currentMap['locard'] = 0
  currentMap['eType'] = 'cplx'
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00036')

  # Attribute WmsSegment.guid
  contentMap['guid'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-09-14-18:48:26_00002')

  # Attribute WmsSegment.isModifiable
  contentMap['isModifiable'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-17-14:16:26_00010__www.ccpn.ac.uk_Fogh_2007-10-03-14:53:27_00001__www.ccpn.ac.uk_Fogh_2006-09-14-16:28:57_00002')

  # Attribute WmsSegment.lastUnlockedBy
  contentMap['lastUnlockedBy'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-12-31-09:00:59_00003__www.ccpn.ac.uk_Fogh_2007-10-03-14:53:27_00001__www.ccpn.ac.uk_Fogh_2006-09-14-16:28:57_00002')

  # Attribute WmsSegment.name
  currentMap = {}
  contentMap['name'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2009-01-29-15:16:56_00034'] = currentMap
  loadMaps['WMS.WmsSegment.name'] = currentMap
  currentMap['tag'] = 'WMS.WmsSegment.name'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2009-01-29-15:16:56_00034'
  currentMap['name'] = 'name'
  currentMap['hicard'] = 1
  currentMap['locard'] = 1
  currentMap['eType'] = 'cplx'
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00033')

  # Role WmsSegment.access
  contentMap['access'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-12-31-09:03:01_00014')

  # Role WmsSegment.projects
  currentMap = {}
  contentMap['projects'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2009-01-29-15:16:56_00031'] = currentMap
  loadMaps['WMS.WmsSegment.projects'] = currentMap
  currentMap['tag'] = 'WMS.WmsSegment.projects'
  currentMap['type'] = 'child'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2009-01-29-15:16:56_00031'
  currentMap['name'] = 'projects'
  currentMap['hicard'] = -1
  currentMap['locard'] = 0
  currentMap['eType'] = 'cplx'
  currentMap['implSkip'] = True
  currentMap['content'] = globalMap.get('WMS').get('abstractTypes')

  # Role WmsSegment.tasks
  currentMap = {}
  contentMap['tasks'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2009-01-29-15:16:56_00033'] = currentMap
  loadMaps['WMS.WmsSegment.tasks'] = currentMap
  currentMap['tag'] = 'WMS.WmsSegment.tasks'
  currentMap['type'] = 'child'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2009-01-29-15:16:56_00033'
  currentMap['name'] = 'tasks'
  currentMap['hicard'] = -1
  currentMap['locard'] = 0
  currentMap['eType'] = 'cplx'
  currentMap['implSkip'] = True
  currentMap['content'] = globalMap.get('WMS').get('abstractTypes')
  # End of WmsSegment

  currentMap = abstractTypes.get('WmsSegment')
  aList = ['createdBy', 'guid', 'isModifiable', 'lastUnlockedBy']
  currentMap['headerAttrs'] = aList
  aList = ['details', 'name']
  currentMap['simpleAttrs'] = aList
  aList = ['tasks', 'projects', 'access', 'applicationData']
  currentMap['cplxAttrs'] = aList
  aList = ['projects', 'tasks']
  currentMap['children'] = aList

  # Out-of-package link to Project
  currentMap = {}
  exolinks['Project'] = currentMap
  loadMaps['WMS.exo-Project'] = currentMap
  currentMap['tag'] = 'WMS.exo-Project'
  currentMap['type'] = 'exo'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2009-01-29-15:16:52_00005'
  currentMap['name'] = 'Project'
  currentMap['eType'] = 'cplx'
  currentMap['class'] = cambridge.api.Wms.Project
  aList = list()
  currentMap['keyMaps'] = aList
  aList.append(mapsByGuid.get('www.ccpn.ac.uk_Fogh_2008-06-30-16:30:50_00001'))
  aList.append(mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00033'))

  # Out-of-package link to ProjectVersion
  currentMap = {}
  exolinks['ProjectVersion'] = currentMap
  loadMaps['WMS.exo-ProjectVersion'] = currentMap
  currentMap['tag'] = 'WMS.exo-ProjectVersion'
  currentMap['type'] = 'exo'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2009-01-29-15:16:52_00006'
  currentMap['name'] = 'ProjectVersion'
  currentMap['eType'] = 'cplx'
  currentMap['class'] = cambridge.api.Wms.ProjectVersion
  aList = list()
  currentMap['keyMaps'] = aList
  aList.append(mapsByGuid.get('www.ccpn.ac.uk_Fogh_2008-06-30-16:30:50_00001'))
  aList.append(mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00033'))
  aList.append(mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00037'))

  # Out-of-package link to RawFile
  currentMap = {}
  exolinks['RawFile'] = currentMap
  loadMaps['WMS.exo-RawFile'] = currentMap
  currentMap['tag'] = 'WMS.exo-RawFile'
  currentMap['type'] = 'exo'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2009-01-29-15:16:52_00004'
  currentMap['name'] = 'RawFile'
  currentMap['eType'] = 'cplx'
  currentMap['class'] = cambridge.api.Wms.RawFile
  aList = list()
  currentMap['keyMaps'] = aList
  aList.append(mapsByGuid.get('www.ccpn.ac.uk_Fogh_2008-06-30-16:30:50_00001'))
  aList.append(mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00033'))
  aList.append(mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00032'))

  # Out-of-package link to Task
  currentMap = {}
  exolinks['Task'] = currentMap
  loadMaps['WMS.exo-Task'] = currentMap
  currentMap['tag'] = 'WMS.exo-Task'
  currentMap['type'] = 'exo'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2009-01-29-15:16:52_00007'
  currentMap['name'] = 'Task'
  currentMap['eType'] = 'cplx'
  currentMap['class'] = cambridge.api.Wms.Task
  aList = list()
  currentMap['keyMaps'] = aList
  aList.append(mapsByGuid.get('www.ccpn.ac.uk_Fogh_2008-06-30-16:30:50_00001'))
  aList.append(mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00032'))

  # Out-of-package link to WmsSegment
  currentMap = {}
  exolinks['WmsSegment'] = currentMap
  loadMaps['WMS.exo-WmsSegment'] = currentMap
  currentMap['tag'] = 'WMS.exo-WmsSegment'
  currentMap['type'] = 'exo'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2009-01-29-15:16:52_00002'
  currentMap['name'] = 'WmsSegment'
  currentMap['eType'] = 'cplx'
  currentMap['class'] = cambridge.api.Wms.WmsSegment
  aList = list()
  currentMap['keyMaps'] = aList
  aList.append(mapsByGuid.get('www.ccpn.ac.uk_Fogh_2008-06-30-16:30:50_00001'))
