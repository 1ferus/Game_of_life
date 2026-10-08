"""Тесты для игры «Жизнь»."""

import numpy as np

from game_of_life import count_neighbors, update, create_grid


def test_empty_field_stays_empty():
    """Пустое поле остаётся пустым."""
    grid = np.zeros((5, 5), dtype=int)
    new_grid = update(grid)
    assert np.array_equal(new_grid, grid)


def test_block_is_stable():
    """Блок 2×2 не меняется со временем."""
    block = np.array([
        [1, 1, 0],
        [1, 1, 0],
        [0, 0, 0],
    ], dtype=int)
    new_block = update(block)
    assert np.array_equal(new_block, block)


def test_count_neighbors_center():
    """В квадрате 3×3 у центра 3 живых соседа."""
    grid = np.array([
        [1, 1, 0],
        [1, 1, 0],
        [0, 0, 0],
    ], dtype=int)
    assert count_neighbors(grid, 1, 1) == 3


def test_glider_moves_by_one_cell_after_4_steps():
    """Глайдер за 4 шага смещается на (1, 1)."""
    glider = np.zeros((10, 10), dtype=int)
    glider[1, 2] = 1
    glider[2, 3] = 1
    glider[3, 1] = 1
    glider[3, 2] = 1
    glider[3, 3] = 1

    result = glider.copy()
    for _ in range(4):
        result = update(result)

    assert result.sum() == 5
    assert result[2, 3] == 1
    assert result[3, 4] == 1
    assert result[4, 2] == 1
    assert result[4, 3] == 1
    assert result[4, 4] == 1


def test_create_grid_shape_and_values():
    """create_grid возвращает матрицу нужного размера с 0/1."""
    grid = create_grid(10, 0.5)
    assert grid.shape == (10, 10)
    assert set(np.unique(grid)).issubset({0, 1})