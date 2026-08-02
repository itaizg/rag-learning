# Tier 10 — Classic ML ✅

The classic-ML substrate underneath the LLM stack: the folk wisdom, optimizers, tree
ensembles, tooling, interpretability, and distributed-data ideas that interviews assume and
tabular problems still demand. Built from 8 foundational papers (2 more from the same batch —
*Attention Is All You Need* and *BERT* — are transformer papers already covered in notebooks
04/05/05b and are handled as cross-links there).

Runs **fully offline** — sklearn datasets only, no API keys.

| # | Notebook | Priority | Source paper(s) |
|---|---|:---:|---|
| 37 | [ML Foundations — the Folk Wisdom](37_ml_foundations_the_folk_wisdom.ipynb) | 🔴 | Domingos 2012, *A Few Useful Things to Know About ML* |
| 38 | [Optimization: Backprop Tricks → Adam](38_optimization_from_backprop_tricks_to_adam.ipynb) | 🔴 | LeCun et al. 1998, *Efficient BackProp*; Kingma & Ba 2014, *Adam* |
| 39 | [Trees, Forests & Boosting](39_trees_forests_and_boosting.ipynb) | 🔴 | Breiman 2001, *Random Forests*; Chen & Guestrin 2016, *XGBoost* |
| 40 | [The scikit-learn Way](40_the_sklearn_way.ipynb) | 🟡 | Pedregosa et al. 2011, *Scikit-learn* |
| 41 | [Model Interpretability & SHAP](41_model_interpretability_shap.ipynb) | 🟡 | Lundberg & Lee 2017, *A Unified Approach to Interpreting Model Predictions* |
| 42 | [Spark & Distributed Data](42_spark_and_distributed_data.ipynb) | 🟢 | Zaharia et al. 2010, *Spark: Cluster Computing with Working Sets* |

Full build plan and build-time notes: `~/.claude/plans/classic-ml-section.md`.
