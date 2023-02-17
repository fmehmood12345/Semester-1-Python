from .panda import WalkingPanda
import argparse


def cli():
    parser = argparse.ArgumentParser(prog="walking_panda")

    # WORKED PRACTICAL: Argument for no rotate
    parser.add_argument("--no-rotate", "-r", help="Suppress Rotation",
                        action="store_true")

    """EXTENDED PRACTICAL Arguments:
                        Part 1:
                            -scale
                            -color
                            -fog
                            -changing color of scenery
                        Part 2:
                            -multi-media
    """

    "I have made scale type float so that if any other type is inputted for example a string then an error can come " \
    "up saying it is an invalid float value. "
    parser.add_argument("--scale", "-s", type=float, help="Make bigger or smaller", const=1, nargs="?", default=1)
    parser.add_argument("--color", "-c", help="changes colour", action="store_true")
    parser.add_argument("--my_sound", "-sd", help="plays sound", action="store_true")
    parser.add_argument("--my_fog", "-f", help="adds fog", action="store_true")
    parser.add_argument("--scenery", "-sc", help="changes colour of scenery", action="store_true")

    args = parser.parse_args()

    walking = WalkingPanda(**vars(args))
    walking.run()
