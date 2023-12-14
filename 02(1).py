names = ["Dennis", "Vera", "Mabel", "Annette", "Sussan"]
jobs = ["Butcher", "Programmer", "Doctor", "Teacher", "Lecturer"]

def assign_person_to_job(nombres, profesiones):
    '''
    Tienes dos listas. Una muestra los nombres de las personas (names), mientras que el otro
    muestra sus profesiones (jobs). Tu tarea es crear un diccionario que muestre a cada persona
    con su respectiva profesión.
    '''
    return dict(zip(nombres, profesiones))
