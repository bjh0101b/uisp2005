#
# $Id: Makefile.am,v 1.9 2004/05/11 16:47:19 troth Exp $
#
# uisp - The Micro In-System Programmer for Atmel AVR microcontrollers.
# Copyright (C) 2002, 2003, 2004  Theodore A. Roth
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
# Makefile.am -- Process this file with automake to produce Makefile.in
#

AUX_DIST             = install-sh missing mkinstalldirs depcomp

man_MANS             = uisp.1

AUX_DIST_EXTRA       = 
EXTRA_DIST           = bootstrap \
                       CHANGES CHANGES.old \
                       kernel/patch-2.2.17-ppdev1.gz \
                       pavr/Makefile pavr/pavr.c \
                       doc/HOWTO.windows doc/README.stk500 \
                       doc/README.xilinx \
                       doc/README.rs232 \
                       doc/uisp-parport-connect.txt \
                       uisp.1.in \
                       ChangeLog-2002 \
                       ChangeLog-2003

SUBDIRS              = src
DIST_SUBDIRS         = src

MAINTAINERCLEANFILES = Makefile.in aclocal.m4 configure src/config-h.in \
                       src/stamp-h.in $(AUX_DIST)

install_aux_files    = AUTHORS COPYING INSTALL CHANGES CHANGES.old TODO \
                       ChangeLog ChangeLog-2003 ChangeLog-2002

DOC_INST_DIR         = $(DESTDIR)$(datadir)/doc/uisp-$(VERSION)

install-data-local:
	$(mkinstalldirs) $(DOC_INST_DIR)
	for file in $(install_aux_files) ; do \
	  echo " $(INSTALL_DATA) $$file $(DOC_INST_DIR)/$$file"; \
	  $(INSTALL_DATA) $(srcdir)/$$file $(DOC_INST_DIR)/$$file; \
	done

uninstall-local:
	rm -rf $(DOC_INST_DIR)

dist-hook: uisp.spec
	cp uisp.spec $(distdir)/uisp.spec
