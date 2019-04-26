[![Python 3.7](https://img.shields.io/badge/python-3.7-brightgreen.svg)](#prerequisites)  [![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)  [![Gitter](https://img.shields.io/gitter/room/saspy-bffs/community.svg?color=777777)](https://gitter.im/saspy-bffs/community)

# Dataset Explorer
This project provides a proof of concept for using the Python package [SASPy](https://sassoftware.github.io/saspy/) to incorporate SAS output into a Python-based web application.

This application is intended to run and be accessed locally in debug mode.

All development was done under Windows 10 with Python 3.7 and SAS 9.4 locally installed. Any deviations from this setup might require modifications to application code.

## Getting Started

1. Download this code repository.
2. Follow the instructions in [sascfg_personal-example.py](sascfg_personal-example.py) to create a file called `sascfg_personal.py` in the project directory.
3. Run the file `app.py`.
4. Visit http://127.0.0.1:8000/ in a web browser.

## Prerequisites

This application assumes a reasonably current version of Python 3 is installed, along with the modules specified in [requirements.txt](requirements.txt).

This application also requires access to installations of Java SE ([https://www.oracle.com/technetwork/java/javase/](https://www.oracle.com/technetwork/java/javase/)) and SAS 9.4 ([https://www.sas.com/en_us/software/sas9.html](https://www.sas.com/en_us/software/sas9.html)).

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Authors
* [ilankham](https://github.com/ilankham)
* [mtslaugh](https://github.com/mtslaugh)

## Disclaimer

This project is in no way affiliated with SAS Institute Inc.
