#                                               -*- Autoconf -*-
#
# $Id: configure.ac,v 1.19 2005/02/07 21:37:16 marga Exp $
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

# Process this file with autoconf to produce a configure script.

AC_PREREQ(2.57)
AC_INIT(uisp, 20050207, uisp-dev@nongnu.org)
AC_CONFIG_SRCDIR([src/Main.C])
AC_CONFIG_HEADER([src/config.h:src/config-h.in])
AM_INIT_AUTOMAKE

# Checks for programs.
AC_PROG_CXX
AC_PROG_CC

# Checks for libraries.

# Checks for header files.
AC_HEADER_STDC
AC_CHECK_HEADERS([fcntl.h inttypes.h stdlib.h string.h sys/ioctl.h sys/time.h termios.h unistd.h])

# Checks for typedefs, structures, and compiler characteristics.
AC_HEADER_STDBOOL
AC_C_CONST
AC_TYPE_SIZE_T
AC_HEADER_TIME

# Checks for library functions.
AC_PROG_GCC_TRADITIONAL
AC_FUNC_MALLOC
AC_FUNC_MEMCMP
AC_FUNC_SELECT_ARGTYPES
AC_FUNC_STRTOD
AC_FUNC_VPRINTF
AC_CHECK_FUNCS([gettimeofday memset select strcasecmp strncasecmp strstr strtol])

# Set the DATE variable for the man page
DATE=`date "+%B, %Y"`
AC_SUBST(DATE)

AC_CONFIG_FILES([Makefile
                 uisp.1
                 uisp.spec
                 src/Makefile])
AC_OUTPUT
