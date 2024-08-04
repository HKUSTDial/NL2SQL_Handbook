## Benchmarks and Training Data Synthesis

### Representative benchmarks

- **Academic, Advising, ATIS, Geography, Restaurants, Scholar, IMDB, Yelp, etc.**  
  + `Blog` [http://jkk.name/text2sql-data/](http://jkk.name/text2sql-data/) 
  + `Code` [https://github.com/jkkummerfeld/text2sql-data](https://github.com/jkkummerfeld/text2sql-data)
  + `Paper` [Improving Text-to-SQL Evaluation Methodology](https://www.aclweb.org/anthology/P18-1033.pdf), _Finegan-Dollak C, Kummerfeld J K, Zhang L, et al._, ACL 2018  
  + `Describe`
---
- **WikiSQL**  
  + `Code` [https://github.com/salesforce/WikiSQL](https://github.com/salesforce/WikiSQL)
  + `Paper` [Seq2sql: Generating structured queries from natural language using reinforcement learning](https://arxiv.org/pdf/1709.00103.pdf), _Zhong V, Xiong C, Socher R._ , 2017.
  + `Describe` 1. Single Table Singe Column Query 2.Contains simple operation 
---
- **Spider**  
  + `Leaderboard` [https://yale-lily.github.io/spider](https://yale-lily.github.io/spider)
  + `Code` [https://github.com/taoyds/spider](https://github.com/taoyds/spider)
  + `Paper` [Spider: A Large-Scale Human-Labeled Dataset for Complex and Cross-Domain Semantic Parsing and Text-to-SQL Task](https://arxiv.org/pdf/1809.08887.pdf) _Yu T, Zhang R, Yang K, et al._ , EMNLP 2018.
  + `Describe` 1.Cross-domain 2. Multi-table and multi-column query and subquery and more operate
---
- **SParC**
  + `Leaderboard` [https://yale-lily.github.io/sparc](https://yale-lily.github.io/sparc)
  + `Paper` [SParC: Cross-Domain Semantic Parsing in Context](https://arxiv.org/pdf/1906.02285.pdf), _Yu T, Zhang R, Yasunaga M, et al._, ACL 2019.
  + `Describe` Context-dependent and **Multi-turn** version of the Spider task. 
---
- **CoSQL**
  + `Leaderboard` [https://yale-lily.github.io/cosql](https://yale-lily.github.io/cosql)
  + `Paper` [CoSQL: A Conversational Text-to-SQL Challenge Towards Cross-Domain Natural Language Interfaces to Databases](https://arxiv.org/pdf/1909.05378.pdf), _Yu T, Zhang R, Er H Y, et al._, EMNLP-IJCNLP 2019. 
  + `Describe` Cross-domain Conversational, the Dilaogue version of the Spider and SParC tasks. And **Involves clarification of intent** .
---
- **KaggleDBQA**
  + `Leaderboard` [https://paperswithcode.com/sota/text-to-sql-on-kaggledbqa](https://paperswithcode.com/sota/text-to-sql-on-kaggledbqa)
   + `Code` [https://github.com/Chia-Hsuan-Lee/KaggleDBQA](https://github.com/Chia-Hsuan-Lee/KaggleDBQA)
  + `Paper` [KaggleDBQA: Realistic Evaluation of Text-to-SQL Parsers](https://aclanthology.org/2021.acl-long.176.pdf), _Lee, Chia-Hsuan and Polozov, et al._, ACL 2021. 
  + `Describe`  (1)Its databases are pulled from **real-world data sources** and **not normalized**.
(2) Its questions are authored in environments that **mimic natural question** answering.
(3) It also provides database documentation which **contain rich in-domain knowledge**.
---
- **DR.Spider**
  + `Paper` [Dr.Spider: A Diagnostic Evaluation Benchmark towards Text-to-SQL Robustness](https://openreview.net/pdf?id=Wc5bmZZU9cy), _Shuaichen C, Jun W, Mingwen D, et al._, ICLR 2023. 
  + `Code` [https://github.com/awslabs/diagnostic-robustness-text-to-sql?tab=readme-ov-file](https://github.com/awslabs/diagnostic-robustness-text-to-sql?tab=readme-ov-file)
  + `Describe` A diagnostic evaluation benchmark toward the **robustness** of text-to-SQL models which contains 17 perturbation test sets to measure the robustness of models from different angles.
---
- **AmbiQT**
   + `Code` [https://github.com/testzer0/AmbiQT](https://github.com/testzer0/AmbiQT)
  + `Paper` [Benchmarking and Improving Text-to-SQL Generation Under Ambiguity](https://arxiv.org/pdf/2310.13659), _Adithya Bhaskar and Tushar Tomar et al._, EMNLP 2023. 
  + `Describe` A novel benchmark called AmbiQT with over 3000 examples where each text is interpretable as two plausible SQLs due to lexical and/or structural ambiguity.
---
- **BIRD**
  + `Leaderboard` [https://bird-bench.github.io/](https://bird-bench.github.io/)
  + `Paper` [Can LLM Already Serve as A Database Interface? A BIg Bench for Large-Scale Database Grounded Text-to-SQLs](https://arxiv.org/pdf/2305.03111), _Li, Jinyang and Hui, Binyuan, et al._, NeurIPS 2023. 
  + `Describe`  New challenges of **dirty and noisy** database values, **external knowledge** grounding between NL questions and database values, and **SQL efficiency**, particularly in the context of massive databases.
---
- **ScienceBenchmark**
  + `Leaderboard` [https://sciencebenchmark.cloudlab.zhaw.ch/](https://sciencebenchmark.cloudlab.zhaw.ch/)
  + `Code` [https://github.com/yizhang-unifr/nl-ql-data-augmentation](https://github.com/yizhang-unifr/nl-ql-data-augmentation)
  + `Paper` [A Complex Real-World Benchmark for Evaluating Natural Language to SQL Systems ](https://arxiv.org/pdf/2306.04743), _Yi Zhang, Jan Deriu et al._, VLDB 2024. 
  + `Describe` A new complex NL-to-SQL benchmark for three real-world, highly domain-specific databases: Research Policy Making, Astrophysics, and Cancer research. **Focus on specific areas with experts**

### Training Data Synthesis