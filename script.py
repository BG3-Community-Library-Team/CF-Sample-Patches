#!/usr/bin/env python3

import xml.etree.ElementTree as ET
import argparse

parser = argparse.ArgumentParser(description='Extracts uuids from the Progressions file')

parser.add_argument('--xmlpath', type=str, required=True, help='Path to the XML file')
parser.add_argument('name', type=str, help='Name parameter')
parser.add_argument('levels', type=int, nargs='+', help='List of level parameters')


# Parse the command-line arguments
args = parser.parse_args()

def parse_xml(xml_path, name, levels):
    # use root = ET.fromstring('xml string content') for debugging/testing
    tree = ET.parse(xml_path)
    root = tree.getroot()
    result = []
    for progression_node in root.findall('.//node[@id="Progression"]'):
        level = int(progression_node.find('attribute[@id="Level"]').attrib['value'])
        if level in levels:
            name_attr = progression_node.find('attribute[@id="Name"]')
            if name_attr is not None and name_attr.attrib['value'] == name:
                uuid_attr = progression_node.find('attribute[@id="UUID"]')
                if uuid_attr is not None:
                    result.append(uuid_attr.attrib['value'])
    
    return result
    
output = parse_xml(args.xmlpath, args.name, args.levels);
print(output)

# usage
# python script.py Magus 1 5 10 --xmlpath path/to/xml/file