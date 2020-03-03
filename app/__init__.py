# Hack to make absolute imports work.
import os
import sys

sys.path.append(os.path.dirname(os.path.realpath(__file__)))
