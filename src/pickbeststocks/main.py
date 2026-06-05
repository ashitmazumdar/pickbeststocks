#!/usr/bin/env python
import sys
import warnings
import os
from datetime import datetime

from pickbeststocks.crew import PickbestStocks

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


def run():
    """
    Run the research crew.
    """
    print("Loading crew (first run can take a few minutes)...", flush=True)
    inputs = {
        'sector': 'EV spare parts'
    }

    # Create and run the crew
    result = PickbestStocks().crew().kickoff(inputs=inputs)

    # Print the result
    print("\n\n=== FINAL DECISION ===\n\n")
    print(result.raw)


if __name__ == "__main__":
    run()
