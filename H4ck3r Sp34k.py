def hacker_speak(s):
    '''
    Que lo traduzca a hacker
    '''
    mapal = s.maketrans('aeios', '43105')
    shacker = s.translate(mapal)
    return shacker
