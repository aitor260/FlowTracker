import sys
from flowtracker.ui.cli.main import main as cli_main

def main():
    cli_main(sys.argv[1:])

if __name__ == "__main__":
    main()