#!/usr/bin/env python3
"""
Minipar Compiler - Command Line Interface
Compile Minipar source files to three-address code
"""

import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from src.compiler import main

if __name__ == '__main__':
    main()
