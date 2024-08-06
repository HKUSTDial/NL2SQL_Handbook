# Evaluation

## Evaluation Metric

- **Execution Accuracy (EX)**
  - **Description:** Execution Accuracy (EX) evaluates the performance of the NL2SQL system by comparing whether the execution result sets of the ground-truth SQL queries and the predicted SQL queries are identical.
  - [Paper Link](https://arxiv.org/abs/1809.08887)
- **String-Match Accuracy (SM)**
  - **Description:** String-Match Accuracy (SM) (also called Logical Form Accuracy) simply compares whether the ground-truth SQL query and the predicted SQL query are identical as strings. It may penalize SQL queries that produce the correct execution result sets but do not have the exact string match with the ground-truth SQL queries.
  - [Paper Link](https://arxiv.org/abs/1709.00103)
- **Component-Match Accuracy (CM)**
  - **Description:** Component-Match Accuracy (CM) evaluates the detailed performance of the NL2SQL system by measuring the exact matching of different SQL components such as `SELECT`, `WHERE` and others between the ground-truth SQL query and the predicted SQL query.
  - [Paper Link](https://arxiv.org/abs/1809.08887)
- **Exact-Match Accuracy (EM)**
  - **Description:** Exact-Match Accuracy is based on the Component-Match Accuracy (CM) and measures whether all SQL components of the predicted SQL query match the ground-truth SQL query.
  - [Paper Link](https://arxiv.org/abs/1809.08887)
- **Valid Efficiency Score (VES)**
  - **Description:** Valid Efficiency Score (VES) measures the execution efficiency of valid SQL queries. It considers both the accuracy and efficiency of SQL execution.
  - [Paper Link](https://arxiv.org/pdf/2305.03111)
- **Query Variance Testing (QVT)**
  - **Description:** Query Variance Testing (QVT) measures the robustness and flexibility of the NL2SQL system in handling variations in NL questions.
  - [Paper Link](https://arxiv.org/abs/2406.01265)

## Evaluation Toolkit

- **NL2SQL360**
  - **Description:** **NL2SQL360** is a testbed for fine-grained evaluation of NL2SQL solutions. The testbed integrates existing NL2SQL benchmarks, a repository of NL2SQL models, and various evaluation metrics, which aims to provide an intuitive and user-friendly platform to enable both standard and customized performance evaluations. Users can utilize **NL2SQL360** to assess different NL2SQL methods against established benchmarks or tailor their evaluations based on specific criteria. This flexibility allows for testing solutions in specific data domains or analyzing performance on different characteristics of SQL queries.
  - [Paper Link](https://arxiv.org/abs/2406.01265)
  - [Repository Link](https://github.com/HKUSTDial/NL2SQL360)
- **MT-TEQL**
  - **Description:** **MT-TEQL** is unified framework for evaluating the performance of NL2SQL systems in handling real-world variations in NL questions and database schemas. It is based on a meta-morphic testing approach, implementing semantic-preserving transformations of NL questions and database schemas to automatically generate their variants without manual efforts.
  - [Paper Link](https://www.vldb.org/pvldb/vol15/p569-ma.pdf)
  - [Repository Link](https://github.com/MTTeql/MT-Teql)