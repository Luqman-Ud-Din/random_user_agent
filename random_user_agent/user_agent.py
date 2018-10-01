import json
import os
import random
import zipfile


class UserAgent:
    ATTRIBUTES_MAP = {
        'user_agents': [],
        'hardware_types': [],
        'software_types': [],
        'software_names': [],
        'software_engines': [],
        'operating_systems': [],
    }

    def __init__(self, *args, **kwargs):
        for attribute, default in self.ATTRIBUTES_MAP.items():
            setattr(self, attribute, kwargs.get(attribute, default))

        _user_agents = self._get_user_agents()
        self._hardware_types = set([ua['hardware_type'] for ua in _user_agents])
        self._software_types = set([ua['software_type'] for ua in _user_agents])
        self._software_names = set([ua['software_name'] for ua in _user_agents])
        self._software_engines = set([ua['software_engine'] for ua in _user_agents])
        self._operating_systems = set([ua['operating_system'] for ua in _user_agents])

        for user_agent in _user_agents:
            if self.hardware_types and user_agent['hardware_type'] not in self.hardware_types:
                continue

            if self.software_types and user_agent['software_type'] not in self.software_types:
                continue

            if self.software_names and user_agent['software_name'] not in self.software_names:
                continue

            if self.software_engines and user_agent['software_engine'] not in self.software_engines:
                continue

            if self.operating_systems and user_agent['operating_system'] not in self.operating_systems:
                continue

            self.user_agents += [user_agent['user_agent']]

    def _get_user_agents(self):
        file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'data/user_agents.zip')

        with zipfile.ZipFile(file_path) as zipped_user_agents:
            with zipped_user_agents.open('user_agents.json') as file:
                user_agents = file.read()

        return json.loads(user_agents)

    def random_user_agent(self):
        return random.choice(self.user_agents)

    @property
    def list_all_operating_systems(self):
        return self._operating_systems

    @property
    def list_all_hardware_types(self):
        return self._hardware_types

    @property
    def list_all_software_types(self):
        return self._software_types

    @property
    def list_all_software_names(self):
        return self._software_names

    @property
    def list_all_software_engines(self):
        return self._software_engines
