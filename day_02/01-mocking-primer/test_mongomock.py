#!/usr/bin/env python3
import pymongo
import pytest
import mongomock
import logging


class SampleHandler:
    """
    Fetches samples from mongo.foo.bar
    """

    DB_NAME = "foo"
    COLLECTION_NAME = "bar"

    def __init__(self):
        self.client = None

    def initialize_from_mongo_uri(self, mongo_uri: str):
        """
        Initialize SampleHandler / MongoDB connection
        """
        self.client = self._get_mongoclient(mongo_uri)
        logging.debug("initialized client: %s", type(self.client))
        self.db = self.client[self.DB_NAME]
        self.cx = self.db[self.COLLECTION_NAME]

    def get_sample(self, sample_id: str):
        """
        Fetch a sample by id from mongo
        """
        query = {"id": sample_id}

        return self.cx.find_one(query)

    def add_sample(self, sample_object: dict) -> pymongo.results.InsertOneResult:
        """
        Add a sample data to mongo
        """
        insert_result = self.cx.insert_one(sample_object)
        logging.debug(insert_result)
        return insert_result

    @staticmethod
    def _get_mongoclient(mongo_uri: str):
        """
        Initializes and returns mongoclient. This will be our mocking target.
        """
        return pymongo.MongoClient(mongo_uri)


@pytest.fixture()
def sample_handler():
    sample_handler = SampleHandler()
    return sample_handler


@pytest.fixture()
def patched_sample_handler(sample_handler, mocker):
    ...
    return sample_handler


@pytest.fixture()
def sample_object():
    sample = {"id": "foo", "status": "awaiting_sacrifice"}
    return sample
