# Machine learning (and more) for scenario generation and data

# augmentation in quantitative wealth and investment management

# QWIM

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
1.1 Need for additional data forQWIM.................................... 4
1.2 Using ML to generate synthetic data forQWIM............................. 4

**2 Relevant references 6**
2.1 Main references................................................ 6
2.2 Comprehensive list of references....................................... 8
2.2.1 Scenarios incorporating interactions and dependencies across and within market periods... 8
2.2.2 Scenarios based on subsets of factors................................ 8
2.2.3 Incorporating expert views within scenarios............................ 8
2.2.4 Data augmentation and scenarios generated using machine learning within context of QWIM 8
2.2.5 Scenarios based on flexible probabilities.............................. 9
2.2.6 Scenarios based on Monte Carlo simulation............................ 9
2.2.7 Scenarios constructed using bootstrapping approach....................... 10
2.2.8 Scenarios constructed using resampling approach......................... 10
2.2.9 Scenarios based on similarities and discords within time series.................. 10



      - 2.2.10 Data augmentation and scenario generation using machine learning models
      - 2.2.11 Scenarios for extreme events and stress testing
      - 2.2.12 Scenarios for extreme events and stress testing within context of QWIM.
      - 2.2.13 Economic scenario generators.
      - 2.2.14 Scenarios incorporating dependencies (correlations, covariances, copulas).
      - 2.2.15 Extreme events and scenarios.
      - 2.2.16 Extreme events and scenarios within context of QWIM
      - 2.2.17 Scenarios based on agent-based modeliing
      - 2.2.18 Validating scenarios and augmented datasets
      - 2.2.19 Software implementations and frameworks.
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

Statistical risk management approaches like Value at Risk (VaR) proved largely ineffective in addressing the kinds
of market movements that occurred with past crisis periods. Scenario analysis addresses many of the shortcomings
of the statistical approache, since it is both forward looking and also able to draw on historical experience that
might not be represented in the development samples for statistical approaches.
There is a need to conduct rigorous and systematic scenario analysis. A key challenge in applying scenario
analysis is constructing “tail event” scenarios that are severe but plausible. We can assess scenario’s plausibility
by reference to the behavior of observable variables used to define the scenario (e.g., asset prices, bond yields,
credit spreads, etc.). To generate realistic scenarios in all relevant market regimes we can use use machine learning
approaches to identify regimes.
Additional scenarios can also be generated through “data augmentation” algorithms used in machine learning
(e.g., through transfer learning or generative adversarial networks GANs).

### 1.1 Need for additional data for QWIM

Not having sufficient data (due to medium to low sampling frequency and/or limited historical data) will have an
impact on

- adequately trainingMLmodels
- tackling unbalanced datasets
- data anonymization and preserving of data privacy
- comprehensive testing of investment strategies and portfolios
- robust portfolio construction
- portfolio risk management
Synthetic data can be obtained through
- ML-based data augmentation **DAug**
- data similarity with data in other time periods
- combine observations with expert views
- agent based modeling
- scenario generation
- construction of stress scenarios

### 1.2 Using ML to generate synthetic data for QWIM

There is significant need for additional data inQWIM

- for adequately trainingMLmodels
- to tackle unbalanced datasets
- for constructing a very comprehensive set of scenarios incorporating most scenarios which were not observed,
    yet are plausible and consistent with market and investor behavior and with economic intuition
- for data anonymization and preserving of data privacy
- for comprehensive testing of investment strategies and portfolios
- for constructing much more robust portfolios using scenario-based optimization


- for better risk management of investment portfolios
Assefa et al. (“Generating Synthetic Data in Finance: Opportunities, Challenges and Pitfalls,” 2019):
synthetic data defined as data obtained from a generative process that learns properties of real data
Synthetic financialTSdata is expected to have universal features, commonly referred to as stylized facts, together
with specialized features of a specific asset class or investment vehicle. When classical approaches are considered,
these stylized facts are often formulated in terms of distribution of returns.
Most promisingMLmethods to generate synthetic financialTS:
- generative adversarial networks GANS
- Variational Autoencoders VAEs
- Restricted Boltzmann Machine RBM


## 2 Relevant references

### 2.1 Main references

List of references:
Alaa et al. (“How Faithful is your Synthetic Data? Sample-level Metrics for Evaluating and Auditing Generative
Models,” 2022)
Asch et al. (“Model-assisted deep learning of rare extreme events from partial observations,” 2022)
Bahrpeyma et al. (“A Methodology for Validating Diversity in Synthetic Time Series Generation,” 2021)
Bhatia et al. (“ExGAN: Adversarial Generation of Extreme Samples,” 2021)
Bond-Taylor et al. (“Deep Generative Modelling: A Comparative Review of VAEs, GANs, Normalizing Flows,
Energy-Based and Autoregressive Models,” 2022)
Bandara et al. (“Improving the accuracy of global forecasting models using time series data augmentation,”
2021)
Buehler et al. (“A Data-driven Market Simulator for Small Data Environments,” 2020)
Buehler et al. (“Generating financial markets with signatures,” 2021)
Cerqueira et al. (“Evaluating time series forecasting models: an empirical study on performance estimation
methods,” 2020)
Cubuk et al. (“RandAugment: Practical data augmentation with no separate search,” 2019)
Czasonis et al. (“Enhanced Scenario Analysis,” 2020)
Czasonis et al. (“Relevance,” 2021)
Dahl and Sorensen (“Time Series (re)sampling using Generative Adversarial Networks,” 2021)
Da Silva and Shi (“Towards Improved Generalization in Financial Markets with Synthetic Data Generation,”
2019)
Debnath et al. (“Exploring Generative Data Augmentation in Multivariate Time Series Forecasting : Opportu-
nities and Challenges,” 2021)
De Gennaro Aquino et al. (“Portfolio Selection With Exploration of New Investment Opportunities,” 2021)
De Meer et al. (“Tackling the exponential scaling of signature-based GANs for high-dimensional financial time
series generation,” 2021)
De Meer Pardo (“Enriching Financial Datasets with Generative Adversarial Networks,” 2019)
Diffenbaugh (“Verification of extreme event attribution: Using out-of-sample observations to assess changes in
probabilities of unprecedented events.,” 2020)
Ding et al. (“Modeling Extreme Events in Time Series Prediction,” 2019)
Dogariu et al. (“Towards Realistic Financial Time Series Generation via Generative Adversarial Learning,” 2021)
Dogariu et al. (“Generation of Realistic Synthetic Financial Time-Series,” 2021)
Faggini et al. (“Crises in economic complex networks: Black Swans or Dragon Kings?” 2019)
Flaig and Junike (“Scenario generation for market risk models using generative neural networks,” 2022)
Franco-Pedroso et al. (“The ETS challenges: a machine learning approach to the evaluation of simulated financial
time series for improving generation processes,” 2019)
Franco-Pedroso et al. (“Generating Virtual Scenarios of Multivariate Financial Data for Quantitative Trading
Applications,” 2019)
Fons et al. (“Adaptive Weighting Scheme for Automatic Time-Series Data Augmentation,” 2021)
Fons et al. (“Augmenting Transferred Representations for Stock Classification,” 2021)
Fritzsch et al. (“Marginals Versus Copulas: Which Account For More Model Risk In Multivariate Risk Fore-
casting?” 2021)
Fu et al. (“Data augmentation for time series,” 2020)
Golub et al. (“Market-Driven Scenarios: An Approach for Plausible Scenario Construction,” 2018)
He et al. (“Data Augmentation Revisited: Rethinking the Distribution Gap between Clean and Augmented
Data,” 2019)
Heaton and Witte (“Synthetic Financial Data: An Application to Regulatory Compliance for Broker-Dealers,”
2021)
Kang et al. (“GRATIS: GeneRAting TIme Series with diverse and controllable characteristics,” 2020)
Kang et al. (“Déjà vu: A data-centric forecasting approach through time series cross-similarity,” 2021)
Kondratyev and Schwarz (“The Market Generator,” 2020)


Koshiyama et al. (“Generative Adversarial Networks for Financial Trading Strategies Fine-Tuning and Combi-
nation,” 2021)
Kritzman et al. (“Portfolio Choice with Path-Dependent Scenarios,” 2021)
Kritzman and Turkington (“History, Shocks, and Drifts: A New Approach to Portfolio Formation,” 2022)
Lerch et al. (“Forecaster’s Dilemma: Extreme Events and Forecast Evaluation,” 2017)
Lezmi et al. (“Improving the Robustness of Trading Strategy Backtesting with Boltzmann Machines and Gen-
erative Adversarial Networks,” 2020)
Lezmi et al. (“Portfolio Allocation with Skewness Risk: A Practical Guide,” 2019)
Li et al. (“SynC: A Copula based Framework for Generating Synthetic Data from Aggregated Sources,” 2020)
Liu et al. (“Efficient Time Series Augmentation Methods,” 2020)
Mannix and Cesa (“’Signatures’ promise quants a tool for all jobs,” 2021)
Mariani et al. (“PAGAN: Portfolio Analysis with Generative Adversarial Networks,” 2019)
Marti et al. (“Exploring and measuring non-linear correlations: Copulas, Lightspeed Transportation and Clus-
tering,” 2017)
Marti (“CORRGAN: sampling realistic financial correlation matrices using generative adversarial networks,”
2020)
Marti et al. (“cCorrGAN: Conditional Correlation GAN for Learning Empirical Conditional Distributions in the
Elliptope,” 2021)
Kuchnik and Smith (“Efficient Augmentation via Data Subsampling,” 2018)
Packham and Woebbeking (“Correlation scenarios and correlation stress testing,” 2021)
Papenbrock et al. (“Matrix Evolutions: Synthetic Correlations and Explainable Machine Learning for Con-
structing Robust Investment Portfolios,” 2021)
Paul et al. (“PSA-GAN: Progressive Self Attention GANs for Synthetic Time Series,” 2022)
Pei et al. (“Towards Generating Real-World Time Series Data,” 2021)
Raab et al. (“Assessing, visualizing and improving the utility of synthetic data,” 2021)
Raghunathan (“Synthetic Data,” 2021)
Rosen and Saunders (“Regress under stress: A simple least-squares method for integrating economic scenarios
with risk simulations,” 2016)
Rosen (“Integrating Economic Scenarios with Advanced Scenario Analytics to Manage Investment Portfolios,”
2015)
Rosen (“Re-Thinking Scenarios: Stress Testing of Multi-Asset Portfolios by Integrating Economic Scenarios
with Advanced Simulation Analytics,” 2015)
Rosolia and Osterrieder (“Analyzing Deep Generated Financial Time Series for Various Asset Classes,” 2021)
Sahamkhadam and Stephan (“Portfolio Optimization Based on Forecasting Models Using Vine Copulas: An
Empirical Assessment for the Financial Crisis,” 2021)
Sapp (“Efficient Estimation of Distributional Tail Shape and the Extremal Index with Applications to Risk
Management,” 2017)
Sharma et al. (“V- U-, L- or W- shaped economic recovery after Covid-19: Insights from an Agent Based Model,”
2021)
Silva and Ferreira (“Surrogate Monte Carlo,” 2021)
Snow (“DataGene: A Framework for Dataset Similarity,” 2020)
Takahashi et al. (“Modeling financial time-series with generative adversarial networks,” 2019)
Wang et al. (“Scalable Data Augmentation for Deep Learning,” 2019)
Wen et al. (“Time Series Data Augmentation for Deep Learning: A Survey,” 2021)
Wiese et al. (“Quant GANs: deep generation of financial time series,” 2020)
Yuan and Yuan (“A Monte Carlo synthetic sample based performance evaluation method for covariance matrix
estimators,” 2021)
Zhang et al. (“DADA: Deep Adversarial Data Augmentation for Extremely Low Data Regime Classification,”
2018)
Ziyin et al. (“What Data Augmentation Do We Need for Deep-Learning-Based Finance?” 2021)
Zorn (“Panic-aware portfolio optimization,” 2019)


### 2.2 Comprehensive list of references

**2.2.1 Scenarios incorporating interactions and dependencies across and within market periods**
List of references:
Bass et al. (“Factor Performance Across Market-Driven Scenarios,” 2018)
Czasonis et al. (“Enhanced Scenario Analysis,” 2020)
Czasonis et al. (“Relevance,” 2021)
Golub et al. (“Market-Driven Scenarios: An Approach for Plausible Scenario Construction,” 2018)
Kritzman et al. (“Portfolio Choice with Path-Dependent Scenarios,” 2021)
Kritzman and Turkington (“History, Shocks and Drifts: A New Approach to Portfolio Formation,” 2021)
Papenbrock et al. (“Matrix Evolutions: Synthetic Correlations and Explainable Machine Learning for Con-
structing Robust Investment Portfolios,” 2021)

**2.2.2 Scenarios based on subsets of factors**
List of references:
Glasserman et al. (“Stress scenario selection by empirical likelihood,” 2015)
Rosen and Saunders (“Regress under stress: A simple least-squares method for integrating economic scenarios
with risk simulations,” 2016)
Rosen and Saunders (“Regress Under Stress: A Simple Least-Squares Method for Integrating Economic Scenarios
with Risk Simulations,” 2015)
Rosen (“Integrating Economic Scenarios with Advanced Scenario Analytics to Manage Investment Portfolios,”
2015)
Rosen (“Re-Thinking Scenarios: Stress Testing of Multi-Asset Portfolios by Integrating Economic Scenarios
with Advanced Simulation Analytics,” 2015)

**2.2.3 Incorporating expert views within scenarios**
List of references:
Bolger and Wright (“Use of expert knowledge to anticipate the future: Issues, analysis and directions,” 2017)
Colson and Cooke (“Cross validation for the classical model of structured expert judgment,” 2017)
Davis and Lleo (“A Simple Procedure for Combining Expert Opinion with Statistical Estimates to Achieve
Superior Portfolio Performance,” 2016)
Davis and Lleo (“Behaviouralizing Black-Litterman: Expert Opinions and Behavioural Biases in a Diffusion
Setting,” 2015)
Franses and Bruijn (“Benchmarking Judgmentally Adjusted Forecasts,” 2017)
Gzyl et al. (“Inferring probability densities from expert opinion,” 2017)
Hsu et al. (“Bridging the divide in financial market forecasting: machine learners vs. financial economists,”
2016)
Johnson and West (“Bayesian Predictive Synthesis: Forecast Calibration and Combination,” 2018)
Nguyen and Chamroukhi (“Practical and theoretical aspects of mixture-of-experts modeling: An overview,”
2018)
Panchekha et al. (“Ensemble Active Management,” 2018)
Silva et al. (“A more human-like portfolio optimization approach,” 2017)
Wood (“How sure are we? Two approaches to statistical inference,” 2018)

**2.2.4 Data augmentation and scenarios generated using machine learning within context of QWIM**
List of references:
Buehler et al. (“Deep hedging,” 2019)
Buehler et al. (“A Data-driven Market Simulator for Small Data Environments,” 2020)
Buehler et al. (“Generating financial markets with signatures,” 2021)
Coletta et al. (“Towards Realistic Market Simulations: a Generative Adversarial Networks Approach,” 2021)
De Meer Pardo (“Enriching Financial Datasets with Generative Adversarial Networks,” 2019)


De Meer Pardo and Lopez (“Mitigating Overfitting on Financial Datasets with Generative Adversarial Net-
works,” 2020)
de Miranda Cardoso et al. (“Algorithms for Learning Graphs in Financial Markets,” 2020)
Eckerli (“Generative Adversarial Networks in finance: an overview,” 2021)
Fons et al. (“Adaptive Weighting Scheme for Automatic Time-Series Data Augmentation,” 2021)
Fons et al. (“Augmenting Transferred Representations for Stock Classification,” 2021)
Franco-Pedroso et al. (“Generating Virtual Scenarios of Multivariate Financial Data for Quantitative Trading
Applications,” 2019)
Franco-Pedroso et al. (“The ETS challenges: a machine learning approach to the evaluation of simulated financial
time series for improving generation processes,” 2019)
Heaton and Witte (“Synthetic Financial Data: An Application to Regulatory Compliance for Broker-Dealers,”
2021)
Henry-Labordere (“Generative models for financial data,” 2019)
Kondratyev and Schwarz (“The Market Generator,” 2020)
Koshiyama et al. (“Generative Adversarial Networks for Financial Trading Strategies Fine-Tuning and Combi-
nation,” 2021)
Lezmi et al. (“Improving the Robustness of Trading Strategy Backtesting with Boltzmann Machines and Gen-
erative Adversarial Networks,” 2020)
Marti (“CORRGAN: sampling realistic financial correlation matrices using generative adversarial networks,”
2020)
Marti (“Generating Realistic Synthetic Data in Finance: Applications of GANs,” 2020)
Rikli et al. (“Wasserstein GAN: Deep Generation applied on Bitcoins financial time series,” 2021)
Rosolia and Osterrieder (“Analyzing Deep Generated Financial Time Series for Various Asset Classes,” 2021)
Shah and Shroff (“Forecasting Market Prices using DL with Data Augmentation and Meta-learning: ARIMA
still wins!” 2021)
Takahashi et al. (“Modeling financial time-series with generative adversarial networks,” 2019)
Wiese et al. (“Quant GANs: deep generation of financial time series,” 2020)
Ziyin et al. (“What Data Augmentation Do We Need for Deep-Learning-Based Finance?” 2021)

**2.2.5 Scenarios based on flexible probabilities**
List of references:
Ardia and Meucci (“Stress testing in non-normal markets via entropy pooling,” 2015)
Ardia and Bluteau (“Stress-Testing With Parametric Models and Fully Flexible Probabilities,” 2017)
Meucci (“Fully Flexible Views: Theory and Practice,” 2008)
Meucci et al. (“Fully Flexible Extreme Views,” 2012)
Sebastian and Gebbie (“Systematic Asset Allocation using Flexible Views for South African Markets,” 2019)

**2.2.6 Scenarios based on Monte Carlo simulation**
List of references:
Chen and Chen ( _Monte-Carlo Simulation-Based Statistical Modeling_ , 2017)
Juan et al. (“A review of the role of heuristics in stochastic optimisation: from metaheuristics to learnheuristics,”
2022)
Lam and Li (“Parametric Scenario Optimization under Limited Data: A Distributionally Robust Optimization
View,” 2020)
Ledermann et al. (“Random orthogonal matrix simulation,” 2011)
Ledermann and Alexander (“Further properties of random orthogonal matrix simulation,” 2012)
Lee (“Stress testing Monte Carlo assumptions,” 2013)
Leon and Reveiz (“Monte Carlo Simulation of Long-Term Dependent Processes: A Primer,” 2012)
Schissler et al. (“Simulating High-Dimensional Multivariate Data using the bigsimr R Package,” 2021)
Silva and Ferreira (“Surrogate Monte Carlo,” 2021)
Staum (“Monte Carlo Computation in Finance,” 2009)
Yuan and Yuan (“A Monte Carlo synthetic sample based performance evaluation method for covariance matrix
estimators,” 2021)


```
Zhang (“Modern Monte Carlo methods for efficient uncertainty quantification and propagation: A survey,” 2020)
```
**2.2.7 Scenarios constructed using bootstrapping approach**
List of references:
Bertsimas and Van Parys (“Bootstrap Robust Prescriptive Analytics,” 2017)
Cavaliere et al. (“An Introduction to Bootstrap Theory in Time Series Econometrics,” 2020)
Cogneau and Zakamouline (“Block bootstrap methods and the choice of stocks for the long run,” 2013)
Davidson (“Diagnostics for the bootstrap and fast double bootstrap,” 2017)
El Karoui and Purdom (“Can we trust the bootstrap in high-dimensions? the case of linear models,” 2018)
Gilleland (“Bootstrap Methods for Statistical Inference. Part I: Comparative Forecast Verification for Continu-
ous Variables,” 2020)
Gilleland (“Bootstrap Methods for Statistical Inference. Part II: Extreme-Value Analysis,” 2020)
Goncalves and Perron (“Bootstrapping factor models with cross sectional dependence,” 2020)
Hambuckers and Heuchenne (“Estimating the Out-of-Sample Predictive Ability of Trading Rules: A Robust
Bootstrap Approach,” 2016)
Honore and Hu (“Poor (Wo)man’s Bootstrap,” 2017)
Horowitz (“Bootstrap methods in econometrics,” 2019)
Imbens and Menzel (“A causal bootstrap,” 2021)
Jaeger et al. (“Understanding machine learning for diversified portfolio construction by explainable AI,” 2020)
Kreiss and Paparoditis (“Bootstrap methods for dependent data: A review,” 2011)
Little and Badawy (“Causal bootstrapping,” 2020)
Page (“How to combine long and short return histories efficiently,” 2013)
Pathak and Rao (“The Sequential Bootstrap,” 2013)
Romano and Wolf (“Multiple Testing of One-Sided Hypotheses: Combining Bonferroni and the Bootstrap,”
2018)
Sani et al. (“The replacement bootstrap for dependent data,” 2015)
Tsamardinos et al. (“Bootstrapping the out-of-sample predictions for efficient and accurate cross-validation,”
2018)
Vinod (“Constructing Scenarios of Time Heterogeneous Series for Stress Testing,” 2012)
Wang and Tu (“Bootstrap methods: the classical theory and recent development,” 2014)
Xu et al. (“Applications of the Fractional-Random-Weight Bootstrap,” 2020)

**2.2.8 Scenarios constructed using resampling approach**
List of references:
Cerqueira et al. (“Evaluating time series forecasting models: an empirical study on performance estimation
methods,” 2020)
Chihara and Hesterberg ( _Mathematical Statistics with Resampling and R, 2nd Edition_ , 2018)
Dahl and Sorensen (“Time Series (re)sampling using Generative Adversarial Networks,” 2021)
Frahm (“A theoretical foundation of portfolio resampling,” 2015)
Hoffman (“Resampling Statistics,” 2015)
Huang and Yu (“A new procedure for resampled portfolio with shrinkaged covariance matrix,” 2020)
Mammen and Nandi (“Bootstrap and Resampling,” 2012)
Michaud and Michaud (“Estimation Error and Portfolio Optimization: A Resampling Solution,” 2015)
Oneto (“Resampling Methods,” 2019)
Sarris et al. (“Exploiting resampling techniques for model selection in forecasting: an empirical evaluation using
out-of-sample tests,” 2020)

**2.2.9 Scenarios based on similarities and discords within time series**
List of references:
Gharghabi et al. (“Matrix profile XII: mpdist: A novel time series distance measure to allow data mining in
more challenging scenarios,” 2018)
Gonzalez et al. (“Similarity Metrics for Transfer Learning in Financial Markets,” 2021)


Kang et al. (“Déjà vu: A data-centric forecasting approach through time series cross-similarity,” 2021)
Kegel et al. (“Feature-based comparison and generation of time series,” 2018)
Kegel et al. (“Generating What-If Scenarios for Time Series Data,” 2017)
Linardi et al. (“VALMOD: A suite for easy and exact detection of variable length motifs in data series,” 2018)
Mikalsen et al. (“Time Series Cluster Kernel for Learning Similarities between Multivariate Time Series with
Missing Data,” 2018)
Snow (“DataGene: A Framework for Dataset Similarity,” 2020)
Stephanovitch et al. (“Optimal 1-Wasserstein Distance for WGANs,” 2022)
Yeh et al. (“Time series joins, motifs, discords and shapelets: a unifying view that exploits the matrix profile,”
2017)
Yeh (“Towards a Near Universal Time Series Data Mining Tool: Introducing the Matrix Profile,” 2020)
Zhu et al. (“Time series chains: A novel tool for time series data mining,” 2018)
Zhu et al. (“Introducing time series chains: a new primitive for time series data mining,” 2019)

#### 2.2.10 Data augmentation and scenario generation using machine learning models

List of references:
Bandara et al. (“Improving the accuracy of global forecasting models using time series data augmentation,”
2021)
Bhattarai et al. (“Sampling Strategies for GAN Synthetic Data,” 2020)
Bond-Taylor et al. (“Deep Generative Modelling: A Comparative Review of VAEs, GANs, Normalizing Flows,
Energy-Based and Autoregressive Models,” 2022)
Chadebec and Allassonniere (“Data Augmentation with Variational Autoencoders and Manifold Sampling,”
2021)
Chalongvorachai and Woraratpanya (“A data generation framework for extremely rare case signals,” 2021)
Charte et al. (“A practical tutorial on autoencoders for nonlinear feature fusion: Taxonomy, models, software
and guidelines,” 2018)
Chen et al. (“An Empirical Survey of Data Augmentation for Limited Data Learning in NLP,” 2021)
Cao and Guo (“Generative Adversarial Network: Some Analytical Perspectives,” 2021)
Dahl and Sorensen (“Time Series (re)sampling using Generative Adversarial Networks,” 2021)
Debnath et al. (“Exploring Generative Data Augmentation in Multivariate Time Series Forecasting : Opportu-
nities and Challenges,” 2021)
De Meer et al. (“Tackling the exponential scaling of signature-based GANs for high-dimensional financial time
series generation,” 2021)
Dogariu et al. (“Towards Realistic Financial Time Series Generation via Generative Adversarial Learning,” 2021)
Dogariu et al. (“Generation of Realistic Synthetic Financial Time-Series,” 2021)
Eckerli and Osterrieder (“Generative Adversarial Networks in finance: an overview,” 2021)
Faez et al. (“Deep Graph Generators: A Survey,” 2020)
Fakoor et al. (“Fast, Accurate, and Simple Models for Tabular Data via Augmented Distillation,” 2020)
Fang and Lin (“Prior knowledge distillation based on financial time series,” 2020)
Fawaz et al. (“Data augmentation using synthetic data for time series classification with deep residual networks,”
2018)
Fons et al. (“Adaptive Weighting Scheme for Automatic Time-Series Data Augmentation,” 2021)
Fu et al. (“Data augmentation for time series,” 2020)
Goel et al. (“Model Patching: Closing the Subgroup Performance Gap with Data Augmentation,” 2020)
He et al. (“Data Augmentation Revisited: Rethinking the Distribution Gap between Clean and Augmented
Data,” 2019)
Hofert et al. (“Multivariate time-series modeling with generative neural networks,” 2021)
Hoffmann et al. (“Machine Learning in a data-limited regime: Augmenting experiments with synthetic data
uncovers order in crumpled sheets,” 2018)
Imokoyende (“Variational Autoencoder In Finance,” 2019)
Iwana and Uchida (“An empirical survey of data augmentation for time series classification with neural net-
works,” 2021)
Jabbar et al. (“A Survey on Generative Adversarial Networks: Variants, Applications, and Training,” 2020)


Javeri et al. (“Improving Neural Networks for Time-Series Forecasting using Data Augmentation and AutoML,”
2021)
Jiang et al. (“Deceive D: Adaptive Pseudo Augmentation for GAN Training with Limited Data,” 2021)
Jin and Rinard (“Towards Context-Agnostic Learning Using Synthetic Data,” 2021)
Kingma and Welling (“An introduction to variational autoencoders,” 2019)
Koesdwiady et al. (“Methods to Improve Multi-Step Time Series Prediction,” 2018)
Kong et al. (“Robust Optimization as Data Augmentation for Large-scale Graphs,” 2022)
Koochali et al. (“If You Like It, GAN It. Probabilistic Multivariate Times Series Forecast With GAN,” 2020)
Kuchnik and Smith (“Efficient Augmentation via Data Subsampling,” 2018)
Laskin et al. (“Reinforcement Learning with Augmented Data,” 2020)
Lawrence et al. (“Data Generating Process to Evaluate Causal Discovery Techniques for Time Series Data,”
2021)
Lezmi et al. (“Improving the Robustness of Trading Strategy Backtesting with Boltzmann Machines and Gen-
erative Adversarial Networks,” 2020)
Leznik et al. (“Multivariate Time Series Synthesis Using Generative Adversarial Networks,” 2021)
Li et al. (“Improving GAN with inverse cumulative distribution function for tabular data synthesis,” 2021)
Li et al. (“A Synthetic Regression Model for Large Portfolio Allocation,” 2022)
Lim et al. (“Noisy Feature Mixup,” 2021)
Liu et al. (“Efficient Time Series Augmentation Methods,” 2020)
Mannix and Cesa (“’Signatures’ promise quants a tool for all jobs,” 2021)
Ni et al. (“Conditional Sig-Wasserstein GANs for Time Series Generation,” 2020)
Padhi et al. (“Tabular Transformers for Modeling Multivariate Time Series,” 2021)
Pan et al. (“Data-Centric Engineering: integrating simulation, machine learning and statistics. Challenges and
Opportunities,” 2021)
Pei et al. (“Towards Generating Real-World Time Series Data,” 2021)
Perez et al. (“Data augmentation through multivariate scenario forecasting in Data Centers using Generative
Adversarial Networks,” 2022)
Raileanu et al. (“Automatic Data Augmentation for Generalization in Deep Reinforcement Learning,” 2021)
Rajabi and Garibay (“TabFairGAN: Fair Tabular Data Generation with Generative Adversarial Networks,”
2021)
Rocca and Rocca (“Intuitively Understanding Variational Autoencoders,” 2019)
Rosolia and Osterrieder (“Analyzing Deep Generated Financial Time Series for Various Asset Classes,” 2021)
Salazar et al. (“Generative Adversarial Networks and Markov Random Fields for oversampling very small training
sets,” 2021)
Saxena and Cao (“Generative Adversarial Networks (GANs),” 2022)
Saxena and Cao (“Generative Adversarial Networks (GANs): Challenges, Solutions, and Future Directions,”
2020)
Shah and Shroff (“Forecasting Market Prices using DL with Data Augmentation and Meta-learning: ARIMA
still wins!” 2021)
Shen et al. (“Towards Out-Of-Distribution Generalization: A Survey,” 2021)
Smith and Smith (“Conditional GAN for timeseries generation,” 2020)
Sun et al. (“Decision-Aware Conditional GANs for Time Series Data,” 2020)
Taylor and Nitschke (“Improving Deep Learning using Generic Data Augmentation,” 2017)
Tran et al. (“A Bayesian Data Augmentation Approach for Learning Deep Models,” 2017)
Vieira (“Generating Synthetic Sequential Data using GANs,” 2020)
Volpi et al. (“Generalizing to Unseen Domains via Adversarial Data Augmentation,” 2018)
Wang et al. (“Regularizing Deep Networks with Semantic Data Augmentation,” 2020)
Wang et al. (“Scalable Data Augmentation for Deep Learning,” 2019)
Wen et al. (“Time Series Data Augmentation for Deep Learning: A Survey,” 2021)
Xie et al. (“Unsupervised Data Augmentation,” 2019)
Yacoby et al. (“Characterizing and Avoiding Problematic Global Optima of Variational Autoencoders,” 2020)
Yao et al. (“Learning with Small Data,” 2020)
Ye and Dai (“Implementing transfer learning across different datasets for time series forecasting,” 2021)
Yoon et al. (“Time-series Generative Adversarial Networks,” 2019)


```
Xu et al. (“Unsupervised meta-learning for few-shot learning,” 2021)
Yu (“A Tutorial on VAEs: From Bayes’ Rule to Lossless Compression,” 2020)
Zhu et al. (“Pagan: Portfolio Analysis with Generative Adversarial Networks,” 2021)
```
#### 2.2.11 Scenarios for extreme events and stress testing

List of references:
Bhatia et al. (“ExGAN: Adversarial Generation of Extreme Samples,” 2021)
Chalongvorachai and Woraratpanya (“A data generation framework for extremely rare case signals,” 2021)
Diffenbaugh (“Verification of extreme event attribution: Using out-of-sample observations to assess changes in
probabilities of unprecedented events.,” 2020)
Ding et al. (“Modeling Extreme Events in Time Series Prediction,” 2019)
Engelke and Ivanovs (“Sparse Structures for Multivariate Extremes,” 2021)
Lerch et al. (“Forecaster’s Dilemma: Extreme Events and Forecast Evaluation,” 2017)
Naveau et al. (“Statistical methods for extreme event attribution in climate science,” 2020)
Qi and Majda (“Using machine learning to predict extreme events in complex systems.,” 2019)
Schwaab et al. (“Modeling Extreme Events: Time-Varying Extreme Tail Shape,” 2021)
Zhao (“Event Prediction in the Big Data Era,” 2022)

#### 2.2.12 Scenarios for extreme events and stress testing within context of QWIM.

List of references:
Al Janabi et al. (“Multivariate dependence and portfolio optimization algorithms under illiquid market scenar-
ios,” 2017)
Albanese et al. (“Reverse Stress Testing,” 2020)
Alokley and Albarrak (“Clustering of Extremes in Financial Returns: A Study of Developed and Emerging
Markets,” 2020)
Ardia and Meucci (“Stress testing in non-normal markets via entropy pooling,” 2015)
Ardia and Bluteau (“Stress-Testing With Parametric Models and Fully Flexible Probabilities,” 2017)
Arora et al. (“Extreme Yet Plausible: Choosing Scenarios to Stress Test Financial Institutions,” 2021)
Aste (“Stress testing and systemic risk measures using multivariate conditional probability,” 2021)
Baes and Schaanning (“Reverse Stress Testing: Scenario Design for Macroprudential Stress Tests,” 2020)
Breuer and Summer (“Systematic stress tests on public data,” 2020)
Bianchi et al. ( _Handbook of Heavy-Tailed Distributions in Asset Management and Risk Management_ , 2019)
Bilgili et al. (“Stress Hedging in Portfolio Construction,” 2017)
Boubaker and Nguyen ( _Handbook of Global Financial Markets_ , 2019)
Chalkis et al. (“Modeling of crisis periods in stock markets,” 2021)
Chen and Nasekin (“Quantifying systemic risk with factor copulas,” 2020)
Cohort et al. (“Analytical scores for stress scenarios,” 2020)
Denev and Mutnikas (“A Formalized, Integrated and Visual Approach to Stress Testing,” 2016)
Engle (“Stress Testing with Market Data,” 2020)
Flood and Korenko (“Systematic scenario selection: stress testing and the nature of uncertainty,” 2015)
Gao et al. (“Efficient Simulation of Financial Stress Testing Scenarios with Suppes-Bayes Causal Networks,”
2017)
Gao et al. (“Causal data science for financial stress testing,” 2018)
Glasserman et al. (“Stress scenario selection by empirical likelihood,” 2015)
Grundke (“Further recipes for quantitative reverse stress testing,” 2012)
Kantos and diBartolomeo (“How the pandemic taught us to turn smart beta into real alpha,” 2020)
Kopeliovich et al. (“Robust Risk Estimation and Hedging: A Reverse Stress Testing Approach,” 2015)
Meucci ( _A Fully Integrated Liquidity and Market Risk Model_ , 2012)
Pesenti et al. (“Scenario weights for importance measurement (SWIM) - an R package for sensitivity analysis,”
2020)
Pesenti et al. (“Reverse sensitivity testing: What does it take to break the model?” 2019)
Rebonato (“The quickest way to lose the money you cannot afford to lose: reverse stress testing with maximum
entropy,” 2018)


Rojas and Dias (“Stress testing network reconstruction via graphical causal model,” 2021)
Rosen and Saunders (“Regress under stress: A simple least-squares method for integrating economic scenarios
with risk simulations,” 2016)
Ruenzi et al. (“Joint Extreme events in equity returns and liquidity and their cross-sectional pricing implications,”
2020)
Schwaab et al. (“Modeling Extreme Events: Time-Varying Extreme Tail Shape,” 2021)
Seabrook et al. (“An Information Filtering approach to stress testing: an application to FTSE markets,” 2021)
Siddique et al. ( _Stress Testing (Second Edition)_ , 2019)
Skoglund (“Quantification of model risk in stress testing and scenario analysis,” 2019)
Tanaka (“Forecasting scenarios from the perspective of a reverse stress test using second-order cone program-
ming,” 2017)
Traccucci et al. (“A Triptych Approach for Reverse Stress Testing of Complex Portfolios,” 2019)
Wang et al. (“Forecasting stock volatility in the presence of extreme shocks: Short-term and long-term effects,”
2020)
Zorn (“Panic-aware portfolio optimization,” 2019)

#### 2.2.13 Economic scenario generators.

List of references:
Barra Montevechi et al. (“A simulation-based approach to perform economic evaluation scenarios,” 2017)
Cheng and Planchet (“Stochastic Deflator for an Economic Scenario Generator with Five Factors,” 2018)
Chen et al. (“Personalised drawdown strategies and partial annuitisation to mitigate longevity risk,” 2021)
Chen et al. (“Using a stochastic economic scenario generator to analyse uncertain superannuation and retirement
outcomes,” 2021)
Czasonis et al. (“Enhanced Scenario Analysis,” 2020)
De Meo (“Scenario Design for Macro-Financial Stress Testing,” 2019)
Facchinato and Pola (“Managing uncertainty with diversification across macroeconomic scenarios (DAMS): from
asset segmentation to portfolio,” 2014)
Flaig and Junike (“Scenario generation for market risk models using generative neural networks,” 2022)
Golub et al. (“Market-Driven Scenarios: An Approach for Plausible Scenario Construction,” 2018)
Haldane and Turrell (“Drawing on different disciplines: macroeconomic agent-based models,” 2018)
Lee et al. (“How can an economic scenario generation model cope with abrupt changes in financial markets?”
2021)
Moudiki and Planchet (“Economic Scenario Generators,” 2016)
Ortec Finance (“Ex ante risk management with scenarios,” 2014)
Rosen (“Integrating Economic Scenarios with Advanced Scenario Analytics to Manage Investment Portfolios,”
2015)
Rosen (“Re-Thinking Scenarios: Stress Testing of Multi-Asset Portfolios by Integrating Economic Scenarios
with Advanced Simulation Analytics,” 2015)
Rosen and Saunders (“Regress Under Stress: A Simple Least-Squares Method for Integrating Economic Scenarios
with Risk Simulations,” 2015)
Rosen and Saunders (“Regress under stress: A simple least-squares method for integrating economic scenarios
with risk simulations,” 2016)
Schneider (“Sparse economic scenarios,” 2020)
Sharma et al. (“V- U-, L- or W- shaped economic recovery after Covid-19: Insights from an Agent Based Model,”
2021)
Siew et al. (“The Impact of Different Economic Scenarios Towards Portfolio Selection in Enhanced Index Tracking
Problem,” 2015)
Steehouwer (“Ex-ante risk management with scenarios,” 2014)
Steehouwer and Slater (“Macroeconomic Scenarios: A Frequency Domain Approach,” 2010)
Trimborn et al. (“SABCEMM: A Simulator for Agent-Based Computational Economic Market Models,” 2020)
van Beek (“Consistent Calibration of Economic Scenario Generators: The Case for Conditional Simulation,”
2020)
Wang (“Discriminating modelling approaches for Point in Time Economic Scenario Generation,” 2021)


```
Zhang (“Optimal Retirement Planning: Scenario Generation, Preferences, and Objectives,” 2018)
```
#### 2.2.14 Scenarios incorporating dependencies (correlations, covariances, copulas).

List of references:
Alexander and Ledermann (“ROM Simulation: Applications to Stress Testing and VaR,” 2012)
Amengual and Sentana (“Is a Normal Copula the Right Copula?” 2020)
Benali et al. (“MTCopula: Synthetic Complex Data Generation Using Copula,” 2021)
Carrillo et al. (“A New Machine Learning Forecasting Algorithm Based on Bivariate Copula Functions,” 2021)
Czado and Nagler (“Vine Copula Based Modeling,” 2022)
Fritzsch et al. (“Marginals Versus Copulas: Which Account For More Model Risk In Multivariate Risk Fore-
casting?” 2021)
Fulle and Herwartz (“A Multivariate Markov-Switching GARCH Model with Copula-Distributed Innovations,”
2021)
Galeeva et al. (“Measuring correlation risk for Energy Derivatives,” 2012)
Großer and Okhrin (“Copulae: An overview and recent developments,” 2021)
Harutyunyan et al. (“Efficient Covariance Estimation from Temporal Data,” 2021)
Janke et al. (“Implicit Generative Copulas,” 2021)
Ledermann and Alexander (“Further properties of random orthogonal matrix simulation,” 2012)
Ledoit and Wolf (“Shrinkage estimation of large covariance matrices: Keep it simple, statistician?” 2021)
Li et al. (“SynC: A Copula based Framework for Generating Synthetic Data from Aggregated Sources,” 2020)
Lu and Ghosh (“Nonparametric estimation of multivariate copula using empirical bayes method,” 2021)
Ma (“copent: Estimating Copula Entropy and Transfer Entropy in R,” 2021)
Marti et al. (“Exploring and measuring non-linear correlations: Copulas, Lightspeed Transportation and Clus-
tering,” 2017)
Marti (“CORRGAN: sampling realistic financial correlation matrices using generative adversarial networks,”
2020)
Marti et al. (“cCorrGAN: Conditional Correlation GAN for Learning Empirical Conditional Distributions in the
Elliptope,” 2021)
Marti et al. (“A review of two decades of correlations, hierarchies, networks and clustering in financial markets,”
2021)
Meyer and Nagler (“Synthia: multidimensional synthetic data generation in Python,” 2021)
Nasri and Rémillard (“Copula-based dynamic models for multivariate time series,” 2019)
Nasri et al. (“Goodness-of-fit for regime-switching copula models with application to option pricing,” 2020)
Opdyke (“Full Probabilistic Control for Direct and Robust, Generalized and Targeted Stressing of the Correlation
Matrix (Even When Eigenvalues are Empirically Challenging,” 2020)
Packham and Woebbeking (“Correlation scenarios and correlation stress testing,” 2021)
Papenbrock et al. (“Matrix Evolutions: Synthetic Correlations and Explainable Machine Learning for Con-
structing Robust Investment Portfolios,” 2021)
Sahamkhadam and Stephan (“Portfolio Optimization Based on Forecasting Models Using Vine Copulas: An
Empirical Assessment for the Financial Crisis,” 2021)
Tan and Zohren (“Large Non-Stationary Noisy Covariance Matrices: A Cross-Validation Approach,” 2021)
Traccucci et al. (“A Triptych Approach for Reverse Stress Testing of Complex Portfolios,” 2019)
Trucı́os et al. (“Forecasting Conditional Covariance Matrices in High-Dimensional Time Series: a General Dy-
namic Factor Approach,” 2021)
Tsanakas and Zhu (“Copula model selection using image recognition,” 2021)
Waller (“Generating Correlation Matrices With Specified Eigenvalues Using the Method of Alternating Projec-
tions,” 2020)
Yu et al. (“Adjusting covariance matrix for risk management,” 2020)
Yuan and Yuan (“A Monte Carlo synthetic sample based performance evaluation method for covariance matrix
estimators,” 2021)


#### 2.2.15 Extreme events and scenarios.

References:
Asch et al. (“Model-assisted deep learning of rare extreme events from partial observations,” 2022)
Bhatia et al. (“ExGAN: Adversarial Generation of Extreme Samples,” 2021)
Buczak et al. (“Crystal Cube: Forecasting Disruptive Events,” 2022)
Chevalier et al. (“Modeling Nonstationary Extreme Dependence With Stationary Max-Stable Processes and
Multidimensional Scaling,” 2021)
Diffenbaugh (“Verification of extreme event attribution: Using out-of-sample observations to assess changes in
probabilities of unprecedented events.,” 2020)
Ding et al. (“Modeling Extreme Events in Time Series Prediction,” 2019)
Faggini et al. (“Crises in economic complex networks: Black Swans or Dragon Kings?” 2019)
Lerch et al. (“Forecaster’s Dilemma: Extreme Events and Forecast Evaluation,” 2017)
Medina et al. (“Spectral learning of multivariate extremes,” 2021)
Naveau et al. (“Statistical methods for extreme event attribution in climate science,” 2020)
Qi and Majda (“Using machine learning to predict extreme events in complex systems.,” 2019)
Racca and Magri (“Statistical prediction of extreme events from small datasets,” 2022)
Yılmaz et al. (“Comparison of different estimation methods for extreme value distribution,” 2021)

#### 2.2.16 Extreme events and scenarios within context of QWIM

References:
Cai et al. (“New volatility evolution model after extreme events,” 2022)
De Luca and Zuccolotto (“A double clustering algorithm for financial time series based on extreme events,”
2016)
Elkamhi and Stefanova (“Dynamic Hedging and Extreme Asset Co-movements,” 2015)
Kapoor and Shrivastava (“Extreme Values Theory and Return Level Analysis for Catastrophe Prediction,” 2014)
Kemp ( _Extreme Events: Robust Portfolio Construction in the Presence of Fat Tails_ , 2014)
Lezmi et al. (“Portfolio Allocation with Skewness Risk: A Practical Guide,” 2019)
Ruenzi et al. (“Joint Extreme events in equity returns and liquidity and their cross-sectional pricing implications,”
2020)
Sapp (“Efficient Estimation of Distributional Tail Shape and the Extremal Index with Applications to Risk
Management,” 2017)
Zorn (“Panic-aware portfolio optimization,” 2019)

#### 2.2.17 Scenarios based on agent-based modeliing

List of references:
Bai et al. (“Efficient Calibration of Multi-Agent Market Simulators from Time Series with Bayesian Optimiza-
tion,” 2021)
Beikirch et al. (“Robust Mathematical Formulation and Probabilistic Description of Agent-Based Computational
Economic Market Models,” 2021)
Chabi-Yo and Loudis (“A Decomposition of Conditional Risk Premia and Implications for Representative Agent
Models,” 2021)
Clark et al. (“Test case generation for agent-based models: A systematic literature review,” 2021)
De Gennaro Aquino et al. (“Portfolio Selection With Exploration of New Investment Opportunities,” 2021)
Foramitti (“AgentPy: A package for agent-based modeling in Python,” 2021)
Esmaeili et al. (“HAMLET: A Hierarchical Agent-based Machine Learning Platform,” 2021)
Harwick (“Helipad: A Framework for Agent-Based Modeling in Python,” 2021)
Istrate (“Models we Can Trust: Toward a Systematic Discipline of (Agent-Based) Model Interpretation and
Validation,” 2021)
Jericevich et al. (“Calibrating an adaptive Farmer-Joshi agent-based model for financial markets,” 2021)
Karaś and Serwatka (“Strong-hand conjecture: agent-based numerical simulation,” 2021)
Lindner et al. (“Learning What To Do by Simulating the Past,” 2021)
Lux (“Can heterogeneous agent models explain the alleged mispricing of the S&P 500?” 2021)


Niemann et al. (“Data-driven model reduction of agent-based systems using the Koopman generator,” 2021)
Papoudakis et al. (“Agent Modelling under Partial Observability for Deep Reinforcement Learning,” 2021)
Perumal and van Zyl (“Surrogate Assisted Methods for the Parameterisation of Agent-Based Models,” 2020)
Sharma et al. (“A constraint-satisfaction agent-based model for the macroeconomy,” 2020)
Shi et al. (“Pyramid scheme in stock market: a kind of financial market simulation,” 2021)
Schuderer et al. (“Sim-Env: Decoupling OpenAI Gym Environments from Simulation Models,” 2021)
Sharma et al. (“V- U-, L- or W- shaped economic recovery after Covid-19: Insights from an Agent Based Model,”
2021)
ter Ellen et al. (“Comparing behavioural heterogeneity across asset classes,” 2021)
Thiem et al. (“Global and Local Reduced Models for Interacting, Heterogeneous Agents,” 2021)
Vandin et al. (“Automated and Distributed Statistical Analysis of Economic Agent-Based Models,” 2021)
Westphal and Sornette (“How Market Intervention Can Prevent Bubbles and Crashes,” 2020)

#### 2.2.18 Validating scenarios and augmented datasets

List of references:
Alaa et al. (“How Faithful is your Synthetic Data? Sample-level Metrics for Evaluating and Auditing Generative
Models,” 2022)
Bahrpeyma et al. (“A Methodology for Validating Diversity in Synthetic Time Series Generation,” 2021)
Cramer et al. (“Validation Methods for Energy Time Series Scenarios from Deep Generative Models,” 2021)
De Meer et al. (“Tackling the exponential scaling of signature-based GANs for high-dimensional financial time
series generation,” 2021)
Ding et al. (“Modeling Extreme Events in Time Series Prediction,” 2019)
Franco-Pedroso et al. (“The ETS challenges: a machine learning approach to the evaluation of simulated financial
time series for improving generation processes,” 2019)
Franco-Pedroso et al. (“Generating Virtual Scenarios of Multivariate Financial Data for Quantitative Trading
Applications,” 2019)
Istrate (“Models we Can Trust: Toward a Systematic Discipline of (Agent-Based) Model Interpretation and
Validation,” 2021)
Lawrence et al. (“Data Generating Process to Evaluate Causal Discovery Techniques for Time Series Data,”
2021)
Ni et al. (“Conditional Sig-Wasserstein GANs for Time Series Generation,” 2020)
Snow (“DataGene: A Framework for Dataset Similarity,” 2020)

#### 2.2.19 Software implementations and frameworks.

List of references:
Foramitti (“AgentPy: A package for agent-based modeling in Python,” 2021)
Esmaeili et al. (“HAMLET: A Hierarchical Agent-based Machine Learning Platform,” 2021)
Harwick (“Helipad: A Framework for Agent-Based Modeling in Python,” 2021)
Hu et al. (“Multiple Imputation and Synthetic Data Generation with the R package NPBayesImputeCat,” 2021)
Jiang et al. (“A set of efficient methods to generate high-dimensional binary data with specified correlation
structures,” 2021)
Kang et al. (“GRATIS: GeneRAting TIme Series with diverse and controllable characteristics,” 2020)
Li et al. (“SynC: A Copula based Framework for Generating Synthetic Data from Aggregated Sources,” 2020)
Lin et al. (“Generating High-fidelity, Synthetic Time Series Datasets with DoppelGANger,” 2019)
Meyer and Nagler (“Synthia: multidimensional synthetic data generation in Python,” 2021)
Pesenti et al. (“Scenario weights for importance measurement (SWIM) - an R package for sensitivity analysis,”
2020)
Siebert et al. (“A systematic review of Python packages for time series analysis,” 2021)
Snow (“DeltaPy: A Framework for Tabular Data Augmentation in Python,” 2020)
Tadayon and Pottie (“tsBNgen: A Python Library to Generate Time Series Data from an Arbitrary Dynamic
Bayesian Network Structure,” 2020)
Vinod (“Constructing Scenarios of Time Heterogeneous Series for Stress Testing,” 2012)
Vinod (“R Package GeneralCorr Functions for Portfolio Choice,” 2021)


Wang et al. (“VEGA: Towards an End-to-End Configurable AutoML Pipeline,” 2020)


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
1) literature review
2) decide on the appropriate metrics and quantitative methods within context of "good enough" for the project
3) write-up summary of literature review: methods, metrics, testing procedures
4) identification of Python and/or R packages which are most appropriate for the selected methods and metrics
5) code design to decide on main code components
6) implementation of code components
7) interactive visualization of numerical results
8) project report containing description of methods, metrics, and tests, and analysis of results.

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
1) methods
2) metrics to assess the performance/robustness of the methods
3) testing procedures
4) numerical results
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
1) visual display of major components of the coding framework
2) UML diagrams for each of the components.
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
1) visual display of major components of the coding framework
2) UML diagrams for each of the components.
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
local remote
```
```
Trainer
Algorithms Auto-ML
```
```
Model Manager
ModelsModelModel Decision GeneratorsModelModel
```
```
Model Interpreter
```
```
Decision Generator
Order executi...
```
```
Execution Results
```
```
Execution Env
VWAP/Close/......Sub-workfl...
```
```
Highly Customiz...
Module in devel...
```
```
Explanation
```
```
Sub-workflow(1) (E.g. High-frequ...
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
Source:Machine Learning in Asset Management^27


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
HFRIFWI HFRI Fund Weighted Composite Index RUMCINTR iShares Russell Mid-Cap ETF
LBUSTRUU Bloomberg Barclays US Aggregate Bond
Index
```
```
RUMRINTR iShares Micro-Cap ETF
LG30TRUU Bloomberg Barclays Global High Yield
Total Return Index Value Unhedge
```
```
RUTPINTR iShares Russell Top 200 ETF
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

NDDUUS MSCI Daily Total Return Net USA USD
Index
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

Al Janabi, M. A. M., Arreola Hernandez, J., Berger, T., and Nguyen, D. K. (2017).“Multivariate dependence and
portfolio optimization algorithms under illiquid market scenarios.” In: _European Journal of Operational Research_
259(3), pp. 1121–1131.
Alaa, A., Van Breugel, B., Saveliev, E. S., and van der Schaar, M. (2022).“How Faithful is your Synthetic Data?
Sample-level Metrics for Evaluating and Auditing Generative Models.” In: _Proceedings of the 39th International
Conference on Machine Learning_. Ed. by K. Chaudhuri, S. Jegelka, L. Song, C. Szepesvari, G. Niu, and S.
Sabato. Vol. 162. Proceedings of Machine Learning Research. PMLR, pp. 290–306.
Albanese, C., Crepey, S., and Iabichino, S. (2020).“Reverse Stress Testing.” In: _SSRN e-Print_.
Alexander, C. and Ledermann, D. (2012).“ROM Simulation: Applications to Stress Testing and VaR.” In: _SSRN
e-Print_.
Alokley, S. A. and Albarrak, M. S. (2020).“Clustering of Extremes in Financial Returns: A Study of Developed
and Emerging Markets.” In: _Journal of Risk and Financial Management_ 13(7), p. 141.
Amengual, D. and Sentana, E. (2020).“Is a Normal Copula the Right Copula?” In: _Journal of Business & Economic
Statistics_ 38(2), pp. 350–366.
Ardia, D. and Bluteau, K. (2017).“Stress-Testing With Parametric Models and Fully Flexible Probabilities.” In:
_Wilmott_ 2017(87), pp. 52–55.
Ardia, D., Boudt, K., and Gagnon-Fleury, J.-P. (2017).“RiskPortfolios: Computation of Risk-Based Portfolios in
R.” In: _The Journal of Open Source Software_ 2(10), pp. 171+.
Ardia, D. and Meucci, A. (2015).“Stress testing in non-normal markets via entropy pooling.” In: _Risk_.
Arora, R., Gao, R., and Tompaidis, S. (2021).“Extreme Yet Plausible: Choosing Scenarios to Stress Test Financial
Institutions.” In: _SSRN e-Print_.
Asch, A., Brady, E., Gallardo, H., Hood, J., Chu, B., and Farazmand, M. (2022). “Model-assisted deep learning of
rare extreme events from partial observations.” In: _arXiv e-Print_.
Assefa, S., Dervovic, D., Mahfouz, M., Balch, T., Reddy, P., and Veloso, M. (2019).“Generating Synthetic Data in
Finance: Opportunities, Challenges and Pitfalls.” In: _NeurIPS’19 Workshop on Robust AI in Financial Services_.
Aste, T. (2021).“Stress testing and systemic risk measures using multivariate conditional probability.” In: _arXiv
e-Print_.
Bacon, C. R. (2019).“Performance Attribution: History and Progress.” In: _CFA Institute Research Foundation
Publications_.
Baes, M. and Schaanning, E. (2020).“Reverse Stress Testing: Scenario Design for Macroprudential Stress Tests.”
In: _SSRN e-Print_.
Bahrpeyma, F., Roantree, M., Cappellari, P., Scriney, M., and McCarren, A. (2021).“A Methodology for Validating
Diversity in Synthetic Time Series Generation.” In: _MethodsX_ 8, p. 101459.
Bai, Y., Lam, H., Vyetrenko, S., and Balch, T. (2021). “Efficient Calibration of Multi-Agent Market Simulators
from Time Series with Bayesian Optimization.” In: _arXiv e-Print_.
Bandara, K., Hewamalage, H., Liu, Y.-H., Kang, Y., and Bergmeir, C. (2021).“Improving the accuracy of global
forecasting models using time series data augmentation.” In: _Pattern Recognition_ 120, p. 108148.
Barra Montevechi, J. A., Silva Costa, R. F. da, Pinho, A. F. de, and Carvalho Miranda, R. de (2017).“A simulation-
based approach to perform economic evaluation scenarios.” In: _Journal of Simulation_ 11(2), pp. 185–192.
Bass, R., Gallagher, K., Ratcliffe, R., and Shah, S. (2018).“Factor Performance Across Market-Driven Scenarios.”
In: _SSRN e-Print_.
Beikirch, M., Cramer, S., Frank, M., Otte, P., Pabich, E., and Trimborn, T. (2021).“Robust Mathematical For-
mulation and Probabilistic Description of Agent-Based Computational Economic Market Models.” In: _arXiv
e-Print_.
Benali, F., Bodenes, D., Labroche, N., and de Runz, C. (2021).“MTCopula: Synthetic Complex Data Generation
Using Copula.” In: _HAL Archives Ouvertes_.
Bertsimas, D. and Van Parys, B. (2017).“Bootstrap Robust Prescriptive Analytics.” In: _arXiv e-Print_.
Bhatia, S., Jain, A., and Hooi, B. (2021).“ExGAN: Adversarial Generation of Extreme Samples.” In: _arXiv e-Print_.
Bhattarai, B., Baek, S., Bodur, R., and Kim, T.-K. (2020).“Sampling Strategies for GAN Synthetic Data.” In:
_ICASSP 2020 - 2020 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)_.
Bianchi, M. L., Stoyanov, S. V., Tassinari, G. L., Fabozzi, F. J., and Focardi, S. M. (2019). _Handbook of Heavy-Tailed
Distributions in Asset Management and Risk Management_. World Scientific. 600 pp.


Bilgili, M. S., Ferconi, M., and Ulitsky, A. (2017).“Stress Hedging in Portfolio Construction.” In: _Risk_.
Boileau, P., Hejazi, N., Collica, B., Laan, M. van der, and Dudoit, S. (2021).“cvCovEst: Cross-validated covariance
matrix estimator selection and evaluation in R.” In: _Journal of Open Source Software_ 6(63), p. 3273.
Bolger, F. and Wright, G. (2017).“Use of expert knowledge to anticipate the future: Issues, analysis and directions.”
In: _International Journal of Forecasting_ 33(1), pp. 230–243.
Bond-Taylor, S., Leach, A., Long, Y., and Willcocks, C. G. (2022). “Deep Generative Modelling: A Comparative
Review of VAEs, GANs, Normalizing Flows, Energy-Based and Autoregressive Models.” In: _arXiv e-Print_.
Boubaker, S. and Nguyen, D. K. (2019). _Handbook of Global Financial Markets_. World Scientific. 828 pp.
Breuer, T. and Summer, M. (2020).“Systematic stress tests on public data.” In: _Journal of Banking & Finance_ 118,
pp. 105886+.
Brugiere, P. (2020). _Quantitative Portfolio Management with Applications in Python_. Springer International Pub-
lishing. 189 pp.
Bryzgalova, S., Pelger, M., and Zhu, J. (2021).“Forest Through the Trees: Building Cross-Sections of Stock Returns.”
In: _SSRN e-Print_.
Buczak, A. L., Baugher, B. D., Martin, C. S., Keiley-Listermann, M. W., Howard, J., Parrish, N. H., Stalick, A. Q.,
Berman, D. S., and Dredze, M. H. (2022).“Crystal Cube: Forecasting Disruptive Events.” In: _Applied Artificial
Intelligence_ 36(1) (2001179), pp. 1–24.
Buehler, H., Gonon, L., Teichmann, J., and Wood, B. (2019).“Deep hedging.” In: _Quantitative Finance_ 19 (8),
pp. 1271–1291.
Buehler, H., Horvath, B., Lyons, T., Arribas, I. P., and Wood, B. (2020).“A Data-driven Market Simulator for
Small Data Environments.” In: _arXiv e-Print_.
Buehler, H., Horvath, B., Lyons, T., Arribas, I. P., and Wood, B. (2021).“Generating financial markets with
signatures.” In: _Risk_.
Cai, M.-L., Chen, Z.-H., Li, S.-P., Xiong, X., Zhang, W., Yang, M.-Y., and Ren, F. (2022).“New volatility evolution
model after extreme events.” In: _arXiv e-Print_.
Cajas, D. (2021a).“Entropic Portfolio Optimization: a Disciplined Convex Programming Framework.” In: _SSRN
e-Print_.
Cajas, D. (2021b).“OWA Portfolio Optimization: a Disciplined Convex Programming Framework.” In: _SSRN e-
Print_.
Cao, H. and Guo, X. (2021).“Generative Adversarial Network: Some Analytical Perspectives.” In: _arXiv e-Print_.
Carrillo, J. A., Nieto, M., Velez, J. F., and Velez, D. (2021).“A New Machine Learning Forecasting Algorithm
Based on Bivariate Copula Functions.” In: _Forecasting_ 3(2), pp. 355–376.
Cavaliere, G., Nielsen, H. B., and Rahbek, A. (2020).“An Introduction to Bootstrap Theory in Time Series Econo-
metrics.” In: _SSRN e-Print_.
Cerqueira, V., Torgo, L., and Mozetič, I. (2020).“Evaluating time series forecasting models: an empirical study on
performance estimation methods.” In: _Machine Learning_ 109, pp. 1997–2028.
Chabi-Yo, F. and Loudis, J. (2021).“A Decomposition of Conditional Risk Premia and Implications for Represen-
tative Agent Models.” In: _SSRN e-Print_.
Chadebec, C. and Allassonniere, S. (2021). “Data Augmentation with Variational Autoencoders and Manifold
Sampling.” In: _arXiv e-Print_.
Chalkis, A., Christoforou, E., Dalamagkas, T., and Emiris, I. Z. (2021).“Modeling of crisis periods in stock markets.”
In: _arXiv e-Print_.
Chalongvorachai, T. and Woraratpanya, K. (2021).“A data generation framework for extremely rare case signals.”
In: _Helyon_ 7(8), e07687.
Charte, D., Charte, F., Garcia, S., Jesus, M. J. del, and Herrera, F. (2018).“A practical tutorial on autoencoders
for nonlinear feature fusion: Taxonomy, models, software and guidelines.” In: _Information Fusion_ 44, pp. 78–96.
Chen, A. Y. and Zimmermann, T. (2022).“Open Source Cross-Sectional Asset Pricing.” In: _American Finance
Association Annual Meeting_.
Chen, C. Y.-H. and Nasekin, S. (2020).“Quantifying systemic risk with factor copulas.” In: _The European Journal
of Finance_ 26(18), pp. 1926–1947.
Chen, D.-G. and Chen, J. D. (2017). _Monte-Carlo Simulation-Based Statistical Modeling_. Ed. by D.-G. Chen and
J. D. Chen. ICSA book series in statistics. Singapore: Springer Singapore. 424 pp.
Chen, J., Tam, D., Raffel, C., Bansal, M., and Yang, D. (2021a).“An Empirical Survey of Data Augmentation for
Limited Data Learning in NLP.” In: _arXiv e-Print_.


Chen, W., Koo, B., Wang, Y., O’Hare, C., Langrené, N., Toscas, P., and Zhu, Z. (2021b).“Using a stochastic eco-
nomic scenario generator to analyse uncertain superannuation and retirement outcomes.” In: _Annals of Actuarial
Science_.
Chen, W., Minney, A., Toscas, P., Koo, B., Zhu, Z., and Pantelous, A. A. (2021c).“Personalised drawdown strategies
and partial annuitisation to mitigate longevity risk.” In: _Finance Research Letters_ 39 (101644).
Cheng, P.-K. and Planchet, F. (2018).“Stochastic Deflator for an Economic Scenario Generator with Five Factors.”
In: _arXiv e-Print_.
Chevalier, C., Martius, O., and Ginsbourger, D. (2021).“Modeling Nonstationary Extreme Dependence With Sta-
tionary Max-Stable Processes and Multidimensional Scaling.” In: _Journal of Computational and Graphical Statis-
tics_.
Chib, S. (2020). _R package czfactor_. Tech. rep. Washington University.
Chib, S. and Zhao, L. (2020). _R package czzg_. Tech. rep. Washington University.
Chihara, L. M. and Hesterberg, T. C. (2018). _Mathematical Statistics with Resampling and R, 2nd Edition_. Wiley.
560 pp.
Clark, A. G., Walkinshaw, N., and Hierons, R. M. (2021).“Test case generation for agent-based models: A systematic
literature review.” In: _arXiv e-Print_.
Cogneau, P. and Zakamouline, V. (2013).“Block bootstrap methods and the choice of stocks for the long run.” In:
_Quantitative Finance_ 13(9), pp. 1443–1457.
Cohort, P., Corbetta, J., and Laachir, I. (2020).“Analytical scores for stress scenarios.” In: _arXiv e-Print_.
Coletta, A., Prata, M., Conti, M., Mercanti, E., Bartolini, N., Moulin, A., Vyetrenko, S., and Balch, T. (2021).
“Towards Realistic Market Simulations: a Generative Adversarial Networks Approach.” In: _arXiv e-Print_.
Colson, A. R. and Cooke, R. M. (2017).“Cross validation for the classical model of structured expert judgment.”
In: _Reliability Engineering and System Safety_ 163, pp. 109–120.
Coqueret, G. (2022). _Perspectives in sustainable equity investing (website version)_.
Coqueret, G. and Guida, T. (2020). _Machine Learning for Factor Investing: R Version_. Chapman and Hall/CRC.
341 pp.
Cramer, E., Gorjao, L. R., Mitsos, A., Schafer, B., Witthaut, D., and Dahmen, M. (2021). “Validation Methods for
Energy Time Series Scenarios from Deep Generative Models.” In: _arXiv e-Print_.
Cubuk, E. D., Zoph, B., Shlens, J., and Le, Q. V. (2019).“RandAugment: Practical data augmentation with no
separate search.” In: _arXiv e-Print_.
Czado, C. and Nagler, T. (2022).“Vine Copula Based Modeling.” In: _Annual Review of Statistics and Its Application_
9(1).
Czasonis, M., Kritzman, M., Pamir, B., and Turkington, D. (2020).“Enhanced Scenario Analysis.” In: _The Journal
of Portfolio Management_ 46(4), pp. 69–79.
Czasonis, M., Kritzman, M., and Turkington, D. (2021).“Relevance.” In: _SSRN e-Print_.
Da Silva, B. and Shi, S. S. (2019).“Towards Improved Generalization in Financial Markets with Synthetic Data
Generation.” In: _arXiv e-Print_.
Dahl, C. M. and Sorensen, E. N. (2021).“Time Series (re)sampling using Generative Adversarial Networks.” In:
_arXiv e-Print_.
Davidson, R. (2017).“Diagnostics for the bootstrap and fast double bootstrap.” In: _Econometric Reviews_ 36(6-9),
pp. 1021–1038.
Davis, M. and Lleo, S. (2015).“Behaviouralizing Black-Litterman: Expert Opinions and Behavioural Biases in a
Diffusion Setting.” In: _SSRN e-Print_.
Davis, M. H. A. and Lleo, S. (2016).“A Simple Procedure for Combining Expert Opinion with Statistical Estimates
to Achieve Superior Portfolio Performance.” In: _The Journal of Portfolio Management_ 42(4), pp. 49–58.
de Carvalho, M. and Rua, A. (2017).“Real-time nowcasting the US output gap: Singular spectrum analysis at
work .” In: _International Journal of Forecasting_ 33(1), pp. 185–198.
De Gennaro Aquino, L., Sornette, D., and Strub, M. S. (2021).“Portfolio Selection With Exploration of New
Investment Opportunities.” In: _SSRN e-Print_.
De Luca, G. and Zuccolotto, P. (2016).“A double clustering algorithm for financial time series based on extreme
events .” In: _Statistics and Risk Modeling_ 0(0).
De Meer, F., Schwendner, P., and Wunsch, M. (2021).“Tackling the exponential scaling of signature-based GANs
for high-dimensional financial time series generation.” In: _SSRN e-Print_.


De Meer Pardo, F. (2019).“Enriching Financial Datasets with Generative Adversarial Networks.” MA thesis. Delft
University of Technology.
De Meer Pardo, F. and Lopez, R. C. (2020).“Mitigating Overfitting on Financial Datasets with Generative Adver-
sarial Networks.” In: _The Journal of Financial Data Science_ 2 (1), pp. 76–85.
De Meo, E. (2019).“Scenario Design for Macro-Financial Stress Testing.” In: _SSRN e-Print_.
de Miranda Cardoso, J. V., Ying, J., and Palomar, D. P. (2020). “Algorithms for Learning Graphs in Financial
Markets.” In: _arXiv e-Print_.
Debnath, A., Waghmare, G., Wadhwa, H., Asthana, S., and Arora, A. (2021).“Exploring Generative Data Aug-
mentation in Multivariate Time Series Forecasting : Opportunities and Challenges.” In: _MiLeTS’21: 7th KDD
Workshop on Mining and Learning from Time Series_.
Denev, A. and Mutnikas, Y. (2016).“A Formalized, Integrated and Visual Approach to Stress Testing.” In: _SSRN
e-Print_.
Diffenbaugh, N. S. (2020).“Verification of extreme event attribution: Using out-of-sample observations to assess
changes in probabilities of unprecedented events.” In: _Science Advances_ 6(12), eaay2368.
Ding, D., Zhang, M., Pan, X., Yang, M., and He, X. (2019).“Modeling Extreme Events in Time Series Prediction.”
In: _Proceedings of the 25th ACM SIGKDD International Conference on Knowledge Discovery & Data Mining_.
ACM.
Ding, L., Ahmed, S., and Shapiro, A. (2020).“A Python package for multi-stage stochastic programming.” In:
_Optimization Online e-Print_.
Dixon, M. and Polson, N. (2020).“Deep Fundamental Factor Models.” In: _SIAM Journal on Financial Mathematics_
11(3), SC–26–SC–37.
Dixon, M. F., Halperin, I., and Bilokon, P. (2020). _Machine Learning in Finance: from theory to practice_. Springer
International Publishing. 548 pp.
Dogariu, M., Stefan, L.-D., Boteanu, B. A., Lamba, C., and Bogdan Ionescu, B. K. nd (2021a).“Generation of
Realistic Synthetic Financial Time-Series.” In: _ACM Trans. Multimedia Comput. Commun. Appl_ 37(4) (111).
Dogariu, M., Stefan, L.-D., Boteanu, B. A., Lamba, C., and Ionescu, B. (2021b).“Towards Realistic Financial Time
Series Generation via Generative Adversarial Learning.” In: _European Signal Processing Conference - EUSIPCO_.
Dong, X., Li, Y., Rapach, D., and Zhou, G. (2022).“Anomalies and the expected market return.” In: _Journal of
Finance_ 27(1), pp. 639–681.
Eckerli, F. (2021).“Generative Adversarial Networks in finance: an overview.” In: _SSRN e-Print_.
Eckerli, F. and Osterrieder, J. (2021).“Generative Adversarial Networks in finance: an overview.” In: _arXiv e-Print_.
El Karoui, N. and Purdom, E. (2018).“Can we trust the bootstrap in high-dimensions? the case of linear models.”
In: _The Journal of Machine Learning Research_.
Elkamhi, R. and Stefanova, D. (2015).“Dynamic Hedging and Extreme Asset Co-movements.” In: _The Review of
Financial Studies_ 28(3), pp. 743–790.
Engelke, S. and Ivanovs, J. (2021).“Sparse Structures for Multivariate Extremes.” In: _Annual Review of Statistics
and Its Application_ 8(1).
Engle, R. F. (2020).“Stress Testing with Market Data.” In: _SSRN e-Print_.
Esmaeili, A., Gallagher, J. C., Springer, J. A., and Matson, E. T. (2021).“HAMLET: A Hierarchical Agent-based
Machine Learning Platform.” In: _ACM Transactions on Autonomous and Adaptive Systems_ 16(3-4), pp. 1–46.
Fabozzi, F. J., Fabozzi, F. A., Lopez de Prado, M., and Stoyanov, S. (2021). _Asset Management: Tools and Issues_.
World Scientific. 516 pp.
Facchinato, S. and Pola, G. (2014).“Managing uncertainty with diversification across macroeconomic scenarios
(DAMS): from asset segmentation to portfolio.” In: _SSRN e-Print_.
Faez, F., Ommi, Y., Baghshah, M. S., and Rabiee, H. R. (2020).“Deep Graph Generators: A Survey.” In: _arXiv
e-Print_.
Faggini, M., Bruno, B., and Parziale, A. (2019).“Crises in economic complex networks: Black Swans or Dragon
Kings?” In: _Economic Analysis and Policy_ 62, pp. 105–115.
Fakoor, R., Mueller, J., Erickson, N., Chaudhari, P., and Smola, A. J. (2020).“Fast, Accurate, and Simple Models
for Tabular Data via Augmented Distillation.” In: _arXiv e-Print_.
Fang, J. and Lin, J. (2020).“Prior knowledge distillation based on financial time series.” In: _arXiv e-Print_.
Fawaz, H. I., Forestier, G., Weber, J., Idoumghar, L., and Muller, P.-A. (2018).“Data augmentation using synthetic
data for time series classification with deep residual networks.” In: _arXiv e-Print_.


Flaig, S. and Junike, G. (2022). “Scenario generation for market risk models using generative neural networks.” In:
_arXiv e-Print_.
Flood, M. D. and Korenko, G. G. (2015).“Systematic scenario selection: stress testing and the nature of uncertainty.”
In: _Quantitative Finance_ 15(1), pp. 43–59.
Fons, E., Dawson, P., Zeng, X.-j., Keane, J., and Iosifidis, A. (2021a).“Adaptive Weighting Scheme for Automatic
Time-Series Data Augmentation.” In: _arXiv e-Print_.
Fons, E., Dawson, P., Zeng, X.-j., Keane, J., and Iosifidis, A. (2021b).“Augmenting Transferred Representations for
Stock Classification.” In: _ICASSP 2021 - 2021 IEEE International Conference on Acoustics, Speech and Signal
Processing (ICASSP)_. IEEE.
Foramitti, J. (2021).“AgentPy: A package for agent-based modeling in Python.” In: _Journal of Open Source Software_
6(62), p. 3065.
Frahm, G. (2015).“A theoretical foundation of portfolio resampling.” In: _Theory and Decision_ 79(1), pp. 107–132.
Franco-Pedroso, J., Gonzalez-Rodriguez, J., Planas, M., Cubero, J., Cobo, R., and Pablos, F. (2019a).“Generating
Virtual Scenarios of Multivariate Financial Data for Quantitative Trading Applications.” In: _The Journal of
Financial Data Science_ 1 (2), pp. 55–77.
Franco-Pedroso, J., Gonzalez-Rodriguez, J., Planas, M., Cubero, J., Cobo, R., and Pablos, F. (2019b).“The ETS
challenges: a machine learning approach to the evaluation of simulated financial time series for improving gen-
eration processes.” In: _The Journal of Financial Data Science_ 1(3) (3), pp. 68–86.
Franses, P. H. and Bruijn, B. de (2017).“Benchmarking Judgmentally Adjusted Forecasts.” In: _International Journal
of Finance and Economics_ 22(1), pp. 3–11.
Fritzsch, S., Timphus, M., and Weiss, G. N. F. (2021).“Marginals Versus Copulas: Which Account For More Model
Risk In Multivariate Risk Forecasting?” In: _SSRN e-Print_.
Fu, B., Kirchbuchner, F., and Kuijper, A. (2020).“Data augmentation for time series.” In: _Proceedings of the 13th
ACM International Conference on Pervasive Technologies Related to Assistive Environments_. ACM.
Fulle, M. J. and Herwartz, H. (2021).“A Multivariate Markov-Switching GARCH Model with Copula-Distributed
Innovations.” In: _SSRN e-Print_.
Galeeva, R., Hoogland, J., and Eydeland, A. (2012).“Measuring correlation risk for Energy Derivatives.” In: _Risk
Management in Commodity Markets: From Shipping to Agriculturals and Energy_.
Gao, G., Mishra, B., and Ramazzotti, D. (2017).“Efficient Simulation of Financial Stress Testing Scenarios with
Suppes-Bayes Causal Networks.” In: _arXiv e-Print_.
Gao, G., Mishra, B., and Ramazzotti, D. (2018).“Causal data science for financial stress testing.” In: _Journal of
Computational Science_ 26, pp. 294–304.
Gharghabi, S., Imani, S., Bagnall, A., Darvishzadeh, A., and Keogh, E. (2018).“Matrix profile XII: mpdist: A
novel time series distance measure to allow data mining in more challenging scenarios.” In: _IEEE International
Conference on Data Mining (ICDM)_. IEEE, pp. 965–970.
Gilleland, E. (2020a).“Bootstrap Methods for Statistical Inference. Part I: Comparative Forecast Verification for
Continuous Variables.” In: _Journal of Atmospheric and Oceanic Technology_ 37(11), pp. 2117–2134.
Gilleland, E. (2020b).“Bootstrap Methods for Statistical Inference. Part II: Extreme-Value Analysis.” In: _Journal
of Atmospheric and Oceanic Technology_ 37(11), pp. 2135–2144.
Glasserman, P., Kang, C., and Kang, W. (2015).“Stress scenario selection by empirical likelihood.” In: _Quantitative
Finance_ 15(1), pp. 25–41.
Goel, K., Gu, A., Li, Y., and Re, C. (2020).“Model Patching: Closing the Subgroup Performance Gap with Data
Augmentation.” In: _arXiv e-Print_.
Golub, B., Greenberg, D., and Ratcliffe, R. (2018).“Market-Driven Scenarios: An Approach for Plausible Scenario
Construction.” In: _The Journal of Portfolio Management_ 44(5), pp. 6–20.
Goncalves, S. and Perron, B. (2020).“Bootstrapping factor models with cross sectional dependence.” In: _Journal of
Econometrics_ 218(2), pp. 476–495.
Gonzalez, D. P., Rebollo, F. F., Polo, F. J. G., and Vyetrenko, S. (2021).“Similarity Metrics for Transfer Learning
in Financial Markets.” In: _ICAPS Workshop on Planning for Financial Services (FinPlan 2021)_.
Grealish, A. and Kolm, P. N. (2021).“Robo-Advisory: From Investing Principles and Algorithms to Future Devel-
opments.” In: _SSRN e-Print_.
Großer, J. and Okhrin, O. (2021).“Copulae: An overview and recent developments.” In: _WIREs Computational
Statistics_.


Grundke, P. (2012).“Further recipes for quantitative reverse stress testing.” In: _Journal of Risk Model Validation_
6(2).
Guijarro-Ordonez, J., Pelger, M., and Zanotti, G. (2021).“Deep Learning Statistical Arbitrage.” In: _SSRN e-Print_.
Gurdogan, H. and Kercheval, A. (2021). “Multi Anchor Point Shrinkage for the Sample Covariance Matrix (Extended
Version).” In: _arXiv e-Print_.
Gzyl, H., Horst, E. ter, and Molina, G. (2017).“Inferring probability densities from expert opinion.” In: _Applied
Mathematical Modelling_ 43, pp. 306–320.
Haldane, A. G. and Turrell, A. E. (2018).“Drawing on different disciplines: macroeconomic agent-based models.”
In: _Journal of Evolutionary Economics_ 29(1), pp. 1–28.
Hambuckers, J. and Heuchenne, C. (2016).“Estimating the Out-of-Sample Predictive Ability of Trading Rules: A
Robust Bootstrap Approach.” In: _Journal of Forecasting_ 35(4), pp. 347–372.
Harutyunyan, H., Moyer, D., Khachatrian, H., Steeg, G. V., and Galstyan, A. (2021).“Efficient Covariance Esti-
mation from Temporal Data.” In: _arXiv e-Print_.
Harwick, C. (2021).“Helipad: A Framework for Agent-Based Modeling in Python.” In: _SSRN e-Print_.
He, Z., Xie, L., Chen, X., Zhang, Y., Wang, Y., and Tian, Q. (2019).“Data Augmentation Revisited: Rethinking
the Distribution Gap between Clean and Augmented Data.” In: _arXiv e-Print_.
Heaton, J. B. and Witte, J. (2021).“Synthetic Financial Data: An Application to Regulatory Compliance for
Broker-Dealers.” In: _SSRN e-Print_.
Henry-Labordere, P. (2019).“Generative models for financial data.” In: _SSRN e-Print_.
Ho, J., Tumkaya, T., Aryal, S., Choi, H., and Claridge-Chang, A. (2019).“Moving beyond P values: data analysis
with estimation graphics.” In: _Nature Methods_ 16(7), pp. 565–566.
Hofert, M., Prasad, A., and Zhu, M. (2021).“Multivariate time-series modeling with generative neural networks.”
In: _arXiv e-Print_.
Hoffman, J. I. E. (2015).“Resampling Statistics.” In: _Biostatistics for Medical and Biomedical Practitioners_. Elsevier,
pp. 655–661.
Hoffmann, J., Bar-Sinai, Y., Lee, L., Andrejevic, J., Mishra, S., Rubinstein, S. M., and Rycroft, C. H. (2018).
“Machine Learning in a data-limited regime: Augmenting experiments with synthetic data uncovers order in
crumpled sheets.” In: _arXiv e-Print_.
Homescu, C. (2014).“Many risks, one (optimal) portfolio.” In: _SSRN e-Print_.
Homescu, C. (2015).“Better Investing Through Factors, Regimes and Sensitivity Analysis.” In: _SSRN e-Print_.
Honore, B. E. and Hu, L. (2017).“Poor (Wo)man’s Bootstrap.” In: _Econometrica_ 85(4), pp. 1277–1301.
Horowitz, J. L. (2019).“Bootstrap methods in econometrics.” In: _Annual review of economics_ 11(1), pp. 193–224.
Hsu, M.-W., Lessmann, S., Sung, M.-C., Ma, T., and Johnson, J. E. V. (2016).“Bridging the divide in financial
market forecasting: machine learners vs. financial economists.” In: _Expert Systems with Applications_ 61, pp. 215–
234.
Hu, J., Akande, O., and Wang, Q. (2021). “Multiple Imputation and Synthetic Data Generation with the R package
NPBayesImputeCat.” In: _arXiv e-Print_.
Huang, M. and Yu, S. (2020).“A new procedure for resampled portfolio with shrinkaged covariance matrix.” In:
_Journal of Applied Statistics_ 47(44), pp. 642–652.
Imbens, G. and Menzel, K. (2021).“A causal bootstrap.” In: _Annals of Statistics_ 49(3).
Imokoyende, M. (2019).“Variational Autoencoder In Finance.” In: _Towards Data Science_.
Irlam, G. (2020a). _AI Planner_ .url:https://www.aiplanner.com/.
Irlam, G. (2020b).“Machine learning for retirement planning.” In: _The Journal of Retirement_ 8(1), pp. 32–29.
Irlam, G. (2020c).“Multi Scenario Financial Planning via Deep Reinforcement Learning AI.” In: _SSRN e-Print_.
Istrate, G. (2021).“Models we Can Trust: Toward a Systematic Discipline of (Agent-Based) Model Interpretation
and Validation.” In: _arXiv e-Print_.
Iwana, B. K. and Uchida, S. (2021).“An empirical survey of data augmentation for time series classification with
neural networks.” In: _PLOS One_ 16(7). Ed. by F. Schwenker, e0254841.
Jabbar, A., Li, X., and Omar, B. (2020).“A Survey on Generative Adversarial Networks: Variants, Applications,
and Training.” In: _arXiv e-Print_.
Jaeger, M., Krugel, S., Marinelli, D., Papenbrock, J., and Schwendner, P. (2020).“Understanding machine learning
for diversified portfolio construction by explainable AI.” In: _SSRN e-Print_.
Janke, T., Ghanmi, M., and Steinke, F. (2021). “Implicit Generative Copulas.” In: _arXiv e-Print_.
Jansen, S. (2020). _Machine Learning for Algorithmic Trading (Second Edition)_. Packt Publishing. 820 pp.


Javeri, I. Y., Toutiaee, M., Arpinar, I. B., Miller, J. A., and Miller, T. W. (2021).“Improving Neural Networks for
Time-Series Forecasting using Data Augmentation and AutoML.” In: _IEEE Seventh International Conference
on Big Data Computing Service and Applications (BigDataService)_. IEEE.
Jericevich, I., McKechnie, M., and Gebbie, T. (2021).“Calibrating an adaptive Farmer-Joshi agent-based model for
financial markets.” In: _arXiv e-Print_.
Jiang, L., Dai, B., Wu, W., and Loy, C. C. (2021a). “Deceive D: Adaptive Pseudo Augmentation for GAN Training
with Limited Data.” In: _arXiv e-Print_.
Jiang, W., Song, S., Hou, L., and Zhao, H. (2021b).“A set of efficient methods to generate high-dimensional binary
data with specified correlation structures.” In: _The American Statistician_ 75(3), pp. 310-3221–37.
Jin, C. and Rinard, M. (2021). “Towards Context-Agnostic Learning Using Synthetic Data.” In: _arXiv e-Print_.
Johnson, M. C. and West, M. (2018).“Bayesian Predictive Synthesis: Forecast Calibration and Combination.” In:
_arXiv e-Print_.
Juan, A. A., Keenan, P., Martı́, R., McGarraghy, S., Panadero, J., Carroll, P., and Oliva, D. (2022).“A review of
the role of heuristics in stochastic optimisation: from metaheuristics to learnheuristics.” In: _Annals of Operations
Research_.
Jurczenko et al. (2020). _Machine Learning for Asset Management_. Ed. by E. Jurczenko. Wiley. 445 pp.
Kakushadze, Z. and Yu, W. (2016).“Statistical Risk Models.” In: _SSRN e-Print_.
Kakushadze, Z. and Yu, W. (2017).“Open Source Fundamental Industry Classification.” In: _MDPI Data_ 22 (2).
Kakushadze, Z. and Yu, W. (2018a).“Betas, Benchmarks, and Beating the Market.” In: _The Journal of Trading_.
Kakushadze, Z. and Yu, W. (2018b).“Decoding stock market with quant alphas.” In: _Journal of Asset Management_ ,
pp. 1–11.
Kakushadze, Z. and Yu, W. (2019).“Machine learning risk models.” In: _SSRN e-Print_.
Kakushadze, Z. and Yu, W. (2020).“Machine learning treasury yields.” In: _SSRN e-Print_.
Kang, Y., Hyndman, R. J., and Li, F. (2020).“GRATIS: GeneRAting TIme Series with diverse and controllable
characteristics.” In: _Statistical Analysis and Data Mining: The ASA Data Science Journal_ 13(4), pp. 354–376.
Kang, Y., Spiliotis, E., Petropoulos, F., Athiniotis, N., Li, F., and Assimakopoulos, V. (2021).“Déjà vu: A data-
centric forecasting approach through time series cross-similarity.” In: _Journal of Business Research_.
Kantos, C. and diBartolomeo, D. (2020).“How the pandemic taught us to turn smart beta into real alpha.” In:
_Journal of Asset Management_ 21(7), pp. 581–590.
Kapoor, A. and Shrivastava, U. (2014).“Extreme Values Theory and Return Level Analysis for Catastrophe Pre-
diction.” In: _The Journal of Investing_ 23(2), pp. 124–135.
Karaś, M. and Serwatka, A. (2021).“Strong-hand conjecture: agent-based numerical simulation.” In: _The Journal
of Investment Strategies_.
Kegel, L., Hahmann, M., and Lehner, W. (2017).“Generating What-If Scenarios for Time Series Data.” In: _Proceed-
ings of the 29th International Conference on Scientific and Statistical Database Management - ’17_. New York,
New York, USA: ACM Press, pp. 1–12.
Kegel, L., Hahmann, M., and Lehner, W. (2018).“Feature-based comparison and generation of time series.” In:
_Proceedings of the 30th International Conference on Scientific and Statistical Database Management - ’18_. New
York, New York, USA: ACM Press, pp. 1–12.
Kemp, M. (2014). _Extreme Events: Robust Portfolio Construction in the Presence of Fat Tails_. Wiley. 334 pp.
Kingma, D. P. and Welling, M. (2019).“An introduction to variational autoencoders.” In: _Foundations and Trends
in Machine Learning_ 12(4), pp. 307–392.
Koesdwiady, A., Khatib, A. E., and Karray, F. (2018).“Methods to Improve Multi-Step Time Series Prediction.”
In: _International Joint Conference on Neural Networks (IJCNN)_. IEEE, pp. 1–8.
Kondratyev, A. and Schwarz, C. (2020).“The Market Generator.” In: _Risk_.
Kong, K., Li, G., Ding, M., Wu, Z., Zhu, C., Ghanem, B., Taylor, G., and Goldstein, T. (2022). “Robust Optimization
as Data Augmentation for Large-scale Graphs.” In: _arXiv e-Print_.
Koochali, A., Dengel, A., and Ahmed, S. (2020).“If You Like It, GAN It. Probabilistic Multivariate Times Series
Forecast With GAN.” In: _arXiv e-Print_.
Kopeliovich, Y., Novosyolov, A., Satchkov, D., and Schachter, B. (2015).“Robust Risk Estimation and Hedging: A
Reverse Stress Testing Approach.” In: _The Journal of Derivatives_ 22(4), pp. 10–25.
Koshiyama, A., Firoozye, N., and Treleaven, P. (2021).“Generative Adversarial Networks for Financial Trading
Strategies Fine-Tuning and Combination.” In: _Quantitative Finance_ 21(5), pp. 797–813.


Kreiss, J.-P. and Paparoditis, E. (2011).“Bootstrap methods for dependent data: A review.” In: _Journal of the
Korean Statistical Society_ 40(4), pp. 357–378.
Kritzman, M., Kinlaw, W., and Turkington, D. (2017). _A Practitioner’s Guide to Asset Allocation_. Wiley. 256 pp.
Kritzman, M., Li, D., Qiu, G. (, and Turkington, D. (2021).“Portfolio Choice with Path-Dependent Scenarios.” In:
_Financial Analysts Journal_ 77(1), pp. 90–100.
Kritzman, M. and Turkington, D. (2021).“History, Shocks and Drifts: A New Approach to Portfolio Formation.”
In: _SSRN e-Print_.
Kritzman, M. and Turkington, D. (2022).“History, Shocks, and Drifts: A New Approach to Portfolio Formation.”
In: _The Journal of Portfolio Management_ 48(2).
Kuchnik, M. and Smith, V. (2018).“Efficient Augmentation via Data Subsampling.” In: _arXiv e-Print_.
Lai, K.-H., Zha, D., Wang, G., Xu, J., Zhao, Y., Kumar, D., Chen, Y., Zumkhawaka, P., Wan, M., Martinez, D.,
and Hu, X. (2021). “TODS: An Automated Time Series Outlier Detection System.” In: _arXiv e-Print_.
Lam, H. and Li, F. (2020).“Parametric Scenario Optimization under Limited Data: A Distributionally Robust
Optimization View.” In: _arXiv e-Print_.
Laskin, M., Lee, K., Stooke, A., Pinto, L., Abbeel, P., and Srinivas, A. (2020). “Reinforcement Learning with
Augmented Data.” In: _arXiv e-Print_.
Lawrence, A. R., Kaiser, M., Sampaio, R., and Sipos, M. (2021).“Data Generating Process to Evaluate Causal
Discovery Techniques for Time Series Data.” In: _arXiv e-Print_.
Ledermann, D. and Alexander, C. (2012). “Further properties of random orthogonal matrix simulation.” In: _Math-
ematics and Computers in Simulation_ 83, pp. 56–79.
Ledermann, W., Alexander, C., and Ledermann, D. (2011). “Random orthogonal matrix simulation.” In: _Linear
Algebra and its Applications_ 434, pp. 1444–1467.
Ledoit, O. and Wolf, M. (2021).“Shrinkage estimation of large covariance matrices: Keep it simple, statistician?”
In: _Journal of Multivariate Analysis_ 186, p. 104796.
Lee, Y.-H., Hsieh, M.-H., Kuo, W., and Tsai, C. J. (2021).“How can an economic scenario generation model cope
with abrupt changes in financial markets?” In: _China Finance Review International_ 11(3), pp. 372–405.
Lee, M. I. (2013).“Stress testing Monte Carlo assumptions.” In: _SSRN e-Print_.
Leon, C. and Reveiz, A. (2012).“Monte Carlo Simulation of Long-Term Dependent Processes: A Primer.” In:
_Wilmott_ 2012(60), pp. 48–57.
Lerch, S., Thorarinsdottir, T. L., Ravazzolo, F., and Gneiting, T. (2017).“Forecaster’s Dilemma: Extreme Events
and Forecast Evaluation.” In: _Statistical Science_ 32(1), pp. 106–127.
Lettau, M. and Pelger, M. (2020).“Factors That Fit the Time Series and Cross-Section of Stock Returns.” In: _The
Review of Financial Studies_ 33(5), pp. 2274–2325.
Lezmi, E., Malongo, H., Roncalli, T., and Sobotka, R. (2019).“Portfolio Allocation with Skewness Risk: A Practical
Guide.” In: _SSRN e-Print_.
Lezmi, E., Roche, J., Roncalli, T., and Xu, J. (2020).“Improving the Robustness of Trading Strategy Backtesting
with Boltzmann Machines and Generative Adversarial Networks.” In: _SSRN e-Print_.
Leznik, M., Michalsky, P., Willis, P., Schanzel, B., Ostberg, P.-O., and Domaschka, J. (2021).“Multivariate Time
Series Synthesis Using Generative Adversarial Networks.” In: _Proceedings of the ACM/SPEC International Con-
ference on Performance Engineering_. ACM.
Li, B., Luo, S., Qin, X., and Pan, L. (2021a).“Improving GAN with inverse cumulative distribution function for
tabular data synthesis.” In: _Neurocomputing_ 456, pp. 373–383.
Li, G., Huang, L., Yang, J., and Zhang, W. (2022).“A Synthetic Regression Model for Large Portfolio Allocation.”
In: _Journal of Business & Economic Statistics_ , pp. 1–13.
Li, Z., Liu, X.-Y., Zheng, J., Wang, Z., Walid, A., and Guo, J. (2021b).“FinRL-Podracer: High Performance and
Scalable Deep Reinforcement Learning for Quantitative Finance.” In: _ACM International Conference on AI in
Finance_.
Li, Z., Zhao, Y., and Fu, J. (2020).“SynC: A Copula based Framework for Generating Synthetic Data from
Aggregated Sources.” In: _International Conference on Data Mining Workshops (ICDMW)_. IEEE.
Lim, S. H., Erichson, N. B., Utrera, F., Xu, W., and Mahoney, M. W. (2021). “Noisy Feature Mixup.” In: _arXiv
e-Print_.
Lin, Z., Jain, A., Wang, C., Fanti, G., and Sekar, V. (2019).“Generating High-fidelity, Synthetic Time Series
Datasets with DoppelGANger.” In: _arXiv e-Print_.


Linardi, M., Zhu, Y., Palpanas, T., and Keogh, E. (2018).“VALMOD: A suite for easy and exact detection of
variable length motifs in data series.” In: _Proceedings of the 2018 International Conference on Management of
Data - SIGMOD ’18_. New York, New York, USA: ACM Press, pp. 1757–1760.
Lindner, D., Shah, R., Abbeel, P., and Dragan, A. (2021). “Learning What To Do by Simulating the Past.” In:
_arXiv e-Print_.
Little, M. A. and Badawy, R. (2020). “Causal bootstrapping.” In: _arXiv e-Print_.
Liu, B., Zhang, Z., and Cui, R. (2020).“Efficient Time Series Augmentation Methods.” In: _13th International
Congress on Image and Signal Processing, BioMedical Engineering and Informatics (CISP-BMEI)_. IEEE.
Liu, X.-Y., Rui, J., Gao, J., Yang, L., Yang, H., Wang, Z., Wang, C. D., and Guo, J. (2022). “FinRL-Meta: A
Universe of Near-Real Market Environments for Data-Driven Deep Reinforcement Learning in Quantitative
Finance.” In: _arXiv e-Print_.
Liu, X.-Y., Yang, H., Gao, J., and Wang, C. (2021).“FinRL: Deep Reinforcement Learning Framework to Automate
Trading in Quantitative Finance.” In: _SSRN e-Print_.
Lopez de Prado, M. (2020). _Machine learning for asset managers_. Cambridge University Press. 190 pp.
Lu, L. and Ghosh, S. (2021). “Nonparametric estimation of multivariate copula using empirical bayes method.” In:
_arXiv e-Print_.
Lux, T. (2021).“Can heterogeneous agent models explain the alleged mispricing of the S&P 500?” In: _Quantitative
Finance_ 21(9), pp. 1413–1433.
Ma, J. (2021). “copent: Estimating Copula Entropy and Transfer Entropy in R.” In: _arXiv e-Print_.
Mammen, E. and Nandi, S. (2012).“Bootstrap and Resampling.” In: _Handbook of Computational Statistics_. Ed. by
J. E. Gentle, W. K. Hardle, and Y. Mori. Springer Handbooks of Computational Statistics. Springer Berlin
Heidelberg, pp. 499–527.
Mannix, R. and Cesa, M. (2021).“’Signatures’ promise quants a tool for all jobs.” In: _Risk (Quant Investing)_.
Mariani, G., Zhu, Y., Li, J., Scheidegger, F., Istrate, R., Bekas, C., and Malossi, A. C. I. (2019).“PAGAN: Portfolio
Analysis with Generative Adversarial Networks.” In: _arXiv e-Print_.
Marinescu, M. (2022).“Risk-Based Optimal Portfolio Strategies: A Compendium.” In: _SSRN e-Print_.
Marti, G. (2020a).“CORRGAN: sampling realistic financial correlation matrices using generative adversarial net-
works .” In: _ICASSP - IEEE nternational Conference on Acoustics, Speech and Signal Processing_. IEEE, pp. 8459–
8463.
Marti, G. (2020b).“Generating Realistic Synthetic Data in Finance: Applications of GANs.” In: _IHS Markit Webinar_.
Marti, G., Andler, S., Nielsen, F., and Donnat, P. (2017). “Exploring and measuring non-linear correlations: Copulas,
Lightspeed Transportation and Clustering.” In: _Proceedings of Machine Learning Research_ 55, pp. 59–69.
Marti, G., Goubet, V., and Nielsen, F. (2021a).“cCorrGAN: Conditional Correlation GAN for Learning Empirical
Conditional Distributions in the Elliptope.” In: _International Conference on Geometric Science of Information_.
Springer International Publishing, pp. 613–620.
Marti, G., Nielsen, F., Bihkowski, M., and Donnat, P. (2021b).“A review of two decades of correlations, hierarchies,
networks and clustering in financial markets.” In: _Progress in Information Geometry_ , pp. 245–274.
Martin, R. (2021).“PyPortfolioOpt: portfolio optimization in Python.” In: _Journal of Open Source Software_ 6(61),
p. 3066.
Marwood, D. and Minnen, D. (2020).“Safely Boosting Retirement Income by Harmonizing Drawdown Paths.” In:
_Journal of Financial Planning_ 33(11), pp. 46–60.
Maschner, C., Moritz, B., and Schmitz, M. (2021).“Modern Asset Management.” In: _SSRN e-Print_.
McIndoe, C. (2020).“A Data Driven Approach to Market Regime Classification.” MA thesis. Imperial College.
Medina, M. A., Davis, R. A., and Samorodnitsky, G. (2021). “Spectral learning of multivariate extremes.” In: _arXiv
e-Print_.
Meucci, A. (2008). “Fully Flexible Views: Theory and Practice.” In: _Risk_ 21(10), pp. 97–102.
Meucci, A. (2012). _A Fully Integrated Liquidity and Market Risk Model_. Tech. rep. EDHEC.
Meucci, A., Ardia, D., and Keel, S. (2012). “Fully Flexible Extreme Views.” In: _Risk_ 14(2), pp. 39–49.
Meyer, D. and Nagler, T. (2021).“Synthia: multidimensional synthetic data generation in Python.” In: _Journal of
Open Source Software_ 6(65), p. 2863.
Michaud, R. O. and Michaud, R. (2015).“Estimation Error and Portfolio Optimization: A Resampling Solution.”
In: _SSRN e-Print_.
Micheli, A. and Neuman, E. (2022). “Evidence of Crowding on Russell 3000 Reconstitution Events.” In: _arXiv
e-Print_.


Mikalsen, K. O., Bianchi, F. M., Soguero-Ruiz, C., and Jenssen, R. (2018).“Time Series Cluster Kernel for Learning
Similarities between Multivariate Time Series with Missing Data.” In: _Pattern Recognition_ 76, pp. 569–581.
Milevsky, M. A. (2020). _Retirement Income Recipes in R: From Ruin Probabilities to Intelligent Drawdowns_. Springer
International Publishing. 302 pp.
Moudiki, T. and Planchet, F. (2016).“Economic Scenario Generators.” In: _Modelling in Life Insurance - A Man-
agement Perspective_. Ed. by J.-P. Laurent, R. Norberg, and F. Planchet. EAA Series. Springer International
Publishing, pp. 81–104.
Nasri, B. R. and Rémillard, B. N. (2019).“Copula-based dynamic models for multivariate time series.” In: _Journal
of Multivariate Analysis_ 172, pp. 107–121.
Nasri, B. R., Rémillard, B. N., and Thioub, M. Y. (2020).“Goodness-of-fit for regime-switching copula models with
application to option pricing.” In: _Canadian Journal of Statistics_ 48(1), pp. 79–96.
Naveau, P., Hannart, A., and Ribes, A. (2020).“Statistical methods for extreme event attribution in climate science.”
In: _Annual Review of Statistics and its Application_ 7(1), pp. 89–110.
Nguyen, H. D. and Chamroukhi, F. (2018).“Practical and theoretical aspects of mixture-of-experts modeling: An
overview.” In: _WIREs Data Mining Knowl Discov_ 8(4), e1246.
Ni, H., Szpruch, L., Wiese, M., Liao, S., and Xiao, B. (2020).“Conditional Sig-Wasserstein GANs for Time Series
Generation.” In: _arXiv e-Print_.
Niemann, J.-H., Klus, S., and Schutte, C. (2021).“Data-driven model reduction of agent-based systems using the
Koopman generator.” In: _arXiv e-Print_.
Oneto, L. (2019).“Resampling Methods.” In: _Model Selection and Error Estimation in a Nutshell_. Springer Inter-
national Publishing, pp. 25–31.
Opdyke, J. D. (2020).“Full Probabilistic Control for Direct and Robust, Generalized and Targeted Stressing of the
Correlation Matrix (Even When Eigenvalues are Empirically Challenging.” In: _QuantMinds/RiskMinds Confer-
ence_.
Ortec Finance (2014).“Ex ante risk management with scenarios.” In: _CFA Society Switzerland_.
Packham, N. and Woebbeking, F. (2021).“Correlation scenarios and correlation stress testing.” In: _SSRN e-Print_.
Padhi, I., Schiff, Y., Melnyk, I., Rigotti, M., Mroueh, Y., Dognin, P., Ross, J., Nair, R., and Altman, E. (2021).
“Tabular Transformers for Modeling Multivariate Time Series.” In: _arXiv e-Print_.
Page, S. (2013).“How to combine long and short return histories efficiently.” In: _Financial Analysts Journal_ 69(1),
pp. 45–52.
Pan, I., Mason, L., and Matar, O. (2021). “Data-Centric Engineering: integrating simulation, machine learning and
statistics. Challenges and Opportunities.” In: _arXiv e-Print_.
Panchekha, A., Tull, R., and Bell, M. M. (2018).“Ensemble Active Management.” In: _SSRN e-Print_.
Papenbrock, J., Schwendner, P., Jaeger, M., and Krugel, S. (2021).“Matrix Evolutions: Synthetic Correlations and
Explainable Machine Learning for Constructing Robust Investment Portfolios.” In: _The Journal of Financial
Data Science_ 3(2), pp. 51–69.
Papoudakis, G., Christianos, F., and Albrecht, S. V. (2021). “Agent Modelling under Partial Observability for Deep
Reinforcement Learning.” In: _arXiv e-Print_.
Pathak, P. K. and Rao, C. R. (2013).“The Sequential Bootstrap.” In: _Handbook of Statistics_. Vol. 31. Elsevier,
pp. 2–18.
Paul, J., Michael, B.-S., Pedro, M., Rajbir, S. N., Shubham, K., Valentin, F., Jan, G., and Tim, J. (2022). “PSA-
GAN: Progressive Self Attention GANs for Synthetic Time Series.” In: _arXiv e-Print_.
Pei, H., Ren, K., Yang, Y., Liu, C., Qin, T., and Li, D. (2021). “Towards Generating Real-World Time Series Data.”
In: _arXiv e-Print_.
Perez, J., Arroba, P., and Moya, J. M. (2022). “Data augmentation through multivariate scenario forecasting in
Data Centers using Generative Adversarial Networks.” In: _arXiv e-Print_.
Perrin, S. and Roncalli, T. (2020).“Machine Learning Optimization Algorithms & Portfolio Allocation.” In: _Machine
Learning for Asset Management: New Developments and Financial Applications_. Ed. by E. Jurczenko. Wiley,
pp. 261–328.
Perumal, R. and van Zyl, T. L. (2020).“Surrogate Assisted Methods for the Parameterisation of Agent-Based
Models.” In: _arXiv e-Print_.
Pesenti, S. M., Bettini, A., Millossovich, P., and Tsanakas, A. (2020).“Scenario weights for importance measurement
(SWIM) - an R package for sensitivity analysis.” In: _SSRN e-Print_.


Pesenti, S. M., Millossovich, P., and Tsanakas, A. (2019).“Reverse sensitivity testing: What does it take to break
the model?” In: _European Journal of Operational Research_ 274(2), pp. 654–670.
Qi, D. and Majda, A. J. (2019).“Using machine learning to predict extreme events in complex systems.” In:
_Proceedings of the National Academy of Sciences of the United States of America_.
Qian, W., Rolling, C. A., Cheng, G., and Yang, Y. (2022).“Combining forecasts for universally optimal perfor-
mance.” In: _International Journal of Forecasting_.
Raab, G. M., Nowok, B., and Dibben, C. (2021). “Assessing, visualizing and improving the utility of synthetic data.”
In: _arXiv e-Print_.
Racca, A. and Magri, L. (2022). “Statistical prediction of extreme events from small datasets.” In: _arXiv e-Print_.
Raghunathan, T. E. (2021).“Synthetic Data.” In: _Annual Review of Statistics and Its Application_ 8(1), pp. 129–140.
Raileanu, R., Goldstein, M., Yarats, D., Kostrikov, I., and Fergus, R. (2021). “Automatic Data Augmentation for
Generalization in Deep Reinforcement Learning.” In: _arXiv e-Print_.
Rajabi, A. and Garibay, O. O. (2021). “TabFairGAN: Fair Tabular Data Generation with Generative Adversarial
Networks.” In: _arXiv e-Print_.
Rao, A. and Jelvis, T. (2022). _Foundations of Reinforcement Learning with Applications in Finance_.
Rebonato, R. (2018).“The quickest way to lose the money you cannot afford to lose: reverse stress testing with
maximum entropy.” In: _Journal of Risk_ 20(3), pp. 83–93.
Rikli, S., Bigler, D. N., Pfenninger, M., and Osterrieder, J. (2021).“Wasserstein GAN: Deep Generation applied on
Bitcoins financial time series.” In: _arXiv e-Print_.
Rocca, J. and Rocca, B. (2019).“Intuitively Understanding Variational Autoencoders.” In: _Towards Data Science_.
Rojas, H. and Dias, D. (2021).“Stress testing network reconstruction via graphical causal model.” In: _Applied
Stochastic Models in Business and Industry_.
Romano, J. P. and Wolf, M. (2018).“Multiple Testing of One-Sided Hypotheses: Combining Bonferroni and the
Bootstrap.” In: _Predictive econometrics and big data_. Ed. by V. Kreinovich, S. Sriboonchitta, and N. Chakpitak.
Vol. 753. Springer International Publishing, pp. 78–94.
Roncalli, T. (2021).“Advanced Course in Asset Management.” In: _SSRN e-Print_.
Rosen, D. (2015a).“Integrating Economic Scenarios with Advanced Scenario Analytics to Manage Investment
Portfolios.” In: _SSRN e-Print_.
Rosen, D. (2015b).“Re-Thinking Scenarios: Stress Testing of Multi-Asset Portfolios by Integrating Economic Sce-
narios with Advanced Simulation Analytics.” In: _SSRN e-Print_.
Rosen, D. and Saunders, D. (2015).“Regress Under Stress: A Simple Least-Squares Method for Integrating Economic
Scenarios with Risk Simulations.” In: _SSRN e-Print_.
Rosen, D. and Saunders, D. (2016).“Regress under stress: A simple least-squares method for integrating economic
scenarios with risk simulations.” In: _Journal of Risk Management in Financial Institutions_ 9(4), pp. 391–412.
Rosolia, A. and Osterrieder, J. (2021).“Analyzing Deep Generated Financial Time Series for Various Asset Classes.”
In: _SSRN e-Print_.
Ruenzi, S., Ungeheuer, M., and Weigert, F. (2020).“Joint Extreme events in equity returns and liquidity and their
cross-sectional pricing implications.” In: _Journal of Banking & Finance_ 115, p. 105809.
Sahamkhadam, M. and Stephan, A. (2021).“Portfolio Optimization Based on Forecasting Models Using Vine
Copulas: An Empirical Assessment for the Financial Crisis.” In: _SSRN e-Print_.
Salazar, A., Vergara, L., and Safont, G. (2021).“Generative Adversarial Networks and Markov Random Fields for
oversampling very small training sets.” In: _Expert Systems with Applications_ 163, p. 113819.
Sani, A., Lazaric, A., and Ryabko, D. (2015).“The replacement bootstrap for dependent data.” In: _IEEE Interna-
tional Symposium on Information Theory (ISIT)_. IEEE, pp. 1194–1198.
Sapp, T. R. A. (2017).“Efficient Estimation of Distributional Tail Shape and the Extremal Index with Applications
to Risk Management.” In: _Journal of Mathematical Finance_ 06(04), pp. 626–659.
Sarmas, E., Xidonas, P., and Doukas, H. (2020). _Multicriteria Portfolio Construction with Python_. Springer Inter-
national Publishing.
Sarris, D., Spiliotis, E., and Assimakopoulos, V. (2020).“Exploiting resampling techniques for model selection in
forecasting: an empirical evaluation using out-of-sample tests.” In: _Operational Research_ 20(2), pp. 701–721.
Saxena, D. and Cao, J. (2020).“Generative Adversarial Networks (GANs): Challenges, Solutions, and Future
Directions.” In: _arXiv e-Print_.
Saxena, D. and Cao, J. (2022).“Generative Adversarial Networks (GANs).” In: _ACM Computing Surveys_ 54(3),
pp. 1–42.


Schissler, A. G., Bedrick, E. J., Knudson, A. D., Kozubowski, T. J., Nguyen, T., Petereit, J., Piegorsch, W. W.,
and Tran, D. (2021). “Simulating High-Dimensional Multivariate Data using the bigsimr R Package.” In: _arXiv
e-Print_.
Schneider, P. G. (2020).“Sparse economic scenarios.” In: _SSRN e-Print_.
Schuderer, A., Bromuri, S., and Eekelen, M. van (2021).“Sim-Env: Decoupling OpenAI Gym Environments from
Simulation Models.” In: _arXiv e-Print_.
Schwaab, B., Zhang, X. (, and Lucas, A. (2021).“Modeling Extreme Events: Time-Varying Extreme Tail Shape.”
In: _SSRN e-Print_.
Seabrook, I., Caccioli, F., and Aste, T. (2021).“An Information Filtering approach to stress testing: an application
to FTSE markets.” In: _arXiv e-Print_.
Sebastian, A. and Gebbie, T. (2019).“Systematic Asset Allocation using Flexible Views for South African Markets.”
In: _arXiv e-Print_.
Shah, V. and Shroff, G. (2021). “Forecasting Market Prices using DL with Data Augmentation and Meta-learning:
ARIMA still wins!” In: _arXiv e-Print_.
Sharma, A., Syrgkanis, V., Zhang, C., and Kiciman, E. (2021a). “DoWhy: Addressing Challenges in Expressing and
Validating Causal Assumptions.” In: _arXiv e-Print_.
Sharma, D., Bouchaud, J.-P., Gualdi, S., Tarzia, M., and Zamponi, F. (2021b).“V- U-, L- or W- shaped economic
recovery after Covid-19: Insights from an Agent Based Model.” In: _PLOS ONE_ 16(3). Ed. by S. C. Gherghina,
e0247823.
Sharma, D., Bouchaud, J.-P., Tarzia, M., and Zamponi, F. (2020).“A constraint-satisfaction agent-based model for
the macroeconomy.” In: _arXiv e-Print_.
Shen, Z., Liu, J., He, Y., Zhang, X., Xu, R., Yu, H., and Cui, P. (2021). “Towards Out-Of-Distribution Generaliza-
tion: A Survey.” In: _arXiv e-Print_.
Shi, X., Xu, D., and Zhang, Z. (2022). “Deep Learning Algorithms for Hedging with Frictions.” In: _arXiv e-Print_.
Shi, Y., Li, B., and Du, G. (2021).“Pyramid scheme in stock market: a kind of financial market simulation.” In:
_arXiv e-Print_.
Siddique, A., Hasan, I., and Lynch, D. (2019). _Stress Testing (Second Edition)_. Risk Books. 500 pp.
Siebert, J., Gross, J., and Schroth, C. (2021).“A systematic review of Python packages for time series analysis.”
In: _Engineering Proceedings_ 5(1) (22).
Siew, L. W., Hj, and Ismail, H. B. (2015).“The Impact of Different Economic Scenarios Towards Portfolio Selection
in Enhanced Index Tracking Problem.” In: _Advanced Science Letters_ , pp. 1285–1288.
Silva, A. C. and Ferreira, F. F. (2021).“Surrogate Monte Carlo.” In: _arXiv e-Print_.
Silva, T., Pinheiro, P. R., and Poggi, M. (2017).“A more human-like portfolio optimization approach.” In: _European
Journal of Operational Research_ 256(1), pp. 252–260.
Simos, T. E., Mourtas, S. D., and Katsikis, V. N. (2021).“Time-varying Black–Litterman portfolio optimization
using a bio-inspired approach and neuronets.” In: _Applied Soft Computing_ 112, p. 107767.
Skoglund, J. (2019).“Quantification of model risk in stress testing and scenario analysis.” In: _Journal of Risk Model
Validation_ 13(1), pp. 1–23.
Smith, K. E. and Smith, A. O. (2020).“Conditional GAN for timeseries generation.” In: _arXiv e-Print_.
Snow, D. (2019).“Machine learning in asset management.” In: _SSRN e-Print_.
Snow, D. (2020a).“DataGene: A Framework for Dataset Similarity.” In: _SSRN e-Print_.
Snow, D. (2020b).“DeltaPy: A Framework for Tabular Data Augmentation in Python.” In: _SSRN e-Print_.
Snow, D. (2020c).“Machine Learning in Asset Management - Part 2: Portfolio Construction - Weight Optimization.”
In: _The Journal of Financial Data Science_ 2 (2), pp. 17–24.
Snow, D. (2020d).“Machine Learning in Asset Management Part 1: Portfolio Construction Trading Strategies.” In:
_The Journal of Financial Data Science_ 2(1) (1), pp. 10–23.
Staum, J. (2009).“Monte Carlo Computation in Finance.” In: _Monte Carlo and Quasi-Monte Carlo Methods 2008_.
Ed. by P. L’ Ecuyer and A. B. Owen. Springer Berlin Heidelberg, pp. 19–42.
Steehouwer, H. (2014).“Ex-ante risk management with scenarios.” In: _CFA Society Switzerland Series_.
Steehouwer, H. and Slater, A. (2010).“Macroeconomic Scenarios: A Frequency Domain Approach.” In: _SSRN e-
Print_.
Stephanovitch, A., Tanielian, U., Cadre, B., Klutchnikoff, N., and Biau, G. (2022). “Optimal 1-Wasserstein Distance
for WGANs.” In: _arXiv e-Print_.


Sun, H., Deng, Z., Chen, H., and Parkes, D. C. (2020).“Decision-Aware Conditional GANs for Time Series Data.”
In: _arXiv e-Print_.
Tadayon, M. and Pottie, G. (2020).“tsBNgen: A Python Library to Generate Time Series Data from an Arbitrary
Dynamic Bayesian Network Structure.” In: _arXiv e-Print_.
Takahashi, S., Chen, Y., and Tanaka-Ishii, K. (2019).“Modeling financial time-series with generative adversarial
networks.” In: _Physica A: Statistical Mechanics and its Applications_ 527, p. 121261.
Tan, V. and Zohren, S. (2021).“Large Non-Stationary Noisy Covariance Matrices: A Cross-Validation Approach.”
In: _SSRN e-Print_.
Tanaka, K. (2017).“Forecasting scenarios from the perspective of a reverse stress test using second-order cone
programming.” In: _Journal of Risk Model Validation_ 11(2), pp. 1–21.
Tatsat, H., Puri, S., and Lookabaugh, B. (2020). _Machine Learning and Data Science Blueprints for Finance: From
Building Trading Strategies to Robo-Advisors Using Python_. O’Reilly. 400 pp.
Taylor, L. and Nitschke, G. (2017).“Improving Deep Learning using Generic Data Augmentation.” In: _arXiv e-Print_.
ter Ellen, S., Hommes, C. H., and Zwinkels, R. C. J. (2021).“Comparing behavioural heterogeneity across asset
classes.” In: _Journal of Economic Behavior & Organization_.
Thiem, T. N., Kemeth, F. P., Bertalan, T., Laing, C. R., and Kevrekidis, I. G. (2021).“Global and Local Reduced
Models for Interacting, Heterogeneous Agents.” In: _arXiv e-Print_.
Traccucci, P., Dumontier, L., Garchery, G., and Jacot, B. (2019).“A Triptych Approach for Reverse Stress Testing
of Complex Portfolios.” In: _Risk (Cutting Edge)_.
Tran, T., Pham, T., Carneiro, G., Palmer, L., and Reid, I. (2017).“A Bayesian Data Augmentation Approach for
Learning Deep Models.” In: _arXiv e-Print_.
Trimborn, T., Otte, P., Cramer, S., Beikirch, M., Pabich, E., and Frank, M. (2020).“SABCEMM: A Simulator for
Agent-Based Computational Economic Market Models.” In: _Computational Economics_ 55(2), pp. 707–744.
Trucı́os, C., Mazzeu, J. H. G., Hallin, M., Hotta, L. K., Pereira, P. L. V., and Zevallos, M. (2021).“Forecasting
Conditional Covariance Matrices in High-Dimensional Time Series: a General Dynamic Factor Approach.” In:
_Journal of Business & Economic Statistics_ , pp. 1–35.
Tsamardinos, I., Greasidou, E., and Borboudakis, G. (2018).“Bootstrapping the out-of-sample predictions for
efficient and accurate cross-validation.” In: _Machine Learning_ , pp. 1–28.
Tsanakas, A. and Zhu, R. (2021).“Copula model selection using image recognition.” In: _SSRN e-Print_.
Tuck, J., Barratt, S., and Boyd, S. (2022).“Portfolio Construction Using Stratified Models.” In: _Machine Learning
in Financial Markets: A guide to contemporary practices_. Ed. by A. Capponi and C.-A. Lehalle. Cambridge
University Press.
Ungolo, F., Sherris, M., and Zhou, Y. (2021).“affine_mortality: A Github repository for estimation, analysis, and
projection of affine mortality models.” In: _SSRN e-Print_.
Vamossy, D. and Skog, R. (2021). “EmTract: Investor Emotions and Market Behavior.” In: _arXiv e-Print_.
van Beek, M. (2020).“Consistent Calibration of Economic Scenario Generators: The Case for Conditional Simula-
tion.” In: _arXiv e-Print_.
Vandin, A., Giachini, D., Lamperti, F., and Chiaromonte, F. (2021).“Automated and Distributed Statistical Anal-
ysis of Economic Agent-Based Models.” In: _arXiv e-Print_.
Vanini, P. (2020).“Asset Management.” In: _SSRN e-Print_.
Vieira, A. (2020).“Generating Synthetic Sequential Data using GANs.” In: _Towards AI_.
Vinod, H. D. (2012).“Constructing Scenarios of Time Heterogeneous Series for Stress Testing.” In: _SSRN e-Print_.
Vinod, H. D. (2021).“R Package GeneralCorr Functions for Portfolio Choice.” In: _SSRN e-Print_.
Volpi, R., Namkoong, H., Sener, O., Duchi, J., Murino, V., and Savarese, S. (2018).“Generalizing to Unseen Domains
via Adversarial Data Augmentation.” In: _arXiv e-Print_.
Waller, N. G. (2020).“Generating Correlation Matrices With Specified Eigenvalues Using the Method of Alternating
Projections.” In: _The American Statistician_ 74(1), pp. 21–28.
Wang, B., Xu, H., Zhang, J., Chen, C., Fang, X., Xu, Y., Kang, N., Hong, L., Jiang, C., Cai, X., Li, J., Zhou, F.,
Li, Y., Liu, Z., Chen, X., Han, K., Shu, H., Song, D., Wang, Y., Zhang, W., Xu, C., Li, Z., Liu, W., and Zhang,
T. (2020a).“VEGA: Towards an End-to-End Configurable AutoML Pipeline.” In: _arXiv e-Print_.
Wang, H. and Tu, W. (2014).“Bootstrap methods: the classical theory and recent development.” In: _Wiley statsref:
statistics reference online_. Ed. by N. Balakrishnan, T. Colton, B. Everitt, W. Piegorsch, F. Ruggeri, and J. L.
Teugels. Chichester, UK: John Wiley & Sons, Ltd, pp. 1–12.


Wang, L., Ma, F., and Liu, G. (2020b).“Forecasting stock volatility in the presence of extreme shocks: Short-term
and long-term effects.” In: _Journal of Forecasting_ 39(5), pp. 797–810.
Wang, R. (2021). “Discriminating modelling approaches for Point in Time Economic Scenario Generation.” In: _arXiv
e-Print_.
Wang, Y., Polson, N. G., and Sokolov, V. O. (2019).“Scalable Data Augmentation for Deep Learning.” In: _arXiv
e-Print_.
Wang, Y., Huang, G., Song, S., Pan, X., Xia, Y., and Wu, C. (2020c).“Regularizing Deep Networks with Semantic
Data Augmentation.” In: _arXiv e-Print_.
Wen, Q., Sun, L., Yang, F., Song, X., Gao, J., Wang, X., and Xu, H. (2021).“Time Series Data Augmentation for
Deep Learning: A Survey.” In: _Proceedings of the Thirtieth IJCAI Conference_.
Westphal, R. and Sornette, D. (2020).“How Market Intervention Can Prevent Bubbles and Crashes.” In: _SSRN
e-Print_.
Wiese, M., Knobloch, R., Korn, R., and Kretschmer, P. (2020).“Quant GANs: deep generation of financial time
series.” In: _Quantitative Finance_ 20(9), pp. 1419–1440.
Wood, M. (2018).“How sure are we? Two approaches to statistical inference.” In: _arXiv e-Print_.
Xie, Q., Dai, Z., Hovy, E., Luong, M.-T., and Le, Q. V. (2019).“Unsupervised Data Augmentation.” In: _arXiv
e-Print_.
Xu, H., Wang, J., Li, H., Ouyang, D., and Shao, J. (2021).“Unsupervised meta-learning for few-shot learning.” In:
_Pattern Recognition_ 116, p. 107951.
Xu, L., Gotwalt, C., Hong, Y., King, C. B., and Meeker, W. Q. (2020).“Applications of the Fractional-Random-
Weight Bootstrap.” In: _The American Statistician_ , pp. 1–21.
Yacoby, Y., Pan, W., and Doshi-Velez, F. (2020).“Characterizing and Avoiding Problematic Global Optima of
Variational Autoencoders.” In: _Proceedings of Machine Learning Research_ , pp. 1–17.
Yang, Y., UY, M. C. S., and Huang, A. (2020). “FinBERT: A Pretrained Language Model for Financial Commu-
nications.” In: _arXiv e-Print_.
Yao, H., Jia, X., Kumar, V., and Li, Z. (2020).“Learning with Small Data.” In: _Proceedings of the 26th ACM
SIGKDD International Conference on Knowledge Discovery & Data Mining_. ACM.
Ye, R. and Dai, Q. (2021).“Implementing transfer learning across different datasets for time series forecasting.” In:
_Pattern Recognition_ 109, p. 107617.
Yeh, C.-C. M. (2020).“Towards a Near Universal Time Series Data Mining Tool: Introducing the Matrix Profile.”
In: _arXiv e-Print_.
Yeh, C.-C. M., Zhu, Y., Ulanova, L., Begum, N., Ding, Y., Dau, H. A., Zimmerman, Z., Silva, D. F., Mueen, A., and
Keogh, E. (2017).“Time series joins, motifs, discords and shapelets: a unifying view that exploits the matrix
profile.” In: _Data Mining and Knowledge Discovery_ 32(1), pp. 1–41.
Yılmaz, A., Kara, M., and Ozdemir, O. (2021).“Comparison of different estimation methods for extreme value
distribution.” In: _Journal of Applied Statistics_ 48(13-15), pp. 2259–2284.
Yoon, J., Jarrett, D., and van der Schaar, M. (2019).“Time-series Generative Adversarial Networks.” In: _NIPS_.
NIPS.
Yu, L., Hardle, W. K., Borke, L., and Benschop, T. (2020a).“An AI approach to measuring financial risk.” In:
_SSRN e-Print_.
Yu, P. L. H., Ng, F. C., and Ting, J. K. W. (2020b).“Adjusting covariance matrix for risk management.” In:
_Quantitative Finance_ 20(10), pp. 1681–1699.
Yu, R. (2020).“A Tutorial on VAEs: From Bayes’ Rule to Lossless Compression.” In: _arXiv e-Print_.
Yuan, J. and Yuan, X. (2021).“A Monte Carlo synthetic sample based performance evaluation method for covariance
matrix estimators.” In: _Applied Economics Letters_.
Zhang, J. (2020).“Modern Monte Carlo methods for efficient uncertainty quantification and propagation: A survey.”
In: _WIREs Computational Statistics_ 13(5).
Zhang, S. (2018).“Optimal Retirement Planning: Scenario Generation, Preferences, and Objectives.” PhD thesis.
University of Waterloo.
Zhang, X., Wang, Z., Liu, D., and Ling, Q. (2018). “DADA: Deep Adversarial Data Augmentation for Extremely
Low Data Regime Classification.” In: _arXiv e-Print_.
Zhao, L. (2022).“Event Prediction in the Big Data Era.” In: _ACM Computing Surveys_ 54(5), pp. 1–37.
Zhu, Y., Mariani, G., and Li, J. (2021).“Pagan: Portfolio Analysis with Generative Adversarial Networks.” In:
_SSRN e-Print_.


Zhu, Y., Imamura, M., Nikovski, D., and Keogh, E. (2018).“Time series chains: A novel tool for time series data
mining.” In: _Proceedings of the Twenty-Seventh International Joint Conference on Artificial Intelligence_. Ed. by
J. Lang. California: International Joint Conferences on Artificial Intelligence Organization, pp. 5414–5418.
Zhu, Y., Imamura, M., Nikovski, D., and Keogh, E. (2019).“Introducing time series chains: a new primitive for
time series data mining.” In: _Knowledge and Information Systems_ 60, pp. 1135–1161.
Ziyin, L., Minami, K., and Imajo, K. (2021).“What Data Augmentation Do We Need for Deep-Learning-Based
Finance?” In: _arXiv e-Print_.
Zorn, J. (2019).“Panic-aware portfolio optimization.” In: _Journal of Asset Management_.


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
    Introduction to Portfolio Construction and Analysis with Python
    Advanced Portfolio Construction and Analysis with Python
    Python and Machine Learning for Asset Management
    Python and Machine Learning for Asset Management with Alternative Data Sets
- Machine Learning and Reinforcement Learning in Finance Specialization
    Guided Tour of Machine Learning in Finance
    Fundamentals of Machine Learning in Finance
    Reinforcement Learning in Finance
    Overview of Advanced Methods of Reinforcement Learning in Finance
- Investment Management Specialization
    Understanding Financial Markets
    Meeting Investors’ Goals
    Portfolio and Risk Management
    Securing Investment Returns in the Long Run
    Planning your Client’s Wealth over a 5-year Horizon
- Investment and Portfolio Management Specialization
    Global Financial Markets and Instruments
    Portfolio Selection and Risk Management
    Biases and Portfolio Selection
    Investment Strategies and Portfolio Analysis
    Build a Winning Investment Portfolio


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


