from argparse import ArgumentParser
import logging

from .parser import LogParser

argument_parser = ArgumentParser(add_help=True)
argument_parser.description = """
Log Parser CLI Tool
Tool that reads raw log files, extract key log metrics, and outputs Markdown report summary.
"""

required_args = argument_parser.add_argument_group("required arguments")
required_args.add_argument(
    "-f", "--file", help="Path to the input log file.", required=True, type=str
)

optional_args = argument_parser.add_argument_group("optional arguments")
optional_args.add_argument(
    "-o",
    "--output",
    help="Path to the output Markdown report file.",
    required=False,
    type=str,
)
optional_args.add_argument(
    "-t",
    "--threshold",
    help="Threshold for log metrics.",
    required=False,
    type=int,
    default=0,
)
optional_args.add_argument(
    "-l",
    "--log-level",
    help="Set the logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL).",
    required=False,
    type=str,
    default="INFO",
)


def main():
    args = argument_parser.parse_args()
    log_file_path = args.file
    output_file_path = args.output
    threshold = args.threshold
    log_level = args.log_level

    logger = logging.getLogger(__name__)

    chosen_level = getattr(logging, log_level.upper(), None)
    if chosen_level is None:
        logger.warning(f"Invalid log level '{log_level}' provided. Defaulting to INFO.")
        chosen_level = logging.INFO

    logger.setLevel(chosen_level)

    logger.info(f"Parsing log file: {log_file_path}")
    logger.info(f"Output report will be saved to: {output_file_path}")
    logger.info(f"Using threshold: {threshold}")

    parser = LogParser(
        log_file_path, output_file_path, threshold, log_level=chosen_level
    )
    parser.parse()


if __name__ == "__main__":
    main()
