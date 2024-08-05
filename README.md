# <h1 align="center">NL2SQL Handbook</h1>

### <h3 align="center">Where are we, and where are we going?</h3>

## 🧭Introduction 
Translating users' natural language queries (NL) into sql queries can significantly reduce barriers to accessing relational databases and support various commercial applications. The performance of NL2SQL has been greatly improved with the emergence of language models (LMs). In this context, it is crucial to assess our current position, determine the NL2SQL solutions that should be adopted for specific scenarios by practitioners, and identify the research topics that researchers should explore next.

## 📈NL2SQL Lifecycle
<p align="center">
<img width="600" src="./assets/nl2sql_lifecycle.svg"/>
</p>

+ Model: NL2SQL translation techniques that tackle not only NL ambiguity and under-specification, but also properly map NL with database schema and instances;

+ Data: From the collection of training data, data synthesis due to training data scarcity, to NL2SQL benchmarks;

+ Evaluation: Evaluating NL2SQL methods from multiple angles using different metrics and granularities;

+ Error Analysis: analyzing NL2SQL errors to find the root cause and guiding NL2SQL models to evolve.

## 🤔Where Are We
We categorize the challenges of NL2SQL into five levels and defined each level's specific challenges. The first three levels focus on challenges that have been addressed or are still being tackled, affirming the progressive development of NL2SQL. The fourth level symbolizes the challenges we aim to resolve in the stage of LLMs. Finally, the fifth level represents our aspirations for the ultimate NL2SQL system.

We describe the evolution of NL2SQL solutions from the perspective of language models, categorizing it into four stages.
For each stage of NL2SQL, we analyze the changes in target users and the extent to which challenges are addressed.
<p align="center">
<img width="600" src="./assets/NL2SQL_Evolution.png"/>
</p>


## 🧩Module-based NL2SQL Method
We summarize the key modules of NL2SQL solutions
utilizing language model. 
+ **Pre-processing** serves as a enhancement to model’s inputs in the NL2SQL parsing process.
+ **NL2SQL translation methods** constitute the core of the
NL2SQL solution, responsible for converting input natural
language queries into SQL queries.
+ **Post-processing** is a crucial step to refine the generated SQL queries, ensuring they meet user expectations more accurately.
<p align="center">
<img width="600" src="./assets/Model_Module_Overview.png"/>
</p>

## 🗺️Where Are We Going

* 🎯Sovle Open NL2SQL Problem
* 🎯Develop Cost-effective NL2SQL Methods
* 🎯Make NL2SQL Solutions Trustworthy
* 🎯NL2SQL with Ambiguous and Unspecified NL Queries
* 🎯Adaptive Training Data Synthesis

## 📰News for NL2SQL
💥Latest paper list:
* CodeS: Towards Building Open-source Language Models for Text-to-SQL. 
[<img src="https://img.shields.io/badge/Paper Link-grey">](https://arxiv.org/abs/2402.16347) <img src="https://img.shields.io/badge/SIGMOD'2024-red">
* FinSQL: Model-Agnostic LLMs-based Text-to-SQL Framework for Financial Analysis. 
[<img src="https://img.shields.io/badge/Paper Link-grey">](https://arxiv.org/abs/2401.10506) <img src="https://img.shields.io/badge/SIGMOD'2024-red">
* The Dawn of Natural Language to SQL: Are We Fully Ready?
[<img src="https://img.shields.io/badge/Paper Link-grey">](https://arxiv.org/abs/2406.01265) <img src="https://img.shields.io/badge/VLDB'2024-blue">
* Text-to-SQL Empowered by Large Language Models: A Benchmark Evaluation. 
[<img src="https://img.shields.io/badge/Paper Link-grey">](https://arxiv.org/abs/2308.15363) <img src="https://img.shields.io/badge/VLDB'2024-blue">
* Interleaving Pre-Trained Language Models and Large Language
Models for Zero-Shot NL2SQL Generation. 
[<img src="https://img.shields.io/badge/Paper Link-grey">](https://arxiv.org/abs/2306.08891) <img src="https://img.shields.io/badge/VLDB'2024-blue">
* PURPLE: Making a Large Language Model a Better SQL Writer. 
[<img src="https://img.shields.io/badge/Paper Link-grey">](https://arxiv.org/abs/2403.20014) <img src="https://img.shields.io/badge/ICDE'2024-green">
* METASQL: A Generate-then-Rank Framework for Natural Language to SQL Translation. 
[<img src="https://img.shields.io/badge/Paper Link-grey">](https://arxiv.org/abs/2402.17144) <img src="https://img.shields.io/badge/ICDE'2024-green">
* DIN-SQL: Decomposed In-Context Learning of Text-to-SQL with Self-Correction. 
[<img src="https://img.shields.io/badge/Paper Link-grey">](https://arxiv.org/abs/2304.11015) <img src="https://img.shields.io/badge/NeurIPS'2023-yellow">
* ACT-SQL: In-Context Learning for Text-to-SQL with Automatically-Generated Chain-of-Thought
[<img src="https://img.shields.io/badge/Paper Link-grey">](https://arxiv.org/abs/2310.17342) <img src="https://img.shields.io/badge/EMNLP'2023-orange">
* RESDSQL: Decoupling Schema Linking and Skeleton Parsing for Text-to-SQL. 
[<img src="https://img.shields.io/badge/Paper Link-grey">](https://arxiv.org/abs/2302.05965) <img src="https://img.shields.io/badge/AAAI'2023-cyan">


## 📖Catalog for Survey
You can get more information from our subsection, we introduce representative papers on related concepts:
* [Pre-Processing](chapter/Pre_Processing.md)
* [NL2SQL translation methods](chapter/Translation_method.md)
* [Post-Processing](chapter/Post_Processing.md)
* [Benchamrk](chapter/Benchmark.md)
* [Evaluation](chapter/Evaluation.md)
* [Error Analysis](chapter/Error_Analysis.md)

## 💾Material for Novice
Practical Materialmation collected for Novice:





