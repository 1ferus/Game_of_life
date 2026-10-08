"""CLI для игры «Жизнь».

Пример запуска:
    python main.py --size 40 --density 0.3 --steps 100
    python main.py --size 60 --density 0.3 --steps 200 --save life.gif
"""

import click
import matplotlib.pyplot as plt
from matplotlib import animation

from game_of_life import create_grid, update


@click.command()
@click.option("--size", default=40, type=int, help="Сторона поля.")
@click.option("--density", default=0.3, type=float, help="Плотность живых клеток (0..1).")
@click.option("--steps", default=100, type=int, help="Число шагов эволюции.")
@click.option("--interval", default=100, type=int, help="Задержка между кадрами, мс.")
@click.option("--save", default=None, type=str, help="Путь для сохранения GIF. Если не задан — открыть окно.")
def main(size, density, steps, interval, save):
    """Запускает игру «Жизнь» с заданными параметрами."""
    grid = create_grid(size, density)

    fig, ax = plt.subplots()
    im = ax.imshow(grid, cmap="binary")
    ax.set_title("Игра «Жизнь»")

    def step_forward(frame):
        nonlocal grid
        grid = update(grid)
        im.set_array(grid)
        ax.set_title(f"Шаг {frame + 1}")
        return (im,)

    anim = animation.FuncAnimation(
        fig, step_forward, frames=steps, interval=interval, blit=True
    )

    if save:
        anim.save(save, writer="pillow")
        click.echo(f"Сохранено в {save}")
    else:
        plt.show()

    plt.close(fig)


if __name__ == "__main__":
    main()