[![Python 3.7](https://img.shields.io/badge/python-3.7-brightgreen.svg)](#prerequisites)  [![license](https://img.shields.io/badge/license-MIT%20License-blue.svg)](LICENSE)

# Dataset Explorer
This repo provides a simple proof of concept for using the Python package [SASPy](https://sassoftware.github.io/saspy/) to incorporate SAS output into a web application using the Flask framework.

This application is intended to run and be accessed locally in debug mode.

All development was done under Windows 10 with Python 3.7 and SAS 9.4 locally installed. Any deviations from this setup might require modifications of application code.

## Getting Started

1. Download this repo.
2. Follow the instructions in [sascfg_personal-example.py](sascfg_personal-example.py) to create a file called `sascfg_personal.py` in the repo directory.
3. Run the file `app.py`.
4. Visit http://127.0.0.1:8000/ in a web browser.

## Prerequisites

This application assumes a reasonably current version of Python 3 is installed, along with the modules specified in [requirements.txt](requirements.txt).

This application also requires access to an installation of SAS 9.4 ([https://www.sas.com/en_us/software/sas9.html](https://www.sas.com/en_us/software/sas9.html)).

## License
This project is licensed under the MIT License; see the [LICENSE](LICENSE) file for details.

## Author
* [ilankham](https://github.com/ilankham)

## Disclaimer

This project is in no way affiliated with SAS Institute Inc.
