from os import path
from ntpath import basename
from pathlib import Path
from shutil import move

MAX_PIN_LEN_BEFORE_WARNING = 4


def lock_file(file_path, pin, long_pin=False):
    str_pin = str(pin)
    pin_len = len(str_pin)

    # Check if the pin is long, and make sure the user knows what they are doing.
    if pin_len > MAX_PIN_LEN_BEFORE_WARNING and not long_pin:
        raise Warning('Pin is very long. Creating this directory structure will use a lot of memory. If you still wish '
                      'to proceed, specify the -l or --long flag.')

    # Make sure the file or directory exists.
    if not path.exists(file_path):
        raise FileNotFoundError("No such file or directory: '{}'".format(file_path))

    for number in range(10**pin_len):
        # Zero pad the number and split it into its digits.
        # For example, in a 4-digit pin, "15" would be turned into "['0', '0', '1', '5']".
        number_list = list(str(number).zfill(pin_len))

        # Create the folder that corresponds to the number.
        # For example, in a 4-digit pin, "15" would create the directory ".../0/0/1/5/".
        Path('{}.locked/{}'.format(
            file_path,
            '/'.join(number_list)
        )).mkdir(parents=True, exist_ok=True)

    # Move the file or directory into the appropriate folder.
    move(file_path, '{}.locked/{}/{}'.format(
        file_path,
        '/'.join(list(str_pin)),
        basename(file_path),
    ))
