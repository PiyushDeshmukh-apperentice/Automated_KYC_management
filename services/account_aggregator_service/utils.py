import json
import os

DATASET_PATH = r"D:\Projects\TCS\datasets"


def read_json(path):

    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)