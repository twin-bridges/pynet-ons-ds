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
        if route_entry["protocol"] != "L":
            network = route_entry["network"]
            nexthop_if = route_entry["nexthop_if"]
            nexthop_ip = route_entry["nexthop_ip"]
            parsed_data[network] = {}
            parsed_data[network]["nexthop_interface"] = nexthop_if
            parsed_data[network]["nexthop_ip"] = nexthop_ip

    pprint(parsed_data)


if __name__ == "__main__":
    main()
