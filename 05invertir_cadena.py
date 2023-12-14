# | Pre:    True
# {         invertir(𝑠: str) -> str
# | Post:   invertir(s) = s[::-1]

#               | "" si s = ""
# invertir (s)  {
#               | invertir(s[1:]) + s[0]

# invertir = lambda s: "" if s == "" else  invertir(s[1:]) + s[0]


invertir_iter = lambda s, acc: acc if s == "" else \
                               invertir_iter(s[1:], s[0] + acc)

invertir = lambda s: invertir_iter(s, "")
