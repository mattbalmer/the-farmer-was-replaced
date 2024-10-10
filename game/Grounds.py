from typing import *

class Soil: pass
class Turf: pass

type Ground = Union[Soil, Turf]