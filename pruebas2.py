import sys

boundaries = [0, 3, 3, 5]

y = boundaries.copy()
print(y[-2])
print(y[1])

clen = y[-2] - y[1]

print(y)
print(clen)

sys.exit()

#y = (boundaries - boundaries[0])
#y = y / (boundaries[-1] - boundaries[0])
#clen = y[-2] - y[1]
#
#print(y)
#print(clen)
#
#sys.exit()
# else

dd

# aqui peta porque clen es 0:
clen = y[-2] - y[1]
automin = (y[2] - y[1]) / clen
automax = (y[-2] - y[-3]) / clen


if isinstance(self.norm, colors.BoundaryNorm):
    y = (self._boundaries - self._boundaries[0])
    y = y / (self._boundaries[-1] - self._boundaries[0])
else:
    y = self.norm(self._boundaries.copy())
if self.extend == 'min':
    # Exclude leftmost interval of y.
    clen = y[-1] - y[1]
    automin = (y[2] - y[1]) / clen
    automax = (y[-1] - y[-2]) / clen
elif self.extend == 'max':
    # Exclude rightmost interval in y.
    clen = y[-2] - y[0]
    automin = (y[1] - y[0]) / clen
    automax = (y[-2] - y[-3]) / clen
else:
    # Exclude leftmost and rightmost intervals in y.
    clen = y[-2] - y[1]
    automin = (y[2] - y[1]) / clen
    automax = (y[-2] - y[-3]) / clen