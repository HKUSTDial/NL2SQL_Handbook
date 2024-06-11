from utils import *
from dataset import *
import pandas as pd
import os


ALL_DATASETS = [
    ATIS(),
    GeoQuery(),
    Restaurants(),
    Academic(),
    IMDB(),
    Yelp(),
    Scholar(),
    WikiSQL(),
    Advising(),
    Spider(),
    BIRD()
]

def report_dataset(dataset: Dataset):
    report_database_complexity = generate_report_database_complexity(dataset.get_all_db_paths(), is_wikisql=isinstance(dataset, WikiSQL))
    report_query_complexity = generate_report_query_complexity(dataset.get_all_queries())
    num_questions = len(dataset.get_all_questions())
    num_quries = len(dataset.get_all_queries())
    dataset_report = {
        "Number of Questions": num_questions,
        "Number of Queries": num_quries,
        "Number of Questions / Number of Queries": round(num_questions / num_quries, 1)
    }
    dataset_report.update(report_database_complexity)
    dataset_report.update(report_query_complexity)
    return dataset_report


if __name__ == "__main__":
    for dataset in ALL_DATASETS:
        print(f"analyze [{dataset.__class__.__name__}] dataset...")
        report = report_dataset(dataset)
        dir = os.path.join("report", dataset.__class__.__name__)
        os.makedirs(dir, exist_ok=True)
        json.dump(report, open(os.path.join(dir, "report.json"), "w", encoding="utf-8"), indent=4)