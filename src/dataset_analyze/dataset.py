import os
import json


class Dataset:
    
    def get_all_questions(self):
        raise NotImplementedError()
    
    def get_all_queries(self):
        raise NotImplementedError()

    def get_all_db_paths(self):
        raise NotImplementedError()


class ATIS(Dataset):
    
    ROOT_PATH = "data/atis"
    
    def get_all_questions(self):
        with open(os.path.join(self.ROOT_PATH, "atis.json"), "r", encoding="utf-8") as f:
            data = json.load(f)
        all_questions = []
        for item in data:
            for sentence in item["sentences"]:
                text = sentence["text"]
                for key, value in sentence["variables"].items():
                    text = text.replace(key, value)
                all_questions.append(text)
        return all_questions
            
    def get_all_queries(self):
        with open(os.path.join(self.ROOT_PATH, "atis.json"), "r", encoding="utf-8") as f:
            data = json.load(f)
        all_queries = []
        for item in data:
            all_queries.append(item["sql"][0])
        return all_queries

    def get_all_db_paths(self):
        return [os.path.join(self.ROOT_PATH, "atis-db.added-in-2020.sqlite")]


class GeoQuery(Dataset):
    
    ROOT_PATH = "data/geoquery"
    
    def get_all_questions(self):
        with open(os.path.join(self.ROOT_PATH, "geography.json"), "r", encoding="utf-8") as f:
            data = json.load(f)
        all_questions = []
        for item in data:
            for sentence in item["sentences"]:
                text = sentence["text"]
                for key, value in sentence["variables"].items():
                    text = text.replace(key, value)
                all_questions.append(text)
        return all_questions
    
    def get_all_queries(self):
        with open(os.path.join(self.ROOT_PATH, "geography.json"), "r", encoding="utf-8") as f:
            data = json.load(f)
        
        all_queries = []
        for item in data:
            all_queries.append(item["sql"][0])
            
        return all_queries
    
    def get_all_db_paths(self):
        return [os.path.join(self.ROOT_PATH, "geography-db.added-in-2020.sqlite")]
    

class Restaurants(Dataset):
    
    ROOT_PATH = "data/restaurants"
    
    def get_all_questions(self):
        with open(os.path.join(self.ROOT_PATH, "restaurants.json"), "r", encoding="utf-8") as f:
            data = json.load(f)
        all_questions = []
        for item in data:
            for sentence in item["sentences"]:
                text = sentence["text"]
                for key, value in sentence["variables"].items():
                    text = text.replace(key, value)
                all_questions.append(text)
        return all_questions
    
    def get_all_queries(self):
        with open(os.path.join(self.ROOT_PATH, "restaurants.json"), "r", encoding="utf-8") as f:
            data = json.load(f)
        
        all_queries = []
        for item in data:
            all_queries.append(item["sql"][0])
        
        return all_queries
    
    def get_all_db_paths(self):
        return [os.path.join(self.ROOT_PATH, "restaurants-db.added-in-2020.sqlite")]
    

class Scholar(Dataset):
    
    ROOT_PATH = "data/scholar"
    
    def get_all_questions(self):
        with open(os.path.join(self.ROOT_PATH, "scholar.json"), "r", encoding="utf-8") as f:
            data = json.load(f)
        all_questions = []
        for item in data:
            for sentence in item["sentences"]:
                text = sentence["text"]
                for key, value in sentence["variables"].items():
                    text = text.replace(key, value)
                all_questions.append(text)
        return all_questions
    
    def get_all_queries(self):
        with open(os.path.join(self.ROOT_PATH, "scholar.json"), "r", encoding="utf-8") as f:
            data = json.load(f)
        
        all_queries = []
        for item in data:
            all_queries.append(item["sql"][0])
        
        return all_queries
    
    def get_all_db_paths(self):
        return [os.path.join(self.ROOT_PATH, "scholar.db")]
    

class Academic(Dataset):
    
    ROOT_PATH = "data/academic"
    
    def get_all_questions(self):
        with open(os.path.join(self.ROOT_PATH, "academic.json"), "r", encoding="utf-8") as f:
            data = json.load(f)
        all_questions = []
        for item in data:
            for sentence in item["sentences"]:
                text = sentence["text"]
                for key, value in sentence["variables"].items():
                    text = text.replace(key, value)
                all_questions.append(text)
        return all_questions
    
    def get_all_queries(self):
        with open(os.path.join(self.ROOT_PATH, "academic.json"), "r", encoding="utf-8") as f:
            data = json.load(f)
        
        all_queries = []
        for item in data:
            all_queries.append(item["sql"][0])
        
        return all_queries
    
    def get_all_db_paths(self):
        return [os.path.join(self.ROOT_PATH, "MAS.db")]


class IMDB(Dataset):
    
    ROOT_PATH = "data/imdb"
    
    def get_all_questions(self):
        with open(os.path.join(self.ROOT_PATH, "imdb.json"), "r", encoding="utf-8") as f:
            data = json.load(f)
        all_questions = []
        for item in data:
            for sentence in item["sentences"]:
                text = sentence["text"]
                for key, value in sentence["variables"].items():
                    text = text.replace(key, value)
                all_questions.append(text)
        return all_questions
    
    def get_all_queries(self):
        with open(os.path.join(self.ROOT_PATH, "imdb.json"), "r", encoding="utf-8") as f:
            data = json.load(f)
        
        all_queries = []
        for item in data:
            all_queries.append(item["sql"][0])
        
        return all_queries
    
    def get_all_db_paths(self):
        return [os.path.join(self.ROOT_PATH, "IMDB.db")]


class Yelp(Dataset):
    
    ROOT_PATH = "data/yelp"
    
    def get_all_questions(self):
        with open(os.path.join(self.ROOT_PATH, "yelp.json"), "r", encoding="utf-8") as f:
            data = json.load(f)
        all_questions = []
        for item in data:
            for sentence in item["sentences"]:
                text = sentence["text"]
                for key, value in sentence["variables"].items():
                    text = text.replace(key, value)
                all_questions.append(text)
        return all_questions
    
    def get_all_queries(self):
        with open(os.path.join(self.ROOT_PATH, "yelp.json"), "r", encoding="utf-8") as f:
            data = json.load(f)
        
        all_queries = []
        for item in data:
            all_queries.append(item["sql"][0])
        
        return all_queries
    
    def get_all_db_paths(self):
        return [os.path.join(self.ROOT_PATH, "YELP.db")]


class Advising(Dataset):
    
    ROOT_PATH = "data/advising"
    
    def get_all_questions(self):
        with open(os.path.join(self.ROOT_PATH, "advising.json"), "r", encoding="utf-8") as f:
            data = json.load(f)
        all_questions = []
        for item in data:
            for sentence in item["sentences"]:
                text = sentence["text"]
                for key, value in sentence["variables"].items():
                    text = text.replace(key, value)
                all_questions.append(text)
        return all_questions
    
    def get_all_queries(self):
        with open(os.path.join(self.ROOT_PATH, "advising.json"), "r", encoding="utf-8") as f:
            data = json.load(f)
        
        all_queries = []
        for item in data:
            all_queries.append(item["sql"][0])
        
        return all_queries
    
    def get_all_db_paths(self):
        return [os.path.join(self.ROOT_PATH, "advising-db.added-in-2020.sqlite")]


class Spider(Dataset):
    
    ROOT_PATH = "data/spider"
    
    def get_all_questions(self):
        data_json = []
        data_json.extend(json.load(open(os.path.join(self.ROOT_PATH, "train_spider.json"), "r", encoding="utf-8")))
        data_json.extend(json.load(open(os.path.join(self.ROOT_PATH, "train_others.json"), "r", encoding="utf-8")))
        data_json.extend(json.load(open(os.path.join(self.ROOT_PATH, "dev.json"), "r", encoding="utf-8")))
        data_json.extend(json.load(open(os.path.join(self.ROOT_PATH, "test_data", "dev.json"), "r", encoding="utf-8")))
        all_questions = [item["question"] for item in data_json]
        return all_questions
    
    def get_all_queries(self):
        data_json = []
        data_json.extend(json.load(open(os.path.join(self.ROOT_PATH, "train_spider.json"), "r", encoding="utf-8")))
        data_json.extend(json.load(open(os.path.join(self.ROOT_PATH, "train_others.json"), "r", encoding="utf-8")))
        data_json.extend(json.load(open(os.path.join(self.ROOT_PATH, "dev.json"), "r", encoding="utf-8")))
        data_json.extend(json.load(open(os.path.join(self.ROOT_PATH, "test_data", "dev.json"), "r", encoding="utf-8")))
        all_queries = list(set([item["query"].strip() for item in data_json]))
        return all_queries
    
    def get_all_db_paths(self):
        # Note that, all databases have been in "test_database" directory
        db_paths = [os.path.join(self.ROOT_PATH, "test_database", db_id, f"{db_id}.sqlite") for db_id in os.listdir(os.path.join(self.ROOT_PATH, "test_database"))]
        # db_paths.extend(
        #     [os.path.join(self.ROOT_PATH, "test_database", db_id) for db_id in os.listdir(os.path.join(self.ROOT_PATH, "test_database"))]
        # )
        return db_paths


class WikiSQL(Dataset):
    
    ROOT_PATH = "data/wikisql"
    
    def get_all_questions(self):
        all_data_json = []
        for data_file in ["train.jsonl", "dev.jsonl", "test.jsonl"]:
            with open(os.path.join(self.ROOT_PATH, data_file), "r", encoding="utf-8") as f:
                lines = f.readlines()
                all_data_json.extend([json.loads(line) for line in lines])
        return [item["question"] for item in all_data_json]
    
    def get_all_queries(self):
        all_data_json = []
        for data_file in ["train.jsonl", "dev.jsonl", "test.jsonl"]:
            with open(os.path.join(self.ROOT_PATH, data_file), "r", encoding="utf-8") as f:
                lines = f.readlines()
                all_data_json.extend([json.loads(line) for line in lines])
        all_queries = []
        # Note: For WikiSQL, we only need to consider whether it contains agg op
        for item in all_data_json:
            if item["sql"]["agg"] == 0:
                # no agg:
                all_queries.append("SELECT dummy_colum FROM dummy_table;")
            else:
                all_queries.append("SELECT max(dummy_colum) FROM dummy_table;")
        return all_queries
    
    def get_all_db_paths(self):
        return [os.path.join(self.ROOT_PATH, "train.db"),
                os.path.join(self.ROOT_PATH, "dev.db"),
                os.path.join(self.ROOT_PATH, "test.db")]


class BIRD(Dataset):
    
    ROOT_PATH = "data/bird"
    
    def get_all_questions(self):
        data_json = []
        data_json.extend(json.load(open(os.path.join(self.ROOT_PATH, "train", "train.json"), "r", encoding="utf-8")))
        data_json.extend(json.load(open(os.path.join(self.ROOT_PATH, "dev", "dev.json"), "r", encoding="utf-8")))
        all_questions = [item["question"] for item in data_json]
        return all_questions
    
    def get_all_queries(self):
        data_json = []
        data_json.extend(json.load(open(os.path.join(self.ROOT_PATH, "train", "train.json"), "r", encoding="utf-8")))
        data_json.extend(json.load(open(os.path.join(self.ROOT_PATH, "dev", "dev.json"), "r", encoding="utf-8")))
        all_queries = list(set([item["SQL"].strip() for item in data_json]))
        return all_queries
    
    def get_all_db_paths(self):
        db_paths = [os.path.join(self.ROOT_PATH, "dev", "dev_databases", db_id, f"{db_id}.sqlite") for db_id in os.listdir(os.path.join(self.ROOT_PATH, "dev", "dev_databases"))]
        db_paths.extend(
            [os.path.join(self.ROOT_PATH, "train", "train_databases", db_id, f"{db_id}.sqlite") for db_id in os.listdir(os.path.join(self.ROOT_PATH, "train", "train_databases"))]
        )
        return db_paths
    

class CSpider(Dataset):
    
    ROOT_PATH = "data/cspider"
    
    def get_all_questions(self):
        data_json = []
        data_json.extend(json.load(open(os.path.join(self.ROOT_PATH, "train.json"), "r", encoding="utf-8")))
        data_json.extend(json.load(open(os.path.join(self.ROOT_PATH, "dev.json"), "r", encoding="utf-8")))
        data_json.extend(json.load(open(os.path.join(self.ROOT_PATH, "test_data", "test.json"), "r", encoding="utf-8")))
        all_questions = [item["question"] for item in data_json]
        return all_questions
    
    def get_all_queries(self):
        data_json = []
        data_json.extend(json.load(open(os.path.join(self.ROOT_PATH, "train.json"), "r", encoding="utf-8")))
        data_json.extend(json.load(open(os.path.join(self.ROOT_PATH, "dev.json"), "r", encoding="utf-8")))
        data_json.extend(json.load(open(os.path.join(self.ROOT_PATH, "test_data", "test.json"), "r", encoding="utf-8")))
        all_queries = list(set([item["query"].strip() for item in data_json]))
        return all_queries
    
    def get_all_db_paths(self):
        db_paths = [os.path.join(self.ROOT_PATH, "test_database", db_id, f"{db_id}.sqlite") for db_id in os.listdir(os.path.join(self.ROOT_PATH, "test_database"))]
        db_paths.extend(
            [os.path.join(self.ROOT_PATH, "database", db_id, f"{db_id}.sqlite") for db_id in os.listdir(os.path.join(self.ROOT_PATH, "database"))]
        )
        return db_paths


class SParC(Dataset):
    
    ROOT_PATH = "data/sparc"
    
    def get_all_questions(self):
        data_json = []
        for item in json.load(open(os.path.join(self.ROOT_PATH, "train.json"), "r", encoding="utf-8")):
            interaction = item["interaction"]
            for turn in interaction:
                data_json.append({
                    "question": turn["utterance"],
                    "query": turn["query"]
                })
        for item in json.load(open(os.path.join(self.ROOT_PATH, "dev.json"), "r", encoding="utf-8")):
            interaction = item["interaction"]
            for turn in interaction:
                data_json.append({
                    "question": turn["utterance"],
                    "query": turn["query"]
                })
        all_questions = [item["question"] for item in data_json]
        return all_questions
        
    def get_all_queries(self):
        data_json = []
        for item in json.load(open(os.path.join(self.ROOT_PATH, "train.json"), "r", encoding="utf-8")):
            interaction = item["interaction"]
            for turn in interaction:
                data_json.append({
                    "question": turn["utterance"],
                    "query": turn["query"]
                })
        for item in json.load(open(os.path.join(self.ROOT_PATH, "dev.json"), "r", encoding="utf-8")):
            interaction = item["interaction"]
            for turn in interaction:
                data_json.append({
                    "question": turn["utterance"],
                    "query": turn["query"]
                })
        all_queries = list(set([item["query"].strip() for item in data_json]))
        return all_queries

    def get_all_db_paths(self):
        db_paths = [os.path.join(self.ROOT_PATH, "database", db_id, f"{db_id}.sqlite") for db_id in os.listdir(os.path.join(self.ROOT_PATH, "database"))]
        return db_paths


class CoSpider(Dataset):
    
    ROOT_PATH = "data/cospider"
    
    def get_all_questions(self):
        data_json = []
        for item in json.load(open(os.path.join(self.ROOT_PATH, "sql_state_tracking", "cosql_train.json"), "r", encoding="utf-8")):
            interaction = item["interaction"]
            for turn in interaction:
                data_json.append({
                    "question": turn["utterance"],
                    "query": turn["query"]
                })
        for item in json.load(open(os.path.join(self.ROOT_PATH, "sql_state_tracking", "cosql_dev.json"), "r", encoding="utf-8")):
            interaction = item["interaction"]
            for turn in interaction:
                data_json.append({
                    "question": turn["utterance"],
                    "query": turn["query"]
                })
        all_questions = [item["question"] for item in data_json]
        return all_questions
    
    def get_all_queries(self):
        data_json = []
        for item in json.load(open(os.path.join(self.ROOT_PATH, "sql_state_tracking", "cosql_train.json"), "r", encoding="utf-8")):
            interaction = item["interaction"]
            for turn in interaction:
                data_json.append({
                    "question": turn["utterance"],
                    "query": turn["query"]
                })
        for item in json.load(open(os.path.join(self.ROOT_PATH, "sql_state_tracking", "cosql_dev.json"), "r", encoding="utf-8")):
            interaction = item["interaction"]
            for turn in interaction:
                data_json.append({
                    "question": turn["utterance"],
                    "query": turn["query"]
                })
        # need to fix "> =" and "< =" issues
        all_queries = list(set([item["query"].strip().replace("> =", ">=").replace("< =", "<=") for item in data_json]))
        return all_queries
    
    def get_all_db_paths(self):
        db_paths = [os.path.join(self.ROOT_PATH, "database", db_id, f"{db_id}.sqlite") for db_id in os.listdir(os.path.join(self.ROOT_PATH, "database"))]
        return db_paths


if __name__ == "__main__":
    dataset = Advising()
    print(len(dataset.get_all_questions()))
    print(len(dataset.get_all_queries()))
    print(len(dataset.get_all_db_paths()))