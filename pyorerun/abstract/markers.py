from abc import abstractmethod

import numpy as np

from .abstract_class import Component
from ..utils.color_utils import get_colors


class Markers(Component):
    @abstractmethod
    def nb_markers(self):
        pass


class MarkerProperties:
    """
    A class used to represent the properties of a marker.


    Attributes
    ----------
    marker_names : list[str]
        a list of names for the markers
    radius : float
        the radius of the markers
    color : np.ndarray
        the color of the markers, in RGB format from 0 to 255, e.g. [0, 0, 255] for blue

    Methods
    -------
    nb_markers():
        Returns the number of markers.
    radius_to_rerun():
        Returns a numpy array with the radius of each marker.
    color_to_rerun():
        Returns a numpy array with the color of each marker.
    """

    def __init__(
        self,
        marker_names: list[str] | tuple[str, ...],
        radius: float | tuple[float, ...],
        color: np.ndarray,
        show_labels: bool | list[bool] = True,
    ):
        """
        Constructs all the necessary attributes for the MarkerProperties object.

        Parameters
        ----------
            marker_names : list[str, ...] | tuple[str, ...]
                a list of names for the markers
            radius : float | tuple[float, ...]
                the radius of the markers
            color : np.ndarray
                the color of the markers
            show_labels : bool
                whether to show the labels of the markers (this can be changed by checking the appropriate box in the GUI)
        """
        self.marker_names = marker_names
        self.radius = radius
        self.color = color
        self.show_labels = show_labels

    @property
    def nb_markers(self):
        """
        Returns the number of markers.

        Returns
        -------
        int
            The number of markers.
        """
        return len(self.marker_names)

    def radius_to_rerun(self) -> None:
        """
        Returns a numpy array with the radius of each marker.

        Returns
        -------
        np.ndarray
            A numpy array with the radius of each marker.
        """
        if isinstance(self.radius, float):
            return np.ones(self.nb_markers) * self.radius
        return np.array(self.radius)

    def color_to_rerun(self, nb_frames: int) -> list[np.ndarray]:
        """
        Returns a numpy array with the color of each marker.

        Returns
        -------
        np.ndarray
            A numpy array with the color of each marker.
        """
        nb_markers = len(self.marker_names)
        colors = get_colors(color=self.color, nb_elements=nb_markers, nb_frames=nb_frames)
        return colors

    def show_labels_to_rerun(self) -> list[bool]:
        """
        Returns a list of booleans indicating if the label of each marker should be displayed.
        """
        if isinstance(self.show_labels, bool):
            return [self.show_labels] * self.nb_markers
        elif isinstance(self.show_labels, list):
            return self.show_labels
        else:
            raise ValueError("The show_labels attribute must be a boolean or a list of booleans.")
