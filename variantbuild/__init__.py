import importlib.metadata
import logging
import sys

__version__ = importlib.metadata.version("variantbuild")


logger = logging.getLogger("variantbuild")
logger.addHandler(logging.StreamHandler(sys.stdout))
logger.setLevel(logging.INFO)
