import random


def distribute_compote(glasses):
    total_compote = sum(glasses)
    num_glasses = len(glasses)

    # Проверяем, можно ли равномерно распределить компот
    if total_compote % num_glasses != 0:
        print("Невозможно равномерно распределить компот.")
        return None

    target_amount = total_compote // num_glasses
    operations = 0

    # Создаем список стаканов с их индексами
    glasses_with_index = list(enumerate(glasses))

    while True:
        # Находим стаканы, которые нужно опустошить и наполнить
        to_empty = [i for i, amount in glasses_with_index if amount > target_amount]
        to_fill = [i for i, amount in glasses_with_index if amount < target_amount]

        # Если все стаканы равны, выходим из цикла
        if not to_empty and not to_fill:
            break

        # Переливаем компот
        for i in to_empty:
            for j in to_fill:
                if glasses_with_index[i][1] > target_amount and glasses_with_index[j][1] < target_amount:
                    transfer_amount = min(glasses_with_index[i][1] - target_amount,
                                          target_amount - glasses_with_index[j][1])
                    glasses_with_index[i] = (glasses_with_index[i][0], glasses_with_index[i][1] - transfer_amount)
                    glasses_with_index[j] = (glasses_with_index[j][0], glasses_with_index[j][1] + transfer_amount)
                    operations += 1  # Увеличиваем количество операций
                    print(
                        f"Переливаем {transfer_amount} мл из стакана {glasses_with_index[i][0]} в стакан {glasses_with_index[j][0]}")

    print(f"Все стаканы теперь содержат {target_amount} мл компота.")
    print(f"Общее количество операций: {operations}")


# Генерируем случайные объемы компота в стаканах
random_glasses = [random.randint(50, 150) for _ in range(5)]
print(f"Начальные объемы компота в стаканах: {random_glasses}")
distribute_compote(random_glasses)
