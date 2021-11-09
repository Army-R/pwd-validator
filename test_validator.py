# Unit testing
# Run with the -s flag

import pwd_validation as pv
import string

success = "SUCCESS: The password"
error = "ERROR: The password"
default = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
punct = string.punctuation


def test_bl():
	""" Test the blank rule """
	assert pv.blanks("abc") == f"{success} has no blanks"
	assert pv.blanks("a b") == f"{error} must not have spaces"
	assert pv.blanks(" ") == f"{error} must not have spaces"

def test_len():
	""" Test the length rule """
	# Set the rule values
	eight = default[:8]
	sixteen = default[:16]
	seven = default[:7]
	seventeen = default[:17]
	# Test
	assert pv.length(eight) == f"{success} have between 8 and 16 characters"
	assert pv.length(sixteen) == f"{success} have between 8 and 16 characters"
	assert pv.length(seven) == f"{error} must be between 8 and 16 characters"
	assert pv.length(seventeen) == f"{error} must be between 8 and 16 characters"

def test_spcl():
	""" Test the special character rule """
	assert pv.special(punct) == f"{success} have at least 1 special character"
	assert pv.special(default) == f"{error} must have at least 1 special character"

def test_num():
	""" Test the number character rule """
	assert pv.number(num) == f"{success} have at leas 1 number"
	assert pv.number(default) == f"{error} must have at least 1 number"

def test_upper():
	""" Test the uppercase character test """
	assert pv.uppercase(upper) == f"{success} have at least 1 uppercase"
	assert pv.uppercase(default) == f"{error} must have at least 1 uppercase"
