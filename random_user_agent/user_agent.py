import json
import os
import random
import zipfile


class UserAgent:
    ATTRIBUTES_MAP = {
        'hardware_types': [],
        'software_types': [],
        'software_names': [],
        'software_engines': [],
        'operating_systems': [],
    }

    def __init__(self, *args, **kwargs):
        self.raw_user_agents = []
        self.user_agents = []

        for attribute, values in self.ATTRIBUTES_MAP.items():
            setattr(self, attribute, kwargs.get(attribute, [v.lower() for v in values]))

        for user_agent in self.load_user_agents():
            if self.hardware_types and user_agent['hardware_type'].lower() not in self.hardware_types:
                continue

            if self.software_types and user_agent['software_type'].lower() not in self.software_types:
                continue

            if self.software_names and user_agent['software_name'].lower() not in self.software_names:
                continue

            if self.software_engines and user_agent['software_engine'].lower() not in self.software_engines:
                continue

            if self.operating_systems and user_agent['operating_system'].lower() not in self.operating_systems:
                continue

            self.user_agents += [user_agent['user_agent']]
            self.raw_user_agents += [user_agent]

    def load_user_agents(self):
        file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'data/user_agents.zip')

        with zipfile.ZipFile(file_path) as zipped_user_agents:
            with zipped_user_agents.open('user_agents.json') as file:
                user_agents = file.read()

        if hasattr(user_agents, 'decode'):
            user_agents = user_agents.decode()

        return json.loads(user_agents)

    def get_user_agents(self):
        return self.raw_user_agents

    def get_random_user_agent(self):
        return random.choice(self.user_agents)

    def get_operating_systems(self):
        return set([ua['operating_system'].lower() for ua in self.get_user_agents()])

    def get_hardware_types(self):
        return set([ua['hardware_type'].lower() for ua in self.get_user_agents()])

    def get_software_types(self):
        return set([ua['software_type'].lower() for ua in self.get_user_agents()])

    def get_software_names(self):
        return set([ua['software_name'].lower() for ua in self.get_user_agents()])

    def get_software_engines(self):
        return set([ua['software_engine'].lower() for ua in self.get_user_agents()])
