from typing import *

class North: pass
class East: pass
class South: pass
class West: pass

type Direction = Union[North, East, South, West]