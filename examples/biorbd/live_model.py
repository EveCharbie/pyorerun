"""
This example is a simple example of how to use the LiveModelAnimation class to animate a model in real-time.
The user can interact with the model by changing the joint angles using sliders.
"""

from pathlib import Path
from pyorerun import LiveModelAnimation


def main(with_q_charts: bool = False):
    current_path = Path(__file__).parent.as_posix()
    model_path = current_path + "/models/Wu_Shoulder_Model_kinova_scaled_adjusted_2.bioMod"
    animation = LiveModelAnimation(model_path, with_q_charts=with_q_charts)
    animation.rerun()


if __name__ == "__main__":
    main(with_q_charts=True)
