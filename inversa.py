inversa = lambda t: () if t == () else inversa(t[1:]) + (t[0],)
