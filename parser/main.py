from argparse import ArgumentParser
import logging

args = ArgumentParser()
args.add_help(description="""
Log Parser
Tool that reads raw log files, extract key log metrics, and outputs Markdown report summary.
""")
required_args = args.add_argument_group("required arguments", required=True)
required_args.add_argument("-f", "--file", help="Path to the input log file.", type=str)

optional_args = args.add_argument_group("optional arguments", required=False)
optional_args.add_argument(
    "-o", "--output", help="Path to the output Markdown report file.", type=str
)
optional_args.add_argument(
    "-t", "--threshold", help="Threshold for log metrics.", type=int, default=0
)
optional_args.add_argument(
    "-l", "--log-level", help="Set the logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL).", type=str, default="INFO"
)


def main():
    args = args.parse_args()
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




if __name__ == "__main__":
    main()
