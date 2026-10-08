"""Игра «Жизнь» — клеточный автомат Джона Конвея.

Модуль содержит функции для создания и эволюции поля игры.

Правила:
- Живая клетка выживает при 2 или 3 живых соседях.
- Мёртвая клетка рождается ровно при 3 живых соседях.
- Иначе клетка умирает или остаётся мёртвой.

Окрестность: Мура (8 соседей).
Границы: периодические (тор).
"""

import numpy as np


def create_grid(size: int, density: float = 0.3) -> np.ndarray:
    """Создаёт квадратное поле size × size со случайным заполнением.

    Параметры
    ---------
    size : int
        Сторона поля.
    density : float
        Вероятность того, что клетка жива (от 0 до 1).

    Возвращает
    ----------
    np.ndarray
        Матрица size × size из 0 и 1.
    """
    random_matrix = np.random.random((size, size))
    return (random_matrix < density).astype(int)


def count_neighbors(grid: np.ndarray, i: int, j: int) -> int:
    """Считает число живых соседей клетки (i, j) в окрестности Мура.

    Границы периодические (тор): вышедший за край «появляется» с другой стороны.
    """
    rows, cols = grid.shape
    count = 0
    for di in (-1, 0, 1):
        for dj in (-1, 0, 1):
            if di == 0 and dj == 0:
                continue
            ni = (i + di) % rows
            nj = (j + dj) % cols
            count += grid[ni, nj]
    return count


def update(grid: np.ndarray) -> np.ndarray:
    """Один шаг эволюции игры «Жизнь»."""
    rows, cols = grid.shape
    new_grid = np.zeros((rows, cols), dtype=int)
    for i in range(rows):
        for j in range(cols):
            n = count_neighbors(grid, i, j)
            if grid[i, j] == 1:
                if n == 2 or n == 3:
                    new_grid[i, j] = 1
            else:
                if n == 3:
                    new_grid[i, j] = 1
    return new_grid


def run(start_grid: np.ndarray, steps: int) -> np.ndarray:
    """Прогоняет модель на steps шагов и возвращает итоговое поле."""
    grid = start_grid.copy()
    for _ in range(steps):
        grid = update(grid)
    return grid