tomar_mientras = lambda f, t: () if t == () else \
                              (t[0],) + tomar_mientras(f, t[1:]) if f(t[0]) else \
                              ()
