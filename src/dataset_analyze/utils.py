import os
import sqlite3
from sql_parser import SQLParser

ROUND_NUM = 2


def generate_report_database_complexity(db_paths: list, is_wikisql=False):
    total_databases = len(db_paths)
    total_tables = 0
    total_columns = 0
    total_records = 0
    
    for db_path in db_paths:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        num_tables = len(tables)
        total_tables += num_tables
    
        for table in tables:
            table_name = table[0]
            
            cursor.execute(f"PRAGMA table_info(`{table_name}`);")
            columns = cursor.fetchall()
            num_columns = len(columns)
            total_columns += num_columns
            
            cursor.execute(f"SELECT COUNT(*) FROM `{table_name}`;")
            num_records = cursor.fetchone()[0]
            total_records += num_records
    
    conn.close()
    
    if is_wikisql:
        total_databases = total_tables
    
    avg_tables_per_db = round(total_tables / total_databases, ROUND_NUM)
    avg_columns_per_table = round(total_columns / total_tables, ROUND_NUM)
    avg_records_per_db = round(total_records / total_databases, ROUND_NUM)
    
    report = {
        "Total Databases": total_databases,
        "Total Tables": total_tables,
        "Average Tables per Database": avg_tables_per_db,
        "Average Columns per Table": avg_columns_per_table,
        "Average Records per Database": avg_records_per_db
    }
    
    return report
    

def generate_report_query_complexity(queries: list[str]):
    tables_per_query = []
    selects_per_query = []
    aggs_per_query = []
    scalar_funcs_per_query = []
    math_computes_per_query = []
    
    for query in queries:
        sql_parser = SQLParser(query)
        tables_per_query.append(sql_parser.count_table)
        selects_per_query.append(sql_parser.count_select)
        aggs_per_query.append(sql_parser.count_aggregation)
        scalar_funcs_per_query.append(sql_parser.count_scalar_function)
        math_computes_per_query.append(sql_parser.count_math_compute)
    
    avg_tables_per_query = round(sum(tables_per_query) / len(tables_per_query), ROUND_NUM)
    avg_selects_per_query = round(sum(selects_per_query) / len(selects_per_query), ROUND_NUM)
    avg_aggs_per_query = round(sum(aggs_per_query) / len(aggs_per_query), ROUND_NUM)
    avg_scalar_funcs_per_query = round(sum(scalar_funcs_per_query) / len(scalar_funcs_per_query), ROUND_NUM)
    avg_math_computes_per_query = round(sum(math_computes_per_query) / len(math_computes_per_query), 2)
    
    report = {
        "Average Tables per Query": avg_tables_per_query,
        "Average Selects per Query": avg_selects_per_query,
        "Average Aggs per Query": avg_aggs_per_query,
        "Average Scalar Functions per Query": avg_scalar_funcs_per_query,
        "Average Math Computations per Query": avg_math_computes_per_query
    }
    
    return report