import sys
import os

import nxt_main.nxt_brick as nxt_brick
from rolocode.rolo import Rolo

if os.environ.get('MOCK_NXT') is None:
    import nxt.bluesock as bluesock
else:
    import nxt_mock.bluesock as bluesock


address = '00:16:53:08:09:1F'


def rolo():
    try:
        brick = bluesock.BlueSock(address).connect()
        return Rolo(nxt_brick.NXTBrickController(brick))
    except IOError:
        print("Error while running test:")
        print(str(sys.exc_info()[1]))
        raise
