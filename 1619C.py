import sys

input = sys.stdin.readline


def solve():
    # Читаем строку ввода и сразу убираем лишние пробелы/переносы
    parts = input().split()
    if not parts:
        return
    A_str, S_str = parts

    i = len(S_str) - 1
    j = len(A_str) - 1

    res_digits = []

    # Двигаемся справа налево по строке S
    while i >= 0:
        # Если в A цифры закончились, считаем, что там 0 (Танины ведущие нули)
        a = int(A_str[j]) if j >= 0 else 0
        s = int(S_str[i])

        if s >= a:
            # Однозначный случай
            b = s - a
            res_digits.append(str(b))
            i -= 1
            j -= 1
        else:
            # Двузначный случай: нужно взять две последние цифры из S
            if i == 0:
                # Если нам нужно 2 цифры, а осталась всего одна — собрать число нельзя
                print(-1)
                return

            s = int(S_str[i - 1:i + 1])
            b = s - a

            if 0 <= b <= 9:
                res_digits.append(str(b))
                i -= 2
                j -= 1
            else:
                print(-1)
                return

    # Если мы разобрали всю строку S, но в A еще остались ненулевые цифры — ошибка
    while j >= 0:
        if A_str[j] != '0':
            print(-1)
            return
        j -= 1

    # Разворачиваем цифры, так как собирали их с конца
    res_digits.reverse()

    # Объединяем в строку и переводим в int, чтобы автоматически убрать ведущие нули
    ans = int("".join(res_digits))
    print(ans)


def main():
    # Считываем количество тестов
    t_str = input()
    if not t_str:
        return
    t = int(t_str)
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
