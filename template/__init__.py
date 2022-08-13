from template.messagelistener import *
from template.ominous863023145463578644 import *
from template.prism863023145463578644 import *


def initApp():
  messagelistener_instance.add_observer("ominous863023145463578644", Ominous863023145463578644())
  messagelistener_instance.add_observer("prism863023145463578644", Prism863023145463578644())
