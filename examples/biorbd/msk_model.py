import numpy as np

from pyorerun import BiorbdModel, PhaseRerun, PersistentMarkerOptions


def main():
    # building some time components
    nb_frames = 50
    nb_seconds = 1
    t_span = np.linspace(0, nb_seconds, nb_frames)

    model = BiorbdModel("models/Wu_Shoulder_Model_kinova_scaled_adjusted_2.bioMod")
    model.options.transparent_mesh = False

    # building some generalized coordinates
    q = np.zeros((model.model.nbQ(), nb_frames))
    q[10, :] = np.linspace(0, np.pi / 8, nb_frames)
    q[12, :] = np.linspace(0, np.pi / 3, nb_frames)
    q[11, :] = np.linspace(0, np.pi / 4, nb_frames)
    q[13, :] = np.linspace(0, np.pi / 8, nb_frames)
    q[14, :] = np.linspace(0, np.pi / 8, nb_frames)
    q[15, :] = np.linspace(0, np.pi / 8, nb_frames)

    import time

    # Initialize the animation with a time vector
    viz = PhaseRerun(t_span)

    # Example of how to add persistent markers with changing color over time
    # NOTE: It is important (I don't know if it is a bug in rerun) to have the colors between 0 and 1, not between 0 and 255
    # It only works for one marker for now and with rerun (not rerun_by_frame), because again we don't know at which idx we aree
    color_timeseries = np.zeros((1, nb_frames, 3))
    color_timeseries[0, 10:20, :] = np.array([0.58039216, 0.40392157, 0.74117647])
    color_timeseries[0, 30:40, :] = np.array([1, 0.40392157, 0.14])
    model.options.persistent_markers = PersistentMarkerOptions(
        marker_names=["ULNA"],
        radius=0.005,
        color=color_timeseries,
        show_labels=False,
        nb_frames=20,
    )

    # Example of how to add persistent marker
    model.options.persistent_markers = PersistentMarkerOptions(
        marker_names=["ULNA", "RADIUS"],
        radius=0.005,
        color=color_timeseries,
        show_labels=False,
        nb_frames=20,
    )

    # viz.add_animated_model(model, q, display_q=True)
    viz.add_animated_model(model, q, display_q=False)

    tic = time.time()
    viz.rerun("msk_model with chunks")
    toc = time.time()
    print(f"Time to run: {toc - tic}")

    tic = time.time()
    viz.rerun_by_frame("msk_model frame by frame")
    toc = time.time()
    print(f"Time to run with chunks: {toc - tic}")


if __name__ == "__main__":
    main()
