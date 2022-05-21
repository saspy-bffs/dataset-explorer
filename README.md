[![Python 3.10](https://img.shields.io/badge/python-3.10-brightgreen.svg)](#prerequisites)  [![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)  [![Gitter](https://img.shields.io/gitter/room/saspy-bffs/community.svg?color=777777)](https://gitter.im/saspy-bffs/community)

# Dataset Explorer
This project provides a proof of concept for incorporating SAS output into a Python-based web application using the Python package [SASPy](https://sassoftware.github.io/saspy/).

This application is intended to run and be accessed locally in debug mode.

All development was done under Windows 10 with SAS 9.4, Java SE version 8 update 201, Python 3.10.4, Git 2.33.1, and PyCharm 2021.2.3 installed. Any deviations from this setup may require modifications to the steps below and/or to application code.

## Online Demo

A [Google Colab Notebook](https://colab.research.google.com/drive/1F0iyLLoUyWfPDUjgC0y1j4cowDotRAPy#offline=true&sandboxMode=true) is available if you'd like to try a version of this application without downloading the repo or configuring a connection to a local SAS installation.

## Prerequisites

This application assumes a reasonably current version of Python 3 is installed, along with the modules specified in [requirements.txt](requirements.txt).

This application also requires access to installations of Java SE ([https://www.oracle.com/technetwork/java/javase/](https://www.oracle.com/technetwork/java/javase/)) and SAS 9.4 ([https://support.sas.com/software/94/](https://support.sas.com/software/94/))

## Getting Started (Quick)

1. Download this code repository.
2. Follow the instructions in _[sascfg_personal-example.py](sascfg_personal-example.py)_ to create a file called `sascfg_personal.py` in the project directory.
3. Run the file `app.py`.
4. Visit http://127.0.0.1:8000/ in a web browser.

## Getting Started (Detailed and Highly Opinionated)

### Setup development environment

1. Download and install Java SE from https://www.java.com/

2. Download and install Python from https://www.python.org/

3. Download and install Git from https://git-scm.com/

4. Download and install PyCharm from https://www.jetbrains.com/pycharm/

### Setup project in PyCharm

1. Clone this repo in PyCharm:

    * If PyCharm is running with no projects open, create a new project by selecting _Get from VCS_ and entering this repo's URL (https://github.com/saspy-bffs/dataset-explorer)

    * Otherwise, if a project is already open, use the **Git Menu**: Git -> Clone -> https://github.com/saspy-bffs/dataset-explorer
 
2. When prompted, create a new virtual environment, and make sure the file `requirements.txt` from the cloned repo is selected under _Dependencies_.

3. Use the project-navigation area in the left-hand panel to open the file `sascfg_personal-example.py` (e.g., by double-clicking its name).

4. Copy the contents of `sascfg_personal-example.py` to the system clipboard.

5. Create a new Python file named `sascfg_personal.py` in the project directory using the **File Menu** : File -> New -> Python File

6. Update line 14 of `sascfg_personal.py`, per the instructions in the file.

### Run Dataset Explorer in PyCharm

1. Use the project-navigation area in the left-hand panel to open the file `app.py` (e.g., by double-clicking its name).

2. Launch the application using the **Run Menu**: Run -> Run... -> app

3. Visit the URL http://127.0.0.1:8000/ in a web browser, and follow the instructions.

Note: If SAS was installed with default options, try the directory `C:\Program Files\SASHome\SASFoundation\9.4\core\sashelp`.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Authors
* [ilankham](https://github.com/ilankham)
* [mtslaugh](https://github.com/mtslaugh)

## Disclaimer

This project is in no way affiliated with SAS Institute Inc.
