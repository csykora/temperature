# Temperature Conversion

### Overview

This program converts temperatures from one format to another:
- Converts temperatures between the following units: Fahrenheit, Celsius, Kelvin, Rankine
- Can be utilized by science teachers as a tool to validate students homework
- The program is written with Python
- Command line arguments are used to pass in the temperature conversion information
- Temperature values are rounded to a single decimal when performing the comparision

Circleci is used to build this project, the current status is:

[![CircleCI](https://circleci.com/gh/csykora/temperature.svg?style=svg)](https://circleci.com/gh/csykora/temperature)

### Installation

- Create a work folder on the workstation that the temperature convert program will be installed into. This guide show instructions for Linux OS installaton.
- Select [the download link](https://github.com/csykora/temperature/blob/master/temperature_convert/temperature_convert.py) to download the program onto the workstation
- Insure the downloaded file has execute permissions

```
> mkdir workarea
> cd workarea
> curl -O https://github.com/csykora/temperature/blob/master/temperature_convert/temperature_convert.py
> chmod 755 temperature_convert.py
```

**NOTE:** The workstation must already have Python installed. If Python is not installed, please see other online documents for the [installation of Python onto the workstation](http://docs.python-guide.org/en/latest/starting/installation/)

### Running

The temperature_convert.py program requires multiple command line parameters to run correctly.  The order of the parameters is important and must follow this pattern:

usage: temperature_convert.py [-h] [--debug] temp_in temp_in_unit temp_target_unit student_response

positional arguments:
  temp_in           Temperature input: 84.2 Fahrenheit
  temp_target_unit  Temperature target unit: Celsius
  student_response  Temperature student response: 29

optional arguments:
  -h, --help        show this help message and exit
  --debug           Turn on debugging messages

Examples:
- python temperature_convert 84.2 Fahrenheit Rankine 543.5
- python temperature_convert 32 Fahrenheit Celcius 0

### Testing

The Python `unittest` framework is used to run the tests for this project. The tests can be found in the `test` folder, follow these steps to run the tests:
- clone the repo
- run the tests
```
> mkdir workarea
> cd workarea
> clone git@github.com:csykora/temperature.git
> cd  temperature
> python python -m unittest discover -v
```

### Issues

Any issues that are encountered should be entered into the Github project page.
