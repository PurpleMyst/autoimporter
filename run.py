#!/usr/bin/env python3
import os
import sys
import runpy

import autoimporter


def main():
    if len(sys.argv) < 2:
        print("USAGE: python3 run.py FILENAME")
        sys.exit(1)
    else:
        filename = sys.argv[1]
        sys.path.insert(0, os.path.dirname(filename))
        module_name = os.path.splitext(os.path.basename(filename))[0]
        runpy._run_module_as_main(module_name)


if __name__ == "__main__":
    main()
