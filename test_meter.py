
from __future__ import print_function
import serial
import time
import re


data_pattern = '(?P<id>[0-9]\.[0-9]\.[0-9])\((?P<data>[0-9a-zA-Z\.\*]*)\)'
ACK = '\x06'
STX = '\x02'
ETX = '\x03'
default_tr = 0.3

def query_data(tr = default_tr):
    """
    Get the data output from the meter

    Parameters
    ----------
    tr: [optional] sleep time after the request has been sent

    Returns
    -------
    dict: contains the different output info from the meter


    Example
    -------
    >>> query_data()
    {'0.9.1': '162620',
     '0.9.2': '171028',
     '1.8.0': '14002.574*kWh',
     '2.8.0': '21450.504*kWh'}

    """

    # Open port
    IskraMT171=serial.Serial(port='/dev/ttyUSB0', baudrate=300, bytesize=7, parity='E', stopbits=1, timeout=1.5); # open port at specified speed

    # Initiate request
    Request_message='/?!\r\n' + ACK + '000\r\n' # IEC 62056-21:2002(E) 6.3.1
    IskraMT171.write(Request_message.encode())
    time.sleep(tr)
    # print('ID:', IskraMT171.readline())

    # Read data
    Acknowledgement_message= ACK + '000\r\n' # IEC 62056-21:2002(E) 6.3.3
    IskraMT171.write(Acknowledgement_message.encode())
    time.sleep(tr)
    data = b''.join([IskraMT171.readline() for i in range(5)])
    # print(data.decode())

    # Close port
    IskraMT171.close()

    # Extract data using REgEx pattern
    processed = dict(re.findall(data_pattern, data.decode()))
    return processed
