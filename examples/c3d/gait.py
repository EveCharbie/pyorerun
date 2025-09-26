from pathlib import Path
import pyorerun as prr

def main():
    current_path = Path(__file__).parent.as_posix()
    prr.c3d(
        current_path + "/gait.c3d",
        show_floor=True,
        show_force_plates=True,
        show_forces=True,
        down_sampled_forces=True,
        show_events=False,
    )

if __name__ == "__main__":
    main()
