## Pre-Processing
Pre-processing serves as a enhancement to model’s inputs in the NL2SQL parsing process. Although not strictly necessary, pre-processing significantly contributes to the refinement of
NL2SQL parsing.
### Schema linking：
#### 🎓Basic concept:
The purpose of the schema linking is to identify the tables and columns related to the given NL query. 
It ensures the accurate mapping and processing of key information within the limited input, thereby improving the performance of the NL2SQL task.
In the LLMs era, schema linking has become increasingly crucial due to the input length limit of LLMs. 
#### 📚Representative papers：
+ `Paper` [RESDSQL: Decoupling Schema Linking and Skeleton Parsing for Text-to-SQL](https://arxiv.org/abs/2302.05965) 
+ `Describe` This paper proposes a ranking-enhanced encoding framework for schema linking. An additional cross-encoder is trained to classify tables and columns based on the input query. This framework ranks and filters them according to classification probabilities, resulting in a ranked sequence of schema items.
---
### DB content Retrival
#### 🎓Basic concept:
The purpose of database content retrieval is to efficiently retrieve cell values through textual searching algorithms and database indexing. Unlike schema linking, which focuses on finding relevant tables and column based on the NL query, database content retrieval emphasizes efficiently retrieving cell values. Given the large scale of databases, retrieving cell values from them is resource-intensive and poses potential risks of exposing sensitive data. Therefore, it is crucial to implement appropriate strategies for the scenario requirement. 
#### 📚Representative papers：
+ `Paper` [Bridging Textual and Tabular Data for Cross-Domain Text-to-SQL Semantic Parsing](https://arxiv.org/pdf/2012.12627) 
+ `Describe` BRIDGE designs an anchor text matching to extract cell values mentioned in the NL automatically. It uses a heuristic method to calculate the maximum sequence match between the problem and the cell values to determine the matching boundary. When the cell values are substrings of words in the query, the heuristic can exclude those string matches. The matching threshold is then adjusted by making coarse accuracy measurements.
+ `Paper` [ValueNet: A Natural Language-to-SQL System that Learns from Database Information](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=9458778&casa_token=UWDqhoU2Wb0AAAAA:QetXS1rDu1qXExZJa6cKotIE5YXzHG-YwWyRNuhdaqwaRnB-Wj_S8MuypI--RIcF9oHb5a7pz1IR8h0&tag=1)
+ `Describe` ValueNet implements three methods for generating candidate cell values based on n-grams method, string similarity and heuristic selection.
+ `Paper` [TaBERT: Pretraining for Joint Understanding of Textual and Tabular Data](https://arxiv.org/pdf/2005.08314)
+ `Describe` TABERT utilizes a method called database content snapshots to encode the relevant subset of database content corresponding to the NL query. It uses an attention mechanism to manage information between cell value representations across different rows.
+ `Paper` [Towards Complex Text-to-SQL in Cross-Domain Database with Intermediate Representation](https://arxiv.org/pdf/1905.08205)
+ `Describe` IRNet employs the knowledge graph ConceptNet to recognize cell value links and search cell value candidates in the knowledge graph. When a result exactly or partially matches a cell value, the column is assigned a type of value exact match or partial match, respectively.
+ `Paper` [RAT-SQL: Relation-Aware Schema Encoding and Linking for Text-to-SQL Parsers](https://arxiv.org/pdf/1911.04942)
+ `Describe` RAT-SQL further improves structural reasoning capabilities by modeling the relationship between cell values and the NL query. Specifically, it identifies the column-value relationship, meaning that the value in the question is part of the candidate cell value of the column. 
+ `Paper` [CHESS: Contextual Harnessing for Efficient SQL Synthesis](https://arxiv.org/pdf/2405.16755)
+ `Describe` CHESS utilizes a Locality-sensitive Hashing algorithm for approximate nearest neighbor searches. It indexes unique cell values to quickly identify the top similar values related to the NL query. This approach significantly speeds up the process of computing the edit distance and semantic embedding between the NL query and cell values.
+ `Paper` [CodeS: Towards Building Open-source Language Models for Text-to-SQL](https://dl.acm.org/doi/abs/10.1145/3654930)
+ `Describe` CodeS introduces a coarse-to-fine cell value matching approach. It leverages indexes for a coarse-grained initial search, followed by a fine-grained matching process. First, it builds the index for all values using BM25. The index identifies candidate values relevant to NL. The Longest Common Substring algorithm is then used to calculate the matching degree between NL and the candidate values to find the most relevant cell values.
---
### Additional Information Acquisition
#### 🎓Basic concept:
Additional information (e.g. *domain knowledge*) plays an essential role in improving the comprehension capabilities of NL2SQL models for understanding the NL query, performing the schema linking, and benefiting the NL2SQL translation. This information can provide demonstration examples, domain knowledge, formulaic evidence, and format information for the NL2SQL backbone model or specific modules, thereby enhancing the quality of the generated results.
#### 📚Representative papers：
+ `Paper` [DIN-SQL: Decomposed In-Context Learning of Text-to-SQL with Self-Correction](https://arxiv.org/pdf/2304.11015v3.pdf)
+ `Describe` DIN-SQL inserts additional information through few-shot learning across multiple stages of the workflow, such as schema linking, query classification, task decomposition, and self-correction. These stages allow DIN-SQL to effectively tackle various challenges, including the complexity of schema links, identification of multiple table joins, and handling of nested queries.
+ `Paper` [CodeS: Towards Building Open-source Language Models for Text-to-SQL](https://dl.acm.org/doi/abs/10.1145/3654930)
+ `Describe` CodeS utilizes metadata examples of cross-domain databases as the main additional information, including data types and annotation text, which help the model resolve potential ambiguity issues and understand entity relationships. This extracted information is transformed into coherent text and concatenated with the question query to form the final input context.
+ `Paper` [PET-SQL: A Prompt-enhanced Two-stage Text-to-SQL Framework with Cross-consistency](https://arxiv.org/pdf/2403.09732)
+ `Describe` PET-SQL constructs a pool of examples from the training set, which contains question frames and question-SQL pairs. Then, it selects the $k$ examples that are most similar to the target question.  These selected examples are combined with customized prompts as the final input.
+ `Paper` [Text-to-SQL Empowered by Large Language Models: A Benchmark Evaluation](https://arxiv.org/pdf/2308.15363v4.pdf)
+ `Describe` DAIL-SQL intricately designs a two-stage representation algorithm for additional information. It begins by presenting the question and database as SQL statement hints, thereby providing comprehensive database information. Following this, it employs a masking mechanism and similarity calculation to select appropriate examples and systematically organizes tags to enhance the efficiency of the algorithm. 
+ `Paper` [The Dawn of Natural Language to SQL: Are We Fully Ready?](https://arxiv.org/pdf/2308.15363v4.pdf)
+ `Describe` SuperSQL extends the representation algorithm of the DAIL-SQL by integrating similarity-based sample selection with schema linking and database content information, which filters out irrelevant schemas, thereby enhancing the quality of SQL generation.
+ `Paper` [Towards Knowledge-Intensive Text-to-SQL Semantic Parsing with Formulaic Knowledge](https://arxiv.org/pdf/2301.01067)
+ `Describe` REGROUP constructs a formulaic knowledge base encompassing various domains, such as finance, real estate, and transportation.  It leverages a Dense Passage Retriever (DPR) to compute similarity scores for the retrieval results from the formulaic knowledge base.  Subsequently, an Erasing-Then-Awakening (ETA) model is used to integrate the entities in these formulaic knowledge items with the entities in NL and schema. This model filters irrelevant entities below a confidence threshold and maps the remainder to schema elements, thereby grounding knowledge for accurate SQL query generation.
+ `Paper` [Reboost Large Language Model-based Text-to-SQL, Text-to-Python, and Text-to-Function - with Real Applications in Traffic Domain](https://arxiv.org/pdf/2310.18752)
+ `Describe` ReBoost engages with the LLMs model using the Explain-Squeeze Schema Linking mechanism. This mechanism is a two-phase strategy. Initially, it presents a generalized schema to the LLMs to establish a foundational understanding. Subsequently, it employs targeted prompting to elicit detailed associations between query phrases and specific database entities, thereby enhancing accuracy in mapping queries to database structures.without incurring excessive token cost.
+ `Paper` [Selective Demonstrations for Cross-domain Text-to-SQL](https://arxiv.org/pdf/2310.06302)
+ `Describe` ODIS proposes SimSQL method to retrieve additional knowledge from cross-domain databases. This method utilizes the BM25 algorithm to measure the resemblance in SQL keywords and schema tokens.  The top examples from each database are selected as the demonstrations that closely align with target SQL.
---