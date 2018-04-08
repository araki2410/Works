#!/usr/bin/python

import numpy as np
import random

newers = random.sample(xrange(31+1), 4).sort()
print newers
newers.sort()
print newers
print ",".join(map(str, newers))

print "\n"

styles = np.random.randint(0,31,4)
print styles
styles.sort()
print styles
print ",".join(map(str, styles))
