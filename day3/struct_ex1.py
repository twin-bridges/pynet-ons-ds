#! /usr/bin/env python
import json
from pprint import pprint


def load_data_from_string(filename):
    with open(filename, "r") as infile:
        infile = infile.read()
    structured_data = json.loads(infile)
    return structured_data


def main():
    structured_data = load_data_from_string("struct_data1.txt")
    pprint(structured_data)
    print()

    print(type(structured_data))
    print(len(structured_data))
    print()

    print(type(structured_data[0]))
    print(len(structured_data[0]))
    print()

    parsed_data = {}
    for route_entry in structured_data:
        if route_entry["protocol"] == "L":
            pass
        else:
            parsed_data[route_entry["network"]] = {}
            parsed_data[route_entry["network"]]["nexthop_interface"] = route_entry[
                "nexthop_if"
            ]
            parsed_data[route_entry["network"]]["nexthop_ip"] = route_entry[
                "nexthop_ip"
            ]

    pprint(parsed_data)


if __name__ == "__main__":
    main()
