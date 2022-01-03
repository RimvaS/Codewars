import re

def valid_number(n):
    return bool(re.fullmatch('[+-]?\d*\.\d\d', n))
  
  
  """
  import re

def valid_number(input_str):
    return re.match(r"""
        [+-]?   # optional +/- sign
        \d*     # optional digits
        \.      # decimal point
        \d\d    # two digits
        $       # end of string
        """, input_str, re.VERBOSE) is not None
  """
