def getList_total(numlst):
    if not isinstance(numlst, list):
        raise TypeError("El argumento debe ser una lista.")
    total = sum(numlst)
    return total


def main():
    numlst = [1,9,23,38,54,76,102,135,180,200]
    total_list = getList_total(numlst)

    print(f'El resulatado de la suma total es: {total_list}')
    


if __name__ == "__main__":
    main()