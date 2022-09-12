class Y:
    def __init__(self, astring):
        self.s = astring

    @classmethod # classmethod to build a factory / alternative constructor
    def fromlist(cls, alist):
      x = cls('')
      x.s = ','.join(str(s) for s in alist)
      return x

    def __repr__(self):
      return f'y({self.s})'

# subclassing of Y - .fromlist() still works
class K(Y):
    def __repr__(self):
      return f'k({self.s.upper()})'

k1 = K.fromlist(['za','bu'])
k1