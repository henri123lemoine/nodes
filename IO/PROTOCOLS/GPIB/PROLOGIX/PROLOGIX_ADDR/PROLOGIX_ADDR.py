import serial
import traceback
from flojoy import flojoy, SerialConnection, DataContainer, TextBlob
from typing import cast, Optional


@flojoy(deps={"pyserial": "3.5"}, inject_connection=True)
def SET_ADDR(
    connection: SerialConnection, default: Optional[DataContainer] = None,
    addr: int = 22
) -> TextBlob:
    """The PROLOGIX_ADDR node sets the GPIB address of an instrument using the Prologix USB-to-GPIB or USB-to-Ethernet adapter.

    Inputs
    ------
    default: DataContainer
        Any DataContainer - likely connected to the output of the OPEN_SERIAL node.

    Parameters
    ----------
    connection: Serial
        The open serial connection with the instrument.

    Returns
    -------
    TextBlob
        Response from the Prologix USB-to-GPIB controller.
    """

    # Start serial communication with the instrument
    ser = cast(serial.Serial, connection.get_handle())

    if ser is None:
        raise ValueError("Serial communication is not open")

    ser.write(b'++addr ' + str(addr) + '\r\n')

    s = ''
    s = ser.read(256);

    return TextBlob(s)