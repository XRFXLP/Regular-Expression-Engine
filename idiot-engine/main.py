from postfX import *
from utility import match


#Should work, I've not tested as I M S PDO OPDOPOEPOEPDOEPODEPODEPDOEPDOE
def fits(regex, string):
  p = postfix(regex)
  return match(p, string)
