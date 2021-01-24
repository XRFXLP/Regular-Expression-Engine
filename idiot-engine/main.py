from postfX import *
from utility import match

#this won't work :P
#Should work, I've not tested as I M S PDO OPDOPOEPOEPDOEPODEPODEPDOEPDOE
def fits(regex, string):
  p = postfix(regex)
  return match(p, string)
