import numpy as np

def equalize_compote(glasses):
    total_volume = sum(glasses)
    num_glasses = len(glasses)
    
    # Проверка, можно ли равномерно распределить компот
    if total_volume % num_glasses != 0:
        print("Невозможно равномерно распределить компот.")
        return None
    
    target_volume = total_volume // num_glasses
    moves = []
    
    while True:
        # Находим стаканы, которые нужно поднять
        overfilled = [i for i in range(num_glasses) if glasses[i] > target_volume]
        underfilled = [i for i in range(num_glasses) if glasses[i] < target_volume]
        
        if not overfilled and not underfilled:
            break  # Все стаканы равны
        
        # Переливаем компот
        for i in overfilled:
            for j in underfilled:
                if glasses[i] > target_volume and glasses[j] < target_volume:
                    transfer_amount = min(glasses[i] - target_volume, target_volume - glasses[j])
                    glasses[i] -= transfer_amount
                    glasses[j] += transfer_amount
                    moves.append((i, j, transfer_amount))
    
    return moves, glasses

# Пример использования
glasses = [100, 200, 300, 400, 500]  # Начальные объемы в мл
moves, final_state = equalize_compote(glasses)

if moves:
    print("Переливания компота:")
    for move in moves:
        print(f"Перелить {move[2]} мл из стакана {move[0] + 1} в стакан {move[1] + 1}")
    print("Конечное состояние стаканов:", final_state)
