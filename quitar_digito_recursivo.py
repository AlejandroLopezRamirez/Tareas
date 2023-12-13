quitar_digitos = lambda s: s if s == '' else str(s[0]) + quitar_digitos(s[1:]) \
                    if not s[0].isdigit() else quitar_digitos(s[1:])
