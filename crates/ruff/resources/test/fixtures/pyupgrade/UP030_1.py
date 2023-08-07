# Valid calls; no errors expected.

'{}'.format(1)

x = ('{0} {1}',)

'{0} {0}'.format(1)

'{0:<{1}}'.format(1, 4)

f"{0}".format(a)

f"{0}".format(1)

print(f"{0}".format(1))

''.format(1)

'{1} {0}'.format(*args)

"{1}_{0}".format(*args, 1)

"{1}_{0}".format(*args, 1, 2)

"{1}_{0}".format(1, **kwargs)

"{1}_{0}".format(1, foo=2)

"{1}_{0}".format(1, 2, **kwargs)

"{1}_{0}".format(1, 2, foo=3, bar=4)
