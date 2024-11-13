# Machine learning (and more) applied to market regimes, changepoints,

# bubbles and crashes in quantitative wealth and investment management

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
1.1 Market states inQWIM........................................... 4
1.2 Structural breaks: market regimes..................................... 5
1.3 Structural breaks: bubbles and crashes................................... 5
1.4 Structural breaks: changepoints....................................... 5

**2 Relevant references 6**
2.1 Main references................................................ 6
2.2 Comprehensive list of references....................................... 7
2.2.1 Regime-based asset allocation, portfolio construction and investment strategies........ 7
2.2.2 Number of market regimes..................................... 9
2.2.3 Market states, regimes, changepoints and structural breaks of time series within context of
QWIM................................................. 9
2.2.4 Market states, regimes, changepoints and structural breaks of time series........... 11
2.2.5 Detection and usage of bubbles, crashes and business cycles within context of QWIM.... 12
2.2.6 Detection and usage of bubbles, crashes and business cycles................... 13
2.2.7 Forecasting under data regimes................................... 14
2.2.8 Numerical methods, models and their implementations to model and analyze data regimes.. 15



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

There is much evidence that crash and bubble periods display much different patterns than normal markets, sug-
gesting that forecasting models (and investing approaches) ought to be based on multiple regimes.
It was shown that asset performance over long time periods can be separated into distinctive periods, called
regimes, which display common characteristics. Regime-based asset allocation has been shown to add value over
rebalancing to static weights and, in particular, reduce potential drawdowns by reacting to changes in market
conditions. regime based asset allocation can effectively respond to changes in financial regimes at the portfolio
level, in an effort to provide better long-term results than more static approaches can offer.
Baltas and Karyampas (“Forecasting the equity risk premium: The importance of regime-dependent evaluation,”
2018):
”Is superior econometric predictability across the business cycle synonymous with predictability at all times?”
It appears that recently introduced forecasting models for equity risk premium ERP, which have been shown to
generate econometrically superior ERP forecasts, have forecasting ability which is regime-dependent. They give rise
to significant relative losses during market downturns, when it matters the most for asset allocators to retain assets
and their client base intact. Conversely, any economic benefit occurring during market upswings is diminished for
high risk-averse and leverage-constrained investors.

### 1.1 Market states in QWIM

It was observed empirically that there are two separate market states:

- low uncertainty (relatively stable and resilient) market
- high uncertainty (relatively chaotic and fragile) market
Markets in **“low uncertainty”** state:
- statistically well behaved
- can be modeled using standard statistical tools
- volatility is stable and low
- correlations relatively stable
- tail events (≥3 std deviations in either direction) quite rare.
Markets in **”high uncertainty”** state:
- not statistically well behaved
- vols and correlations change significantly on regular basis
- Tail events happen with much more regularity
To account for the two market states, practitioners use a relatively similar concept of **”risk on, risk off”** :
The **“high uncertainty”** state can incorporate multiple instances and multiple types of significant changes in
time series:
- market regimes
- changepoints
- bubbles and crashes


### 1.2 Structural breaks: market regimes

Regime changes, some transitory, some recurring (recessions versus expansions) some permanent (structural breaks),
are prevalent across a wide range of financial markets and in behavior of many macro variables. Examples of regimes
considered in academia and/or practitioners:

- bull vs. bear market regimes
- inflationary vs. recessionary regimes
- high vs. low volatility regimes
- mean reverting vs. trending regimes
Regime shifts are challenging for investors because they cause portfolio performance, risk and behavior to depart
significantly from ranges implied by long-term averages of means and covariances. Regime-based asset allocation
was shown to deliver improved performance and risk profile
Goof performance of investment strategies greatly enhanced with introduction of regime switching modelsRSMs
.RSMs characterize market states using estimates of parameters of some underlying model, and use a transition
matrix to quantify probability of moving from one state to another.
MLmay be effective at detecting change (even in chaotic system), for example through robust anomaly detection.
It can be enhanced to compute probability of observation in previously observed “market regimes” (defined as
clusters inML). Thus clustering algorithms can identify regimes in datasets. What they have in common with
regular regime switching models is ability of producing probabilities of “switching” into another regime. MLcan
also feed on large amounts of data to detect preconditions of a break

### 1.3 Structural breaks: bubbles and crashes

Chaotic systems of the real world are comparable to stock market indices evolution.Llog-periodic power law sin-
gularity (LPPLS) model captures well bubbles and crashes LPPLS framework successfully captures, ex-ante, most
prominent bubbles across different time scales (Black Monday, Dot-com, and Subprime Crisis).

### 1.4 Structural breaks: changepoints

Change point detection (CPD) is the problem of finding abrupt changes in data when a property of the time series
changes. Segmentation, edge detection, event detection, and anomaly detection are similar concepts withinML
space.
Traditional changepoint detection methods only look for statistically-detectable boundaries that are defined as
abrupt variations in the generative parameters of a data sequence.. However, it is observed that breakpoints occur
on more subtle boundaries non-trivial to detect with these statistical methods, but detectable using deep learning


## 2 Relevant references

### 2.1 Main references

List of references:
Akioyamen et al. (“A Hybrid Learning Approach to Detecting Regime Switches in Financial Markets,” 2021)
Bae et al. (“Dynamic asset allocation for varied financial markets under regime switching framework,” 2014)
Baitinger and Flegel (“The better turbulence index? Forecasting adverse financial markets regimes with persis-
tent homology,” 2021)
Benhamou et al. (“Explainable AI (XAI) Models Applied to Planning in Financial Markets,” 2021)
Benhamou et al. (“Detecting and Adapting to Crisis Pattern with Context Based Deep Reinforcement Learning,”
2021)
Bhansali and Holdom (“Good States, Bad States: What Do Options Tell Us About Schizophrenic Behavior of
Mr. Market and What Can We Do About It?” 2021)
Bilokon et al. (“Market regime classification with signatures,” 2021)
Botte and Bao ( _A Machine Learning Approach to Regime Modeling_ , 2021)
Bucci and Ciciretti (“Market Regime Detection via Realized Covariances: A Comparison between Unsupervised
Learning and Nonlinear Models,” 2021)
Campani et al. (“Optimal portfolio strategies in the presence of regimes in asset returns,” 2021)
Chalkis et al. (“Modeling of crisis periods in stock markets,” 2021)
Clacher et al. (“A Practical Guide to Regime Switching in Financial Economics,” 2015)
Costa and Kwon (“Risk parity portfolio optimization under a Markov regime-switching framework,” 2019)
Costa and Kwon (“A regime-switching factor model for mean-variance optimization,” 2020)
Dai et al. (“Robo-Advising: A Dynamic Mean-Variance Approach,” 2021)
Dal Pra et al. (“Regime Shifts in Excess Stock Return Predictability: An Out-of-Sample Portfolio Analysis,”
2018)
Das et al. (“Optimal Goals-Based Investment Strategies For Switching Between Bull and Bear Markets,” 2021)
Das et al. (“Optimal Goals-Based Investment Strategies For Switching Between Bull and Bear Markets,” 2022)
Demos and Sornette (“Birth or burst of financial bubbles: which one is easier to diagnose?” 2017)
Filimonov et al. (“Modified profile likelihood inference and interval forecast of the burst of financial bubbles,”
2017)
Fischer and Murg (“A combined regime-switching and Black Litterman model for optimal asset allocation,”
2015)
Flint et al. (“Defining and measuring portfolio diversification,” 2021)
Flint and du Plooy (“Extending risk budgeting for market regimes and quantile factor models,” 2018)
Fons et al. (“A novel dynamic asset allocation system using Feature Saliency Hidden Markov models for smart
beta investing,” 2021)
Gatumel and Ielpo (“The Number of Regimes Across Asset Returns: Identification and Economic Value,” 2014)
Gu and Mulvey (“Factor Momentum and Regime-Switching Overlay Strategy,” 2021)
Hallac et al. (“Greedy Gaussian segmentation of multivariate time series,” 2019)
Harvey et al. (“Real-Time Detection of Regimes of Predictability in the U.S. Equity Premium,” 2021)
Hao (“A Regime-Aware Agent-Based Framework for Financial Planning,” 2019)
Heckens and Guhr (“A new attempt to identify long-term precursors for endogenous financial crises in the market
correlation structures,” 2022)
Horvath et al. (“Clustering Market Regimes Using the Wasserstein Distance,” 2021)
Jacquier et al. (“Market regime classification with signatures,” 2021)
Kaya (“Managing ambiguity in asset allocation,” 2017)
Kelliher et al. (“A Novel Approach to Risk Parity: Diversification across Risk Factors and Market Regimes,”
2022)
Kunjal et al. (“The performance of South African exchange traded funds under changing market conditions,”
2021)
Lattanzi and Leonelli (“A changepoint approach for the identification of financial extreme regimes,” 2019)
Lezmi et al. (“Portfolio Allocation with Skewness Risk: A Practical Guide,” 2019)
Li and Mulvey (“Portfolio Optimization Under Regime Switching and Transaction Costs: Combining Neural
Networks and Dynamic Programs,” 2021)


Li and Zakamulin (“Stock volatility predictability in bull and bear markets,” 2020)
Liu et al. (“Predicting financial crises with machine learning methods,” 2022)
McIndoe (“A Data Driven Approach to Market Regime Classification,” 2020)
Messer (“Bivariate change point detection: joint detection of changes in expectation and variance,” 2021)
Mizuno et al. (“Detecting Stock Market Bubbles Based on the Cross-Sectional Dispersion of Stock Prices,” 2020)
Nystrup et al. (“Dynamic Allocation or Diversification: A Regime-Based Approach to Multiple Assets,” 2018)
Nystrup et al. (“Dynamic portfolio optimization across hidden market regimes,” 2018)
Nystrup et al. (“Learning hidden Markov models with persistent states by penalizing jumps,” 2020)
Nystrup et al. (“Detecting change points in VIX and S&P 500: A new approach to dynamic asset allocation,”
2016)
Nystrup et al. (“Regime-Based Versus Static Asset Allocation: Letting the Data Speak,” 2015)
Oprisor and Kwon (“Multi-Period Portfolio Optimization with Investor Views under Regime Switching,” 2021)
Pharasi et al. (“Market states: A new understanding,” 2020)
Procacci and Aste (“Forecasting market states,” 2019)
Schatz (“Financial Modeling of Bubbles and Crashes,” 2020)
Shi et al. (“A Comparison of Single and Multiple Changepoint Techniques for Time Series Data,” 2021)
Simonian (“Mixed Ag: A Regime-Based Analysis of Multi-Asset Agriculture Portfolios,” 2020)
Simonian and Wu (“Factors in Time: Fine-Tuning Hedge Fund Replication,” 2019)
Sornette et al. (“Can We Use Volatility to Diagnose Financial Bubbles? Lessons from 40 Historical Bubbles,”
2017)
Stillwagon and Sullivan (“Markov switching in exchange rate models: will more regimes help?” 2020)
Sueppel ( _Classifying market regimes_ , 2021)
Tajeuna et al. (“Modeling Regime Shifts in Multiple Time Series,” 2022)
Tu (“Is Regime Switching in Stock Returns Important in Portfolio Decisions?” 2010)
Uysal and Mulvey (“A Machine Learning Approach in Regime-Switching Risk Parity Portfolios,” 2021)
Wheatley et al. (“Are bitcoin bubbles predictable? combining a generalized metcalfe’s law and the LPPLS
model,” 2018)
Zakamulin (“Not All Bull and Bear Markets Are Alike: Insights From a Five-State Hidden Semi-Markov Model,”
2020)
Zhao and Sornette (“Bubbles for Fama from Sornette,” 2022)

### 2.2 Comprehensive list of references

**2.2.1 Regime-based asset allocation, portfolio construction and investment strategies**
List of references:
Ahmad and Sehgal (“Regime shifts and volatility in BRIICKS stock markets: an asset allocation perspective,”
2015)
Ahmad et al. (“Regime dependent dynamics and European stock markets: Is asset allocation really possible?”
2015)
Ang and Bekaert (“How do Regimes Affect Asset Allocation,” 2004)
Bae et al. (“Dynamic asset allocation for varied financial markets under regime switching framework,” 2014)
Berger and Gencay (“Short-run wavelet-based covariance regimes for applied portfolio management,” 2020)
Bhansali and Holdom (“Good States, Bad States: What Do Options Tell Us About Schizophrenic Behavior of
Mr. Market and What Can We Do About It?” 2021)
Blin et al. (“A Macro Risk-Based Approach to Alternative Risk Premia Allocation,” 2017)
Blitz and Van Vliet (“Dynamic Strategic Asset Allocation: Risk and Return Across Economic Regimes,” 2009)
BNYMellon Research ( _Great expectations: regime based asset allocation seeks higher return, lower drawdowns_ ,
2013)
Bradrania and Neghab (“State-dependent asset allocation using neural networks,” 2022)
Campani et al. (“Optimal portfolio strategies in the presence of regimes in asset returns,” 2021)
Chen and Yang (“Markowitz’s Mean-Variance Asset-Liability Management with Regime Switching: A Multi-
Period Model,” 2011)
Cheng et al. (“Trending Fast and Slow,” 2021)
Costa and Kwon (“Risk parity portfolio optimization under a Markov regime-switching framework,” 2019)


Dai et al. (“Robo-Advising: A Dynamic Mean-Variance Approach,” 2021)
Dapena et al. (“Risk On-Risk Off: A Regime Switching Model for Active Portfolio Management,” 2020)
Das et al. (“Optimal Goals-Based Investment Strategies For Switching Between Bull and Bear Markets,” 2022)
Dou et al. (“Cross-region and cross-sector asset allocation with regimes,” 2014)
Elkamhi et al. (“Portfolio Tilts using Views on Macroeconomic Regimes,” 2021)
Erlwein et al. (“HMM based scenario generation for an investment optimisation problem,” 2012)
Erlwein-Sayer et al. (“Portfolio Strategies and Estimation in a Hidden Markov Model Using State Dependent,
State Independent or No Correlation,” 2016)
Fischer and Murg (“A combined regime-switching and Black Litterman model for optimal asset allocation,”
2015)
Flint and Mare (“Regime-Based Tactical Allocation for Equity Factors and Balanced Portfolios,” 2019)
Flint and du Plooy (“Extending risk budgeting for market regimes and quantile factor models,” 2018)
Fons et al. (“A novel dynamic asset allocation system using Feature Saliency Hidden Markov models for smart
beta investing,” 2021)
Gkatzilakis and Sivasubramanian (“Active Allocation of Smart Beta Indices based on Factor Timing and Regime
Switching,” 2014)
Gu and Mulvey (“Factor Momentum and Regime-Switching Overlay Strategy,” 2021)
Guidolin and Timmermann (“International asset allocation under regime switching, skew, and kurtosis prefer-
ences,” 2008)
Guidolin (“Markov Switching in Portfolio Choice and Asset Pricing Models: A Survey,” 2011)
Hu et al. (“Mean variance asset liability management with regime switching,” 2022)
Iqbal (“Application of Regime Switching and Random Matrix Theory for Portfolio Optimization,” 2018)
James (“Evolutionary correlation, regime switching, spectral dynamics and optimal trading strategies for cryp-
tocurrencies and equities,” 2021)
Jiang et al. (“International Asset Allocation with Regime Switching: Evidence from the ETFs,” 2015)
Kelliher et al. (“A Novel Approach to Risk Parity: Diversification across Risk Factors and Market Regimes,”
2022)
Kim et al. (“Global Asset Allocation Strategy Using a Hidden Markov Model,” 2019)
Kritzman et al. (“Regime Shifts: Implications for Dynamic Strategies,” 2012)
Kunjal et al. (“The performance of South African exchange traded funds under changing market conditions,”
2021)
Lezmi et al. (“Portfolio Allocation with Skewness Risk: A Practical Guide,” 2019)
Li (“Risk of investing in volatility products: A regime-switching approach,” 2021)
Li and Mulvey (“Portfolio Optimization Under Regime Switching and Transaction Costs: Combining Neural
Networks and Dynamic Programs,” 2021)
Liszewski (“Asset allocation under multiple regimes,” 2016)
Nystrup et al. (“Dynamic portfolio optimization across hidden market regimes,” 2018)
Nystrup et al. (“Regime-Based Versus Static Asset Allocation: Letting the Data Speak,” 2015)
Nystrup et al. (“Dynamic Allocation or Diversification: A Regime-Based Approach to Multiple Assets,” 2018)
Oliveira and Valls Pereira (“Asset Allocation With Markovian Regime Switching: Efficient Frontier and Tangent
Portfolio With Regime Switching,” 2018)
Oprisor and Kwon (“Multi-Period Portfolio Optimization with Investor Views under Regime Switching,” 2021)
Reus and Mulvey (“Dynamic allocations for currency futures under switching regimes signals,” 2016)
Scherer and Apel (“Business cycle-related timing of alternative risk premia strategies,” 2020)
Seidl (“Markowitz versus Regime Switching: An Empirical Approach,” 2012)
Sharaiha and Johansson (“The state-dependent time variation in the value premium,” 2014)
Sheikh and Sun (“Regime Change: Implications of Macroeconomic Shifts on Asset Class and Portfolio Perfor-
mance,” 2012)
Simonian (“Mixed Ag: A Regime-Based Analysis of Multi-Asset Agriculture Portfolios,” 2020)
SSgA Research ( _Optimizing asset allocations to market regimes_ , 2015)
Stillwagon and Sullivan (“Markov switching in exchange rate models: will more regimes help?” 2020)
Tachibana (“Flight-to-quality in the stock-bond return relation: a regime-switching copula approach,” 2020)
van Vliet and Blitz (“Dynamic strategic asset allocation: Risk and return across the business cycle,” 2011)


Vo and Maurer (“Dynamic Asset Allocation under Regime Switching, Predictability and Parameter Uncertainty,”
2013)
Wang and Hsieh (“Unraveling S&P500 stock volatility and networks – An encoding-and-decoding approach,”
2021)
Wood et al. (“Trading with the Momentum Transformer: An Intelligent and Interpretable Architecture,” 2022)

**2.2.2 Number of market regimes**
List of references:
Gatumel and Ielpo (“The Number of Regimes Across Asset Returns: Identification and Economic Value,” 2014)
Horvath et al. (“Clustering Market Regimes Using the Wasserstein Distance,” 2021)
Kasahara and Shimotsu (“Testing the Number of Regimes in Markov Regime Switching Models,” 2017)
Ma et al. (“Portfolio optimization model with regime-switching risk factors for sector exchange traded funds,”
2011)
Massacci (“Multivariate Regime Switching Model with Flexible Threshold Variable,” 2014)
Nystrup et al. (“Detecting change points in VIX and S&P 500: A new approach to dynamic asset allocation,”
2016)
Prakash et al. (“Structural Clustering of Volatility Regimes for Dynamic Trading Strategies,” 2021)
Stillwagon and Sullivan (“Markov switching in exchange rate models: will more regimes help?” 2020)
Zakamulin (“Not All Bull and Bear Markets Are Alike: Insights From a Five-State Hidden Semi-Markov Model,”
2020)

**2.2.3 Market states, regimes, changepoints and structural breaks of time series within context of
QWIM**
List of references:
Ahelegbey et al. (“Modeling Turning Points In Global Equity Market,” 2020)
Akioyamen et al. (“A Hybrid Learning Approach to Detecting Regime Switches in Financial Markets,” 2021)
Alberico et al. (“Regime identification for sovereign bond portfolio construction,” 2018)
Ang and Timmermann (“Regime Changes and Financial Markets,” 2012)
Angelini et al. (“Uncertainty across volatility regimes,” 2019)
Arago and Salvador (“Non-linear Tradeoff between Risk and Return: A Regime-switching Multi-factor Frame-
work,” 2013)
Bae et al. (“Dynamic asset allocation for varied financial markets under regime switching framework,” 2014)
Baitinger and Flegel (“The better turbulence index? Forecasting adverse financial markets regimes with persis-
tent homology,” 2021)
Balcerak and Schmelzer (“Constructing trading strategy ensembles by classifying market states,” 2020)
Baltas and Karyampas (“Forecasting the Equity Risk Premium: The Importance of Regime-Dependent Evalu-
ation,” 2020)
Barkai et al. (“A Cryptocurrency Risk-Return Analysis for Bull and Bear Regimes,” 2021)
Benhamou et al. (“Explainable AI (XAI) Models Applied to Planning in Financial Markets,” 2021)
Benhamou et al. (“Detecting and Adapting to Crisis Pattern with Context Based Deep Reinforcement Learning,”
2021)
Benhamou et al. (“Planning in Financial Markets in Presence of Spikes: Using Machine Learning GBDT,” 2021)
Bernhart et al. (“Asset Correlations in Turbulent Markets and the Impact of Different Regimes on Asset Man-
agement,” 2011)
Billio et al. (“Evaluation of Regime Switching Models for Real-Time Business Cycle Analysis of the Euro Area,”
2013)
Bilokon et al. (“Market regime classification with signatures,” 2021)
Botte and Bao ( _A Machine Learning Approach to Regime Modeling_ , 2021)
Bucci and Ciciretti (“Market Regime Detection via Realized Covariances: A Comparison between Unsupervised
Learning and Nonlinear Models,” 2021)
Campani et al. (“Optimal portfolio strategies in the presence of regimes in asset returns,” 2021)
Chalkis et al. (“Modeling of crisis periods in stock markets,” 2021)


Chen and Tsang ( _Detecting regime change in computational finance: data science, machine learning and algo-
rithmic trading_ , 2020)
Chen et al. (“Clustering commodity markets in space and time: Clarifying returns, volatility, and trading regimes
through unsupervised machine learning,” 2021)
Clacher et al. (“A Practical Guide to Regime Switching in Financial Economics,” 2015)
Corbelli et al. (“Investigating Optimal Regimes for Prediction in the Stock Market,” 2020)
Costa and Kwon (“Risk parity portfolio optimization under a Markov regime-switching framework,” 2019)
Costa and Kwon (“A regime-switching factor model for mean-variance optimization,” 2020)
Dal Pra et al. (“Regime Shifts in Excess Stock Return Predictability: An Out-of-Sample Portfolio Analysis,”
2018)
Das et al. (“Optimal Goals-Based Investment Strategies For Switching Between Bull and Bear Markets,” 2021)
Dias et al. (“Clustering financial time series: New insights from an extended hidden Markov model,” 2015)
Duprey and Klaus (“How to Predict Financial Stress? An Assessment of Markov Switching Models,” 2017)
Edirisinghe and Zhao (“Smart Indexing Under Regime-Switching Economic States,” 2020)
Elouai et al. (“Bubbles and Regimes: Two Complementary Approaches,” 2013)
Endres and Stubinger (“A flexible regime switching model with pairs trading application to the S&P 500 high-
frequency stock returns,” 2019)
Filimonov et al. (“Modified profile likelihood inference and interval forecast of the burst of financial bubbles,”
2017)
Flint et al. (“Defining and measuring portfolio diversification,” 2021)
Fischer and Murg (“A combined regime-switching and Black Litterman model for optimal asset allocation,”
2015)
Fulop and Yu (“Bayesian analysis of bubbles in asset prices,” 2017)
Gallagher et al. (“Using Smooth Transition Regressions to Model Risk Regimes,” 2020)
Gao et al. (“Long memory or regime switching in volatility? Evidence from high-frequency returns on the U.S.
stock indices,” 2018)
Gatumel and Ielpo (“The Number of Regimes Across Asset Returns: Identification and Economic Value,” 2014)
Glasserman et al. (“Dynamic information regimes in financial markets,” 2021)
Haase and Neuenkirch (“Predictability of Bull and Bear Markets: A New Look at Forecasting Stock Market
Regimes (and Returns) in the U.S.,” 2021)
Hao (“A Regime-Aware Agent-Based Framework for Financial Planning,” 2019)
Harvey et al. (“Real-Time Detection of Regimes of Predictability in the U.S. Equity Premium,” 2021)
Hauptmann et al. (“Forecasting market turbulence using regime-switching models,” 2014)
Heckens and Guhr (“A new attempt to identify long-term precursors for endogenous financial crises in the market
correlation structures,” 2022)
Hollstein et al. (“How Robust are Empirical Factor Models to the Choice of Breakpoints?” 2022)
Horvath et al. (“Clustering Market Regimes Using the Wasserstein Distance,” 2021)
Huang et al. (“Forecasting Stock Returns in Good and Bad Times: The Role of Market States,” 2017)
Jacquier et al. (“Market regime classification with signatures,” 2021)
Kaihatsu and Nakajima ( _Has Trend Inflation Shifted? An Empirical Analysis with a Regime-Switching Model_ ,
2015)
Kashif and Leirvik (“Regime Switching Stock Returns and Hybrid Tail Risk,” 2021)
Kaya (“Managing ambiguity in asset allocation,” 2017)
Kim et al. (“Global Asset Allocation Strategy Using a Hidden Markov Model,” 2019)
Koki et al. (“Exploring the predictability of cryptocurrencies via Bayesian hidden Markov models,” 2022)
Komatsu and Makimoto (“Dynamic Investment Strategy with Factor Models Under Regime Switches,” 2015)
Li and Zakamulin (“Stock volatility predictability in bull and bear markets,” 2020)
Li and Mulvey (“Portfolio Optimization Under Regime Switching and Transaction Costs: Combining Neural
Networks and Dynamic Programs,” 2021)
Massacci (“Testing for Regime Changes in Portfolios with a Large Number of Assets: A Robust Approach to
Factor Heteroskedasticity,” 2021)
Martirosyan and Simonian (“Emerging Market Stock Momentum Returns during US Economic Regimes,” 2021)
McGee (“Can Market Regimes Really be Timed with Historical Volatility?” 2021)
McIndoe (“A Data Driven Approach to Market Regime Classification,” 2020)


McQuarrie (“New Lessons from Market History: Sometimes Bonds Win,” 2021)
Muller and Preissler (“In Good and in Bad Times? The Relation between Anomaly Returns and Market States,”
2021)
Mulvey et al. (“Machine learning, economic regimes and portfolio optimisation,” 2018)
Nystrup et al. (“Regime-Based Versus Static Asset Allocation: Letting the Data Speak,” 2015)
Nystrup et al. (“Dynamic portfolio optimization across hidden market regimes,” 2018)
Nystrup (“Regime-Based Asset Allocation: Do Profitable Strategies Exist?” 2014)
Nystrup et al. (“Dynamic Allocation or Diversification: A Regime-Based Approach to Multiple Assets,” 2018)
O’Cinneid (“Applications of machine learning in finance: analysis of international portfolio flows using regime-
switching models,” 2019)
Omerovic et al. (“Modelling Multiple Regimes in Economic Growth by Mixtures of Generalised Nonlinear
Models,” 2021)
Omerovic et al. (“Modelling Multiple Regimes in Economic Growth by Mixtures of Generalised Nonlinear
Models,” 2021)
Papenbrock and Schwendner (“Handling risk-on/risk-off dynamics with correlation regimes and correlation net-
works,” 2015)
Platanakis et al. (“Portfolios in a Regime Shifting Non-Normal World: Are Alternative Assets Beneficial?” 2017)
Peters (“Stable vs. Unstable Markets: A Tale of Two States,” 2015)
Pharasi et al. (“Market states: A new understanding,” 2020)
Pharasi et al. (“Dynamics of market states and risk assessment,” 2020)
Procacci and Aste (“Forecasting market states,” 2019)
Rebonato and El Aouadi (“How Do the Volatilities of Rates Depend on Their Level? The ”Universal Relation-
ship” Revisited,” 2021)
Reher and Wilfling (“A nesting framework for Markov-switching GARCH modelling with an application to the
German stock market,” 2015)
Sarwar et al. (“A tale of two states: asymmetries in the UK small, value and momentum premiums,” 2017)
Satchell (“Regime-switching in financial markets,” 2011)
Seidl (“Markowitz versus Regime Switching: An Empirical Approach,” 2012)
Sheikh and Sun (“Regime Change: Implications of Macroeconomic Shifts on Asset Class and Portfolio Perfor-
mance,” 2012)
Singh and Singh (“Risk-Return Relationship in BRIC Equity Markets: Evidence from Markov Regime Switching
Model with Time-varying Transition Probabilities,” 2016)
Silveira and Oscar (“Inflation Targeting Regimes in Emerging Market Economies: To Invest or Not to Invest?”
2021)
Simonian and Wu (“Minsky vs. Machine: New Foundations for Quant-Macro Investing,” 2019)
Stillwagon and Sullivan (“Markov switching in exchange rate models: will more regimes help?” 2020)
Sueppel ( _Classifying market regimes_ , 2021)
Tajeuna et al. (“Modeling Regime Shifts in Multiple Time Series,” 2022)
Tu (“Is Regime Switching in Stock Returns Important in Portfolio Decisions?” 2010)
Uysal (“Risk Budgeting Portfolios Under a Modern Optimization and Machine Learning Lens,” 2021)
Uysal and Mulvey (“A Machine Learning Approach in Regime-Switching Risk Parity Portfolios,” 2021)
Wang et al. (“Volatility forecasting revisited using Markov-switching with time-varying probability transition,”
2022)
Wang and Hsieh (“Unraveling S&P500 stock volatility and networks – An encoding-and-decoding approach,”
2021)
Wu (“On the Predictive Performance of the Stock Returns by Using the Markov-Switching Models,” 2020)
Zakamulin (“Not All Bull and Bear Markets Are Alike: Insights From a Five-State Hidden Semi-Markov Model,”
2020)
Zaremba et al. (“A Tale of Two States: An Application of a Markov Switching Model to Anomaly Returns,”
2020)

**2.2.4 Market states, regimes, changepoints and structural breaks of time series**
List of references:


Amini and Bayat (“hhsmm: An R package for hidden hybrid Markov/semi-Markov models,” 2022)
Blazquez-Garcia et al. (“A review on outlier/anomaly detection in time series data,” 2022)
Botte and Bao ( _A Machine Learning Approach to Regime Modeling_ , 2021)
Braei and Wagner (“Anomaly Detection in Univariate Time-series: A Survey on the State-of-the-Art,” 2020)
Chalapathy and Chawla (“Deep Learning for Anomaly Detection: A Survey,” 2019)
Chalapathy et al. (“Robust Deep Learning Methods for Anomaly Detection,” 2020)
Chapman and Killick (“An assessment of practitioners approaches to forecasting in the presence of changepoints,”
2020)
Das et al. (“Active Anomaly Detection via Ensembles: Insights, Algorithms, and Interpretability,” 2019)
Dette et al. (“Change Point Analysis of Correlation in Non-stationary Time Series,” 2019)
Dette et al. (“Multiscale change point detection for dependent data,” 2021)
Foorthuis (“On the Nature and Types of Anomalies: A Review,” 2021)
Geiger et al. (“TadGAN: Time Series Anomaly Detection Using Generative Adversarial Networks,” 2020)
Gerstenberger (“Robust discrimination between long-range dependence and a change in mean,” 2021)
Goswami et al. (“Abrupt transitions in time series with uncertainties,” 2018)
Guérin et al. (“Markov-Switching Three-Pass Regression Filter,” 2020)
Hallac et al. (“Greedy Gaussian segmentation of multivariate time series,” 2019)
Jacob et al. (“Exathlon: A Benchmark for Explainable Anomaly Detection over Time Series,” 2021)
Jacquier et al. (“Market regime classification with signatures,” 2021)
Jewell et al. (“Testing for a Change in Mean After Changepoint Detection,” 2021)
Jiang et al. (“Determining the number of change-point via high-dimensional cross-validation,” 2020)
Koki et al. (“Exploring the predictability of cryptocurrencies via Bayesian hidden Markov models,” 2022)
Lee et al. (“ReRe: A Lightweight Real-time Ready-to-Go Anomaly Detection Approach for Time Series,” 2020)
Lee et al. (“Factor-driven two-regime regression,” 2021)
Massacci and Kapetanios (“Forecasting in Factor Augmented Regressions under Structural Change,” 2021)
Meitz and Saikkonen (“Testing for observation-dependent regime switching in mixture autoregressive models,”
2021)
Messer (“Bivariate change point detection: joint detection of changes in expectation and variance,” 2021)
Navarro et al. (“Network Clustering for Latent State and Changepoint Detection,” 2021)
Neto et al. (“Uncovering regimes in out of sample forecast errors,” 2021)
Odendahl et al. (“Comparing Forecast Performance with State Dependence,” 2020)
Pang et al. (“Unlocking the Full Potential of Small Data with Diverse Supervision,” 2021)
Perikos et al. (“Sentiment analysis using novel and interpretable architectures of Hidden Markov Models,” 2021)
Pinto and Castle ( _A machine learning dynamic switching approach to forecasting when there are structural
breaks_ , 2021)
Prakash et al. (“Structural clustering of volatility regimes for dynamic trading strategies,” 2021)
Ruff et al. (“A Unifying Review of Deep and Shallow Anomaly Detection,” 2021)
Shi (“A Survey of Changepoint Techniques for Time Series Data,” 2020)
Shi et al. (“A Comparison of Single and Multiple Changepoint Techniques for Time Series Data,” 2021)
Siliverstovs and Wochner (“State-Dependent Evaluation of Predictive Ability,” 2021)
Smith and Timmermann (“Break Risk,” 2021)
Tajeuna et al. (“Modeling Regime Shifts in Multiple Time Series,” 2022)
Tran et al. (“Model Selection for Bayesian Autoencoders,” 2021)
van den Burg and Williams (“An Evaluation of Change Point Detection Algorithms,” 2022)
Wang et al. (“Deep Learning for Anomaly Detection,” 2020)
Wolchover (“Machine Learning’s ’Amazing’ Ability to Predict Chaos,” 2018)
Wu and Keogh (“Current Time Series Anomaly Detection Benchmarks are Flawed and are Creating the Illusion
of Progress,” 2021)
Zheng et al. (“Regime switching model estimation: spectral clustering hidden Markov model,” 2021)

**2.2.5 Detection and usage of bubbles, crashes and business cycles within context of QWIM**
List of references:
Allaj and Sanfelici (“An Early Warning System for Identifying Financial Instability,” 2022)


Astill et al. (“Real-Time Monitoring for Explosive Financial Bubbles,” 2018)
Bianchi (“The Great Depression and the Great Recession: A view from financial markets,” 2020)
Benhamou et al. (“Explainable AI (XAI) Models Applied to Planning in Financial Markets,” 2021)
Benhamou et al. (“Detecting and Adapting to Crisis Pattern with Context Based Deep Reinforcement Learning,”
2021)
Benhamou et al. (“Planning in Financial Markets in Presence of Spikes: Using Machine Learning GBDT,” 2021)
Bordalo et al. (“Diagnostic bubbles,” 2021)
Bucci and Ciciretti (“Market Regime Detection via Realized Covariances: A Comparison between Unsupervised
Learning and Nonlinear Models,” 2021)
Bybee et al. (“Narrative Asset Pricing: Interpretable Systematic Risk Factors from News Text,” 2022)
Chabi-Yo et al. (“Multivariate Crash Risk,” 2022)
Chowdhury et al. (“Bubbles and Crashes in Cryptocurrencies: Interdependence, Contagion, or Asset Rotation?”
2021)
Cram (“Late to Recessions: Stocks and the Business Cycle,” 2020)
Douady and Kornprobst (“An Empirical Approach to Financial Crisis Indicators Based on Random Matrices,”
2018)
Elkind et al. (“When Do Investors Freak Out? Machine Learning Predictions of Panic Selling,” 2022)
Engle and Ruan (“Measuring the probability of a financial crisis,” 2019)
Gerlach et al. (“Crash-sensitive Kelly Strategy built on a modified Kreuser-Sornette bubble model tested over
three decades of twenty equity indices,” 2020)
Gobel and Araujo (“Indicators of economic crises: a data-driven clustering approach,” 2020)
Glocker and Wegmueller (“Business cycle dating and forecasting with real-time Swiss GDP data,” 2020)
Heckens and Guhr (“A new attempt to identify long-term precursors for endogenous financial crises in the market
correlation structures,” 2022)
Horváth et al. (“How to identify the different phases of stock market bubbles statistically?” 2022)
Kabran and Unlu (“A two-step machine learning approach to predict S&P 500 bubbles,” 2021)
Kole and van Dijk (“How to Identify and Forecast Bull and Bear Markets?” 2016)
Liu et al. (“Predicting financial crises with machine learning methods,” 2022)
Malevergne et al. (“A model of financial bubbles and drawdowns with non-local behavioral self-referencing,”
2021)
Mehta (“The Mechanism behind the Bursting of Financial Bubbles and Market Crashes,” 2020)
Min et al. (“The 2021 Bitcoin Bubbles and Crashes – Detection and Classification,” 2021)
Mizuno et al. (“Detecting Stock Market Bubbles Based on the Cross-Sectional Dispersion of Stock Prices,” 2020)
Ohana et al. (“Explainable AI Models of Stock Crashes: A Machine-Learning Explanation of the Covid March
2020 Equity Meltdown,” 2021)
Samal et al. (“Network geometry and market instability,” 2021)
Schatz (“Financial Modeling of Bubbles and Crashes,” 2020)
Smug et al. (“Predicting Financial Market Crashes Using Ghost Singularities,” 2017)
Viebig (“Exuberance in Financial Markets: Evidence from Machine Learning Algorithms,” 2020)
Wang and Zong (“Are Crises Predictable? A Review of the Early Warning Systems in Currency and Stock
Markets,” 2020)
Wehrli and Sornette (“Classification of flash crashes using the Hawkes(p,q) framework,” 2022)
Yan and Huang (“Financial cycle and business cycle: An empirical analysis based on the data from the U.S,”
2020)
Yao and Li (“A study on the bursting point of Bitcoin based on the BSADF and LPPLS methods,” 2021)
Zhang et al. (“LPPLS bubble indicators over two centuries of the S&P 500 index,” 2016)
Zhang et al. (“LPPLS bubble indicators over two centuries of the S&P 500 index,” 2016)
Zhao and Sornette (“Bubbles for Fama from Sornette,” 2022)

**2.2.6 Detection and usage of bubbles, crashes and business cycles**
List of references:
Chalkis et al. (“Modeling of crisis periods in stock markets,” 2021)
Francis et al. ( _Business Cycles Across Space and Time_ , 2021)


Kreuser and Sornette (“Super-Exponential RE bubble model with efficient crashes,” 2019)
Shu et al. (“The 2021 Bitcoin Bubbles and Crashes – Detection and Classification,” 2021)
Smith et al. (“Equity Premium Forecasts with an Unknown Number of Structural Breaks,” 2020)
Sornette (“Dragon-kings and Predictions: Diagnostics and Forecasts for the World Financial Crisis,” 2014)
Sornette and Cauwels (“Financial bubbles: mechanisms and diagnostics,” 2014)
Sornette et al. (“Real-time prediction and post-mortem analysis of the Shanghai 2015 stock market bubble and
crash,” 2015)
Sornette et al. (“Resolving Persistent Uncertainty by Self-Organized Consensus to Mitigate Market Bubbles,”
2016)
Sornette et al. (“Can We Use Volatility to Diagnose Financial Bubbles? Lessons from 40 Historical Bubbles,”
2017)

**2.2.7 Forecasting under data regimes**
List of references:
Bansal et al. (“The term structure of equity risk premia,” 2021)
Bahrami et al. (“Are advanced emerging market stock returns predictable? A regime-switching forecast combi-
nation approach,” 2019)
Baltas and Karyampas (“Forecasting the equity risk premium: The importance of regime-dependent evaluation,”
2018)
Beccarini (“Testing for the omission of relevant variables and regime-switching misspecification,” 2019)
Bel and Paap (“Modeling the impact of forecast-based regime switches on US inflation,” 2016)
Bianchi and Guidolin (“Can Linear Predictability Models Time Bull and Bear Real Estate Markets? Out-of-
Sample Evidence from REIT Portfolios,” 2014)
Boot (“Macroeconomic Forecasting under Regime Switching, Structural Breaks and High-dimensional Data,”
2017)
Can (“To Switch or Not to Switch: Return Prediction and financial cycles,” 2019)
Chang et al. (“A new approach to model regime switching,” 2017)
Chiappa (“Unified Treatment of Hidden Markov Switching Models,” 2011)
Chollete et al. (“Modeling International Financial Returns with a Multivariate Regime-switching Copula,” 2009)
Dal Pra et al. (“Regime Shifts in Excess Stock Return Predictability: An Out-of-Sample Portfolio Analysis,”
2018)
Elliott and Timmermann (“Optimal forecast combination under regime switching,” 2005)
Guidolin et al. (“How good can heuristic-based forecasts be? A comparative performance of econometric and
heuristic models for UK and US asset returns,” 2018)
Haase and Neuenkirch (“Predictability of Bull and Bear Markets: A New Look at Forecasting Stock Market
Regimes (and Returns) in the U.S.,” 2021)
Hammerschmid and Lohre (“Regime Shifts and Stock Return Predictability,” 2018)
Harvey et al. (“Real-Time Detection of Regimes of Predictability in the U.S. Equity Premium,” 2021)
Kim and Kang (“Bayesian Inference of Multivariate Regression Models with Endogenous Markov Regime-
Switching Parameters,” 2022)
Lee et al. (“Factor-Driven Two-Regime Regression,” 2020)
Neto et al. (“Uncovering regimes in out of sample forecast errors,” 2021)
Pruser (“Forecasting US inflation using Markov dimension switching,” 2021)
Ren (“Essays in Asset Pricing and Financial Econometrics,” 2016)
Smith (“International Stock Return Predictability and Asset Pricing Models,” 2021)
Smith et al. (“Equity Premium Forecasts with an Unknown Number of Structural Breaks,” 2020)
Wang et al. (“Volatility forecasting revisited using Markov-switching with time-varying probability transition,”
2022)
Werge (“Predicting Risk-adjusted Returns using an Asset Independent Regime-switching Model,” 2021)
Wu (“On the Predictive Performance of the Stock Returns by Using the Markov-Switching Models,” 2020)


**2.2.8 Numerical methods, models and their implementations to model and analyze data regimes**
List of references:
Ansari et al. (“Deep Explicit Duration Switching Models for Time Series,” 2021)
Bazzi et al. (“Time-Varying Transition Probabilities for Markov Regime Switching Models,” 2017)
Bergmeir et al. (“Time Series Modeling and Forecasting Using Memetic Algorithms for Regime-Switching Mod-
els,” 2012)
Bianchi (“Methods for measuring expectations and uncertainty in Markov-switching models,” 2016)
Chen (“Studying Regime Change using Directional Change,” 2019)
Chuffart (“An Implementation of Markov Regime Switching GARCH Models in Matlab,” 2017)
Ding (“An Implementation of Markov Regime Switching Model with Time Varying Transition Probabilities in
Matlab,” 2012)
Jochmann and Koop (“Regime-switching cointegration,” 2015)
Kamenshchikov (“Bifurcation patterns of market regime transition,” 2016)
Kasahara and Shimotsu (“Testing the Order of Multivariate Normal Mixture Models,” 2019)
Khalili et al. (“Regularization in Regime-Switching Gaussian Autoregressive Models,” 2016)
Moreno-Pino et al. (“PyHHMM: A Python Library for Heterogeneous Hidden Markov Models,” 2022)
Ou et al. (“Whats for dynr: A Package for Linear and Nonlinear Dynamic Modeling in R,” 2019)
Zheng et al. (“Regime switching model estimation: spectral clustering hidden Markov model,” 2021)


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
Source:Machine Learning in Asset Management^24


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

Ahelegbey, D. F., Billio, M., and Casarin, R. (2020).“Modeling Turning Points In Global Equity Market.” In: _SSRN
e-Print_.
Ahmad, W., Bhanumurthy, N. R., and Sehgal, S. (2015).“Regime dependent dynamics and European stock markets:
Is asset allocation really possible?” In: _Empirica_ 42(1), pp. 77–107.
Ahmad, W. and Sehgal, S. (2015).“Regime shifts and volatility in BRIICKS stock markets: an asset allocation
perspective.” In: _International Journal of Emerging Markets_ 10(3), pp. 383–408.
Akioyamen, P., Tang, Y. Z., and Hussien, H. (2021).“A Hybrid Learning Approach to Detecting Regime Switches
in Financial Markets.” In: _arXiv e-Print_.
Alberico, S., Coche, J., Sahakyan, V., and Zulaica, O. (2018).“Regime identification for sovereign bond portfolio
construction.” In: _Advances in the practice of public investment management: portfolio modelling, performance
attribution and governance_. Ed. by N. Bulusu, J. Coche, A. Reveiz, F. Rivadeneyra, V. Sahakyan, and G. Yanou.
Springer International Publishing, pp. 247–274.
Allaj, E. and Sanfelici, S. (2022).“An Early Warning System for Identifying Financial Instability.” In: _SSRN e-Print_.
Amini, M. and Bayat, A. (2022). “hhsmm: An R package for hidden hybrid Markov/semi-Markov models.” In: _arXiv
e-Print_.
Ang, A. and Bekaert, G. (2004).“How do Regimes Affect Asset Allocation.” In: _Financial Analysts Journal_ 60(2),
pp. 86–99.
Ang, A. and Timmermann, A. (2012).“Regime Changes and Financial Markets.” In: _Annual Review of Financial
Economics_ 4(1), pp. 313–337.
Angelini, G., Bacchiocchi, E., Caggiano, G., and Fanelli, L. (2019).“Uncertainty across volatility regimes.” In:
_Journal of Applied Econometrics_ 34(3), pp. 437–455.
Ansari, A. F., Benidis, K., Kurle, R., Turkmen, A. C., Soh, H., Smola, A. J., Wang, Y., and Januschowski, T.
(2021). “Deep Explicit Duration Switching Models for Time Series.” In: _arXiv e-Print_.
Arago, V. and Salvador, E. (2013).“Non-linear Tradeoff between Risk and Return: A Regime-switching Multi-factor
Framework.” In: _Modeling and Simulation in Engineering, Economics, and Management_. Ed. by M. Fernandez-
Izquierdo, M. Munoz-Torres, and R. Leon. Vol. 145. Lecture Notes in Business Information Processing. Springer
Berlin Heidelberg, pp. 64–74.
Ardia, D., Boudt, K., and Gagnon-Fleury, J.-P. (2017).“RiskPortfolios: Computation of Risk-Based Portfolios in
R.” In: _The Journal of Open Source Software_ 2(10), pp. 171+.
Astill, S., Harvey, D. I., Leybourne, S. J., Sollis, R., and Taylor, A. M. R. (2018).“Real-Time Monitoring for
Explosive Financial Bubbles.” In: _Journal of Time Series Analysis_ 39(6), pp. 863–891.
Bacon, C. R. (2019).“Performance Attribution: History and Progress.” In: _CFA Institute Research Foundation
Publications_.
Bae, G. I., Kim, W. C., and Mulvey, J. M. (2014).“Dynamic asset allocation for varied financial markets under
regime switching framework.” In: _European Journal of Operational Research_ 234(2), pp. 450–458.
Bahrami, A., Shamsuddin, A., and Uylangco, K. (2019).“Are advanced emerging market stock returns predictable?
A regime-switching forecast combination approach.” In: _Pacific-Basin Finance Journal_ 55, pp. 142–160.
Baitinger, E. and Flegel, S. (2021).“The better turbulence index? Forecasting adverse financial markets regimes
with persistent homology.” In: _Financial Markets and Portfolio Management_.
Balcerak, M. and Schmelzer, T. (2020).“Constructing trading strategy ensembles by classifying market states.” In:
_arXiv e-Print_.
Baltas, N. and Karyampas, D. (2018).“Forecasting the equity risk premium: The importance of regime-dependent
evaluation.” In: _Journal of Financial Markets_ 38(March), pp. 83–102.
Baltas, N. and Karyampas, D. (2020).“Forecasting the Equity Risk Premium: The Importance of Regime-Dependent
Evaluation.” In: _SSRN e-Print_.
Bansal, R., Miller, S., Song, D., and Yaron, A. (2021).“The term structure of equity risk premia.” In: _Journal of
Financial Economics_.
Barkai, I., Shushi, T., and Yosef, R. (2021).“A Cryptocurrency Risk-Return Analysis for Bull and Bear Regimes.”
In: _The Journal of Alternative Investments_ 24(1), pp. 95–118.
Bazzi, M., Blasques, F., Koopman, S. J., and Lucas, A. (2017).“Time-Varying Transition Probabilities for Markov
Regime Switching Models.” In: _Journal of Time Series Analysis_ 38(3), pp. 458–478.


Beccarini, A. (2019).“Testing for the omission of relevant variables and regime-switching misspecification.” In:
_Empirical economics_ 56(3), pp. 775–796.
Bel, K. and Paap, R. (2016).“Modeling the impact of forecast-based regime switches on US inflation.” In: _Interna-
tional Journal of Forecasting_ 32(4), pp. 1306–1316.
Benhamou, E., Ohana, J.-J., Saltiel, D., and Guez, B. (2021a).“Explainable AI (XAI) Models Applied to Planning
in Financial Markets.” In: _SSRN e-Print_.
Benhamou, E., Ohana, J.-J., Saltiel, D., and Guez, B. (2021b).“Planning in Financial Markets in Presence of
Spikes: Using Machine Learning GBDT.” In: _SSRN e-Print_.
Benhamou, E., Saltiel, D., Ohana, J.-J., and Atif, J. (2021c).“Detecting and Adapting to Crisis Pattern with
Context Based Deep Reinforcement Learning.” In: _SSRN e-Print_.
Berger, T. and Gencay, R. (2020).“Short-run wavelet-based covariance regimes for applied portfolio management.”
In: _Journal of Forecasting_ 39(4), pp. 642–660.
Bergmeir, C., Triguero, I., Molina, D., Aznarte, J. L., and Benitez, J. M. (2012).“Time Series Modeling and Fore-
casting Using Memetic Algorithms for Regime-Switching Models.” In: _IEEE Transactions on Neural Networks
and Learning Systems_ 23(11), pp. 1841–1847.
Bernhart, G., Hocht, S., Neugebauer, M., Neumann, M., and Zagst., R. (2011).“Asset Correlations in Turbulent
Markets and the Impact of Different Regimes on Asset Management.” In: _Asia-Pacific Journal of Operational
Research_ 28(01), pp. 1–23.
Bhansali, V. and Holdom, J. (2021).“Good States, Bad States: What Do Options Tell Us About Schizophrenic
Behavior of Mr. Market and What Can We Do About It?” In: _Journal of Investment Strategies_ 19(4), pp. 79–91.
Bianchi, D. and Guidolin, M. (2014).“Can Linear Predictability Models Time Bull and Bear Real Estate Markets?
Out-of-Sample Evidence from REIT Portfolios.” In: _The Journal of Real Estate Finance and Economics_ 49(1),
pp. 116–164.
Bianchi, F. (2016).“Methods for measuring expectations and uncertainty in Markov-switching models.” In: _Journal
of Econometrics_ 190(1), pp. 79–99.
Bianchi, F. (2020).“The Great Depression and the Great Recession: A view from financial markets.” In: _Journal of
Monetary Economics_ 114, pp. 240–261.
Billio, M., Ferrara, L., Guegan, D., and Mazzi, G. L. (2013).“Evaluation of Regime Switching Models for Real-Time
Business Cycle Analysis of the Euro Area.” In: _Journal of Forecasting_ 32(7), pp. 577–586.
Bilokon, P., Jacquier, A., and McIndoe, C. (2021).“Market regime classification with signatures.” In: _arXiv e-Print_.
Blazquez-Garcia, A., Conde, A., Mori, U., and Lozano, J. A. (2022).“A review on outlier/anomaly detection in
time series data.” In: _ACM Computing Surveys_ 54(3), pp. 1–33.
Blin, O., Ielpo, F., Lee, J., and Teiletche, J. (2017).“A Macro Risk-Based Approach to Alternative Risk Premia
Allocation.” In: _Factor Investing_. Elsevier, pp. 285–316.
Blitz, D. and Van Vliet, P. (2009).“Dynamic Strategic Asset Allocation: Risk and Return Across Economic Regimes.”
In: _SSRN e-Print_.
BNYMellon Research (2013). _Great expectations: regime based asset allocation seeks higher return, lower drawdowns_.
Tech. rep. BNY Mellon.
Boileau, P., Hejazi, N., Collica, B., Laan, M. van der, and Dudoit, S. (2021).“cvCovEst: Cross-validated covariance
matrix estimator selection and evaluation in R.” In: _Journal of Open Source Software_ 6(63), p. 3273.
Boot, T. (2017).“Macroeconomic Forecasting under Regime Switching, Structural Breaks and High-dimensional
Data.” PhD thesis. Tinbergen Instituut.
Bordalo, P., Gennaioli, N., Kwon, S. Y., and Shleifer, A. (2021).“Diagnostic bubbles.” In: _Journal of Financial
Economics_ 141(3), pp. 1060–1077.
Botte, A. and Bao, D. (2021). _A Machine Learning Approach to Regime Modeling_. Tech. rep. Two Sigma.
Bradrania, R. and Neghab, D. P. (2022).“State-dependent asset allocation using neural networks.” In: _The European
Journal of Finance_.
Braei, M. and Wagner, S. (2020).“Anomaly Detection in Univariate Time-series: A Survey on the State-of-the-Art.”
In: _arXiv e-Print_.
Brugiere, P. (2020). _Quantitative Portfolio Management with Applications in Python_. Springer International Pub-
lishing. 189 pp.
Bryzgalova, S., Pelger, M., and Zhu, J. (2021).“Forest Through the Trees: Building Cross-Sections of Stock Returns.”
In: _SSRN e-Print_.


Bucci, A. and Ciciretti, V. (2021).“Market Regime Detection via Realized Covariances: A Comparison between
Unsupervised Learning and Nonlinear Models.” In: _arXiv e-Print_.
Bybee, L., Kelly, B. T., and Su, Y. (2022).“Narrative Asset Pricing: Interpretable Systematic Risk Factors from
News Text.” In: _SSRN e-Print_.
Cajas, D. (2021a).“Entropic Portfolio Optimization: a Disciplined Convex Programming Framework.” In: _SSRN
e-Print_.
Cajas, D. (2021b).“OWA Portfolio Optimization: a Disciplined Convex Programming Framework.” In: _SSRN e-
Print_.
Campani, C. H., Garcia, R., and Lewin, M. (2021).“Optimal portfolio strategies in the presence of regimes in asset
returns.” In: _Journal of Banking & Finance_ 123, p. 106030.
Can, H. (2019).“To Switch or Not to Switch: Return Prediction and financial cycles.” MA thesis. Erasmus University.
Chabi-Yo, F., Huggenberger, M., and Weigert, F. (2022).“Multivariate Crash Risk.” In: _Journal of Financial
Economics_.
Chalapathy, R. and Chawla, S. (2019).“Deep Learning for Anomaly Detection: A Survey.” In: _arXiv e-Print_.
Chalapathy, R., Khoa, N. L. D., and Chawla, S. (2020).“Robust Deep Learning Methods for Anomaly Detection.”
In: _Proceedings of the 26th ACM SIGKDD International Conference on Knowledge Discovery & Data Mining_.
ACM.
Chalkis, A., Christoforou, E., Dalamagkas, T., and Emiris, I. Z. (2021).“Modeling of crisis periods in stock markets.”
In: _arXiv e-Print_.
Chang, Y., Choi, Y., and Park, J. Y. (2017).“A new approach to model regime switching.” In: _Journal of Economics_
196(1), pp. 127–143.
Chapman, J.-L. and Killick, R. (2020).“An assessment of practitioners approaches to forecasting in the presence
of changepoints.” In: _Quality and Reliability Engineering International_ 36(8), pp. 2676–2687.
Chen, A. Y. and Zimmermann, T. (2022).“Open Source Cross-Sectional Asset Pricing.” In: _American Finance
Association Annual Meeting_.
Chen, J. M., Rehman, M. U., and Vo, X. V. (2021).“Clustering commodity markets in space and time: Clarify-
ing returns, volatility, and trading regimes through unsupervised machine learning.” In: _Resources Policy_ 73,
p. 102162.
Chen, J. (2019).“Studying Regime Change using Directional Change.” PhD thesis. University of Essex.
Chen, J. and Tsang, E. P. K. (2020). _Detecting regime change in computational finance: data science, machine
learning and algorithmic trading_. Boca Raton: CRC Press, Taylor & Francis Group. 164 pp.
Chen, P. and Yang, H. (2011).“Markowitz’s Mean-Variance Asset-Liability Management with Regime Switching:
A Multi-Period Model.” In: _Applied Mathematical Finance_ 18(1), pp. 29–50.
Cheng, E., Kostyuchyk, N., Lee, W., Liu, P., and Ma, C. (2021).“Trending Fast and Slow.” In: _The Journal of
Portfolio Management_.
Chiappa, S. (2011).“Unified Treatment of Hidden Markov Switching Models.” In: _arXiv e-Print_.
Chib, S. (2020). _R package czfactor_. Tech. rep. Washington University.
Chib, S. and Zhao, L. (2020). _R package czzg_. Tech. rep. Washington University.
Chollete, L., Heinen, A., and Valdesogo, A. (2009).“Modeling International Financial Returns with a Multivariate
Regime-switching Copula.” In: _Journal of Financial Econometrics_ 7(4), pp. 437–480.
Chowdhury, M. S. R., Damianov, D. S., and Elsayed, A. H. (2021).“Bubbles and Crashes in Cryptocurrencies:
Interdependence, Contagion, or Asset Rotation?” In: _SSRN e-Print_.
Chuffart, T. (2017).“An Implementation of Markov Regime Switching GARCH Models in Matlab.” In: _SSRN
e-Print_.
Clacher, I., Freeman, M., Hillier, D., Kemp, M., and Zhang, Q. (2015).“A Practical Guide to Regime Switching in
Financial Economics.” In: _Quantitative Financial Risk Management: Theory and Practice_. Ed. by C. Zopounidis
and E. Galariotis. John Wiley and Sons, Inc, pp. 71–97.
Coqueret, G. (2022). _Perspectives in sustainable equity investing (website version)_.
Coqueret, G. and Guida, T. (2020). _Machine Learning for Factor Investing: R Version_. Chapman and Hall/CRC.
341 pp.
Corbelli, R., Vellasco, M., and Veiga, A. (2020).“Investigating Optimal Regimes for Prediction in the Stock Market.”
In: _IEEE Congress on Evolutionary Computation (CEC)_. IEEE.
Costa, G. and Kwon, R. H. (2019).“Risk parity portfolio optimization under a Markov regime-switching framework.”
In: _Quantitative Finance_ 19(33), pp. 453–471.


Costa, G. and Kwon, R. H. (2020).“A regime-switching factor model for mean-variance optimization.” In: _Journal
of Risk_ 22(4), pp. 31–59.
Cram, R. G. (2020).“Late to Recessions: Stocks and the Business Cycle.” In: _SSRN e-Print_.
Dai, M., Jin, H., Kou, S., and Xu, Y. (2021).“Robo-Advising: A Dynamic Mean-Variance Approach.” In: _SSRN
e-Print_.
Dal Pra, G., Guidolin, M., Pedio, M., and Vasile, F. (2018).“Regime Shifts in Excess Stock Return Predictability:
An Out-of-Sample Portfolio Analysis.” In: _The Journal of Portfolio Management_ 44(3), pp. 10–24.
Dapena, J. P., Serur, J. A., and Siri, J. R. (2020).“Risk On-Risk Off: A Regime Switching Model for Active Portfolio
Management.” In: _SSRN e-Print_.
Das, S. R., Ostrov, D. N., Casanova, A., Radhakrishnan, A., and Srivastav, D. (2021).“Optimal Goals-Based
Investment Strategies For Switching Between Bull and Bear Markets.” In: _SSRN e-Print_.
Das, S. R., Ostrov, D. N., Casanova, A., Radhakrishnan, A., and Srivastav, D. (2022).“Optimal Goals-Based
Investment Strategies For Switching Between Bull and Bear Markets.” In: _The Journal of Wealth Management_
24(4), pp. 8–36.
Das, S., Islam, M. R., Jayakodi, N. K., and Doppa, J. R. (2019).“Active Anomaly Detection via Ensembles: Insights,
Algorithms, and Interpretability.” In: _arXiv e-Print_.
de Carvalho, M. and Rua, A. (2017).“Real-time nowcasting the US output gap: Singular spectrum analysis at
work .” In: _International Journal of Forecasting_ 33(1), pp. 185–198.
Demos, G. and Sornette, D. (2017).“Birth or burst of financial bubbles: which one is easier to diagnose?” In:
_Quantitative Finance_ 17(5), pp. 657–675.
Dette, H., Eckle, T., and Vetter, M. (2021).“Multiscale change point detection for dependent data.” In: _Scandinavian
Journal of Statistics_.
Dette, H., Wu, W., and Zhou, Z. (2019).“Change Point Analysis of Correlation in Non-stationary Time Series.” In:
_Statistica Sinica_ (29), pp. 611–643.
Dias, J. G., Vermunt, J. K., and Ramos, S. (2015).“Clustering financial time series: New insights from an extended
hidden Markov model.” In: _European Journal of Operational Research_ 243(3), pp. 852–864.
Ding, L., Ahmed, S., and Shapiro, A. (2020).“A Python package for multi-stage stochastic programming.” In:
_Optimization Online e-Print_.
Ding, Z. (2012).“An Implementation of Markov Regime Switching Model with Time Varying Transition Probabil-
ities in Matlab.” In: _SSRN e-Print_.
Dixon, M. and Polson, N. (2020).“Deep Fundamental Factor Models.” In: _SIAM Journal on Financial Mathematics_
11(3), SC–26–SC–37.
Dixon, M. F., Halperin, I., and Bilokon, P. (2020). _Machine Learning in Finance: from theory to practice_. Springer
International Publishing. 548 pp.
Dong, X., Li, Y., Rapach, D., and Zhou, G. (2022).“Anomalies and the expected market return.” In: _Journal of
Finance_ 27(1), pp. 639–681.
Dou, P. Y., Gallagher, D. R., Schneider, D., Walter, T., and Berkman, H. (2014).“Cross-region and cross-sector
asset allocation with regimes.” In: _Accounting and Finance_ 54(3), pp. 809–846.
Douady, R. and Kornprobst, A. (2018).“An Empirical Approach to Financial Crisis Indicators Based on Random
Matrices.” In: _International Journal of Theoretical and Applied Finance_ 21(03), p. 1850022.
Duprey, T. and Klaus, B. (2017).“How to Predict Financial Stress? An Assessment of Markov Switching Models.”
In: _SSRN e-Print_.
Edirisinghe, C. and Zhao, Y. (2020).“Smart Indexing Under Regime-Switching Economic States.” In: _Applied
Mathematical Finance_ 27(5), pp. 422–456.
Elkamhi, R., Lee, J., and Salerno, M. (2021).“Portfolio Tilts using Views on Macroeconomic Regimes.” In: _SSRN
e-Print_.
Elkind, D., Kaminski, K., Lo, A. W., Siah, K. W., and Wong, C. H. (2022).“When Do Investors Freak Out?
Machine Learning Predictions of Panic Selling.” In: _The Journal of Financial Data Science_ 4(1), pp. 11–39.
Elliott, G. and Timmermann, A. (2005).“Optimal forecast combination under regime switching.” In: _International
Economic Review_ 46(4), pp. 1081–1102.
Elouai, H. M., Lambinet, R., and Morel, T. (2013). “Bubbles and Regimes: Two Complementary Approaches.” In:
_SSRN e-Print_.
Endres, S. and Stubinger, J. (2019).“A flexible regime switching model with pairs trading application to the S&P
500 high-frequency stock returns.” In: _Quantitative Finance_ , pp. 1–14.


Engle, R. F. and Ruan, T. (2019).“Measuring the probability of a financial crisis.” In: _Proceedings of the National
Academy of Sciences_ 116(37), pp. 18341–18346.
Erlwein, C., Mitra, G., and Roman, D. (2012).“HMM based scenario generation for an investment optimisation
problem.” In: _Annals of Operations Research_ 193(1), pp. 173–192.
Erlwein-Sayer, C., Grimm, S., Sass, J., and Sayer, T. (2016).“Portfolio Strategies and Estimation in a Hidden
Markov Model Using State Dependent, State Independent or No Correlation.” In: _SSRN e-Print_.
Fabozzi, F. J., Fabozzi, F. A., Lopez de Prado, M., and Stoyanov, S. (2021). _Asset Management: Tools and Issues_.
World Scientific. 516 pp.
Filimonov, V., Demos, G., and Sornette, D. (2017).“Modified profile likelihood inference and interval forecast of
the burst of financial bubbles.” In: _Quantitative Finance_ 17(8), pp. 1167-11861–20.
Fischer, E. O. and Murg, M. (2015).“A combined regime-switching and Black Litterman model for optimal asset
allocation.” In: _Journal of Investment Strategies_ 4(3), pp. 1–36.
Flint, E., Seymour, A., and Chikurunhe, F. (2021).“Defining and measuring portfolio diversification.” In: _South
African Actuarial Journal_ 20(1), pp. 17–48.
Flint, E. and du Plooy, S. (2018).“Extending risk budgeting for market regimes and quantile factor models.” In:
_Journal of Investment Strategies_ 7(4), pp. 51–74.
Flint, E. J. and Mare, E. (2019).“Regime-Based Tactical Allocation for Equity Factors and Balanced Portfolios.”
In: _South African Actuarial Journal_ 19(1), pp. 27–52.
Fons, E., Dawson, P., Yau, J., Zeng, X.-j., and Keane, J. (2021).“A novel dynamic asset allocation system using
Feature Saliency Hidden Markov models for smart beta investing.” In: _Expert Systems with Applications_ 163,
pp. 113720+.
Foorthuis, R. (2021).“On the Nature and Types of Anomalies: A Review.” In: _arXiv e-Print_.
Francis, N., Owyang, M. T., and Soques, D. (2021). _Business Cycles Across Space and Time_. Tech. rep. SSRN
e-Print.
Fulop, A. and Yu, J. (2017).“Bayesian analysis of bubbles in asset prices.” In: _Econometrics_ 5(4), p. 47.
Gallagher, L. A., Hutchinson, M. C., and O’Brien, J. (2020).“Using Smooth Transition Regressions to Model
Risk Regimes.” In: _Handbook of Financial Econometrics, Mathematics, Statistics, and Machine Learning_. World
Scientific, pp. 4281–4311.
Gao, G., Ho, K.-Y., and Shi, Y. (2018).“Long memory or regime switching in volatility? Evidence from high-
frequency returns on the U.S. stock indices.” In: _Pacific-Basin Finance Journal_.
Gatumel, M. and Ielpo, F. (2014).“The Number of Regimes Across Asset Returns: Identification and Economic
Value .” In: _International Journal of Theoretical and Applied Finance_ 17(06), pp. 1450040+.
Geiger, A., Liu, D., Alnegheimish, S., Cuesta-Infante, A., and Veeramachaneni, K. (2020).“TadGAN: Time Series
Anomaly Detection Using Generative Adversarial Networks.” In: _arXiv e-Print_.
Gerlach, J.-C., Kreuser, J. L., and Sornette, D. (2020).“Crash-sensitive Kelly Strategy built on a modified Kreuser-
Sornette bubble model tested over three decades of twenty equity indices.” In: _SSRN e-Print_.
Gerstenberger, C. (2021).“Robust discrimination between long-range dependence and a change in mean.” In: _Journal
of Time Series Analysis_ 42(1), pp. 34–62.
Gkatzilakis, G.-X. and Sivasubramanian, S. (2014).“Active Allocation of Smart Beta Indices based on Factor
Timing and Regime Switching.” MA thesis. EDHEC Risk Institute.
Glasserman, P., Mamaysky, H., and Shen, Y. (2021).“Dynamic information regimes in financial markets.” In: _SSRN
e-Print_.
Glocker, C. and Wegmueller, P. (2020).“Business cycle dating and forecasting with real-time Swiss GDP data.” In:
_Empirical Economics_ 58(1), pp. 73–105.
Gobel, M. and Araujo, T. (2020).“Indicators of economic crises: a data-driven clustering approach.” In: _Applied
Network Science_ 5(1) (44).
Goswami, B., Boers, N., Rheinwalt, A., Marwan, N., Heitzig, J., Breitenbach, S. F. M., and Kurths, J. (2018).
“Abrupt transitions in time series with uncertainties.” In: _Nature Communications_ 9(1) (48).
Grealish, A. and Kolm, P. N. (2021).“Robo-Advisory: From Investing Principles and Algorithms to Future Devel-
opments.” In: _SSRN e-Print_.
Gu, J. and Mulvey, J. M. (2021).“Factor Momentum and Regime-Switching Overlay Strategy.” In: _The Journal of
Financial Data Science_ 3(4), pp. 101–129.
Guérin, P., Leiva-Leon, D., and Marcellino, M. (2020).“Markov-Switching Three-Pass Regression Filter.” In: _Journal
of Business & Economic Statistics_ 38(2), pp. 285–302.


Guidolin, M. (2011).“Markov Switching in Portfolio Choice and Asset Pricing Models: A Survey.” In: _Advances in
Econometrics_. Emerald Group Publishing, pp. 87–178.
Guidolin, M., Orlov, A. G., and Pedio, M. (2018).“How good can heuristic-based forecasts be? A comparative
performance of econometric and heuristic models for UK and US asset returns.” In: _Quantitative Finance_ 18(1),
pp. 139–169.
Guidolin, M. and Timmermann, A. (2008).“International asset allocation under regime switching, skew, and kurtosis
preferences.” In: _The Review of Financial Studies_ 21(2), pp. 889–935.
Guijarro-Ordonez, J., Pelger, M., and Zanotti, G. (2021).“Deep Learning Statistical Arbitrage.” In: _SSRN e-Print_.
Gurdogan, H. and Kercheval, A. (2021). “Multi Anchor Point Shrinkage for the Sample Covariance Matrix (Extended
Version).” In: _arXiv e-Print_.
Haase, F. and Neuenkirch, M. (2021).“Predictability of Bull and Bear Markets: A New Look at Forecasting Stock
Market Regimes (and Returns) in the U.S.” In: _SSRN e-Print_.
Hallac, D., Nystrup, P., and Boyd, S. (2019).“Greedy Gaussian segmentation of multivariate time series.” In:
_Advances in Data Analysis and Classification_ 13(3), pp. 727–751.
Hammerschmid, R. and Lohre, H. (2018).“Regime Shifts and Stock Return Predictability.” In: _International Review
of Economics and Finance_ 56, pp. 138–160.
Hao, H. (2019).“A Regime-Aware Agent-Based Framework for Financial Planning.” PhD thesis. Princeton Univer-
sity.
Harvey, D. I., Leybourne, S. J., Sollis, R., and Taylor, A. M. R. (2021).“Real-Time Detection of Regimes of
Predictability in the U.S. Equity Premium.” In: _Journal of Applied Econometrics_ 36, pp. 45–70.
Hauptmann, J., Hoppenkamps, A., Min, A., Ramsauer, F., and Zagst, R. (2014).“Forecasting market turbulence
using regime-switching models.” In: _Financial Markets and Portfolio Management_ 28(2), pp. 139–164.
Heckens, A. J. and Guhr, T. (2022).“A new attempt to identify long-term precursors for endogenous financial crises
in the market correlation structures.” In: _Journal of Statistical Mechanics: Theory and Experiment_ 2022(4),
p. 043401.
Ho, J., Tumkaya, T., Aryal, S., Choi, H., and Claridge-Chang, A. (2019).“Moving beyond P values: data analysis
with estimation graphics.” In: _Nature Methods_ 16(7), pp. 565–566.
Hollstein, F., Prokopczuk, M., and Voigts, V. (2022).“How Robust are Empirical Factor Models to the Choice of
Breakpoints?” In: _SSRN e-Print_.
Homescu, C. (2014).“Many risks, one (optimal) portfolio.” In: _SSRN e-Print_.
Homescu, C. (2015).“Better Investing Through Factors, Regimes and Sensitivity Analysis.” In: _SSRN e-Print_.
Horvath, B., Issa, Z., and Muguruza, A. (2021).“Clustering Market Regimes Using the Wasserstein Distance.” In:
_SSRN e-Print_.
Horváth, L., Li, H., and Liu, Z. (2022).“How to identify the different phases of stock market bubbles statistically?”
In: _Finance Research Letters_ 46 (Part A) (102366).
Hu, Y., Shi, X., and Xu, Z. Q. (2022). “Mean variance asset liability management with regime switching.” In: _arXiv
e-Print_.
Huang, D., Jiang, F., Tu, J., and Zhou, G. (2017).“Forecasting Stock Returns in Good and Bad Times: The Role
of Market States.” In: _SSRN e-Print_.
Iqbal, J. (2018).“Application of Regime Switching and Random Matrix Theory for Portfolio Optimization.” PhD
thesis. University of Essex.
Irlam, G. (2020a). _AI Planner_ .url:https://www.aiplanner.com/.
Irlam, G. (2020b).“Machine learning for retirement planning.” In: _The Journal of Retirement_ 8(1), pp. 32–29.
Irlam, G. (2020c).“Multi Scenario Financial Planning via Deep Reinforcement Learning AI.” In: _SSRN e-Print_.
Jacob, V., Song, F., Stiegler, A., Diao, Y., and Tatbul, N. (2021).“Exathlon: A Benchmark for Explainable Anomaly
Detection over Time Series.” In: _arXiv e-Print_.
Jacquier, A., Bilokon, P., and McIndoe, C. (2021).“Market regime classification with signatures.” In: _SSRN e-Print_.
James, N. (2021). “Evolutionary correlation, regime switching, spectral dynamics and optimal trading strategies for
cryptocurrencies and equities.” In: _arXiv e-Print_.
Jansen, S. (2020). _Machine Learning for Algorithmic Trading (Second Edition)_. Packt Publishing. 820 pp.
Jewell, S., Fearnhead, P., and Witten, D. (2021).“Testing for a Change in Mean After Changepoint Detection.” In:
_arXiv e-Print_.
Jiang, H., Li, J., and Li, Z. (2020).“Determining the number of change-point via high-dimensional cross-validation.”
In: _Stat_ 9(1) (e284).


Jiang, P., Liu, Q., and Tse, Y. (2015).“International Asset Allocation with Regime Switching: Evidence from the
ETFs .” In: _Asia-Pacific Journal of Financial Studies_ 44(5), pp. 661–687.
Jochmann, M. and Koop, G. (2015).“Regime-switching cointegration.” In: _Studies in Nonlinear Dynamics and
Econometrics_ 19(1).
Jurczenko et al. (2020). _Machine Learning for Asset Management_. Ed. by E. Jurczenko. Wiley. 445 pp.
Kabran, F. B. and Unlu, K. D. (2021).“A two-step machine learning approach to predict S&P 500 bubbles.” In:
_Journal of Applied Statistics_ 48(13-15), pp. 2776–2794.
Kaihatsu, S. and Nakajima, J. (2015). _Has Trend Inflation Shifted? An Empirical Analysis with a Regime-Switching
Model_. Tech. rep. Bank of Japan.
Kakushadze, Z. and Yu, W. (2016).“Statistical Risk Models.” In: _SSRN e-Print_.
Kakushadze, Z. and Yu, W. (2017).“Open Source Fundamental Industry Classification.” In: _MDPI Data_ 22 (2).
Kakushadze, Z. and Yu, W. (2018a).“Betas, Benchmarks, and Beating the Market.” In: _The Journal of Trading_.
Kakushadze, Z. and Yu, W. (2018b).“Decoding stock market with quant alphas.” In: _Journal of Asset Management_ ,
pp. 1–11.
Kakushadze, Z. and Yu, W. (2019).“Machine learning risk models.” In: _SSRN e-Print_.
Kakushadze, Z. and Yu, W. (2020).“Machine learning treasury yields.” In: _SSRN e-Print_.
Kamenshchikov, S. (2016).“Bifurcation patterns of market regime transition.” In: _Quantitative Finance_ 16(11),
pp. 1631–1636.
Kasahara, H. and Shimotsu, K. (2017). “Testing the Number of Regimes in Markov Regime Switching Models.” In:
_Canadian Econometric Study Group (CESG)_.
Kasahara, H. and Shimotsu, K. (2019).“Testing the Order of Multivariate Normal Mixture Models.” In: _arXiv
e-Print_.
Kashif, M. and Leirvik, T. (2021).“Regime Switching Stock Returns and Hybrid Tail Risk.” In: _SSRN e-Print_.
Kaya, H. (2017).“Managing ambiguity in asset allocation.” In: _Journal of Asset Management_ 18(3), pp. 163–187.
Kelliher, C., Hazrachoudhury, A., and Irving, B. (2022).“A Novel Approach to Risk Parity: Diversification across
Risk Factors and Market Regimes.” In: _The Journal of Portfolio Management_ 48(3).
Khalili, A., Chen, J., and Stephens, D. A. (2016).“Regularization in Regime-Switching Gaussian Autoregressive
Models.” In: _Advanced Statistical Methods in Data Science_. Springer Singapore, pp. 13–34.
Kim, E.-c., Jeong, H.-w., and Lee, N.-y. (2019).“Global Asset Allocation Strategy Using a Hidden Markov Model.”
In: _Journal of Risk and Financial Management_ 12(4), p. 168.
Kim, Y. M. and Kang, K. H. (2022).“Bayesian Inference of Multivariate Regression Models with Endogenous
Markov Regime-Switching Parameters.” In: _Journal of Financial Econometrics_.
Koki, C., Leonardos, S., and Piliouras, G. (2022).“Exploring the predictability of cryptocurrencies via Bayesian
hidden Markov models.” In: _Research in International Business and Finance_ 59, p. 101554.
Kole, E. and van Dijk, D. (2016).“How to Identify and Forecast Bull and Bear Markets?” In: _Journal of Applied
Econometrics_ 32(1), pp. 120–139.
Komatsu, T. and Makimoto, N. (2015).“Dynamic Investment Strategy with Factor Models Under Regime Switches.”
In: _Asia-Pacific Financial Markets_ 22(2), pp. 209–237.
Kreuser, J. and Sornette, D. (2019).“Super-Exponential RE bubble model with efficient crashes.” In: _The European
Journal of Finance_ 25(4), pp. 338–368.
Kritzman, M., Kinlaw, W., and Turkington, D. (2017). _A Practitioner’s Guide to Asset Allocation_. Wiley. 256 pp.
Kritzman, M., Page, S., and Turkington, D. (2012).“Regime Shifts: Implications for Dynamic Strategies.” In:
_Financial Analysts Journal_ 68(3).
Kunjal, D., Peerbhai, F., and Muzindutsi, P.-F. (2021).“The performance of South African exchange traded funds
under changing market conditions.” In: _Journal of Asset Management_ 22(5), pp. 350–359.
Lai, K.-H., Zha, D., Wang, G., Xu, J., Zhao, Y., Kumar, D., Chen, Y., Zumkhawaka, P., Wan, M., Martinez, D.,
and Hu, X. (2021). “TODS: An Automated Time Series Outlier Detection System.” In: _arXiv e-Print_.
Lattanzi, C. and Leonelli, M. (2019).“A changepoint approach for the identification of financial extreme regimes.”
In: _arXiv e-Print_.
Lee, M.-C., Lin, J.-C., and Gran, E. G. (2020a).“ReRe: A Lightweight Real-time Ready-to-Go Anomaly Detection
Approach for Time Series.” In: _arXiv e-Print_.
Lee, S., Liao, Y., Seo, M. H., and Shin, Y. (2020b).“Factor-Driven Two-Regime Regression.” In: _arXiv e-Print_.
Lee, S., Liao, Y., Seo, M. H., and Shin, Y. (2021).“Factor-driven two-regime regression.” In: _Annals of Statistics_
49(3).


Lettau, M. and Pelger, M. (2020).“Factors That Fit the Time Series and Cross-Section of Stock Returns.” In: _The
Review of Financial Studies_ 33(5), pp. 2274–2325.
Lezmi, E., Malongo, H., Roncalli, T., and Sobotka, R. (2019).“Portfolio Allocation with Skewness Risk: A Practical
Guide.” In: _SSRN e-Print_.
Li, L. (2021).“Risk of investing in volatility products: A regime-switching approach.” In: _Investment Analysts
Journal_ 50(1), pp. 1–16.
Li, X. and Mulvey, J. M. (2021).“Portfolio Optimization Under Regime Switching and Transaction Costs: Combining
Neural Networks and Dynamic Programs.” In: _INFORMS Journal on Optimization_ 3(4), pp. 398–417.
Li, X. and Zakamulin, V. (2020).“Stock volatility predictability in bull and bear markets.” In: _Quantitative Finance_
20(7), pp. 1149–1167.
Li, Z., Liu, X.-Y., Zheng, J., Wang, Z., Walid, A., and Guo, J. (2021).“FinRL-Podracer: High Performance and
Scalable Deep Reinforcement Learning for Quantitative Finance.” In: _ACM International Conference on AI in
Finance_.
Liszewski, O. (2016).“Asset allocation under multiple regimes.” MA thesis. Erasmus University.
Liu, L., Chen, C., and Wang, B. (2022a).“Predicting financial crises with machine learning methods.” In: _Journal
of Forecasting_.
Liu, X.-Y., Rui, J., Gao, J., Yang, L., Yang, H., Wang, Z., Wang, C. D., and Guo, J. (2022b). “FinRL-Meta:
A Universe of Near-Real Market Environments for Data-Driven Deep Reinforcement Learning in Quantitative
Finance.” In: _arXiv e-Print_.
Liu, X.-Y., Yang, H., Gao, J., and Wang, C. (2021).“FinRL: Deep Reinforcement Learning Framework to Automate
Trading in Quantitative Finance.” In: _SSRN e-Print_.
Lopez de Prado, M. (2020). _Machine learning for asset managers_. Cambridge University Press. 190 pp.
Ma, Y., MacLean, L., Xu, K., and Zhao, Y. G. (2011).“Portfolio optimization model with regime-switching risk
factors for sector exchange traded funds.” In: _Pacific Journal of Optimization_ 7, pp. 455–470.
Malevergne, Y., Sornette, D., and Wei, R. (2021).“A model of financial bubbles and drawdowns with non-local
behavioral self-referencing.” In: _SSRN e-Print_.
Marinescu, M. (2022).“Risk-Based Optimal Portfolio Strategies: A Compendium.” In: _SSRN e-Print_.
Martin, R. (2021).“PyPortfolioOpt: portfolio optimization in Python.” In: _Journal of Open Source Software_ 6(61),
p. 3066.
Martirosyan, A. and Simonian, J. (2021).“Emerging Market Stock Momentum Returns during US Economic
Regimes.” In: _The Journal of Portfolio Management_ 47(7), pp. 27–45.
Marwood, D. and Minnen, D. (2020).“Safely Boosting Retirement Income by Harmonizing Drawdown Paths.” In:
_Journal of Financial Planning_ 33(11), pp. 46–60.
Maschner, C., Moritz, B., and Schmitz, M. (2021).“Modern Asset Management.” In: _SSRN e-Print_.
Massacci, D. (2014).“Multivariate Regime Switching Model with Flexible Threshold Variable.” In: _SSRN e-Print_.
Massacci, D. (2021).“Testing for Regime Changes in Portfolios with a Large Number of Assets: A Robust Approach
to Factor Heteroskedasticity.” In: _Journal of Financial Econometrics_.
Massacci, D. and Kapetanios, G. (2021).“Forecasting in Factor Augmented Regressions under Structural Change.”
In: _SSRN e-Print_.
McGee, R. (2021).“Can Market Regimes Really be Timed with Historical Volatility?” In: _SSRN e-Print_.
McIndoe, C. (2020).“A Data Driven Approach to Market Regime Classification.” MA thesis. Imperial College.
McQuarrie, E. F. (2021).“New Lessons from Market History: Sometimes Bonds Win.” In: _SSRN e-Print_.
Mehta, P. (2020).“The Mechanism behind the Bursting of Financial Bubbles and Market Crashes.” In: _SSRN
e-Print_.
Meitz, M. and Saikkonen, P. (2021).“Testing for observation-dependent regime switching in mixture autoregressive
models.” In: _Journal of Econometrics_ 222(1), pp. 601–624.
Messer, M. (2021).“Bivariate change point detection: joint detection of changes in expectation and variance.” In:
_arXiv e-Print_.
Micheli, A. and Neuman, E. (2022). “Evidence of Crowding on Russell 3000 Reconstitution Events.” In: _arXiv
e-Print_.
Milevsky, M. A. (2020). _Retirement Income Recipes in R: From Ruin Probabilities to Intelligent Drawdowns_. Springer
International Publishing. 302 pp.
Min, S., Song, R., and Zhu, W. (2021).“The 2021 Bitcoin Bubbles and Crashes – Detection and Classification.” In:
_SSRN e-Print_.


Mizuno, T., Ohnishi, T., and Watanabe, T. (2020).“Detecting Stock Market Bubbles Based on the Cross-Sectional
Dispersion of Stock Prices.” In: _Proceedings of the 23rd Asia Pacific symposium on intelligent and evolutionary
systems_. Ed. by H. Sato, S. Iwanaga, and A. Ishii. Vol. 12. Springer International Publishing, pp. 194–202.
Moreno-Pino, F., Sukei, E., Olmos, P. M., and Artes-Rodriguez, A. (2022). “PyHHMM: A Python Library for
Heterogeneous Hidden Markov Models.” In: _arXiv e-Print_.
Muller, S. and Preissler, F. (2021).“In Good and in Bad Times? The Relation between Anomaly Returns and
Market States.” In: _SSRN e-Print_.
Mulvey, J. M., Hao, H., and Li, N. (2018).“Machine learning, economic regimes and portfolio optimisation.” In:
_International Journal of Financial Engineering and Risk Management_ 2(4), p. 260.
Navarro, M., Allen, G. I., and Weylandt, M. (2021). “Network Clustering for Latent State and Changepoint Detec-
tion.” In: _arXiv e-Print_.
Neto, A. E. D., Gonzalo, J., and Pitarakis, J.-Y. (2021).“Uncovering regimes in out of sample forecast errors.” In:
_Oxford Bulletin of Economics and Statistics_ 83(3), pp. 713–741.
Nystrup, P. (2014).“Regime-Based Asset Allocation: Do Profitable Strategies Exist?” MA thesis. Technical Uni-
versity of Denmark.
Nystrup, P., Hansen, B. W., Larsen, H. O., Madsen, H., and Lindstrom, E. (2018a).“Dynamic Allocation or
Diversification: A Regime-Based Approach to Multiple Assets.” In: _The Journal of Portfolio Management_ 44(2),
pp. 62–73.
Nystrup, P., Hansen, B. W., Madsen, H., and Lindstrom, E. (2015).“Regime-Based Versus Static Asset Allocation:
Letting the Data Speak.” In: _The Journal of Portfolio Management_ 42(1), pp. 103–109.
Nystrup, P., Lindstrom, E., and Madsen, H. (2020).“Learning hidden Markov models with persistent states by
penalizing jumps.” In: _Expert Systems with Applications_ 150, p. 113307.
Nystrup, P., Madsen, H., and Lindstrom, E. (2018b).“Dynamic portfolio optimization across hidden market
regimes.” In: _Quantitative Finance_ 18(1), pp. 83–95.
Nystrup, P., William Hansen, B., Madsen, H., and Lindstrom, E. (2016).“Detecting change points in VIX and S&P
500: A new approach to dynamic asset allocation.” In: _Journal of Asset Management_ 17, pp. 361–374.
O’Cinneid, R. (2019).“Applications of machine learning in finance: analysis of international portfolio flows using
regime-switching models.” PhD thesis. University College Cork.
Odendahl, F., Rossi, B., and Sekhposyan, T. (2020).“Comparing Forecast Performance with State Dependence.”
In: _SSRN e-Print_.
Ohana, J.-J., Ohana, S., Benhamou, E., Saltiel, D., and Guez, B. (2021).“Explainable AI Models of Stock Crashes:
A Machine-Learning Explanation of the Covid March 2020 Equity Meltdown.” In: _SSRN e-Print_.
Oliveira, A. B. and Valls Pereira, P. L. (2018).“Asset Allocation With Markovian Regime Switching: Efficient
Frontier and Tangent Portfolio With Regime Switching.” In: _SSRN e-Print_.
Omerovic, S., Friedl, H., and Grun, B. (2021).“Modelling Multiple Regimes in Economic Growth by Mixtures of
Generalised Nonlinear Models.” In: _Econometrics and Statistics_.
Oprisor, R. and Kwon, R. (2021).“Multi-Period Portfolio Optimization with Investor Views under Regime Switch-
ing.” In: _Journal of Risk and Financial Management_ 14(1), p. 3.
Ou, L., Hunter, M. D., and Chow, S.-M. (2019).“Whats for dynr: A Package for Linear and Nonlinear Dynamic
Modeling in R.” In: _The R Journal_.
Pang, Z., Hu, Z., Tokmakov, P., Wang, Y.-X., and Hebert, M. (2021). “Unlocking the Full Potential of Small Data
with Diverse Supervision.” In: _arXiv e-Print_.
Papenbrock, J. and Schwendner, P. (2015).“Handling risk-on/risk-off dynamics with correlation regimes and cor-
relation networks.” In: _Financial Markets and Portfolio Management_ 29(2), pp. 125–147.
Perikos, I., Kardakis, S., and Hatzilygeroudis, I. (2021).“Sentiment analysis using novel and interpretable architec-
tures of Hidden Markov Models.” In: _Knowledge-Based Systems_ 229, p. 107332.
Perrin, S. and Roncalli, T. (2020).“Machine Learning Optimization Algorithms & Portfolio Allocation.” In: _Machine
Learning for Asset Management: New Developments and Financial Applications_. Ed. by E. Jurczenko. Wiley,
pp. 261–328.
Peters, E. (2015).“Stable vs. Unstable Markets: A Tale of Two States.” In: _SSRN e-Print_.
Pharasi, H. K., Seligman, E., Sadhukhan, S., and Seligman, T. H. (2020a).“Dynamics of market states and risk
assessment.” In: _arXiv e-Print_.
Pharasi, H. K., Seligman, E., and Seligman, T. H. (2020b).“Market states: A new understanding.” In: _arXiv e-Print_.


Pinto, J. M. and Castle, J. (2021). _A machine learning dynamic switching approach to forecasting when there are
structural breaks_. Tech. rep. University of Oxford.
Platanakis, E., Sakkas, A., and Sutcliffe, C. (2017).“Portfolios in a Regime Shifting Non-Normal World: Are
Alternative Assets Beneficial?” In: _European Financial Management Association Annual Meeting Athens_.
Prakash, A., James, N., Menzies, M., and Francis, G. (2021a).“Structural Clustering of Volatility Regimes for
Dynamic Trading Strategies.” In: _Applied Mathematical Finance_ 28(3), pp. 236–274.
Prakash, A., James, N., Menzies, M., and Francis, G. (2021b).“Structural clustering of volatility regimes for dynamic
trading strategies.” In: _arXiv e-Print_.
Procacci, P. F. and Aste, T. (2019).“Forecasting market states.” In: _Quantitative Finance_ 19(9), pp. 1491–1498.
Pruser, J. (2021).“Forecasting US inflation using Markov dimension switching.” In: _Journal of Forecasting_ 40(3),
pp. 481–499.
Qian, W., Rolling, C. A., Cheng, G., and Yang, Y. (2022).“Combining forecasts for universally optimal perfor-
mance.” In: _International Journal of Forecasting_.
Rao, A. and Jelvis, T. (2022). _Foundations of Reinforcement Learning with Applications in Finance_.
Rebonato, R. and El Aouadi, A. (2021).“How Do the Volatilities of Rates Depend on Their Level? The ”Universal
Relationship” Revisited.” In: _The Journal of Fixed Income_ 30(4), pp. 17–31.
Reher, G. and Wilfling, B. (2015).“A nesting framework for Markov-switching GARCH modelling with an appli-
cation to the German stock market.” In: _Quantitative Finance_ , pp. 1–16.
Ren, D. (2016).“Essays in Asset Pricing and Financial Econometrics.” PhD thesis. University of Guelph.
Reus, L. and Mulvey, J. M. (2016).“Dynamic allocations for currency futures under switching regimes signals.” In:
_European Journal of Operational Research_ 253(1), pp. 85–93.
Roncalli, T. (2021).“Advanced Course in Asset Management.” In: _SSRN e-Print_.
Ruff, L., Kauffmann, J. R., Vandermeulen, R. A., Montavon, G., Samek, W., Kloft, M., Dietterich, T. G., and
Muller, K.-R. (2021).“A Unifying Review of Deep and Shallow Anomaly Detection.” In: _arXiv e-Print_.
Samal, A., Pharasi, H. K., Ramaia, S. J., Kannan, H., Saucan, E., Jost, J., and Chakraborti, A. (2021).“Network
geometry and market instability.” In: _Royal Society Open Science_ 8(2).
Sarmas, E., Xidonas, P., and Doukas, H. (2020). _Multicriteria Portfolio Construction with Python_. Springer Inter-
national Publishing.
Sarwar, G., Mateus, C., and Todorovic, N. (2017).“A tale of two states: asymmetries in the UK small, value and
momentum premiums.” In: _Applied Economics_ 49(5), pp. 456–476.
Satchell, S. (2011).“Regime-switching in financial markets.” In: _Journal of Asset Management_ 12(5), p. 309.
Schatz, M. (2020).“Financial Modeling of Bubbles and Crashes.” PhD thesis. ETH Zurich.
Scherer, B. and Apel, M. (2020).“Business cycle-related timing of alternative risk premia strategies.” In: _The Journal
of Alternative Investments_ 22(4), pp. 8–24.
Seidl, I. (2012).“Markowitz versus Regime Switching: An Empirical Approach.” In: _The Review of Finance and
Banking_ 04(1), pp. 033–043.
Sharaiha, Y. M. and Johansson, K. K. (2014).“The state-dependent time variation in the value premium.” In:
_Journal of Asset Management_ 15(2), pp. 150–161.
Sharma, A., Syrgkanis, V., Zhang, C., and Kiciman, E. (2021). “DoWhy: Addressing Challenges in Expressing and
Validating Causal Assumptions.” In: _arXiv e-Print_.
Sheikh, A. Z. and Sun, J. (2012).“Regime Change: Implications of Macroeconomic Shifts on Asset Class and
Portfolio Performance.” In: _The Journal of Investing_ 21(3), pp. 36–54.
Shi, X., Xu, D., and Zhang, Z. (2022). “Deep Learning Algorithms for Hedging with Frictions.” In: _arXiv e-Print_.
Shi, X. (2020).“A Survey of Changepoint Techniques for Time Series Data.” PhD thesis. Clemson University.
Shi, X., Gallagher, C., Lund, R., and Killick, R. (2021).“A Comparison of Single and Multiple Changepoint
Techniques for Time Series Data.” In: _arXiv e-Print_.
Shu, M., Song, R., and Zhu, W. (2021).“The 2021 Bitcoin Bubbles and Crashes – Detection and Classification.”
In: _SSRN e-Print_.
Siebert, J., Gross, J., and Schroth, C. (2021).“A systematic review of Python packages for time series analysis.”
In: _Engineering Proceedings_ 5(1) (22).
Siliverstovs, B. and Wochner, D. (2021).“State-Dependent Evaluation of Predictive Ability.” In: _Journal of Fore-
casting_ 40(3), pp. 547–574.
Silveira, D. and Oscar, R. B. L. M. (2021).“Inflation Targeting Regimes in Emerging Market Economies: To Invest
or Not to Invest?” In: _SSRN e-Print_.


Simonian, J. (2020).“Mixed Ag: A Regime-Based Analysis of Multi-Asset Agriculture Portfolios.” In: _The Journal
of Portfolio Management_ 46(6), pp. 135–146.
Simonian, J. and Wu, C. (2019a).“Factors in Time: Fine-Tuning Hedge Fund Replication.” In: _The Journal of
Portfolio Management_ 45 (3), pp. 159–164.
Simonian, J. and Wu, C. (2019b).“Minsky vs. Machine: New Foundations for Quant-Macro Investing.” In: _The
Journal of Financial Data Science_ 1(2), pp. 94–110.
Simos, T. E., Mourtas, S. D., and Katsikis, V. N. (2021).“Time-varying Black–Litterman portfolio optimization
using a bio-inspired approach and neuronets.” In: _Applied Soft Computing_ 112, p. 107767.
Singh, A. and Singh, M. (2016). “Risk-Return Relationship in BRIC Equity Markets: Evidence from Markov Regime
Switching Model with Time-varying Transition Probabilities.” In: _Metamorphosis : A Journal of Management
Research_.
Smith, S. (2021).“International Stock Return Predictability and Asset Pricing Models.” In: _SSRN e-Print_.
Smith, S. C., Bulkley, G., and Leslie, D. S. (2020).“Equity Premium Forecasts with an Unknown Number of
Structural Breaks.” In: _Journal of Financial Econometrics_ 18(1), pp. 59–94.
Smith, S. C. and Timmermann, A. (2021).“Break Risk.” In: _The Review of Financial Studies_ 34(4), pp. 2045–2100.
Smug, D., Ashwin, P., and Sornette, D. (2017).“Predicting Financial Market Crashes Using Ghost Singularities.”
In: _SSRN e-Print_.
Snow, D. (2019).“Machine learning in asset management.” In: _SSRN e-Print_.
Snow, D. (2020a).“Machine Learning in Asset Management - Part 2: Portfolio Construction - Weight Optimization.”
In: _The Journal of Financial Data Science_ 2 (2), pp. 17–24.
Snow, D. (2020b).“Machine Learning in Asset Management Part 1: Portfolio Construction Trading Strategies.” In:
_The Journal of Financial Data Science_ 2(1) (1), pp. 10–23.
Sornette, D. (2014).“Dragon-kings and Predictions: Diagnostics and Forecasts for the World Financial Crisis.” In:
_SSRN e-Print_.
Sornette, D., Andraszewicz, S., Murphy, R. O., Rindler, P. B., and Sanadgol, D. (2016).“Resolving Persistent
Uncertainty by Self-Organized Consensus to Mitigate Market Bubbles.” In: _SSRN e-Print_.
Sornette, D. and Cauwels, P. (2014).“Financial bubbles: mechanisms and diagnostics.” In: _arXiv e-Print_.
Sornette, D., Cauwels, P., and Smilyanov, G. (2017).“Can We Use Volatility to Diagnose Financial Bubbles? Lessons
from 40 Historical Bubbles.” In: _SSRN e-Print_.
Sornette, D., Demos, G., Zhang, Q., Cauwels, P., Filimonov, V., and Zhang, Q. (2015).“Real-time prediction and
post-mortem analysis of the Shanghai 2015 stock market bubble and crash.” In: _Journal of Investment Strategies_
4(4).
SSgA Research (2015). _Optimizing asset allocations to market regimes_. Tech. rep. State Street Global Advisors.
Stillwagon, J. and Sullivan, P. (2020).“Markov switching in exchange rate models: will more regimes help?” In:
_Empirical Economics_ , pp. 413–436.
Sueppel, R. (2021). _Classifying market regimes_. Tech. rep. Systematic Risk and Systematic Value.
Tachibana, M. (2020).“Flight-to-quality in the stock-bond return relation: a regime-switching copula approach.”
In: _Financial Markets and Portfolio Management_ 34, pp. 429–470.
Tajeuna, E. G., Bouguessa, M., and Wang, S. (2022). “Modeling Regime Shifts in Multiple Time Series.” In: _arXiv
e-Print_.
Tatsat, H., Puri, S., and Lookabaugh, B. (2020). _Machine Learning and Data Science Blueprints for Finance: From
Building Trading Strategies to Robo-Advisors Using Python_. O’Reilly. 400 pp.
Tran, B.-H., Rossi, S., Milios, D., Michiardi, P., Bonilla, E. V., and Filippone, M. (2021). “Model Selection for
Bayesian Autoencoders.” In: _arXiv e-Print_.
Tu, J. (2010).“Is Regime Switching in Stock Returns Important in Portfolio Decisions?” In: _Management Science_
56, pp. 1198–1215.
Tuck, J., Barratt, S., and Boyd, S. (2022).“Portfolio Construction Using Stratified Models.” In: _Machine Learning
in Financial Markets: A guide to contemporary practices_. Ed. by A. Capponi and C.-A. Lehalle. Cambridge
University Press.
Ungolo, F., Sherris, M., and Zhou, Y. (2021).“affine_mortality: A Github repository for estimation, analysis, and
projection of affine mortality models.” In: _SSRN e-Print_.
Uysal, A. S. and Mulvey, J. M. (2021).“A Machine Learning Approach in Regime-Switching Risk Parity Portfolios.”
In: _The Journal of Financial Data Science_ 3(2), pp. 87–108.


Uysal, S. (2021).“Risk Budgeting Portfolios Under a Modern Optimization and Machine Learning Lens.” PhD
thesis. Princeton University.
Vamossy, D. and Skog, R. (2021). “EmTract: Investor Emotions and Market Behavior.” In: _arXiv e-Print_.
van den Burg, G. J. J. and Williams, C. K. I. (2022).“An Evaluation of Change Point Detection Algorithms.” In:
_arXiv e-Print_.
van Vliet, P. and Blitz, D. (2011).“Dynamic strategic asset allocation: Risk and return across the business cycle.”
In: _Journal of Asset Management_ 12(5), pp. 360–375.
Vanini, P. (2020).“Asset Management.” In: _SSRN e-Print_.
Viebig, J. (2020).“Exuberance in Financial Markets: Evidence from Machine Learning Algorithms.” In: _Journal of
Behavioral Finance_ 21(2), pp. 128–135.
Vinod, H. D. (2021).“R Package GeneralCorr Functions for Portfolio Choice.” In: _SSRN e-Print_.
Vo, H. T. and Maurer, R. (2013).“Dynamic Asset Allocation under Regime Switching, Predictability and Parameter
Uncertainty.” In: _SSRN e-Print_.
Wang, J., Ma, F., Liang, C., and Chen, Z. (2022).“Volatility forecasting revisited using Markov-switching with
time-varying probability transition.” In: _International Journal of Finance & Economics_.
Wang, P. and Zong, L. (2020).“Are Crises Predictable? A Review of the Early Warning Systems in Currency and
Stock Markets.” In: _arXiv e-Print_.
Wang, R., Nie, K., Chang, Y.-J., Gong, X., Wang, T., Yang, Y., and Long, B. (2020).“Deep Learning for Anomaly
Detection.” In: _Proceedings of the 26th ACM SIGKDD International Conference on Knowledge Discovery & Data
Mining_. ACM.
Wang, X. and Hsieh, F. (2021). “Unraveling S&P500 stock volatility and networks – An encoding-and-decoding
approach.” In: _arXiv e-Print_.
Wehrli, A. and Sornette, D. (2022).“Classification of flash crashes using the Hawkes(p,q) framework.” In: _Quanti-
tative Finance_ 22(2), pp. 213–240.
Werge, N. (2021). “Predicting Risk-adjusted Returns using an Asset Independent Regime-switching Model.” In:
_arXiv e-Print_.
Wheatley, S., Sornette, D., Huber, T., Reppen, M., and Gantner, R. N. (2018).“Are bitcoin bubbles predictable?
combining a generalized metcalfe’s law and the LPPLS model.” In: _SSRN e-Print_.
Wolchover, N. (2018).“Machine Learning’s ’Amazing’ Ability to Predict Chaos.” In: _Quanta Magazine_.
Wood, K., Giegerich, S., Roberts, S., and Zohren, S. (2022). “Trading with the Momentum Transformer: An Intel-
ligent and Interpretable Architecture.” In: _arXiv e-Print_.
Wu, R. and Keogh, E. J. (2021).“Current Time Series Anomaly Detection Benchmarks are Flawed and are Creating
the Illusion of Progress.” In: _arXiv e-Print_.
Wu, Y. (2020).“On the Predictive Performance of the Stock Returns by Using the Markov-Switching Models.”
MA thesis. University of Uppsala.
Yan, C. and Huang, K. X. D. (2020).“Financial cycle and business cycle: An empirical analysis based on the data
from the U.S.” In: _Economic Modelling_ 93, pp. 693–701.
Yang, Y., UY, M. C. S., and Huang, A. (2020). “FinBERT: A Pretrained Language Model for Financial Commu-
nications.” In: _arXiv e-Print_.
Yao, C.-Z. and Li, H.-Y. (2021).“A study on the bursting point of Bitcoin based on the BSADF and LPPLS
methods.” In: _The North American Journal of Economics and Finance_ (101280).
Yu, L., Hardle, W. K., Borke, L., and Benschop, T. (2020).“An AI approach to measuring financial risk.” In: _SSRN
e-Print_.
Zakamulin, V. (2020).“Not All Bull and Bear Markets Are Alike: Insights From a Five-State Hidden Semi-Markov
Model .” In: _SSRN e-Print_.
Zaremba, A., Czapkiewicz, A., and Kambouris, G. D. (2020).“A Tale of Two States: An Application of a Markov
Switching Model to Anomaly Returns.” In: _Eurasian Studies in Business and Economics_. Springer International
Publishing, pp. 227–240.
Zhang, Q., Sornette, D., Balcilar, M., Gupta, R., Ozdemir, Z. A., and Yetkiner, H. (2016).“LPPLS bubble indicators
over two centuries of the S&P 500 index.” In: _Physica A: Statistical Mechanics and its Applications_ 458, pp. 126–
139.
Zhao, D. and Sornette, D. (2022).“Bubbles for Fama from Sornette.” In: _SSRN e-Print_.
Zheng, K., Li, Y., and Xu, W. (2021).“Regime switching model estimation: spectral clustering hidden Markov
model .” In: _Annals of Operations Research_ 303(1-2), pp. 297–319.


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


