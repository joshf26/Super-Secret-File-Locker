from argparse import ArgumentParser


def parse_input():
    argument_parser = ArgumentParser()

    argument_parser.add_argument(
        'filename',
        type=str,
        help='the name of the file to lock',
    )  # TODO: This can easily support directories as long as the slash is stripped.
    argument_parser.add_argument(
        'pin',
        type=int,  # TODO: This actually needs to be a string so that it can be zero padded.
        help='the pin number to lock the file with',
    )
    argument_parser.add_argument(
        '-l',
        '--long',
        action='store_true',
        help='explicitly state that the pin is long. Without this flag, a pin greater than 4 digits will throw a '
             'warning since it will take up a lot of memory to create the directory structure.',
    )

    args = argument_parser.parse_args()

    return (
        args.filename,
        args.pin,
        args.long,
    )
