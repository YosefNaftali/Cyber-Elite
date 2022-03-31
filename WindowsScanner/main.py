from sys import argv
from Printer import *
from Search import Search


def main(argv):
    try:
        printer = Printer()
        searcher = Search()
        severity = 'Default'
        if len(argv) > 1:
            if argv[1] == '-s':
                severity = argv[2]
            else:
                print('Unknown parameter')
                return

        search_data = searcher.search_machine(severity)
        printer.print_tuple_to_chart(search_data, ['Package Name', 'CVE ID', 'Severity'])
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main(argv)
