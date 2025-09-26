from pathlib import Path
import opensim

from pyorerun import OsimModel, PhaseRerun, OsimTimeSeries, DisplayModelOptions


def main():
    current_path = Path(__file__).parent.as_posix()
    osim_model = opensim.Model(current_path + "/Rajagopal2015.osim")
    display_options = DisplayModelOptions()
    display_options.mesh_path = current_path + "/Geometry_cleaned"
    prr_model = OsimModel.from_osim_object(osim_model, options=display_options)

    mot_file = current_path + "/ik.mot"
    mot_time_series = OsimTimeSeries(mot_file, osim_model)

    viz = PhaseRerun(mot_time_series.times)
    viz.add_animated_model(prr_model, mot_time_series.q_in_radian)
    viz.rerun("msk_model")


if __name__ == "__main__":
    main()
