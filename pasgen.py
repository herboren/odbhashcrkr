import random
from string import *

def pasgen(length):
    return "".join(random.sample("".join([ascii_lowercase,ascii_uppercase,digits]), length))