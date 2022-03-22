def put_in():
    array = []
    print("Вводите числа.")
    while True:
        try:
            x = int(input())
        except ValueError:
            print("Целые числа закончились.")
            break
        array.append(int(x))
    return array


def output():
    returner = put_in()
    print("Введено чисел -", len(returner))
    print("Список чисел -", returner)


def main():
    output()


if __name__ == '__main__':
    main()

