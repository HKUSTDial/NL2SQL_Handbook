import os
import json
import pandas as pd


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
    
    agg_ops = ['', 'MAX', 'MIN', 'COUNT', 'SUM', 'AVG']
    cond_ops = ['=', '>', '<', 'OP']
    
    def get_all_questions(self):
        all_data_json = []
        for data_file in ["train.jsonl", "dev.jsonl", "test.jsonl"]:
            with open(os.path.join(self.ROOT_PATH, data_file), "r", encoding="utf-8") as f:
                lines = f.readlines()
                all_data_json.extend([json.loads(line) for line in lines])
        return [item["question"] for item in all_data_json]
    
    def get_all_queries(self):
        all_queries = []
        
        tables = dict()
        with open(os.path.join(self.ROOT_PATH, "train.tables.jsonl"), "r", encoding="utf-8") as f:
            for line in f.readlines():
                item = json.loads(line)
                tables[item["id"]] = item
        with open(os.path.join(self.ROOT_PATH, "train.jsonl"), "r", encoding="utf-8") as f:
            for line in f.readlines():
                item = json.loads(line)
                sel_col_name = tables[item["table_id"]]["header"][item["sql"]["sel"]]
                agg_name = self.agg_ops[item["sql"]["agg"]]
                table_name = tables[item["table_id"]].get("name", item["table_id"])
                if agg_name:
                    rep = 'SELECT {agg}(`{sel}`) FROM `{table}`'.format(
                        agg=agg_name,
                        sel=sel_col_name,
                        table=table_name
                    )
                else:
                    rep = 'SELECT `{sel}` FROM `{table}`'.format(
                        sel=sel_col_name,
                        table=table_name
                    )
                if item["sql"]["conds"]:
                    rep +=  ' WHERE ' + ' AND '.join(["`{}` {} {}".format(tables[item["table_id"]]["header"][i], self.cond_ops[o], v) for i, o, v in item["sql"]["conds"]])
                all_queries.append(rep)
                
        
        tables = dict()
        with open(os.path.join(self.ROOT_PATH, "dev.tables.jsonl"), "r", encoding="utf-8") as f:
            for line in f.readlines():
                item = json.loads(line)
                tables[item["id"]] = item
        with open(os.path.join(self.ROOT_PATH, "dev.jsonl"), "r", encoding="utf-8") as f:
            for line in f.readlines():
                item = json.loads(line)
                sel_col_name = tables[item["table_id"]]["header"][item["sql"]["sel"]]
                agg_name = self.agg_ops[item["sql"]["agg"]]
                table_name = tables[item["table_id"]].get("name", item["table_id"])
                if agg_name:
                    rep = 'SELECT {agg}(`{sel}`) FROM `{table}`'.format(
                        agg=agg_name,
                        sel=sel_col_name,
                        table=table_name
                    )
                else:
                    rep = 'SELECT `{sel}` FROM `{table}`'.format(
                        sel=sel_col_name,
                        table=table_name
                    )
                if item["sql"]["conds"]:
                    rep +=  ' WHERE ' + ' AND '.join(["`{}` {} {}".format(tables[item["table_id"]]["header"][i], self.cond_ops[o], v) for i, o, v in item["sql"]["conds"]])
                all_queries.append(rep)
                
        tables = dict()
        with open(os.path.join(self.ROOT_PATH, "test.tables.jsonl"), "r", encoding="utf-8") as f:
            for line in f.readlines():
                item = json.loads(line)
                tables[item["id"]] = item
        with open(os.path.join(self.ROOT_PATH, "test.jsonl"), "r", encoding="utf-8") as f:
            for line in f.readlines():
                item = json.loads(line)
                sel_col_name = tables[item["table_id"]]["header"][item["sql"]["sel"]]
                agg_name = self.agg_ops[item["sql"]["agg"]]
                table_name = tables[item["table_id"]].get("name", item["table_id"])
                if agg_name:
                    rep = 'SELECT {agg}(`{sel}`) FROM `{table}`'.format(
                        agg=agg_name,
                        sel=sel_col_name,
                        table=table_name
                    )
                else:
                    rep = 'SELECT `{sel}` FROM `{table}`'.format(
                        sel=sel_col_name,
                        table=table_name
                    )
                if item["sql"]["conds"]:
                    rep +=  ' WHERE ' + ' AND '.join(["`{}` {} {}".format(tables[item["table_id"]]["header"][i], self.cond_ops[o], v) for i, o, v in item["sql"]["conds"]])
                all_queries.append(rep)
                
        all_queries = list(set(all_queries))
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


class SpiderSyn(Dataset):
    
    ROOT_PATH = "data/spider_syn"
    
    def get_all_questions(self):
        data_json = json.load(open(os.path.join(self.ROOT_PATH, "dev.json"), "r", encoding="utf-8"))
        all_questions = [item["SpiderSynQuestion"] for item in data_json]
        return all_questions
    
    def get_all_queries(self):
        data_json = json.load(open(os.path.join(self.ROOT_PATH, "dev.json"), "r", encoding="utf-8"))
        all_queries = list(set([item["query"].strip() for item in data_json]))
        return all_queries
    
    def get_all_db_paths(self):
        db_paths = [os.path.join(self.ROOT_PATH, "database", db_id, f"{db_id}.sqlite") for db_id in os.listdir(os.path.join(self.ROOT_PATH, "database"))]
        return db_paths
    
    
class SpiderRealistic(Dataset):
    
    ROOT_PATH = "data/spider_realistic"
    
    def get_all_questions(self):
        data_json = json.load(open(os.path.join(self.ROOT_PATH, "spider_realistic.json"), "r", encoding="utf-8"))
        all_questions = [item["question"] for item in data_json]
        return all_questions
    
    def get_all_queries(self):
        data_json = json.load(open(os.path.join(self.ROOT_PATH, "spider_realistic.json"), "r", encoding="utf-8"))
        all_queries = list(set([item["query"].strip() for item in data_json]))
        return all_queries
    
    def get_all_db_paths(self):
        db_paths = [os.path.join(self.ROOT_PATH, "database", db_id, f"{db_id}.sqlite") for db_id in os.listdir(os.path.join(self.ROOT_PATH, "database"))]
        return db_paths


class SpiderDK(Dataset):
    
    ROOT_PATH = "data/spider_dk"
    
    def get_all_questions(self):
        data_json = json.load(open(os.path.join(self.ROOT_PATH, "spider_dk.json"), "r", encoding="utf-8"))
        all_questions = [item["question"] for item in data_json]
        return all_questions
    
    def get_all_queries(self):
        data_json = json.load(open(os.path.join(self.ROOT_PATH, "spider_dk.json"), "r", encoding="utf-8"))
        all_queries = list(set([item["query"].strip() for item in data_json]))
        return all_queries
    
    def get_all_db_paths(self):
        db_paths = [os.path.join(self.ROOT_PATH, "database", db_id, f"{db_id}.sqlite") for db_id in os.listdir(os.path.join(self.ROOT_PATH, "database"))]
        return db_paths


class DrSpider(Dataset):
    
    ROOT_PATH = "data/dr_spider"
    
    def get_all_questions(self):
        all_perturbations = os.listdir(os.path.join(self.ROOT_PATH))
        data_json = []
        for perturbation in all_perturbations:
            if perturbation.startswith("DB_"):
                question_file_name = "questions_post_perturbation.json"
            else:
                question_file_name = "questions_post_perturbation.json"
            data_json.extend(json.load(open(os.path.join(self.ROOT_PATH, perturbation, question_file_name), "r", encoding="utf-8")))

        all_questions = [item["question"] for item in data_json]
        return all_questions
    
    def get_all_queries(self):
        all_perturbations = os.listdir(os.path.join(self.ROOT_PATH))
        data_json = []
        for perturbation in all_perturbations:
            if perturbation.startswith("DB_"):
                question_file_name = "questions_post_perturbation.json"
            else:
                question_file_name = "questions_post_perturbation.json"
            data_json.extend(json.load(open(os.path.join(self.ROOT_PATH, perturbation, question_file_name), "r", encoding="utf-8")))

        all_queries = list(set([item["query"].strip() for item in data_json]))
        return all_queries
    
    def get_all_db_paths(self):
        all_perturbations = os.listdir(os.path.join(self.ROOT_PATH))
        db_paths = []
        for perturbation in all_perturbations:
            if perturbation.startswith("DB_"):
                db_dir_name = "database_post_perturbation"
            else:
                db_dir_name = "databases"
            for db_id in os.listdir(os.path.join(self.ROOT_PATH, perturbation, db_dir_name)):
                if os.path.isdir(os.path.join(self.ROOT_PATH, perturbation, db_dir_name, db_id)):
                    db_paths.append(os.path.join(self.ROOT_PATH, perturbation, db_dir_name, db_id, f"{db_id}.sqlite"))
        return db_paths
    

class SQUALL(Dataset):
    
    ROOT_PATH = "data/squall"
    
    def get_all_questions(self):
        all_data_json = json.load(open(os.path.join(self.ROOT_PATH, "squall.json"), "r", encoding="utf-8"))
        return [" ".join(item["nl"]) for item in all_data_json]
    
    def get_all_queries(self):
        all_data_json = json.load(open(os.path.join(self.ROOT_PATH, "squall.json"), "r", encoding="utf-8"))
        all_queries = []
        for item in all_data_json:
            sql = " ".join([tok[1] for tok in item["sql"]])
            all_queries.append(sql.strip())
        return list(set(all_queries))
    
    def get_all_db_paths(self):
        db_paths = [os.path.join(self.ROOT_PATH, "db", db_file) for db_file in os.listdir(os.path.join(self.ROOT_PATH, "db"))]
        return db_paths
    

class FIBEN(Dataset):
    
    ROOT_PATH = "data/fiben"
    
    def __init__(self):
        all_table_csv = os.listdir(os.path.join(self.ROOT_PATH, "data"))
        self._total_databases = 1
        self._total_tables = len(all_table_csv)
        all_table_dataframe = []
        for table_csv in all_table_csv:
            try:
                df = pd.read_csv(os.path.join(self.ROOT_PATH, "data", table_csv), header=None, low_memory=False)
                all_table_dataframe.append(df)
            except pd.errors.EmptyDataError:
                all_table_dataframe.append(pd.DataFrame())
        total_columns, total_records = 0, 0
        for table_dataframe in all_table_dataframe:
            total_columns += len(table_dataframe.columns)
            total_records += len(table_dataframe)
        self._avg_tables_per_db = self._total_tables / self._total_databases
        self._avg_columns_per_table = total_columns / self._total_tables
        self._avg_records_per_db = total_records / self._total_databases
    
    def get_all_questions(self):
        all_data_json = json.load(open(os.path.join(self.ROOT_PATH, "FIBEN_Queries.json"), "r", encoding="utf-8"))
        return [item["question"] for item in all_data_json]
    
    def get_all_queries(self):
        all_data_json = json.load(open(os.path.join(self.ROOT_PATH, "FIBEN_Queries.json"), "r", encoding="utf-8"))
        all_queries = list(set([item["SQL"].strip() for item in all_data_json]))
        return all_queries
    
    def get_all_db_paths(self):
        return []
    

class KaggleDBQA(Dataset):
    
    ROOT_PATH = "data/kaggledbqa"
    
    def get_all_questions(self):
        all_data_json = []
        for filename in os.listdir(os.path.join(self.ROOT_PATH, "examples")):
            if "_fewshot" in filename or "_test" in filename:
                continue
            all_data_json.extend(json.load(open(os.path.join(self.ROOT_PATH, "examples", filename), "r", encoding="utf-8")))
        return [item["question"] for item in all_data_json]
    
    def get_all_queries(self):
        all_data_json = []
        for filename in os.listdir(os.path.join(self.ROOT_PATH, "examples")):
            if "_fewshot" in filename or "_test" in filename:
                continue
            all_data_json.extend(json.load(open(os.path.join(self.ROOT_PATH, "examples", filename), "r", encoding="utf-8")))
        all_queries = list(set([item["query"].strip() for item in all_data_json]))
        return all_queries
    
    def get_all_db_paths(self):
        db_paths = [os.path.join(self.ROOT_PATH, "databases", db_id, f"{db_id}.sqlite") for db_id in os.listdir(os.path.join(self.ROOT_PATH, "databases"))]
        return db_paths
    

class SEDE(Dataset):
    
    ROOT_PATH = "data/sede"
    
    def __init__(self):
        schemas = json.load(open(os.path.join(self.ROOT_PATH, "tables_so.json"), "r", encoding="utf-8"))
        self._total_databases = len(schemas)
        self._total_tables = 0
        total_columns, total_records = 0, 0
        for db in schemas:
            self._total_tables += len(db["table_names_original"])
            total_columns += (len(db["column_names_original"]) - 1) # ignore star col
        self._avg_tables_per_db = self._total_tables / self._total_databases
        self._avg_columns_per_table = total_columns / self._total_tables
        self._avg_records_per_db = total_records / self._total_databases
    
    def get_all_questions(self):
        all_data_json = []
        for filename in ["train.jsonl", "val.jsonl", "test.jsonl"]:
            with open(os.path.join(self.ROOT_PATH, filename), "r", encoding="utf-8") as f:
                for line in f.readlines():
                    sample = json.loads(line)
                    all_data_json.append(sample)
        return [item["Title"] for item in all_data_json]
    
    def get_all_queries(self):
        all_data_json = []
        for filename in ["train.jsonl", "val.jsonl", "test.jsonl"]:
            with open(os.path.join(self.ROOT_PATH, filename), "r", encoding="utf-8") as f:
                for line in f.readlines():
                    sample = json.loads(line)
                    all_data_json.append(sample)
        all_queries = list(set([item["QueryBody"].split("\n\n")[-1] for item in all_data_json]))
        return all_queries
    
    def get_all_db_paths(self):
        return []


class MTTEQL(Dataset):
    
    ROOT_PATH = "data/mt_teql"
    
    def __init__(self):
        schemas = []
        for filename in ["dev-tables.json", "train-tables.json"]:
            schemas.extend(json.load(open(os.path.join(self.ROOT_PATH, filename), "r", encoding="utf-8")))
        self._total_databases = len(schemas)
        self._total_tables = 0
        total_columns, total_records = 0, 0
        for db in schemas:
            self._total_tables += len(db["table_names_original"])
            total_columns += (len(db["column_names_original"]) - 1) # ignore star col
        self._avg_tables_per_db = self._total_tables / self._total_databases
        self._avg_columns_per_table = total_columns / self._total_tables
        self._avg_records_per_db = total_records / self._total_databases
    
    def get_all_questions(self):
        all_data_json = []
        for filename in ["train.json", "dev.json"]:
            all_data_json.extend(json.load(open(os.path.join(self.ROOT_PATH, filename), "r", encoding="utf-8")))
        return [item["question"] for item in all_data_json]
    
    def get_all_queries(self):
        all_data_json = []
        for filename in ["train.json", "dev.json"]:
            all_data_json.extend(json.load(open(os.path.join(self.ROOT_PATH, filename), "r", encoding="utf-8")))
        all_queries = []
        for item in all_data_json:
            if "query" in item:
                all_queries.append(item["query"].strip())
        all_queries = list(set(all_queries))
        return all_queries
    
    def get_all_db_paths(self):
        return []


class AmbiQT(Dataset):
    
    ROOT_PATH = "data/ambiqt"
    
    def get_all_questions(self):
        all_data_json = []
        for benchmark_type in os.listdir(os.path.join(self.ROOT_PATH, "benchmark")):
            all_data_json.extend(json.load(open(os.path.join(self.ROOT_PATH, "benchmark", benchmark_type, "train.json"), "r", encoding="utf-8")))
            all_data_json.extend(json.load(open(os.path.join(self.ROOT_PATH, "benchmark", benchmark_type, "validation.json"), "r", encoding="utf-8")))
        return [item["question"] for item in all_data_json]
    
    def get_all_queries(self):
        all_data_json = []
        for benchmark_type in os.listdir(os.path.join(self.ROOT_PATH, "benchmark")):
            all_data_json.extend(json.load(open(os.path.join(self.ROOT_PATH, "benchmark", benchmark_type, "train.json"), "r", encoding="utf-8")))
            all_data_json.extend(json.load(open(os.path.join(self.ROOT_PATH, "benchmark", benchmark_type, "validation.json"), "r", encoding="utf-8")))
        all_queries = []
        all_queries.extend([item["query1"].strip() for item in all_data_json])
        all_queries.extend([item["query2"].strip() for item in all_data_json])
        all_queries = list(set(all_queries))
        return all_queries
    
    def get_all_db_paths(self):
        db_paths = [os.path.join(self.ROOT_PATH, "database", db_id, f"{db_id}.sqlite") for db_id in os.listdir(os.path.join(self.ROOT_PATH, "database"))]
        return db_paths


class ScienceBenchmark(Dataset):
    
    ROOT_PATH = "data/sciencebenchmark"
    
    def __init__(self):
        self._total_databases = -1
        self._total_tables = -1
        total_columns, total_records = 0, 0
        self._avg_tables_per_db = self._total_tables / self._total_databases
        self._avg_columns_per_table = total_columns / self._total_tables
        self._avg_records_per_db = total_records / self._total_databases
    
    def get_all_questions(self):
        all_data_json = []
        for domain in os.listdir(self.ROOT_PATH):
            all_data_json.extend(
                json.load(open(os.path.join(self.ROOT_PATH, domain, "seed.json"), "r", encoding="utf-8"))
            )
            all_data_json.extend(
                json.load(open(os.path.join(self.ROOT_PATH, domain, "dev.json"), "r", encoding="utf-8"))
            )
            all_data_json.extend(
                json.load(open(os.path.join(self.ROOT_PATH, domain, "synth.json"), "r", encoding="utf-8"))
            )
        return [item["question"] for item in all_data_json]
    
    def get_all_queries(self):
        all_data_json = []
        for domain in os.listdir(self.ROOT_PATH):
            all_data_json.extend(
                json.load(open(os.path.join(self.ROOT_PATH, domain, "seed.json"), "r", encoding="utf-8"))
            )
            all_data_json.extend(
                json.load(open(os.path.join(self.ROOT_PATH, domain, "dev.json"), "r", encoding="utf-8"))
            )
            all_data_json.extend(
                json.load(open(os.path.join(self.ROOT_PATH, domain, "synth.json"), "r", encoding="utf-8"))
            )
        all_queries = [item["query"].strip() for item in all_data_json]
        all_queries = list(set(all_queries))
        return all_queries
    
    def get_all_db_paths(self):
        db_paths = []
        return db_paths


class BULL(Dataset):
    
    """_summary_

    Note that, we only do statistics for "train" split, because the dev data is not public
    """
    
    ROOT_PATH = "data/bull"
    
    def get_all_questions(self):
        all_data_json = []
        all_data_json.extend(json.load(open(os.path.join(self.ROOT_PATH, "BULL-cn", "train.json"), "r", encoding="utf-8")))
        # all_data_json.extend(json.load(open(os.path.join(self.ROOT_PATH, "BULL-cn", "dev_cn.json"), "r", encoding="utf-8")))
        all_data_json.extend(json.load(open(os.path.join(self.ROOT_PATH, "BULL-en", "train.json"), "r", encoding="utf-8")))
        # all_data_json.extend(json.load(open(os.path.join(self.ROOT_PATH, "BULL-en", "dev_en.json"), "r", encoding="utf-8")))
        return [item["question"] for item in all_data_json]
    
    def get_all_queries(self):
        all_data_json = []
        all_data_json.extend(json.load(open(os.path.join(self.ROOT_PATH, "BULL-cn", "train.json"), "r", encoding="utf-8")))
        # all_data_json.extend(json.load(open(os.path.join(self.ROOT_PATH, "BULL-cn", "dev_cn.json"), "r", encoding="utf-8")))
        all_data_json.extend(json.load(open(os.path.join(self.ROOT_PATH, "BULL-en", "train.json"), "r", encoding="utf-8")))
        # all_data_json.extend(json.load(open(os.path.join(self.ROOT_PATH, "BULL-en", "dev_en.json"), "r", encoding="utf-8")))
        all_queries = [item["sql_query"].strip() for item in all_data_json]
        all_queries = list(set(all_queries))
        return all_queries
    
    def get_all_db_paths(self):
        db_paths = [
            # os.path.join(self.ROOT_PATH, "database_cn", "ccks_fund", "ccks_fund.sqlite"),
            # os.path.join(self.ROOT_PATH, "database_cn", "ccks_macro", "ccks_macro.sqlite"),
            # os.path.join(self.ROOT_PATH, "database_cn", "ccks_stock", "ccks_stock.sqlite"),
            os.path.join(self.ROOT_PATH, "database_en", "ccks_fund", "ccks_fund.sqlite"),
            os.path.join(self.ROOT_PATH, "database_en", "ccks_macro", "ccks_macro.sqlite"),
            os.path.join(self.ROOT_PATH, "database_en", "ccks_stock", "ccks_stock.sqlite")
        ]
        return db_paths
    

class BookSQL(Dataset):
    
    ROOT_PATH = "data/booksql"
    
    def get_all_questions(self):
        all_data_json = []
        all_data_json.extend(json.load(open(os.path.join(self.ROOT_PATH, "train.json"), "r", encoding="utf-8")))
        all_data_json.extend(json.load(open(os.path.join(self.ROOT_PATH, "BookSQL_val.json"), "r", encoding="utf-8")))
        return [item["Query"] for item in all_data_json]
    
    def get_all_queries(self):
        all_data_json = []
        all_data_json.extend(json.load(open(os.path.join(self.ROOT_PATH, "train.json"), "r", encoding="utf-8")))
        all_data_json.extend(json.load(open(os.path.join(self.ROOT_PATH, "BookSQL_val.json"), "r", encoding="utf-8")))
        all_queries = [item["SQL"].strip().replace("\"\"", "'") for item in all_data_json]
        all_queries = list(set(all_queries))
        return all_queries
    
    def get_all_db_paths(self):
        db_paths = [
            os.path.join(self.ROOT_PATH, "accounting.sqlite"),
        ]
        return db_paths
    

class PAUQ(Dataset):
    
    ROOT_PATH = "data/pauq"
    
    def get_all_questions(self):
        all_data_json = []
        all_data_json.extend(json.load(open(os.path.join(self.ROOT_PATH, "pauq_dev.json"), "r", encoding="utf-8")))
        all_data_json.extend(json.load(open(os.path.join(self.ROOT_PATH, "pauq_train.json"), "r", encoding="utf-8")))
        return [item["question"]["ru"] for item in all_data_json]
    
    def get_all_queries(self):
        all_data_json = []
        all_data_json.extend(json.load(open(os.path.join(self.ROOT_PATH, "pauq_dev.json"), "r", encoding="utf-8")))
        all_data_json.extend(json.load(open(os.path.join(self.ROOT_PATH, "pauq_train.json"), "r", encoding="utf-8")))
        all_queries = [item["query"]["ru"].strip() for item in all_data_json]
        all_queries = list(set(all_queries))
        return all_queries
    
    def get_all_db_paths(self):
        db_paths = [os.path.join(self.ROOT_PATH, "merged_database", db_id, f"{db_id}.sqlite") for db_id in os.listdir(os.path.join(self.ROOT_PATH, "merged_database"))]
        return db_paths


class CHASE(Dataset):
    
    ROOT_PATH = "data/chase"
    
    def get_all_questions(self):
        data_json = []
        for item in json.load(open(os.path.join(self.ROOT_PATH, "chase_train.json"), "r", encoding="utf-8")):
            interaction = item["interaction"]
            for turn in interaction:
                data_json.append({
                    "question": turn["utterance"],
                    "query": turn["query"]
                })
        for item in json.load(open(os.path.join(self.ROOT_PATH, "chase_dev.json"), "r", encoding="utf-8")):
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
        for item in json.load(open(os.path.join(self.ROOT_PATH, "chase_train.json"), "r", encoding="utf-8")):
            interaction = item["interaction"]
            for turn in interaction:
                data_json.append({
                    "question": turn["utterance"],
                    "query": turn["query"]
                })
        for item in json.load(open(os.path.join(self.ROOT_PATH, "chase_dev.json"), "r", encoding="utf-8")):
            interaction = item["interaction"]
            for turn in interaction:
                data_json.append({
                    "question": turn["utterance"],
                    "query": turn["query"]
                })
        all_queries = list(set([item["query"].strip() for item in data_json]))
        return all_queries
    
    def get_all_db_paths(self):
        db_paths = [os.path.join(self.ROOT_PATH, "database", db_file) for db_file in os.listdir(os.path.join(self.ROOT_PATH, "database"))]
        return db_paths


class DuSQL(Dataset):
    
    ROOT_PATH = "data/dusql"
    
    def __init__(self):
        schemas = json.load(open(os.path.join(self.ROOT_PATH, "db_schema.json"), "r", encoding="utf-8"))
        self._total_databases = len(schemas)
        self._total_tables = 0
        total_columns, total_records = 0, 0
        for db in schemas:
            self._total_tables += len(db["table_names"])
            total_columns += (len(db["column_names"]) - 1) # ignore star col
        self._avg_tables_per_db = self._total_tables / self._total_databases
        self._avg_columns_per_table = total_columns / self._total_tables
        
        db_content = json.load(open(os.path.join(self.ROOT_PATH, "db_content.json"), "r", encoding="utf-8"))
        
        for db in db_content:
            for k, v in db["tables"].items():
                total_records += len(v["cell"])
        
        self._avg_records_per_db = total_records / self._total_databases
    
    def get_all_questions(self):
        all_data_json = []
        all_data_json.extend(
            json.load(open(os.path.join(self.ROOT_PATH, "train.json"), "r", encoding="utf-8"))
        )
        all_data_json.extend(
            json.load(open(os.path.join(self.ROOT_PATH, "dev.json"), "r", encoding="utf-8"))
        )
        return [item["question"] for item in all_data_json]
    
    def get_all_queries(self):
        all_data_json = []
        all_data_json.extend(
            json.load(open(os.path.join(self.ROOT_PATH, "train.json"), "r", encoding="utf-8"))
        )
        all_data_json.extend(
            json.load(open(os.path.join(self.ROOT_PATH, "dev.json"), "r", encoding="utf-8"))
        )
        all_queries = [item["query"].strip() for item in all_data_json]
        all_queries = list(set(all_queries))
        return all_queries
    
    def get_all_db_paths(self):
        db_paths = []
        return db_paths


class ViText2SQL(Dataset):
    
    ROOT_PATH = "data/vitext2sql"
    
    def get_all_questions(self):
        data_json = []
        data_json.extend(json.load(open(os.path.join(self.ROOT_PATH, "word-level", "train.json"), "r", encoding="utf-8")))
        data_json.extend(json.load(open(os.path.join(self.ROOT_PATH, "word-level", "dev.json"), "r", encoding="utf-8")))
        data_json.extend(json.load(open(os.path.join(self.ROOT_PATH, "word-level", "test.json"), "r", encoding="utf-8")))
        all_questions = [item["question"] for item in data_json]
        return all_questions
    
    def get_all_queries(self):
        data_json = []
        data_json.extend(json.load(open(os.path.join(self.ROOT_PATH, "word-level", "train.json"), "r", encoding="utf-8")))
        data_json.extend(json.load(open(os.path.join(self.ROOT_PATH, "word-level", "dev.json"), "r", encoding="utf-8")))
        data_json.extend(json.load(open(os.path.join(self.ROOT_PATH, "word-level", "test.json"), "r", encoding="utf-8")))
        all_queries = list(set([item["query"].strip() for item in data_json]))
        return all_queries
    
    def get_all_db_paths(self):
        db_paths = [os.path.join("data/spider", "database", db_id, f"{db_id}.sqlite") for db_id in os.listdir(os.path.join("data/spider", "database"))]
        return db_paths


class MIMICSQL(Dataset):
    
    ROOT_PATH = "data/mimicsql"
    
    def __init__(self):
        self._total_databases = -1
        self._total_tables = -1
        total_columns, total_records = 0, 0
        self._avg_tables_per_db = self._total_tables / self._total_databases
        self._avg_columns_per_table = total_columns / self._total_tables
        self._avg_records_per_db = total_records / self._total_databases
    
    def get_all_questions(self):
        all_data_json = []
        with open(os.path.join(self.ROOT_PATH, "mimicsql_template", "train.json"), "r", encoding="utf-8") as f:
            for line in f.readlines():
                all_data_json.append(json.loads(line))
        with open(os.path.join(self.ROOT_PATH, "mimicsql_template", "test.json"), "r", encoding="utf-8") as f:
            for line in f.readlines():
                all_data_json.append(json.loads(line))
        with open(os.path.join(self.ROOT_PATH, "mimicsql_template", "dev.json"), "r", encoding="utf-8") as f:
            for line in f.readlines():
                all_data_json.append(json.loads(line))
        with open(os.path.join(self.ROOT_PATH, "mimicsql_natural_v2", "train.json"), "r", encoding="utf-8") as f:
            for line in f.readlines():
                all_data_json.append(json.loads(line))
        with open(os.path.join(self.ROOT_PATH, "mimicsql_natural_v2", "test.json"), "r", encoding="utf-8") as f:
            for line in f.readlines():
                all_data_json.append(json.loads(line))
        with open(os.path.join(self.ROOT_PATH, "mimicsql_natural_v2", "dev.json"), "r", encoding="utf-8") as f:
            for line in f.readlines():
                all_data_json.append(json.loads(line))
        return [item["question_refine"] for item in all_data_json]
    
    def get_all_queries(self):
        all_data_json = []
        with open(os.path.join(self.ROOT_PATH, "mimicsql_template", "train.json"), "r", encoding="utf-8") as f:
            for line in f.readlines():
                all_data_json.append(json.loads(line))
        with open(os.path.join(self.ROOT_PATH, "mimicsql_template", "test.json"), "r", encoding="utf-8") as f:
            for line in f.readlines():
                all_data_json.append(json.loads(line))
        with open(os.path.join(self.ROOT_PATH, "mimicsql_template", "dev.json"), "r", encoding="utf-8") as f:
            for line in f.readlines():
                all_data_json.append(json.loads(line))
        with open(os.path.join(self.ROOT_PATH, "mimicsql_natural_v2", "train.json"), "r", encoding="utf-8") as f:
            for line in f.readlines():
                all_data_json.append(json.loads(line))
        with open(os.path.join(self.ROOT_PATH, "mimicsql_natural_v2", "test.json"), "r", encoding="utf-8") as f:
            for line in f.readlines():
                all_data_json.append(json.loads(line))
        with open(os.path.join(self.ROOT_PATH, "mimicsql_natural_v2", "dev.json"), "r", encoding="utf-8") as f:
            for line in f.readlines():
                all_data_json.append(json.loads(line))
        all_queries = [item["sql"].strip() for item in all_data_json]
        all_queries = list(set(all_queries))
        return all_queries
    
    def get_all_db_paths(self):
        db_paths = []
        return db_paths
    
    
class PortugueseSpider(Dataset):
    ROOT_PATH = "data/spider"
    
    def get_all_questions(self):
        data_json = []
        data_json.extend(json.load(open(os.path.join(self.ROOT_PATH, "train_spider.json"), "r", encoding="utf-8")))
        data_json.extend(json.load(open(os.path.join(self.ROOT_PATH, "train_others.json"), "r", encoding="utf-8")))
        data_json.extend(json.load(open(os.path.join(self.ROOT_PATH, "dev.json"), "r", encoding="utf-8")))
        all_questions = [item["question"] for item in data_json]
        return all_questions
    
    def get_all_queries(self):
        data_json = []
        data_json.extend(json.load(open(os.path.join(self.ROOT_PATH, "train_spider.json"), "r", encoding="utf-8")))
        data_json.extend(json.load(open(os.path.join(self.ROOT_PATH, "train_others.json"), "r", encoding="utf-8")))
        data_json.extend(json.load(open(os.path.join(self.ROOT_PATH, "dev.json"), "r", encoding="utf-8")))
        all_queries = list(set([item["query"].strip() for item in data_json]))
        return all_queries
    
    def get_all_db_paths(self):
        db_paths = [os.path.join(self.ROOT_PATH, "database", db_id, f"{db_id}.sqlite") for db_id in os.listdir(os.path.join(self.ROOT_PATH, "database"))]
        return db_paths
    
    
if __name__ == "__main__":
    dataset = PortugueseSpider()
    print(len(dataset.get_all_questions()))
    print(len(dataset.get_all_queries()))
    print(len(dataset.get_all_db_paths()))
