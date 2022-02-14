from typing import Mapping
from .service import Service


class Registry:
    def __init__(self):
        self.state: Mapping[str, Service] = {}

    def all(self):
        return [i.to_dict() for i in self.state.values()]

    def get_service(self, name: str):
        service = self.state.get(name.lower())
        return service

    def create_service(self, name: str):
        new_service = Service(name.lower(), [])
        self.state[name.lower()] = new_service
        return new_service

    def remove_service(self, name: str):
        del self.state[name.lower()]
