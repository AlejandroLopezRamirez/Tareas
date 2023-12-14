concatenar = lambda t1, t2 : t2 if t1 == () else \
                             t1 + t2 if len(t1) == 1 else \
                             t1[0] + concatenar(t1[1:], t2)
