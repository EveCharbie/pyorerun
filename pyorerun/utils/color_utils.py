import numpy as np


def get_colors(color: np.ndarray, nb_elements: int, nb_frames: int) -> list[int]:
    """
    Returns a list of colors for each marker at each frame.

    Parameters
    ----------
    color: np.ndarray
        The color of the elements. It can be:
        - a single color (shape (3,)): all elements will have the same color at all frames
        - a color per element (shape (nb_elements, 3)): each element will have its own color at all frames
        - a color per element and per frame (shape (nb_elements, nb_frames, 3)): each element will have its own color at each frame
    nb_elements: int
        The number of elements (markers, line strips, ...).
    nb_frames : int
        The number of frames in the simulation.

    Returns
    -------
    list[np.ndarray]
        A list of colors for each marker at each frame.
    """
    if len(color.shape) == 3:
        colors = [rgb255_to_hex_rgba(color[s, f, :]) for f in range(nb_frames) for s in range(nb_elements)]
    elif len(color.shape) == 2:
        colors = [rgb255_to_hex_rgba(color[s, :]) for _ in range(nb_frames) for s in range(nb_elements)]
    else:
        colors = [rgb255_to_hex_rgba(color) for _ in range(nb_frames * nb_elements)]
    return colors


def rgb255_to_hex_rgba(color_rgb, alpha=255) -> int:
    # color_rgb: np.ndarray ou list \[R, G, B] en 0–255
    r, g, b = [int(np.clip(c, 0, 255)) for c in color_rgb[:3]]
    a = int(np.clip(alpha, 0, 255))
    return (r << 24) | (g << 16) | (b << 8) | a