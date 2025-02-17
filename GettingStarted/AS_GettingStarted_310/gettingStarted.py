from taipy.gui import Gui
from math import cos, exp

value = 10
page = """
# Welcome to MyTaipyDemo!

<|{value}|text|>
<|{value}|slider|on_change=on_slider|>
<|{data}|chart|>
"""


def on_slider(state):
    state.data = compute_data(state.value)


def compute_data(decay: int) -> list:
    return [cos(i / 6) * exp(-i * decay / 600) for i in range(100)]


data = compute_data(value)

if __name__ == "__main__":
    Gui(page).run(title="MyTaipyDemo")
