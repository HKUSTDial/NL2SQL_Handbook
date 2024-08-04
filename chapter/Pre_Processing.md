## Pre-Processing
Pre-processing serves as a enhancement to model’s inputs in the NL2SQL parsing process. Although not strictly necessary, pre-processing significantly contributes to the refinement of
NL2SQL parsing.
### Schema linking：
#### 🎓Basic concept:
The purpose of the schema linking is to identify the tables and columns related to the given NL query. 
It ensures the accurate mapping and processing of key information within the limited input, thereby improving the performance of the NL2SQL task.
In the LLMs era, schema linking has become increasingly crucial due to the input length limit of LLMs. 
#### 📚Representative papers：
---
+ `Paper` [RESDSQL: Decoupling Schema Linking and Skeleton Parsing for Text-to-SQL](https://arxiv.org/abs/2302.05965) 
+ `Describe` This paper proposes a ranking-enhanced encoding framework for schema linking. An additional cross-encoder is trained to classify tables and columns based on the input query. This framework ranks and filters them according to classification probabilities, resulting in a ranked sequence of schema items.
---
### DB content Retrival

### Additional Information Acquisitio