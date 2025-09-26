from pathlib import Path
import pyorerun as prr


def main():
    current_path = Path(__file__).parent.as_posix()
    prr.c3d(
        current_path + "/example.c3d",
        show_forces=False,
        show_events=False,
        marker_trajectories=True,
        show_marker_labels=False,
    )


if __name__ == "__main__":
    main()
