from enum import Enum

from studies import StudyConfiguration, PlotOptions, StudySetup, get_nmpc, Program


class Conditions(Enum):
    DEBUG_FAST = StudyConfiguration(
        studies=(
            get_nmpc(Program.TORQUE_DRIVEN_XIA,
                     StudySetup(
                         n_round_trips_to_advance=1,
                         n_round_trips=3,
                         n_total_round_trips=8,
                         split_controls=True,
                     )),
        ),
        rmse_index=None,
        plot_options=PlotOptions(
            title="%s pour les conditions $C/\\tau\\varnothing$  et $C/\\alpha\\varnothing$",
            legend_indices=None,
            options=({"linestyle": "-"}, {"linestyle": "--"}),
            to_degrees=True,
        ),
    )

    DEBUG_ALL_CONDITIONS = StudyConfiguration(
        studies=(
            # get_nmpc(Program.TORQUE_DRIVEN_NO_FATIGUE, StudySetup(n_total_round_trips=5)),
            # get_nmpc(Program.MUSCLE_DRIVEN_NO_FATIGUE, StudySetup(n_total_round_trips=5)),
            get_nmpc(Program.TORQUE_DRIVEN_XIA, StudySetup(n_total_round_trips=20, split_controls=True)),
            # get_nmpc(Program.TORQUE_DRIVEN_XIA, StudySetup(n_total_round_trips=5, split_controls=False)),
            # get_nmpc(Program.MUSCLE_DRIVEN_XIA, StudySetup(n_total_round_trips=5)),
        ),
        rmse_index=None,
        plot_options=PlotOptions(
            title="Fast debugger",
            legend_indices=None,
            options=(
                {"linestyle": "-"},
                {"linestyle": "--"},
                {"linestyle": "-"},
                {"linestyle": "--"},
                {"linestyle": "-"},
            ),
            to_degrees=True,
        ),
    )

    CONDITIONS = StudyConfiguration(
        studies=(
            get_nmpc(Program.TORQUE_DRIVEN_XIA,
                     StudySetup(
                         round_trip_time=1,
                         n_shoot_per_round_trip=50,
                         n_round_trips_to_advance=1,
                         n_round_trips=3,
                         n_total_round_trips=60,
                         # split_controls=True,
                         split_controls=True,
                     ),),
        ),
        rmse_index=None,
        plot_options=PlotOptions(
            title="Fast debugger",
            legend_indices=None,
            options=(
                {"linestyle": "-"},
                {"linestyle": "--"},
                {"linestyle": "-"},
                {"linestyle": "--"},
                {"linestyle": "-"},
            ),
            to_degrees=True,
        ),
    )
    CONDITIONS_ONLY_FATIGUE = StudyConfiguration(
        studies=(
            get_nmpc(Program.TORQUE_DRIVEN_XIA_FATIGUE_ONLY,
                     StudySetup(
                         round_trip_time=1,
                         n_shoot_per_round_trip=50,
                         n_round_trips_to_advance=1,
                         n_round_trips=3,
                         n_total_round_trips=60,
                         split_controls=True,
                     ), ),
        ),
            rmse_index=None,
        plot_options=PlotOptions(
            title="Fast debugger",
            legend_indices=None,
            options=(
                {"linestyle": "-"},
                {"linestyle": "--"},
                {"linestyle": "-"},
                {"linestyle": "--"},
                {"linestyle": "-"},
            ),
            to_degrees=True,
        ),
    )
    CONDITIONS_ONLY_TORQUE = StudyConfiguration(
        studies=(
            get_nmpc(Program.TORQUE_DRIVEN_XIA_TORQUE_ONLY,
                     StudySetup(
                         round_trip_time=1,
                         n_shoot_per_round_trip=50,
                         n_round_trips_to_advance=1,
                         n_round_trips=3,
                         n_total_round_trips=60,
                         split_controls=True,
                     ), ),
        ),
        rmse_index=None,
        plot_options=PlotOptions(
            title="Fast debugger",
            legend_indices=None,
            options=(
                {"linestyle": "-"},
                {"linestyle": "--"},
                {"linestyle": "-"},
                {"linestyle": "--"},
                {"linestyle": "-"},
            ),
            to_degrees=True,
        ),
    )

    CONDITIONS_2 = StudyConfiguration(
        studies=(
            get_nmpc(Program.TORQUE_DRIVEN_XIA,
                     StudySetup(
                         round_trip_time=2,
                         n_shoot_per_round_trip=100,
                         n_round_trips_to_advance=1,
                         n_round_trips=3,
                         n_total_round_trips=60,
                         split_controls=True,
                     ), ),
        ),
        rmse_index=None,
        plot_options=PlotOptions(
            title="Fast debugger",
            legend_indices=None,
            options=(
                {"linestyle": "-"},
                {"linestyle": "--"},
                {"linestyle": "-"},
                {"linestyle": "--"},
                {"linestyle": "-"},
            ),
            to_degrees=True,
        ),
    )

    CONDITIONS_3 = StudyConfiguration(
        studies=(
            get_nmpc(Program.TORQUE_DRIVEN_XIA,
                     StudySetup(
                         round_trip_time=4,
                         n_shoot_per_round_trip=150,
                         n_round_trips_to_advance=1,
                         n_round_trips=3,
                         n_total_round_trips=60,
                         split_controls=True,
                     ), ),
        ),
        rmse_index=None,
        plot_options=PlotOptions(
            title="Fast debugger",
            legend_indices=None,
            options=(
                {"linestyle": "-"},
                {"linestyle": "--"},
                {"linestyle": "-"},
                {"linestyle": "--"},
                {"linestyle": "-"},
            ),
            to_degrees=True,
        ),
    )


