#!/usr/bin/env python3

import time


class ThingieThatDoesThing:
    def __init__(self) -> None:
        pass

    def do_the_thing(self):
        result = self._time_consuming_subthing()
        if result:
            print("Did the thing!")

    def _time_consuming_subthing(self):
        time.sleep(secs=10)
        return True


def test_do_the_thing():
    ...
