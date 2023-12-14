def rps(p1, p2):
    reglas = {('Rock','Rock') : "It's a draw", ('Paper','Paper') : "It's a draw", \
        ('Scissors','Scissors') : "It'Scissors a draw", ('Rock','Scissors') : 'The winner is p1', \
        ('Scissors','Paper') : 'The winner is p1', ('Paper','Rock') : 'The winner is p1', \
        ('Scissors','Rock') : 'The winner is p2', ('Paper','Scissors') : 'The winner is p2',
        ('Rock','Paper') : 'The winner is p2'}
    return reglas[(p1,p2)]
