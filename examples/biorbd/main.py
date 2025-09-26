from pathlib import Path
import numpy as np

import pyorerun as prr


def main():
    # building some time components
    nb_frames = 200
    nb_seconds = 1
    t_span = np.linspace(0, nb_seconds, nb_frames)

    # building some generalized coordinates
    q = np.zeros((2, nb_frames))
    q[0, :] = np.linspace(0, 0.1, nb_frames)
    q[1, :] = np.linspace(0, 0.3, nb_frames)

    # running the animation
    current_path = Path(__file__).parent.as_posix()
    prr.animate(current_path + "/models/double_pendulum.bioMod", q, tspan=t_span)


if __name__ == "__main__":
    main()
