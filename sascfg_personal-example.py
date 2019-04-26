# Setup steps for Windows 10 with Java SE and SAS 9.4 locally installed:
#
# (1) Make a copy of this file called "sascfg_personal.py" in the same directory as this project.
#
# (2) Fill in the value of JAVA_CLASSES_PATH below with the directory for the files
#     sas.svc.connection.jar, log4j.jar, sas.security.sspi.jar, and sas.core.jar associated with
#     SASDeploymentManager on your local machine. If default options were used when SAS was installed,
#     this should be a path like the following:
#
#     C:\Program Files\SASHome\SASDeploymentManager\9.4\products\deploywiz__94492__prt__xx__sp0__1\deploywiz
#
#     However, depending on your SAS version (or maintenance release), the second-to-last portion
#     deploywiz__94492__prt__xx__sp0__1 might differ.
#
# (3) Fill in the value of SASEXT_PATH below with the path to the directory containing the file
#     sspiauth.dll file on your local machine. If default options were used when SAS was installed,
#     this should be a path like the following:
#
#     C:\Program Files\SASHome\SASFoundation\9.4\core\sasext
#
# (4) Fill in the value of SITE_PACKAGES_PATH below with the path to the site-packages directory
#     for a Python 3 installation with SASPy installed. For example, if your project folder is at
#     the root level of your C:\ drive and you've created a virtual environment called venv, this
#     should be a path like the following:
#
#     C:\dataset-explorer\venv\Lib\site-packages
#
# For more information, see https://sassoftware.github.io/saspy/install.html
#
# See also https://github.com/sassoftware/saspy/blob/master/saspy/sascfg.py for documentation of other
# possible configuration options.


import os

# Fill in the paths below, and remove the square brackets. The r-prefix means "raw string",
# allowing non-escaped back slashes to be used. (In other words, without the r-prefix, each
# back slash would need to be doubled up, such as in 'C:\\Program Files\\SASHome\\'.)
JAVA_CLASSES_PATH = r'[FILL IN WITH YOUR LOCAL FILE PATH AND REMOVE THE SQUARE BRACKETS]'
SASEXT_PATH = r'[FILL IN WITH YOUR LOCAL FILE PATH AND REMOVE THE SQUARE BRACKETS]'
SITE_PACKAGES_PATH = r'[FILL IN WITH YOUR LOCAL FILE PATH AND REMOVE THE SQUARE BRACKETS]'


JAVA_CLASSES = [
    JAVA_CLASSES_PATH + r'\sas.svc.connection.jar',
    JAVA_CLASSES_PATH + r'\log4j.jar',
    JAVA_CLASSES_PATH + r'\sas.security.sspi.jar',
    JAVA_CLASSES_PATH + r'\sas.core.jar',
    SITE_PACKAGES_PATH + r'\saspy\java\saspyiom.jar',
]
WIN_LOCAL_SASPY_CONFIG = {
    'java': 'java',
    'encoding': 'windows-1252',
    'classpath': ';'.join(JAVA_CLASSES)
}

SAS_config_names = ['WIN_LOCAL_SASPY_CONFIG']

os.environ['PATH'] += ';' + SASEXT_PATH
