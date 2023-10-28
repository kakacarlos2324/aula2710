class Curso:
    def __init__(self, nome):
        self.nome = nome
        self.professor = None

    def atribuir_professor(self, professor):
        self.professor = professor

class Professor:
    def __init__(self, nome):
        self.nome = nome

universidade = []

# Criando cursos e professores
curso1 = Curso("Matemática")
curso2 = Curso("Física")
professor1 = Professor("Prof. A")
professor2 = Professor("Prof. B")

# Atribuindo professores aos cursos
curso1.atribuir_professor(professor1)
curso2.atribuir_professor(professor2)

# Adicionando cursos e professores à universidade
universidade.append(curso1)
universidade.append(curso2)
universidade.append(professor1)
universidade.append(professor2)

# Listando os cursos lecionados por um professor
def listar_cursos_lecionados_por_professor(professor):
    cursos_lecionados = []
    for item in universidade:
        if isinstance(item, Curso) and item.professor == professor:
            cursos_lecionados.append(item.nome)
    return cursos_lecionados

cursos_prof_A = listar_cursos_lecionados_por_professor(professor1)
print("Cursos lecionados pelo Prof. A:", cursos_prof_A)

cursos_prof_B = listar_cursos_lecionados_por_professor(professor2)
print("Cursos lecionados pelo Prof. B:", cursos_prof_B)