from icalendar import Calendar, Event
import json
import argparse

# Program to extract rooms from a calendar file (given as an inpute)
def main(args: argparse.Namespace):
    
    with open(args.input) as ics_file, open(args.output, "w") as class_file:

        calendar = Calendar.from_ical(ics_file.read())

        rooms_list = list()

        for component in calendar.walk():
            if component.name == "VEVENT":
                room = component.get('location')
                if(room not in rooms_list):
                    rooms_list.append(room)

        for room in rooms_list:
            print(room,"\n")
            class_file.write("%s\n" % room)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Extract all rooms from an ics file.')
    parser.add_argument("-i", "--input", required=True,
                        help="Path to the calendar file.")
    parser.add_argument("-o", "--output", required=True,
                        help="Path to the list class file (output).")

    args = parser.parse_args()

    main(args)