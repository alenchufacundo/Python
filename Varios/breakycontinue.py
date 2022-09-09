titulo_curso = 'Curso profesional de Python'

#se saltea todas las 'o' porque dice que cuando encuentre la o, se saltee el print y vaya la siguiente letra.
for caracter in titulo_curso:
    if caracter == 'o':
        continue
    print(caracter)