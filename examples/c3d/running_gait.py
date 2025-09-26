from pathlib import Path
import pyorerun as prr


def main():
    current_path = Path(__file__).parent.as_posix()
    prr.c3d(
        current_path + "/Running_0002.c3d",
        show_floor=True,
        show_force_plates=True,
        show_forces=True,
        down_sampled_forces=True,
        show_events=False,
        video=(current_path + "/Running_0002_Oqus_6_15004.avi", current_path + "/Running_0002_Oqus_9_15003.avi"),
    )


if __name__ == "__main__":
    main()
