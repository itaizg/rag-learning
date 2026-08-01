# Tier 10 — Classic ML 🚧 (planned)

The classic-ML substrate underneath the LLM stack: the folk wisdom, optimizers, tree
ensembles, tooling, interpretability, and distributed-data ideas that interviews assume and
tabular problems still demand. Built from 8 foundational papers (2 more from the same batch —
*Attention Is All You Need* and *BERT* — are transformer papers already covered in notebooks
04/05/05b and are handled as cross-links there).

Runs **fully offline** — sklearn datasets only, no API keys.

| # | Notebook (planned) | Priority | Source paper(s) |
|---|---|:---:|---|
| 37 | ML Foundations — the folk wisdom | 🔴 | Domingos 2012, *A Few Useful Things to Know About ML* |
| 38 | Optimization: backprop tricks → Adam | 🔴 | LeCun et al. 1998, *Efficient BackProp*; Kingma & Ba 2014, *Adam* |
| 39 | Trees, forests & boosting | 🔴 | Breiman 2001, *Random Forests*; Chen & Guestrin 2016, *XGBoost* |
| 40 | The scikit-learn way | 🟡 | Pedregosa et al. 2011, *Scikit-learn* |
| 41 | Model interpretability & SHAP | 🟡 | Lundberg & Lee 2017, *A Unified Approach to Interpreting Model Predictions* |
| 42 | Spark & distributed data | 🟢 | Zaharia et al. 2010, *Spark: Cluster Computing with Working Sets* |

Full build plan: `~/.claude/plans/classic-ml-section.md`.
