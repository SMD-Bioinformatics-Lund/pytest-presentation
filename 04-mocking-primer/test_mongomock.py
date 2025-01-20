#!/usr/bin/env python3
import pymongo


class MongoDB:
    def __init__(self, mongo_uri: str = "localhost:27017"):
        self.cx = MongoDB._get_mongoclient(mongo_uri)

    @staticmethod
    def _get_mongoclient(mongo_uri: str):
        return pymongo.MongoClient(mongo_uri)

    def get_sample(self, query: dict | None):
        if query is None:
            query = {}

        # TODO: collections
        self.cx.find_one(query)

    def add_sample(self, sample_object: dict) -> pymongo.results.InsertOneResult:
        insert_result = self.cx.insert_one(sample_object)
        return insert_result


def empty_mock_mongodb():
    ...


@pytest.fixture()
def sample_object():
    sample = {"id": "foo", "status": "awaiting_sacrifice"}
    return sample
