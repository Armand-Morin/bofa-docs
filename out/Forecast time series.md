# Machine learning (and more) to forecast time series in quantitative

# wealth and investment management QWIM

## Cristian Homescu

## December 2022

```
Abstract
This document provides details for this QWIM project, and it incorporates the following sections
```
- Motivation
- Relevant references
- Suggested project tasks and timelines
- Practical info
    Recommended software tools
    Recommended datasets
- Design and implementation for the project codes
- Potentially useful Python and R packages, codes and frameworks
- Appendices
    Appendices include
- Overviews of investment processes and models in QWIM
- Comparison of investment portfolios using portfolios metrics and benchmark portfolios

## Contents

**1 Motivation for the project 4**
1.1 Empirical asset pricing and risk premia forecasting............................ 4

**2 Relevant references 6**
2.1 Main References............................................... 6
2.1.1 Main references on empirical asset pricing and forecasting of QWIM time series........ 6
2.1.2 Main references on time series forecasting............................. 7
2.2 Comprehensive list of references....................................... 8
2.2.1 Forecasting QWIM time series, empirical asset pricing, and predictability of financial returns 8
2.2.2 Testing procedures for QWIM time series, empirical asset pricing and predictability of financial
returns................................................ 11
2.2.3 Forecasting time series........................................ 12
2.2.4 Forecasting time series using Machine Learning.......................... 13
2.2.5 Testing procedures to evaluate and compare forecasts...................... 15
2.2.6 Combinations of forecasting methods for time series....................... 16
2.2.7 Combination of statistical and machine learning approaches................... 17
2.2.8 Probabilistic forecasting of time series............................... 18
2.2.9 Metrics to assess forecast performance............................... 18
2.2.10 Software implementations and frameworks............................ 19



- 3 Practical details for the project
   - 3.1 Interaction with students
   - 3.2 Data.
   - 3.3 Private GitHub repository for the QWIM project.
   - 3.4 Deliverables.
   - 3.5 (Optional) Article submission to leading journals
- 4 Project tasks and timelines
   - 4.1 Suggested timelines for project tasks
   - 4.2 Literature review.
   - 4.3 Write-up summary of literature review.
   - 4.4 Identification of appropriate Python and/or R packages
   - 4.5 Code design.
   - 4.6 Implementation of coding framework and components
   - 4.7 Interactive visualizer.
   - 4.8 Project report and presentation.
- 5 Design and implementation for the project codes
   - 5.1 Visualize project workflow and coding framework.
   - 5.2 Representative examples of Python libraries with well designed folder structure
- 6 Practical Info
   - 6.1 Recommended software tools
      - 6.1.1 Python
      - 6.1.2 R.
      - 6.1.3 R IDE.
      - 6.1.4 Python IDE.
      - 6.1.5 Bibliography Manager
      - 6.1.6 Document processor
      - 6.1.7 Source control manager
      - 6.1.8 File editor.
      - 6.1.9 Runtime libraries.
   - 6.2 Recommended datasets
- 7 Potentially useful Python and R software implementations: packages, codes and frameworks
   - 7.1 Collections and repositories of resources
   - 7.2 Connection between Python and R codes
   - 7.3 Anomaly detection and data outliers
   - 7.4 Bayesian analysis and modeling.
   - 7.5 Causality, inference and dependencies
   - 7.6 Classification, Motifs, Neighbors, Wavelets, Transforms.
   - 7.7 Clustering.
   - 7.8 Coding utilities and frameworks.
   - 7.9 Computational performance.
   - 7.10 Containers, projects, pipelines and deployment
   - 7.11 Covariances, correlations and volatilities.
   - 7.12 Data analysis and exploration.
   - 7.13 Data augmentation, scenario generation and synthetic time series.
   - 7.14 Data cleaning, preparation and validation
   - 7.15 Data Imputation
   - 7.16 Data regimes, states and changepoints: analysis and modeling.
   - 7.17 Data structures, storage and serialization
   - 7.18 Dates and times
   - 7.19 Dimensionality reduction
   - 7.20 Distances and Similarity.
   - 7.21 ESG and Impact Investing.
   - 7.22 Explainability, Interpretability, Fairness, Data Privacy
   - 7.23 Features for time series.
   - 7.24 Filtering and spectral analysis for time series
   - 7.25 Forecasting time series.
   - 7.26 Graphs and graphical modeling.
   - 7.27 Linear algebra.
   - 7.28 Machine Learning.
   - 7.29 Machine Learning frameworks (includes Automated ML and hyperparameters tuning)
   - 7.30 Network and graph analysis.
   - 7.31 Numerical methods (includes numerical optimization)
   - 7.32 Probabilistic modeling (includes mixture models and Gaussian Processes)
   - 7.33 Reinforcement learning.
   - 7.34 Robust numerical methods.
   - 7.35 Selection of features, variables, models, data splits
   - 7.36 Sensitivity analysis and numerical derivatives
   - 7.37 Statistics and Probability
   - 7.38 Stress testing, rare events, extreme values and scenarios, survival analysis
   - 7.39 Symbolic regression & data-driven model discovery and machine learning
   - 7.40 Testing (numerical, statistical, etc.), comparison and ranking
   - 7.41 Testing software codes
   - 7.42 Time series analysis and modeling
   - 7.43 Text, sentiment and topic analytics (including NLP)
   - 7.44 Uncertainty: analysis and modeling.
   - 7.45 Visualization and reporting
- 8 Codes for QWIM (Quantitative Wealth and Investment Management)
   - 8.1 Collections of resources
   - 8.2 Research studies with code
   - 8.3 Python software implementations.
   - 8.4 R software implementations
- References
- Appendix A: Overviews of investment processes and models in QWIM
- Appendix C: Comparison of investment using portfolios metrics and benchmark portfolios


## 1 Motivation for the project

Over recent decades, machine learning (ML) algorithms have achieved remarkable success in various areas. The
key to their success is the fact that, given a large representative dataset,MLalgorithms can learn to identify
complex non-linear patterns and explore unstructured relationships without hypothesizing them a priori. Thus,
MLalgorithms are not limited by assumptions or pre-defined data generating processes, which allows the data to
speak for itself.
However, the superiority ofMLis not apparent when it comes to typical time series forecasting, where the data
availability is often limited, as shown by results of M4 competition. The strength ofMLalgorithms, and in fact the
requirement for their successful use, is cross-learning, i.e., using many series to train a single model. This is unlike
standard statistical time series algorithms, where a separate model is developed for each series.
Producing probabilistic forecasts for large collections of similar and/or dependent time series is a highly relevant,
yet challenging task in practice. While classical time series models fail to capture complex patterns in the data
and multivariate techniques struggle to scale to large problem sizes, their reliance on strong structural assumptions
makes them data-efficient and allows them to provide estimates of uncertainty. The converse is true for models
based on deep neural networks, which can learn complex patterns and dependencies given enough data. A hybrid
model that incorporates the benefits of both approaches can deliver better results.
Exploiting cross-series information in forecasting is an idea that gets increased attention lately, especially in the
aftermath of the M4 competition. The idea is that instead of developing one model per each time series in the
dataset, a global model is developed by exploiting information from many time series simultaneously.
Time series are often hierarchical. Many forecasting applications require multiple time series to be forecast
simultaneously. These are often hierarchical in nature and often represent sets of time series which can be highly
correlated
Recently, researchers have used the idea of developing global models within a machine learning context. The
winning solution at the M4 forecasting competition uses the global model concept with local parameters as well,
to cater for individual requirements of different series. This can also be done by clustering groups of related time
series. A global model is developed per each cluster.
Performance for time series forecasting has to be assesed through a combination of metrics
It is also argues that it is more practical to compareMLand statistical forecasting from other perspectives:

- global versus local methods
- probabilistic versus point forecasts
- data driven versus model-driven
- ensemble versus single models
- explanatory/interpretable versus predictive

Combinations of forecasting methods appear to have best results for forecasting of time series of similar granularity
as the ones used inQWIM.

### 1.1 Empirical asset pricing and risk premia forecasting

Asset pricing literature has produced hundreds of potential risk factors. Literature mainly builds on linear or
linear-like models, due to simplicity, transparency and computational efficiency. However, this simplicity may miss
important features of returns, such as nonlinearity, clustering or dependency structure
The literature shows soncerns for risk premia estimation: potential omission of factors, measurement error,
nonlinearity, while linear risk factors may still fall short.
Relative to traditional empirical methods in asset pricing, machine learning accommodates a far more expansive
list of potential predictor variables, as well as richer specifications of functional form. Machine learning methods
can be successfully applied to the two canonical problems of empirical asset pricing: predicting returns in the cross
section and time series.
Gu et al. (“Empirical asset pricing via machine learning,” 2020):

- MLimproved performance compared to traditional methods for both cross section and time series stock return
    prediction


- Predictive gains traced to inclusion of nonlinear interactions
- MLmethods agree on a fairly small set of dominant predictive signals

Leung et al. (“The Promises and Pitfalls of Machine Learning for Predicting Cross-Sectional Stock Returns,” 2020):
Despite statistical advantage ofMLmodel predictions, economic gains corresponding are more limited, and largely
dependent on ability to take risk and implement trades efficiently.
The literature has accumulated a staggering list of predictors that various researchers have argued possess fore-
casting power for returns. The number of stock-level predictive characteristics reported in the literature numbers
in the hundreds and macroeconomic predictors of the aggregate market number in the dozens. Additionally, predic-
tors are often close cousins and highly correlated. Traditional prediction methods break down when the predictor
count approaches the observation count or predictors are highly correlated. With an emphasis on variable selection
and dimension reduction techniques, machine learning is well suited for such challenging prediction problems by
reducing degrees of freedom and condensing redundant variation among predictors.
Moreover, there is ambiguity regarding functional forms through which the high-dimensional predictor set enter
into risk premia. Should they enter linearly? If nonlinearities are needed, which form should they take? Must we
consider interactions among predictors? Such questions rapidly proliferate the set of potential model specifications.
Three aspects of machine learning make it well suited for problems of ambiguous functional form. The first is
its diversity. As a suite of dissimilar methods it casts a wide net in its specification search. Second, with methods
ranging from generalized linear models to regression trees and neural networks, machine learning is explicitly
designed to approximate complex nonlinear associations. Third, parameter penalization and conservative model
selection criteria complement the breadth of functional forms spanned by these methods in order to avoid overfit
biases and false discovery.
Moreover, macroeconomic signals seem to substantially improve out-of-sample performance, especially when
non-linear features are incorporated via machine learning.


## 2 Relevant references

### 2.1 Main References

**2.1.1 Main references on empirical asset pricing and forecasting of QWIM time series**

List of references:
Abhyankar and Wu (“Circus Ring to Zoo to Museum: The Fragility of Factors in Characteristic-based Asset
Pricing Models,” 2020)
Baitinger and Flegel (“New Concepts in Financial Forecasting: Network-Based Information, Topological Data
Analysis and their Combination,” 2021)
Baltussen et al. (“Predicting Bond Returns: 70 Years of International Evidence,” 2021)
Bessembinder et al. (“Time Series Variation in the Factor Zoo,” 2022)
Bianchi et al. (“Bond Risk Premiums with Machine Learning,” 2021)
Bielinski and Broby (“Machine Learning Methods in Asset Pricing,” 2021)
Breitung and Knuppel (“How far can we forecast? Statistical tests of the predictive content,” 2021)
Bryzgalova et al. (“Bayesian solutions for the factor zoo: we just ran two quadrillion models,” 2021)
Chatigny et al. (“Neural forecasting at scale,” 2021)
Chen and Zimmermann (“Open Source Cross-Sectional Asset Pricing,” 2021)
Chen et al. (“Deep learning in asset pricing,” 2021)
Chiang et al. (“Modeling the cross-section of stock returns using sensible models in a model pool,” 2021)
Chib et al. (“On Comparing Asset Pricing Models,” 2020)
Cohen et al. (“Visual Time Series Forecasting: An Image-driven Approach,” 2021)
Coqueret and Guida ( _Machine Learning for Factor Investing: R Version_ , 2020)
Czasonis et al. (“Addition by Subtraction: A Better Way to Forecast Factor Returns (and Everything Else),”
2020)
Czasonis et al. (“Relevance,” 2021)
Czasonis et al. (“The Past as Prologue: How to Forecast Presidential Elections,” 2021)
Faria and Verona (“Time-frequency forecast of the equity premium,” 2021)
Feng et al. (“Taming the factor zoo: A test of new factors,” 2020)
Freyberger et al. (“Dissecting Characteristics Nonparametrically,” 2020)
Giovannelli et al. (“Forecasting Stock Returns with Large Dimensional Factor Models,” 2021)
Gospodinov and Robotti (“Common pricing across asset classes: Empirical evidence revisited,” 2021)
Gu et al. (“Autoencoder asset pricing models,” 2021)
Gu et al. (“Empirical asset pricing via machine learning,” 2020)
Hassler and Pohle (“Forecasting under Long Memory,” 2021)
Iworiso and Vrontos (“On the Predictability of the Equity Premium Using Deep Learning Techniques,” 2021)
Kozak et al. (“Shrinking the cross-section,” 2020)
Lettau and Pelger (“Factors That Fit the Time Series and Cross-Section of Stock Returns,” 2020)
Leung et al. (“The Promises and Pitfalls of Machine Learning for Predicting Stock Returns,” 2021)
Meligkotsidou et al. (“Out-of-sample equity premium prediction: a complete subset quantile regression ap-
proach,” 2021)
McMillan (“Forecasting sector stock market returns,” 2021)
McMillan (“Forecasting U.S. stock returns,” 2021)
Messmer and Audrino (“The Lasso and the Factor Zoo - Expected Returns in the Cross-Section,” 2020)
Nietert and Otto (“Empirical asset pricing: economic significance and economic model evaluation,” 2020)
Oh and Patton (“Better the Devil You Know: Improved Forecasts from Imperfect Models,” 2021)
Rapach et al. (“Industry return predictability: A machine learning approach,” 2019)
Rapach and Zhou (“Time-series and Cross-sectional Stock Return Forecasting: New Machine Learning Meth-
ods,” 2020)
Rapach and Zhou (“Asset Pricing: Time-Series Predictability,” 2022)
Reschenhofer et al. (“Evaluation of current research on stock return predictability,” 2020)
Remlinger et al. (“Expert Aggregation for Financial Forecasting,” 2022)
Ruan et al. (“Stock Price Prediction Under Anomalous Circumstances,” 2021)
Smith and Timmermann (“Break Risk,” 2021)


Smith et al. (“Equity Premium Forecasts with an Unknown Number of Structural Breaks,” 2020)
Wang et al. (“The Best of Both Worlds: Forecasting US Equity Market Returns Using a Hybrid Machine
Learning Time Series Approach,” 2021)
Wang et al. (“Forecasting stock returns: A time-dependent weighted least squares approach,” 2021)
Weigand (“Machine learning in empirical asset pricing,” 2019)
Yang et al. (“Why Existing Machine Learning Methods Fails At Extracting the Information of Future Returns
Out of Historical Stock Prices : the Curve-Shape-Feature and Non-Curve-Shape-Feature Modes,” 2021)
Yin (“Equity premium prediction: keep it sophisticatedly simple,” 2021)

**2.1.2 Main references on time series forecasting**

List of references:
Alexander et al. (“Evaluating the Discrimination Ability of Proper Multivariate Scoring Rules,” 2021)
Alexandrov et al. (“GluonTS: Probabilistic and Neural Time Series Modeling in Python,” 2020)
Ansari et al. (“Deep Explicit Duration Switching Models for Time Series,” 2021)
Athanasopoulos and Kourentzes ( _On the evaluation of hierarchical forecasts_ , 2020)
Atiya (“Why does forecast combination work so well?” 2020)
Bandara et al. (“Improving the accuracy of global forecasting models using time series data augmentation,”
2021)
Bandara et al. (“Forecasting across time series databases using recurrent neural networks on groups of similar
series: A clustering approach,” 2020)
Bandara et al. (“Improving the accuracy of global forecasting models using time series data augmentation,”
2021)
Benidis et al. (“Neural forecasting: Introduction and literature overview,” 2020)
Bauer et al. (“Telescope: An Automatic Feature Extraction and Transformation Approach for Time Series
Forecasting on a Level-Playing Field,” 2020)
Botchkarev (“A new typology design of performance metrics to measure errors in machine learning regression
algorithms,” 2019)
Castle et al. (“Forecasting Principles from Experience with Forecasting Competitions,” 2021)
Cerqueira et al. (“Evaluating time series forecasting models: an empirical study on performance estimation
methods,” 2020)
Dama and Sinoquet (“Analysis and modeling to forecast in time series: a systematic review,” 2021)
Faloutsos et al. (“Forecasting Big Time Series: Theory and Practice,” 2019)
Fosten and Gutknecht (“Horizon confidence sets,” 2021)
Gastinger et al. (“A study on Ensemble Learning for Time Series Forecasting and the need for Meta-Learning,”
2021)
Godahewa et al. (“Ensembles of localised models for time series forecasting,” 2021)
Grazzi et al. (“Meta-Forecasting by combining Global Deep Representations with Local Adaptation,” 2021)
Hannadige et al. (“Forecasting a Nonstationary Time Series Using a Mixture of Stationary and Nonstationary
Predictors,” 2021)
Hewamalage et al. (“Recurrent Neural Networks for Time Series Forecasting: Current status and future direc-
tions,” 2021)
Hunt (“In-sample tests of predictability are superior to pseudo-out-of-sample tests, even when data mining,”
2022)
Hyndman and Athanasopoulos ( _Forecasting: Principles and Practice (Third Edition)_ , 2020)
Januschowski et al. (“Forecasting with trees,” 2022)
Kang et al. (“Déjà vu: A data-centric forecasting approach through time series cross-similarity,” 2021)
**Kang-et-al-2021e**
Lichtendahl and Winkler (“Why do some combinations perform better than others?” 2020)
Loning and Kiraly (“Forecasting with sktime: Designing sktime’s New Forecasting API and Applying It to
Replicate and Extend the M4 Study,” 2020)
Martin et al. (“Optimal probabilistic forecasts: When do they work?” 2022)
Masini et al. (“Machine Learning Advances for Time Series Forecasting,” 2021)


Montero-Manso and Hyndman (“Principles and Algorithms for Forecasting Groups of Time Series: Locality and
Globality,” 2021)
Neto et al. (“Uncovering regimes in out of sample forecast errors,” 2021)
Nybrant (“On Robust Forecast Combinations With Applications to Automated Forecasting,” 2021)
Oreshkin et al. (“N-BEATS: Neural basis expansion analysis for interpretable time series forecasting,” 2020)
Perron and Yamamoto (“Testing for Changes in Forecasting Performance,” 2021)
Petropoulos et al. (“Forecasting: theory and practice,” 2022)
Post et al. (“Robust optimization of forecast combinations,” 2019)
Qian et al. (“Combining forecasts for universally optimal performance,” 2022)
Quaedvlieg (“Multi-Horizon Forecast Comparison,” 2021)
Radchenko et al. (“Too similar to combine? On negative weights in forecast combination,” 2022)
Rossi (“Forecasting in the Presence of Instabilities: How Do We Know Whether Models Predict Well and How
to Improve Them,” 2020)
Salinas et al. (“DeepAR: Probabilistic Forecasting with Autoregressive Recurrent Networks,” 2020)
Siliverstovs and Wochner (“State-Dependent Evaluation of Predictive Ability,” 2021)
Smyl (“A hybrid method of exponential smoothing and recurrent neural networks for time series forecasting,”
2020)
Tadayon and Iwashita (“Comprehensive Analysis of Time Series Forecasting Using Neural Networks,” 2020)
Talagala et al. (“FFORMPP: Feature-based forecast model performance prediction,” 2022)
Thorarinsdottir (“Forecast evaluation,” 2021)
Wu et al. (“AutoCTS: Automated Correlated Time Series Forecasting – Extended Version,” 2021)

### 2.2 Comprehensive list of references

**2.2.1 Forecasting QWIM time series, empirical asset pricing, and predictability of financial returns**

List of references:
Ahmed et al. (“Best of the Best: A Comparison of Factor Models,” 2019)
Alhnaity and Abbod (“A new hybrid financial time series prediction model,” 2020)
Arias-Calluari et al. (“Methods for forecasting the effect of exogenous risks on stock markets,” 2021)
Babiak and Barunik (“Deep Learning, Predictability, and Optimal Portfolio Returns,” 2020)
Bahrami et al. (“Are advanced emerging market stock returns predictable? A regime-switching forecast combi-
nation approach,” 2019)
Bailey et al. (“Measurement of Factor Strength: Theory and Practice,” 2020)
Baitinger and Flegel (“New Concepts in Financial Forecasting: Network-Based Information, Topological Data
Analysis and their Combination,” 2021)
Bali et al. (“Different Strokes: Return Predictability Across Stocks and Bonds with Machine Learning and Big
Data,” 2021)
Baltas and Karyampas (“Forecasting the Equity Risk Premium: The Importance of Regime-Dependent Evalu-
ation,” 2020)
Baltussen et al. (“Predicting Bond Returns: 70 Years of International Evidence,” 2020)
Bektic et al. (“Factor-based investing in government bond markets: a survey of the current state of research,”
2020)
Bessembinder et al. (“Time Series Variation in the Factor Zoo,” 2022)
Bianchi and McAlinn (“Divide and Conquer: Financial Ratios and Industry Returns Predictability,” 2021)
Bianchi et al. (“Bond Risk Premiums with Machine Learning,” 2021)
Bianchi and Tamoni (“Sparse Predictive Regressions: Statistical Performance and Economic Significance,” 2020)
Bielinski and Broby (“Machine Learning Methods in Asset Pricing,” 2021)
Blitz et al. (“Five Concerns with the Five-Factor Model,” 2018)
Bryzgalova et al. (“Bayesian solutions for the factor zoo: we just ran two quadrillion models,” 2021)
Capolongo and Pacella (“Forecasting inflation in the euro area: countries matter!” 2021)
Carr and Wu ( _Decomposing Long Bond Returns: A Decentralized Theory_ , 2021)
Castilho et al. (“Forecasting Financial Market Structure from Network Features using Machine Learning,” 2021)
Charles et al. (“Stock return predictability: Evaluation based on interval forecasts,” 2022)


Chatterjee et al. (“Stock Price Prediction Using Time Series, Econometric, Machine Learning, and Deep Learning
Models,” 2021)
Chen and Zimmermann (“Open Source Cross-Sectional Asset Pricing,” 2021)
Cheng et al. (“Financial time series forecasting with multi-modality graph neural network,” 2022)
Chevallier et al. (“Is It Possible to Forecast the Price of Bitcoin?” 2021)
Chiang et al. (“Modeling the cross-section of stock returns using sensible models in a model pool,” 2021)
Chib et al. (“Winners from Winners: A Tale of Risk Factors,” 2022)
Chib et al. (“On Comparing Asset Pricing Models,” 2020)
Chu (“Forecasting Recessions with Financial Variables and Temporal Dependence,” 2021)
Chudik et al. (“Variable Selection and Forecasting in High Dimensional Linear Regressions with Structural
Breaks,” 2021)
Cohen et al. (“Visual Forecasting of Time Series with Image-to-Image Regression,” 2020)
Cohen et al. (“Visual Time Series Forecasting: An Image-driven Approach,” 2021)
Collot and Hemauer (“A literature review of new methods in empirical asset pricing: omitted-variable and
errors-in-variable bias,” 2021)
Cong et al. (“Deep Sequence Modeling: Development and Applications in Asset Pricing,” 2021)
Cornell (“Stock characteristics and stock returns: a skeptic’s look at the cross section of expected returns,”
2020)
Czasonis et al. (“Addition by Subtraction: A Better Way to Forecast Factor Returns (and Everything Else),”
2020)
Czasonis et al. (“Relevance,” 2021)
Czasonis et al. (“The Past as Prologue: How to Forecast Presidential Elections,” 2021)
Dai et al. (“Predicting stock returns: A risk measurement perspective,” 2021)
Dai et al. (“Forecasting stock return volatility: The role of shrinkage approaches in a data-rich environment,”
2022)
Dendramis et al. (“A similarity-based approach for macroeconomic forecasting,” 2020)
Dong et al. (“Predictive power of ARIMA models in forecasting equity returns: a sliding window method,” 2020)
Dong et al. (“Anomalies and the expected market return,” 2022)
Drobetz and Otto (“Empirical Asset Pricing via Machine Learning: Evidence from the European Stock Market,”
2020)
Elkamhi et al. (“Factor Investing Using Capital Market Assumptions,” 2021)
Ellingsen et al. (“News media vs. FRED-MD for macroeconomic forecasting,” 2022)
Fama and French (“Choosing factors,” 2018)
Fama and French (“Comparing Cross-Section and Time-Series Factor Models,” 2020)
Fan et al. (“FarmTest: Factor-adjusted robust multiple testing with approximate false discovery control,” 2019)
Faria and Verona (“Time-frequency forecast of the equity premium,” 2021)
Fleiss and Cui (“Forecasting Stock Price Changes Using Natural Language Processing,” 2021)
Fulton and Hubrich (“Forecasting US Inflation in Real Time,” 2021)
Gafka et al. (“Sources of Return Predictability,” 2021)
Geertsema and Lu (“Long-horizon predictability and information decay in equity markets,” 2021)
Ghorbani and Chong (“A dimension reduction method for stock-price prediction using multiple predictors,”
2021)
Giovannelli et al. (“Forecasting stock returns with large dimensional factor models,” 2021)
Goliński and Spencer (“Estimating the Term Structure with Linear Regressions: Getting to the Roots of the
Problem,” 2021)
Gospodinov and Maasoumi (“Generalized aggregation of misspecified models: with an application to asset
pricing,” 2021)
Gospodinov and Robotti (“Common pricing across asset classes: Empirical evidence revisited,” 2021)
Gu et al. (“Autoencoder asset pricing models,” 2021)
Hammerschmid and Lohre (“Regime Shifts and Stock Return Predictability,” 2018)
Haase and Neuenkirch (“Forecasting Stock Market Recessions in the US: Predictive Modeling using Different
Identification Approaches,” 2021)
Harvey et al. (“Real-Time Detection of Regimes of Predictability in the U.S. Equity Premium,” 2021)
Hassler and Pohle (“Forecasting under Long Memory,” 2021)


Hauzenberger et al. (“Real-time Inflation Forecasting Using Non-linear Dimension Reduction Techniques,” 2021)
He and Gu (“Multi-modal Attention Network for Stock Movements Prediction,” 2022)
Ho and Lin (“Training by Rolling: Machine Learning and Stock Returns Forecasting,” 2021)
Hull and Qiao (“A Practitioner’s Defense of Return Predictability,” 2017)
Ilmanen et al. (“Demystifying illiquid assets: expected returns for private equity,” 2020)
Iworiso and Vrontos (“On the Predictability of the Equity Premium Using Deep Learning Techniques,” 2021)
Kalfa and Marquez (“Forecasting FOMC Forecasts,” 2021)
Karolyi and Van Nieuwerburgh (“New Methods for the Cross-Section of Returns,” 2020)
Kelly et al. (“Characteristics are covariances: A unified model of risk and return,” 2019)
Klingberg Malmer and Pettersson (“Tidying up the factor zoo: Using machine learning to find sparse factor
models that predict asset returns,” 2020)
Kozak et al. (“Shrinking the cross-section,” 2020)
Kynigakis and Panopoulou (“Does Model Complexity add Value to Asset Allocation? Evidence from Machine
Learning Forecasting Models,” 2021)
Lee and Seregina (“Optimal Portfolio Using Factor Graphical Lasso,” 2022)
Lettau and Pelger (“Factors That Fit the Time Series and Cross-Section of Stock Returns,” 2020)
Leung et al. (“The Promises and Pitfalls of Machine Learning for Predicting Stock Returns,” 2021)
Li and Bastos (“Stock Market Forecasting Using Deep Learning and Technical Analysis: A Systematic Review,”
2020)
Martinez et al. ( _Smooth Robust Multi-Horizon Forecasts_ , 2020)
McMillan (“Forecasting sector stock market returns,” 2021)
McMillan (“Forecasting U.S. stock returns,” 2021)
Meligkotsidou et al. (“Out-of-sample equity premium prediction: a complete subset quantile regression ap-
proach,” 2021)
Neri (“Domain Specific Concept Drift Detectors for Predicting Financial Time Series,” 2021)
Nevasalmi (“Recession forecasting with high-dimensional data,” 2022)
Nietert and Otto (“Empirical asset pricing: economic significance and economic model evaluation,” 2020)
Noguer i Alonso and Srivastava (“The Shape of Performance Curve in Financial Time Series,” 2021)
Noguer i Alonso et al. (“Deep Learning for Equity Time Series Prediction,” 2020)
Nonejad (“Bayesian model averaging and the conditional volatility process: an application to predicting aggre-
gate equity returns by conditioning on economic variables,” 2021)
Oh and Patton (“Better the Devil You Know: Improved Forecasts from Imperfect Models,” 2021)
Paranhos (“Predicting Inflation with Neural Networks,” 2021)
Pinho (“Forecast comparison of volatility models and their combinations (FTSE100): a tied race,” 2020)
Rahimikia and Poon (“Machine Learning for Realised Volatility Forecasting,” 2021)
Rapach et al. (“Industry return predictability: A machine learning approach,” 2019)
Rapach and Zhou (“Time-series and Cross-sectional Stock Return Forecasting: New Machine Learning Meth-
ods,” 2020)
Rapach and Zhou (“Asset Pricing: Time-Series Predictability,” 2022)
Reschenhofer et al. (“Evaluation of current research on stock return predictability,” 2020)
Roy (“A six-factor asset pricing model: The Japanese evidence,” 2021)
Salisu and Tchankam (“US Stock return predictability with high dimensional models,” 2022)
Smith and Timmermann (“Break Risk,” 2021)
Smith et al. (“Equity Premium Forecasts with an Unknown Number of Structural Breaks,” 2020)
Son and Lee (“Graph-based multi-factor asset pricing model,” 2022)
Stein (“Out-of-Sample Equity Premium Prediction: Combination Forecasts with Frequency-Decomposed Vari-
ables,” 2021)
Stivers (“Equity premium predictions with many predictors: A risk-based explanation of the size and value
factors,” 2018)
Stoyanov and Fabozzi (“Dynamics of Equity Factor Returns and Asset Pricing,” 2021)
Tilly and Livan (“Macroeconomic forecasting with statistically validated knowledge graphs,” 2021)
Tilly et al. (“Macroeconomic forecasting through news, emotions and narrative,” 2021)
Timmermann (“Forecasting methods in finance,” 2018)


Trucı́os et al. (“Forecasting Conditional Covariance Matrices in High-Dimensional Time Series: a General Dy-
namic Factor Approach,” 2021)
Viswanathan and Stephen (“Does Machine Learning Algorithms Improve Forecasting Accuracy? Predicting
Stock Market Index Using Ensemble Model,” 2020)
Wang et al. (“The Best of Both Worlds: Forecasting US Equity Market Returns Using a Hybrid Machine
Learning Time Series Approach,” 2021)
Wang et al. (“Forecasting stock returns: A time-dependent weighted least squares approach,” 2021)
Weigand (“Machine learning in empirical asset pricing,” 2019)
Wu et al. (“Equity2Vec: End-to-end Deep Learning Framework for Cross-sectional Asset Pricing,” 2021)
Xu et al. (“HIST: A Graph-based Framework for Stock Trend Forecasting via Mining Concept-Oriented Shared
Information,” 2022)
Yang et al. (“NumHTML: Numeric-Oriented Hierarchical Transformer Model for Multi-task Financial Forecast-
ing,” 2022)
Yang et al. (“Why Existing Machine Learning Methods Fails At Extracting the Information of Future Returns
Out of Historical Stock Prices : the Curve-Shape-Feature and Non-Curve-Shape-Feature Modes,” 2021)
Yara et al. (“Value return predictability across asset classes and commonalities in risk premia,” 2021)
Yin (“Equity premium prediction: keep it sophisticatedly simple,” 2021)
Zeng et al. (“Deep Video Prediction for Time Series Forecasting,” 2021)
Zhan and Xiao (“A Fast Evidential Approach for Stock Forecasting,” 2021)
Zhang (“Empirical asset pricing and ensemble machine learning,” 2021)
Zhu et al. (“High-Dimensional Estimation, Basis Assets, and the Adaptive Multi-Factor Model,” 2021)

**2.2.2 Testing procedures for QWIM time series, empirical asset pricing and predictability of finan-
cial returns**

List of references:
Ardia and Dufays (“Measuring uncertainty and uncertainty dispersion from a large set of model predictions,”
2021)
Barillas and Shanken (“Real-time Portfolio Choice Implications of Asset Pricing Models,” 2019)
Barras (“A large-scale approach for evaluating asset pricing models,” 2019)
Bryzgalova et al. (“Bayesian solutions for the factor zoo: we just ran two quadrillion models,” 2021)
Cai et al. (“Testing capital asset pricing models using functional-coefficient panel data models with cross-sectional
dependence,” 2022)
Chai et al. (“Which model best explains the returns of large Australian stocks?” 2019)
Charles et al. (“Stock return predictability: Evaluation based on interval forecasts,” 2022)
Chen et al. (“Predicting returns out of sample: A naive model averaging approach,” 2020)
Chiah et al. (“A Better Model? An Empirical Investigation of the Fama-French Five-factor Model in Australia,”
2016)
Chib and Zeng (“Which factors are risk factors in asset pricing? A model scan framework,” 2020)
Chib et al. (“On Comparing Asset Pricing Models,” 2020)
Chib et al. (“Winners from Winners: A Tale of Risk Factors,” 2022)
Chordia et al. (“Anomalies and false rejections,” 2020)
Frenkel et al. (“Testing for the rationality of central bank interest rate forecasts,” 2021)
Gospodinov and Robotti (“Common pricing across asset classes: Empirical evidence revisited,” 2021)
Goyal and Jegadeesh (“Cross-Sectional and Time-Series Tests of Return Predictability: What Is the Difference?”
2018)
Gramespacher and Banziger (“The Bias in Two-Pass Regression Tests of Asset-Pricing Models in Presence of
Idiosyncratic Errors with Cross-Sectional Dependence,” 2019)
Harvey and Liu (“Detecting Repeatable Performance,” 2020)
Harvey et al. (“An Evaluation of Alternative Multiple Testing Methods for Finance Applications,” 2020)
Hoga and Dimitriadis (“On Testing Equal Conditional Predictive Ability Under Measurement Error,” 2021)
Janssen (“Multi-horizon comparison of multivariate inflation forecasting,” 2019)
Jegadeesh et al. (“Empirical tests of asset pricing models with individual assets: Resolving the errors-in-variables
bias in risk premium estimation,” 2019)


Kelly et al. (“Characteristics are covariances: A unified model of risk and return,” 2019)
Kruse et al. (“Comparing Predictive Accuracy under Long Memory, With an Application to Volatility Forecast-
ing,” 2019)
Kyriakou et al. (“Longer-Term Forecasting of Excess Stock Returns – The Five-Year Case,” 2020)
Ledoit et al. (“Efficient Sorting: A More Powerful Test for Cross-Sectional Anomalies,” 2019)
Mikeliani and Kavlashvili (“Evaluation and comparison of machine learning and classical econometric AR model
on financial time series data,” 2020)
Odendahl et al. (“Comparing Forecast Performance with State Dependence,” 2020)
Pesaran and Smith (“The Role of Factor Strength and Pricing Errors for Estimation and Inference in Asset
Pricing Models,” 2019)
Pinho (“Forecast comparison of volatility models and their combinations (FTSE100): a tied race,” 2020)
Prasad et al. (“Prediction of Stock Prices Using Statistical and Machine Learning Models: A Comparative
Analysis,” 2021)
Siami-Namini et al. (“A Comparative Analysis of Forecasting Financial Time Series Using ARIMA, LSTM, and
BiLSTM,” 2019)
Siliverstovs and Wochner (“State-Dependent Evaluation of Predictive Ability,” 2021)
Suhonen et al. (“Quantifying Backtest Overfitting in Alternative Beta Strategies,” 2017)
Tang et al. (“Out-of-sample equity premium prediction: A scenario analysis approach,” 2018)
Tunaru et al. (“Testing the Forecasting Ability of Multi-Factor Models on Non-US Interbank Rates,” 2021)
Vincent et al. (“Investment styles and the multiple testing of cross-sectional stock return predictability,” 2020)
Xie (“Forecasting Long-Term Equity Returns: A Comparison of Popular Methodologies,” 2021)
Zhao (“Essays on Asset Pricing: A Model Comparison Perspective,” 2020)

**2.2.3 Forecasting time series**

List of references:
Alexandrov et al. (“GluonTS: Probabilistic and Neural Time Series Modeling in Python,” 2020)
Ankile and Krange (“The DONUT Approach to Ensemble Combination Forecasting,” 2022)
Ansari et al. (“Deep Explicit Duration Switching Models for Time Series,” 2021)
Ashouri et al. (“Fast Forecast Reconciliation Using Linear Models,” 2022)
Athanasopoulos and Kourentzes ( _On the evaluation of hierarchical forecasts_ , 2020)
Athanasopoulos et al. (“Hierarchical Forecasting,” 2019)
Bandara et al. (“Improving the accuracy of global forecasting models using time series data augmentation,”
2021)
Berardi et al. (“Mind the (Convergence) Gap: Bond Predictability Strikes Back!” 2021)
Berrisch and Ziel (“CRPS Learning,” 2021)
Bisaglia and Grigoletto (“A new time-varying model for forecasting long-memory series,” 2021)
Castle et al. (“Forecasting Principles from Experience with Forecasting Competitions,” 2021)
Castle et al. (“Selecting a Model for Forecasting,” 2021)
Cerqueira et al. (“Evaluating time series forecasting models: an empirical study on performance estimation
methods,” 2020)
Cerqueira et al. (“Model Selection for Time Series Forecasting: Empirical Analysis of Different Estimators,”
2021)
Challu et al. (“DMIDAS: Deep Mixed Data Sampling Regression for Long Multi-Horizon Time Series Forecast-
ing,” 2021)
Chen et al. (“Learning from Multiple Time Series: A Deep Disentangled Approach to Diversified Time Series
Forecasting,” 2021)
Dama and Sinoquet (“Analysis and modeling to forecast in time series: a systematic review,” 2021)
Deshpande et al. (“Long Horizon Forecasting With Temporal Point Processes,” 2021)
Faloutsos et al. (“Forecasting Big Time Series: Theory and Practice,” 2019)
Feldkircher et al. (“Factor Augmented Vector Autoregressions, Panel VARs, and Global VARs,” 2020)
Godahewa et al. (“Monash Time Series Forecasting Archive,” 2021)
Grazzi et al. (“Meta-Forecasting by combining Global Deep Representations with Local Adaptation,” 2021)
Harris et al. (“Construction and visualization of confidence sets for frequentist distributional forecasts,” 2019)


Hassler and Pohle (“Forecasting under Long Memory,” 2021)
Hewamalage et al. (“Global Models for Time Series Forecasting: A Simulation Study,” 2020)
Hewamalage et al. (“Recurrent Neural Networks for Time Series Forecasting: Current status and future direc-
tions,” 2021)
Hyndman and Athanasopoulos ( _Forecasting: Principles and Practice (Third Edition)_ , 2020)
Inoue et al. (“Rolling window selection for out-of-sample forecasting with time-varying parameters,” 2017)
Kang et al. (“Déjà vu: A data-centric forecasting approach through time series cross-similarity,” 2021)
Liu et al. (“Forecast Methods for Time Series Data: A Survey,” 2021)
Loning and Kiraly (“Forecasting with sktime: Designing sktime’s New Forecasting API and Applying It to
Replicate and Extend the M4 Study,” 2020)
Makridakis et al. (“Forecasting in social settings: The state of the art,” 2020)
Masini et al. (“Machine Learning Advances for Time Series Forecasting,” 2021)
Montero-Manso and Hyndman (“Principles and Algorithms for Forecasting Groups of Time Series: Locality and
Globality,” 2020)
Nystrup et al. (“Dimensionality reduction in forecasting with temporal hierarchies,” 2021)
Petropoulos and Grushka-Cockayne (“Fast and Frugal Time Series Forecasting,” 2021)
Petropoulos et al. (“Forecasting: theory and practice,” 2022)
Okuno et al. (“Combining multiple forecasts for multivariate time series via state-dependent weighting.,” 2019)
Oreshkin et al. (“N-BEATS: Neural basis expansion analysis for interpretable time series forecasting,” 2019)
Salinas et al. (“DeepAR: Probabilistic Forecasting with Autoregressive Recurrent Networks,” 2020)
Smyl (“A hybrid method of exponential smoothing and recurrent neural networks for time series forecasting,”
2020)
Tadayon and Iwashita (“Comprehensive Analysis of Time Series Forecasting Using Neural Networks,” 2020)
Talagala et al. (“FFORMPP: Feature-based forecast model performance prediction,” 2022)
Timmermann (“Forecasting methods in finance,” 2018)
Wang et al. (“Deep Factors for Forecasting,” 2019)
Wellens et al. (“Transfer learning for hierarchical forecasting: Reducing computational efforts of M5 winning
methods,” 2022)
Wen et al. (“Forecasting realized volatility of Chinese stock market: A simple but efficient truncated approach,”
2022)
Wu et al. (“AutoCTS: Automated Correlated Time Series Forecasting – Extended Version,” 2021)

**2.2.4 Forecasting time series using Machine Learning**

List of references:
Alexandrov et al. (“GluonTS: Probabilistic and Neural Time Series Modeling in Python,” 2020)
Ansari et al. (“Deep Explicit Duration Switching Models for Time Series,” 2021)
Babii et al. (“Machine Learning Panel Data Regressions with Heavy-tailed Dependent Data: Theory and Ap-
plication,” 2021)
Bhatnagar et al. (“Merlion: A Machine Learning Library for Time Series,” 2021)
Bielinski and Broby (“Machine Learning Methods in Asset Pricing,” 2021)
Bloemheuvel et al. (“Multivariate Time Series Regression with Graph Neural Networks,” 2022)
Castilho et al. (“Forecasting Financial Market Structure from Network Features using Machine Learning,” 2021)
Chen et al. (“Deep learning in asset pricing,” 2021)
Chen et al. (“Multi-Scale Adaptive Graph Neural Network for Multivariate Time Series Forecasting,” 2022)
Chatterjee et al. (“Stock Price Prediction Using Time Series, Econometric, Machine Learning, and Deep Learning
Models,” 2021)
Chatigny et al. (“Neural forecasting at scale,” 2021)
Cholakov and Kolev (“Transformers predicting the future. Applying attention in next-frame and time series
forecasting,” 2021)
Cohen et al. (“Visual Time Series Forecasting: An Image-driven Approach,” 2021)
Debnath et al. (“Exploring Generative Data Augmentation in Multivariate Time Series Forecasting : Opportu-
nities and Challenges,” 2021)
Du et al. (“AdaRNN: Adaptive Learning and Forecasting of Time Series,” 2021)


Faloutsos et al. (“Forecasting Big Time Series: Theory and Practice,” 2019)
Filipovic and Khalilzadeh (“Machine Learning for Predicting Stock Return Volatility,” 2021)
Fjellstrom (“Long Short-Term Memory Neural Network for Financial Time Series,” 2022)
Geertsema and Lu (“Long-horizon predictability and information decay in equity markets,” 2021)
Harris et al. (“Construction and visualization of confidence sets for frequentist distributional forecasts,” 2019)
Herzen et al. (“Darts: User-Friendly Modern Machine Learning for Time Series,” 2022)
Hewamalage et al. (“Recurrent Neural Networks for Time Series Forecasting: Current status and future direc-
tions,” 2021)
Januschowski et al. (“Forecasting with trees,” 2022)
Jin et al. (“Robust Forecast Comparison,” 2017)
Kiefer et al. (“Univariate Time Series Forecasting: Machine Learning Prediction of the Best Suitable Forecast
Model Based on Time Series Characteristics,” 2021)
Kosman and Castro (“Vision-Guided Forecasting – Visual Context for Multi-Horizon Time Series Forecasting,”
2021)
Kynigakis and Panopoulou (“Does Model Complexity add Value to Asset Allocation? Evidence from Machine
Learning Forecasting Models,” 2021)
Lara-Benı́tez et al. (“Evaluation of the Transformer Architecture for Univariate Time Series Forecasting,” 2021)
Lara-Benitez et al. (“An Experimental Review on Deep Learning Architectures for Time Series Forecasting,”
2021)
Le Guen and Thome (“Deep Time Series Forecasting with Shape and Temporal Criteria,” 2021)
Li and Bastos (“Stock Market Forecasting Using Deep Learning and Technical Analysis: A Systematic Review,”
2020)
Li et al. (“Bayesian forecast combination using time-varying features,” 2021)
Lim and Zohren (“Time-series forecasting with deep learning: a survey,” 2021)
Liu et al. (“Time Series is a Special Sequence: Forecasting with Sample Convolution and Interaction,” 2021)
Loning and Kiraly (“Forecasting with sktime: Designing sktime’s New Forecasting API and Applying It to
Replicate and Extend the M4 Study,” 2020)
Mancuso et al. (“A machine learning approach for forecasting hierarchical time series,” 2021)
Masini et al. (“Machine Learning Advances for Time Series Forecasting,” 2021)
Nevasalmi (“Forecasting multinomial stock returns using machine learning methods,” 2020)
Noguer i Alonso and Srivastava (“The Shape of Performance Curve in Financial Time Series,” 2021)
Papaioannou et al. (“Time Series Forecasting Using Manifold Learning,” 2021)
Paranhos (“Predicting Inflation with Neural Networks,” 2021)
Oreshkin et al. (“N-BEATS: Neural basis expansion analysis for interpretable time series forecasting,” 2019)
Petropoulos and Spiliotis (“The Wisdom of the Data: Getting the Most Out of Univariate Time Series Fore-
casting,” 2021)
Petropoulos et al. (“Forecasting: theory and practice,” 2022)
Pinto and Castle ( _A machine learning dynamic switching approach to forecasting when there are structural
breaks_ , 2021)
Rajapaksha et al. (“LoMEF: A Framework to Produce Local Explanations for Global Model Time Series Fore-
casts,” 2021)
Rožanec et al. (“Explaining Bad Forecasts in Global Time Series Models,” 2021)
Salinas et al. (“DeepAR: Probabilistic Forecasting with Autoregressive Recurrent Networks,” 2020)
Smyl (“A hybrid method of exponential smoothing and recurrent neural networks for time series forecasting,”
2020)
Spiliotis et al. (“Hierarchical forecast reconciliation with machine learning,” 2021)
Tadayon and Iwashita (“Comprehensive Analysis of Time Series Forecasting Using Neural Networks,” 2020)
Theodosiou and Kourentzes (“Forecasting with Deep Temporal Hierarchies,” 2021)
Viswanathan and Stephen (“Does Machine Learning Algorithms Improve Forecasting Accuracy? Predicting
Stock Market Index Using Ensemble Model,” 2020)
Wang et al. (“Deep Factors for Forecasting,” 2019)
Wellens et al. (“Transfer learning for hierarchical forecasting: Reducing computational efforts of M5 winning
methods,” 2022)


Wen et al. (“Forecasting realized volatility of Chinese stock market: A simple but efficient truncated approach,”
2022)
Wu et al. (“Autoformer: Decomposition Transformers with Auto-Correlation for Long-Term Series Forecasting,”
2022)
Xu et al. (“Instance-wise Graph-based Framework for Multivariate Time Series Forecasting,” 2021)
Xu et al. (“HIST: A Graph-based Framework for Stock Trend Forecasting via Mining Concept-Oriented Shared
Information,” 2022)
Yang et al. (“Why Existing Machine Learning Methods Fails At Extracting the Information of Future Returns
Out of Historical Stock Prices : the Curve-Shape-Feature and Non-Curve-Shape-Feature Modes,” 2021)
Zhang (“Empirical asset pricing and ensemble machine learning,” 2021)

**2.2.5 Testing procedures to evaluate and compare forecasts**

List of references:
Anghel (“Data Snooping Bias in Tests of the Relative Performance of Multiple Forecasting Models,” 2021)
Aparicio and Lopez de Prado (“How Hard Is It to Pick the Right Model? MCS and backtest overfitting,” 2018)
Arnold et al. (“Sequentially valid tests for forecast calibration,” 2022)
Arvanitis et al. (“Nonparametric tests for Optimal Predictive Ability,” 2021)
Bates et al. (“Cross-validation: what does it estimate and how well does it do it?” 2021)
Ben Baccar (“Comparative Study on Time Series Forecasting Models,” 2019)
Bergmeir et al. (“A note on the validity of cross-validation for evaluating autoregressive time series prediction,”
2018)
Bouallegue et al. (“The diagonal score: Definition, properties, and interpretations,” 2018)
Brehmer and Gneiting (“Properization: constructing proper scoring rules via Bayes acts,” 2020)
Brehmer et al. (“Using scoring functions to evaluate point process forecasts,” 2021)
Breitung and Knuppel (“How far can we forecast? Statistical tests of the predictive content,” 2021)
Bulut (“Does Statistical Significance Help to Evaluate Predictive Performance of Competing Models?” 2019)
Cerqueira et al. (“Model Selection for Time Series Forecasting: Empirical Analysis of Different Estimators,”
2021)
Cetin and Yavuz (“Comparison of forecast accuracy of Ata and exponential smoothing,” 2021)
Choe and Ramdas (“Comparing Sequential Forecasters,” 2022)
Coroneo et al. (“Testing the Predictive Accuracy of COVID-19 Forecasts,” 2021)
Costantini and Kunst (“On using predictive-ability tests in the selection of time-series prediction models: A
Monte Carlo evaluation,” 2021)
Davydenko and Goodwin (“Assessing Point Forecast Bias Across Multiple Time Series: Measures and Visual
Tools,” 2021)
De Baets and Harvey (“Using judgment to select and adjust forecasts from statistical models,” 2020)
Diebold (“Comparing Predictive Accuracy, Twenty Years Later: A Personal Perspective on the Use and Abuse
of Diebold-Mariano Tests,” 2015)
Fauvel et al. (“A Performance-Explainability Framework to Benchmark Machine Learning Methods: Application
to Multivariate Time Series Classifiers,” 2021)
Fosten and Gutknecht (“Horizon confidence sets,” 2021)
Geweke and Amisano (“Comparing and evaluating Bayesian predictive distributions of asset returns,” 2010)
Gilleland et al. (“Testing the Tests: What Are the Impacts of Incorrect Assumptions When Applying Confidence
Intervals or Hypothesis Tests to Compare Competing Forecasts?” 2018)
Gneiting and Resin (“Regression Diagnostics meets Forecast Evaluation: Conditional Calibration, Reliability
Diagrams, and Coefficient of Determination,” 2022)
Hounyo and Lahiri (“Estimating the variance of a combined forecast: Bootstrap-based approach,” 2022)
Hunt (“In-sample tests of predictability are superior to pseudo-out-of-sample tests, even when data mining,”
2022)
Ilic et al. (“Augmented Out-of-Sample Comparison Method for Time Series Forecasting Techniques,” 2020)
Jin et al. (“Robust Forecast Comparison,” 2017)
Kang et al. (“Assessing Goodness of Fit for Verifying Probabilistic Forecasts,” 2021)
Koutsandreas et al. (“On the selection of forecasting accuracy measures,” 2021)


Lerch et al. (“Forecaster’s Dilemma: Extreme Events and Forecast Evaluation,” 2015)
Lerch et al. (“Forecaster’s Dilemma: Extreme Events and Forecast Evaluation,” 2017)
Martin et al. (“Optimal probabilistic forecasts: When do they work?” 2022)
McCracken (“Tests of Conditional Predictive Ability: Existence, Size, and Power,” 2020)
Murray and Blume (“False Discovery Rate Computation: Illustrations and Modifications,” 2020)
Neto et al. (“Uncovering regimes in out of sample forecast errors,” 2021)
Patton (“Comparing Possibly Misspecified Forecasts,” 2020)
Perron and Yamamoto (“Testing for Changes in Forecasting Performance,” 2021)
Pitarakis (“A Novel Approach to Predictive Accuracy Testing in Nested Environments,” 2020)
Qu et al. (“Comparing forecasting performance in cross-sections,” 2021)
Quaedvlieg (“Multi-Horizon Forecast Comparison,” 2021)
Rožanec et al. (“Explaining Bad Forecasts in Global Time Series Models,” 2021)
Rytchkov and Zhong (“Information Aggregation and P-Hacking,” 2020)
Sharma et al. (“Prediction-Oriented Model Selection in Partial Least Squares Path Modeling,” 2020)
Siliverstovs and Wochner (“State-Dependent Evaluation of Predictive Ability,” 2021)
Spiliotis et al. (“Tales from tails: On the empirical distributions of forecasting errors and their implication to
risk,” 2019)
Stauskas and Westerlund (“Tests of Equal Forecasting Accuracy for Nested Models with Estimated CCE Fac-
tors,” 2022)
Taggart (“Evaluation of point forecasts for extreme events using consistent scoring functions,” 2021)
Taillardat et al. (“Extreme events evaluation using CRPS distributions,” 2022)
Vovk and Wang (“E-values: Calibration, combination, and applications,” 2021)
Wang and Ramdas (“False discovery rate control with e-values,” 2020)
Westerlund et al. (“Testing for Predictability in panels with General Predictors,” 2017)
Yeoleka et al. (“Feature Selection on a Flare Forecasting Testbed: A Comparative Study of 24 Methods,” 2021)
Zhao et al. (“Empirical Quantitative Analysis of COVID-19 Forecasting Models,” 2021)
Zhu and Timmermann (“Can Two Forecasts Have the Same Conditional Expected Accuracy?” 2020)
Ziel and Berk (“Multivariate Forecasting Evaluation: On Sensitive and Strictly Proper Scoring Rules,” 2019)

**2.2.6 Combinations of forecasting methods for time series**

List of references:
Atiya (“Why does forecast combination work so well?” 2020)
Bahrami et al. (“Are advanced emerging market stock returns predictable? A regime-switching forecast combi-
nation approach,” 2019)
Caldeira et al. (“Yield curve forecast combinations based on bond portfolio performance,” 2018)
Cerqueira et al. (“Model Compression for Dynamic Forecast Combination,” 2021)
Chan and Pauwels (“Some theoretical results on forecast combinations,” 2018)
Di Fonzo and Girolimetto (“Cross-temporal forecast reconciliation: Optimal combination method and heuristic
alternatives,” 2020)
Di Fonzo and Girolimetto (“Forecast combination based forecast reconciliation: insights and extensions,” 2021)
Di Fonzo and Girolimetto (“Cross-temporal forecast reconciliation: Optimal combination method and heuristic
alternatives,” 2022)
Fameliti and Skintzi (“Predictive ability and economic gains from volatility forecast combinations,” 2020)
Fang et al. (“Optimal forecast combination based on ensemble empirical mode decomposition for agricultural
commodity futures prices,” 2020)
Godahewa et al. (“Ensembles of localised models for time series forecasting,” 2021)
Hannadige et al. (“Forecasting a Nonstationary Time Series Using a Mixture of Stationary and Nonstationary
Predictors,” 2021)
Hofmarcher and Grun (“Bayesian Model Averaging,” 2020)
Hollyman et al. (“Understanding forecast reconciliation,” 2021)
Holzmann and Klar (“Using Proxies to Improve Forecast Evaluation,” 2021)
Hsiao and Wan (“Is there an optimal forecast combination?” 2014)
Jaganathan and Prakash (“A combination-based forecasting method for the M4-competition,” 2020)


Lee and Seregina (“Optimal Portfolio Using Factor Graphical Lasso,” 2022)
Lichtendahl and Winkler (“Why do some combinations perform better than others?” 2020)
Montero-Manso et al. (“FFORMA: Feature-based Forecast Model Averaging,” 2020)
Montero-Manso and Hyndman (“Principles and Algorithms for Forecasting Groups of Time Series: Locality and
Globality,” 2021)
Nybrant (“On Robust Forecast Combinations With Applications to Automated Forecasting,” 2021)
Okuno et al. (“Combining multiple forecasts for multivariate time series via state-dependent weighting.,” 2019)
Patton (“Comparing Possibly Misspecified Forecasts,” 2020)
Petropoulos and Svetunkov (“A simple combination of univariate models,” 2020)
Petropoulos et al. (“Model combinations through revised base-rates,” 2021)
Post et al. (“Robust optimization of forecast combinations,” 2019)
Qian et al. (“On the forecast combination puzzle,” 2019)
Qian et al. (“Combining forecasts for universally optimal performance,” 2022)
Radchenko et al. (“Too similar to combine? On negative weights in forecast combination,” 2022)
Rehman et al. (“Individual and combination approaches to forecasting hierarchical time series with correlated
data: an empirical study,” 2019)
Roccazzella et al. (“Optimal and robust combination of forecasts via constrained optimization and shrinkage,”
2022)
Shaub (“Fast and accurate yearly time series forecasting with forecast combinations,” 2020)
Stein (“Out-of-Sample Equity Premium Prediction: Combination Forecasts with Frequency-Decomposed Vari-
ables,” 2021)
Svensson (“An Evaluation of Methods for Combining Univariate Time Series Forecasts,” 2018)
Thomson et al. (“Combining forecasts: Performance and coherence,” 2019)
Vaiciukynas et al. (“Two-Step Meta-Learning for Time-Series Forecasting Ensemble,” 2022)
van Dijk and Franses (“Combining expert-adjusted forecasts,” 2019)
Weiss et al. (“Forecast Combinations in R using the ForecastComb Package,” 2018)
Winkler (“Equal Versus Differential Weighting in Combining Forecasts,” 2015)
Zhang (“Empirical asset pricing and ensemble machine learning,” 2021)
Zhao (“The robustness of forecast combination in unstable environments: a Monte Carlo study of advanced
algorithms,” 2021)

**2.2.7 Combination of statistical and machine learning approaches**

List of references:
Allende and Valle (“Ensemble methods for time series forecasting,” 2017)
Barrow and Crone (“A comparison of AdaBoost algorithms for time series forecast combination,” 2016)
Bergmeir et al. (“Time Series Modeling and Forecasting Using Memetic Algorithms for Regime-Switching Mod-
els,” 2012)
Billio et al. (“Time-varying combinations of predictive densities using nonlinear filtering,” 2013)
Gilliland (“The value added by machine learning approaches in forecasting,” 2020)
Grazzi et al. (“Meta-Forecasting by combining Global Deep Representations with Local Adaptation,” 2021)
Habibnia (“Essays in high-dimensional nonlinear time series analysis,” 2016)
Hewamalage et al. (“Recurrent Neural Networks for Time Series Forecasting: Current status and future direc-
tions,” 2021)
Joshi (“Time Series Analysis and Forecasting of the US Housing Starts using Econometric and Machine Learning
Model,” 2019)
Karathanasopoulos et al. (“Modelling and Trading the English and German Stock Markets with Novelty Opti-
mization Techniques,” 2017)
Kuznetsov and Mohri (“Time series prediction and online learning,” 2016)
McDonald et al. (“A comparison of forecasting approaches for capital markets,” 2014)
Menezes and Mastelini (“MegazordNet: combining statistical and machine learning standpoints for time series
forecasting,” 2021)
Pinto and Marçal (“Cross-Validation Based Forecasting Method: A Machine Learning Approach,” 2019)


Pinto and Marçal (“Inflation Rate Forecasting: Extreme Learning Machine as a Model Combination Method,”
2020)
Qian et al. (“Combining forecasts for universally optimal performance,” 2022)
Risse (“Combining Wavelet Decomposition with Machine Learning to Forecast Gold Returns,” 2017)
Talagala et al. (“FFORMPP: Feature-based forecast model performance prediction,” 2021)
Vaiciukynas et al. (“Two-Step Meta-Learning for Time-Series Forecasting Ensemble,” 2022)
Viswanathan and Stephen (“Does Machine Learning Algorithms Improve Forecasting Accuracy? Predicting
Stock Market Index Using Ensemble Model,” 2020)
Zang (“Deep Learning in Multiple Multistep Time Series Prediction,” 2017)

**2.2.8 Probabilistic forecasting of time series**

List of references:
Bjerregård et al. (“An introduction to multivariate probabilistic forecast evaluation,” 2021)
Bouallegue et al. (“The diagonal score: Definition, properties, and interpretations,” 2018)
Deshpande and Sarawagi (“Long Range Probabilistic Forecasting in Time-Series using High Order Statistics,”
2021)
Gonzalez-Rivera et al. (“Prediction regions for interval-valued time series,” 2020)
Graziani et al. (“Probabilistic recalibration of forecasts,” 2021)
Greenberg (“Calibration Scoring Rules for Practical Prediction Training,” 2020)
Jordan et al. (“Evaluating probabilistic forecasts with scoringRules,” 2019)
Le Guen and Thome (“Probabilistic Time Series Forecasting with Structured Shape and Temporal Diversity,”
2020)
Lerch et al. (“Forecaster’s Dilemma: Extreme Events and Forecast Evaluation,” 2017)
Lerch et al. (“Forecaster’s Dilemma: Extreme Events and Forecast Evaluation,” 2015)
Kamarthi et al. (“CAMul: Calibrated and Accurate Multi-view Time-Series Forecasting,” 2021)
Kang et al. (“Assessing Goodness of Fit for Verifying Probabilistic Forecasts,” 2021)
Martin et al. (“Optimal probabilistic forecasts: When do they work?” 2020)
Prayogo et al. (“Time Series Sampling for Probabilistic Forecasting,” 2020)
Taylor and Taylor (“Combining probabilistic forecasts of COVID-19 mortality in the United States,” 2021)

**2.2.9 Metrics to assess forecast performance**

List of references:
Alexander et al. (“Evaluating the Discrimination Ability of Proper Multivariate Scoring Rules,” 2021)
Botchkarev (“A new typology design of performance metrics to measure errors in machine learning regression
algorithms,” 2019)
Cheng et al. (“Forecast Evaluation,” 2019)
Chiu et al. (“A new approach for detecting shifts in forecast accuracy,” 2019)
Gasthaus et al. (“Probabilistic Forecasting with Spline Quantile Function RNNs,” 2019)
Hyndman and Athanasopoulos ( _Forecasting: Principles and Practice (Third Edition)_ , 2020)
Makridakis et al. (“The M4 Competition: 100,000 time series and 61 forecasting methods,” 2019)
Makridakis and Petropoulos (“The M4 competition: Conclusions,” 2020)
Neto et al. (“Uncovering regimes in out of sample forecast errors,” 2021)
Petropoulos et al. (“The inventory performance of forecasting methods: Evidence from the M3 competition
data,” 2019)
Ryll and Seidens (“Evaluating the Performance of Machine Learning Algorithms in Financial Market Forecasting:
A Comprehensive Survey,” 2019)
Samuels and Sekkel (“Model Confidence Sets and forecast combination,” 2017)
Thorarinsdottir (“Forecast evaluation,” 2021)


**2.2.10 Software implementations and frameworks**

List of references:
Alexandrov et al. (“GluonTS: Probabilistic and Neural Time Series Modeling in Python,” 2020)
Bacher et al. (“onlineforecast: An R package for adaptive and recursive forecasting,” 2022)
Bernardi and Catania (“The Model Confidence Set package for R,” 2014)
Bhatnagar et al. (“Merlion: A Machine Learning Library for Time Series,” 2021)
Bokde et al. (“ForecastTB - An R Package as a Test-Bench for Time Series Forecasting, with Application of
Wind Speed and Solar Radiation Modeling,” 2020)
Burns and Whyne (“Seglearn: A Python Package for Learning Sequences and Time Series,” 2018)
Charte et al. (“predtoolsTS: R package for streamlining time series forecasting,” 2019)
de Valk et al. (“Nowcasting: An R Package for Predicting Economic Variables Using Dynamic Factor Models,”
2019)
Golyandina et al. ( _Singular Spectrum Analysis with R_ , 2018)
Herzen et al. (“Darts: User-Friendly Modern Machine Learning for Time Series,” 2022)
Hyndman (“Tidy Time Series and Forecasting in R,” 2020)
Jordan et al. (“Evaluating probabilistic forecasts with scoringRules,” 2019)
Leroy et al. (“MAGMA: Inference and Prediction with Multi-Task Gaussian Processes,” 2020)
Loning et al. (“sktime: A Unified Interface for Machine Learning with Time Series,” 2019)
Qian et al. (“Combining forecasts for universally optimal performance,” 2022)
Salles et al. (“TSPred: A framework for nonstationary time series prediction,” 2022)
Seca (“TimeGym: Debugging for Time Series Modeling in Python,” 2021)
Shaub (“Fast and accurate yearly time series forecasting with forecast combinations,” 2020)
Siebert et al. (“A systematic review of Python packages for time series analysis,” 2021)


## 3 Practical details for the project

The main purpose of the project described in this document is to provide exposure to students on important (and
interesting) practical topics in quantitative wealth and investment management QWIM.
The level of complexity depends on the number of hours designated for the project. For example, 50-60 hours for
a regular project, and 100-120 hours for a thesis/capstone project. Upon request, the scope (and the corresponding
number if hours) of any given project can be extended.
The students would work on the project as part of a team (usually with 2-3 students).
All QWIM projects were selected such that the students’ efforts have a good chance of producing results relevant
to the industry, and at least as good as the results presented in the QWIM literature. Thus for each project we
may consider (on an optional basis, based primarily on students’ preference) to submit a corresponding article to
journals widely followed by practitioners and academics in investment and wealth management, with participating
students included as the leading coauthors of the submitted article.
The main challenge for each project is to identify the criteria for what would be considered **“good enough** ”.
Similar to projects in the industry, the meaning of “good enough” is based on a combination of comprehensive
literature review, discussions within team and with me (and/or my colleagues) and analysis of results. Emphasis is
placed on creating a narrative (with the aid of an interactive visualizer) for convincing the intended audience that
what was done in the project delivers **“good enough** ” outcome.

### 3.1 Interaction with students

For each project I would make myself available for meetings on a weekly basis (for discussions and guidance).
Some of my colleagues have also expressed interest to participate in such meetings. Due to our work schedule and
deliverables, most of the discussions will have to be scheduled outisde working hours (in weekends or evenings).
The meetings will take place through video conferencing such as WebEx, Zoom, Google Meet, Microsoft Teams,
etc., based on the team’s preference. If the meetings are through WebEx, I would provide a link, while the student
team will provide a link for any other video conferencing tool.
The students working on a given project can also send questions by email (my recommendation is to aggregate
the questions from team members into an email sent once a day). We aim to provide answers within 1-2 days, either
by email or through a phone discussion.

### 3.2 Data.

Due to compliance reasons all projects would be based on publicly available, non-proprietary and non-confidential
data (indices, ETFs, mutual funds, etc.). Since neither I nor my team are allowed to provide these datasets, I can
only provide a list of suggested datasets. This list is included in a later section named Practical Info.
The datasets were selected to have the following features:

- be good proxies for most representative asset and subasset classes
- to be widely available
- to be as liquid as possible
- to have daily granularity
- to encompass periods with as many market regimes as possibles (most proposed daily datasets are from 1990
    or 1991)
- time series have “nicer” statistical properties compared to time series of, say, individual stocks or bonds

### 3.3 Private GitHub repository for the QWIM project.

The team will create a private GitHub repository, which will store relevant project materials, including codes. The
team will use Git Desktop application as source control repository linked to the GitHub repository.


### 3.4 Deliverables.

The project deliverables include literature survey, numerical results, analysis and visualization. For each project
references will be provided for a comprehensive literature survey, and students are encouraged to identify additional
relevant literature. Regarding the implementation, the project will primarily use existing codes:

- Python and R packages from official repositories (PyPi for Python and CRAN for R)
- machine learning platforms such as TensorFlow, PyTorch, CNTK, Chainer, mlr3, H20, PlaidML, mlpack, etc.
- implementations of articles through codes available in repositories such as GitHub, BitBucket, GitLab, etc.

Visualization of data and results visualization will be interactive and it will be based on Shiny R framework; to
reduce programming effort, a template for such a Shiny visualizer will be provided in the team private GitHub
repository.
The deliverables are:

- written report including literature survey and numerical results
- interactive visualizer (most likely Shiny-based visualizer using R and Python packages)
- (optional) presentation slides, and/or RMarkdown presentation, and/or Jupyter Notebook(s)

### 3.5 (Optional) Article submission to leading journals

On an optional basis (based primarily on students’ preference), a version of the report can be prepared for submision
to leading journals such as Journal of Financial Data Science, Journal of Portfolio Management, Journal of Asset
Management, Journal of Investment Strategies, Quantitative Finance, Journal of Wealth Management, Journal of
Investing, Journal of Machine Learning in Finance, etc.


## 4 Project tasks and timelines

For each project the main tasks are:

```
1) literature review
```
```
2) decide on the appropriate metrics and quantitative methods within context of "good enough" for the project
```
```
3) write-up summary of literature review: methods, metrics, testing procedures
```
```
4) identification of Python and/or R packages which are most appropriate for the selected methods and metrics
```
```
5) code design to decide on main code components
```
```
6) implementation of code components
```
```
7) interactive visualization of numerical results
```
```
8) project report containing description of methods, metrics, and tests, and analysis of results.
```
### 4.1 Suggested timelines for project tasks

The table below suggests a timeline for the project tasks and the corresponding percentages of project time:

```
Table 1: Suggested timeline for project tasks
Task ID Task Name Percentage of project time
1 Literature review 15%
2 Identification of "good enough" metrics and quantitative methods 5%
3 Write-up of summary of literature review 5%
4 Identification of appropriate packages in Python and/or R 10%
5 Code design for main components of project coding framework 5%
6 Implementation of coding framework and components 40%
7 Interactive visualizer using the provided Shiny template 10%
8 Project report and presentation 10%
```
### 4.2 Literature review.

The first task is based on a comprehensive literature survey, included in the preliminary document of the project.
Students are encouraged to identify additional relevant literature.
This task may be the most important of the project, since it provides an overview of what was done, what works
well and less well, and what appear to be the most promising avenues to complete the project.
Emphasis is placed on information contained in the Main References; the other References would be considered
only if time permits and the team is interested in exploring other avenues.
When reading the literature, there are 4 main directions to consider:

```
1) methods
```
```
2) metrics to assess the performance/robustness of the methods
```
```
3) testing procedures
```
```
4) numerical results
```
The primary focus would be on the the references included in "Main References" subsection of the document for your
QWIM project. Then, to the extent there is time, to consider the other references included in the project document.
In the same time, you are encouraged to identify other references that might be considered "Main references", and
to share those references with me for discussion.
For the articles in Main References category, the suggested approach would be the following:


- For each article focus primarily on Abstract, Conclusion, and Numerical Results
- Do this for all articles considered to be Main References, such that you gain a high-level understanding of
    what is currently done in the literature
- Select the metrics that you may want to use in order to quantify the meaning of "good enough" for the project.
- Select the quantitative methods which appear to be most likely to be "good enough" for the project.
- Perform a "deeper dive" into the articles containing the approaches you consider the most promising,

For the articles which are not in "Main References" category, read Abstract, Conclusion, and Numerical Results, to
see whether any of those articles might need to be considered for inclusion in your summary.

### 4.3 Write-up summary of literature review.

The write-up summary summarizes the methods, metrics, testing procedures, and numerical results identified during
the literature review. The write-up could also be incorporated within reports and/or presentations for the QWIM
project.

### 4.4 Identification of appropriate Python and/or R packages

Based on the literature review and on diiscussions, we identify the most potentially useful methods, metrics and
testing procedures. Then wee identify the most appropriate implementations of the selected methods and metrics.
The primary sources of implementatins are existing codes from:

- Python and R packages from official repositories (PyPi for Python and CRAN for R)
- machine learning platforms such as TensorFlow, PyTorch, CNTK, Chainer, mlr3, H20, PlaidML, mlpack, etc.
- Codes available in repositories such as GitHub, BitBucket, GitLab, etc.

### 4.5 Code design.

An important task is to have a code design session to decide in advance on the main code components, which are
meant to be modular and encapsulated, such that the entire team can work on the codes.
Examples of such main components include extracting data, calculate metrics for the considered procedures,
portfolio metrics, performing tests, construct interactive visualizer, etc.
The code design procedure consists of:

```
1) visual display of major components of the coding framework
```
```
2) UML diagrams for each of the components.
```
The Appendix contains an illustrative example within context of a QWIM project on forecasting of financial
time series. The first figure shows the major components, while the second figure shows UML diagrams of those
components (the names of data members and methods are currently generic, and one would need to change them
to appropriate names)
While these figures were obtained through Microsoft Visio using a code design file (.vsd file), there are other
software tools (either online or installed locally) which can be used to create such code design diagrams. NOTE: if
you have access to Microsoft Visio and you want to use it for code design diagrams, you can ask me for the .vsd
file which was exported into the PDF from which I have extracted the snapshots.
List of software tools for code design diagrams, which are either free (open source) or have a free type of account

- Modelio (eitherdesktopversion oronlineversion)
- LucidChart (online)
- draw.io (eitherdesktopversion oronlineversion, now called app.diagrams.net)


- Visual Paradigm (online)
- UMLet (eitherdesktopor onlineversion)
- Curated list of UML tools – 2019 edition
- Top online UML modeling tools in 2019

### 4.6 Implementation of coding framework and components

The implementation is done using identified packages or codes, in Python and/or R. The project will primarily use
existing codes:

- Python and R packages from official repositories (PyPi for Python and CRAN for R)
- machine learning platforms such as TensorFlow, PyTorch, CNTK, Chainer, mlr3, H20, PlaidML, mlpack, etc.
- implementations of articles through codes available in repositories such as GitHub, BitBucket, GitLab, etc.

### 4.7 Interactive visualizer.

While visualization of data and numerical results can be done through various tools (including Jupyter notebooks
or Dash in Python), my recommendation is to consider an interactive visualizer based on Shiny framework in R.
A template for the Shiny visualizer will be provided in the private GitHub repository set up by the team for the
project.
Some information about Shiny:

- Shiny from RStudio: tutorialsand gallery
- Why R Shiny Trumps UI and JavaScript Based Visualization Tools
- Shiny’s Holy Grail: Interactivity with reproducibility

### 4.8 Project report and presentation.

The report containing description of methods, metrics, and tests, and analysis of results.
While the report can be written using various tools (including Microsoft Word), my recommendation is to use
LyX to write both the project report and the project presentation. Two LyX templates for creating reports and,
respectively, presentations will be provided in the private GitHub repository set up by the team for the project.
Some information about Shiny:

- LyX features
- LyX tutorialwith PDFhere
- LyX Tutorial videoPart Oneand Part Two
- LyX tutorial videoPart Oneand Part Twoand Part Threeand Part Four
- Introduction to LyX
- Insert figures in LyX
- Essentials of LyX


## 5 Design and implementation for the project codes

This section describes a possible approach for the design process and for the implementation (folder structure) of
the project. This approach is presented only to exemplify how it could be done. Each student team has freedom to
consider their own design process.
Design and implementation would be based on following principles:

- coding framework is Python based, with calls to functions available in existing Python and R packages
- leverage common components (such as data input/output, numerical methods, time series, testing, interactive
    visualization and reporting, etc.)
- reusability
- incorporate best practices in coding and numerical implementations
- use, augment and enhance (to largest extent possible) existing Python and R packages and codes

### 5.1 Visualize project workflow and coding framework.

The starting point is to visualize the project workflow in terms of major components, and then to design the code
framework.
The code design procedure consists of:

```
1) visual display of major components of the coding framework
```
```
2) UML diagrams for each of the components.
```
We present examples below for projects including time series forecasting and analysis, machine learning for portfolio
construction, etc.

```
Figure 1: Examples of architecture of coding framework: AlphaPy
```
Source:AlphaPy


```
Figure 2: Examples of architecture of coding framework: Greykite
```
Source:Geykite

```
Figure 3: QLib Framework
```
```
Trading Agent
```
```
Meta Controller
```
```
Analyser
```
```
Decision
```
```
Forecast Model
```
```
Interface
```
```
Multi-level Workflow
```
```
Infrastracture
```
```
Forecasting...Portfolio A...Execution...
```
```
Information Extractor
```
```
Online Serving
```
```
Graph Event
```
```
Factor Text
Alpha Risk
```
```
Data Server
```
```
local remote
```
```
Trainer
```
```
Algorithms Auto-ML
```
```
Model Manager
```
```
ModelModel
Models
Decision GeneratorsModelModel
```
```
Model Interpreter
```
```
Decision Generator
```
```
Order executi...
```
```
Execution Results
```
```
Execution Env
```
```
VWAP/Close/......Sub-workfl...
```
```
Highly Customiz...
```
```
Module in devel...
```
```
Explanation
```
```
Sub-workflow(1) (E.g. High-frequ...
```
```
Execution E...
...
```
```
(1) The sub-workflow will make more fine-grained decisions according to the decision from the upper-level trading agent
```
```
Asset allocat...Stock selecti...
```
```
Trading...
```
```
Viewer does not support full SVG 1.1
```

Figure 4: Examples of major components of coding framework (top) and UML diagrams (bottom)


```
Figure 5: Financial Machine Learning in Portfolio Construction
```
Source:Machine Learning in Asset Management

##### 28


### 5.2 Representative examples of Python libraries with well designed folder structure

List of Python libraries

- QLib is a AI-oriented quantitative investment platform in Python developed by Microsoft researchers
- GluonTSis a Python library deveoped by Amazon researchers for probabilistic time series modeling
- sktimeis a unified framework for machine learning with time series, developed by researchers at Alan Turing
    Institute for data science and artificial intelligence.
- darts is a Python library for easy manipulation and forecasting of time series, developed by researchers at
    Unit8 AI and data analytics company.
- Kats is a Python library developed by Facebook researchers to analyze time series data.
- Kats is a Python library developed by Tinkoff AI researchers to analyze time series data.
- MLFinLab(Machine Learning Financial Laboratory) is a Python library developed by researchers at Hudson
    & Thames.


## 6 Practical Info

### 6.1 Recommended software tools

The sections below describe the recommended software tools, including corresponding versions/subversions, tutorials
and details

#### 6.1.1 Python

The recommended versions are:

- Python version 3.8 (subversion Python 3.8.10 or 3.8.15)
- Python version 3.9 (subversion Python 3.9.10 or 3.9.15)
- Python version 3.10 (latest subversion, currently Python 3.10.8)

There are also relevant Python packages, identified while you are working the project. As a starting point you can
consider the packages included in section on Potentially useful Python and R packages.

#### 6.1.2 R.

The recommended versions are:

- R version 4.2 (recommended is latest subversion, currently R 4.2.2)
- R version 3.6 (subversion R 3.6.3)

On Windows computers you also need to installRtoolsto build R packages from source through compilation, since
not all packages have associated Windows binaries.
There are also relevant R packages, identified while you are working the project. As a starting point you can
consider the packages included in section on Potentially useful Python and R packages.

#### 6.1.3 R IDE.

The recommended R IDE is RStudio Desktop Open Source

- latest version, currently 2022.07.2+576

#### 6.1.4 Python IDE.

The recommended Python IDE is Visual Studio Code VSC

- latest version, currently VSC 1.73

Then add Python extension and other Visual Studio Code extensions from Visual Studio MarketPlace.
Note: Upon request I can provide a list of potentially useful VSC extensions, which can be installed on your
computer (see for examplelink)

#### 6.1.5 Bibliography Manager

The recomemnded bibliography manager isJabRef

- latest version: version 5.7, or
- latest development version fromlink


I can provide you with a bibliography file which contains all refeernces mentioned in the project description, This
file (of extension bib) can be viewed and edited with JabRef, and used together with LyX to write your project
related documents (report, presentation, etc.).
You can easily add/delete/edit this bib file using JabRef.
There are video tutorials on using JabRef:link 1 , link 2 , link 3.
In addition to these video tutorials, I can also have a video online session, to provide an overview and answer
your questions on using LyX and JabRef. This online session (through Google Meet Google Meet) can be recorded
and shared with you afterwards.

#### 6.1.6 Document processor

The recommended document processor isLyX, which is a document processor that encourages an approach to
writing based on the structure of your documents (WYSIWYM) and not simply their appearance (WYSIWYG).
LyX combines the power and flexibility of TeX/LaTeX with the ease of use of a graphical interface. It shoudl
be emohasized that you do not need to know/learn LaTeX in order to tuse LyX.
To install LyX, you need to download and install first TeXLive (seelink), which is a packaged distribution of
LaTeX and associated packages
Then install LyX usinginstallers, making sure that you are pointing to location of installed TeXLive when asked
for a LaTeX distribution during the run of LyX installer.
Recommended versions:

- TexLive (recommended is latest version, currently TeXLive 2022)
- LyX (recommended is latest subversion, currently LyX 2.3.6.1)

There are video tutorials (link 1and link 2 ).
In addition to these video tutorials, I can also have a video online session, to provide an overview and answer
your questions on using LyX and JabRef. This online session (through Google Meet Google Meet) can be recorded
and shared with you afterwards.

#### 6.1.7 Source control manager

The recommended source control manager isGitHub desktop, which can be used in conjunction with thr private
GitHub repository that each student team will create for their project

- latest subversion, currently GitHub Desktop 3.1.2

#### 6.1.8 File editor.

The recommended file editor isNotepad++

- latest subversion (currently Notepad++ 8.4.7) with various plugins (see list of available plugins atlink 1and
    link 2 )

#### 6.1.9 Runtime libraries.

Many Python and R packages require runtime libraries such asMicrosoft Visual C++ Redistributable

- latest version, currently Microsoft Visual C++ Redistributable 64-bit for Visual Studio 2015, 2017, 2019, and
    2022

### 6.2 Recommended datasets

The datasets below were selected to have the following features:

- to be representative proxies for most relevant asset and subasset classes
- to be widely available


- to be as liquid as possible
- to have daily granularity
- to encompass time periods containing as many market regimes as possibles (under this consideration, the
    recommended daily datasets start from early 1990s)
- to have “nicer” statistical properties, which will make modeling easier (under this consideration, time series of
    recommended financial indices have “nicer” statistical properties compared to time series of individual stocks
    or bonds)

The following datasets are suggested

```
Table 2: Daily data sets
Name Description Name Description
BCOMTR Bloomberg Commodity Index Total
Return
```
```
RU20VATR iShares Russell 2000 Value ETF
```
```
HFRIFWI HFRI Fund Weighted Composite Index RUMCINTR iShares Russell Mid-Cap ETF
LBUSTRUU Bloomberg Barclays US Aggregate Bond
Index
```
```
RUMRINTR iShares Micro-Cap ETF
```
```
LG30TRUU Bloomberg Barclays Global High Yield
Total Return Index Value Unhedge
```
```
RUTPINTR iShares Russell Top 200 ETF
```
```
LMBITR Bloomberg Barclays Municipal Bond
Index Total Return Index Value
Unhedged USD
```
```
S5COND S&P 500 Consumer Discretionary Index
```
```
NDDUE15X Amundi MSCI Europe Ex UK Ucits ETF
Dr
```
```
S5CONS S&P 500 Consumer Staples Index
```
```
NDDUJN MSCI Japan Index S5ENRS S&P 500 Energy Index
NDDUNA iShares MSCI North America UCITS
ETF
```
```
S5FINL S&P 500 Financials Sector GICS Level 1
Index
NDDUPXJ MSCI Pacific ex Japan UCITS ETF S5HLTH S&P 500 Health Care Index
NDDUUK iShares MSCI UK ETF S5INDU S&P 500 Industrials Index
NDDUWXUS MSCI World ex USA total net return S5INFT S&P 500 Information Technology Index
NDUEEGF SPDR MSCI Emerging Markets UCITS
ETF
```
```
S5MATR S&P 500 Materials Index
```
```
RU10GRTR iShares Russell 1000 Growth ETF S5RLST S&P 500 Real Estate Index
RU10VATR  iShares Russell 1000 Value ETF S5TELS S&P 500 Communication Services Index
RU20GRTR  iShares Russell 2000 Growth ETF S5UTIL S&P 500 Utilities Index
RU20INTR Russell 2000 Total Return SPXT Proshares S&P 500 EX Technology ETF
```

Table 3: Monthly data sets
Name Description Name Description

IBXXSHY1 iShares 0-5 Year High Yield Corporate
Bond ETF

```
M2USEV MSCI USA Enhanced Value Index
```
IDCT20RT ICE U.S. Treasury 20+ Year Bond Total
Return Index

```
M2USRWGT MSCI USA Risk Weighted Index
```
LBUSTRUU Bloomberg Barclays US Agg Total Return
Value Unhedged USD

```
M2USSNQ MSCI USA Sector Neutral Quality Index
```
LC07TRUU Bloomberg Barclays U.S. Universal Total
Return Index Value Unhedged

```
MID S&P 400 Mid Cap Index index
```
LD01TRUU Bloomberg Barclays 1-3 Yr Credit Total
Return Index Value Unhedged US

```
MXEA MSCI EAFE Index
```
LT01TRUU Bloomberg Barclays US Treasury 1-3
Year Index

```
MXEF MSCI Emerging Markets Index
```
LUICTRUU Bloomberg Barclays U.S. Intermediate
Credit Total Return Index

```
MXUSMVOL MSCI USA Minimum Volatility Index
```
LULCTRUU Bloomberg Barclays U.S. Long Credit
Index

```
MXWD MSCI All Countries World Index
```
M1CXBRU iShares Core MSCI International
Developed Markets ETF

```
MXWOUIM MSCI All Countries World Index
```
M1USMVOL MSCI USA Minimum Volatility (USD)
Index

```
NDDUUS MSCI Daily Total Return Net USA USD
Index
```
M2US000$ iShares Edge MSCI USA Momentum
Factor ETF

```
SPX S&P 500 Index
```

## 7 Potentially useful Python and R software implementations: packages, codes and frameworks

## ages, codes and frameworks

### 7.1 Collections and repositories of resources

**For Data Science, Numerical Methods/ Algorithms, Programming**

List of links:

- Data Science CheatSheet
- professional-programming: collection of full-stack resources for programmers.

**For Python**

List of links:

- Awesome Python
- Awesome Python frameworks, libraries, software and resources
- Best of Python
- Curated list of Python frameworks, libraries, software and resources
- Pythonidae: Curated decibans of scientific programming resources in Python
- Ranked list of Python open-source Machine Learning libraries and tools
- Ranked list of Python open-source libraries and tools
- Ranked list of Python developer tools and libraries
- Time series: analytics, statistics, machine learning, frameworks and databases
- Time series Python packages

**For R**

List of links:

- Available CRAN Packages By Date of Publication
- CRAN Task Views

### 7.2 Connection between Python and R codes

List of links:

- arrow: R interface to ’Apache’ ’Arrow’, a cross-language for accelerated data interchange in-memory data
- pyarrow: Python library for Apache Arrow
- reticulate: R Interface to ’Python’ modules, classes, and functions
- rpy2: Python interface to the R language
- rpy2-arrow: Share Apache Arrow datasets between Python and R
- R Extension for Visual Studio Code


### 7.3 Anomaly detection and data outliers

**Collections of resources**

List of links:

- Anomaly detection related books, papers, videos, and toolboxes

**Python software implementations**

List of packages and/or codes and/or frameworks and/or links:

- adtk: Python toolkit for rule-based/unsupervised anomaly detection in time series
- Anomaly Detection Learning Resources
- Awesome anomaly detection resources
- Curve: time series data anomaly detection by Baidu
- kats: kit to analyze time series data by Facebook
- luminaire: ML driven package by Zillow for monitoring time series data
- Merlion: A Machine Learning Framework for Time Series Intelligence by SalesForce
- PyGOD: Graph Outlier Detection (Anomaly Detection)
- PyOD: Python Toolbox for Scalable Outlier Detection (Anomaly Detection)
- PyODDS: An End-to-end Outlier Detection System
- ruptures: change point detection in Python
- seriesdistancematrix: implements the Series Distance Matrix framework, a flexible component-based frame-
    work that bundles various Matrix Profile related techniques
- Software tools and datasets for anomaly detection on time series data
- Tools and datasets for anomaly detection on time-series data.
- tsad: Time Series Forecasting and Anomaly Detection
- TODS: An Automated Time-series Outlier Detection System
- tsmoothie: time-series smoothing and outlier detection

**R software implementations**

List of packages and/or codes and/or frameworks and/or links:

- amelie: Anomaly Detection with Normal Probability Functions
- ANN2: Artificial Neural Networks for Anomaly Detection
- anomaly: Detecting Anomalies in Data
- AnomalyDetection: package by Twitter to detect anomalies
- anomalize: Tidy Anomaly Detection
- composits: Compositional, Multivariate and Univariate Time Series Outlier Ensemble
- dobin: Dimension Reduction for Outlier Detection


- dsos: Dataset Shift with Outlier Scores
- HDoutliers: Leland Wilkinson’s Algorithm for Detecting Multidimensional Outliers
- isotree: Isolation-Based Outlier Detection
- kssa: automatically identify and validate the best method for missing data imputation in a time series
- lookout: Leave One Out Kernel Density Estimates for Outlier Detection
- mvoutlier: Multivariate Outlier Detection Based on Robust Methods
- odetector: Outlier Detection Using Partitioning Clustering Algorithms
- otsad: Online Time Series Anomaly Detectors
- outForest: Multivariate Outlier Detection and Replacement
- outliers: Tests for Outliers
- outliertree: Explainable Outlier Detection Through Decision Tree Conditioning
- stray: Anomaly Detection in High Dimensional and Temporal Data
- TagAnomaly: Anomaly detection analysis and labeling tool by Microsoft
- trendsegmentR: Linear Trend Segmentation and Point Anomaly Detection
- tsoutliers: Detection of Outliers in Time Series
- univOutl: Detection of Univariate Outliers

### 7.4 Bayesian analysis and modeling.

**Python software implementations**

List of packages and/or codes and/or frameworks and/or links:

- ArviZ: Exploratory analysis of Bayesian models with Python
- baal: enable Bayesian active learning in your research or labeling work
- bambi: BAyesian Model-Building Interface (Bambi)
- bilby: Bayesian inference library
- BayesianOptimization: implementation of global optimization with gaussian processes
- BayesTSA: ayesian methods for solving estimation and forecasting problems in time series analysis
- BoTorch: Bayesian optimization in PyTorch
- Bumps: data fitting and uncertainty estimation
- nutpie: A fast sampler for bayesian posteriors
- Orbit: Bayesian forecasting package by Uber
- PyApprox: high-dimensional approximation and uncertainty quantification
- pyMC: Bayesian Modeling and Probabilistic Machine Learning with Aesara
- PyStan: Python interface to Stan, a platform for statistical modeling
- zeus: Lightning Fast MCMC


**R software implementations**

List of packages and/or codes and/or frameworks and/or links:

- ashr: Methods for Adaptive Shrinkage, using Empirical Bayes
- bain: Bayes Factors for Informative Hypotheses (equality, inequality, and about equality constrained hypothe-
    ses)
- bamp: Bayesian Age-Period-Cohort Modeling and Prediction
- bsamGP: Bayesian Spectral Analysis Models using Gaussian Process Priors
- bayesdfa: Bayesian Dynamic Factor Analysis (DFA) with ’Stan’
- bayefdr: Bayesian Estimation and Optimisation of Expected False Discovery Rate
- BayesFM: Bayesian Inference for Factor Modeling
- bayesforecast: Bayesian Time Series Modeling with Stan
- BayesHMM: Full Bayesian Inference for Hidden Markov Models
- bayesian: Bindings for Bayesian TidyModels
- bayesmodels: The ’Tidymodels’ Extension for Bayesian Models
- bayesplot: Plotting for Bayesian Models
- BayesPostEst: Generate Postestimation Quantities for Bayesian MCMC Estimation
- bayestestR: Understand and Describe Bayesian Models and Posterior Distributions
- BayesTools: Tools for Bayesian Analyses
- BayesVarSel: Bayes Factors, Model Choice and Variable Selection in Linear Models
- BEST: Bayesian Estimation Supersedes the t-Test
- beyondWhittle: Bayesian Spectral Inference for Stationary Time Series
- BFpack: Flexible Bayes Factor Testing of Scientific Expectations
- BMAmevt: Multivariate Extremes: Bayesian Estimation of the Spectral Measure
- bmixture: Bayesian Estimation for Finite Mixture of Distributions
- bnmonitor: An Implementation of Sensitivity Analysis in Bayesian Networks
- BNPmix: Bayesian Nonparametric Mixture Models
- bpcs: Bayesian Paired Comparison Analysis with Stan
- bpgmm: Bayesian Model Selection Approach for Parsimonious Gaussian Mixture Models
- brms: Bayesian Regression Models using ’Stan’
- BSL: Bayesian Synthetic Likelihood
- bspec: Bayesian Spectral Inference
- bsvars: Bayesian Estimation of Structural Vector Autoregressive Models
- dalmatian: Automating the Fitting of Double Linear Mixed Models in ’JAGS’ and ’nimble’
- dbnR: Dynamic Bayesian Network Learning and Inference


- DEBBI: Differential Evolution-Based Bayesian Inference
- ensembleBMA: Probabilistic Forecasting using Ensembles and Bayesian Model Averaging
- fbst: The Full Bayesian Evidence Test, Full Bayesian Significance Test and the e-Value
- greta: scalable statistical modelling in R
- LaplacesDemon: Complete Environment for Bayesian Inference
- mBvs: Bayesian Variable Selection Methods for Multivariate Data
- mlr3mbo: Flexible Bayesian Optimization
- mombf: Bayesian Model Selection and Averaging for Non-Local and Local Priors
- networkABC: Network Reverse Engineering with Approximate Bayesian Computation
- nimble: MCMC, Particle Filtering, and Programmable Hierarchical Modeling
- Nmix: Bayesian Inference on Univariate Normal Mixtures
- posterior: Tools for Working with Posterior Distributions
- rBayesianOptimization: Bayesian Optimization of Hyperparameters
- Rbeast: Bayesian Change-Point Detection and Time Series Decomposition
- REBayes: Empirical Bayes Estimation and Inference
- Revticulate: Interaction with ”RevBayes” in R
- rstan: R Interface to Stan
- rstanarm: Bayesian Applied Regression Modeling via Stan
- SequenceSpikeSlab: Exact Bayesian Model Selection Methods for the Sparse Normal Sequence Model
- shrinkTVP: Efficient Bayesian Inference for Time-Varying Parameter Models with Shrinkage
- tidybayes: Tidy Data and ’Geoms’ for Bayesian Models

### 7.5 Causality, inference and dependencies

**Python software implementations**

List of packages and/or codes and/or frameworks and/or links:

- bilby: Bayesian inference library
- CausalDiscoveryToolbox: causal inference in graphs and in the pairwise settings
- causality: Tools for causal analysis
- causalml: package by Uber for Uplift modeling and causal inference with machine learning algorithms
- copulae: Multivariate data modelling with Copulas
- DoWhy: library by Microsoft for causal inference that supports explicit modeling and testing of causal as-
    sumptions
- HiDimStat: High-dimensional statistical inference tool
- tigramite: time series analysis python module for causal discovery


**R software implementations**

List of packages and/or codes and/or frameworks and/or links:

- causal.decomp: Causal Decomposition Analysis
- CausalImpact: toolkit by Google to infer Causal Effects using Bayesian Structural Time-Series Models
- causaloptim: An Interface to Specify Causal Graphs and Compute Bounds on Causal Effects
- copula: Multivariate Dependence with Copulas
- dCovTS: Distance Covariance and Correlation for Time Series Analysis
- estimatr: Fast Estimators for Design-Based Inference
- flipr: Flexible Inference via Permutations in R
- generalCorr: Generalized Correlations, Causal Paths and Portfolio Selection
- HellCor: The Hellinger Correlation
- infer: Tidy Statistical Inference
- jackstraw: Statistical Inference for Unsupervised Learning
- konfound: Quantify the Robustness of Causal Inferences
- mashr: Multivariate Adaptive Shrinkage
- multivariance: Measuring Multivariate Dependence Using Distance Multivariance
- NlinTS: Models for Non Linear Causality Detection in Time Series
- NNS: Nonlinear nonparametric statistics using partial moments
- pcalg: Methods for Graphical Models and Causal Inference
- qmd: Quantification of Multivariate Dependence
- rmcfs: The MCFS-ID Algorithm for Feature Selection and Interdependency Discovery
- sherlock: package by Netflix for causal machine learning for segment discovery and analysis
- SIHR: Statistical Inference in High Dimensional Regression
- tlverse: One Stop to Targeted Learning in R
- tscopula: Time Series Copula Models
- VLTimeCausality: Variable-Lag Time Series Causality Inference Framework

### 7.6 Classification, Motifs, Neighbors, Wavelets, Transforms.

**Python software implementations**

List of packages and/or codes and/or frameworks and/or links:

- abess: Fast Best-Subset Selection Library
- catboost: Gradient Boosting on Decision Trees by Yandex
- HiClass: hierarchical classification compatible with scikit-learn


- LightGBM: fast, distributed, high performance gradient boosting (GBT, GBDT, GBRT, GBM or MART)
    framework by Microsoft
- Local Cascade Ensemble (LCE) is a high-performing, scalable and user-friendly machine learning method for
    the general tasks of Classification and Regression
- matrixprofile: time series data mining tasks, utilizing matrix profile algorithms
- pyts: time series classification
- scikit-learn: machine learning in Python
- seriesdistancematrix: implements the Series Distance Matrix framework, a flexible component-based frame-
    work that bundles various Matrix Profile related techniques
- sktime: unified framework for machine learning with time series
- stumpy: modern time series analysis
- tslearn: machine learning toolkit dedicated to time-series data

**R software implementations**

List of packages and/or codes and/or frameworks and/or links:

- abess: Fast Best-Subset Selection Library
- AUC: Threshold Independent Performance Measures for Probabilistic Classifiers
- bcTSNE: Projected t-SNE for Batch Correction
- biwavelet: Conduct Univariate and Bivariate Wavelet Analyses
- caret: Classification and Regression Training
- classmap: Visualizing Classification Results
- classifly: Explore Classification Models in High Dimensions
- ContaminatedMixt: Clustering and Classification with the Contaminated Normal
- CORElearn: Classification, Regression and Feature Evaluation
- cvms: Cross-Validation for Model Selection
- ddalpha: Depth-Based Classification and Calculation of Data Depth
- dtw: Dynamic Time Warping Algorithms
- greed: Clustering and Model Selection with the Integrated Classification Likelihood
- ipred: Improved Predictors
- klaR: Classification and Visualization
- matrixProfile: Matrix Profile
- matrixprofiler: Matrix Profile for R
- mclust: Gaussian Mixture Modelling for Model-Based Clustering, Classification, and Density Estimation
- MixGHD: Model Based Clustering, Classification and Discriminant Analysis Using the Mixture of Generalized
    Hyperbolic Distributions
- MixMatrix: Classification with Matrix Variate Normal and t Distributions


- mixSPE: Mixtures of Power Exponential and Skew Power Exponential Distributions for Use in Model-Based
    Clustering and Classification
- mixture: Mixture Models for Clustering and Classification
- randomUniformForest: Random Uniform Forests for Classification, Regression and Unsupervised Learning
- rbooster: AdaBoost Framework for Any Classifier
- rebmix: Finite Mixture Modeling, Clustering & Classification
- regtools: Regression and Classification Tools
- Rmixmod: Classification with Mixture Modelling
- RSSL: Implementations of Semi-Supervised Learning Approaches for Classification
- Rtsne: T-Distributed Stochastic Neighbor Embedding using a Barnes-Hut Implementation
- sbfc: Selective Bayesian Forest Classifier
- SKNN: A Super K-Nearest Neighbor (SKNN) Classification Algorithm
- stacks: Tidy Model Stacking
- TSMining: Mining Univariate and Multivariate Motifs in Time-Series Data
- tsmp: Time Series with Matrix Profile
- yardstick: Tidy Characterizations of Model Performance

### 7.7 Clustering.

**Python software implementations**

List of packages and/or codes and/or frameworks and/or links:

- cclust: Convex Clustering Methods and Clustering Indexes
- ChronoClust: perform clustering on each of a time-series of discrete datasets, and explicitly track the evolution
    of clusters over time
- classix: Fast and explainable clustering based on sorting
- ClusterEnsembles: package for cluster ensembles
- clustergram: Visualization and diagnostics for cluster analysis in Python
- Clusteval: methods for unsupervised cluster validation
- deeptime: analysis of time series data including dimensionality reduction, clustering, and Markov model
    estimation
- dtaidistance: Time series distances: Dynamic Time Warping
- DTCR: Learning Representations for Time Series Clustering
- DTW_kmedoids: Multivariate time series clustering using Dynamic Time Warping (DTW) and k-mediods
- ETNA Time Series Library by Tinkoff AI
- faiss: efficient similarity search and clustering of dense vectors
- fastcluster: Fast hierarchical clustering routines


- genieclust: Fast and Robust Hierarchical Clustering with Noise Point Detection
- hcluster: Hierarchical Clustering Algorithms
- hdbscan: high performance implementation of HDBSCAN clustering
- scikit-learn: machine learning in Python
- TimeSeriesDeepClustering: End-to-end deep representation learning for time series clustering
- tslearn: machine learning toolkit dedicated to time-series data
- validclust: Validate clustering results

**R software implementations**

List of packages and/or codes and/or frameworks and/or links:

- apcluster: Affinity Propagation Clustering
- bahc: bahc: Filter Covariance and Correlation Matrices with Bootstrapped-Averaged Hierarchical Ansatz
- bootcluster: Bootstrapping Estimates of Clustering Stability
- cclust: Convex Clustering Methods and Clustering Indexes
- clue: Cluster Ensembles
- clusrank: Wilcoxon Rank Tests for Clustered Data
- clustAnalytics: Cluster Evaluation on Graphs
- ClustAssess: Tools for Assessing Clustering
- ClustBlock: Hierarchical and partitioning algorithms of blocks of variables
- cluster: ”Finding Groups in Data”: Cluster Analysis Extended Rousseeuw et al.
- clusterability: Performs Tests for Cluster Tendency of a Data Set
- ClusterBootstrap: Analyze Clustered Data with Generalized Linear Models using the Cluster Bootstrap
- Clustering: Techniques for Evaluating Clustering
- clusterSEs: Calculate Cluster-Robust p-Values and Confidence Intervals
- ClusterR: Gaussian Mixture Models, K-Means, Mini-Batch-Kmeans, K-Medoids and Affinity Propagation
    Clustering
- clusterSim: Searching for Optimal Clustering Procedure for a Data Set
- clustrd: Methods for Joint Dimension Reduction and Clustering
- clustree: Visualise Clusterings at Different Resolutions
- clValid: Validation of Clustering Results
- cmbClust: Conditional Mixture Modeling and Model-Based Clustering
- Ckmeans.1d.dp: Optimal, Fast, and Reproducible Univariate Clustering
- diceR: Diverse Cluster Ensemble in R
- dtwclust: Time Series Clustering Along with Optimizations for the Dynamic Time Warping Distance


- evclust: Evidential Clustering
- fastcluster: Fast Hierarchical Clustering Routines for R and ’Python’
- fastkmedoids: Faster K-Medoids Clustering Algorithms: FastPAM, FastCLARA, FastCLARANS
- FCPS: Fundamental Clustering Problems Suite
- flexclust: Flexible Cluster Algorithms
- fpc: Flexible Procedures for Clustering
- genie: Fast, Robust, and Outlier Resistant Hierarchical Clustering
- genieclust: The Genie++ Hierarchical Clustering Algorithm with Noise Points Detection
- heatmaply: Interactive Cluster Heat Maps Using ’plotly’ and ’ggplot2’
- HierPortfolios: Hierarchical Clustering-Based Portfolio Allocation Strategies
- htestClust: Reweighted Marginal Hypothesis Tests for Clustered Data
- kselection: Selection of K in K-Means Clustering
- l1spectral: An L1-Version of the Spectral Clustering
- leaderCluster: Leader Clustering Algorithm
- LearnClust: Learning Hierarchical Clustering Algorithms
- MatTransMix: Clustering with Matrix Gaussian and Matrix Transformation Mixture Models
- mclust: Gaussian Mixture Modelling for Model-Based Clustering, Classification, and Density Estimation
- mclustcomp: Measures for Comparing Clusters
- mdendro: Extended Agglomerative Hierarchical Clustering
- Mercator: Clustering and Visualizing Distance Matrices
- MixGHD: Model Based Clustering, Classification and Discriminant Analysis Using the Mixture of Generalized
    Hyperbolic Distributions
- MixSim: Simulating Data to Study Performance of Clustering Algorithms
- mixSPE: Mixtures of Power Exponential and Skew Power Exponential Distributions for Use in Model-Based
    Clustering and Classification
- mixture: Mixture Models for Clustering and Classification
- MKMeans: A Modern K-Means (MKMeans) Clustering Algorithm
- mlr3cluster: Cluster Extension for ’mlr3’
- motifcluster: Motif-Based Spectral Clustering of Weighted Directed Networks
- MSclust: Multiple-Scaled Clustering
- mstknnclust: MST-kNN Clustering Algorithm
- NNS: Nonlinear nonparametric statistics using partial moments
- ProjectionBasedClustering: Projection Based Clustering
- protoclust: Hierarchical Clustering with Prototypes


- pytorch_cluster: PyTorch Extension Library of Optimized Graph Cluster Algorithms
- QuClu: Quantile-Based Clustering Algorithms
- rebmix: Finite Mixture Modeling, Clustering & Classification
- RCTS: Clustering Time Series While Resisting Outliers
- RMBC: Robust Model Based Clustering
- sClust: R Toolbox for Unsupervised Spectral Clustering
- sigclust: Statistical Significance of Clustering
- SLBDD: Statistical Learning for Big Dependent Data
- Spectrum: Fast Adaptive Spectral Clustering for Single and Multi-View Data
- T4cluster: Tools for Cluster Analysis
- tclust: Robust Trimmed Clustering
- tglkmeans: Efficient Implementation of K-Means++ Algorithm
- TSclust: Time Series Clustering Utilities
- vimpclust: Variable Importance in Clustering

### 7.8 Coding utilities and frameworks.

**Python software implementations**

List of packages and/or codes and/or frameworks and/or links:

- Algviz is an algorithm visualization tool for your Python code
- asteval: minimalistic evaluator of python expression using ast module
- autoflake: Removes unused imports and unused variables as reported by pyflakes
- autopep8: automatically formats Python code to conform to the PEP 8 style guide
- autoray: Write numeric code that automatically works with any numpy-ish libraries
- bandit: find common security issues in Python code
- birdseye: Graphical debugger to view the values of all evaluated expressions
- black: uncompromising Python code formatter
- BLUE: The slightly less uncompromising Python code formatter
- Bowler: Safe code refactoring by Facebook for modern Python
- Comprehensive Python Cheatsheet
- conda-deps: Generate conda environment files from Python and R source code
- Crashtest is a Python library that makes exceptions handling and inspection easier.
- darker: Apply black reformatting to Python files only in regions changed since a given commit
- enum_tools: Tools to expand Python’s enum module.
- erdantic: tool for drawing entity relationship diagrams (ERDs) for Python data model classes.


- flake8: glues together pycodestyle, pyflakes, mccabe, and third-party plugins to check the style and quality of
    code
- flake8-black: flake8 plugin to run black for checking Python coding style
- friendly: replaces standard tracebacks by something easier to understand
- Hatch is a modern, extensible Python project manager.
- icecream: Never use print() to debug again
- ipdb: exports functions to access the IPython debugger
- isort: utility / library to sort imports
- jedi: autocompletion, static analysis and refactoring library
- jsonschema: implementation of the JSON Schema specification for Python
- kedro: framework for creating reproducible, maintainable and modular data science code
- kedro-viz: Visualise your Kedro data and machine-learning pipelines and track your experiments.
- libfyaml: Fully feature complete YAML parser and emitter
- luddite: Checks for out-of-date package versions
- makepackage: easy packaging of Python code
- mamba: Fast Cross-Platform Package Manager (reimplementation of the conda package manager in C++)
- memray: memory profiler for Python
- metaflow: build and manage real-life data science projects
- mkdocs: Project documentation with Markdown
- mkdocs-material: Technical documentation that just works
- MonkeyType: toolkit by Instagram to generate static type annotations by collecting runtime types
- Monty: supplementary useful functions for Python that are not part of the standard library
- mypy: Optional static typing for Python
- nptyping: Type hints for Numpy
- numpydoc: Numpy’s Sphinx extensions
- pdbpp: a drop-in replacement for pdb (the Python debugger)
- PlantUML: Generate UML diagram from textual description
- poetry: dependency management and packaging made easy
- Pretty_Errors: Prettify Python exception output to make it legible
- prospector: Inspects source files and provides information about type and location of classes, methods
- ptvsd: debugger package by Microsoft for use with Visual Studio and Visual Studio Code
- pudb: Full-screen console debugger for Python
- pyan: Static call graph generator
- pycodestyle: Simple Python style checker


- pydantic: Data parsing and validation using Python type hints
- pyDeprecate: tooling for marking deprecated functions or classes and re-routing to the new successors’ in-
    stance.
- pyflakes: checks Python source files for errors
- pylint: static code analysis tool
- pyquickhelper: automation of many things
- pyre: framework for building scientific applications in Python
- pyre-check: Performant type-checking toolkit by Facebook
- pyright: Static type checker by Microsoft
- PyScaffold: Python project template generator with batteries included
- PySnooper: Never use print for debugging again
- py-spy: Sampling profiler for Python programs
- pytools: a big bag of things that are ”missing” from the Python standard library
- pytype: static type analyzer by Google
- radon: tool that computes various metrics from the source code
- rope: refactoring library
- scalene: high-performance, high-precision CPU, GPU, and memory profiler for Python
- sphinx: Sphinx documentation builder
- StrictYAML is a type-safe YAML parser that parses and validates a restricted subset of the YAML specification
- tryceratops: linter to prevent exception handling antipatterns in Python
- typeguard: Run-time type checker for Python
- TypePigeon: type converter focused on converting values between various Python data types.
- varname:Dark magics about variable names in python
- vulture: Find dead Python code
- xlwings: ibrary that makes it easy to call Python from Excel and vice versa
- yapf: formatter by Google for Python files
- yappi: Yet Another Python Profiler, but this time multithreading, asyncio and gevent aware.


**R software implementations**

List of packages and/or codes and/or frameworks and/or links:

- adaptalint: Check Code Style Painlessly
- baguette: Efficient Model Functions for Bagging
- box: Write Reusable, Composable and Modular R Code
- butcher: Model Butcher: axe components of fitted model objects and help reduce the size of model objects
    saved to disk
- cartbonate: Create beautiful images of source code using ’carbon.js
- checkmate: Fast and Versatile Argument Checks
- checkpoint: Install Packages from Snapshots on the Checkpoint Server for Reproducibility
- cleanr: Helps You to Code Cleaner
- delayed: A Framework for Parallelizing Dependent Tasks
- goodpractice: Advice on R Package Building
- hardhat: Construct Modeling Packages
- IRdisplay: ’Jupyter’ Display Machinery
- IRkernel: Native R Kernel for the ’Jupyter Notebook’
- jetpack: A Friendly Package Manager
- leprechaun: Create Simple ’Shiny’ Applications as Packages
- lintr: A ’Linter’ for R Code
- lvec: Out of Memory Vectors
- memuse: Memory Estimation Utilities
- metaflow: build and manage real-life data science projects
- miniCRAN: Create a Mini Version of CRAN Containing Only Selected Packages
- mongolite: Fast and Simple ’MongoDB’ Client for R
- packager: Create, Build and Maintain Packages
- parsnip: A Common API to Modeling and Analysis Functions
- prettifyAddins: ’RStudio’ Addins to Prettify ’JavaScript’, ’C++’, ’Python’, and More
- R6: Encapsulated Classes with Reference Semantics
- R6P: Design Patterns in R
- recipes: Preprocessing and Feature Engineering Steps for Modeling
- renv: Project Environments
- rhino: A Framework for Enterprise Shiny Applications
- roxut: Document Unit Tests Roxygen-Style
- roxygen2: In-Line Documentation for R


- rstudio.prefs: Set ’RStudio’ Preferences
- tidymodules: obust framework for developing ‘Shiny’ modules based on R6 classes which should facilitates
    inter-modules communication.
- waldo: Find Differences Between R Objects
- vetiver: Version, Share, Deploy, and Monitor Models
- workflows: Modeling Workflows
- workflowsets: Create a Collection of ’tidymodels’ Workflows

### 7.9 Computational performance.

**Python software implementations**

List of packages and/or codes and/or frameworks and/or links:

- Aesara: definie, optimize, and efficiently evaluate mathematical expressions involving multi-dimensional ar-
    rays.
- arctic: High performance datastore by Man Group for time series and tick data
- bottleneck: Fast NumPy array functions written in C
- Dask: Parallel computing with task scheduling
- Dask-ML provides scalable machine learning in Python using Dask alongside popular machine learning libraries
- datatable: library for fast multi-threaded data manipulation and munging
- fairscale: PyTorch extensions for high performance and large scale training.
- fastcore: Python supercharged for the fastai library
- hypre: high performance preconditioners
- jax: automatically differentiate native Python and NumPy functions
- modin: ake your pandas code run faster by changing one line of code
- multiprocess: better multiprocessing and multithreading in python
- numexpr: Fast numerical expression evaluator for NumPy
- PandaPy: speed of NumPy and the usability of Pandas but much faster
- pandarallel: parallelize Pandas operations on all available CPUs
- pandasvault:Advanced Pandas Vault - Utilities, Functions and Snippets
- polars: Fast multi-threaded DataFrame library
- ppft: distributed and parallel python
- PyArma: Linear algebra library for Python
- PyArmadillo: an alternative approach to linear algebra in Python
- pyperf: Toolkit to run Python benchmarks
- pyperformance: Python Performance Benchmark Suite
- py-spy: Sampling profiler for Python programs


- scalene: high-performance, high-precision CPU, GPU, and memory profiler for Python
- swifter: efficiently applies any function to a pandas dataframe or series in the fastest available manner
- tempeh is a framework to TEst Machine learning PErformance exHaustively which includes tracking memory
    usage and run time.

**R software implementations**

List of packages and/or codes and/or frameworks and/or links:

- collapse: Advanced and Fast Data Transformation
- dataPreparation: Automated Data Preparation
- delayed: A Framework for Parallelizing Dependent Tasks
- dplyr: A Grammar of Data Manipulation
- MatrixStats: Methods that Apply to Rows and Columns of Matrices (and to Vectors)
- mirai: Minimalist Async Evaluation Framework for R
- purrr: Functional Programming Tools
- tidyverse: set of packages that work in harmony because they share common data representations and ’API’
    design
- timetk: A Tool Kit for Working with Time Series in R
- tibble: Simple Data Frames
- tidytidbits: A Collection of Tools and Helpers Extending the Tidyverse
- tsibble: Tidy Temporal Data Frames and Tools

### 7.10 Containers, projects, pipelines and deployment

**Python software implementations**

List of packages and/or codes and/or frameworks and/or links:

- Driblet - Google Cloud based ML pipeline by Google
- MLflow: A Machine Learning Lifecycle Platform
- metaflow: Python/R library by Netflix to build and manage real-life data science projects
- mlflow: Interface to ’MLflow’
- mlxtend: extension and helper modules for data analysis and machine learning libraries
- NNI: toolkit by Microsoft to help users automate Feature Engineering, Neural Architecture Search, Hyperpa-
    rameter Tuning and Model Compression
- petastorm: toolkit by Uber for single machine or distributed training and evaluation of deep learning models
    (Tensorflow, Pytorch, and PySpark) from datasets in Apache Parquet format
- pipelines: Machine Learning Pipelines for Kubeflow
- Prefect: second-generation dataflow coordination and orchestration platform
- PyTorch Lightning: The lightweight PyTorch wrapper for high performance AI research
- Tango: toolkit by Allen Institute of Articial Intelligence for choreographing machine learning research


**R software implementations**

List of packages and/or codes and/or frameworks and/or links:

- DriveML: Self-Drive Machine Learning Projects
- metaflow: Python/R library by Netflix to build and manage real-life data science projects
- mlflow: Interface to ’MLflow’

### 7.11 Covariances, correlations and volatilities.

**Python software implementations**

List of packages and/or codes and/or frameworks and/or links:

- numpy: scientific computing
- precise: online covariance and precision forecasting, portfolios, and model ensembles
- PyPortfolioOpt: Financial portfolio optimization
- sklearn.covariance: covariance estimation in scikit-learn
- statsmodels: statistical modeling and econometrics

**R software implementations**

List of packages and/or codes and/or frameworks and/or links:

- bahc: Filter Covariance and Correlation Matrices with Bootstrapped-Averaged Hierarchical Ansatz
- BBcor: Bayesian Bootstrapping Correlations
- BEKKs: Multivariate Conditional Volatility Modelling and Forecasting
- BSCOV: Detection of Multiple Structural Breaks in Large Covariance Matrices
- clubSandwich: Cluster-Robust (Sandwich) Variance Estimators with Small-Sample Corrections
- cocor: Comparing Correlations
- corpcor: Efficient Estimation of Covariance and (Partial) Correlation
- correlation: Methods for Correlation Analysis
- corx: Create and Format Correlation Matrices
- CovTools: Statistical Tools for Covariance Analysis
- cvCovEst: Cross-Validated Covariance Matrix Estimation
- dcortools: Providing Fast and Flexible Functions for Distance Correlation Analysis
- dCovTS: Distance Covariance and Correlation for Time Series Analysis
- fitHeavyTail: Mean and Covariance Matrix Estimation under Heavy Tails
- FRCC: Fast Regularized Canonical Correlation Analysis
- gencor: Generate Customized Correlation Matrices
- generalCorr: Generalized Correlations, Causal Paths and Portfolio Selection
- mashr: Multivariate Adaptive Shrinkage


- MatrixCorrelation: Matrix Correlation Coefficients
- MTS: All-Purpose Toolkit for Analyzing Multivariate Time Series (MTS) and Estimating Multivariate Volatil-
    ity Models
- NonParRolCor: a Non-Parametric Statistical Significance Test for Rolling Window Correlation
- NNS: Nonlinear nonparametric statistics using partial moments
- rags2ridges: Ridge Estimation of Precision Matrices from High-Dimensional Data
- rmcorr: Repeated Measures Correlation
- robcor: Robust Correlations
- robustcov: Collection of Robust Covariance and (Sparse) Precision Matrix Estimators
- RSC: Robust and Sparse Correlation Matrix
- sandwich: Robust Covariance Matrix Estimators
- WGCNA: Weighted Correlation Network Analysis

### 7.12 Data analysis and exploration.

**Python software implementations**

List of packages and/or codes and/or frameworks and/or links:

- AutoViz: Automatically Visualize any dataset, any size with a single line of code.
- daal4py: simplified API to Intel oneAPI Data Analytics Library
- DeepGraph: scalable, general-purpose data analysis with Pandas-based Networks
- D-tale:Visualizer by Man Group for pandas data structures
- dython: Data analysis tools
- empiricaldist: empirical distribution functions
- hyperspy: Multidimensional data analysis
- Lux: automate the visualization and data analysis process
- mlxtend: extension and helper modules for Python’s data analysis and machine learning libraries.
- numericalunits: Units and dimensional analysis compatible with everything
- Orange: Interactive data analysis
- pandas-profiling: Create HTML profiling reports from pandas DataFrame objects
- PyApprox: high-dimensional approximation and uncertainty quantification
- sweetviz: Visualize and compare datasets, target values and associations


**R software implementations**

List of packages and/or codes and/or frameworks and/or links:

- checkmate: Fast and Versatile Argument Checks
- collapse: Advanced and Fast Data Transformation
- datacleanr: Interactive and Reproducible Data Cleaning
- DataEditR: An Interactive Editor for Viewing, Entering, Filtering & Editing Data
- DataExplorer: Automate Data Exploration and Treatment
- datamods: Modules to Import and Manipulate Data in ’Shiny’
- dataprep: Efficient and Flexible Data Preprocessing Tools
- DataVisualizations: Visualizations of High-Dimensional Data
- datawizard: Easy Data Wrangling
- DescTools: Tools for Descriptive Statistics
- dimensio: Multivariate Data Analysis
- discoveR: Exploratory Data Analysis System
- dlookr: Tools for Data Diagnosis, Exploration, Transformation
- EasyDescribe: A Convenient Way of Descriptive Statistics
- esquisse: Explore and Visualize Your Data Interactively
- explor: Interactive Interfaces for Results Exploration
- exploratory: A Tool for Large-Scale Exploratory Analyses
- explore: Simplifies Exploratory Data Analysis
- factoextra: extract and visualize the output of multivariate data analyses, including ’PCA’ (Principal Compo-
    nent Analysis), ’CA’ (Correspondence Analysis), ’MCA’ (Multiple Correspondence Analysis), ’FAMD’ (Factor
    Analysis of Mixed Data), ’MFA’ (Multiple Factor Analysis) and ’HMFA’ (Hierarchical Multiple Factor Anal-
    ysis)
- FactoInvestigate: Automatic Description of Factorial Analysis
- FactoMineR: Multivariate Exploratory Data Analysis and Data Mining
- ggESDA: Exploratory Symbolic Data Analysis with ’ggplot2’
- HDTSA: High Dimensional Time Series Analysis Tools
- infotheo: Information-Theoretic Measures
- kfa: K-Fold Cross Validation for Factor Analysis
- MazamaRollUtils: Efficient Rolling Functions
- mmpca: Integrative Analysis of Several Related Data Matrices
- praznik: Tools for Information-Based Feature Selection and Scoring
- predictoR: Predictive Data Analysis System


- rigr: Regression, Inference, and General Data Analysis Tools in R
- robCompositions: Compositional Data Analysis
- rrcov: Scalable Robust Estimators with High Breakdown Point
- SmartEDA: Summarize and Explore the Data
- statsExpressions: Tidy Dataframes and Expressions with Statistical Details
- Statsomat: Shiny Apps for Automated Data Analysis and Automated Interpretation
- thinkr: Tools for Cleaning Up Messy Files
- tswge: Time Series for Data Science.Accompanies the texts Time Series for Data Science and Applied Time
    Series Analysis with R,
- validata: Validate Data Frames
- validate: Data Validation Infrastructure
- validatetools: Checking and Simplifying Validation Rule Sets
- wrangle: A Systematic Data Wrangling Idiom

### 7.13 Data augmentation, scenario generation and synthetic time series.

**Collections of resources**

List of links:

- Synthetic data generation by Van Der Schaar Lab
- Useful data augmentation resources

**Python software implementations**

List of packages and/or codes and/or frameworks and/or links:

- agots: Anomaly Generator on Time Series
- benchmark_VAE: Unifying Generative Autoencoder implementations in Python
- Copulas: model multivariate data using copulas
- CTGAN: Conditional GAN for Tabular Data
- COMET Flows: Towards Generative Modeling of Multivariate Extremes and Tail Dependence
- DataGeneration: Synthetic financial correlation matrix and time series generation
- DECAF: Generating Fair Synthetic Data Using Causally-Aware Generative Networks
- DeepEcho: Synthetic Data Generation for mixed-type, multivariate time series
- deltapy: Tabular Data Augmentation
- extremeIndex: Forecast Verification for Extreme Events
- ixmp: platform for integrated and cross-cutting scenario analysis
- MLlforHealthLab: Machine Learning and Artificial Intelligence for Medicine
- pydantic-factories: Pydantic based mock data generation


- pythae: Unifying Generative Autoencoder implementations in Python
- RDT: Reversible Data Transforms to reproduce realistic data
- scattering_covariance: analysis and generation of time series
- SDMetrics: Metrics for Synthetic Data Generation Projects
- SDGym: Benchmarking synthetic data generation methods
- SDV: Synthetic Data Generation for tabular, relational and time series data
- SignalFilters: Signal Filtering and Generation of Synthetic Time-Series
- snorkel: system for quickly generating training data with weak supervision
- synthia: Multidimensional synthetic data generation in Python
- TGAN: Generative adversarial training for generating synthetic tabular data
- TimeGAN: Time-series Generative Adversarial Networks
- time-series-generator: Time Series Generator
- TimeSynth: Synthetic Time Series Generation
- tsaug: time series augmentation
- tsBNgen: Generate Time Series Data Based on an Arbitrary Bayesian Network Structure
- tsGAN: Time-series Generative Adversarial Networks
- ydata-synthetic: Synthetic structured data generators

**R software implementations**

List of packages and/or codes and/or frameworks and/or links:

- anySim: Simulation of Non-Gaussian Correlated Random Variables, Stochastic Processes and Random Fields
- bootComb: Combine Parameter Estimates via Parametric Bootstrap
- conjurer: A Parametric Method for Generating Synthetic Data
- covsim: VITA, IG and PLSIM Simulation for Given Covariance and Marginals
- fabricatr: Imagine Your Data Before You Collect It
- fwb: Fractional Weighted Bootstrap
- gencor: Generate Customized Correlation Matrices
- gratis: Generating Time Series with Diverse and Controllable Characteristics
- meboot: Maximum Entropy Bootstrap for Time Series
- metamer: Create Data with Identical Statistics
- missMethods: Methods for Missing Data
- MixSim: Simulating Data to Study Performance of Clustering Algorithms
- modeltime.resample: Resampling Tools for Time Series Forecasting
- MonteCarlo: Automatic Parallelized Monte Carlo Simulations


- MSCMT: Multivariate Synthetic Control Method Using Time Series
- mvlognCorrEst: Sampling from Multivariate Lognormal Distributions and Estimating Correlations from Un-
    complete Correlation Matrix
- naive: Empirical Extrapolation of Time Feature Patterns
- RMT4DS: Computation of Random Matrix Models
- rsample: General Resampling Infrastructure
- segen: Sequence Generalization Through Similarity Network
- SimJoint: Simulate Joint Distribution
- simmer: Discrete-Event Simulation for R
- simts: Time Series Analysis Tools
- spooky: Time Feature Extrapolation Using Spectral Analysis and Jack-Knife Resampling
- Synth: Synthetic Control Group Method for Comparative Case Studies
- synthesis: Generate Synthetic Data from Statistical Models
- tetragon: Automatic Sequence Prediction by Expansion of the Distance Matrix
- TidyDensity: Functions for Tidy Analysis and Generation of Random Data
- tscopula: Time Series Copula Models

### 7.14 Data cleaning, preparation and validation

**Python software implementations**

List of packages and/or codes and/or frameworks and/or links:

- cerberus: Lightweight, extensible data validation library
- datatest: Tools for test driven data-wrangling and data validation
- doubtlab: Doubt your data, find bad labels
- framework: Data management framework for Python that provides functionality to describe, extract, validate,
    and transform tabular data
- formencode: validation and form generation
- pandera: perform data validation on dataframes
- pydantic: Data parsing and validation using Python type hints
- pyjanitor: Clean APIs for data cleaning. Python implementation of R package Janitor
- PyOptimus: framework for cleaning and pre-processing data in a distributed fashion
- scikit-learn: machine learning in Python
- schema: library for validating Python data structures
- serde: framework for defining, serializing, deserializing, and validating data structures
- typical: Fast, simple, & correct data-validation using Python 3 typing.
- validators: Python data validation for Humans


- Voluptuous: data validation library.
- validr: simple, fast, extensible python library for data validation
- wtforms: flexible forms validation and rendering library

**R software implementations**

List of packages and/or codes and/or frameworks and/or links:

- cleanTS: Testbench for Univariate Time Series Cleaning
- dataPreparation: Automated Data Preparation
- data.validator: Automatic Data Validation and Reporting
- datawizard: Easy Data Wrangling
- errorlocate: Locate Errors with Validation Rules
- pointblank: Data Validation and Organization of Metadata for Local and Remote Tables
- testdat: Data Unit Testing for R
- tsrobprep: Robust Preprocessing of Time Series Data
- validate: Data Validation Infrastructure
- validatetools: Checking and Simplifying Validation Rule Sets
- wrangle: A Systematic Data Wrangling Idiom

### 7.15 Data Imputation

**Python software implementations**

List of packages and/or codes and/or frameworks and/or links:

- AutoImpute: Imputation Methods
- Clairvoyance: a Unified, End-to-End AutoML Pipeline for Medical Time Series
- fancyimpute: Multivariate imputation and matrix completion algorithms
- HyperImpute: framework for prototyping and benchmarking imputation methods
- imputena: automated and customized treatment of missing values in datasets
- miceforest: Fast, Memory Efficient Imputation with LightGBM
- MissForestExtra: nonparametric imputation on missing values
- scikit-learn: machine learning in Python
- statsmodels: statistical modeling and econometrics
- tsai: time series tasks like classification, regression, forecasting, imputation


**R software implementations**

List of packages and/or codes and/or frameworks and/or links:

- Amelia: A Program for Missing Data
- CoImp: Copula Based Imputation Method
- deductive: Data Correction and Imputation Using Deductive Methods
- ggmice: Visualizations for ’mice’ with ’ggplot2’
- howManyImputations: Calculate How many Imputations are Needed for Multiple Imputation
- imputeFin: Imputation of Financial Time Series with Missing Values and/or Outliers
- imputeGeneric: Ease the Implementation of Imputation Methods
- imputeTestbench: Test Bench for the Comparison of Imputation Methods
- imputeTS: Time Series Missing Value Imputation
- Iscores: Proper Scoring Rules for Missing Value Imputation
- mdgc: Missing Data Imputation Using Gaussian Copulas
- mice: Multivariate Imputation by Chained Equations
- miceadds: Some Additional Multiple Imputation Functions, Especially for ’mice’
- miceafter: Data and Statistical Analyses after Multiple Imputation
- miceFast: Fast Imputations Using ’Rcpp’ and ’Armadillo’
- micemd: Multiple Imputation by Chained Equations with Multilevel Data
- misPRIME: Partial Replacement Imputation Estimation for Missing Covariates
- missMDA: Handling Missing Values with Multivariate Data Analysis
- missMethods: Methods for Missing Data
- missRanger: Fast Imputation of Missing Values
- mlim: Multiple Imputation with Automated Machine Learning
- NADIA: NA Data Imputation Algorithms
- naniar: Data Structures, Summaries, and Visualisations for Missing Data
- rego: Automatic Time Series Forecasting and Missing Value Imputation
- Rforestry: Random Forests, Linear Trees, and Gradient Boosting for Inference and Interpretability
- simputation: Simple Imputation
- SLBDD: Statistical Learning for Big Dependent Data
- smcfcs: Multiple Imputation of Covariates by Substantive Model Compatible Fully Conditional Specification
- univOutl: Detection of Univariate Outliers
- VIM: Visualization and Imputation of Missing Values
- yaImpute: Nearest Neighbor Observation Imputation and Evaluation Tools


### 7.16 Data regimes, states and changepoints: analysis and modeling.

**Collections of resources**

List of links:

- Classifying market regimes
- TCPD: toolkit by UK national institute for data science and artificial intelligence for Turing Change Point
    Dataset - A collection of time series for the evaluation and development of change point detection algorithms
- TCPDBench: toolkit by UK national institute for data science and artificial intelligence for Turing Change
    Point Detection Benchmark: An Extensive Benchmark Evaluation of Change Point Detection Algorithms on
    real-world data

**Python software implementations**

List of packages and/or codes and/or frameworks and/or links:

- changeforest: Random Forests for Change Point Detection
- deeptime: analysis of time series data including dimensionality reduction, clustering, and Markov model
    estimation
- greykite: flexible, intuitive and fast forecasting library
- HMMLearn: Hidden Markov Models in Python with scikit-learn like API
- kalmanfilter: Kalman Filter
- kats: tookit by Facebook for time series analysis and forecasting
- kimfilter: Rcpp’ implementation of the multivariate Kim filter, which combines the Kalman and Hamilton
    filters for state probability inference
- Merlion: A Machine Learning Framework for Time Series Intelligence by SalesForce
- msmtools: estimation and analysis of discrete state space Markov chains via Markov state models (MSM)
- PyEMMA: Emma’s Markov Model Algorithms
- pyGPCCA: Generalized Perron Cluster Cluster Analysis to coarse-grain reversible and non-reversible Markov
    state models.
- pyhsmm: Bayesian inference in HSMMs and HMMs
- pymc3-hmm: Hidden Markov models in PyMC3
- ruptures: change point detection
- SST: fast implementation of Singular Spectrum Transformation
- Stone-Soup: framework for the development and testing of tracking algorithms
- statsmodels: Markov switching models in statsmodels
- transitionMatrix: Statistical analysis and visualization of state transition phenomena
- tsmoothie: time-series smoothing and outlier detection


**R software implementations**

List of packages and/or codes and/or frameworks and/or links:

- BayesHMM: Full Bayesian Inference for Hidden Markov Models
- breakfast: Methods for Fast Multiple Change-Point Detection and Estimation
- BSCOV: Detection of Multiple Structural Breaks in Large Covariance Matrices
- ChangepointInference: Tools to test for a change in mean after changepoint detection
- changepoints: A Collection of Change-Point Detection Methods
- ChangePointTaylor: Identify Changes in Mean
- chngpt: Estimation and Hypothesis Testing for Threshold Regression
- cpss: Change-Point Detection by Sample-Splitting Methods
- crossvalidationCP: Cross-Validation for Change-Point Regression
- depmixS4: Dependent Mixture Models - Hidden Markov Models of GLMs and Other Distributions in S4
- dynr: Dynamic Models with Regime-Switching
- earlywarnings: Early Warning Signals Toolbox for Detecting Critical Transitions in Timeseries
- fabisearch: Change Point Detection in High-Dimensional Time Series Networks
- fHMM: Fitting Hidden Markov Models to Financial Data
- inflection: Finds the Inflection Point of a Curve
- InspectChangepoint: High-Dimensional Changepoint Estimation via Sparse Projection
- jcp: Joint Change Point Detection
- HMM: Hidden Markov Models
- hmm.discnp: Hidden Markov Models with Discrete Non-Parametric Observation Distributions
- hmmr: ”Mixture and Hidden Markov Models with R” Datasets and Example Code
- KFAS: Kalman Filter and Smoother for Exponential Family State Space Models
- ldhmm: Hidden Markov Model for Financial Time-Series Based on Lambda Distribution
- mHMMbayes: Multilevel Hidden Markov Models Using Bayesian Estimation
- MSGARCH: Markov-Switching GARCH Models
- MSTest: Hypothesis Testing for Markov Switching Models
- NHMSAR: Non-Homogeneous Markov Switching Autoregressive Models
- onlineBcp: Online Bayesian Methods for Change Point Analysis
- plotHMM: Plot Hidden Markov Models
- pomp: Statistical Inference for Partially Observed Markov Processes
- Rbeast: Bayesian Change-Point Detection and Time Series Decomposition
- RChest: Locating Distributional Changes in Highly Dependent Time Series


- robcp: Robust Change-Point Tests
- segmented: Regression Models with Break-Points / Change-Points Estimation
- seqHMM: Mixture Hidden Markov Models for Social Sequence Data and Other Multivariate, Multichannel
    Categorical Time Series
- trendchange: Innovative Trend Analysis and Time-Series Change Point Analysis
- tsDyn: Nonlinear Time Series Models with Regime Switching
- wbsts: Multiple Change-Point Detection for Nonstationary Time Series

### 7.17 Data structures, storage and serialization

**Python software implementations**

List of packages and/or codes and/or frameworks and/or links:

- addict: Python Dict
- anndata: package for handling annotated data matrices in memory and on disk
- arctic: High performance datastore by Man Group for time series and tick data
- cloudpickle: serialize Python constructs not supported by the default pickle module
- dataclassy is a reimplementation of data classes in Python
- datatable: fast multi-threaded data manipulation and munging
- dill: extends Python’s pickle module for serializing and deserializing python objects to the majority of the
    built-in python types.
- extendedjson: Easily extend JSON to encode and decode arbitrary Python objects
- framework: Data management framework for Python that provides functionality to describe, extract, validate,
    and transform tabular data
- MarketStore: DataFrame Server for Financial Timeseries Data
- marshmallow: lightweight library for converting complex objects to and from simple Python datatypes
- modin.pandas DataFrame is a parallel and distributed drop-in replacement for panda
- Mongita is to MongoDB as SQLite is to SQL
- mongo-arrow: Tools for using Apache Arrow with MongoDB
- multidict: multidict implementation
- Odo provides a uniform API for moving data between different formats
- pandas: data structures for data analysis, time series, and statistics
- pandasvault: Advanced Pandas Vault - Utilities, Functions and Snippets
- pickle: Python object serialization
- polars: Fast multi-threaded DataFrame library
- pyarrow: Python API for Apache Arrow, a language independent columnar memory format for flat and
    hierarchical data


- PyMongo - the Python driver for MongoDB
- PyStore: Fast data store for Pandas time-series data
- PyTables: package for managing hierarchical datasets
- rpy2-arrow: Share Apache Arrow datasets between Python and R
- serde: framework for defining, serializing, deserializing, and validating data structures
- sklearn-pandas: bridge between Scikit-Learn’s machine learning methods and pandas-style Data Frames
- sortedcontainers: Sorted Containers – Sorted List, Sorted Dict, Sorted Set
- sqlite: Persistent dict, backed by sqlite3 and pickle, multithread-safe.
- sparse: Sparse Multidimensional Arrays
- srsly: Modern high performance serialization utilities
- tablib: Module for Tabular Datasets in XLS, CSV, JSON, YAML,
- tabmat: Efficient matrix representations for working with tabular data
- TileDB: powerful engine for storing and accessing dense and sparse multi-dimensional arrays
- tidypandas: grammar of data manipulation for pandas inspired by tidyverse
- tinyarray: Tinyarrays are similar to NumPy arrays, but optimized to be much faster for small sizes
- TinyDB is a lightweight document oriented database optimized for your happiness
- tinyflux: iny time series database optimized for your happiness
- torcharrow: torch.Tensor-like DataFrame library by Facebook using Arrow as a common memory format
- ubermagtable: package for manipulating tabular data
- ultrajson: Ultra fast JSON decoder and encoder written in C with Python bindings
- Vector: arrays of 2D, 3D, and Lorentz vectors
- Woodwork is a Python library that provides robust methods for managing and communicating data typing
    information
- xarray: multidimensional labeled arrays and datasets
- xpandas: Universal 1d/2d data containers with Transformers functionality for data analysis

**R software implementations**

List of packages and/or codes and/or frameworks and/or links:

- arrow: Integration to Apache Arrow
- dibble: Dimensional Data Frames
- fst: Lightning Fast Serialization of Data Frames
- gluedown: Wrap Vectors in Markdown Formatting
- listdown: Create R Markdown from Lists
- motifcluster: Motif-Based Spectral Clustering of Weighted Directed Networks


- qs: Quick Serialization of R Objects
- RcppSimdJson: ’Rcpp’ Bindings for the ’simdjson’ Header-Only Library for ’JSON’ Parsing
- tibble: stricter checking and better formatting than the traditional data frame
- tibblify: Rectangle Nested Lists
- tidytable: Tidy Interface to ’data.table’
- tiledb: Universal Storage Engine for Sparse and Dense Multidimensional Arrays
- tsibble: Tidy Temporal Data Frames and Tools
- tsbox: Class-Agnostic Time Series
- vtreat: A Statistically Sound data.frame Processor/Conditioner

### 7.18 Dates and times

**Python software implementations**

List of packages and/or codes and/or frameworks and/or links:

- arrow: Better dates and times for Python
- dateparser: parser for human readable dates
- dateutil: Useful extensions to the standard Python datetime features
- orjson: Fast, correct Python JSON library supporting dataclasses, datetimes, and numpy
- parsedatetime: human-readable date/time strings
- pendulum: datatimes made easy
- Pyrsistent: Persistent/Functional/Immutable data structures
- python-dateutil: Useful extensions to the standard Python datetime features
- PyTime: operate datetime by string

**R software implementations**

List of packages and/or codes and/or frameworks and/or links:

- clock: Date-Time Types and Tools
- lubridate: Make Dealing with Dates a Little Easier
- qlcal: R Bindings to the Calendaring Functionality of ’QuantLib’
- tidyquant: Tidy Quantitative Financial Analysis
- timechange: Efficient Manipulation of Date-Times
- timetk: A Tool Kit for Working with Time Series in R
- tsbox: Class-Agnostic Time Series
- TSrepr: Time Series Representations
- xts: eXtensible Time Series
- zoo: S3 Infrastructure for Regular and Irregular Time Series


### 7.19 Dimensionality reduction

**Python**

List of packages/codes/frameworks/links:

- abess: Fast Best-Subset Selection Library
- deeptime: analysis of time series data including dimensionality reduction, clustering, and Markov model
    estimation
- direpack: State-of-the-Art Statistical Dimension Reduction Methods
- EZyRB: Easy Reduced Basis method ; performs a data-driven model order reduction for parametrized prob-
    lems exploiting the recent approaches.
- humap: Hierarchical Manifold Approximation and Projection (HUMAP) is a technique based on UMAP for
    hierarchical non-linear dimensionality reduction.
- pyFIt-SNE: FFT-accelerated Interpolation-based t-SNE (FIt-SNE)
- scikit-dimension: intrinsic dimension estimation
- scikit-learn: machine learning in Python
- (t-SNE: t-Distributed Stochastic Neighbor Embedding (t-SNE) for dimensionality reduction
- UMAP: Uniform Manifold Approximation and Projection

**R software implementations**

List of packages and/or codes and/or frameworks and/or links:

- abess: Fast Best-Subset Selection Library
- abundant: High-Dimensional Principal Fitted Components and Abundant Regression
- bayesdfa: Bayesian Dynamic Factor Analysis (DFA) with ’Stan’
- clustrd: Methods for Joint Dimension Reduction and Clustering
- dimRed: A Framework for Dimensionality Reduction
- DLPCA: The Distributed Local PCA Algorithm
- dobin: Dimension Reduction for Outlier Detection
- dyndimred: Dimensionality Reduction Methods in a Common Format
- EMD: Empirical Mode Decomposition and Hilbert Spectral Analysis
- ForeCA: Forecastable Component Analysis
- freqdom: Frequency Domain Based Analysis: Dynamic PCA
- ica: Independent Component Analysis
- ICtest: Estimating and Testing the Number of Interesting Components in Linear Dimension Reduction
- prinvars: Principal Variables (methods for reducing the number of features within a data set)
- quantdr: Dimension Reduction Techniques for Conditional Quantiles
- rrpack: Reduced-Rank Regression


- Rdimtools: Dimension Reduction and Estimation Methods
- RSpectra: Solvers for Large-Scale Eigenvalue and SVD Problems
- shrinkTVP: Efficient Bayesian Inference for Time-Varying Parameter Models with Shrinkage
- spcr: Sparse Principal Component Regression
- SuperPCA: Supervised Principal Component Analysis
- svd: Interfaces to Various State-of-Art SVD and Eigensolvers
- tapkee: tapkee: Wrapper for ’tapkee’ Dimension Reduction Library
- tidydr: Unify Dimensionality Reduction Results
- TSrepr: Time Series Representations (dimensionality reduction, preprocessing, feature extraction)
- umap: Uniform Manifold Approximation and Projection

### 7.20 Distances and Similarity.

**Python software implementations**

List of packages and/or codes and/or frameworks and/or links:

- DataGene: Identify How Similar TS Datasets Are to One Another
- dcor: Distance correlation and related E-statistics
- dtaidistance: Distance measures for time series
- dtw-python: comprehensive implementation of dynamic time warping (DTW) algorithms
- faiss: efficient similarity search and clustering of dense vectors
- FLANN: Fast Library for Approximate Nearest Neighbors
- GraKeL: scikit-learn compatible library for graph kernels
- khiva-python: Python binding for Khiva library for time series analytics
- mass-ts: MASS (Mueen’s Algorithm for Similarity Search)
- MatrixProfile: ime series data mining tasks utilizing matrix profile
- matrixprofile-ts: detect patterns and anomalies in massive datasets using Matrix Profile
- netrd: library for network {reconstruction, distances, dynamics}
- POT : Python Optimal Transport
- PyMD: imple but general framework for embedding, called Minimum-Distortion Embedding (MDE), for finite
    sets of items, such as images, biological cells, nodes in a network, or any other abstract object
- PySCAMP: SCAlable Matrix Profile
- seriesdistancematrix: implements the Series Distance Matrix framework, a flexible component-based frame-
    work that bundles various Matrix Profile related techniques
- sktime: unified framework for machine learning with time series by UK national institute for data science and
    artificial intelligence
- Stone-Soup: framework for the development and testing of tracking algorithms


- stumpy: variety of time series data mining tasks
- tidydr: Unify Dimensionality Reduction Results
- timesmash: Quantifier of universal similarity amongst arbitrary data streams without a priori knowledge,
    features, or training
- wildboar: Time series learning

**R software implementations**

List of packages and/or codes and/or frameworks and/or links:

- dispRity: Measuring Disparity (multidimensional space occupancy)
- Distance: Distance Sampling Detection Function and Abundance Estimation
- distantia: Assessing Dissimilarity Between Multivariate Time Series
- dtw: Dynamic Time Warping Algorithms
- dtwclust: Time Series Clustering Along with Optimizations for the Dynamic Time Warping Distance
- fICA: Classical, Reloaded and Adaptive FastICA Algorithms
- gdm: Generalized Dissimilarity Modeling
- IncDTW: Incremental Calculation of Dynamic Time Warping
- KernelKnn: Extends the simple k-nearest neighbors algorithm by incorporating numerous kernel functions
    and a variety of distance metrics
- MatrixCorrelation: Matrix Correlation Coefficients
- mclustcomp: Measures for Comparing Clusters
- Mercator: Clustering and Visualizing Distance Matrices
- philentropy: Similarity and Distance Quantification Between Probability Functions
- proxy: Distance and Similarity Measures
- segen: Sequence Generalization Through Similarity Network
- tetragon: Automatic Sequence Prediction by Expansion of the Distance Matrix
- TSclust: set of measures of dissimilarity between time series to perform time series clustering
- TSdist: Distance Measures for Time Series Data
- tsmp: UCR Matrix Profile Algorithm
- VPdtw: Variable Penalty Dynamic Time Warping

### 7.21 ESG and Impact Investing.

**Python software implementations**

List of packages and/or codes and/or frameworks and/or links:

- ESG AI: ESG scoring as an automatic, data-driven process
- ESG-BERT: Domain Specific BERT Model for Text Mining in Sustainable Investing


**R software implementations**

List of packages and/or codes and/or frameworks and/or links:

- EnvStats: Package for Environmental Statistics, Including US EPA Guidance
- ESGBoost: ESG and ECHO-based model for smart investing
- gfer: Green Finance and Environmental Risk
- text2sdg: Detecting UN Sustainable Development Goals in Text

### 7.22 Explainability, Interpretability, Fairness, Data Privacy

**Python software implementations**

List of packages and/or codes and/or frameworks and/or links:

- AIF360: comprehensive set of fairness metrics for datasets and machine learning models, explanations for
    these metrics, and algorithms to mitigate bias in datasets and models
- captum: Model interpretability and understanding for PyTorch
- CrypTen: framework for Privacy Preserving Machine Learning
- Dice-ML: Generate Diverse Counterfactual Explanations for any machine learning model
- DoWhy: toolkit by Microsoft for causal inference that supports explicit modeling and testing of causal as-
    sumptions
- Interpret: Fit interpretable models by Microsoft. Explain blackbox machine learning
- Interpretability dashboard, for understanding model predictions
- Lime: Local Interpretable Model-Agnostic Explanations for machine learning classifiers
- Lucid: neural network interpretability
- PyExplainer: A Local Rule-Based Model-Agnostic Technique
- Skater: Model Interpretation/Explanations
- transformers-interpret: Model explainability that works seamlessly with transformers
- XAI: eXplainability toolbox for machine learning
- Xplique: toolkit dedicated to explainability, currently based on Tensorflow

**R software implementations**

List of packages and/or codes and/or frameworks and/or links:

- DALEX: moDel Agnostic Language for Exploration and eXplanation
- distillML: Model Distillation and Interpretability Methods for Machine Learning Models
- fairml: Fair Models in Machine Learning
- iml: Interpretable Machine Learning
- interpret: Fit Interpretable Machine Learning Models
- modelDown: Make Static HTML Website for Predictive Models
- modelStudio: Interactive Studio for Explanatory Model Analysis


- pdp: Partial Dependence Plots
- pre: Prediction Rule Ensembles
- Rforestry: Random Forests, Linear Trees, and Gradient Boosting for Inference and Interpretability
- rSAFE: Surrogate-Assisted Feature Extraction
- sensitivity: Global Sensitivity Analysis of Model Outputs
- triplot: Explaining Correlated Features in Machine Learning Models
- yhat: Interpreting Regression Effects

### 7.23 Features for time series.

**Python software implementations**

List of packages and/or codes and/or frameworks and/or links:

- cesium: Platform for Time Series Inference
- Clairvoyance: a Unified, End-to-End AutoML Pipeline for Medical Time Series
- FeatureTools: automated feature engineering
- Featurewiz: advanced feature engineering strategies
- khiva-python: Python binding for Khiva library for time series analytics
- mne-features: MNE-Features software for extracting features from multivariate time series
- scikit-learn: machine learning in Python
- seglearn: integrated pipeline for segmentation, feature extraction, feature processing, and final estimator
- tsfeatures: Calculates various features from time series data
- tsfel: extract features from time series
- tsflex: Flexible time series feature extraction & processing
- tsfresh: extract features from time series

**R software implementations**

List of packages and/or codes and/or frameworks and/or links:

- autostsm: Automatic Structural Time Series Models
- bfast: Breaks for Additive Season and Trend
- entropy: Estimation of Entropy, Mutual Information and Related Quantities
- feasts: Feature Extraction and Statistics for Time Series
- fsMTS: Feature Selection for Multivariate Time Series
- naive: Empirical Extrapolation of Time Feature Patterns
- plsVarSel: Variable Selection in Partial Least Squares
- MDFS: MultiDimensional Feature Selection
- Rcatch22: Calculation of 22 CAnonical Time-Series CHaracteristics


- theft: Tools for Handling Extraction of Features from Time Series
- tsfeatures: Time Series Feature Extraction
- TSrepr: Time Series Representations (dimensionality reduction, preprocessing, feature extraction)

### 7.24 Filtering and spectral analysis for time series

**Python software implementations**

List of packages and/or codes and/or frameworks and/or links:

- FilterPy: Kalman filtering and optimal estimation library
- mkl_fft: NumPy-based Python interface to Intel (R) MKL FFT functionality
- pyfilter: Particle filtering and sequential parameter inference
- PyWavelets: Wavelet Transforms in Python
- simdkalman: Kalman filters vectorized as Single Instruction, Multiple Data
- Stone-Soup: framework for the development and testing of tracking algorithms

**R software implementations**

List of packages and/or codes and/or frameworks and/or links:

- ASSA: Applied Singular Spectrum Analysis (ASSA)
- beyondWhittle: Bayesian Spectral Inference for Stationary Time Series
- BMAmevt: Multivariate Extremes: Bayesian Estimation of the Spectral Measure
- bsamGP: Bayesian Spectral Analysis Models using Gaussian Process Priors
- bspec: Bayesian Spectral Inference
- cohortBuilder: Data Source Agnostic Filtering Tools
- EMD: Empirical Mode Decomposition and Hilbert Spectral Analysis
- FKF: Fast Kalman Filter
- FKF.SP: Fast Kalman Filtering Through Sequential Processing
- frequencyConnectedness: Spectral Decomposition of Connectedness Measures
- kalmanfilter: Kalman Filter
- KFAS: Kalman Filter and Smoother for Exponential Family State Space Models
- kimfilter: Rcpp’ implementation of the multivariate Kim filter, which combines the Kalman and Hamilton
    filters for state probability inference
- LMfilteR: Filter Methods for Parameter Estimation in Linear and Non Linear Regression Models
- mlr3filters: Filter Based Feature Selection for ’mlr3’
- multitaper: Spectral Analysis Tools using the Multitaper Method
- neverhpfilter: An Alternative to the Hodrick-Prescott Filter
- praznik: Tools for Information-Based Feature Selection and Scoring


- psd: Adaptive, Sine-Multitaper Power Spectral Density and Cross Spectrum Estimation
- psdr: Use Time Series to Generate and Compare Power Spectral Density
- quantspec: Quantile-Based Spectral Analysis of Time Series
- Rfssa: Functional Singular Spectrum Analysis
- rhosa: Higher-Order Spectral Analysis
- robfilter: Robust Time Series Filters
- RobKF: Innovative and/or Additive Outlier Robust Kalman Filtering
- RSpectra: Solvers for Large-Scale Eigenvalue and SVD Problems
- Rssa: A Collection of Methods for Singular Spectrum Analysis
- Rwave: Time-Frequency Analysis of 1-D Signals
- SLBDD: Statistical Learning for Big Dependent Data
- spectral: Common Methods of Spectral Data Analysis
- Spectrum: Fast Adaptive Spectral Clustering for Single and Multi-View Data
- spooky: Time Feature Extrapolation Using Spectral Analysis and Jack-Knife Resampling
- wavethresh: Wavelets Statistics and Transforms

### 7.25 Forecasting time series.

**Collections of resources**

List of links:

- Popular Python Time Series Packages
- State of the art research (with codes) on time series forecasting

**Python software implementations**

List of packages and/or codes and/or frameworks and/or links:

- anticipy: time series forecasting
- atspy: Automated Time Series Models in Python
- Autoformer: Decomposition Transformers with Auto-Correlation for Long-Term Series Forecasting
- AutoTS: Automated Time Series Forecasting
- Auto_TS: Automatically build multiple Time Series models using a Single Line of Code
- Clairvoyance: Unified, End-to-End AutoML Pipeline for Medical Time Series
- darts: toolkit by Unit8 for easy manipulation and forecasting of time series
- ETNA Time Series Library by Tinkoff AI
- fbprophet: forecasting toolkit by Facebook
- fireTS: multi-variate time series prediction library working with sklearn
- Flow Forecast: Deep learning PyTorch library for time series forecasting, classification, and anomaly detection


- glum: Generalized linear models
- GluonTS: toolkit by Amazon for Probabilistic time series modeling in Python
- greykite: flexible, intuitive and fast forecasting library by LinkedIn
- hcrystallball: unifies the API for most commonly used libraries and modeling techniques for time-series
    forecasting in the Python ecosystem
- HierarchicalForecast: Hierarchical forecasting with statistical and econometric methods
- kats: tookit by Facebook for time series analysis and forecasting
- lazypredict: build models without much code
- Local Cascade Ensemble (LCE) is a high-performing, scalable and user-friendly machine learning method for
    the general tasks of Classification and Regression
- MAPIE: scikit-learn-compatible module for estimating prediction intervals.
- Merlion: A Machine Learning Framework for Time Series Intelligence by SalesForce
- MLForecast: Scalable machine learning based time series forecasting
- NGBoost: Natural Gradient Boosting for Probabilistic Prediction
- N-HiTS: Neural Hierarchical Interpolation for Time Series Forecasting
- NeuralForecast: time series forecasting with deep learning models
- nixtla: Automated time series processing and forecasting
- Orbit: Bayesian forecasting package by Uber
- piecewise-regression: For fitting straight line models to data with one or more breakpoints where the gradient
    changes
- pmdarima: tatistical library designed to fill the void in Python’s time series analysis capabilities
- predictionrevisited: implements the core statistical concepts from the book ”Prediction Revisited: The Im-
    portance of Observation”
- Prophet: Automatic Forecasting Procedure by Facebook
- PyAF: Automatic Time Series Forecasting
- PyFlux: modern time series models, nference options (frequentist and Bayesian) that can be applied to these
    models
- pyFTS: Fuzzy Time Series for Python
- pysf: Supervised forecasting of sequential data by UK national institute for data science and artificial intelli-
    gence
- PyTorch Forecasting: Forecasting timeseries with PyTorch - dataloaders, normalizers, metrics and models
- pyts: time series classification
- pytsal: Time Series analysis, visualization, forecasting along with AutoTS
- scikit-hts: Hierarchical Time Series Forecasting
- scikit-learn: machine learning in Python


- sktime: unified framework for machine learning with time series by UK national institute for data science and
    artificial intelligence
- slearn: package linking symbolic representation with scikit-learn machine learning
- statsforecast: Lightning � fast forecasting with statistical and econometric models
- Statsmodels: statistical modeling and econometrics in Python
- tbats: BATS and TBATS time series forecasting methods
- timemachines: Autonomous, univariate, k-step ahead time-series forecasting functions assigned Elo ratings
- TIMEX: time series forecasting as a service
- TSCV: Time Series CrossValidation
- ts-eval: Time Series analysis and evaluation tools
- tslearn: machine learning toolkit dedicated to time series data

**R software implementations**

List of packages and/or codes and/or frameworks and/or links:

- ACV: Optimal Out-of-Sample Forecast Evaluation and Testing under Stationarity
- AIafter: Forecast Combination Using the AI-AFTER Algorithm
- arfima: Fractional ARIMA (and Other Long Memory) Time Series Modeling
- ATAforecasting: Automatic Time Series Analysis and Forecasting Using the Ata Method
- autoTS: Automatic Model Selection and Prediction for Univariate Time Series
- baguette: Efficient Model Functions for Bagging
- bigtime: Sparse Estimation of Large Time Series Models
- BINtools: Bayesian BIN (Bias, Information, Noise) Model of Forecasting
- boot.pval: Bootstrap p-Values
- caretForecast: Time Series Forecasting Using Caret Infrastructure
- cvms: Cross-Validation for Model Selection
- dsos: Dataset Shift with Outlier Scores
- ensembleBMA: Probabilistic Forecasting using Ensembles and Bayesian Model Averaging
- fable: Forecasting Models for Tidy Time Series
- fable.ata: ATAforecasting Modelling Interface for fable Framework
- fable.prophet: Prophet Modelling Interface for ’fable’
- fabletools: Core Tools for Packages in the ’fable’ Framework
- FinnTS: Microsoft Finance Time Series Forecasting Framework
- flexmix: Flexible Mixture Modeling
- ForeCA: Forecastable Component Analysis


- ForecastComb: Forecast Combination Methods
- forecastHybrid: Convenient Functions for Ensemble Time Series Forecasts
- forecastML: Time Series Forecasting with Machine Learning Methods
- forecastSNSTS: Forecasting for Stationary and Non-Stationary Time Series
- ForecastTB: Test Bench for the Comparison of Forecast Methods
- FoReco: Point Forecast Reconciliation
- forecTheta: Forecasting Time Series by Theta Models
- fpp3: Data for ”Forecasting: Principles and Practice” (3rd Edition)
- fracdiff: Fractionally Differenced ARIMA aka ARFIMA(P,d,q) Models
- fwildclusterboot: Fast Wild Cluster Bootstrap Inference for Linear Models
- greybox: Toolbox for Model Building and Forecasting
- Greymodels: Shiny App for Grey Forecasting Model
- hts: Hierarchical and Grouped Time Series
- ipred: Improved Predictors
- legion: Forecasting Using Multivariate Models
- MAPA: Multiple Aggregation Prediction Algorithm
- mFLICA: Leadership-Inference Framework for Multivariate Time Series
- modeltime: The Tidymodels Extension for Time Series Modeling
- modeltime.ensemble: Ensemble Algorithms for Time Series Forecasting with Modeltime
- modeltime.gluonts: ’GluonTS’ Deep Learning
- modeltime.resample: Resampling Tools for Time Series Forecasting
- ngboostForecast: Probabilistic Time Series Forecasting
- OOS: Out-of-Sample Time Series Forecasting
- origami: Generalized Framework for Cross-Validation
- pre: Prediction Rule Ensembles
- predtoolsTS: Time Series Prediction Tools
- profoc: Probabilistic Forecast Combination Using CRPS Learning
- prophet: Automatic Forecasting Procedure
- PSF: Forecasting of Univariate Time Series Using the Pattern Sequence-Based Forecasting (PSF) Algorithm
- PTSR: Positive Time Series Regression
- RFpredInterval: Prediction Intervals with Random Forests and Boosted Forests
- rigr: Regression, Inference, and General Data Analysis Tools in R
- Rlgt: Bayesian Exponential Smoothing Models with Trend Modifications


- robets: Forecasting Time Series with Robust Exponential Smoothing
- robustarima: Robust ARIMA Modeling
- scoringfunctions: A Collection of Scoring Functions for Assessing Point Forecasts
- scoringRules: Scoring Rules for Parametric and Simulated Distribution Forecasts
- scoringutils: Utilities for Scoring and Assessing Predictions
- s2dverification: Set of Common Tools for Forecast Verification
- see: Visualisation Toolbox for ’easystats’ and Extra Geoms, Themes and Color Palettes for ’ggplot2’
- seer: Feature-Based Forecast Model Selection
- segmented: Regression Models with Break-Points / Change-Points Estimation
- sense: Automatic Stacked Ensemble for Regression Tasks
- shrink: Global, Parameterwise and Joint Shrinkage Factor Estimation
- SLBDD: Statistical Learning for Big Dependent Data
- smooth: Forecasting Using State Space Models
- spcr: Sparse Principal Component Regression
- SPlit: Split a Dataset for Training and Testing
- StabilizedRegression: Stabilizing Regression and Variable Selection
- stacks: Tidy Model Stacking
- subsemble: An Ensemble Method for Combining Subset-Specific Algorithm Fits
- tensorTS: Factor and Autoregressive Models for Tensor Time Series
- tfarima: Transfer Function and ARIMA Models
- thief: Temporal Hierarchical Forecasting
- tidymv: Tidy Model Visualisation for Generalised Additive Models
- traineR: Predictive Models Homologator
- TSdeeplearning: Deep Learning Model for Time Series Forecasting
- tsDyn: Nonlinear Time Series Models with Regime Switching
- tsensembler: Dynamic Ensembles for Time Series Forecasting
- TSPred: Functions for Benchmarking Time Series Prediction
- TSstudio: Functions for Time Series Analysis and Forecasting
- tsutils: Time Series Exploration, Modelling and Forecasting
- tswge: Time Series for Data Science.Accompanies the texts Time Series for Data Science and Applied Time
    Series Analysis with R,
- vars: VAR Modelling
- yardstick: Tidy Characterizations of Model Performance
- yhat: Interpreting Regression Effects


### 7.26 Graphs and graphical modeling.

**Python software implementations**

List of packages and/or codes and/or frameworks and/or links:

- ogb: Benchmark datasets, data loaders, and evaluators for graph machine learning
- pathpy: analysis of time series data on networks using higher-order and multi-order graphical models
- PGM: Probabilistic Graphical Models
- pgmpy: Probabilistic Graphical Models
- PGM_PyLib: Inference and Learning of Probabilistic Graphical Models
- pyaGrUM: Bayesian networks and other Probabilistic Graphical Models
- scikit-network: nalysis of large graphs
- skggm: Scikit-learn compatible estimation of general graphical models
- vishwakarma: visualization library for Probabilistic Graphical Models, Discrete & Continuous Distributions,
    and a lot more

**R software implementations**

List of packages and/or codes and/or frameworks and/or links:

- backbone: Extracts the Backbone from Graphs
- deepgp: Deep Gaussian Processes using MCMC
- gmgm: Gaussian Mixture Graphical Model Learning and Inference
- pcalg: Methods for Graphical Models and Causal Inference
- Revticulate: Interaction with ”RevBayes” in R
- tgp: Bayesian Treed Gaussian Process Models
- tidygraph: A Tidy API for Graph Manipulation

### 7.27 Linear algebra.

**Python software implementations**

List of packages and/or codes and/or frameworks and/or links:

- arctic: High performance datastore by Man Group for time series and tick data
- PyArma: Linear algebra library for Python
- PyArmadillo: an alternative approach to linear algebra in Python
- PyPardiso: Python interface to the Intel MKL Pardiso library to solve large sparse linear systems of equations
- Scipy: mathematics, science, and engineering


**R software implementations**

List of packages and/or codes and/or frameworks and/or links:

- EigenR: Complex Matrix Algebra with ’Eigen’
- fastmatrix: Fast Computation of some Matrices Useful in Statistics
- freqdom: Frequency Domain Based Analysis: Dynamic PCA
- ica: Independent Component Analysis
- Matrix: Sparse and Dense Matrix Classes and Methods
- MatrixExtra: Extra Methods for Sparse Matrices
- matsbyname: An Implementation of Matrix Mathematics
- proxyC: Computes Proximity in Large Sparse Matrices
- rARPACK: Solvers for Large Scale Eigenvalue and SVD Problems
- RcppArmadillo: ’Rcpp’ Integration for the ’Armadillo’ Templated Linear Algebra Library
- RcppEigen: ’Rcpp’ Integration for the ’Eigen’ Templated Linear Algebra Library
- Rlinsolve: Iterative Solvers for (Sparse) Linear System of Equations
- RSpectra: Solvers for Large-Scale Eigenvalue and SVD Problems
- sanic: Solving Ax = b Nimbly in C++
- SparseChol: Sparse Cholesky LDL Decomposition of Symmetric Matrices
- SparseM: Sparse Linear Algebra
- svd: Interfaces to Various State-of-Art SVD and Eigensolvers

### 7.28 Machine Learning.

**Collections of resources**

List of links:

- Curated list of open source libraries to deploy, monitor, version and scale machine learning
- Dive into Machine Learning
- Artificial Intelligence and Machine Learning For Quantum Technologies

**Python software implementations**

List of packages and/or codes and/or frameworks and/or links:

- abess: Fast Best Subset Selection
- AIF360: comprehensive set of fairness metrics for datasets and machine learning models, explanations for
    these metrics, and algorithms to mitigate bias in datasets and models
- benchmark_VAE: Unifying Generative Autoencoder implementations in Python
- bindsnet: Simulation of spiking neural networks (SNNs) using PyTorch
- biosphere: Simple, fast random forests


- Catalyst: PyTorch framework for Deep Learning Research and Development
- catboost: Gradient Boosting on Decision Trees by Yandex
- Chainer: flexible framework of neural networks for deep learning
- combo: A Python Toolbox for Machine Learning Model Combination
- compose: machine learning tool for automated prediction engineering
- coremltools: convert machine learning models from third-party libraries to the Core ML format (by Apple)
- CrypTen: framework for Privacy Preserving Machine Learning
- DeepChecks: Testing and Validating ML Models and Data
- DoubleML: Double Machine Learning in Python
- Driblet - Google Cloud based ML pipeline by Google
- geotorch: Constrained optimization toolkit for PyTorch
- GPyTorch: Gaussian processes for modern machine learning systems.
- Hub for Tensorflow: library for transfer learning by reusing parts of TensorFlow models
- Hummingbird: library by Microsoft for compiling trained traditional ML models into tensor computations
- InvarianceUnitTests: Linear unit-tests for invariance discovery
- JAX: toolkit by Google for composable transformations of Python+NumPy programs: differentiate, vectorize,
    JIT to GPU/TPU, and more
- jraph: Graph Neural Network Library in Jax
- karateclub: Framework for Unsupervised Learning on Graphs
- keras: deep learning API written in Python, running on top of the machine learning platform TensorFlow
- Local Cascade Ensemble (LCE) is a high-performing, scalable and user-friendly machine learning method for
    the general tasks of Classification and Regression
- LightGBM: fast, distributed, high performance gradient boosting (GBT, GBDT, GBRT, GBM or MART)
    framework by Microsoft
- Merlion: A Machine Learning Framework for Time Series Intelligence by SalesForce
- mlflow: Interface to ’MLflow’
- MLForecast: Scalable machine learning based time series forecasting
- mlinsights: Extends scikit-learn with new models, transformers, metrics, plotting.
- MLJAR Automated Machine Learning for Humans
- mlxtend: extension and helper modules for Python’s data analysis and machine learning libraries.
- MMdnn: toolkit by Microsoft to convert models between Caffe, Keras, MXNet, Tensorflow, CNTK, PyTorch
    Onnx and CoreML.
- Model Garden for TensorFlow
- mvlearn is an open-source Python software package for multiview learning tools.


- NannyM: estimate post-deployment model performance (without access to targets), detect data drift, and
    intelligently link data drift alerts back to changes in model performance
- NeuralForecast: time series forecasting with deep learning models
- NGBoost: Natural Gradient Boosting for Probabilistic Prediction
- nimbusml: toolkit by Microsoft that provides Python bindings for ML.NET
- nolearn: Combines the ease of use of scikit-learn with the power of Theano/Lasagne
- norse: Deep learning with spiking neural networks (SNNs) in PyTorch.
- OPACUS: Training PyTorch models with differential privacy
- ptgnn: PyTorch Graph Neural Network Library
- PyCaret : machine learning library
- PyTorch: Tensors and Dynamic neural networks in Python with strong GPU acceleration
- PyTorch Lightning: lightweight PyTorch wrapper for ML researchers
- Ray: packaged with RLlib, a scalable reinforcement learning library, and Tune, a scalable hyperparameter
    tuning librar
- scikit-learn: machine learning in Python
- scikit-learn-intelex: Intel Extension for Scikit-learn
- sklearn-onnx converts scikit-learn models to ONNX
- skorch: scikit-learn compatible neural network library that wraps PyTorch
- SNNTORCH: Deep and online learning with spiking neural networks
- tensorflow: end-to-end open source platform for machine learning
- tf2onnx: Convert TensorFlow, Keras, Tensorflow.js and Tflite models to ONNX
- Transfer Learning Library for Domain Adaptation, Task Adaptation, and Domain Generalization
- transformers: State-of-the-art Machine Learning for Pytorch, TensorFlow, and JAX
- Trax: Deep Learning by Google with Clear Code and Speed
- tslearn: machine learning toolkit dedicated to time-series data
- xformers: Hackable and optimized Transformers building blocks, supporting a composable construction
- yellowbrick: Visual analysis and diagnostic tools to facilitate machine learning model selection

**R software implementations**

List of packages and/or codes and/or frameworks and/or links:

- abess: Fast Best Subset Selection
- agua: ’tidymodels’ Integration with ’h2o’
- APML: An Approach for Machine-Learning Modelling
- arenar: Arena for the Exploration and Comparison of any ML Models
- brulee: High-Level Modeling Functions with ’torch’


- distillML: Model Distillation and Interpretability Methods for Machine Learning Models
- elmNNRcpp: The Extreme Learning Machine Algorithm
- fairmodels: Flexible Tool for Bias Detection, Visualization, and Mitigation
- familiar: End-to-End Automated Machine Learning and Model Evaluation
- KernelKnn: Extends the simple k-nearest neighbors algorithm by incorporating numerous kernel functions
    and a variety of distance metrics
- lightgbm: Light Gradient Boosting Machine by Microsoft
- MachineShop: Machine Learning Models and Tools
- mcboost: Multi-Calibration Boosting
- MetricsWeighted: Weighted Metrics, Scoring Functions and Performance Measures for Machine Learning
- mikropml: User-Friendly R Package for Supervised Machine Learning Pipelines
- mlflow: Interface to ’MLflow’
- mlquantify: Algorithms for Class Distribution Estimation
- mlr3: Machine Learning in R - Next Generation
- mlr3cluster: Cluster Extension for ’mlr3’
- mlr3learners: Recommended Learners for ’mlr3’
- mlr3tuning: hyperparameter tuning with ’mlr3’
- mlr3verse: package family is a set of packages for machine-learning purposes built in a modular fashion
- mlr3viz: Visualizations for’mlr3
- mlrintermbo: Model-Based Optimization for ’mlr3’ Through ’mlrMBO’
- mlrMBO: Bayesian Optimization and Model-Based Optimization of Expensive Black-Box Functions
- multiview: Cooperative Learning for Multi-View Analysis
- rTorch: R Bindings to ’PyTorch’
- SPlit: Split a Dataset for Training and Testing
- tensorflow: R Interface to ’TensorFlow’
- tfdatasets: Interface to ’TensorFlow’ Datasets
- tfprobability: Interface to ’TensorFlow Probability’
- TSdeeplearning: Deep Learning Model for Time Series Forecasting
- xgboost: Extreme Gradient Boosting


### 7.29 Machine Learning frameworks (includes Automated ML and hyperparameters tuning)

**Python software implementations**

List of packages and/or codes and/or frameworks and/or links:

- AI2 Tango: library for choreographing machine learning research
- AutoGluon: toolkit by Amazon on AutoML for Text, Image, and Tabular Data
- AutoKeras: An AutoML system based on Keras
- AutoPyTorch: Automatic architecture search and hyperparameter optimization for PyTorch
- auto-sklearn: Automated Machine Learning with scikit-learn
- BayesianOptimization: global optimization with gaussian processes.
- cesium: Machine Learning Time-Series Platform
- Clairvoyance: Unified, End-to-End AutoML Pipeline for Medical Time Series
- Colossal-AI: A Unified Deep Learning System for Big Model Era
- EvalML is an AutoML library which builds, optimizes, and evaluates machine learning pipelines using domain-
    specific objective functions.
- FLAML: accurate machine learning models automatically, efficiently and economically (by Microsoft)
- flax: neural network library for JAX that is designed for flexibility
- H2O is an Open Source, Distributed, Fast & Scalable Machine Learning Platform
- Hypernets: General Automated Machine Learning framework
- HyperOpt: Distributed Asynchronous Hyperparameter Optimization
- hyperopt-sklearn: Hyper-parameter optimization for sklearn
- kedro: framework for creating reproducible, maintainable and modular data science code
- kedro-viz: Visualise your Kedro data and machine-learning pipelines and track your experiments.
- keras-tuner: hyperparameter optimization framework
- MLBox: Automated Machine Learning library
- mlpack: ’Rcpp’ Integration for the ’mlpack’ Library
- mlr3tuning: Tuning for ’mlr3’
- model_search: framework (by Google) that implements AutoML algorithms for model architecture search at
    scale
- NannyM: estimate post-deployment model performance (without access to targets), detect data drift, and
    intelligently link data drift alerts back to changes in model performance
- NNI: toolkit by Microsoft to help users automate Feature Engineering, Neural Architecture Search, Hyperpa-
    rameter Tuning and Model Compression
- oneflow: OneFlow is a deep learning framework designed to be user-friendly, scalable and efficient.
- ONNX: Open Neural Network Exchange is an Open standard for machine learning interoperability


- Optuna: hyperparameter optimization framework
- PyCaret : machine learning library
- squirrel-core: library that enables ML teams to share, load, and transform data in a collaborative, flexible,
    and efficient way.
- Relevance AI - The ML Platform for Unstructured Data Analysis
- Talos: Hyperparameter Optimization for TensorFlow, Keras and PyTorch
- trax: end-to-end library (by Google Brain) for deep learning that focuses on clear code and speed.
- tune-sklearn: drop-in replacement for Scikit-Learn’s GridSearchCV / RandomizedSearchCV – but with cutting
    edge hyperparameter tuning techniques
- vowpal_wabbit: machine learning system which pushes the frontier of machine learning with techniques such
    as online, hashing, allreduce, reductions, learning2search, active, and interactive learning

**R software implementations**

List of packages and/or codes and/or frameworks and/or links:

- autokeras: R Interface to ’AutoKeras’
- automl: Deep Learning with Metaheuristic
- DriveML: Self-Drive Machine Learning Projects
- familiar: End-to-End Automated Machine Learning and Model Evaluation
- mlpack: ’Rcpp’ Integration for the ’mlpack’ Library
- mlr3tuningspaces: Search Spaces for Hyperparameter Tuning
- ParBayesianOptimization: Parallel Bayesian Optimization of Hyperparameters
- rBayesianOptimization: Bayesian Optimization of Hyperparameters
- RemixAutoML: automation of machine learning, forecasting, feature engineering, model evaluation, model
    interpretation, recommenders, and EDA.

### 7.30 Network and graph analysis.

**Python software implementations**

List of packages and/or codes and/or frameworks and/or links:

- dantro: handle, transform, and visualize hierarchically structured data
- deeptime: nalysis of time series data including dimensionality reduction, clustering, and Markov model esti-
    mation
- ETNA Time Series Library by Tinkoff AI
- fastpath: find the path through a network of nodes
- GraKeL: scikit-learn compatible library for graph kernels
- grapharray: handle network link/node attributes as Numpy arrays
- GraphVite: A General and High-performance Graph Embedding System
- karateclub: Framework for Unsupervised Learning on Graphs


- netrd: etwork {reconstruction, distances, dynamics}
- networkit: toolkit for large-scale network analysis
- NetworkX: Network Analysis in Python
- pandana: Pandas Network Analysis: fast accessibility metrics and shortest paths, using contraction hierarchies
- pyvis: visualizing interactive network graphs
- rustworkx: high performance Python graph library implemented in Rust
- scikit-learn: machine learning in Python
- tslearn: machine learning toolkit dedicated to time-series data

**R software implementations**

List of packages and/or codes and/or frameworks and/or links:

- backbone: identify the most ‘important’ or ‘significant’ edges in a network
- bnmonitor: An Implementation of Sensitivity Analysis in Bayesian Networks
- bootnet: Bootstrap Methods for Various Network Estimation Routines
- CINNA: Deciphering Central Informative Nodes in Network Analysis
- dbnR: Dynamic Bayesian Network Learning and Inference
- diceR: Diverse Cluster Ensemble in R
- dtwclust: Time Series Clustering Along with Optimizations for the Dynamic Time Warping Distance
- fabisearch: Change Point Detection in High-Dimensional Time Series Networks
- fastkmedoids: Faster K-Medoids Clustering Algorithms: FastPAM, FastCLARA, FastCLARANS
- gRain: Graphical Independence Networks
- heatmaply: Interactive Cluster Heat Maps Using ’plotly’ and ’ggplot2’
- influential: Identification and Classification of the Most Influential Nodes
- MatTransMix: Clustering with Matrix Gaussian and Matrix Transformation Mixture Models
- Mercator: Clustering and Visualizing Distance Matrices
- MixSim: Simulating Data to Study Performance of Clustering Algorithms
- mixture: Mixture Models for Clustering and Classification
- MKMeans: A Modern K-Means (MKMeans) Clustering Algorithm
- ndtv: Network Dynamic Temporal Visualizations
- network: Classes for Relational Data
- networkABC: Network Reverse Engineering with Approximate Bayesian Computation
- networkDynamic: Dynamic Extensions for Network Objects
- NetworKit: tool suite for high-performance network analysis
- networktools: Tools for Identifying Important Nodes in Networks


- statnet: Software Tools for the Statistical Analysis of Network Data
- visNetwork: Network Visualization using ’vis.js’ Library
- wdnet: Weighted and Directed Networks
- WGCNA: Weighted Correlation Network Analysis

### 7.31 Numerical methods (includes numerical optimization)

**Python software implementations**

List of packages and/or codes and/or frameworks and/or links:

- ADE: Asynchronous Differential Evolution, with efficient multiprocessing
- autoray: Write numeric code that automatically works with any numpy-ish libraries
- BayesianOptimization: global optimization with gaussian processes
- CasADi is a symbolic framework for numeric optimization implementing automatic differentiation in forward
    and reverse modes on sparse matrix-valued computational graphs
- cmaes: Covariance Matrix Adaptation Evolution Strategy (CMA-ES)
- coco: Numerical Black-Box Optimization Benchmarking Framework
- cp_solver: CP-SAT Solver by Google
- cvxopt: convex optimization
- cvxpy: convex optimization
- DEAP: Distributed Evolutionary Algorithms in Python
- derivative: Numerical differentiation of noisy time series data
- Differential Evolution expensiveopt
- eigenpy: Efficient Python bindings between Numpy/Eigen
- ELA drframework: Dimensionality Reduction Framework for Exploratory Landscape Analysis
- evol: grammar for evolutionary algorithms and heuristics
- fcmaes complements scipy optimize by providing additional optimization methods, faster C++/Eigen based
    implementations and a coordinated parallel retry mechanism.
- gemseo: Generic Engine for Multi-disciplinary Scenarios, Exploration and Optimization
- General Purpose Optimization Library GPOL
- HiGHS: Linear optimization
- hyperactive: optimization and data collection toolbox for convenient and fast prototyping of computationally
    expensive models
- ipopt: Cython interface for the interior point optimzer IPOPT
- ipyopt: interface for the interior point optimizer COIN-OR IPOpt
- mystic: highly-constrained non-convex optimization and uncertainty quantification
- nevergrad: Python toolbox for performing gradient-free optimization by Facebook


- nlopt: nonlinear optimization
- Open MDAO: optimization framework
- optima: library for numerical optimization calculations
- OR-Tools: optimization toolkit by Google
- osqp: Operator Splitting QP Solver
- pybobyqa: Derivative-Free Optimization with Bound Constraints
- pycma: Covariance Matrix Adaptation Evolution Strategy (CMA-ES)
- pymoo: Multi-objective Optimization
- pyomo: supports a diverse set of optimization capabilities for formulating and analyzing optimization models.
- PyOptSparse: object-oriented framework for formulating and solving nonlinear constrained optimization prob-
    lems
- PyPDE: solve partial differential equations using finite differences.
- qpsolvers: Quadratic programming solvers in Python with a unified API
- root_numpy: interface between ROOT and NumPy
- scikit-opt: Swarm Optimization methods
- scikit-optimize: Sequential model-based optimization with a ‘scipy.optimize‘ interface
- Scipy: Fundamental algorithms for scientific computing
- SHADE: Success-History Based Parameter Adaptation for Differential Evolution
- stgaircase: data analysis package based on mathematical step functions
- theseus: differentiable nonlinear optimization
- torchquad: High-performance numerical integration on the GPU with PyTorch, JAX and Tensorflow
- torchsde: Differentiable SDE solvers with GPU support and efficient sensitivity analysis
- trust-region:trust-region subproblem solvers for nonlinear optimization

**R software implementations**

List of packages and/or codes and/or frameworks and/or links:

- ao: Alternating Optimization
- bbotk: Black-Box Optimization Toolkit
- CGNM: Cluster Gauss-Newton Method: Find multiple solutions of a nonlinear least squares problem
- CVXR: Disciplined Convex Optimization
- DEoptim: Global Optimization by Differential Evolution
- DEoptimR: Differential Evolution Optimization in Pure R
- ECOSolveR: Embedded Conic Solver in R
- ggblanket: Simplify ’ggplot2’ Visualisation


- graDiEnt: derivative-free, optim-style Stochastic Quasi-Gradient Differential Evolution optimization
- itp: The Interpolate, Truncate, Project (ITP) Root-Finding Algorithm
- LowRankQP: Low Rank Quadratic Programming
- miesmuschel: Mixed Integer Evolution Strategies
- minqa: Derivative-Free Optimization Algorithms by Quadratic Approximation
- mlr3mbo: Flexible Bayesian Optimization
- NMOF: Numerical Methods and Optimization in Finance
- osqp: Quadratic Programming Solver using the ’OSQP’ Library
- RcppEnsmallen: Header-Only C++ Mathematical Optimization Library for ’Armadillo’
- rvinecopulib: High Performance Algorithms for Vine Copula Modeling
- rgenoud: R Version of GENetic Optimization Using Derivatives
- rmoo: Multi-Objective Optimization in R
- scs: Splitting Conic Solver for linear programs (’LPs’), second-order cone programs (’SOCPs’), semidefinite
    programs (’SDPs’), exponential cone programs (’ECPs’), and power cone programs (’PCPs’), or problems
    with any combination of those cone
- SimEngine: A Modular Framework for Statistical Simulations in R
- trustOptim: Trust Region Optimization for Nonlinear Functions with Sparse Hessians

### 7.32 Probabilistic modeling (includes mixture models and Gaussian Processes)

Links to resources

- Professionally curated list of awesome Conformal Prediction videos, tutorials, books, papers, PhD and MSc
    theses, articles and open-source libraries

**Python software implementations**

List of packages and/or codes and/or frameworks and/or links:

- beanmachine: inference on probabilistic models
- celerite2: fast and scalable Gaussian Process (GP) Regression
- conformal-rnn: code for ”Conformal time-series forecasting”, NeurIPS 2021
- crepes: Conformal Regressors and Conformal Predictive Systems
- EnbPI: Ensemble batch prediction intervals
- EnCQR: ensemble conformalized quantile regression (EnCQR)
- GluonTS: toolkit by Amazon for Probabilistic time series modeling in Python
- gptools: Gaussian processes with arbitrary derivative constraints and predictions.
- GPy: Gaussian processes framework
- GPyTorch: Gaussian processes for modern machine learning systems.
- MAPIE: scikit-learn-compatible module for estimating prediction intervals


- NGBoost: Natural Gradient Boosting for Probabilistic Prediction
- orbit-ml: Bayesian forecasting package by Uber
- pgmpy: Probabilistic Graphical Models – learning (Structure and Parameter), inference (Probabilistic and
    Causal), and simulations in Bayesian Networks
- pplbench: Evaluation Framework for Probabilistic Programming Languages
- PyMC: Bayesian Modeling and Probabilistic Machine Learning with Aesara
- pyro: Deep universal probabilistic programming with Python and PyTorch
- PySloth: Probabilistic Prediction
- skpro: toolkit by UK national institute for data science and artificial intelligence for Supervised domain-
    agnostic prediction framework for probabilistic modelling
- tinyGP: The tiniest of Gaussian Process libraries
- zhusuan: probabilistic programming library for Bayesian deep learning, generative models, based on Tensor-
    flow

**R software implementations**

List of packages and/or codes and/or frameworks and/or links:

- AdequacyModel: Adequacy of Probabilistic Models and General Purpose Optimization
- AdMit: Adaptive Mixture of Student-t Distributions
- aldvmm: Adjusted Limited Dependent Variable Mixture Models
- bgmm: Gaussian Mixture Modeling Algorithms and the Belief-Based Mixture Modeling
- bmixture: Bayesian Estimation for Finite Mixture of Distributions
- BNPmix: Bayesian Nonparametric Mixture Models
- bpgmm: Bayesian Model Selection Approach for Parsimonious Gaussian Mixture Models
- ClusterR: Gaussian Mixture Models, K-Means, Mini-Batch-Kmeans, K-Medoids and Affinity Propagation
    Clustering
- conformalInference.multi: Conformal Inference Tools for Regression with Multivariate Response
- DistributionOptimization: Distribution Optimization
- distributionsrd: Distribution Fitting and Evaluation
- EMCluster: EM Algorithm for Model-Based Clustering of Finite Mixture Gaussian Distribution
- evmix: Extreme Value Mixture Modelling, Threshold Estimation and Boundary Corrected Kernel Density
    Estimation
- flexmix: Flexible Mixture Modeling
- flexmixNL: Finite Mixture Modeling of Generalized Nonlinear Models
- GauPro: Gaussian Process Fitting
- gmgm: Gaussian Mixture Graphical Model Learning and Inference
- greta.gp: Gaussian Process Modelling in ’greta’


- hmmr: ”Mixture and Hidden Markov Models with R” Datasets and Example Code
- ltmix: Left-Truncated Mixtures of Gamma, Weibull, and Lognormal Distributions
- MatrixMixtures: Model-Based Clustering via Matrix-Variate Mixture Models
- MGMM: Missingness Aware Gaussian Mixture Models
- mistr: Mixture and Composite Distributions
- mixComp: Estimation of Order of Mixture Distributions
- MixMatrix: Classification with Matrix Variate Normal and t Distributions
- MixSim: Simulating Data to Study Performance of Clustering Algorithms
- mixsmsn: Fitting Finite Mixture of Scale Mixture of Skew-Normal Distributions
- mixreg: Functions to Fit Mixtures of Regressions
- mixSPE: Mixtures of Power Exponential and Skew Power Exponential Distributions for Use in Model-Based
    Clustering and Classification
- mixsqp: Sequential Quadratic Programming for Fast Maximum-Likelihood Estimation of Mixture Proportions
- mixtools: Tools for Analyzing Finite Mixture Models
- mixture: Mixture Models for Clustering and Classification
- mclust: Gaussian Mixture Modelling for Model-Based Clustering, Classification, and Density Estimation
- mlr3proba: Probabilistic Supervised Learning for ’mlr3’
- MoMPCA: Inference and Clustering for Mixture of Multinomial Principal Component Analysis
- mvgb: Multivariate Probabilities of Scale Mixtures of Multivariate Normal Distributions via the Genz and
    Bretz (2002) QRSVN Method
- ngboostForecast: Probabilistic Time Series Forecasting
- nlsmsn: Fitting Nonlinear Models with Scale Mixture of Skew-Normal Distributions
- Nmix: Bayesian Inference on Univariate Normal Mixtures
- nvmix: Multivariate Normal Variance Mixtures
- opGMMassessment: Optimized Automated Gaussian Mixture Assessment
- pgmm: Parsimonious Gaussian Mixture Models
- pGPx: Pseudo-Realizations for Gaussian Process Excursions
- pks: Probabilistic Knowledge Structures
- plgp: Particle Learning of Gaussian Processes
- plotmm: Tidy Tools for Visualizing Mixture Models
- QuantileGH: Quantile Least Mahalanobis Distance Estimator for Tukey g-&-h Mixture
- rebmix: Finite Mixture Modeling, Clustering & Classification
- Revticulate: Interaction with ”RevBayes” in R
- RGMM: Robust Mixture Model


- RMixtComp: Mixture Models with Heterogeneous and (Partially) Missing Data
- robmixglm: Robust Generalized Linear Models (GLM) using Mixtures
- Rmixmod: Classification with Mixture Modelling
- RobMixReg: Robust Mixture Regression
- rrMixture: Reduced-Rank Mixture Models
- seqHMM: Mixture Hidden Markov Models for Social Sequence Data and Other Multivariate, Multichannel
    Categorical Time Series
- skewlmm: Scale Mixture of Skew-Normal Linear Mixed Models
- skewMLRM: Estimation for Scale-Shape Mixtures of Skew-Normal Distributions
- uGMAR: Estimate Univariate Gaussian and Student’s t Mixture Autoregressive Models

### 7.33 Reinforcement learning.

**Collections of resources**

List of links:

- Awesome Reinforcement Learning: Reinforcement learning resources curated
- Awesome Deep RL: curated list of awesome Deep Reinforcement Learning resources

**Python software implementations**

List of packages and/or codes and/or frameworks and/or links:

- Acme: a research framework by DeepMind for reinforcement learning
- Baconian: Model-based Reinforcement Learning Framework
- Open AI Baselines: high-quality implementations by OpenAI of reinforcement learning algorithms
- Catalyst.RL: Distributed Framework for Reproducible RL Research
- ChainerRL: deep reinforcement learning library built on top of Chainer
- Coach: Reinforcement Learning by Intel AI Lab
- d3rlpy: offline deep reinforcement learning library
- Decision Transformer: Reinforcement Learning via Sequence Modeling
- DRL with PyTorch: PyTorch implementations of deep reinforcement learning algorithms and environments
- Deep Reinforcement Learning Hands-On
- deer: DEEp Reinforcement learning framework
- Dopamine: research framework by Google for fast prototyping of reinforcement learning algorithms
- ElegantRL: Lightweight and scalable deep reinforcement learning using PyTorch
- FinRL: Deep Reinforcement Learning for Quantitative Finance
- FinRL-Meta: Universe of Near-Real Market Environments for Data-Driven Financial Reinforcement Learning
- garage: toolkit for reproducible reinforcement learning research


- Gym: ttolkit by openAI for toolkit for developing and comparing reinforcement learning algorithms
- HRAC: Generating Adjacency-Constrained Subgoals in Hierarchical Reinforcement Learning
- keras-rl: Deep Reinforcement Learning for Keras
- Mava: library of multi-agent reinforcement learning components and systems
- Multi-Agent Resource Optimization (MARO) platform is an instance of Reinforcement Learning as a Service
    (RaaS) for real-world resource optimization problems.
- MBRL-Lib: toolbox by Facebook for facilitating development of Model-Based Reinforcement Learning algo-
    rithms
- Mushroom RL: modular toolkit able to use modularity allows to use libraries for tensor computation (e.g.
    PyTorch, Tensorflow) and RL benchmarks (e.g. OpenAI Gym, PyBullet, Deepmind Control Suite)
- PettingZoo: Gym for multi-agent reinforcement learning
- PFRL: PyTorch-based deep reinforcement learning library
- PGPortfolio: Policy Gradient Portfolio
- PyTorchRL: reinforcement learning library focused on modularity and simplicity
- Rainbow: Combining Improvements in Deep Reinforcement Learning
- ReAgent: platform by Facebook for Reasoning systems (Reinforcement Learning, Contextual Bandits, etc.)
- rl: modular, primitive-first, python-first PyTorch library for Reinforcement Learning.
- RLkit: Collection of reinforcement learning algorithms
- RLlib: Ray is packaged with RLlib, a scalable reinforcement learning library, and Tune, a scalable hyperpa-
    rameter tuning librar
- RLMeta is a light-weight flexible framework for Distributed Reinforcement Learning Research
- rlpyt: Reinforcement Learning in PyTorch
- rlstructures: Facebook library to facilitate the implementation of new reinforcement learning algorithms
- skrl: Modular reinforcement learning
- Stable Baselines3: PyTorch version of Stable Baselines, reliable implementations of reinforcement learning
    algorithms
- Tensorforce: TensorFlow library for applied reinforcement learning
- TensorLayer: Deep Learning and Reinforcement Learning Library for Scientists and Engineers
- TF-Agents: TensorFlow library for Contextual Bandits and Reinforcement Learning
- Tianshou: PyTorch deep reinforcement learning library
- Tonic RL: Tonic RL library
- TorchBeast: A PyTorch Platform by Facebook for Distributed RL
- TRFL: TensorFlow Reinforcement Learning by DeepMind
- vowpal_wabbit: machine learning system which pushes the frontier of machine learning with techniques such
    as online, hashing, allreduce, reductions, learning2search, active, and interactive learning


**R software implementations**

List of packages and/or codes and/or frameworks and/or links:

- Hands-On Reinforcement Learning
- QLearning: Reinforcement Learning using the Q Learning Algorithm
- reinforcelearn: reinforcement learning, including Q-Learning algorithm
- ReinforcementLearning: Model-Free Reinforcement Learning
- RLT: Reinforcement Learning Trees

### 7.34 Robust numerical methods.

**Python software implementations**

List of packages and/or codes and/or frameworks and/or links:

- derivative: Numerical differentiation of noisy time series data
- hypothesize: hypothesis testing using robust statistics
- robusta: interface to many common statistical analyses, performed using through R and RPY2.
- Robustats is a Python library for high-performance computation of robust statistical estimators
- robustbase: Statistical Estimators (Sn, Qn, MAD, IQR)

**R software implementations**

List of packages and/or codes and/or frameworks and/or links:

- clubSandwich: Cluster-Robust (Sandwich) Variance Estimators with Small-Sample Corrections
- l1spectral: An L1-Version of the Spectral Clustering
- L2E: Robust Structured Regression via the L2 Criterion
- pcaPP: Robust PCA by Projection Pursuit
- RCTS: Clustering Time Series While Resisting Outliers
- RDnp: Robust Test for Complete Independence in High-Dimensions
- revss: Robust Estimation in Very Small Samples
- RGMM: Robust Mixture Model
- rigr: Regression, Inference, and General Data Analysis Tools in R
- robcp: Robust Change-Point Tests
- robcor: Robust Correlations
- robfilter: Robust Time Series Filters
- robmixglm: Robust Generalized Linear Models (GLM) using Mixtures
- RobMixReg: Robust Mixture Regression
- RobStatTM: Robust Statistics: Theory and Methods
- robust: Port of the S+ ”Robust Library”


- RobustANOVA: Robust One-Way ANOVA Tests under Heteroscedasticity and Nonnormality
- robustbase: Basic Robust Statistics
- RobustCalibration: Robust Calibration of Imperfect Mathematical Models
- robustcov: Collection of Robust Covariance and (Sparse) Precision Matrix Estimators
- robustHD: Robust Methods for High-Dimensional Data
- rrcov: Scalable Robust Estimators with High Breakdown Point
- RSC: Robust and Sparse Correlation Matrix
- sandwich: Robust Covariance Matrix Estimators
- StabilizedRegression: Stabilizing Regression and Variable Selection
- tsrobprep: Robust Preprocessing of Time Series Data
- walrus: Robust Statistical Methods

### 7.35 Selection of features, variables, models, data splits

**Collections of resources**

List of links:

- Data Science Feature Engineering and Selection Tutorials
- Feature Engineering and Selection: A Practical Approach for Predictive Models
- Guide for Feature Engineering and Feature Selection

**Python software implementations**

List of packages and/or codes and/or frameworks and/or links:

- abess: Fast Best-Subset Selection Library
- boruta_py: Boruta all-relevant feature selection method
- dython: Data analysis tools
- featureclass: Feature engineering library to keep track of feature dependencies, documentation and schema
- feature_engine: library with multiple transformers to engineer and select features for use in machine learning
    models
- FeatureTools: automated feature engineering
- Featurewiz: advanced feature engineering strategies
- ITMO_FS: Feature selection library
- KnockPy: Knockoffs for controlled variable selection
- kydavra: feature selection
- Py_FS: Feature Selection
- pyHSICLasso: Versatile Nonlinear Feature Selection Algorithm for High-dimensional Data
- python_stepwiseSelection: Automated Backward and Forward Selection


- scikit-learn: machine learning in Python
- scikit-rebate: scikit-learn-compatible Python implementation of ReBATE, a suite of Relief-based feature
    selection algorithms
- Sklearn-genetic-opt: Hyperparameters tuning and feature selection, using evolutionary algorithms
- sktime: unified framework for machine learning with time series by UK national institute for data science and
    artificial intelligence
- tsfeatures: Calculates various features from time series data. Python implementation of the R package
    tsfeatures
- UltraNest: Fit and compare complex models reliably and rapidly. Advanced nested sampling
- zoofs: feature selection using a variety of nature-inspired wrapper algorithms

**R software implementations**

List of packages and/or codes and/or frameworks and/or links:

- abess: Fast Best-Subset Selection Library
- BAS: Bayesian Variable Selection and Model Averaging using Bayesian Adaptive Sampling
- basad: Bayesian Variable Selection with Shrinking and Diffusing Priors
- BayesVarSel: Bayes Factors, Model Choice and Variable Selection in Linear Models
- bpgmm: Bayesian Model Selection Approach for Parsimonious Gaussian Mixture Models
- bravo: Bayesian Screening and Variable Selection
- care: High-Dimensional Regression and CAR Score Variable Selection
- dials: Tools for Creating Tuning Parameter Values
- EMVS: The Expectation-Maximization Approach to Bayesian Variable Selection
- FeatureTerminatoR: Feature Selection Engine to Remove Features with Minimal Predictive Power
- FSinR: Feature Selection
- fsMTS: Feature Selection for Multivariate Time Series
- gausscov: The Gaussian Covariate Method for Variable Selection
- greybox: Toolbox for Model Building and Forecasting
- hrqglas: Group Variable Selection for Quantile and Robust Mean Regression
- knockoff: The Knockoff Filter for Controlled Variable Selection
- mBvs: Bayesian Variable Selection Methods for Multivariate Data
- MDFS: MultiDimensional Feature Selection
- mlr3fselect: Feature Selection for ’mlr3’
- mplot: Graphical Model Stability and Variable Selection Procedures
- MXM: Feature Selection (Including Multiple Solutions) and Bayesian Networks
- nestfs: Cross-Validated (Nested) Forward Selection


- NonpModelCheck: Model Checking and Variable Selection in Nonparametric Regression
- pcaPP: Robust PCA by Projection Pursuit
- picR: Predictive Information Criteria for Model Selection
- plsVarSel: Variable Selection in Partial Least Squares
- praznik: Tools for Information-Based Feature Selection and Scoring
- prinvars: Principal Variables (methods for reducing the number of features within a data set)
- projpred: Projection Predictive Feature Selection
- Rforestry: Random Forests, Linear Trees, and Gradient Boosting for Inference and Interpretability
- rmcfs: The MCFS-ID Algorithm for Feature Selection and Interdependency Discovery
- rSAFE: Surrogate-Assisted Feature Extraction
- rstanarm: Bayesian Applied Regression Modeling via Stan
- SelectBoost: A General Algorithm to Enhance the Performance of Variable Selection Methods in Correlated
    Datasets
- SignifReg: Consistent Significance Controlled Variable Selection in Generalized Linear Regression
- sivs: Stable Iterative Variable Selection
- smoothic: Variable Selection Using a Smooth Information Criterion
- SPlit: Split a Dataset for Training and Testing
- splitTools: Tools for Data Splitting
- stabiliser: Stabilising Variable Selection
- stabm: Stability Measures for Feature Selection
- stacks: Tidy Model Stacking
- stepgbm: Stepwise Variable Selection for Generalized Boosted Regression Modeling
- SWIM: Scenario Weights for Importance Measurement
- theft: Tools for Handling Extraction of Features from Time Series
- tornado: Plots for Model Sensitivity and Variable Importance
- valse: Variable Selection with Mixture of Models
- WLasso: Variable Selection for Highly Correlated Predictors


### 7.36 Sensitivity analysis and numerical derivatives

**Python software implementations**

List of packages and/or codes and/or frameworks and/or links:

- derivative: Numerical differentiation of noisy time series data
- higher: obtain higher order gradients
- jacobi: Numerical derivatives for Python
- JAX: toolkit by Google for composable transformations of Python+NumPy programs: differentiate, vectorize,
    JIT to GPU/TPU, and more
- OMSens: OpenModelica sensitivity analysis and optimization module
- PyApprox: high-dimensional approximation and uncertainty quantification by Sandia Labs
- SALib: Sensitivity Analysis Library (Contains Sobol, Morris, FAST, and other methods)
- sensitivity: Sensitivity Analysis
- tangent: library (by Google) for automatic differentiation providing Source-to-Source Debuggable Derivatives
    in Pure Python
- torchsde: Differentiable SDE solvers with GPU support and efficient sensitivity analysis

**R software implementations**

List of packages and/or codes and/or frameworks and/or links:

- bnmonitor: An Implementation of Sensitivity Analysis in Bayesian Networks
- GSA.UN: Global Sensitivity Analysis Tool
- reval: Argument Table Generation for Sensitivity Analysis
- samon: Sensitivity Analysis for Missing Data
- sensemakr: Sensitivity Analysis Tools for Regression Models
- sensitivity: Global Sensitivity Analysis of Model Outputs
- sensobol: Computation of Variance-Based Sensitivity Indices
- SWIM: Scenario Weights for Importance Measurement
- tornado: Plots for Model Sensitivity and Variable Importance

### 7.37 Statistics and Probability

**Python software implementations**

List of packages and/or codes and/or frameworks and/or links:

- distfit: probability density function fitting and hypothesis testing
- empiricaldist: empirical distribution functions
- momentum: Running mean, variance, skew, and kurtosis
- pingouin: Statistical package in Python based on Pandas
- probs: Probability library


- PyProbables: Probabilistic data structures in python
- PyStats: statistical analysis and distributions
- RunStats: Computing Statistics and Regression in One Pass
- statsmodels: statistical modeling and econometrics
- tensorflow-probability: Probabilistic reasoning and statistical analysis in TensorFlow
- wquantiles: Weighted quantiles

**R software implementations**

List of packages and/or codes and/or frameworks and/or links:

- arsenal: An Arsenal of ’R’ Functions for Large-Scale Statistical Summaries
- ashr: Methods for Adaptive Shrinkage, using Empirical Bayes
- confintr: Confidence Intervals
- DEM: The Distributed EM Algorithms in Multivariate Gaussian Mixture Models
- DescTools: Tools for Descriptive Statistics
- distr6: The Complete R6 Probability Distributions Interface
- distr: Object Oriented Implementation of Distributions
- distrEx: Extensions of Package ’distr’
- distributionsrd: Distribution Fitting and Evaluation
- DPQ: Density, Probability, Quantile (’DPQ’) Computations
- EasyDescribe: A Convenient Way of Descriptive Statistics
- entropy: Estimation of Entropy, Mutual Information and Related Quantities
- estimatr: Fast Estimators for Design-Based Inference
- evd: Functions for Extreme Value Distributions
- expectreg: Expectile and Quantile Regression
- fitur: Fit Univariate Distributions
- fromo: Fast Robust Moments
- Gmedian: Geometric Median, k-Medians Clustering and Robust Median PCA
- HSAUR3: A Handbook of Statistical Analyses Using R (3rd Edition)
- lmom: L-Moments
- lmomco: L-Moments, Censored L-Moments, Trimmed L-Moments, L-Comoments, and Many Distributions
- matrixdist: Statistics for Matrix Distributions
- MatrixModels: Modelling with Sparse and Dense Matrices
- matrixStats: Functions that Apply to Rows and Columns of Matrices (and to Vectors)
- minsample2: The Minimum Sample Size


- mlquantify: Algorithms for Class Distribution Estimation
- mvtnorm: Multivariate Normal and t Distributions
- NNS: Nonlinear nonparametric statistics using partial moments
- overlapping: Estimation of Overlapping in Empirical Distributions
- PCDimension: Finding the Number of Significant Principal Components
- philentropy: Similarity and Distance Quantification Between Probability Functions
- pls: Partial Least Squares and Principal Component Regression
- psre: Presenting Statistical Results Effectively
- Qest: Quantile-Based Estimator
- qp: Quantile parametrization for probability distribution functions
- RcppRoll: Efficient Rolling / Windowed Operations
- revss: Robust Estimation in Very Small Samples
- RobStatTM: Robust Statistics: Theory and Methods
- robustbase: Basic Robust Statistics
- roll: Rolling and Expanding Statistics
- statsExpressions: Tidy Dataframes and Expressions with Statistical Details
- walrus: Robust Statistical Methods
- weights: Weighting and Weighted Statistics

### 7.38 Stress testing, rare events, extreme values and scenarios, survival analysis

**Python software implementations**

List of packages and/or codes and/or frameworks and/or links:

- pyextremes: Extreme Value Analysis
- pycox is a python package for survival analysis and time-to-event prediction with PyTorch
- scikit-extremes: univariate extreme value calculations

**R software implementations**

List of packages and/or codes and/or frameworks and/or links:

- BMAmevt: Multivariate Extremes: Bayesian Estimation of the Spectral Measure
- climextRemes: Tools for Analyzing Climate Extremes
- extRemes: Extreme Value Analysis
- extremeStat: Extreme Value Statistics and Quantile Estimation
- evd: Functions for Extreme Value Distributions
- evmix: Extreme Value Mixture Modelling, Threshold Estimation and Boundary Corrected Kernel Density
    Estimation


- ExtremalDep: Extremal Dependence Models
- ExtremeRisks: Extreme Risk Measures
- lax: Loglikelihood Adjustment for Extreme Value Models
- lite: Likelihood-Based Inference for Time Series Extremes
- mev: Modelling of Extreme Values
- survivalmodels: Models for Survival Analysis

### 7.39 Symbolic regression & data-driven model discovery and machine learning

**Python software implementations**

List of packages and/or codes and/or frameworks and/or links:

- 2SEGP: Simple Simultaneous Ensemble Learning in Genetic Programming
- AIFeynman: Physics-Inspired Method for Symbolic Regression
- BindingGP: Symbolic Regression with Dimension Calculation
- Data Driven Symbolic Regression
- DEAP: Distributed Evolutionary Algorithms
- DeepSymReg: Neural Network-Based Symbolic Regression in Deep Learning for Scientific Discovery
- DeepSymRegTorch: PyTorch implementation of the EQL network, a neural network for symbolic regression
- Deep symbolic optimization
- diffeqpy: Solving differential equations in Python using DifferentialEquations.jl and the SciML Scientific
    Machine Learning organization
- ellyn: python-wrapped version of ellen, a linear genetic programming system for symbolic regression and
    classification
- EQLearner: A Seq2Seq approach to Symbolic Regression
- ffx: Fast Function Extraction for symbolic regressio
- geppy: framework for gene expression programming
- gplearn: Genetic Programming in Python, with a scikit-learn inspired API
- hal-cgp: Cartesian genetic programming
- Neural Symbolic Regression That Scales
- pyglyph: library based on deap providing abstraction layers for symbolic regression problems
- pymbolic: Easy Expression Trees and Term Rewriting
- PySR: High-Performance Symbolic Regression in Python
- PySINDy: sparse identification of nonlinear dynamical systems from data
- pySRURGS: Symbolic regression by uniform random global search
- salmon-lm: symbolic algebra of linear regression and modeling
- slearn: package linking symbolic representation with scikit-learn machine learning


- SR Bench: benchmark framework for symbolic regression
- SymEngine is a fast symbolic manipulation library
- symfit: Symbolic Fitting; fitting as it should be.
- symbolic experiments: Repository for symbolic regression/classification experiments
- Symbolic Regression Boosting
- Simpy: symbolic mathematics
- symreg: A Symbolic Regression engine

**R software implementations**

List of packages and/or codes and/or frameworks and/or links:

- DiffEqR: Solving differential equations in R using DifferentialEquations.jl and the SciML Scientific Machine
    Learning ecosystem
- gramEvol: Grammatical Evolution for R
- symbolicDA: Analysis of Symbolic Data
- symengine: Interface to the ’SymEngine’ Library

### 7.40 Testing (numerical, statistical, etc.), comparison and ranking

**Python software implementations**

List of packages and/or codes and/or frameworks and/or links:

- AutoTS: Automated Time Series Forecasting
- darts: toolkit by Unit8 for easy manipulation and forecasting of time series
- goftests: Generic goodness of fit tests for random plain old data
- hypothesize: hypothesis testing using robust statistics
- hypothetical: Hypothesis and statistical testing
- hyppo: multivariate hypothesis testing
- InvarianceUnitTests: Linear unit-tests for invariance discovery
- MAPIE: scikit-learn-compatible module for estimating prediction intervals.
- Merlion: A Machine Learning Framework for Time Series Intelligence by SalesForce
- permute: permutation tests and confidence sets
- PhiK: practical correlation constant that works consistently between categorical, ordinal and interval variables
- pingouin: Statistical package in Python based on Pandas
- responsible-ai-toolbox: Error Analysis dashboard, for identifying model errors and discovering cohorts of data
    for which the model underperforms.
- RunStats: Computing Statistics and Regression in One Pass
- scikit-learn: machine learning in Python
- statsmodels: statistical modeling and econometrics
- UltraNest: Fit and compare complex models reliably and rapidly. Advanced nested sampling.
- xskillscore: Metrics for verifying forecasts


**R software implementations**

List of packages and/or codes and/or frameworks and/or links:

- ACV: Optimal Out-of-Sample Forecast Evaluation and Testing under Stationarity
- amp: Statistical Test for the Multivariate Point Null Hypotheses
- ashr: Methods for Adaptive Shrinkage, using Empirical Bayes
- bayefdr: Bayesian Estimation and Optimisation of Expected False Discovery Rate
- BEST: Bayesian Estimation Supersedes the t-Test
- BFpack: Flexible Bayes Factor Testing of Scientific Expectations
- blocklength: Select an Optimal Block-Length to Bootstrap Dependent Data (Block Bootstrap)
- boot: Bootstrap Functions
- boot.pval: Bootstrap p-Values
- bootUR: Bootstrap Unit Root Tests
- CADFtest: A Package to Perform Covariate Augmented Dickey-Fuller Unit Root Tests
- ChangepointTesting: Change Point Estimation for Clustered Signals
- clusrank: Wilcoxon Rank Tests for Clustered Data
- cocor: Comparing Correlations
- corTESTsrd: Significance Testing of Rank Cross-Correlations under SRD
- CovTools: Statistical Tools for Covariance Analysis
- crossvalidationCP: Cross-Validation for Change-Point Regression
- crseEventStudy: A Robust and Powerful Test of Abnormal Stock Returns in Long-Horizon Event Studies
- cvCovEst: Cross-Validated Covariance Matrix Estimation
- cvms: Cross-Validation for Model Selection
- CVST: Fast Cross-Validation via Sequential Testing
- dgof: Discrete Goodness-of-Fit Tests
- digitTests: Tests for Detecting Irregular Digit Patterns
- DiscreteFDR: Multiple Testing Procedures with Adaptation for Discrete Tests
- dsos: Dataset Shift with Outlier Scores
- elo: Ranking Teams by Elo Rating and Comparable Methods
- energy: E-Statistics: Multivariate Inference via the Energy of Data
- exactRankTests: Exact Distributions for Rank and Permutation Tests
- FactorAssumptions: Set of Assumptions for Factor and Principal Component Analysis
- FAMT: Factor Analysis for Multiple Testing (FAMT) : Simultaneous Tests under Dependence in High-
    Dimensional Data
- fbst: The Full Bayesian Evidence Test, Full Bayesian Significance Test and the e-Value


- fdrci: Permutation-Based FDR Point and Confidence Interval Estimation
- FDRestimation: Estimate, Plot, and Summarize False Discovery Rates
- funtimes: Nonparametric estimators and tests for time series analysis
- fwb: Fractional Weighted Bootstrap
- fwildclusterboot: Fast Wild Cluster Bootstrap Inference for Linear Models
- gvlma: Global Validation of Linear Models Assumptions
- gt: Easily Create Presentation-Ready Display Tables
- gtExtras: Extending ’gt’ for Beautiful HTML Tables
- heplots: Visualizing Hypothesis Tests in Multivariate Linear Models
- HSAUR3: A Handbook of Statistical Analyses Using R (3rd Edition)
- htestClust: Reweighted Marginal Hypothesis Tests for Clustered Data
- ICtest: Estimating and Testing the Number of Interesting Components in Linear Dimension Reduction
- inferr: Inferential Statistics (parametric and non-parametric statistical tests)
- L2DensityGoFtest: Density Goodness-of-Fit Test
- locits: Test of Stationarity and Localized Autocovariance
- mashr: Multivariate Adaptive Shrinkage
- mcStats: Visualize Results of Statistical Hypothesis Tests
- melt: Multiple Empirical Likelihood Tests
- metrica: evaluate prediction performance of point-forecast models
- MixedIndTests: Tests of Randomness and Tests of Independence
- modeltime.resample: Resampling Tools for Time Series Forecasting
- MSTest: Hypothesis Testing for Markov Switching Models
- multDM: Multivariate Version of the Diebold-Mariano Test
- MultiFit: Multiscale Fisher’s Independence Test for Multivariate Dependence
- MultiHorizonSPA: Multi Horizon Superior Predictive Ability
- multiverse: ’Explorable Multiverse’ Data Analysis and Reports to show the robustness of statistical inference
- MVTests: Multivariate Hypothesis Tests and the confidence intervals
- nestedcv: Nested Cross-Validation with ’glmnet’ and ’caret’
- NonParRolCor: a Non-Parametric Statistical Significance Test for Rolling Window Correlation
- OOS: Out-of-Sample Time Series Forecasting
- origami: Generalized Framework for Cross-Validation
- OptSig: Optimal Level of Significance for Regression and Other Statistical Tests
- OPTtesting: Optimal Testing


- OutliersO3: Draws Overview of Outliers (O3) Plots
- pbo: Probability of Backtest Overfitting
- performance: Assessment of Regression Models Performance
- permutes: Permutation Tests for Time Series Data
- poolr: Methods for Pooling P-Values from (Dependent) Tests
- portes: Portmanteau Tests for Univariate and Multivariate Time Series Models
- randtoolbox: Toolbox for Pseudo and Quasi Random Number Generation and Random Generator Tests
- RDieHarder: R Interface to the ’DieHarder’ RNG Test Suite
- RDnp: Robust Test for Complete Independence in High-Dimensions
- rigr: Regression, Inference, and General Data Analysis Tools in R
- Rita: Automated Transformations, Normality Testing, and Reporting
- rmcorr: Repeated Measures Correlation
- RobustANOVA: Robust One-Way ANOVA Tests under Heteroscedasticity and Nonnormality
- robusTest: Calibrated Correlation, Two-Sample Tests
- rsample: General Resampling Infrastructure
- rstatix: Pipe-Friendly Framework for Basic Statistical Tests
- s2dverification: Set of Common Tools for Forecast Verification
- scoringfunctions: A Collection of Scoring Functions for Assessing Point Forecasts
- scoringRules: Scoring Rules for Parametric and Simulated Distribution Forecasts
- scoringutils: Utilities for Scoring and Assessing Predictions
- sdafilter: distribution free multiple testing rules for false discovery rate (FDR) control under general depen-
    dence
- sgof: Multiple Hypothesis Testing
- SHT: Statistical Hypothesis Testing Toolbox
- slider: Sliding Window Functions
- SlidingWindows: Methods for Time Series Analysis
- SPlit: Split a Dataset for Training and Testing
- splitTools: Tools for Data Splitting
- statsExpressions: Tidy Dataframes and tests (parametric, nonparametric, robust, etc)
- tidyposterior: Bayesian Analysis to Compare Models using Resampling Statistics
- tidystats: Save Output of Statistical Tests
- UnitStat: Performs Unit Root Test Statistics
- urca: Unit Root and Cointegration Tests for Time Series Data
- USP: U-Statistic Permutation Tests of Independence for all Data Types
- walrus: Robust Statistical Methods
- yardstick: Tidy Characterizations of Model Performance


### 7.41 Testing software codes

**Python software implementations**

List of packages and/or codes and/or frameworks and/or links:

- benchmark: microbenchmark support library
- bugsnag error monitoring and error reporting
- case: Python unittest Utilities
- cxxtest: CxxTest Unit Testing Framework
- dirty-equals: make python code (generally unit tests) more declarative and therefore easier to read and write.
- expectest: implements expect tests (also known as ”golden” tests)
- formencode: validation and form generation
- freezegun: allows your Python tests to travel through time by mocking the datetime module
- green: clean, colorful, fast python test runner
- Hypothesis: family of testing libraries which let you write tests parametrized by a source of examples
- Mamba Test Runner: definitive testing tool for Python
- mutattest: Safely run mutation trials without source code modifications and see what will get past your test
    suite.
- nose2: unittest with plugins.
- nox: Flexible test automation for Python
- partialtesting: toolkit by Man Group to run only the tests relevant for code changes
- playwright-python: Python version of the Playwright testing and automation library
- Pynguin: PYthoN General UnIt Test geNerator
- pyperformance: intended to be an authoritative source of benchmarks for all Python implementations
- pytest: easy to write small tests, yet scales to support complex functional testing
- pytest-benchmark: py.test fixture for benchmarking code
- pytest-check: pytest plugin that allows multiple failures per test.
- pytest-html: Plugin for generating HTML reports for pytest results
- pytest-parallel: pytest plugin for parallel and concurrent testing
- pytest-regressions: Pytest plugin for regression testing
- stestr: parallel Python test runner built around subunit
- TestSlide: test framework by Facebook
- testtools: extensions to the Python standard library’s unit testing framework.
- tox: Command line driven CI frontend and development task automation tool
- ward: modern test framework for Python with a focus on productivity and readability.


**R software implementations**

List of packages and/or codes and/or frameworks and/or links:

- exampletestr: Help for Writing Unit Tests Based on Function Examples
- melt: Multiple Empirical Likelihood Tests
- mockthat: Function Mocking for Unit Testing
- patrick: Parameterized Unit Testing by Google
- realtest: When Expectations Meet Reality: Realistic Unit Testing
- shinytest2: Testing for Shiny Applications
- testdat: Data Unit Testing for R
- testthat: Unit Testing for R
- testthis: Utils and ’RStudio’ Addins to Make Testing Even More Fun
- ttdo: Extend ’tinytest’ with ’diffobj’
- unitizer: Interactive R Unit Tests
- unittest: TAP-Compliant Unit Testing
- xpectr: Generates Expectations for ’testthat’ Unit Testing

### 7.42 Time series analysis and modeling

**Collections of resources**

List of links:

- Curated list with python packages for time series analysis
- Popular Python Time Series Packages
- Resources for working with time series and sequence data

**Python software implementations**

List of packages and/or codes and/or frameworks and/or links:

- Clairvoyance: Unified, End-to-End AutoML Pipeline for Medical Time Series
- darts: toolkit by Unit8 for easy manipulation and forecasting of time series
- DataGene: Identify How Similar TS Datasets Are to One Another
- deeptime: analysis of time series data including dimensionality reduction, clustering, and Markov model
    estimation
- EntropyHub: open-source toolkit for entropic time-series analysis.
- ETNA Time Series Library by Tinkoff AI
- fastreg: Fast sparse regressions with advanced formula syntax. OLS, GLM, Poisson, Maxlike, and more.
    High-dimensional fixed effects
- Featuretools: automated feature engineering
- glum: Generalized linear models


- hcrystalball: unifies the API for most commonly used libraries and modeling techniques for time-series fore-
    casting in the Python ecosystem
- HyperTools: toolbox for gaining geometric insights into high-dimensional data
- HyperTS: Full-Pipeline Automated Time Series (AutoTS) Analysis Toolkit
- kats: tookit by Facebook for time series analysis and forecasting
- KFAS: Kalman Filter and Smoother for Exponential Family State Space Models
- khiva-python: Python binding for Khiva library for time series analytics
- Loud ML: inference engine for metrics and events
- luminaire: ML driven solutions for monitoring time series data
- matrixprofile-ts: detect patterns and anomalies in massive datasets using Matrix Profile
- MatrixStats: Methods that Apply to Rows and Columns of Matrices (and to Vectors)
- mkl_fft: NumPy-based Python interface to Intel (R) MKL FFT functionality
- nixtla: Automated time series processing and forecasting
- pandas: data structures for data analysis, time series, and statistics
- pyFFTW is a pythonic wrapper around FFTW 3, the speedy FFT library
- pyFIt-SNE: FFT-accelerated Interpolation-based t-SNE (FIt-SNE)
- pyts: time series classification
- pytsal: Time Series analysis, visualization, forecasting along with AutoTS
- seglearn: machine learning for time series
- sktime: unified framework for machine learning with time series by UK national institute for data science and
    artificial intelligence
- slearn: package linking symbolic representation with scikit-learn machine learning
- statsmodels: statistical modeling and econometrics
- stumpy: variety of time series data mining tasks
- theft: Tools for Handling Extraction of Features from Time Series
- timemachines: Evaluation and standardization of popular time series packages
- timetk: A Tool Kit for Working with Time Series in R
- Traces: library for unevenly-spaced time series analysis
- tsai: time series tasks like classification, regression, forecasting, imputation
- tsam: time series aggregation module (tsam)
- ts-eval: Time Series analysis and evaluation tools
- tsfresh: extracts relevant characteristics from time series
- tslearn: machine learning toolkit dedicated to time-series data
- tspreprocess: package to preprocess time series
- tsmoothie: time-series smoothing and outlier detection in a vectorized way
- vectorbt: library for backtesting and analyzing trading strategies at scale


**R software implementations**

List of packages and/or codes and/or frameworks and/or links:

- ASSA: Applied Singular Spectrum Analysis
- astsa: Applied Statistical Time Series Analysis
- autostsm: Automatic Structural Time Series Models
- bdots: Bootstrapped Differences of Time Series
- bfast: Breaks for Additive Season and Trend
- bimets: Time Series and Econometric Modeling
- bootUR: Bootstrap Unit Root Tests
- ctbi: A Procedure to Clean, Decompose and Aggregate Timeseries
- energy: E-Statistics: Multivariate Inference via the Energy of Data
- entropy: Estimation of Entropy, Mutual Information and Related Quantities
- freqdom: Frequency Domain Based Analysis: Dynamic PCA
- funtimes: Functions for Time Series Analysis
- garchx: Flexible and Robust GARCH-X Modelling
- LMD: A Self-Adaptive Approach for Demodulating Multi-Component Signal
- LSTS: Locally Stationary Time Series
- lubridate: Make Dealing with Dates a Little Easier
- mcvis: Multi-Collinearity Visualization
- MixedIndTests: Tests of Randomness and Tests of Independence
- MTS: All-Purpose Toolkit for Analyzing Multivariate Time Series (MTS) and Estimating Multivariate Volatil-
    ity Models
- NonlinearTSA: Nonlinear Time Series Analysis
- nonlinearTseries: Nonlinear Time Series Analysis
- nortsTest: Assessing Normality of Stationary Process
- NTS: Nonlinear Time Series Analysis
- Rfssa: Functional Singular Spectrum Analysis
- rhosa: Higher-Order Spectral Analysis
- rrcov: Scalable Robust Estimators with High Breakdown Point
- rrMixture: Reduced-Rank Mixture Models
- Rssa: A Collection of Methods for Singular Spectrum Analysis
- rtrend: Trend Estimating Tools
- Rwave: Time-Frequency Analysis of 1-D Signals
- seastests: Seasonality Tests


- shrink: Global, Parameterwise and Joint Shrinkage Factor Estimation
- simts: Time Series Analysis Tools
- SLBDD: Statistical Learning for Big Dependent Data
- svars: Data-Driven Identification of SVAR Models
- tempdisagg: Temporal Disaggregation and Interpolation of Time Series
- theft: Tools for Handling Extraction of Features from Time Series
- TidyDensity: Functions for Tidy Analysis and Generation of Random Data
- timetk: A Tool Kit for Working with Time Series in R
- TSA: Time Series Analysis
- tsbox: Class-Agnostic Time Series
- tscopula: Time Series Copula Models
- tseries: Time Series Analysis and Computational Finance
- TSrepr: Time Series Representations
- tsrobprep: Robust Preprocessing of Time Series Data
- TSstudio: Functions for Time Series Analysis and Forecasting
- tsutils: Time Series Exploration, Modelling and Forecasting
- tsviz: Easy and Interactive Time Series Visualization
- vars: VAR Modelling
- xts: eXtensible Time Series

### 7.43 Text, sentiment and topic analytics (including NLP)

**Python software implementations**

- AllenNLP: toolkit by Allen Institute of Articial Intelligence for NLP research
- EmTract: Extracting Emotions from Social Media Text Tailored for Financial Contexts
- EvoMSA: Sentiment Analysis System based on B4MSA and EvoDAG
- fairseq: Facebook AI Research Sequence-to-Sequence Toolkit
- FastFormers: toolkit by Microsoft to achieve inference of Transformer models for Natural Language Under-
    standing
- gensim: topic modelling, document indexing and similarity retrieval with large corpora
- GPT-3: Language Models are Few-Shot Learners
- LIT: Language Interpretability Tool: Interactively analyze NLP models for model understanding
- LangTech Text Library (LTTL) is an open-source python package for text processing and analysis.
- Natural Language Processing Best Practices and Examples by Microsoft
- netts: toolkit by UK national institute for data science and artificial intelligence for creating networks cap-
    turing semantic content of speech transcripts


- nlpaug: Data augmentation for NLP
- nltk: Natural Language Toolkit
- pytext: A natural language modeling framework based on PyTorch
- PyTorch-NLP: Basic Utilities for PyTorch Natural Language Processing (NLP)
- Senta: Baidu’s open-source Sentiment Analysis System.
- spaCy: Industrial-strength Natural Language Processing (NLP) in Python
- stocksight: Stock market analyzer and predictor using Elasticsearch, Twitter, News headlines, NLP and
    sentiment analysis
- sumy: automatic summarization of text documents and HTML pages
- textacy: NLP, before and after spaCy
- vaderSentiment: VADER (Valence Aware Dictionary and sEntiment Reasoner) is a lexicon and rule-based
    sentiment analysis tool
- wordfreq: Access a database of word frequencies, in various natural languages.

**R software implementations**

- cleanNLP: Tidy Data Model for Natural Language Processing
- doc2concrete: Measuring Concreteness in Natural Language
- fastTextR: An Interface to the ’fastText’ Library
- globaltrends: Google Trends portal.
- lsa: Latent Semantic Analysis
- LSX: Model for Semisupervised Text Analysis Based on Word Embeddings
- meanr: Sentiment Analysis Scorer
- NLP: Natural Language Processing Infrastructure
- opitools: Analyzing the Opinions in a Big Text Document
- quanteda: Quantitative Analysis of Textual Data
- saotd: Sentiment Analysis of Twitter Data
- sentiment.ai: Simple Sentiment Analysis Using Deep Learning
- SentimentAnalysis: Dictionary-Based Sentiment Analysis
- sentimentr: Calculate Text Polarity Sentiment
- sentometrics: Integrated Framework for Textual Sentiment Time Series Aggregation and Prediction
- spacyr: Wrapper to the ’spaCy’ ’NLP’ Library
- sweater: Speedy Word Embedding Association Test and Extras Using R
- syuzhet: Extracts Sentiment and Sentiment-Derived Plot Arcs from Text
- tau: Text Analysis Utilities
- text2map: R Tools for Text Matrices, Embeddings, and Networks


- text2sdg: Detecting UN Sustainable Development Goals in Text
- text2vec: Modern Text Mining Framework for R
- texter: An Easy Text and Sentiment Analysis Library
- TextForecast: Regression Analysis and Forecasting Using Textual Data from a Time-Varying Dictionary
- textTinyR: Text Processing for Small or Big Data Files
- tidytext: Text Mining using ’dplyr’, ’ggplot2’, and Other Tidy Tools
- transforEmotion: Sentiment Analysis for Text and Qualitative Data
- tsentiment: Fetching Tweet Data for Sentiment Analysis
- Xplortext: Statistical Analysis of Textual Data

### 7.44 Uncertainty: analysis and modeling.

Links to resources

- Professionally curated list of awesome Conformal Prediction videos, tutorials, books, papers, PhD and MSc
    theses, articles and open-source libraries

**Python software implementations**

List of packages and/or codes and/or frameworks and/or links:

- Bumps: data fitting and uncertainty estimation
- conformal-rnn: code for ”Conformal time-series forecasting”, NeurIPS 2021
- crepes: Conformal Regressors and Conformal Predictive Systems
- EasyVVUQ: verification, validation and uncertainty quantification in high performance computing
- EnbPI: Ensemble batch prediction intervals
- EnCQR: ensemble conformalized quantile regression (EnCQR)
- MAPIE: scikit-learn-compatible module for estimating prediction intervals
- mystic: highly-constrained non-convex optimization and uncertainty quantification
- OpenTURNS (Open source initiative to Treat Uncertainties, Risks’N Statistics)
- PySloth: Probabilistic Prediction
- UncertaintyToolbox: predictive uncertainty quantification, calibration, metrics, and visualization
- UQpy: UQpy (Uncertainty Quantification with python) is a general purpose Python toolbox for modeling
    uncertainty in physical and mathematical systems

**R software implementations**

List of packages and/or codes and/or frameworks and/or links:

- bootComb: Combine Parameter Estimates via Parametric Bootstrap


### 7.45 Visualization and reporting

**Python software implementations**

List of packages and/or codes and/or frameworks and/or links:

- Algviz is an algorithm visualization tool for your Python code
- appmode: Jupyter extension that turns notebooks into web applications
- Best of Streamlit
- clustergram: Visualization and diagnostics for cluster analysis in Python
- dash: framework for building ML and data science web apps
- dash-extensions:extensions to the Plotly Dash framework
- D-tale:Visualizer by Man Group for pandas data structures
- FlameScope: visualization ny Netflix for exploring different time ranges as Flame Graphs.
- HyperTools: toolbox for gaining geometric insights into high-dimensional data
- ipyslides: Create Interactive Slides in Jupyter Notebook with all kind of rich content
- itables: Pandas DataFrames as Interactive DataTables
- Lux: automate the visualization and data analysis process
- Markdown: Python implementation of markdown
- matplotlib: omprehensive library for creating static, animated, and interactive visualizations
- mpl-animators: interative animation framework for matplotlib
- Orange: Interactive data analysis
- plotly: graphing library makes interactive, publication-quality graphs
- Plotly Resampler: Visualize large time-series data in plotly
- plotnine: A grammar of graphics for Python
- plottable: Beautifully customized tables with matplotlib
- psyplot: interactive data visualization
- PyGraphistry: quickly load, shape, embed, and explore big graphs with the GPU-accelerated Graphistry
    visual graph analyzer
- PyMetis: Python wrapper around Metis, a graph partitioning package
- PyShiny: Shiny for Python
- pyvis: visualizing interactive network graphs
- seaborn: statistical data visualization
- seaborn analyzer: data analysis and visualization tool using Seaborn library
- streamlit: fastest way to build and share data apps
- tensorboard: TensorFlow’s Visualization Toolkit
- torchsde: Differentiable SDE solvers with GPU support and efficient sensitivity analysis


- tourr: Tour Methods for Multivariate Data Visualisation
- Vega-Altair is a declarative statistical visualization library for Pytho
- VisPy: interactive scientific visualization in Python
- visdom: lexible tool for creating, organizing, and sharing visualizations of live, rich data

**R software implementations**

List of packages and/or codes and/or frameworks and/or links:

- apexcharter: Create Interactive Chart with the JavaScript ’ApexCharts’ Library
- autoplotly: Automatic Generation of Interactive Visualizations for Statistical Results
- classmap: Visualizing Classification Results
- cleanrmd: Clean Class-Less ’R Markdown’ HTML Documents
- clustree: Visualise Clusterings at Different Resolutions
- ComplexUpset: Create Complex UpSet Plots Using ’ggplot2’ Components
- condformat: Conditional Formatting in Data Frames
- conductor: Create Tours in ’Shiny’ Apps Using ’Shepherd.js’
- d3po: Fast and Beautiful Interactive Visualization for ’Markdown’ and ’Shiny’
- DataVisualizations: Visualizations of High-Dimensional Data
- descriptr: Generate Descriptive Statistics
- DT: A Wrapper of the JavaScript Library ’DataTables’
- echarty: Minimal R/Shiny Interface to JavaScript Library ’ECharts’
- esquisse: Explore and Visualize Your Data Interactively
- fmtr: Easily Apply Formats to Data
- ggalluvial: Alluvial Plots in ’ggplot2’
- GGally: Extension to ’ggplot2’
- gganimate: A Grammar of Animated Graphics
- ggbreak: Set Axis Break for ’ggplot2’
- ggcharts: Shorten the Distance from Data Visualization Idea to Actual Plot
- ggcorrplot: Visualization of a Correlation Matrix using ’ggplot2’
- ggcorset: The Corset Plot
- ggdag: Analyze and Create Elegant Directed Acyclic Graphs
- ggdist: Visualizations of Distributions and Uncertainty
- ggDoubleHeat: A Heatmap-Like Visualization Tool
- ggeffects: Create Tidy Data Frames of Marginal Effects for ’ggplot’ from Model Outputs
- ggESDA: Exploratory Symbolic Data Analysis with ’ggplot2’


- ggfocus: Scales that Focus Specific Levels in your ggplot
- ggforce: Accelerating ’ggplot2’
- ggformula: Formula Interface to the Grammar of Graphics
- ggfortify: Data Visualization Tools for Statistical Analysis Results
- gghdr: Visualisation of Highest Density Regions in ’ggplot2’
- ggheatmap: Plot Heatmap
- gghighlight: Highlight Lines and Points in ’ggplot2’
- ggh4x: Hacks for ’ggplot2’
- ggiraph: Make ’ggplot2’ Graphics Interactive
- ggmatplot: Plot Columns of Two Matrices Against Each Other Using ’ggplot2’
- ggmice: Visualizations for ’mice’ with ’ggplot2’
- ggmosaic: Mosaic Plots in the ’ggplot2’ Framework
- ggmulti: High Dimensional Data Visualization
- ggnetwork: Geometries to Plot Networks with ’ggplot2’
- ggpattern: ’ggplot2’ Pattern Geoms
- ggpie: pie, donut and rose pie plots with ggplot2
- ggplot2: Create Elegant Data Visualisations Using the Grammar of Graphics
- ggplotify: Convert Plot to ’grob’ or ’ggplot’ Object
- ggpmisc: Miscellaneous Extensions to ’ggplot2’
- ggpubr: ’ggplot2’ Based Publication Ready Plots
- ggpval: Annotate Statistical Tests for ’ggplot2’
- ggquickeda: Quickly Explore Your Data Using ’ggplot2’ and ’table1’ Summary Tables
- ggside extends ’ggplot2’ by allowing users to add graphical information about one of the main panel’s axis
    using a familiar ’ggplot2’ style API with tidy data
- ggsignif: Significance Brackets for ’ggplot2’
- ggstance: Horizontal ’ggplot2’ Components
- ggstar: Multiple Geometric Shape Point Layer for ’ggplot2’
- ggstatsplot: ’ggplot2’ Based Plots with Statistical Details
- ggthemes: Extra Themes, Scales and Geoms for ’ggplot2’
- ggtrace: Provides ggplot2 geoms that allow groups of data points to be outlined or highlighted for emphasis
- gluedown: Wrap Vectors in Markdown Formatting
- gridstackeR: easy way to create responsive layouts with just a few lines of code using gridstack.js
- gt: Easily Create Presentation-Ready Display Tables
- gtExtras: additional functions for creating tables with gt


- gtsummary: Presentation-Ready Data Summary and Analytic Result Tables
- heatmaply: Interactive Cluster Heat Maps Using ’plotly’ and ’ggplot2’
- heplots: Visualizing Hypothesis Tests in Multivariate Linear Models
- htmlTable: Advanced Tables for Markdown/HTML
- huxtable: Easily Create and Style Tables for LaTeX, HTML and Other Formats
- jjAnno: An Annotation Package for ’ggplot2’ Output
- kableExtra: Construct Complex Table with ’kable’ and Pipe Syntax
- listdown: Create R Markdown from Lists
- loon: Interactive Statistical Data Visualization
- loon.ggplot: A Grammar of Interactive Graphics
- magick: Advanced Graphics and Image-Processing in R
- memoiR: R Markdown and Bookdown Templates to Publish Documents
- ndtv: Network Dynamic Temporal Visualizations
- numform: Tools to Format Numbers for Publication
- performance: Assessment of Regression Models Performance
- plot.matrix: Visualizes a Matrix as Heatmap
- presenter: Present Data with Style
- prompter: Add Tooltips in ’Shiny’ Apps with ’Hint.css’
- psre: Presenting Statistical Results Effectively
- quarto: R Interface to ’Quarto’ Markdown Publishing System
- r2resize: In-Text Resizing for Containers, Images and Data Tables in ’Shiny’, ’Markdown’ and ’Quarto’
    Documents
- r3js: allow WebGL-based 3D plotting using the three.js library
- reactR: Make it easy to use ’React’ in R with ’htmlwidget’ scaffolds
- reporter: Creates Statistical Reports
- rheroicons: A Zero Dependency ’SVG’ Icon Library for ’Shiny’
- rhino: A Framework for Enterprise Shiny Applications
- rintrojs: Wrapper for the ’Intro.js’ Library
- rmarkdown: Dynamic Documents for R
- rsvg: Render SVG Images into PDF, PNG, (Encapsulated) PostScript, or Bitmap Arrays
- semantic.dashboard: Dashboard with Fomantic UI Support for Shiny
- shapviz: visualize SHapley Additive exPlanations (SHAP) - waterfall, force, importance, dependence plots
- shiny: Web Application Framework for R
- shinyChakraUI: A Wrapper of the ’React’ Library ’Chakra UI’ for ’Shiny’


- shinydlplot: Add a Download Button to a ’shiny’ Plot or ’plotly’
- shinyHugePlot: Efficient Plotting of Large-Sized Data
- shinyMobile: Mobile Ready ’shiny’ Apps with Standalone Capabilities
- shinySelect: A Wrapper of the ’react-select’ Library
- shiny.semantic: Semantic UI Support for Shiny
- shinytest: Test Shiny Apps
- shinyWidgets: Custom Inputs Widgets for Shiny
- starry: Explore Data with Plots and Tables
- statsExpressions: Tidy Dataframes and Expressions with Statistical Details
- sugrrants: Supporting Graphs for Analysing Time Series
- tidybayes: Tidy Data and ’Geoms’ for Bayesian Models
- tidycharts: Generate Tidy Charts Inspired by ’IBCS’
- tidyHeatmap: A Tidy Implementation of Heatmap
- tourr: Tour Methods for Multivariate Data Visualisation
- tornado: Plots for Model Sensitivity and Variable Importance
- trelliscopejs: Create Interactive Trelliscope Displays
- tsviz: Easy and Interactive Time Series Visualization
- UpSetR: A More Scalable Alternative to Venn and Euler Diagrams for Visualizing Intersecting Sets
- visNetwork: Network Visualization using ’vis.js’ Library
- visStatistics: Automated Visualization of Statistical Tests
- vtable: Variable Table for Variable Documentation
- xaringan: Presentation Ninja
- yardstick: Tidy Characterizations of Model Performance

## 8 Codes for QWIM (Quantitative Wealth and Investment Management)

## ment)

### 8.1 Collections of resources

List of links:

- Curated list of practical financial machine learning tools and applications
- EliteQuant: online resources for quantitative modeling, trading, portfolio management


### 8.2 Research studies with code

Ardia et al. (“RiskPortfolios: Computation of Risk-Based Portfolios in R,” 2017)
Boileau et al. (“cvCovEst: Cross-validated covariance matrix estimator selection and evaluation in R,” 2021)
Brugiere ( _Quantitative Portfolio Management with Applications in Python_ , 2020)
Bryzgalova et al. (“Forest Through the Trees: Building Cross-Sections of Stock Returns,” 2021)
Cajas (“Entropic Portfolio Optimization: a Disciplined Convex Programming Framework,” 2021)
Cajas (“OWA Portfolio Optimization: a Disciplined Convex Programming Framework,” 2021)
Chen and Zimmermann (“Open Source Cross-Sectional Asset Pricing,” 2022)
Chib ( _R package czfactor_ , 2020)
Chib and Zhao ( _R package czzg_ , 2020)
Coqueret and Guida ( _Machine Learning for Factor Investing: R Version_ , 2020)
Coqueret ( _Perspectives in sustainable equity investing (website version)_ , 2022)
de Carvalho and Rua (“Real-time nowcasting the US output gap: Singular spectrum analysis at work,” 2017)
Ding et al. (“A Python package for multi-stage stochastic programming,” 2020)
Dixon et al. ( _Machine Learning in Finance: from theory to practice_ , 2020)
Dixon and Polson (“Deep Fundamental Factor Models,” 2020)
Dong et al. (“Anomalies and the expected market return,” 2022)
Guijarro-Ordonez et al. (“Deep Learning Statistical Arbitrage,” 2021)
Gurdogan and Kercheval (“Multi Anchor Point Shrinkage for the Sample Covariance Matrix (Extended Ver-
sion),” 2021)
Ho et al. (“Moving beyond P values: data analysis with estimation graphics,” 2019)
Irlam (“Multi Scenario Financial Planning via Deep Reinforcement Learning AI,” 2020)
Irlam ( _AI Planner_ , 2020)
Irlam (“Machine learning for retirement planning,” 2020)
Jansen ( _Machine Learning for Algorithmic Trading (Second Edition)_ , 2020)
Kakushadze and Yu (“Statistical Risk Models,” 2016)
Kakushadze and Yu (“Open Source Fundamental Industry Classification,” 2017)
Kakushadze and Yu (“Betas, Benchmarks, and Beating the Market,” 2018)
Kakushadze and Yu (“Decoding stock market with quant alphas,” 2018)
Kakushadze and Yu (“Machine learning risk models,” 2019)
Kakushadze and Yu (“Machine learning treasury yields,” 2020)
Lai et al. (“TODS: An Automated Time Series Outlier Detection System,” 2021)
Lettau and Pelger (“Factors That Fit the Time Series and Cross-Section of Stock Returns,” 2020)
Li et al. (“FinRL-Podracer: High Performance and Scalable Deep Reinforcement Learning for Quantitative
Finance,” 2021)
Liu et al. (“FinRL: Deep Reinforcement Learning Framework to Automate Trading in Quantitative Finance,”
2021)
Liu et al. (“FinRL-Meta: A Universe of Near-Real Market Environments for Data-Driven Deep Reinforcement
Learning in Quantitative Finance,” 2022)
Marinescu (“Risk-Based Optimal Portfolio Strategies: A Compendium,” 2022)
Martin (“PyPortfolioOpt: portfolio optimization in Python,” 2021)
Marwood and Minnen (“Safely Boosting Retirement Income by Harmonizing Drawdown Paths,” 2020)
McIndoe (“A Data Driven Approach to Market Regime Classification,” 2020)
Micheli and Neuman (“Evidence of Crowding on Russell 3000 Reconstitution Events,” 2022)
Milevsky ( _Retirement Income Recipes in R: From Ruin Probabilities to Intelligent Drawdowns_ , 2020)
Qian et al. (“Combining forecasts for universally optimal performance,” 2022)
Rao and Jelvis ( _Foundations of Reinforcement Learning with Applications in Finance_ , 2022)
Sarmas et al. ( _Multicriteria Portfolio Construction with Python_ , 2020)
Sharma et al. (“DoWhy: Addressing Challenges in Expressing and Validating Causal Assumptions,” 2021)
Shi et al. (“Deep Learning Algorithms for Hedging with Frictions,” 2022)
Siebert et al. (“A systematic review of Python packages for time series analysis,” 2021)
Simos et al. (“Time-varying Black–Litterman portfolio optimization using a bio-inspired approach and neu-
ronets,” 2021)
Snow (“Machine learning in asset management,” 2019)


Snow (“Machine Learning in Asset Management Part 1: Portfolio Construction Trading Strategies,” 2020)
Snow (“Machine Learning in Asset Management - Part 2: Portfolio Construction - Weight Optimization,” 2020)
Tatsat et al. ( _Machine Learning and Data Science Blueprints for Finance: From Building Trading Strategies to
Robo-Advisors Using Python_ , 2020)
Tuck et al. (“Portfolio Construction Using Stratified Models,” 2022)
Ungolo et al. (“affine_mortality: A Github repository for estimation, analysis, and projection of affine mortality
models,” 2021)
Vamossy and Skog (“EmTract: Investor Emotions and Market Behavior,” 2021)
Vinod (“R Package GeneralCorr Functions for Portfolio Choice,” 2021)
Yang et al. (“FinBERT: A Pretrained Language Model for Financial Communications,” 2020)
Yu et al. (“An AI approach to measuring financial risk,” 2020)

### 8.3 Python software implementations.

List of packages and/or codes and/or frameworks and/or links:

- alive-progress: new kind of Progress Bar, with real-time throughput, ETA, and very cool animations
- alphalens: Performance analysis of predictive (alpha) stock factors
- AlphaPy: Automated Machine Learning [AutoML] with Python, scikit-learn, Keras, XGBoost, LightGBM,
    and CatBoost
- auquantoolbox: Backtesting toolbox for trading strategies
- azapy: Financial Portfolio Optimization Algorithms
- bt: flexible backtesting framework
- btgym: Scalable, event-driven, deep-learning-friendly backtesting library
- Clairvoyant: identify and monitor social/historical cues for short term stock movement
- CVXPortfolio: Portfolio optimization and simulation
- cyanure: Toolbox for Empirical Risk Minimization
- Elegant-FinRL: algorithmic strategies using Reinforcement Learning
- Empyrial: AI and data-driven quantitative portfolio management for risk and performance analytics
- empyrical: Common financial risk and performance metrics
- EmTract: Extracting Emotions from Social Media Text Tailored for Financial Contexts
- ffn: Financial functions for Python
- FinDataPy: download market data via Bloomberg, Eikon, Quandl, Yahoo etc.
- FinMarketPy: backtesting trading strategies and analyzing financial markets
- finnhub-python: Finnhub Python API Client to provide financial data(real-time stock price, global funda-
    mentals, global ETFs holdings and alternative data)
- FinRL: Deep Reinforcement Learning for Quantitative Finance
- FinRL-Meta: Universe of Near-Real Market Environments for Data-Driven Financial Reinforcement Learning
- fredapi is a Python interface to the Federal Reserve Economic Data (FRED) and ALFRED databases
- lifelib: Actuarial models in Python
- lifelines: Survival analysis in Python, including Kaplan Meier, Nelson Aalen and regression


- lrsm_portfolio: Portfolio Construction using Stratified Models
- Machine Learning and Data Science Blueprints for Finance (codes for the book)
- Machine Learning fior asset management
- Machine Learning for Algorithmic Trading (codes for the book)
- MLFinLab: Machine Learning Financial Laboratory
- momentum: Running mean, variance, skew, and kurtosis
- Multicriteria Portfolio Construction with Python
- okama: investment portfolio analyzing and optimization tools
- OpenBBTerminal: modern Python-based integrated environment for investment research
- OptimalPortfolio: portfolio optimization
- QuantAxis: Quantitative Financial FrameWork
- QuantEcon: quantitative economics
- Pandas TA: Technical Analysis Indicators
- portfolio-backtest: backtest portfolio asset allocation
- precise: online covariance and precision forecasting, portfolios, and model ensembles
- predictionrevisited: implements the core statistical concepts from the book ”Prediction Revisited: The Im-
    portance of Observation”
- pyfinance: general financial and security returns analysis
- pyfolio: Portfolio and risk analytics in Python
- pyhrp: hierarchical risk parity algorithms
- PyPortfolioOpt: Financial portfolio optimisation
- Qlib: Microsoft AI-oriented quantitative investment platform
- QuantEcon.py: quantitative economics
- QuantLib: Python bindings for the QuantLib library
- QuantResearch: Quantitative analysis, strategies and backtests
- Quantropy: Financial pipeline for the data-driven investor to research, develop and deploy robust strategie
- QuantStats: Portfolio analytics for quants
- Riskfolio-Lib: Portfolio Optimization and Quantitative Strategic Asset Allocation
- Robust Risk-aware reinforcement learning
- stocksight: Stock market analyzer and predictor using Elasticsearch, Twitter, News headlines, NLP and
    sentiment analysis
- ta: Technical Analysis Library using Pandas and Numpy
- TA-lib: Python wrapper for TA-Lib Technical Analysis Library
- Tax-Calculator: USA Federal Individual Income and Payroll Tax Microsimulation Model
- tf-quant-finance: High-performance TensorFlow library by Google for quantitative finance.
- vectorbt: Supercharged backtesting and technical analysis for quants
- zipline: Algorithmic Trading Library


### 8.4 R software implementations

List of packages and/or codes and/or frameworks and/or links:

- ASSA: Applied Singular Spectrum Analysis
- AssetAllocation: Backtesting Simple Asset Allocation Strategies
- BEKKs: Multivariate Conditional Volatility Modelling and Forecasting
- crseEventStudy: A Robust and Powerful Test of Abnormal Stock Returns in Long-Horizon Event Studies
- DOSPortfolio: Dynamic Optimal Shrinkage Portfolio
- ExtremeRisks: Extreme Risk Measures
- FFdownload: Download Data from Kenneth French’s Website
- FinnTS: Microsoft Finance Time Series Forecasting Framework
- finreportr: Financial Data from U.S. Securities and Exchange Commission
- fHMM: Fitting Hidden Markov Models to Financial Data
- FinnTS: Microsoft Finance Time Series Forecasting Framework
- fitHeavyTail: Mean and Covariance Matrix Estimation under Heavy Tails
- fixedincome: Fixed Income Models, Calculations, Data Structures and Instruments
- generalCorr: Generalized Correlations, Causal Paths and Portfolio Selection
- greeks: Sensitivities of Prices of Financial Options
- HDShOP: High-Dimensional Shrinkage Optimal Portfolios
- HierPortfolios: Hierarchical Clustering-Based Portfolio Allocation Strategies
- highOrderPortfolios: Design of High-Order Portfolios via Mean, Variance, Skewness, and Kurtosis
- imputeFin: Imputation of Financial Time Series with Missing Values and/or Outliers
- MarkowitzR: Statistical Significance of the Markowitz Portfolio
- MortCast: Estimation and Projection of Age-Specific Mortality Rates
- parma: Portfolio Allocation and Risk Management Applications
- pbo: Probability of Backtest Overfitting
- pec: Prediction Error Curves for Risk Prediction Models in Survival Analysis
- pedquant: Public Economic Data and Quantitative Analysis
- PerformanceAnalytics: Econometric Tools for Performance and Risk Analysis
- PortfolioAnalytics: Portfolio Analysis, Including Numerical Methods for Optimization of Portfolios
- portfolioBacktest: Automated Backtesting of Portfolios over Multiple Datasets
- portvine: portfolio level risk estimates using ARMA-GARCH and vine copulas
- priceR: Economics and Pricing Tools
- qlcal: R Bindings to the Calendaring Functionality of ’QuantLib’


- qrmtools: Tools for Quantitative Risk Management
- quantmod: Quantitative Financial Modelling Framework
- RcppQuantuccia: R Bindings to the Calendaring Functionality of ’QuantLib’
- riskParityPortfolio: Design of Risk Parity Portfolios
- RiskPortfolios: Computation of Risk-Based Portfolios
- riskRegression: Risk Regression Models and Prediction Scores for Survival Analysis with Competing Risks
- RPESE: Estimates of Standard Errors for Risk and Performance Measures
- RQuantLib: R Interface to the ’QuantLib’ Library
- SharpeR: Statistical Significance of the Sharpe Ratio
- sharpeRratio: Moment-Free Estimation of Sharpe Ratios
- sparseIndexTracking: Design of Portfolio of Stocks to Track an Index
- SWIM: Scenario Weights for Importance Measurement
- TextForecast: Regression Analysis and Forecasting Using Textual Data from a Time-Varying Dictionary
- tidyquant: Tidy Quantitative Financial Analysis
- Trading: CCR, Advanced Correlation & Beta Estimates, Betting Strategies
- tseries: Time Series Analysis and Computational Finance
- ufRisk: Risk Measure Calculation in Financial TS
- usincometaxes: wrapper to the NBER’s TAXSIM 35 tax simulator for federal and state income taxes
- ycevo: Nonparametric Estimation of the Yield Curve Evolution
- yfR: Downloads and Organizes Financial Data from Yahoo Finance


## References

Abhyankar, A. and Wu, Y. (2020).“Circus Ring to Zoo to Museum: The Fragility of Factors in Characteristic-based
Asset Pricing Models.” In: _SSRN e-Print_.
Ahmed, S., Bu, Z., and Tsvetanov, D. (2019).“Best of the Best: A Comparison of Factor Models.” In: _Journal of
Financial and Quantitative Analysis_ 54(4), pp. 1713–1758.
Alexander, C., Coulon, M., Han, Y., and Meng, X. (2021).“Evaluating the Discrimination Ability of Proper Mul-
tivariate Scoring Rules.” In: _arXiv e-Print_.
Alexandrov, A., Benidis, K., Bohlke-Schneider, M., Flunkert, V., Gasthaus, J., Januschowski, T., Maddix, D. C.,
Rangapuram, S., Salinas, D., Schulz, J., Stella, L., Turkmen, A. C., and Wang, Y. (2020).“GluonTS: Probabilistic
and Neural Time Series Modeling in Python.” In: _Journal of Machine Learning Research_ 21(116), pp. 1–6.
Alhnaity, B. and Abbod, M. (2020).“A new hybrid financial time series prediction model.” In: _Engineering Appli-
cations of Artificial Intelligence_ 95, p. 103873.
Allende, H. and Valle, C. (2017).“Ensemble methods for time series forecasting.” In: _Claudio Moraga: A Passion for
Multi-Valued Logic and Soft Computing_. Ed. by R. Seising and H. Allende-Cid. Vol. 349. Springer International
Publishing, pp. 217–232.
Anghel, D. G. (2021).“Data Snooping Bias in Tests of the Relative Performance of Multiple Forecasting Models.”
In: _Journal of Banking & Finance_ 126, p. 106113.
Ankile, L. L. and Krange, K. (2022). “The DONUT Approach to Ensemble Combination Forecasting.” In: _arXiv
e-Print_.
Ansari, A. F., Benidis, K., Kurle, R., Turkmen, A. C., Soh, H., Smola, A. J., Wang, Y., and Januschowski, T.
(2021). “Deep Explicit Duration Switching Models for Time Series.” In: _arXiv e-Print_.
Aparicio, D. and Lopez de Prado, M. (2018).“How Hard Is It to Pick the Right Model? MCS and backtest
overfitting.” In: _Algorithmic Finance_ 7, pp. 53–61.
Ardia, D., Boudt, K., and Gagnon-Fleury, J.-P. (2017).“RiskPortfolios: Computation of Risk-Based Portfolios in
R.” In: _The Journal of Open Source Software_ 2(10), pp. 171+.
Ardia, D. and Dufays, A. (2021).“Measuring uncertainty and uncertainty dispersion from a large set of model
predictions.” In: _SSRN e-Print_.
Arias-Calluari, K., Alonso-Marroquin, F., Najafi, M. N., and Harré, M. (2021).“Methods for forecasting the effect
of exogenous risks on stock markets.” In: _Physica A: Statistical Mechanics and its Applications_ 568, p. 125587.
Arnold, S., Henzi, A., and Ziegel, J. F. (2022). “Sequentially valid tests for forecast calibration.” In: _arXiv e-Print_.
Arvanitis, S., Post, T., Potı̀, V., and Karabati, S. (2021).“Nonparametric tests for Optimal Predictive Ability.” In:
_International Journal of Forecasting_ 37(2), pp. 881–898.
Ashouri, M., Hyndman, R. J., and Shmueli, G. (2022).“Fast Forecast Reconciliation Using Linear Models.” In:
_Journal of Computational and Graphical Statistics_.
Athanasopoulos, G., Gamakumara, P., Panagiotelis, A., Hyndman, R. J., and Affan, M. (2019).“Hierarchical
Forecasting.” In: _Macroeconomic Forecasting in the Era of Big Data_. Springer International Publishing, pp. 689–
719.
Athanasopoulos, G. and Kourentzes, N. (2020). _On the evaluation of hierarchical forecasts_. Tech. rep. Monash
University.
Atiya, A. F. (2020).“Why does forecast combination work so well?” In: _International Journal of Forecasting_ 36(1),
pp. 197–200.
Babiak, M. and Barunik, J. (2020).“Deep Learning, Predictability, and Optimal Portfolio Returns.” In: _SSRN
e-Print_.
Babii, A., Ball, R. T., Ghysels, E., and Striaukas, J. (2021).“Machine Learning Panel Data Regressions with
Heavy-tailed Dependent Data: Theory and Application.” In: _SSRN e-Print_.
Bacher, P., Bergsteinsson, H. G., Frolke, L., Sorensen, M. L., Lemos-Vinasco, J., Liisberg, J., Moller, J. K., Nielsen,
H. A., and Madsen, H. (2022). “onlineforecast: An R package for adaptive and recursive forecasting.” In: _arXiv
e-Print_.
Bacon, C. R. (2019).“Performance Attribution: History and Progress.” In: _CFA Institute Research Foundation
Publications_.
Bahrami, A., Shamsuddin, A., and Uylangco, K. (2019).“Are advanced emerging market stock returns predictable?
A regime-switching forecast combination approach.” In: _Pacific-Basin Finance Journal_ 55, pp. 142–160.


Bailey, N., Kapetanios, G., and Pesaran, M. H. (2020).“Measurement of Factor Strength: Theory and Practice.”
In: _SSRN e-Print_.
Baitinger, E. and Flegel, S. (2021).“New Concepts in Financial Forecasting: Network-Based Information, Topolog-
ical Data Analysis and their Combination.” In: _SSRN e-Print_.
Bali, T. G., Goyal, A., Huang, D., Jiang, F., and Wen, Q. (2021).“Different Strokes: Return Predictability Across
Stocks and Bonds with Machine Learning and Big Data.” In: _SSRN e-Print_.
Baltas, N. and Karyampas, D. (2020).“Forecasting the Equity Risk Premium: The Importance of Regime-Dependent
Evaluation.” In: _SSRN e-Print_.
Baltussen, G., Martens, M., and Penninga, O. (2020).“Predicting Bond Returns: 70 Years of International Evidence.”
In: _SSRN e-Print_.
Baltussen, G., Martens, M., and Penninga, O. (2021).“Predicting Bond Returns: 70 Years of International Evidence.”
In: _Financial Analysts Journal_ 77(3), pp. 133–155.
Bandara, K., Bergmeir, C., and Smyl, S. (2020).“Forecasting across time series databases using recurrent neu-
ral networks on groups of similar series: A clustering approach.” In: _Expert Systems with Applications_ 140,
pp. 112896+.
Bandara, K., Hewamalage, H., Liu, Y.-H., Kang, Y., and Bergmeir, C. (2021).“Improving the accuracy of global
forecasting models using time series data augmentation.” In: _Pattern Recognition_ 120, p. 108148.
Barillas, F. and Shanken, J. (2019).“Real-time Portfolio Choice Implications of Asset Pricing Models.” In: _Consor-
tium on Factor Investing Conference_. Vol. 73.
Barras, L. (2019).“A large-scale approach for evaluating asset pricing models.” In: _Journal of Financial Economics_
134(3), pp. 549–569.
Barrow, D. K. and Crone, S. F. (2016).“A comparison of AdaBoost algorithms for time series forecast combination.”
In: _International Journal of Forecasting_ 32(4), pp. 1103–1119.
Bates, S., Hastie, T., and Tibshirani, R. (2021).“Cross-validation: what does it estimate and how well does it do
it?” In: _arXiv e-Print_.
Bauer, A., Zufle, M., Herbst, N., Kounev, S., and Curtef, V. (2020).“Telescope: An Automatic Feature Extraction
and Transformation Approach for Time Series Forecasting on a Level-Playing Field.” In: _Proceedings of the 36th
International Conference on Data Engineering (ICDE)_ , pp. 1902–1905.
Bektic, D., Hachenberg, B., and Schiereck, D. (2020).“Factor-based investing in government bond markets: a survey
of the current state of research.” In: _Journal of Asset Management_ 21, pp. 94–105.
Ben Baccar, Y. (2019).“Comparative Study on Time Series Forecasting Models.” en. MA thesis. ParisTech.
Benidis, K., Rangapuram, S. S., Flunkert, V., Wang, B., Maddix, D., Turkmen, C., Gasthaus, J., Bohlke-Schneider,
M., Salinas, D., Stella, L., Callot, L., and Januschowski, T. (2020).“Neural forecasting: Introduction and liter-
ature overview.” In: _arXiv e-Print_.
Berardi, A., Markovich, M., Plazzi, A., and Tamoni, A. (2021).“Mind the (Convergence) Gap: Bond Predictability
Strikes Back!” In: _Management Science_.
Bergmeir, C., Triguero, I., Molina, D., Aznarte, J. L., and Benitez, J. M. (2012).“Time Series Modeling and Fore-
casting Using Memetic Algorithms for Regime-Switching Models.” In: _IEEE Transactions on Neural Networks
and Learning Systems_ 23(11), pp. 1841–1847.
Bergmeir, C., Hyndman, R. J., and Koo, B. (2018).“A note on the validity of cross-validation for evaluating
autoregressive time series prediction.” In: _Computational Statistics & Data Analysis_ 120, pp. 70–83.
Bernardi, M. and Catania, L. (2014).“The Model Confidence Set package for R.” In: _arXiv e-Print_.
Berrisch, J. and Ziel, F. (2021).“CRPS Learning.” In: _arXiv e-Print_.
Bessembinder, H. (, Burt, A. P., and Hrdlicka, C. M. (2022).“Time Series Variation in the Factor Zoo.” In: _SSRN
e-Print_.
Bhatnagar, A., Kassianik, P., Liu, C., Lan, T., Yang, W., Cassius, R., Sahoo, D., Arpit, D., Subramanian, S., Woo,
G., Saha, A., Jagota, A. K., Gopalakrishnan, G., Singh, M., Krithika, K. C., Maddineni, S., Cho, D., Zong, B.,
Zhou, Y., Xiong, C., Savarese, S., Hoi, S., and Wang, H. (2021). “Merlion: A Machine Learning Library for Time
Series.” In: _arXiv e-Print_.
Bianchi, D., Buchner, M., and Tamoni, A. (2021).“Bond Risk Premiums with Machine Learning.” In: _The Review
of Financial Studies_ 34(2), pp. 1046–1089.
Bianchi, D. and McAlinn, K. (2021).“Divide and Conquer: Financial Ratios and Industry Returns Predictability.”
In: _SSRN e-Print_.


Bianchi, D. and Tamoni, A. (2020).“Sparse Predictive Regressions: Statistical Performance and Economic Signif-
icance.” In: _Machine Learning for Asset Management: New Developments and Financial Applications_. Ed. by
E. Jurczenko. Wiley, pp. 75–113.
Bielinski, A. and Broby, D. (2021).“Machine Learning Methods in Asset Pricing.” In: _SSRN e-Print_.
Billio, M., Casarin, R., Ravazzolo, F., and Dijk, H. K. van (2013).“Time-varying combinations of predictive densities
using nonlinear filtering.” In: _Journal of Econometrics_ 177(2), pp. 213–232.
Bisaglia, L. and Grigoletto, M. (2021).“A new time-varying model for forecasting long-memory series.” In: _Statistical
Methods & Applications_ 30, pp. 139–155.
Bjerregård, M. B., Møller, J. K., and Madsen, H. (2021).“An introduction to multivariate probabilistic forecast
evaluation.” In: _Energy and AI_ 4, p. 100058.
Blitz, D., Hanauer, M. X., Vidojevic, M., and Vliet, P. v. (2018).“Five Concerns with the Five-Factor Model.” In:
_The Journal of Portfolio Management_ 44(4), pp. 71–78.
Bloemheuvel, S., van den Hoogen, J., Jozinovic, D., Michelini, A., and Atzmueller, M. (2022). “Multivariate Time
Series Regression with Graph Neural Networks.” In: _arXiv e-Print_.
Boileau, P., Hejazi, N., Collica, B., Laan, M. van der, and Dudoit, S. (2021).“cvCovEst: Cross-validated covariance
matrix estimator selection and evaluation in R.” In: _Journal of Open Source Software_ 6(63), p. 3273.
Bokde, N. D., Yaseen, Z. M., and Andersen, G. B. (2020).“ForecastTB - An R Package as a Test-Bench for Time
Series Forecasting, with Application of Wind Speed and Solar Radiation Modeling.” In: _Energies_ 13(10), p. 2578.
Botchkarev, A. (2019).“A new typology design of performance metrics to measure errors in machine learning
regression algorithms.” In: _Interdisciplinary Journal of Information, Knowledge, and Management_ 14, pp. 045–
076.
Bouallegue, Z. B., Haiden, T., and Richardson, D. S. (2018).“The diagonal score: Definition, properties, and
interpretations.” In: _Quarterly Journal of the Royal Meteorological Society_ 144(714), pp. 1463–1473.
Brehmer, J., Gneiting, T., Schlather, M., and Strokorb, K. (2021). “Using scoring functions to evaluate point process
forecasts.” In: _arXiv e-Print_.
Brehmer, J. R. and Gneiting, T. (2020).“Properization: constructing proper scoring rules via Bayes acts.” In: _Annals
of the Institute of Statistical Mathematics_ 72(3), pp. 659–673.
Breitung, J. and Knuppel, M. (2021).“How far can we forecast? Statistical tests of the predictive content.” In:
_Journal of Applied Econometrics_ 36(4), pp. 369–392.
Brugiere, P. (2020). _Quantitative Portfolio Management with Applications in Python_. Springer International Pub-
lishing. 189 pp.
Bryzgalova, S., Huang, J., and Julliard, C. (2021a).“Bayesian solutions for the factor zoo: we just ran two quadrillion
models.” In: _SSRN e-Print_.
Bryzgalova, S., Pelger, M., and Zhu, J. (2021b).“Forest Through the Trees: Building Cross-Sections of Stock
Returns.” In: _SSRN e-Print_.
Bulut, L. (2019).“Does Statistical Significance Help to Evaluate Predictive Performance of Competing Models?”
In: _SSRN e-Print_.
Burns, D. M. and Whyne, C. M. (2018).“Seglearn: A Python Package for Learning Sequences and Time Series.”
In: _arXiv e-Print_.
Cai, Z., Fang, Y., and Xu, Q. (2022).“Testing capital asset pricing models using functional-coefficient panel data
models with cross-sectional dependence.” In: _Journal of Econometrics_ 227(1), pp. 114–133.
Cajas, D. (2021a).“Entropic Portfolio Optimization: a Disciplined Convex Programming Framework.” In: _SSRN
e-Print_.
Cajas, D. (2021b).“OWA Portfolio Optimization: a Disciplined Convex Programming Framework.” In: _SSRN e-
Print_.
Caldeira, J. F., Moura, G. V., and Santos, A. A. P. (2018).“Yield curve forecast combinations based on bond
portfolio performance.” In: _Journal of Forecasting_ 37(1), pp. 64–82.
Capolongo, A. and Pacella, C. (2021).“Forecasting inflation in the euro area: countries matter!” In: _Empirical
Economics_ 61, pp. 2477–2499.
Carr, P. P. and Wu, L. (2021). _Decomposing Long Bond Returns: A Decentralized Theory_. Tech. rep. NYU.
Castilho, D., Souza, T. T. P., Kang, S. M., Gama, J., and Carvalho, A. C. P. L. F. de (2021). “Forecasting Financial
Market Structure from Network Features using Machine Learning.” In: _arXiv e-Print_.
Castle, J. L., Doornik, J. A., and Hendry, D. F. (2021a).“Forecasting Principles from Experience with Forecasting
Competitions.” In: _Forecasting_ 3(1), pp. 138–165.


Castle, J. L., Doornik, J. A., and Hendry, D. F. (2021b).“Selecting a Model for Forecasting.” In: _Econometrics_ 9(3),
p. 26.
Cerqueira, V., Torgo, L., and Mozetič, I. (2020).“Evaluating time series forecasting models: an empirical study on
performance estimation methods.” In: _Machine Learning_ 109, pp. 1997–2028.
Cerqueira, V., Torgo, L., and Soares, C. (2021a).“Model Selection for Time Series Forecasting: Empirical Analysis
of Different Estimators.” In: _arXiv e-Print_.
Cerqueira, V., Torgo, L., Soares, C., and Bifet, A. (2021b).“Model Compression for Dynamic Forecast Combination.”
In: _arXiv e-Print_.
Cetin, B. and Yavuz, I. (2021).“Comparison of forecast accuracy of Ata and exponential smoothing.” In: _Journal
of Applied Statistics_ 48(13-15), pp. 2580–2590.
Chai, D., Chiah, M., and Gharghori, P. (2019).“Which model best explains the returns of large Australian stocks?”
In: _Pacific-Basin Finance Journal_ 55, pp. 182–191.
Challu, C., Olivares, K. G., Welter, G., and Dubrawski, A. (2021). “DMIDAS: Deep Mixed Data Sampling Regression
for Long Multi-Horizon Time Series Forecasting.” In: _arXiv e-Print_.
Chan, F. and Pauwels, L. L. (2018).“Some theoretical results on forecast combinations.” In: _International Journal
of Forecasting_ 34(1), pp. 64–74.
Charles, A., Darné, O., and Kim, J. H. (2022).“Stock return predictability: Evaluation based on interval forecasts.”
In: _Bulletin of Economic Research_ 74(2), pp. 363–385.
Charte, F., Vico, A., Perez-Godoy, M. D., and Rivera, A. J. (2019).“predtoolsTS: R package for streamlining time
series forecasting.” In: _Progress in Artificial Intelligence_ 8(4), pp. 505–510.
Chatigny, P., Wang, S., Patenaude, J.-M., and Oreshkin, B. N. (2021). “Neural forecasting at scale.” In: _arXiv
e-Print_.
Chatterjee, A., Bhowmick, H., and Sen, J. (2021). “Stock Price Prediction Using Time Series, Econometric, Machine
Learning, and Deep Learning Models.” In: _arXiv e-Print_.
Chen, A. Y. and Zimmermann, T. (2021).“Open Source Cross-Sectional Asset Pricing.” In: _SSRN e-Print_.
Chen, A. Y. and Zimmermann, T. (2022).“Open Source Cross-Sectional Asset Pricing.” In: _American Finance
Association Annual Meeting_.
Chen, H., Jiang, L., and Liu, W. (2020).“Predicting returns out of sample: A naive model averaging approach.” In:
_SSRN e-Print_.
Chen, L., Chen, D., Shang, Z., Zhang, Y., Wen, B., and Yang, C. (2022). “Multi-Scale Adaptive Graph Neural
Network for Multivariate Time Series Forecasting.” In: _arXiv e-Print_.
Chen, L., Chen, W., Wu, B., Zhang, Y., Wen, B., and Yang, C. (2021a). “Learning from Multiple Time Series: A
Deep Disentangled Approach to Diversified Time Series Forecasting.” In: _arXiv e-Print_.
Chen, L., Pelger, M., and Zhu, J. (2021b).“Deep learning in asset pricing.” In: _SSRN e-Print_.
Cheng, D., Yang, F., Xiang, S., and Liu, J. (2022).“Financial time series forecasting with multi-modality graph
neural network.” In: _Pattern Recognition_ 121, p. 108218.
Cheng, M., Swanson, N. R., and Yao, C. (2019).“Forecast Evaluation.” In: _SSRN e-Print_.
Chevallier, J., Guégan, D., and Goutte, S. (2021).“Is It Possible to Forecast the Price of Bitcoin?” In: _Forecasting_
3(2), pp. 377–420.
Chiah, M., Chai, D., Zhong, A., and Li, S. (2016).“A Better Model? An Empirical Investigation of the Fama-French
Five-factor Model in Australia.” In: _International Review of Finance_ 16(4), pp. 595–638.
Chiang, I.-H. E., Liao, Y., and Zhou, Q. (2021).“Modeling the cross-section of stock returns using sensible models
in a model pool.” In: _Journal of Empirical Finance_ 60, pp. 56–73.
Chib, S. (2020). _R package czfactor_. Tech. rep. Washington University.
Chib, S. and Zeng, X. (2020).“Which factors are risk factors in asset pricing? A model scan framework.” In: _Journal
of Business & Economic Statistics_ 38(4), pp. 771–783.
Chib, S., Zeng, X., and Zhao, L. (2020).“On Comparing Asset Pricing Models.” In: _Journal of Finance_ 75(11),
pp. 551–577.
Chib, S. and Zhao, L. (2020). _R package czzg_. Tech. rep. Washington University.
Chib, S., Zhao, L., Huang, D., and Zhou, G. (2022).“Winners from Winners: A Tale of Risk Factors.” In: _SSRN
e-Print_.
Chiu, C.-W., Hayes, S., Kapetanios, G., and Theodoridis, K. (2019).“A new approach for detecting shifts in forecast
accuracy.” In: _International Journal of Forecasting_ 35(4), pp. 1596–1612.
Choe, Y. J. and Ramdas, A. (2022). “Comparing Sequential Forecasters.” In: _arXiv e-Print_.


Cholakov, R. and Kolev, T. (2021). “Transformers predicting the future. Applying attention in next-frame and time
series forecasting.” In: _arXiv e-Print_.
Chordia, T., Goyal, A., and Saretto, A. (2020).“Anomalies and false rejections.” In: _The Review of Financial Studies_
33(5), pp. 2134–2179.
Chu, P. K. (2021).“Forecasting Recessions with Financial Variables and Temporal Dependence.” In: _Economies_
9(3), p. 118.
Chudik, A., Pesaran, M. H., and Sharifvaghefi, M. (2021).“Variable Selection and Forecasting in High Dimensional
Linear Regressions with Structural Breaks.” In: _SSRN e-Print_ 2020(394).
Cohen, N., Sood, S., Zeng, Z., Balch, T., and Veloso, M. (2020). “Visual Forecasting of Time Series with Image-to-
Image Regression.” In: _arXiv e-Print_.
Cohen, N., Sood, S., Zeng, Z., Balch, T., and Veloso, M. (2021).“Visual Time Series Forecasting: An Image-driven
Approach.” In: _MiLeTS’21: 7th KDD Workshop on Mining and Learning from Time Series_.
Collot, S. and Hemauer, T. (2021).“A literature review of new methods in empirical asset pricing: omitted-variable
and errors-in-variable bias.” In: _Financial Markets and Portfolio Management_ 35, pp. 77–100.
Cong, L. W., Tang, K., Wang, J., and Zhang, Y. (2021).“Deep Sequence Modeling: Development and Applications
in Asset Pricing.” In: _The Journal of Financial Data Science_ 3(1), pp. 28–42.
Coqueret, G. (2022). _Perspectives in sustainable equity investing (website version)_.
Coqueret, G. and Guida, T. (2020). _Machine Learning for Factor Investing: R Version_. Chapman and Hall/CRC.
341 pp.
Cornell, B. (2020).“Stock characteristics and stock returns: a skeptic’s look at the cross section of expected returns.”
In: _The Journal of Portfolio Management_ 46(5), pp. 131–142.
Coroneo, L., Iacone, F., Paccagnini, A., and Monteiro, P. S. (2021).“Testing the Predictive Accuracy of COVID-19
Forecasts.” In: _SSRN e-Print_.
Costantini, M. and Kunst, R. M. (2021).“On using predictive-ability tests in the selection of time-series prediction
models: A Monte Carlo evaluation.” In: _International Journal of Forecasting_ 37(2), pp. 445–460.
Czasonis, M., Kritzman, M., and Turkington, D. (2020).“Addition by Subtraction: A Better Way to Forecast Factor
Returns (and Everything Else).” In: _The Journal of Portfolio Management_ 46(8), pp. 98–107.
Czasonis, M., Kritzman, M., and Turkington, D. (2021a).“Relevance.” In: _SSRN e-Print_.
Czasonis, M., Kritzman, M., and Turkington, D. (2021b).“The Past as Prologue: How to Forecast Presidential
Elections.” In: _SSRN e-Print_.
Dai, Z., Kang, J., and Wen, F. (2021).“Predicting stock returns: A risk measurement perspective.” In: _International
Review of Financial Analysis_ 74, p. 101676.
Dai, Z., Li, T., and Yang, M. (2022).“Forecasting stock return volatility: The role of shrinkage approaches in a
data-rich environment.” In: _Journal of Forecasting_.
Dama, F. and Sinoquet, C. (2021).“Analysis and modeling to forecast in time series: a systematic review.” In: _arXiv
e-Print_.
Davydenko, A. and Goodwin, P. (2021).“Assessing Point Forecast Bias Across Multiple Time Series: Measures and
Visual Tools.” In: _International Journal of Statistics and Probability_ 10(5), p. 46.
De Baets, S. and Harvey, N. (2020).“Using judgment to select and adjust forecasts from statistical models.” In:
_European Journal of Operational Research_ 284(3), pp. 882–895.
de Carvalho, M. and Rua, A. (2017).“Real-time nowcasting the US output gap: Singular spectrum analysis at
work .” In: _International Journal of Forecasting_ 33(1), pp. 185–198.
de Valk, S., Mattos, D. de, and Ferreira, P. (2019).“Nowcasting: An R Package for Predicting Economic Variables
Using Dynamic Factor Models.” In: _The R Journal_.
Debnath, A., Waghmare, G., Wadhwa, H., Asthana, S., and Arora, A. (2021).“Exploring Generative Data Aug-
mentation in Multivariate Time Series Forecasting : Opportunities and Challenges.” In: _MiLeTS’21: 7th KDD
Workshop on Mining and Learning from Time Series_.
Dendramis, Y., Kapetanios, G., and Marcellino, M. (2020).“A similarity-based approach for macroeconomic fore-
casting.” In: _Journal of the Royal Statistical Society Series A_ 183(3), pp. 801–827.
Deshpande, P., Marathe, K., De, A., and Sarawagi, S. (2021).“Long Horizon Forecasting With Temporal Point
Processes.” In: _arXiv e-Print_.
Deshpande, P. and Sarawagi, S. (2021). “Long Range Probabilistic Forecasting in Time-Series using High Order
Statistics.” In: _arXiv e-Print_.


Di Fonzo, T. and Girolimetto, D. (2020).“Cross-temporal forecast reconciliation: Optimal combination method and
heuristic alternatives.” In: _arXiv e-Print_.
Di Fonzo, T. and Girolimetto, D. (2021). “Forecast combination based forecast reconciliation: insights and exten-
sions.” In: _arXiv e-Print_.
Di Fonzo, T. and Girolimetto, D. (2022).“Cross-temporal forecast reconciliation: Optimal combination method and
heuristic alternatives.” In: _International Journal of Forecasting_.
Diebold, F. X. (2015).“Comparing Predictive Accuracy, Twenty Years Later: A Personal Perspective on the Use
and Abuse of Diebold-Mariano Tests.” In: _Journal of Business and Economic Statistics_ 33(1), p. 1.
Ding, L., Ahmed, S., and Shapiro, A. (2020).“A Python package for multi-stage stochastic programming.” In:
_Optimization Online e-Print_.
Dixon, M. and Polson, N. (2020).“Deep Fundamental Factor Models.” In: _SIAM Journal on Financial Mathematics_
11(3), SC–26–SC–37.
Dixon, M. F., Halperin, I., and Bilokon, P. (2020). _Machine Learning in Finance: from theory to practice_. Springer
International Publishing. 548 pp.
Dong, H., Guo, X., Reichgelt, H., and Hu, R. (2020).“Predictive power of ARIMA models in forecasting equity
returns: a sliding window method.” In: _Journal of Asset Management_ (21), pp. 549–566.
Dong, X., Li, Y., Rapach, D., and Zhou, G. (2022).“Anomalies and the expected market return.” In: _Journal of
Finance_ 27(1), pp. 639–681.
Drobetz, W. and Otto, T. (2020).“Empirical Asset Pricing via Machine Learning: Evidence from the European
Stock Market.” In: _SSRN e-Print_.
Du, Y., Wang, J., Feng, W., Pan, S., Qin, T., Xu, R., and Wang, C. (2021). “AdaRNN: Adaptive Learning and
Forecasting of Time Series.” In: _arXiv e-Print_.
Elkamhi, R., Lee, J. S. H., and Salerno, M. (2021).“Factor Investing Using Capital Market Assumptions.” In: _The
Journal of Portfolio Management_.
Ellingsen, J., Larsen, V. H., and Thorsrud, L. A. (2022).“News media vs. FRED-MD for macroeconomic forecasting.”
In: _Journal of Applied Econometrics_.
Fabozzi, F. J., Fabozzi, F. A., Lopez de Prado, M., and Stoyanov, S. (2021). _Asset Management: Tools and Issues_.
World Scientific. 516 pp.
Faloutsos, C., Flunkert, V., Gasthaus, J., Januschowski, T., and Wang, Y. (2019).“Forecasting Big Time Series:
Theory and Practice.” In: _Tutorial for the 25TH ACM SIGKDD Conference on Knowledge Discovery and Data
Mining_. ACM.
Fama, E. F. and French, K. R. (2018).“Choosing factors.” In: _Journal of Financial Economics_ 128(2), pp. 234–252.
Fama, E. F. and French, K. R. (2020).“Comparing Cross-Section and Time-Series Factor Models.” In: _The Review
of Financial Studies_ 33(5), pp. 1891–1926.
Fameliti, S. P. and Skintzi, V. D. (2020).“Predictive ability and economic gains from volatility forecast combina-
tions.” In: _Journal of Forecasting_ 39(2), pp. 200–219.
Fan, J., Ke, Y., Sun, Q., and Zhou, W.-X. (2019).“FarmTest: Factor-adjusted robust multiple testing with approx-
imate false discovery control.” In: _Journal of the American Statistical Association_ 114(528), pp. 1880–1893.
Fang, Y., Guan, B., Wu, S., and Heravi, S. (2020).“Optimal forecast combination based on ensemble empirical
mode decomposition for agricultural commodity futures prices.” In: _Journal of Forecasting_ 39(6), pp. 877–886.
Faria, G. and Verona, F. (2021).“Time-frequency forecast of the equity premium.” In: _Quantitative Finance_.
Fauvel, K., Masson, V., and Fromont, elisa (2021). “A Performance-Explainability Framework to Benchmark Ma-
chine Learning Methods: Application to Multivariate Time Series Classifiers.” In: _arXiv e-Print_.
Feldkircher, M., Huber, F., and Pfarrhofer, M. (2020).“Factor Augmented Vector Autoregressions, Panel VARs,
and Global VARs.” In: _Macroeconomic Forecasting in the Era of Big Data_. Springer International Publishing,
pp. 65–93.
Feng, G., Giglio, S., and Xiu, D. (2020).“Taming the factor zoo: A test of new factors.” In: _The Journal of Finance_
75(3), pp. 1327–1370.
Filipovic, D. and Khalilzadeh, A. (2021).“Machine Learning for Predicting Stock Return Volatility.” In: _SSRN
e-Print_.
Fjellstrom, C. (2022). “Long Short-Term Memory Neural Network for Financial Time Series.” In: _arXiv e-Print_.
Fleiss, A. and Cui, H. (2021).“Forecasting Stock Price Changes Using Natural Language Processing.” In: _SSRN
e-Print_.
Fosten, J. and Gutknecht, D. (2021).“Horizon confidence sets.” In: _Empirical Economics_.


Frenkel, M., Jung, J.-K., and Rulke, J.-C. (2021).“Testing for the rationality of central bank interest rate forecasts.”
In: _Empirical Economics_.
Freyberger, J., Neuhierl, A., and Weber, M. (2020).“Dissecting Characteristics Nonparametrically.” In: _The Review
of Financial Studies_ 33(5), pp. 2326–2377.
Fulton, C. and Hubrich, K. (2021).“Forecasting US Inflation in Real Time.” In: _SSRN e-Print_ (014).
Gafka, B., Savor, P. G., and Wilson, M. I. (2021).“Sources of Return Predictability.” In: _SSRN e-Print_.
Gasthaus, J., Benidis, K., Wang, Y., Rangapuram, S. S., Salinas, D., Flunkert, V., and Januschowski, T. (2019).
“Probabilistic Forecasting with Spline Quantile Function RNNs.” In: _Proceedings of Machine Learning Research_
89, pp. 1901–1910.
Gastinger, J., Nicolas, S., Stepic, D., Schmidt, M., and Schulke, A. (2021).“A study on Ensemble Learning for
Time Series Forecasting and the need for Meta-Learning.” In: _arXiv e-Print_.
Geertsema, P. G. and Lu, H. (2021).“Long-horizon predictability and information decay in equity markets.” In:
_SSRN e-Print_.
Geweke, J. and Amisano, G. (2010).“Comparing and evaluating Bayesian predictive distributions of asset returns.”
In: _International Journal of Forecasting_ 26(2), pp. 216–230.
Ghorbani, M. and Chong, E. K. P. (2021).“A dimension reduction method for stock-price prediction using multiple
predictors.” In: _Operational Research_.
Gilleland, E., Hering, A. S., Fowler, T. L., and Brown, B. G. (2018).“Testing the Tests: What Are the Impacts
of Incorrect Assumptions When Applying Confidence Intervals or Hypothesis Tests to Compare Competing
Forecasts?” In: _Monthly Weather Review_ 146(6), pp. 1685–1703.
Gilliland, M. (2020).“The value added by machine learning approaches in forecasting.” In: _International Journal
of Forecasting_ 36(1), pp. 161–166.
Giovannelli, A., Massacci, D., and Soccorsi, S. (2021a).“Forecasting Stock Returns with Large Dimensional Factor
Models.” In: _SSRN e-Print_.
Giovannelli, A., Massacci, D., and Soccorsi, S. (2021b).“Forecasting stock returns with large dimensional factor
models.” In: _Journal of Empirical Finance_ 63, pp. 252–269.
Gneiting, T. and Resin, J. (2022). “Regression Diagnostics meets Forecast Evaluation: Conditional Calibration,
Reliability Diagrams, and Coefficient of Determination.” In: _arXiv e-Print_.
Godahewa, R., Bandara, K., Webb, G. I., Smyl, S., and Bergmeir, C. (2021a).“Ensembles of localised models for
time series forecasting.” In: _Knowledge-Based Systems_ 233, p. 107518.
Godahewa, R., Bergmeir, C., Webb, G. I., Hyndman, R. J., and Montero-Manso, P. (2021b).“Monash Time Series
Forecasting Archive.” In: _arXiv E-Print_.
Goliński, A. and Spencer, P. (2021).“Estimating the Term Structure with Linear Regressions: Getting to the Roots
of the Problem.” In: _Journal of Financial Econometrics_ 19(5), pp. 960–984.
Golyandina, N., Korobeynikov, A., and Zhigljavsky, A. (2018). _Singular Spectrum Analysis with R_. Springer Berlin
Heidelberg. 272 pp.
Gonzalez-Rivera, G., Luo, Y., and Ruiz, E. (2020).“Prediction regions for interval-valued time series.” In: _Journal
of Applied Econometrics_ 35(4), pp. 373–390.
Gospodinov, N. and Maasoumi, E. (2021).“Generalized aggregation of misspecified models: with an application to
asset pricing.” In: _Journal of Econometrics_ 222(1), pp. 451–467.
Gospodinov, N. and Robotti, C. (2021).“Common pricing across asset classes: Empirical evidence revisited.” In:
_Journal of Financial Economics_ 132(2), pp. 292–324.
Goyal, A. and Jegadeesh, N. (2018).“Cross-Sectional and Time-Series Tests of Return Predictability: What Is the
Difference?” In: _The Review of Financial Studies_ 31(5), pp. 1784–1824.
Gramespacher, T. and Banziger, A. (2019).“The Bias in Two-Pass Regression Tests of Asset-Pricing Models in Pres-
ence of Idiosyncratic Errors with Cross-Sectional Dependence.” In: _Review of Pacific Basin Financial Markets
and Policies_ 22(02), p. 1950012.
Graziani, C., Rosner, R., Adams, J. M., and Machete, R. L. (2021).“Probabilistic recalibration of forecasts.” In:
_International Journal of Forecasting_ 37(1), pp. 1–27.
Grazzi, R., Flunkert, V., Salinas, D., Januschowski, T., Seeger, M., and Archambeau, C. (2021). “Meta-Forecasting
by combining Global Deep Representations with Local Adaptation.” In: _arXiv e-Print_.
Grealish, A. and Kolm, P. N. (2021).“Robo-Advisory: From Investing Principles and Algorithms to Future Devel-
opments.” In: _SSRN e-Print_.
Greenberg, S. (2020).“Calibration Scoring Rules for Practical Prediction Training.” In: _arXiv e-Print_.


Gu, S., Kelly, B., and Xiu, D. (2021).“Autoencoder asset pricing models.” In: _Journal of Econometrics_ 222(1),
pp. 429–450.
Gu, S., Kelly, B. T., and Xiu, D. (2020).“Empirical asset pricing via machine learning.” In: _The Review of Financial
Studies_ 33 (5), pp. 2223–2273.
Guijarro-Ordonez, J., Pelger, M., and Zanotti, G. (2021).“Deep Learning Statistical Arbitrage.” In: _SSRN e-Print_.
Gurdogan, H. and Kercheval, A. (2021). “Multi Anchor Point Shrinkage for the Sample Covariance Matrix (Extended
Version).” In: _arXiv e-Print_.
Haase, F. and Neuenkirch, M. (2021).“Forecasting Stock Market Recessions in the US: Predictive Modeling using
Different Identification Approaches.” In: _SSRN e-Print_.
Habibnia, A. (2016).“Essays in high-dimensional nonlinear time series analysis.” PhD thesis. London School of
Economics and Political Science.
Hammerschmid, R. and Lohre, H. (2018).“Regime Shifts and Stock Return Predictability.” In: _International Review
of Economics and Finance_ 56, pp. 138–160.
Hannadige, S. B., Gao, J., Silvapulle, M. J., and Silvapulle, P. (2021).“Forecasting a Nonstationary Time Series
Using a Mixture of Stationary and Nonstationary Predictors.” In: _SSRN e-Print_.
Harris, D., Martin, G. M., Perera, I., and Poskitt, D. S. (2019).“Construction and visualization of confidence sets
for frequentist distributional forecasts.” In: _Journal of Computational and Graphical Statistics_ 28(2), pp. 92–104.
Harvey, C. R. and Liu, Y. (2020).“Detecting Repeatable Performance.” In: _SSRN e-Print_.
Harvey, C. R., Liu, Y., and Saretto, A. (2020).“An Evaluation of Alternative Multiple Testing Methods for Finance
Applications.” In: _The Review of Asset Pricing Studies_ 10(2), pp. 199–248.
Harvey, D. I., Leybourne, S. J., Sollis, R., and Taylor, A. M. R. (2021).“Real-Time Detection of Regimes of
Predictability in the U.S. Equity Premium.” In: _Journal of Applied Econometrics_ 36, pp. 45–70.
Hassler, U. and Pohle, M.-O. (2021).“Forecasting under Long Memory.” In: _Journal of Financial Econometrics_.
Hauzenberger, N., Huber, F., and Klieber, K. (2021). “Real-time Inflation Forecasting Using Non-linear Dimension
Reduction Techniques.” In: _arXiv e-Print_.
He, S. and Gu, S. (2022). “Multi-modal Attention Network for Stock Movements Prediction.” In: _arXiv e-Print_.
Herzen, J., Lassig, F., Piazzetta, S. G., Neuer, T., Tafti, L., Raille, G., Pottelbergh, T. V., Pasieka, M., Skrodzki,
A., Huguenin, N., Dumonal, M., Koscisz, J., Bader, D., Gusset, F., Benheddi, M., Williamson, C., Kosinski,
M., Petrik, M., and Grosch, G. (2022). “Darts: User-Friendly Modern Machine Learning for Time Series.” In:
_Journal of Machine Learning Research_ 23(124), pp. 1–6.
Hewamalage, H., Bergmeir, C., and Bandara, K. (2020).“Global Models for Time Series Forecasting: A Simulation
Study.” In: _arXiv e-Print_.
Hewamalage, H., Bergmeir, C., and Bandara, K. (2021).“Recurrent Neural Networks for Time Series Forecasting:
Current status and future directions.” In: _International Journal of Forecasting_ 37(1), pp. 388–427.
Ho, J., Tumkaya, T., Aryal, S., Choi, H., and Claridge-Chang, A. (2019).“Moving beyond P values: data analysis
with estimation graphics.” In: _Nature Methods_ 16(7), pp. 565–566.
Ho, T.-W. and Lin, Y.-c. (2021).“Training by Rolling: Machine Learning and Stock Returns Forecasting.” In: _SSRN
e-Print_.
Hofmarcher, P. and Grun, B. (2020).“Bayesian Model Averaging.” In: _Macroeconomic Forecasting in the Era of Big
Data_. Springer International Publishing, pp. 359–388.
Hoga, Y. and Dimitriadis, T. (2021).“On Testing Equal Conditional Predictive Ability Under Measurement Error.”
In: _arXiv e-Print_.
Hollyman, R., Petropoulos, F., and Tipping, M. E. (2021).“Understanding forecast reconciliation.” In: _European
Journal of Operational Research_ 294(1), pp. 149–160.
Holzmann, H. and Klar, B. (2021). “Using Proxies to Improve Forecast Evaluation.” In: _arXiv e-Print_.
Homescu, C. (2014).“Many risks, one (optimal) portfolio.” In: _SSRN e-Print_.
Homescu, C. (2015).“Better Investing Through Factors, Regimes and Sensitivity Analysis.” In: _SSRN e-Print_.
Hounyo, U. and Lahiri, K. (2022).“Estimating the variance of a combined forecast: Bootstrap-based approach.” In:
_Journal of Econometrics_.
Hsiao, C. and Wan, S. K. (2014).“Is there an optimal forecast combination?” In: _Journal of Econometrics_ 178,
pp. 294–309.
Hull, B. and Qiao, X. (2017).“A Practitioner’s Defense of Return Predictability.” In: _The Journal of Portfolio
Management_ 43(3), pp. 60–76.


Hunt, I. (2022).“In-sample tests of predictability are superior to pseudo-out-of-sample tests, even when data mining.”
In: _International Journal of Forecasting_.
Hyndman, R. J. (2020).“Tidy Time Series and Forecasting in R.” In: _RStudio conf2020_.
Hyndman, R. J. and Athanasopoulos, G. (2020). _Forecasting: Principles and Practice (Third Edition)_. OTexts.
380 pp.
Ilic, I., Gorgulu, B., and Cevik, M. (2020).“Augmented Out-of-Sample Comparison Method for Time Series Fore-
casting Techniques.” In: _Advances in Artificial Intelligence_. Springer International Publishing, pp. 302–308.
Ilmanen, A., Chandra, S., and McQuinn, N. (2020).“Demystifying illiquid assets: expected returns for private
equity .” In: _The Journal of Alternative Investments_ 22(3), pp. 8–22.
Inoue, A., Jin, L., and Rossi, B. (2017).“Rolling window selection for out-of-sample forecasting with time-varying
parameters.” In: _Journal of Econometrics_ 196(1), pp. 55–67.
Irlam, G. (2020a). _AI Planner_ .url:https://www.aiplanner.com/.
Irlam, G. (2020b).“Machine learning for retirement planning.” In: _The Journal of Retirement_ 8(1), pp. 32–29.
Irlam, G. (2020c).“Multi Scenario Financial Planning via Deep Reinforcement Learning AI.” In: _SSRN e-Print_.
Iworiso, J. and Vrontos, S. (2021).“On the Predictability of the Equity Premium Using Deep Learning Techniques.”
In: _The Journal of Financial Data Science_ 3(1), pp. 74–92.
Jaganathan, S. and Prakash, P. K. S. (2020).“A combination-based forecasting method for the M4-competition.”
In: _International Journal of Forecasting_ 36(1), pp. 98–104.
Jansen, S. (2020). _Machine Learning for Algorithmic Trading (Second Edition)_. Packt Publishing. 820 pp.
Janssen, R. V. (2019).“Multi-horizon comparison of multivariate inflation forecasting.” MA thesis. Erasmus School
of Economics.
Januschowski, T., Wang, Y., Torkkola, K., Erkkila, T., Hasson, H., and Gasthaus, J. (2022).“Forecasting with
trees.” In: _International Journal of Forecasting_.
Jegadeesh, N., Noh, J., Pukthuanthong, K., Roll, R., and Wang, J. (2019).“Empirical tests of asset pricing models
with individual assets: Resolving the errors-in-variables bias in risk premium estimation.” In: _Journal of Financial
Economics_ 113(2), pp. 273–298.
Jin, S., Corradi, V., and Swanson, N. R. (2017).“Robust Forecast Comparison.” In: _Econometric Theory_ 33(06),
pp. 1306–1351.
Jordan, A., Kruger, F., and Lerch, S. (2019).“Evaluating probabilistic forecasts with scoringRules.” In: _Journal of
Statistical Software_ 90(12).
Joshi, S. (2019).“Time Series Analysis and Forecasting of the US Housing Starts using Econometric and Machine
Learning Model.” In: _arXiv e-Print_.
Jurczenko et al. (2020). _Machine Learning for Asset Management_. Ed. by E. Jurczenko. Wiley. 445 pp.
Kakushadze, Z. and Yu, W. (2016).“Statistical Risk Models.” In: _SSRN e-Print_.
Kakushadze, Z. and Yu, W. (2017).“Open Source Fundamental Industry Classification.” In: _MDPI Data_ 22 (2).
Kakushadze, Z. and Yu, W. (2018a).“Betas, Benchmarks, and Beating the Market.” In: _The Journal of Trading_.
Kakushadze, Z. and Yu, W. (2018b).“Decoding stock market with quant alphas.” In: _Journal of Asset Management_ ,
pp. 1–11.
Kakushadze, Z. and Yu, W. (2019).“Machine learning risk models.” In: _SSRN e-Print_.
Kakushadze, Z. and Yu, W. (2020).“Machine learning treasury yields.” In: _SSRN e-Print_.
Kalfa, S. Y. and Marquez, J. (2021).“Forecasting FOMC Forecasts.” In: _Econometrics_ 9(3), p. 34.
Kamarthi, H., Kong, L., Rodriguez, A., Zhang, C., and Prakash, B. A. (2021). “CAMul: Calibrated and Accurate
Multi-view Time-Series Forecasting.” In: _arXiv e-Print_.
Kang, T.-H., Sharma, A., and Marshall, L. (2021a).“Assessing Goodness of Fit for Verifying Probabilistic Forecasts.”
In: _Forecasting_ 3(4), pp. 763–773.
Kang, Y., Spiliotis, E., Petropoulos, F., Athiniotis, N., Li, F., and Assimakopoulos, V. (2021b).“Déjà vu: A data-
centric forecasting approach through time series cross-similarity.” In: _Journal of Business Research_.
Karathanasopoulos, A., Mitra, S., Skindilias, K., and Lo, C. C. (2017).“Modelling and Trading the English and
German Stock Markets with Novelty Optimization Techniques.” In: _Journal of Forecasting_ 36(8) (8), pp. 974–
988.
Karolyi, A. and Van Nieuwerburgh, S. (2020).“New Methods for the Cross-Section of Returns.” In: _The Review of
Financial Studies_ 33(5), pp. 1879–1890.
Kelly, B. T., Pruitt, S., and Su, Y. (2019).“Characteristics are covariances: A unified model of risk and return.” In:
_Journal of Financial Economics_ 134(3), pp. 501–524.


Kiefer, D., Bauer, M., and Grimm, F. (2021).“Univariate Time Series Forecasting: Machine Learning Prediction of
the Best Suitable Forecast Model Based on Time Series Characteristics.” In: _Human Centred Intelligent Systems_.
Springer Singapore, pp. 152–162.
Klingberg Malmer, O. and Pettersson, G. (2020).“Tidying up the factor zoo: Using machine learning to find sparse
factor models that predict asset returns.” MA thesis. University of Goteborg.
Kosman, E. and Castro, D. D. (2021). “Vision-Guided Forecasting – Visual Context for Multi-Horizon Time Series
Forecasting.” In: _arXiv e-Print_.
Koutsandreas, D., Spiliotis, E., Petropoulos, F., and Assimakopoulos, V. (2021).“On the selection of forecasting
accuracy measures.” In: _Journal of the Operational Research Society_.
Kozak, S., Nagel, S., and Santosh, S. (2020).“Shrinking the cross-section.” In: _Journal of Financial Economics_ 135
(2), pp. 271–292.
Kritzman, M., Kinlaw, W., and Turkington, D. (2017). _A Practitioner’s Guide to Asset Allocation_. Wiley. 256 pp.
Kruse, R., Leschinski, C., and Will, M. (2019).“Comparing Predictive Accuracy under Long Memory, With an
Application to Volatility Forecasting.” In: _Journal of Financial Econometrics_ 17(2), pp. 180–228.
Kuznetsov, V. and Mohri, M. (2016).“Time series prediction and online learning.” In: _29th Annual Conference on
Learning Theory_. Ed. by V. Feldman, A. Rakhlin, and O. Shamir. Vol. 49. Proceedings of Machine Learning
Research. Columbia University, New York, New York, USA: PMLR, pp. 1190–1213.
Kynigakis, I. and Panopoulou, E. (2021).“Does Model Complexity add Value to Asset Allocation? Evidence from
Machine Learning Forecasting Models.” In: _Journal of Applied Econometrics_.
Kyriakou, I., Mousavi, P., Nielsen, J. P., and Scholz, M. (2020).“Longer-Term Forecasting of Excess Stock Returns

- The Five-Year Case.” In: _Mathematics_ 8(6), p. 927.
Lai, K.-H., Zha, D., Wang, G., Xu, J., Zhao, Y., Kumar, D., Chen, Y., Zumkhawaka, P., Wan, M., Martinez, D.,
and Hu, X. (2021). “TODS: An Automated Time Series Outlier Detection System.” In: _arXiv e-Print_.
Lara-Benitez, P., Carranza-Garcia, M., and Riquelme, J. C. (2021).“An Experimental Review on Deep Learning
Architectures for Time Series Forecasting.” In: _arXiv e-Print_.
Lara-Benı́tez, P., Gallego-Ledesma, L., Carranza-Garcı́a, M., and Luna-Romera, J. M. (2021).“Evaluation of the
Transformer Architecture for Univariate Time Series Forecasting.” In: _Conference of the Spanish Association
for Artificial IntelligenceCAEPIA 2021: Advances in Artificial Intelligence_. Springer International Publishing,
pp. 106–115.
Le Guen, V. and Thome, N. (2020).“Probabilistic Time Series Forecasting with Structured Shape and Temporal
Diversity.” In: _arXiv e-Print_.
Le Guen, V. and Thome, N. (2021).“Deep Time Series Forecasting with Shape and Temporal Criteria.” In: _arXiv
e-Print_.
Ledoit, O., Wolf, M., and Zhao, Z. (2019).“Efficient Sorting: A More Powerful Test for Cross-Sectional Anomalies.”
In: _Journal of Financial Econometrics_ 17(4), pp. 645–686.
Lee, T.-H. and Seregina, E. (2022). “Optimal Portfolio Using Factor Graphical Lasso.” In: _arXiv e-Print_.
Lerch, S., Thorarinsdottir, T. L., Ravazzolo, F., and Gneiting, T. (2015).“Forecaster’s Dilemma: Extreme Events
and Forecast Evaluation.” In: _arXiv e-Print_.
Lerch, S., Thorarinsdottir, T. L., Ravazzolo, F., and Gneiting, T. (2017).“Forecaster’s Dilemma: Extreme Events
and Forecast Evaluation.” In: _Statistical Science_ 32(1), pp. 106–127.
Leroy, A., Latouche, P., Guedj, B., and Gey, S. (2020). “MAGMA: Inference and Prediction with Multi-Task
Gaussian Processes.” In: _arXiv e-Print_.
Lettau, M. and Pelger, M. (2020).“Factors That Fit the Time Series and Cross-Section of Stock Returns.” In: _The
Review of Financial Studies_ 33(5), pp. 2274–2325.
Leung, E., Lohre, H., Mischlich, D., Shea, Y., and Stroh, M. (2020).“The Promises and Pitfalls of Machine Learning
for Predicting Cross-Sectional Stock Returns.” In: _SSRN e-Print_.
Leung, E., Lohre, H., Mischlich, D., Shea, Y., and Stroh, M. (2021).“The Promises and Pitfalls of Machine Learning
for Predicting Stock Returns.” In: _The Journal of Financial Data Science_ 3(2), pp. 21–50.
Li, A. W. and Bastos, G. S. (2020).“Stock Market Forecasting Using Deep Learning and Technical Analysis: A
Systematic Review.” In: _IEEE Access_ 8, pp. 185232–185242.
Li, L., Kang, Y., and Li, F. (2021a). “Bayesian forecast combination using time-varying features.” In: _arXiv e-Print_.
Li, Z., Liu, X.-Y., Zheng, J., Wang, Z., Walid, A., and Guo, J. (2021b).“FinRL-Podracer: High Performance and
Scalable Deep Reinforcement Learning for Quantitative Finance.” In: _ACM International Conference on AI in
Finance_.


Lichtendahl, K. C. and Winkler, R. L. (2020).“Why do some combinations perform better than others?” In:
_International Journal of Forecasting_ 36(1), pp. 142–149.
Lim, B. and Zohren, S. (2021).“Time-series forecasting with deep learning: a survey.” In: _Philosophical Transactions
of the Royal Society A: Mathematical, Physical and Engineering Sciences_ 379(2194), p. 20200209.
Liu, M., Zeng, A., Xu, Z., Lai, Q., and Xu, Q. (2021a). “Time Series is a Special Sequence: Forecasting with Sample
Convolution and Interaction.” In: _arXiv e-Print_.
Liu, X.-Y., Rui, J., Gao, J., Yang, L., Yang, H., Wang, Z., Wang, C. D., and Guo, J. (2022). “FinRL-Meta: A
Universe of Near-Real Market Environments for Data-Driven Deep Reinforcement Learning in Quantitative
Finance.” In: _arXiv e-Print_.
Liu, X.-Y., Yang, H., Gao, J., and Wang, C. (2021b).“FinRL: Deep Reinforcement Learning Framework to Automate
Trading in Quantitative Finance.” In: _SSRN e-Print_.
Liu, Z., Zhu, Z., Gao, J., and Xu, C. (2021c).“Forecast Methods for Time Series Data: A Survey.” In: _IEEE Access_
9, pp. 91896–91912.
Loning, M., Bagnall, A., Ganesh, S., Kazakov, V., Lines, J., and Kiraly, F. J. (2019).“sktime: A Unified Interface
for Machine Learning with Time Series.” In: _arXiv e-Print_.
Loning, M. and Kiraly, F. (2020).“Forecasting with sktime: Designing sktime’s New Forecasting API and Applying
It to Replicate and Extend the M4 Study.” In: _arXiv e-Print_.
Lopez de Prado, M. (2020). _Machine learning for asset managers_. Cambridge University Press. 190 pp.
Makridakis, S., Hyndman, R. J., and Petropoulos, F. (2020).“Forecasting in social settings: The state of the art.”
In: _International Journal of Forecasting_ 36 (1), pp. 15–28.
Makridakis, S. and Petropoulos, F. (2020).“The M4 competition: Conclusions.” In: _International Journal of Fore-
casting_ 36(1), pp. 224–227.
Makridakis, S., Spiliotis, E., and Assimakopoulos, V. (2019).“The M4 Competition: 100,000 time series and 61
forecasting methods.” In: _International Journal of Forecasting_ 36 (1), pp. 54–74.
Mancuso, P., Piccialli, V., and Sudoso, A. M. (2021).“A machine learning approach for forecasting hierarchical
time series.” In: _Expert Systems with Applications_ 182, p. 115102.
Marinescu, M. (2022).“Risk-Based Optimal Portfolio Strategies: A Compendium.” In: _SSRN e-Print_.
Martin, G. M., Loaiza-Maya, R., Frazier, D. T., Maneesoonthorn, W., and Hassan, A. R. (2020).“Optimal proba-
bilistic forecasts: When do they work?” In: _arXiv e-Print_.
Martin, G. M., Loaiza-Maya, R., Maneesoonthorn, W., Frazier, D. T., and Ramı́rez-Hassan, A. (2022).“Optimal
probabilistic forecasts: When do they work?” In: _International Journal of Forecasting_.
Martin, R. (2021).“PyPortfolioOpt: portfolio optimization in Python.” In: _Journal of Open Source Software_ 6(61),
p. 3066.
Martinez, A. B., Castle, J. L., and Hendry, D. F. (2020). _Smooth Robust Multi-Horizon Forecasts_. Tech. rep. George
Washington University.
Marwood, D. and Minnen, D. (2020).“Safely Boosting Retirement Income by Harmonizing Drawdown Paths.” In:
_Journal of Financial Planning_ 33(11), pp. 46–60.
Maschner, C., Moritz, B., and Schmitz, M. (2021).“Modern Asset Management.” In: _SSRN e-Print_.
Masini, R. P., Medeiros, M. C., and Mendes, E. F. (2021).“Machine Learning Advances for Time Series Forecasting.”
In: _arXiv e-Print_.
McCracken, M. W. (2020).“Tests of Conditional Predictive Ability: Existence, Size, and Power.” In: _SSRN e-Print_.
McDonald, S., Coleman, S., McGinnity, T. M., Li, Y., and Belatreche, A. (2014).“A comparison of forecasting
approaches for capital markets.” In: _IEEE Conference on Computational Intelligence for Financial Engineering
and Economics (CIFEr)_. London, UK: IEEE, pp. 32–39.
McIndoe, C. (2020).“A Data Driven Approach to Market Regime Classification.” MA thesis. Imperial College.
McMillan, D. G. (2021a).“Forecasting sector stock market returns.” In: _Journal of Asset Management_ 22(4), pp. 291–
300.
McMillan, D. G. (2021b).“Forecasting U.S. stock returns.” In: _The European Journal of Finance_ 27(1-2), pp. 86–
109.
Meligkotsidou, L., Panopoulou, E., Vrontos, I. D., and Vrontos, S. D. (2021).“Out-of-sample equity premium
prediction: a complete subset quantile regression approach.” In: _The European Journal of Finance_ 27(1-2),
pp. 110–135.
Menezes, A. G. and Mastelini, S. M. (2021).“MegazordNet: combining statistical and machine learning standpoints
for time series forecasting.” In: _arXiv e-Print_.


Messmer, M. and Audrino, F. (2020).“The Lasso and the Factor Zoo - Expected Returns in the Cross-Section.” In:
_SSRN e-Print_.
Micheli, A. and Neuman, E. (2022). “Evidence of Crowding on Russell 3000 Reconstitution Events.” In: _arXiv
e-Print_.
Mikeliani, R. and Kavlashvili, N. (2020).“Evaluation and comparison of machine learning and classical econometric
AR model on financial time series data.” MA thesis. University of Tartu.
Milevsky, M. A. (2020). _Retirement Income Recipes in R: From Ruin Probabilities to Intelligent Drawdowns_. Springer
International Publishing. 302 pp.
Montero-Manso, P., Athanasopoulos, G., Hyndman, R. J., and Talagala, T. S. (2020).“FFORMA: Feature-based
Forecast Model Averaging.” In: _International Jurnal of Forecasting_ 36 (1), pp. 86–92.
Montero-Manso, P. and Hyndman, R. J. (2020).“Principles and Algorithms for Forecasting Groups of Time Series:
Locality and Globality.” In: _arXiv e-Print_.
Montero-Manso, P. and Hyndman, R. J. (2021).“Principles and Algorithms for Forecasting Groups of Time Series:
Locality and Globality.” In: _International Journal of Forecasting_ 37(4), pp. 1632–1653.
Murray, M. H. and Blume, J. D. (2020).“False Discovery Rate Computation: Illustrations and Modifications.” In:
_arXiv e-Print_.
Neri, F. (2021).“Domain Specific Concept Drift Detectors for Predicting Financial Time Series.” In: _arXiv e-Print_.
Neto, A. E. D., Gonzalo, J., and Pitarakis, J.-Y. (2021).“Uncovering regimes in out of sample forecast errors.” In:
_Oxford Bulletin of Economics and Statistics_ 83(3), pp. 713–741.
Nevasalmi, L. (2020).“Forecasting multinomial stock returns using machine learning methods.” In: _The Journal of
Finance and Data Science_ 6, pp. 86–106.
Nevasalmi, L. (2022).“Recession forecasting with high-dimensional data.” In: _Journal of Forecasting_.
Nietert, B. and Otto, T. (2020).“Empirical asset pricing: economic significance and economic model evaluation.”
In: _SSRN e-Print_.
Noguer i Alonso, M., Batres-Estrada, G., and Moulin, A. (2020).“Deep Learning for Equity Time Series Prediction.”
In: _SSRN e-Print_.
Noguer i Alonso, M. and Srivastava, S. (2021).“The Shape of Performance Curve in Financial Time Series.” In:
_SSRN e-Print_.
Nonejad, N. (2021).“Bayesian model averaging and the conditional volatility process: an application to predicting
aggregate equity returns by conditioning on economic variables.” In: _Quantitative Finance_ 21(8), pp. 1387–1411.
Nybrant, A. (2021).“On Robust Forecast Combinations With Applications to Automated Forecasting.” MA thesis.
University of Uppsala.
Nystrup, P., Lindstrom, E., Møller, J. K., and Madsen, H. (2021).“Dimensionality reduction in forecasting with
temporal hierarchies.” In: _International Journal of Forecasting_ 37(3), pp. 1127–1146.
Odendahl, F., Rossi, B., and Sekhposyan, T. (2020).“Comparing Forecast Performance with State Dependence.”
In: _SSRN e-Print_.
Oh, D. H. and Patton, A. J. (2021).“Better the Devil You Know: Improved Forecasts from Imperfect Models.” In:
_Finance and Economics Discussion Series_ 2021(070), pp. 1–45.
Okuno, S., Aihara, K., and Hirata, Y. (2019).“Combining multiple forecasts for multivariate time series via state-
dependent weighting.” In: _Chaos_ 29(3), p. 033128.
Oreshkin, B. N., Carpov, D., Chapados, N., and Bengio, Y. (2019).“N-BEATS: Neural basis expansion analysis for
interpretable time series forecasting.” In: _arXiv e-Print_.
Oreshkin, B. N., Carpov, D., Chapados, N., and Bengio, Y. (2020).“N-BEATS: Neural basis expansion analysis for
interpretable time series forecasting.” In: _ICLR 2020 Conference_.
Papaioannou, P., Talmon, R., Serafino, D. di, and Siettos, C. (2021). “Time Series Forecasting Using Manifold
Learning.” In: _arXiv e-Print_.
Paranhos, L. (2021). “Predicting Inflation with Neural Networks.” In: _arXiv e-Print_.
Patton, A. J. (2020).“Comparing Possibly Misspecified Forecasts.” In: _Journal of Business & Economic Statistics_
38(4), pp. 796–809.
Perrin, S. and Roncalli, T. (2020).“Machine Learning Optimization Algorithms & Portfolio Allocation.” In: _Machine
Learning for Asset Management: New Developments and Financial Applications_. Ed. by E. Jurczenko. Wiley,
pp. 261–328.
Perron, P. and Yamamoto, Y. (2021).“Testing for Changes in Forecasting Performance.” In: _Journal of Business &
Economic Statistics_ 39(1), pp. 148–165.


Pesaran, M. H. and Smith, R. (2019).“The Role of Factor Strength and Pricing Errors for Estimation and Inference
in Asset Pricing Models.” In: _SSRN e-Print_.
Petropoulos, F., Apiletti, D., Assimakopoulos, V., Babai, M. Z., Barrow, D. K., Ben Taieb, S., Bergmeir, C., Bessa,
R. J., Bijak, J., Boylan, J. E., Browell, J., Carnevale, C., Castle, J. L., Cirillo, P., Clements, M. P., Cordeiro,
C., Oliveira, F. L. C., De Baets, S., Dokumentov, A., Ellison, J., Fiszeder, P., Franses, P. H., Frazier, D. T.,
Gilliland, M., Gonul, M. S., Goodwin, P., Grossi, L., Grushka-Cockayne, Y., Guidolin, M., Guidolin, M., Gunter,
U., Guo, X., Guseo, R., Harvey, N., Hendry, D. F., Hollyman, R., Januschowski, T., Jeon, J., Jose, V. R. R.,
Kang, Y., Koehler, A. B., Kolassa, S., Kourentzes, N., Leva, S., Li, F., Litsiou, K., Makridakis, S., Martin,
G. M., Martinez, A. B., Meeran, S., Modis, T., Nikolopoulos, K., Onkal, D., Paccagnini, A., Panagiotelis, A.,
Panapakidis, I., Pavia, J. M., Pedio, M., Pedregal, D. J., Pinson, P., Ramos, P., Rapach, D. E., Reade, J. J.,
Rostami-Tabar, B., Rubaszek, M., Sermpinis, G., Shang, H. L., Spiliotis, E., Syntetos, A. A., Talagala, P. D.,
Talagala, T. S., Tashman, L., Thomakos, D., Thorarinsdottir, T., Todini, E., Arenas, J. R. T., Wang, X.,
Winkler, R. L., Yusupova, A., and Ziel, F. (2022).“Forecasting: theory and practice.” In: _International Journal
of Forecasting_.
Petropoulos, F. and Grushka-Cockayne, Y. (2021).“Fast and Frugal Time Series Forecasting.” In: _SSRN e-Print_.
Petropoulos, F. and Spiliotis, E. (2021).“The Wisdom of the Data: Getting the Most Out of Univariate Time Series
Forecasting.” In: _Forecasting_ 3(3), pp. 478–497.
Petropoulos, F., Spiliotis, E., and Panagiotelis, A. (2021).“Model combinations through revised base-rates.” In:
_arXiv e-Print_.
Petropoulos, F. and Svetunkov, I. (2020).“A simple combination of univariate models.” In: _International Journal
of Forecasting_ 36(1), pp. 110–115.
Petropoulos, F., Wang, X., and Disney, S. M. (2019).“The inventory performance of forecasting methods: Evidence
from the M3 competition data.” In: _International Journal of Forecasting_ 35(1), pp. 251–265.
Pinho, D. M. (2020).“Forecast comparison of volatility models and their combinations (FTSE100): a tied race.”
MA thesis. Universidade do Minho.
Pinto, J. M. and Castle, J. (2021). _A machine learning dynamic switching approach to forecasting when there are
structural breaks_. Tech. rep. University of Oxford.
Pinto, J. M. and Marçal, E. F. (2019).“Cross-Validation Based Forecasting Method: A Machine Learning Approach.”
In: _SSRN e-Print_.
Pinto, J. M. and Marçal, E. F. (2020).“Inflation Rate Forecasting: Extreme Learning Machine as a Model Combi-
nation Method.” In: _Contributions to Statistics_. Springer International Publishing, pp. 365–385.
Pitarakis, J.-Y. (2020).“A Novel Approach to Predictive Accuracy Testing in Nested Environments.” In: _arXiv
e-Print_.
Post, T., Karabati, S., and Arvanitis, S. (2019).“Robust optimization of forecast combinations.” In: _International
Journal of Forecasting_ 35(3), pp. 910–926.
Prasad, V. V., Gumparthi, S., Venkataramana, L. Y., Srinethe, S., Sree, R. M. S., and Nishanthi, K. (2021).
“Prediction of Stock Prices Using Statistical and Machine Learning Models: A Comparative Analysis.” In: _The
Computer Journal_.
Prayogo, N., Cevik, M., and Bodur, M. (2020). “Time Series Sampling for Probabilistic Forecasting.” In: _Proceedings
of the 30th Annual International Conference on Computer Science and Software Engineering_. USA: IBM Corp.,
pp. 153–162.
Qian, W., Rolling, C. A., Cheng, G., and Yang, Y. (2019).“On the forecast combination puzzle.” In: _Econometrics_
7(3), p. 39.
Qian, W., Rolling, C. A., Cheng, G., and Yang, Y. (2022).“Combining forecasts for universally optimal perfor-
mance.” In: _International Journal of Forecasting_.
Qu, R., Timmermann, A., and Zhu, Y. (2021).“Comparing forecasting performance in cross-sections.” In: _Journal
of Econometrics_.
Quaedvlieg, R. (2021).“Multi-Horizon Forecast Comparison.” In: _Journal of Business & Economic Statistics_.
Radchenko, P., Vasnev, A. L., and Wang, W. (2022).“Too similar to combine? On negative weights in forecast
combination.” In: _International Journal of Forecasting_.
Rahimikia, E. and Poon, S.-H. (2021).“Machine Learning for Realised Volatility Forecasting.” In: _SSRN e-Print_.
Rajapaksha, D., Bergmeir, C., and Hyndman, R. J. (2021). “LoMEF: A Framework to Produce Local Explanations
for Global Model Time Series Forecasts.” In: _arXiv e-Print_.
Rao, A. and Jelvis, T. (2022). _Foundations of Reinforcement Learning with Applications in Finance_.


Rapach, D. and Zhou, G. (2022).“Asset Pricing: Time-Series Predictability.” In: _SSRN e-Print_.
Rapach, D. E., Strauss, J. K., Tu, J., and Zhou, G. (2019).“Industry return predictability: A machine learning
approach.” In: _The Journal of Financial Data Science_ 1(3), pp. 9–28.
Rapach, D. E. and Zhou, G. (2020).“Time-series and Cross-sectional Stock Return Forecasting: New Machine
Learning Methods.” In: _Machine Learning for Asset Management: New Developments and Financial Applications_.
Ed. by E. Jurczenko. Wiley, pp. 1–33.
Rehman, H.-U., Wan, G., Ullah, A., and Shaukat, B. (2019).“Individual and combination approaches to forecasting
hierarchical time series with correlated data: an empirical study.” In: _Journal of Management Analytics_ 6(3),
pp. 231–249.
Remlinger, C., Alasseur, C., Briere, M., and Mikael, J. (2022).“Expert Aggregation for Financial Forecasting.” In:
_SSRN e-Print_.
Reschenhofer, E., Mangat, M. K., Zwatz, C., and Guzmics, S. (2020).“Evaluation of current research on stock
return predictability.” In: _Journal of Forecasting_ 39(2), pp. 334–351.
Risse, M. (2017).“Combining Wavelet Decomposition with Machine Learning to Forecast Gold Returns.” In: _SSRN
e-Print_.
Roccazzella, F., Gambetti, P., and Vrins, F. (2022).“Optimal and robust combination of forecasts via constrained
optimization and shrinkage.” In: _International Journal of Forecasting_.
Roncalli, T. (2021).“Advanced Course in Asset Management.” In: _SSRN e-Print_.
Rossi, B. (2020).“Forecasting in the Presence of Instabilities: How Do We Know Whether Models Predict Well and
How to Improve Them.” In: _Journal of Economic Literature_.
Roy, R. (2021).“A six-factor asset pricing model: The Japanese evidence.” In: _Financial Planning Review_ 4(1).
Rožanec, J., Trajkova, E., Kenda, K., Fortuna, B., and Mladenić, D. (2021).“Explaining Bad Forecasts in Global
Time Series Models.” In: _Applied Sciences_ 11(19), p. 9243.
Ruan, J., Wu, W., and Luo, J. (2021).“Stock Price Prediction Under Anomalous Circumstances.” In: _arXiv e-Print_.
Ryll, L. and Seidens, S. (2019).“Evaluating the Performance of Machine Learning Algorithms in Financial Market
Forecasting: A Comprehensive Survey.” In: _arXiv e-Print_.
Rytchkov, O. and Zhong, X. (2020).“Information Aggregation and P-Hacking.” In: _Management Science_ 66(4),
pp. 1509–1782.
Salinas, D., Flunkert, V., and Gasthaus, J. (2020).“DeepAR: Probabilistic Forecasting with Autoregressive Recur-
rent Networks.” In: _International Journal of Forecasting_ 36 (3), pp. 1181–1191.
Salisu, A. A. and Tchankam, J. P. (2022).“US Stock return predictability with high dimensional models.” In:
_Finance Research Letters_ 45 (102194), pp. 153–163.
Salles, R., Pacitti, E., Bezerra, E., Porto, F., and Ogasawara, E. (2022).“TSPred: A framework for nonstationary
time series prediction.” In: _Neurocomputing_ 467, pp. 197–202.
Samuels, J. D. and Sekkel, R. M. (2017).“Model Confidence Sets and forecast combination.” In: _International
Journal of Forecasting_ 33(1), pp. 48–60.
Sarmas, E., Xidonas, P., and Doukas, H. (2020). _Multicriteria Portfolio Construction with Python_. Springer Inter-
national Publishing.
Seca, D. (2021).“TimeGym: Debugging for Time Series Modeling in Python.” In: _arXiv e-Print_.
Sharma, A., Syrgkanis, V., Zhang, C., and Kiciman, E. (2021). “DoWhy: Addressing Challenges in Expressing and
Validating Causal Assumptions.” In: _arXiv e-Print_.
Sharma, P. N., Shmueli, G., Sarstedt, M., Danks, N., and Ray, S. (2020).“Prediction-Oriented Model Selection in
Partial Least Squares Path Modeling.” In: _Decision Sciences_.
Shaub, D. (2020).“Fast and accurate yearly time series forecasting with forecast combinations.” In: _International
Journal of Forecasting_ 33(1), pp. 116–120.
Shi, X., Xu, D., and Zhang, Z. (2022). “Deep Learning Algorithms for Hedging with Frictions.” In: _arXiv e-Print_.
Siami-Namini, S., Tavakoli, N., and Namin, A. S. (2019).“A Comparative Analysis of Forecasting Financial Time
Series Using ARIMA, LSTM, and BiLSTM.” In: _arXiv e-Print_.
Siebert, J., Gross, J., and Schroth, C. (2021).“A systematic review of Python packages for time series analysis.”
In: _Engineering Proceedings_ 5(1) (22).
Siliverstovs, B. and Wochner, D. (2021).“State-Dependent Evaluation of Predictive Ability.” In: _Journal of Fore-
casting_ 40(3), pp. 547–574.
Simos, T. E., Mourtas, S. D., and Katsikis, V. N. (2021).“Time-varying Black–Litterman portfolio optimization
using a bio-inspired approach and neuronets.” In: _Applied Soft Computing_ 112, p. 107767.


Smith, S. C., Bulkley, G., and Leslie, D. S. (2020).“Equity Premium Forecasts with an Unknown Number of
Structural Breaks.” In: _Journal of Financial Econometrics_ 18(1), pp. 59–94.
Smith, S. C. and Timmermann, A. (2021).“Break Risk.” In: _The Review of Financial Studies_ 34(4), pp. 2045–2100.
Smyl, S. (2020).“A hybrid method of exponential smoothing and recurrent neural networks for time series fore-
casting.” In: _International Journal of Forecasting_ 36(1) (1), pp. 75–85.
Snow, D. (2019).“Machine learning in asset management.” In: _SSRN e-Print_.
Snow, D. (2020a).“Machine Learning in Asset Management - Part 2: Portfolio Construction - Weight Optimization.”
In: _The Journal of Financial Data Science_ 2 (2), pp. 17–24.
Snow, D. (2020b).“Machine Learning in Asset Management Part 1: Portfolio Construction Trading Strategies.” In:
_The Journal of Financial Data Science_ 2(1) (1), pp. 10–23.
Son, B. and Lee, J. (2022).“Graph-based multi-factor asset pricing model.” In: _Finance Research Letters_ 44 (102032).
Spiliotis, E., Abolghasemi, M., Hyndman, R. J., Petropoulos, F., and Assimakopoulos, V. (2021).“Hierarchical
forecast reconciliation with machine learning.” In: _Applied Soft Computing_ 112, p. 107756.
Spiliotis, E., Nikolopoulos, K., and Assimakopoulos, V. (2019).“Tales from tails: On the empirical distributions of
forecasting errors and their implication to risk.” In: _International Journal of Forecasting_ 35(2), pp. 687–698.
Stauskas, O. and Westerlund, J. (2022).“Tests of Equal Forecasting Accuracy for Nested Models with Estimated
CCE Factors.” In: _Journal of Business & Economic Statistics_ , pp. 1–14.
Stein, T. (2021).“Out-of-Sample Equity Premium Prediction: Combination Forecasts with Frequency-Decomposed
Variables.” In: _2nd Frontiers of Factor Investing Conference_.
Stivers, A. (2018).“Equity premium predictions with many predictors: A risk-based explanation of the size and
value factors.” In: _Journal of Empirical Finance_ 45, pp. 126–140.
Stoyanov, S. V. and Fabozzi, F. A. (2021).“Dynamics of Equity Factor Returns and Asset Pricing.” In: _Journal of
Financial Econometrics_.
Suhonen, A., Lennkh, M., and Perez, F. (2017).“Quantifying Backtest Overfitting in Alternative Beta Strategies.”
In: _The Journal of Portfolio Management_ 43 (2), pp. 90–104.
Svensson, M. (2018).“An Evaluation of Methods for Combining Univariate Time Series Forecasts.” MA thesis. Lund
University.
Tadayon, M. and Iwashita, Y. (2020).“Comprehensive Analysis of Time Series Forecasting Using Neural Networks.”
In: _arXiv e-Print_.
Taggart, R. J. (2021). “Evaluation of point forecasts for extreme events using consistent scoring functions.” In: _arXiv
e-Print_.
Taillardat, M., Fougeres, A.-L., Naveau, P., and de Fondeville, R. (2022). “Extreme events evaluation using CRPS
distributions.” In: _arXiv e-Print_.
Talagala, T. S., Li, F., and Kang, Y. (2021).“FFORMPP: Feature-based forecast model performance prediction.”
In: _arXiv e-Print_.
Talagala, T. S., Li, F., and Kang, Y. (2022).“FFORMPP: Feature-based forecast model performance prediction.”
In: _International Journal of Forecasting_.
Tang, X., Hu, F., and Wang, P. (2018).“Out-of-sample equity premium prediction: A scenario analysis approach.”
In: _Journal of Forecasting_ 37(5), pp. 604–626.
Tatsat, H., Puri, S., and Lookabaugh, B. (2020). _Machine Learning and Data Science Blueprints for Finance: From
Building Trading Strategies to Robo-Advisors Using Python_. O’Reilly. 400 pp.
Taylor, J. W. and Taylor, K. S. (2021).“Combining probabilistic forecasts of COVID-19 mortality in the United
States.” In: _European Journal of Operational Research_.
Theodosiou, F. and Kourentzes, N. (2021).“Forecasting with Deep Temporal Hierarchies.” In: _SSRN e-Print_.
Thomson, M. E., Pollock, A. C., Onkal, D., and Gonul, M. S. (2019).“Combining forecasts: Performance and
coherence.” In: _International Journal of Forecasting_ 35(2), pp. 474–484.
Thorarinsdottir, T. L. (2021).“Forecast evaluation.” In: _CUSO winter school_.
Tilly, S., Ebner, M., and Livan, G. (2021).“Macroeconomic forecasting through news, emotions and narrative.” In:
_Expert Systems with Applications_ 175, p. 114760.
Tilly, S. and Livan, G. (2021).“Macroeconomic forecasting with statistically validated knowledge graphs.” In: _Expert
Systems with Applications_ 186, p. 115765.
Timmermann, A. (2018).“Forecasting methods in finance.” In: _Annual Review of Financial Economics_ 10(1),
pp. 449–470.


Trucı́os, C., Mazzeu, J. H. G., Hallin, M., Hotta, L. K., Pereira, P. L. V., and Zevallos, M. (2021).“Forecasting
Conditional Covariance Matrices in High-Dimensional Time Series: a General Dynamic Factor Approach.” In:
_Journal of Business & Economic Statistics_ , pp. 1–35.
Tuck, J., Barratt, S., and Boyd, S. (2022).“Portfolio Construction Using Stratified Models.” In: _Machine Learning
in Financial Markets: A guide to contemporary practices_. Ed. by A. Capponi and C.-A. Lehalle. Cambridge
University Press.
Tunaru, D., Fabozzi, F. A., and Fabozzi, F. J. (2021).“Testing the Forecasting Ability of Multi-Factor Models on
Non-US Interbank Rates.” In: _The Journal of Fixed Income_ 31(2).
Ungolo, F., Sherris, M., and Zhou, Y. (2021).“affine_mortality: A Github repository for estimation, analysis, and
projection of affine mortality models.” In: _SSRN e-Print_.
Vaiciukynas, E., Danenas, P., Kontrimas, V., and Butleris, R. (2022).“Two-Step Meta-Learning for Time-Series
Forecasting Ensemble.” In: _IEEE Access_ 9, pp. 62687–62696.
Vamossy, D. and Skog, R. (2021). “EmTract: Investor Emotions and Market Behavior.” In: _arXiv e-Print_.
van Dijk, D. and Franses, P. H. (2019).“Combining expert-adjusted forecasts.” In: _Journal of Forecasting_ 38(5),
pp. 415–421.
Vanini, P. (2020).“Asset Management.” In: _SSRN e-Print_.
Vincent, K., Hsu, Y.-C., and Lin, H.-W. (2020).“Investment styles and the multiple testing of cross-sectional stock
return predictability.” In: _Journal of Financial Markets_.
Vinod, H. D. (2021).“R Package GeneralCorr Functions for Portfolio Choice.” In: _SSRN e-Print_.
Viswanathan, T. and Stephen, M. (2020).“Does Machine Learning Algorithms Improve Forecasting Accuracy?
Predicting Stock Market Index Using Ensemble Model.” In: _Advances in Distributed Computing and Machine
Learning_. Springer Singapore, pp. 511–519.
Vovk, V. and Wang, R. (2021).“E-values: Calibration, combination, and applications.” In: _Annals of Statistics_
49(3), pp. 1736–1753.
Wang, H., Ahluwalia, H. S., Aliaga-Diaz, R. A., and Davis, J. H. (2021a).“The Best of Both Worlds: Forecasting US
Equity Market Returns Using a Hybrid Machine Learning Time Series Approach.” In: _The Journal of Financial
Data Science_ 3(2), pp. 9–20.
Wang, R. and Ramdas, A. (2020).“False discovery rate control with e-values.” In: _arXiv e-Print_.
Wang, Y., Hao, X., and Wu, C. (2021b).“Forecasting stock returns: A time-dependent weighted least squares
approach.” In: _Journal of Financial Markets_ 53 (100568), p. 100568.
Wang, Y., Smola, A., Maddix, D., Gasthaus, J., Foster, D., and Januschowski, T. (2019).“Deep Factors for Fore-
casting.” In: _Proceedings of Machine Learning Research_ 97, pp. 6607–6617.
Weigand, A. (2019).“Machine learning in empirical asset pricing.” In: _Financial Markets and Portfolio Management_
33, pp. 93–104.
Weiss, C. E., Raviv, E., and Roetzer, G. (2018).“Forecast Combinations in R using the ForecastComb Package.”
In: _The R Journal_ 10(2), pp. 262–281.
Wellens, A. P., Udenio, M., and Boute, R. N. (2022).“Transfer learning for hierarchical forecasting: Reducing
computational efforts of M5 winning methods.” In: _International Journal of Forecasting_.
Wen, D., He, M., Zhang, Y., and Wang, Y. (2022).“Forecasting realized volatility of Chinese stock market: A simple
but efficient truncated approach.” In: _Journal of Forecasting_.
Westerlund, J., Karabiyik, H., and Narayan, P. (2017).“Testing for Predictability in panels with General Predictors.”
In: _Journal of Applied Econometrics_ 32(3), pp. 554–574.
Winkler, R. L. (2015).“Equal Versus Differential Weighting in Combining Forecasts.” In: _Risk Analysis_ 35(11),
pp. 16–18.
Wu, H., Xu, J., Wang, J., and Long, M. (2022).“Autoformer: Decomposition Transformers with Auto-Correlation
for Long-Term Series Forecasting.” In: _arXiv e-Print_.
Wu, Q., Brinton, C. G., Zhang, Z., Pizzoferrato, A., Liu, Z., and Cucuringu, M. (2021a). “Equity2Vec: End-to-end
Deep Learning Framework for Cross-sectional Asset Pricing.” In: _arXiv e-Print_.
Wu, X., Zhang, D., Guo, C., He, C., Yang, B., and Jensen, C. S. (2021b). “AutoCTS: Automated Correlated Time
Series Forecasting – Extended Version.” In: _arXiv e-Print_.
Xie, A. (2021).“Forecasting Long-Term Equity Returns: A Comparison of Popular Methodologies.” In: _SSRN e-
Print_.
Xu, W., Liu, W., Bian, J., Yin, J., and Liu, T.-Y. (2021). “Instance-wise Graph-based Framework for Multivariate
Time Series Forecasting.” In: _arXiv e-Print_.


Xu, W., Liu, W., Wang, L., Xia, Y., Bian, J., Yin, J., and Liu, T.-Y. (2022). “HIST: A Graph-based Framework
for Stock Trend Forecasting via Mining Concept-Oriented Shared Information.” In: _arXiv e-Print_.
Yang, J.-Y., Zhu, H., Hou, Y.-J., Zhang, P., and Zhou, C.-C. (2021). “Why Existing Machine Learning Methods
Fails At Extracting the Information of Future Returns Out of Historical Stock Prices : the Curve-Shape-Feature
and Non-Curve-Shape-Feature Modes.” In: _arXiv e-Print_.
Yang, L., Li, J., Dong, R., Zhang, Y., and Smyth, B. (2022). “NumHTML: Numeric-Oriented Hierarchical Trans-
former Model for Multi-task Financial Forecasting.” In: _arXiv e-Print_.
Yang, Y., UY, M. C. S., and Huang, A. (2020). “FinBERT: A Pretrained Language Model for Financial Commu-
nications.” In: _arXiv e-Print_.
Yara, F. B., Boons, M., and Tamoni, A. (2021).“Value return predictability across asset classes and commonalities
in risk premia.” In: _Review of Finance_ 25(2), pp. 449–484.
Yeoleka, A., Patel, S., Talla, S., Puthucode, K. R., Ahmadzadeh, A., Sadykov, V. M., and Angryk, R. A. (2021).
“Feature Selection on a Flare Forecasting Testbed: A Comparative Study of 24 Methods.” In: _arXiv e-Print_.
Yin, A. (2021).“Equity premium prediction: keep it sophisticatedly simple.” In: _Quantitative Finance and Economics_
5(2), pp. 264–286.
Yu, L., Hardle, W. K., Borke, L., and Benschop, T. (2020).“An AI approach to measuring financial risk.” In: _SSRN
e-Print_.
Zang, C. (2017).“Deep Learning in Multiple Multistep Time Series Prediction.” In: _arXiv e-Print_.
Zeng, Z., Balch, T., and Veloso, M. (2021).“Deep Video Prediction for Time Series Forecasting.” In: _arXiv e-Print_.
Zhan, T. and Xiao, F. (2021).“A Fast Evidential Approach for Stock Forecasting.” In: _arXiv e-Print_.
Zhang, H. (2021).“Empirical asset pricing and ensemble machine learning.” PhD thesis. Tilburg University.
Zhao, L. (2020).“Essays on Asset Pricing: A Model Comparison Perspective.” PhD thesis. Washington University
in St. Louis.
Zhao, Y. (2021).“The robustness of forecast combination in unstable environments: a Monte Carlo study of advanced
algorithms.” In: _Empirical Economics_ 61, pp. 173–199.
Zhao, Y., Wang, Y., Liu, J., Xia, H., Xu, Z., Hong, Q., Zhou, Z., and Petzold, L. (2021). “Empirical Quantitative
Analysis of COVID-19 Forecasting Models.” In: _arXiv e-Print_.
Zhu, L., Basu, S., Jarrow, R. A., and Wells, M. T. (2021). “High-Dimensional Estimation, Basis Assets, and the
Adaptive Multi-Factor Model.” In: _arXiv e-Print_.
Zhu, Y. and Timmermann, A. (2020).“Can Two Forecasts Have the Same Conditional Expected Accuracy?” In:
_arXiv e-Print_.
Ziel, F. and Berk, K. (2019).“Multivariate Forecasting Evaluation: On Sensitive and Strictly Proper Scoring Rules.”
In: _arXiv e-Print_.


## Appendix A: Overviews of investment processes and models in QWIM

### References

List of references:
Coqueret and Guida ( _Machine Learning for Factor Investing: R Version_ , 2020)
Dixon et al. ( _Machine Learning in Finance: from theory to practice_ , 2020)
Fabozzi et al. ( _Asset Management: Tools and Issues_ , 2021)
Grealish and Kolm (“Robo-Advisory: From Investing Principles and Algorithms to Future Developments,” 2021)
Homescu (“Many risks, one (optimal) portfolio,” 2014)
Homescu (“Better Investing Through Factors, Regimes and Sensitivity Analysis,” 2015)
Jansen ( _Machine Learning for Algorithmic Trading (Second Edition)_ , 2020)
Jurczenko et al. ( _Machine Learning for Asset Management_ , 2020)
Kritzman et al. ( _A Practitioner’s Guide to Asset Allocation_ , 2017)
Lopez de Prado ( _Machine learning for asset managers_ , 2020)
Maschner et al. (“Modern Asset Management,” 2021)
Perrin and Roncalli (“Machine Learning Optimization Algorithms & Portfolio Allocation,” 2020)
Roncalli (“Advanced Course in Asset Management,” 2021)
Vanini (“Asset Management,” 2020)

### Online courses

List of online courses:

- Investment Management with Python and Machine Learning Specialization

```
Introduction to Portfolio Construction and Analysis with Python
Advanced Portfolio Construction and Analysis with Python
Python and Machine Learning for Asset Management
Python and Machine Learning for Asset Management with Alternative Data Sets
```
- Machine Learning and Reinforcement Learning in Finance Specialization

```
Guided Tour of Machine Learning in Finance
Fundamentals of Machine Learning in Finance
Reinforcement Learning in Finance
Overview of Advanced Methods of Reinforcement Learning in Finance
```
- Investment Management Specialization

```
Understanding Financial Markets
Meeting Investors’ Goals
Portfolio and Risk Management
Securing Investment Returns in the Long Run
Planning your Client’s Wealth over a 5-year Horizon
```
- Investment and Portfolio Management Specialization

```
Global Financial Markets and Instruments
Portfolio Selection and Risk Management
Biases and Portfolio Selection
Investment Strategies and Portfolio Analysis
Build a Winning Investment Portfolio
```

## Appendix C: Comparison of investment using portfolios metrics and benchmark portfolios

## mark portfolios

For your QWIM project it is likely that you would compare investment portfolios constructed using your method(s)
versus benchmark portfolios constructed using most common "optimal portfolio" types used in the industry and in
academia. See below for an example of how this can be done.

```
Figure 6: Example of portfolio optimization process
```
Source:PyPortfolioOpt

### Portfolio optimization methods

List of portfolio optimization methods may include (seeRoncalli (“Advanced Course in Asset Management,” 2021)
and Perrin and Roncalli (“Machine Learning Optimization Algorithms & Portfolio Allocation,” 2020)for a com-
prehensive overview of such methods):

- equal weighting
- mean variance optimization (Markowitz)
- minimum variance optimization
- maximum diversification
- risk budgeting/risk parity
- hierarchical risk parity
- Black-Litterman
- robust versions of some the above portfolio optimization methods

Some relevant links:

- Portfolio Optimization: A General Framework for Portfolio Choice
- Performance of risk-based asset allocation strategies
- Revisiting the Portfolio Optimization Machine Portfolio
- Construction Techniques Applied to Traditional Multi Asset Portfolios


### Python and R packages/codes for portfolio optimization

- Codes mentioned inSnow (“Machine Learning in Asset Management - Part 2: Portfolio Construction - Weight
    Optimization,” 2020)
- Empyrial
- MLFinLab
- Optimal Portfolio
- PortfolioAnalytics
- PortfolioLab
- PyPortfolioOpt
- Quantropy
- Riskfolio-Lib
- RiskPortfolios
- riskparityportfolio

### Portfolio metrics

List of portfolio metrics may include some of the following (seeBacon (“Performance Attribution: History and
Progress,” 2019)for a comprehensive list):

- Sharpe ratio
- Sortino ratio
- Information ratio
- Maximum Drawdown
- expected shortfall
- maximum loss
- and more.

Some relevant links:

- Portfolio metrics
- Picking the Right Risk-Adjusted Performance Metric
- Risk-Adjusted Performance Measurement – State of the Art
- An Investor’s Guide to the Risk Versus Return Conundrum
- How sharp is the Sharpe ratio? Risk-adjusted Performance Measures


### Python and R packages/codes for portfolio metrics and performance evaluation

- bt
- empyrical
- ffn
- JFE
- MLFinLab
- PerformanceAnalytics
- portfolioBacktest
- Portfolio Optimization and Performance Evaluation
- Pyfolio
- QuantStats
- Riskfolio-Lib
- tidyquant

### How to compare investment portfolios

Let us consider portfolio optimization methods (selected from the ones implemented in Python and/or R packages
mentioned above, such as PyPortfolioOpt) which rely on based on expected returns and expected covariance matrix.
One would construct two portfolios (let’s call them Traditional and Enhanced) using the same portfolio op-
timization method(s), where the only difference would be in terms of the inputs (expected returns and expected
covariance matrix) to the optimization method:
As of the date of portfolio construction, expected returns and expected covariance matrix can be either calculated
using only historical data or, respectively, output from your model. Then one would compare side-by-side various
portfolio metrics for these two portfolios. Comparison would be done across the entire Out-Of-Sample period, and
also across each market regine period.
NOTE: If you have N forecasting methods used in your coding framework, then for each optimizaton method
you would end up with (1+N) optimal portfolios
To exemplifty, let’s say that you want to construct portfolios at date of June 20, 2019, and you have data as
below

- Range of entire dataset: January 1st, 1990 - August 1, 2020
- Range of Training dataset: January 1st, 1990- February 20, 2017
- Range of Test dataset: February 20, 2017 - August 1, 2020

For Traditional portfolio:

- vector of expected means is calculated based on historical data available at June 20, 2019 (namely from 1990
    to June 19, 2019)
- expected covariance matrix is calculated based on historical data available at June 20, 2019 (namely from
    1990 to June 19, 2019)

For Enhanced portfolio:

- vector of expected means is calculated based on forecasted values available at June 20, 2019 and obtained
    using the forecasted model trained on given training dataset (which is from 1990 to 2017)


- expected covariance matrix is calculated based on forecasted values available at June 20, 2019 and obtained
    using the forecasted model trained on given training dataset (which is from 1990 to 2017)

Then one would compare various portfolio metrics among the two portfolios. These metrics can be calculated on
following time periods:

- from date of portfolio construction (June 20, 2019) to last date for which you have data (August 1, 2020)
- from starting date of dataset (January 1st, 1990) to last date for which you have data (August 1, 2020)
- from starting date of dataset (January 1st, 1990) to date of portfolio construction (June 20, 2019)

So you would have side-by-side comparisons of portfolio metrics for each of the above 3 time periods.
Portfolio metrics can be calculated using various Python and/or R packages mentioned above.


