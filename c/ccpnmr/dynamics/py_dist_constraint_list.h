
/*
======================COPYRIGHT/LICENSE START==========================

py_dist_constraint_list.h: Part of the CcpNmr Analysis program

Copyright (C) 2009 Wayne Boucher and Tim Stevens (University of Cambridge)

=======================================================================

This file contains reserved and/or proprietary information
belonging to the author and/or organisation holding the copyright.
It may not be used, distributed, modified, transmitted, stored,
or in any way accessed, except by members or employees of the CCPN,
and by these people only until 31 December 2005 and in accordance with
the guidelines of the CCPN.
 
A copy of this license can be found in ../../../license/CCPN.license.

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
*/
#ifndef _incl_py_dist_constraint_list
#define _incl_py_dist_constraint_list

#include "Python.h"

#include "macros.h"
#include "types.h"

#include "py_dist_constraint.h"
#include "dist_constraint_list.h"

typedef struct Py_Dist_constraint_list
{
    PyObject_HEAD
    int ndist_constraints;
    int ndist_constraints_alloc;
    Py_Dist_constraint *py_dist_constraints;
}   *Py_Dist_constraint_list;
 
extern Bool is_py_dist_constraint_list(PyObject *obj);

extern Dist_constraint_list get_dist_constraint_list(Py_Dist_constraint_list py_dist_constraint_list);

#endif /* _incl_py_dist_constraint_list */
