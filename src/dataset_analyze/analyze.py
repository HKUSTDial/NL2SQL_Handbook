from utils import *
from dataset import *
import pandas as pd
import os


ALL_DATASETS = [
    # ATIS(),
    # GeoQuery(),
    # Restaurants(),
    # Academic(),
    # IMDB(),
    # Yelp(),
    # Scholar(),
    # WikiSQL(),
    # Advising(),
    # Spider(),
    # BIRD(),
    # CSpider(),
    # SParC(),
    # CoSpider(),
    # SpiderSyn(),
    # SpiderRealistic(),
    # SpiderDK(),
    # DrSpider(),
    # SQUALL(),
    # FIBEN(),
    # KaggleDBQA(),
    # SEDE(),
    # MTTEQL(),
    # AmbiQT(),
    # ScienceBenchmark(),
    # BULL(),
    # BookSQL(),
    # PAUQ(),
    # CHASE(),
    # DuSQL(),
    # ViText2SQL(),
    # MIMICSQL(),
    # PortugueseSpider(),
    Archer()
]

def report_dataset(dataset: Dataset):
    if dataset.get_all_db_paths():
        report_database_complexity = generate_report_database_complexity(dataset.get_all_db_paths(), is_wikisql=isinstance(dataset, WikiSQL))
    else:
        report_database_complexity = {
            "Total Databases": dataset._total_databases,
            "Total Tables": dataset._total_tables,
            "Average Tables per Database": dataset._avg_tables_per_db,
            "Average Columns per Table": dataset._avg_columns_per_table,
            "Average Records per Database": dataset._avg_records_per_db
        }
    if isinstance(dataset, WikiSQL):
        _queries = [query.split("WHERE")[0].strip() for query in dataset.get_all_queries()]
        report_query_complexity = generate_report_query_complexity(_queries)
    else:
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