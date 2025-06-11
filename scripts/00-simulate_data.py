#### Preamble ####
# Purpose: Simulates response rubric grades for LLM paper
# Author: Evelyn Hughes
# Date: 13 May 2025
# Contact: evelyn.hughes@utoronto.ca
# License: MIT
# Pre-requisites: 
  # - `polars` must be installed (pip install polars)
  # - `numpy` must be installed (pip install numpy)


#### Workspace setup ####
import polars as pl
import numpy as np
np.random.seed(853)

#### Simulate data ####

#constants
MODELS = ["ChatGPT 3.0", "ChatGPT 4.0", "Gemini", "Claude"]
CODE_RUBRIC = ["Replicable", "Tests"]
PAPER_RUBRIC = ["Prose", "References", "Introduction", "Data", "Abstract", "Title", "Figures"]
AGGREGATED_RUBRIC = ["Code", "Paper", "Total"]

# Generate the 
#creating dictionary w/ columns
scores = dict()
scores["Model"] = MODELS
for column in CODE_RUBRIC:
  scores[column] = [0,]*len(MODELS)
for column in PAPER_RUBRIC:
  scores[column] = [0, ]*len(MODELS)

#generating random values for each rubric category, aggregate for total
for i in range(len(MODELS)):
  for category in CODE_RUBRIC:
    score = int(3*np.random.rand())
    scores[category][i] = score
  for category in PAPER_RUBRIC:
    score = int(3*np.random.rand())
    scores[category][i] = score

#saves raw generated data
scores_data = pl.DataFrame(scores)
scores_data.write_csv("data/00-simulated_data/raw_grade.csv")

## Create Analysis Data ##

aggregated_scores = dict()
aggregated_scores["Model"] = MODELS
for column in AGGREGATED_RUBRIC:
  aggregated_scores[column] = [0,]*len(MODELS)

#aggregate code score
for i in range(len(MODELS)):
  code_score = 0
  paper_score = 0
  for category in CODE_RUBRIC:
    code_score += scores[category][i]
  aggregated_scores["Code"][i] = code_score
  for category in PAPER_RUBRIC:
    paper_score += scores[category][i]
  aggregated_scores["Paper"][i] = paper_score
  aggregated_scores["Total"][i] = paper_score + code_score

#saves raw generated data
aggregated_scores = pl.DataFrame(aggregated_scores)
aggregated_scores.write_csv("data/00-simulated_data/aggregated_scores.csv")
  
    

