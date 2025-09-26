import numpy as np
from ..abstract.markers import MarkerProperties


class PersistentMarkerOptions(MarkerProperties):
    def __init__(
        self,
        marker_names: list[str] | tuple[str, ...],
        radius: float | tuple[float, ...],
        color: np.ndarray,
        nb_frames: int,
        show_labels: bool | list[bool] = True,
    ) -> None:
        """
        Initialization of a marker trajectory

        Parameters
        ----------
        marker_names: list[str, ...] | tuple[str, ...]
            The name of the markers to display a trajectory for.
        radius : float | tuple[float, ...]
                the radius of the markers to display a trajectory for.
        color : np.ndarray
            the color of the markers to display a trajectory for
        show_labels : bool
            whether to show the labels of the markers to display a trajectory for.
        nb_frames: int
            The number of frames to display the trajectory for.
            Example: nb_frames=20 means that the position of the marker for the last 20 frames will be displayed at each current frame.
        """
        super().__init__(marker_names, radius, color, show_labels)
        self.nb_frames = nb_frames

    def frames_to_keep(self, frame_idx: int) -> list[int]:
        """
        Give the list of frames to keep for a given current frame index.

        Examples
        --------
        - If nb_frames=5 and frame_idx=10, it will return [6, 7, 8, 9, 10]
        - If nb_frames=5 and frame_idx=3, it will return [0, 1, 2, 3]

        Parameters
        ----------
        frame_idx : int
            The current frame index.
        """
        n = self.nb_frames
        start = max(0, frame_idx - n + 1)
        return list(range(start, frame_idx + 1))

    def all_frames_to_keep(self, total_frames: int) -> list[list[int]]:
        """
        Give the list of frames to keep for all frames from 0 to total_frames-1.

        Parameters
        ----------
        total_frames : int
            The total number of frames in the simulation.
        """
        return [self.frames_to_keep(frame_idx) for frame_idx in range(total_frames)]
