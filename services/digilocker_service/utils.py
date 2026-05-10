import os
import json

DATASET_PATH = r"D:\Projects\TCS\datasets"


def read_xml(path):

    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def read_json(path):

    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)