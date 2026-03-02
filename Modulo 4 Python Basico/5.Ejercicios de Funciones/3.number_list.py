# def main():
#     number_list = [1,9,23,38,54,76,102,135,180,200]
#     total_sum = 0
#     for number in number_list:
#         total_sum = addition(total_sum, number)
#     print(f'El resulatado de la suma total es: {total_sum}')


def getList_total(total):
    number_list = [1,9,23,38,54,76,102,135,180,200]
    total = sum(number_list)

    return total 


def main():
    total_list = []
    total = getList_total(total_list)
    print(f'El resulatado de la suma total es: {total}')


if __name__ == "__main__":
    main()