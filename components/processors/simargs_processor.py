"""
This is a simargs library for configuring a Processor,
allowing command-line customization of Processor params,
e.g., the number of cores
"""
from typing import Dict, Any
import util.simarglib as simarglib

###
# PARSER CONFIGURATION
parser = simarglib.add_parser("Processor")
parser.add_argument("--cores", type=int, default=1, help="Processor core count")
###

def get_processor_params() -> Dict[str, Any]:
    params = {}

    if simarglib.get("cores"):
        params["cores"] = simarglib.get("cores")

    return params
