def script():
  paises = input('Escriba una lista de paises separados por comas: '
                 '\n')

  listaPaises = [pais for pais in paises.replace(" ", "").split(",")]

  print(", ".join(sorted(list(set(listaPaises)))))


if __name__ == '__main__':
  script()
