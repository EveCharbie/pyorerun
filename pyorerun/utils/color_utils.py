import numpy as np


def get_colors(color: np.ndarray, nb_elements: int, nb_frames: int) -> list[np.ndarray]:
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
        colors = [color[s, f, :] for f in range(nb_frames) for s in range(nb_elements)]
    elif len(color.shape) == 2:
        colors = [color[s, :] for _ in range(nb_frames) for s in range(nb_elements)]
    else:
        colors = [color for _ in range(nb_frames * nb_elements)]
    return colors
