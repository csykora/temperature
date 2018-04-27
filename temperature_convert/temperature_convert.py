# Convert between different temperature units
import argparse
import sys

# call into existing API
# http://webservices.daehosting.com/services/TemperatureConversions.wso  (only F to C) shucks

# Also wasn't sure if I could just use an existing python library
# If so, I did find pint: https://pypi.org/project/Pint/
# Anyway, I'll write my own

valid_units = ['Fahrenheit', 'Celsius', 'Kelvin', 'Rankine']

# Check temp_in matches valid formats
def valid_temp_in(temp_in, debug):
    # Must contain exactly 2 items
    try:
        if ( len(temp_in) != 2 ):
            raise ValueError
    except ValueError:
        if debug:
            print ("ERROR: --temp_in There must be only 2 values: <num> <unit>  (Ex. 84.2 Fahrenheit)")
        sys.exit("invalid")

    # Item 1 must be a number
    try:
        float(temp_in[0])
    except:
        if debug:
            print ("ERROR: --temp_in Temperature value must be a number: <num> <unit>  (Ex. 84.2 Fahrenheit)")
        sys.exit("invalid")

    # Second item must be a valid unit
    if ( temp_in[1] not in valid_units ):
        if debug:
            print ("ERROR: --temp_in Temperature unit must match: Fahrenheit, Celsius, Kelvin, Rankine")
        sys.exit("invalid")

    return True

# Check student_response is valid format
def valid_student_response(student_response, debug):
    # must be a number
    try:
        float(student_response)
    except:
        if debug:
            print ("ERROR: --student_response must be a number (Ex. 84.2)")
        sys.exit("incorrect")
    return True

# Check temperature targer unit is valid format
def valid_temp_target_unit(temp_unit, debug):
    if not temp_unit in valid_units:
        if debug:
            print ("ERROR: --temp_target_unit must be one of the following", valid_units)
        sys.exit("invalid")
    return True

# Convert to base unit of Fahrenheit then calculate all other units
def convert_temp_units(temp_value, temp_unit, debug):
    temps = {}

    if temp_unit == 'Fahrenheit':
        base_f_temp = temp_value
    elif temp_unit == 'Celsius':
        base_f_temp = temp_value * 9/5 + 32
    elif temp_unit == 'Kelvin':
        base_f_temp = temp_value * 9/5 - 459.67
    elif temp_unit == 'Rankine':
        base_f_temp = temp_value - 459.67
    else:
        sys.exit("invalid")

    # Calculate all temp units
    temps["Fahrenheit"] = base_f_temp
    temps["Celsius"] = (base_f_temp - 32) * 5/9
    temps["Kelvin"] = (base_f_temp + 459.67) * 5/9
    temps["Rankine"] = base_f_temp + 459.67

    if debug:
        for key,value in temps.items():
            print key, "=>", value

    return temps

# Check the student response for correctness
def check_correctness(temp_target_unit, student_response, temp, debug):

    if round(temp[temp_target_unit],1) == round(float(student_response),1):
#        sys.exit("correct")
        return("correct")
    else:
        if debug:
            print "INCORRECT: Temp ", round(temp[temp_target_unit],1), "Student Response: ", round(float(student_response),1)
        sys.exit("incorrect")

def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('temp_in', type=str, nargs='+',
                        help='Temperature input: 84.2 Fahrenheit')
    parser.add_argument('temp_target_unit', # not sure how to return invalid choices=valid_units,
                        help='Temperature target unit: Celsius')
    parser.add_argument('student_response', # not sure how to return invalid type=float,
                        help='Temperature student response: 29')
    parser.add_argument('--debug', action="store_true", help='Turn on debugging messages')
    return parser

# Main
def main():
    parser = create_parser()
    args = parser.parse_args()

    # Additional validation of input parameters
    valid_temp_in(args.temp_in, args.debug)
    valid_student_response(args.student_response, args.debug)
    valid_temp_target_unit(args.temp_target_unit, args.debug)

    # Check student response for correctness
    print check_correctness(args.temp_target_unit, args.student_response, convert_temp_units( float(args.temp_in[0]), args.temp_in[1], args.debug ), args.debug)

if __name__ == '__main__':
    main()
