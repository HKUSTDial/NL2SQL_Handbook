## NL2SQL Translation Methods

### Encoding Strategy
#### 🎓Basic concept:
#### 📚Representative papers：

### Decoding Strategy
#### 🎓Basic concept:
#### 📚Representative papers：

### Task-specific Prompt Strategy
#### 🎓Basic concept:
In the era of LLMs, prompt engineering can harness the capabilities of LLMs and has been widely adopted in natural language processing, with various frameworks developed for specific tasks. In the NL2SQL field, task-specific prompt strategy refers to the tailored prompt engineering techniques used in the NL2SQL translation process. These strategies instruct the LLMs to optimize the SQL query generation process according to task-specific rules, improving the accuracy of translating complex semantic NL query into the corresponding SQL query.
#### 📚Representative papers：
+ `Paper` [CHESS: Contextual Harnessing for Efficient SQL Synthesis](https://arxiv.org/pdf/2405.16755)
+ `Describe` CHESS transforms NL into SQL statements using a streamlined pipeline that relies on LLMs and CoT. This process comprises entity and context retrieval, schema selection, SQL generation, and revision.
+ `Paper` [DTS-SQL: Decomposed Text-to-SQL with Small Large Language Models](https://arxiv.org/pdf/2402.01117)
+ `Describe` DTS-SQL splits the work task into two subtasks, schema linking, and generation, to close the performance gap between open-source LLMs and closed-source LLMs.
+ `Paper` [Towards Generalizable and Robust Text-to-SQL Parsing](https://arxiv.org/pdf/2210.12674)
+ `Describe` The TKK framework divides the initial NL2SQL parsing tasks into various small individual subtasks, with each corresponding to the mapping of the NL query to one or more clauses of the SQL query.  
+ `Paper` [MAC-SQL: A Multi-Agent Collaborative Framework for Text-to-SQL](https://arxiv.org/abs/2312.11242) 
+ `Describe` MAC-SQL incorporates a Decomposer agent designed to break down the user's original problem into several subproblems. This decomposition process aims to lessen the complexity of the origin question, enabling the generation of simpler SQL queries to solve each individual subproblem.
+ `Paper` [DIN-SQL: Decomposed In-Context Learning of Text-to-SQL with Self-Correction](https://arxiv.org/pdf/2304.11015v3.pdf)
+ `Describe` DIN-SQL employs a sophisticated categorization module for decomposition. It classify queries into distinct complexity groups: EASY, NON-NESTED, and NESTED, with the reference of NL and database schema.This module is fundamental for the subsequent decomposition process, which meticulously dissects complex queries into simpler sub-problems. By strategically identifying and separating schema linking, join conditions, and nested structures, the module facilitates a structured generation of SQL queries and amplifies the accuracy of translating complex the NL query into executable SQL.

### Intermediate Representation for NL2SQL Translation
#### 🎓Basic concept:
As mentioned before, the NL2SQL task is challenging due to the complexity and ambiguity of NL queries, as well as the formal and structured nature of SQL. Thus, researchers try to simplify this process by designing a *grammar-free* intermediate representation compared to SQL as the bridge between the ''free-form'' NL query and the ''constrained and formal'' SQL query.Roughly speaking, an intermediate representation (IR) is a structured yet flexible grammar that captures the essential components and relationships of an NL query without the strict syntax rules of SQL. 
#### 📚Representative papers：
+ `Paper` [Schema-free SQL](https://dl.acm.org/doi/pdf/10.1145/2588555.2588571)
+ `Describe` In the research of Schema-free SQL, the original question can be transformed into an intermediate representation even in the absence of user knowledge about schema information.
+ `Paper` [SyntaxSQLNet: Syntax Tree Networks for Complex and Cross-DomainText-to-SQL Task](https://arxiv.org/pdf/1810.05237)
+ `Describe` SyntaxSQLNet removes portions of the FROM and JOIN clauses in the syntax language.
+ `Paper` [SemQL: a semantic query language for multidatabase systems](https://dl.acm.org/doi/pdf/10.1145/319950.320011)
+ `Describe` SemQL removes the FROM, JOIN, ON and GROUP BY clauses and combines WHERE and HAVING conditions.
+ `Paper` [Editing-Based SQL Query Generation for Cross-Domain Context-Dependent Questions](https://arxiv.org/pdf/1909.00786)
+ `Describe` EditSQL adds WHERE and HAVING conditions but retains the GROUP BY clause.
+ `Paper` [Natural SQL: Making SQL Easier to Infer from Natural Language Specifications](https://arxiv.org/pdf/2109.05153.pdf)
+ `Describe` Natural SQL (NatSQL) is a widely recognized SQL-like syntax language that eliminates SQL statement operators, keywords, set operators, and other elements seldom found in user problem descriptions. It enhances schema linking by minimizing the necessary number of schema items.
+ `Paper` [Semantic Decomposition of Question and SQL for Text-to-SQL Parsing](https://arxiv.org/pdf/2310.13575)
+ `Describe` The Query Plan Language (QPL) leverages the problem decomposition strategy to improve the parsing of intricate SQL queries. By breaking down a SQL query into modularized sub-queries, the complexity of the original query is reduced. This approach mitigates parsing difficulties associated with complex problems and cross-domain complex queries.
+ `Paper` [Weakly Supervised Text-to-SQL Parsing through Question Decomposition](https://arxiv.org/pdf/2112.06311)
+ `Describe` Question Decomposition Meaning Representation (QDMR) decomposes the original question into a number of atomic questions. Each atomic question serves as an intermediate representation of the original question and can be translated into a set of small-scale formal operations involving tasks such as selecting entities, retrieving attributes, or aggregating information. 
+ `Paper` [Few-shot Text-to-SQL Translation using Structure and Content Prompt Learning](https://dl.acm.org/doi/pdf/10.1145/3589292)
+ `Describe` The SC-prompt utilizes a two-stage divide and conquer method for NL2SQL parsing. During the initial phase, it instructs PLM to generate specific SQL structures, such as query commands and operators, while also supplying placeholders for any missing identifiers. In the subsequent phase, it directs the PLM to generate SQL structures containing actual values to fill the previously provided placeholders.
+ `Paper` [CatSQL: Towards Real World Natural Language to SQL Applications](https://dl.acm.org/doi/pdf/10.14778/3583140.3583165)
+ `Describe` CatSQL constructs a template sketch with slots serving as initial placeholders. Different from the former, this sketch is much more general. Its base model can focus on the parsing of user queries to fill these placeholders, consequently decreasing the computational resource cost. Furthermore, it implements a novel semantic correction algorithm to assess the semantic accuracy of the resulting SQL queries and rectify any semantic issues detected in the generated queries. 
+ `Paper` [Interleaving Pre-Trained Language Models and Large Language Models for Zero-Shot NL2SQL Generation](https://arxiv.org/pdf/2306.08891)
+ `Describe` ZeroNL2SQL integrates the schema alignment capabilities of PLM with the complex reasoning capabilities of LLMs. Initially, it utilizes PLM to produce SQL sketches for achieving schema alignment and subsequently employs LLMs to execute complex content reasoning for populating missing information. Additionally, it also proposes a predicate calibration method for guiding the design of language models for SQL sketches based on database instances and selecting the optimal SQL query.
+ `Paper` [Before Generation, Align it! A Novel and Effective Strategy for Mitigating Hallucinations in Text-to-SQL Generation](https://arxiv.org/pdf/2405.15307)
+ `Describe` TA-SQL combines pandas code and symbolic representation to generate an abstract sketch of SQL and uses this sketch to align with schema information in subsequent modules to generate complete SQL.
+ `Paper` [RESDSQL: Decoupling Schema Linking and Skeleton Parsing for Text-to-SQL](https://arxiv.org/pdf/2302.05965v3.pdf)
+ `Describe` RESDSQL introduces a rank-enhanced encoding and skeleton-aware decoding framework, which separates schema linking from skeleton parsing.  During the decoding generation phase, its decoder initially produces the SQL skeleton and then generates the actual SQL query. This approach implicitly constrains the SQL parsing and governs the quality of generation. When combined with NatSQL, RESDSQL demonstrates the ability to further enhance the quality of SQL query generation.
