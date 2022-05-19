# Setup steps for Windows 10 with Java SE and SAS 9.4 locally installed:
#
# (1) Make a copy of this file called "sascfg_personal.py" in the same directory
# as this project.
#
# (2) Locate the file sspiauth.dll in your local SAS installation. If default
# options were used when SAS was installed, this should be a path like the
# following:
#
#     C:\Program Files\SASHome\SASFoundation\9.4\core\sasext
#
# (3) Fill in the path below, and remove the square brackets:

SASEXT_PATH = r'[FILL IN WITH YOUR LOCAL FILE PATH AND REMOVE THE SQUARE BRACKETS]'

# For reference, here's an example of a properly set SASEXT_PATH when SAS was
# installed with default options:
#
# SASEXT_PATH = r'C:\Program Files\SASHome\SASFoundation\9.4\core\sasext'
#
# Note: The r-prefix means "raw string". This allows non-escaped back slashes to
# be used. In other words, without the r-prefix, each back slash would need to
# be doubled up, such as in 'C:\\Program Files\\SASHome\\'.
#
# For more information about SASPy configuration, including other connection
# options, see the following:
#
#     https://sassoftware.github.io/saspy/configuration.html
#
#     https://github.com/sassoftware/saspy/blob/master/saspy/sascfg.py

import os

WIN_LOCAL_SASPY_CONFIG = {
    'java': 'java',
}

SAS_config_names = ['WIN_LOCAL_SASPY_CONFIG']

os.environ['PATH'] += ';' + SASEXT_PATH
