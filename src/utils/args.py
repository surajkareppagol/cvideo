from argparse import ArgumentParser

parser = ArgumentParser(
    prog="cvideo",
    description="Config to Video generator",
)

parser.add_argument("filename", help="Config file")
parser.add_argument("-c", "--config", action="store_true", help="Print JSON")


def util_parse_cmd_args():
    return parser.parse_args()


def util_print_help():
    parser.print_help()
