#                                               -*- Autoconf -*-
# Process this file with autoconf to produce a configure script.

AC_PREREQ([2.69])
AC_INIT([project], [1.0], [roggero@eurecom.fr])
AM_INIT_AUTOMAKE([1.9 foreign])
AC_CONFIG_SRCDIR([src/lib_foo/foo.c])
AC_CONFIG_HEADERS([config.h])

# Checks for programs.
AC_PROG_CC
AC_PROG_RANLIB

# Checks for libraries.
# found at https://stackoverflow.com/questions/28031742/test-if-a-function-accept-one-or-two-parameter-in-configure-ac
AC_COMPILE_IFELSE([AC_LANG_PROGRAM([[#include <mistery.h>]],[[mistery_value(2);]])],[AC_DEFINE([MISTERY_VALUE_ONEPARAM], [42], [The famous answer])],[])
AC_SEARCH_LIBS([mystery_value], [mystery voodoo magic], [], [AC_MSG_ERROR([unable to find the mystery_value function])])

# Checks for header files.

# Checks for typedefs, structures, and compiler characteristics.

# Checks for library functions.

AC_CONFIG_FILES([Makefile
                  src/Makefile
                  src/lib_foo/Makefile
                  src/main/Makefile])
AC_OUTPUT
