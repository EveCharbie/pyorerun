from pathlib import Path
import numpy as np

from pyorerun import PhaseRerun, BiorbdModel


def main():
    current_path = Path(__file__).parent.as_posix()
    biorbd_model_path = current_path + "/models/2d_wheelchair.bioMod"

    # building some time components
    nb_frames = 200
    nb_seconds = 1
    t_span = np.linspace(0, nb_seconds, nb_frames)

    # loading biorbd model
    biorbd_model = BiorbdModel(biorbd_model_path)
    nq = biorbd_model.model.nbQ()

    # running the animation
    rerun_biorbd = PhaseRerun(t_span)
    np.random.seed(42)
    q = np.linspace(np.array([0, 0, 0, -1]), np.array([0.35 * 2, -2, 1, 1.5]), nb_frames).T
    rerun_biorbd.add_animated_model(biorbd_model, q)
    rerun_biorbd.rerun("animation")


if __name__ == "__main__":
    main()
