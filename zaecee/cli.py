#!/usr/bin/env python3
import logging
import argparse
import sys
import zaecee

def main():
    logging.basicConfig(level=logging.INFO, datefmt='%Y-%m-%dT%H:%M:%S', stream=sys.stderr, format="%(asctime)s %(process)d %(thread)d %(levelno)03d:%(levelname)-8s %(name)-12s %(module)s:%(lineno)s:%(funcName)s %(message)s")
    argument_parser = argparse.ArgumentParser(add_help = False)
    argument_parser.add_argument("-v", "--verbose", action="count", dest="verbosity", help="increase verbosity level")
    argument_parser.add_argument("-h", "--help", action="help", help="shows this help message and exit")

    arguments = argument_parser.parse_args( args = sys.argv[1:] )

    if arguments.verbosity is not None:
        root_logger = logging.getLogger("")
        root_logger.setLevel( root_logger.getEffectiveLevel() - (min(1,arguments.verbosity))*10 - min(max(0,arguments.verbosity - 1),9)*1 )

    logging.info("arguments = %s", arguments)
    logging.debug("sys.argv = %s", sys.argv)
    logging.debug("logging.level = %s", logging.getLogger("").getEffectiveLevel())

    logging.log(1, "hello %s", __name__)
    logging.debug("hello %s", __name__)
    logging.info("hello %s %s", __name__, __file__)

    logging.info("zaecee.zaecee_function(...) = %s", zaecee.zaecee_function("this is my {}".format(__name__)))

    logging.info("this is now ... 01")

if __name__ == "__main__":
    main()
