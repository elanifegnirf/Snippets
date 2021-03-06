#!/usr/bin/env python
# -*- coding: utf-8 -*-

#**********************************************************************************************************************
#
# Copyright (C) 2009 - 2012 - Thomas Mansencal - thomas.mansencal@gmail.com
#
#**********************************************************************************************************************

"""
**Constants.py**

**Platform:**
	Windows, Linux, Mac Os X.

**Description:**
	Snippets constants Module.

**Others:**

"""

#**********************************************************************************************************************
#***	Module attributes.
#**********************************************************************************************************************
__author__ = "Thomas Mansencal"
__copyright__ = "Copyright (C) 2010 - 2012 - Thomas Mansencal"
__license__ = "GPL V3.0 - http://www.gnu.org/licenses/"
__maintainer__ = "Thomas Mansencal"
__email__ = "thomas.mansencal@gmail.com"
__status__ = "Production"

__all__ = ["Constants"]

#**********************************************************************************************************************
#***	Module classes and definitions.
#**********************************************************************************************************************
class Constants():
	"""
	This class is the **Constants** class.
	"""

	logger = "Snippets_Logger"
	verbosityLevel = 3
	loggingSeparators = "*" * 96

	libraryExtension = "py"
	libraryCompiledExtension = "pyc"

	librariesDirectory = "libraries"
	resourcesDirectory = "resources"

	nullObject = "None"
