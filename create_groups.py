#!/usr/bin/env python3

from setup_logger import logger
import random
import json


class CreateGroups:

    def __init__(self):
        self.names_list = []
        self.little_groups = {}

    def get_data_from_file(self):
        try:
            logger.info('open file (groupes.txt)')
            all_name = open(
                'files/groupes.txt', 'r').read()
        except ValueError:
            logger.error('file not found')
            print(f'error file not found = {ValueError}')
        else:
            self.names_list = list(map(str, all_name.split()))

    def generate_groups(self):
        max_nb_by_groups = int(input("Number of people per group:\n"))
        count = 1
        while max_nb_by_groups <= len(self.names_list):
            selected = random.sample(self.names_list, k=max_nb_by_groups)
            print(f'Group #{count} : {selected}')
            self.little_groups[f'GROUP_{str(count)}'] = selected
            for element in selected:
                self.names_list.remove(element)
            count += 1

    def create_json_file(self):
        logger.info('create json file')
        with open('files/json/groupes.json', 'w') as outfile:
            json.dump(self.little_groups, outfile, indent=4)

    def app_start(self):
        self.get_data_from_file()
        self.generate_groups()
        self.create_json_file()
