if __name__ == '__main__':
    custo = float(input("# horas"))
    num_horas: float = float(input("# horas:"))

    if num_horas >=1: #calcula o preço 1 hora
        custo += 5.0
        num_horas -= 1
        custo += num_horas * 4.5
        