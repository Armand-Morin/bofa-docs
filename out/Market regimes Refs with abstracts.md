References with abstracts for QWIMproject: machine learning (and
more) applied to market regimes, changepoints, bubbles and crashes in
quantitative wealth and investment management
Cristian Homescu
December 2022
Abstract
This document includes the list of references (including abstracts) for this QWIM project
Contents
1 Motivation for the project 2
1\.1 Market states in QWIM. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2
1\.2 Structural breaks: market regimes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
1\.3 Structural breaks: bubbles and crashes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
1\.4 Structural breaks: changepoints . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
2 Relevant references 4
2\.1 Main references . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
2\.2 Comprehensive list of references . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
2\.2\.1 Regime\-based asset allocation, portfolio construction and investment strategies . . . . . . . . 5
2\.2\.2 Number of market regimes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
2\.2\.3 Market states, regimes, changepoints and structural breaks of time series within context of
QWIM. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
2\.2\.4 Market states, regimes, changepoints and structural breaks of time series . . . . . . . . . . . 9
2\.2\.5 Detection and usage of bubbles, crashes and business cycles within context of QWIM . . . .10
2\.2\.6 Detection and usage of bubbles, crashes and business cycles . . . . . . . . . . . . . . . . . . . 11
2\.2\.7 Forecasting under data regimes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
2\.2\.8 Numerical methods, models and their implementations to model and analyze data regimes . .13
References 14
11 Motivation for the project
There is much evidence that crash and bubble periods display much different patterns than normal markets, sug\-
gesting that forecasting models (and investing approaches) ought to be based on multiple regimes.
It was shown that asset performance over long time periods can be separated into distinctive periods, called
regimes, which display common characteristics. Regime\-based asset allocation has been shown to add value over
rebalancing to static weights and, in particular, reduce potential drawdowns by reacting to changes in market
conditions. regime based asset allocation can effectively respond to changes in financial regimes at the portfolio
level, in an effort to provide better long\-term results than more static approaches can offer.
BaltasandKaryampas(“Forecastingtheequityrisk premium: Theimportanceof regime\-dependentevaluation,”
2018\):
”Is superior econometric predictability across the business cycle synonymous with predictability at all times?”
It appears that recently introduced forecasting models for equity risk premium ERP, which have been shown to
generate econometrically superior ERP forecasts, have forecasting ability which is regime\-dependent. They give rise
to significant relative losses during market downturns, when it matters the most for asset allocators to retain assets
and their client base intact. Conversely, any economic benefit occurring during market upswings is diminished for
high risk\-averse and leverage\-constrained investors.
1\.1 Market states in QWIM
It was observed empirically that there are two separate market states:
•low uncertainty (relatively stable and resilient) market
•high uncertainty (relatively chaotic and fragile) market
Markets in “low uncertainty ”state:
•statistically well behaved
•can be modeled using standard statistical tools
•volatility is stable and low
•correlations relatively stable
•tail events ( 3 std deviations in either direction) quite rare.
Markets in ”high uncertainty ”state:
•not statistically well behaved
•vols and correlations change significantly on regular basis
•Tail events happen with much more regularity
To account for the two market states, practitioners use a relatively similar concept of ”risk on, risk off” :
The“high uncertainty” state can incorporate multiple instances and multiple types of significant changes in
time series:
•market regimes
•changepoints
•bubbles and crashes
21\.2 Structural breaks: market regimes
Regimechanges, sometransitory, somerecurring(recessionsversusexpansions)somepermanent(structuralbreaks),
are prevalent across a wide range of financial markets and in behavior of many macro variables. Examples of regimes
considered in academia and/or practitioners:
•bull vs. bear market regimes
•inflationary vs. recessionary regimes
•high vs. low volatility regimes
•mean reverting vs. trending regimes
Regime shifts are challenging for investors because they cause portfolio performance, risk and behavior to depart
significantly from ranges implied by long\-term averages of means and covariances. Regime\-based asset allocation
was shown to deliver improved performance and risk profile
Goof performance of investment strategies greatly enhanced with introduction of regime switching models RSMs
.RSMs characterize market states using estimates of parameters of some underlying model, and use a transition
matrix to quantify probability of moving from one state to another.
MLmaybeeffectiveatdetectingchange(eveninchaoticsystem), forexamplethroughrobustanomalydetection.
It can be enhanced to compute probability of observation in previously observed “market regimes” (defined as
clusters in ML). Thus clustering algorithms can identify regimes in datasets. What they have in common with
regular regime switching models is ability of producing probabilities of “switching” into another regime. MLcan
also feed on large amounts of data to detect preconditions of a break
1\.3 Structural breaks: bubbles and crashes
Chaotic systems of the real world are comparable to stock market indices evolution.Llog\-periodic power law sin\-
gularity (LPPLS) model captures well bubbles and crashes LPPLS framework successfully captures, ex\-ante, most
prominent bubbles across different time scales (Black Monday, Dot\-com, and Subprime Crisis).
1\.4 Structural breaks: changepoints
Change point detection (CPD) is the problem of finding abrupt changes in data when a property of the time series
changes . Segmentation, edge detection, event detection, and anomaly detection are similar concepts within ML
space.
Traditional changepoint detection methods only look for statistically\-detectable boundaries that are defined as
abrupt variations in the generative parameters of a data sequence. . However, it is observed that breakpoints occur
on more subtle boundaries non\-trivial to detect with these statistical methods, but detectable using deep learning
32 Relevant references
2\.1 Main references
List of references:
Akioyamen et al. (“A Hybrid Learning Approach to Detecting Regime Switches in Financial Markets,” 2021\)
Bae et al. (“Dynamic asset allocation for varied financial markets under regime switching framework,” 2014\)
Baitinger and Flegel (“The better turbulence index? Forecasting adverse financial markets regimes with persis\-
tent homology,” 2021\)
Benhamou et al. (“Explainable AI (XAI) Models Applied to Planning in Financial Markets,” 2021\)
Benhamouetal.(“DetectingandAdaptingtoCrisisPatternwithContextBasedDeepReinforcementLearning,”
2021\)
Bhansali and Holdom (“Good States, Bad States: What Do Options Tell Us About Schizophrenic Behavior of
Mr. Market and What Can We Do About It?” 2021\)
Bilokon et al. (“Market regime classification with signatures,” 2021\)
Botte and Bao ( A Machine Learning Approach to Regime Modeling , 2021\)
Bucci and Ciciretti (“Market Regime Detection via Realized Covariances: A Comparison between Unsupervised
Learning and Nonlinear Models,” 2021\)
Campani et al. (“Optimal portfolio strategies in the presence of regimes in asset returns,” 2021\)
Chalkis et al. (“Modeling of crisis periods in stock markets,” 2021\)
Clacher et al. (“A Practical Guide to Regime Switching in Financial Economics,” 2015\)
Costa and Kwon (“Risk parity portfolio optimization under a Markov regime\-switching framework,” 2019\)
Costa and Kwon (“A regime\-switching factor model for mean\-variance optimization,” 2020\)
Dai et al. (“Robo\-Advising: A Dynamic Mean\-Variance Approach,” 2021\)
Dal Pra et al. (“Regime Shifts in Excess Stock Return Predictability: An Out\-of\-Sample Portfolio Analysis,”
2018\)
Das et al. (“Optimal Goals\-Based Investment Strategies For Switching Between Bull and Bear Markets,” 2021\)
Das et al. (“Optimal Goals\-Based Investment Strategies For Switching Between Bull and Bear Markets,” 2022\)
Demos and Sornette (“Birth or burst of financial bubbles: which one is easier to diagnose?” 2017\)
Filimonov et al. (“Modified profile likelihood inference and interval forecast of the burst of financial bubbles,”
2017\)
Fischer and Murg (“A combined regime\-switching and Black Litterman model for optimal asset allocation,”
2015\)
Flint et al. (“Defining and measuring portfolio diversification,” 2021\)
Flint and du Plooy (“Extending risk budgeting for market regimes and quantile factor models,” 2018\)
Fons et al. (“A novel dynamic asset allocation system using Feature Saliency Hidden Markov models for smart
beta investing,” 2021\)
Gatumel and Ielpo (“The Number of Regimes Across Asset Returns: Identification and Economic Value,” 2014\)
Gu and Mulvey (“Factor Momentum and Regime\-Switching Overlay Strategy,” 2021\)
Hallac et al. (“Greedy Gaussian segmentation of multivariate time series,” 2019\)
Harvey et al. (“Real\-Time Detection of Regimes of Predictability in the U.S. Equity Premium,” 2021\)
Hao (“A Regime\-Aware Agent\-Based Framework for Financial Planning,” 2019\)
HeckensandGuhr(“Anewattempttoidentifylong\-termprecursorsforendogenousfinancialcrisesinthemarket
correlation structures,” 2022\)
Horvath et al. (“Clustering Market Regimes Using the Wasserstein Distance,” 2021\)
Jacquier et al. (“Market regime classification with signatures,” 2021\)
Kaya (“Managing ambiguity in asset allocation,” 2017\)
Kelliher et al. (“A Novel Approach to Risk Parity: Diversification across Risk Factors and Market Regimes,”
2022\)
Kunjal et al. (“The performance of South African exchange traded funds under changing market conditions,”
2021\)
Lattanzi and Leonelli (“A changepoint approach for the identification of financial extreme regimes,” 2019\)
Lezmi et al. (“Portfolio Allocation with Skewness Risk: A Practical Guide,” 2019\)
Li and Mulvey (“Portfolio Optimization Under Regime Switching and Transaction Costs: Combining Neural
Networks and Dynamic Programs,” 2021\)
4Li and Zakamulin (“Stock volatility predictability in bull and bear markets,” 2020\)
Liu et al. (“Predicting financial crises with machine learning methods,” 2022\)
McIndoe (“A Data Driven Approach to Market Regime Classification,” 2020\)
Messer (“Bivariate change point detection: joint detection of changes in expectation and variance,” 2021\)
Mizuno et al. (“Detecting Stock Market Bubbles Based on the Cross\-Sectional Dispersion of Stock Prices,” 2020\)
Nystrup et al. (“Dynamic Allocation or Diversification: A Regime\-Based Approach to Multiple Assets,” 2018\)
Nystrup et al. (“Dynamic portfolio optimization across hidden market regimes,” 2018\)
Nystrup et al. (“Learning hidden Markov models with persistent states by penalizing jumps,” 2020\)
Nystrup et al. (“Detecting change points in VIX and S\&P 500: A new approach to dynamic asset allocation,”
2016\)
Nystrup et al. (“Regime\-Based Versus Static Asset Allocation: Letting the Data Speak,” 2015\)
Oprisor and Kwon (“Multi\-Period Portfolio Optimization with Investor Views under Regime Switching,” 2021\)
Pharasi et al. (“Market states: A new understanding,” 2020\)
Procacci and Aste (“Forecasting market states,” 2019\)
Schatz (“Financial Modeling of Bubbles and Crashes,” 2020\)
Shi et al. (“A Comparison of Single and Multiple Changepoint Techniques for Time Series Data,” 2021\)
Simonian (“Mixed Ag: A Regime\-Based Analysis of Multi\-Asset Agriculture Portfolios,” 2020\)
Simonian and Wu (“Factors in Time: Fine\-Tuning Hedge Fund Replication,” 2019\)
Sornette et al. (“Can We Use Volatility to Diagnose Financial Bubbles? Lessons from 40 Historical Bubbles,”
2017\)
Stillwagon and Sullivan (“Markov switching in exchange rate models: will more regimes help?” 2020\)
Sueppel ( Classifying market regimes , 2021\)
Tajeuna et al. (“Modeling Regime Shifts in Multiple Time Series,” 2022\)
Tu (“Is Regime Switching in Stock Returns Important in Portfolio Decisions?” 2010\)
Uysal and Mulvey (“A Machine Learning Approach in Regime\-Switching Risk Parity Portfolios,” 2021\)
Wheatley et al. (“Are bitcoin bubbles predictable? combining a generalized metcalfe’s law and the LPPLS
model,” 2018\)
Zakamulin (“Not All Bull and Bear Markets Are Alike: Insights From a Five\-State Hidden Semi\-Markov Model,”
2020\)
Zhao and Sornette (“Bubbles for Fama from Sornette,” 2022\)
2\.2 Comprehensive list of references
2\.2\.1 Regime\-based asset allocation, portfolio construction and investment strategies
List of references:
Ahmad and Sehgal (“Regime shifts and volatility in BRIICKS stock markets: an asset allocation perspective,”
2015\)
Ahmad et al. (“Regime dependent dynamics and European stock markets: Is asset allocation really possible?”
2015\)
Ang and Bekaert (“How do Regimes Affect Asset Allocation,” 2004\)
Bae et al. (“Dynamic asset allocation for varied financial markets under regime switching framework,” 2014\)
Berger and Gencay (“Short\-run wavelet\-based covariance regimes for applied portfolio management,” 2020\)
Bhansali and Holdom (“Good States, Bad States: What Do Options Tell Us About Schizophrenic Behavior of
Mr. Market and What Can We Do About It?” 2021\)
Blin et al. (“A Macro Risk\-Based Approach to Alternative Risk Premia Allocation,” 2017\)
Blitz and Van Vliet (“Dynamic Strategic Asset Allocation: Risk and Return Across Economic Regimes,” 2009\)
BNYMellon Research ( Great expectations: regime based asset allocation seeks higher return, lower drawdowns ,
2013\)
Bradrania and Neghab (“State\-dependent asset allocation using neural networks,” 2022\)
Campani et al. (“Optimal portfolio strategies in the presence of regimes in asset returns,” 2021\)
Chen and Yang (“Markowitz’s Mean\-Variance Asset\-Liability Management with Regime Switching: A Multi\-
Period Model,” 2011\)
Cheng et al. (“Trending Fast and Slow,” 2021\)
Costa and Kwon (“Risk parity portfolio optimization under a Markov regime\-switching framework,” 2019\)
5Dai et al. (“Robo\-Advising: A Dynamic Mean\-Variance Approach,” 2021\)
Dapena et al. (“Risk On\-Risk Off: A Regime Switching Model for Active Portfolio Management,” 2020\)
Das et al. (“Optimal Goals\-Based Investment Strategies For Switching Between Bull and Bear Markets,” 2022\)
Dou et al. (“Cross\-region and cross\-sector asset allocation with regimes,” 2014\)
Elkamhi et al. (“Portfolio Tilts using Views on Macroeconomic Regimes,” 2021\)
Erlwein et al. (“HMM based scenario generation for an investment optimisation problem,” 2012\)
Erlwein\-Sayer et al. (“Portfolio Strategies and Estimation in a Hidden Markov Model Using State Dependent,
State Independent or No Correlation,” 2016\)
Fischer and Murg (“A combined regime\-switching and Black Litterman model for optimal asset allocation,”
2015\)
Flint and Mare (“Regime\-Based Tactical Allocation for Equity Factors and Balanced Portfolios,” 2019\)
Flint and du Plooy (“Extending risk budgeting for market regimes and quantile factor models,” 2018\)
Fons et al. (“A novel dynamic asset allocation system using Feature Saliency Hidden Markov models for smart
beta investing,” 2021\)
Gkatzilakis and Sivasubramanian (“Active Allocation of Smart Beta Indices based on Factor Timing and Regime
Switching,” 2014\)
Gu and Mulvey (“Factor Momentum and Regime\-Switching Overlay Strategy,” 2021\)
Guidolin and Timmermann (“International asset allocation under regime switching, skew, and kurtosis prefer\-
ences,” 2008\)
Guidolin (“Markov Switching in Portfolio Choice and Asset Pricing Models: A Survey,” 2011\)
Hu et al. (“Mean variance asset liability management with regime switching,” 2022\)
Iqbal (“Application of Regime Switching and Random Matrix Theory for Portfolio Optimization,” 2018\)
James (“Evolutionary correlation, regime switching, spectral dynamics and optimal trading strategies for cryp\-
tocurrencies and equities,” 2021\)
Jiang et al. (“International Asset Allocation with Regime Switching: Evidence from the ETFs,” 2015\)
Kelliher et al. (“A Novel Approach to Risk Parity: Diversification across Risk Factors and Market Regimes,”
2022\)
Kim et al. (“Global Asset Allocation Strategy Using a Hidden Markov Model,” 2019\)
Kritzman et al. (“Regime Shifts: Implications for Dynamic Strategies,” 2012\)
Kunjal et al. (“The performance of South African exchange traded funds under changing market conditions,”
2021\)
Lezmi et al. (“Portfolio Allocation with Skewness Risk: A Practical Guide,” 2019\)
Li (“Risk of investing in volatility products: A regime\-switching approach,” 2021\)
Li and Mulvey (“Portfolio Optimization Under Regime Switching and Transaction Costs: Combining Neural
Networks and Dynamic Programs,” 2021\)
Liszewski (“Asset allocation under multiple regimes,” 2016\)
Nystrup et al. (“Dynamic portfolio optimization across hidden market regimes,” 2018\)
Nystrup et al. (“Regime\-Based Versus Static Asset Allocation: Letting the Data Speak,” 2015\)
Nystrup et al. (“Dynamic Allocation or Diversification: A Regime\-Based Approach to Multiple Assets,” 2018\)
Oliveira and Valls Pereira (“Asset Allocation With Markovian Regime Switching: Efficient Frontier and Tangent
Portfolio With Regime Switching,” 2018\)
Oprisor and Kwon (“Multi\-Period Portfolio Optimization with Investor Views under Regime Switching,” 2021\)
Reus and Mulvey (“Dynamic allocations for currency futures under switching regimes signals,” 2016\)
Scherer and Apel (“Business cycle\-related timing of alternative risk premia strategies,” 2020\)
Seidl (“Markowitz versus Regime Switching: An Empirical Approach,” 2012\)
Sharaiha and Johansson (“The state\-dependent time variation in the value premium,” 2014\)
Sheikh and Sun (“Regime Change: Implications of Macroeconomic Shifts on Asset Class and Portfolio Perfor\-
mance,” 2012\)
Simonian (“Mixed Ag: A Regime\-Based Analysis of Multi\-Asset Agriculture Portfolios,” 2020\)
SSgA Research ( Optimizing asset allocations to market regimes , 2015\)
Stillwagon and Sullivan (“Markov switching in exchange rate models: will more regimes help?” 2020\)
Tachibana (“Flight\-to\-quality in the stock\-bond return relation: a regime\-switching copula approach,” 2020\)
van Vliet and Blitz (“Dynamic strategic asset allocation: Risk and return across the business cycle,” 2011\)
6VoandMaurer(“DynamicAssetAllocationunderRegimeSwitching,PredictabilityandParameterUncertainty,”
2013\)
Wang and Hsieh (“Unraveling S\&P500 stock volatility and networks – An encoding\-and\-decoding approach,”
2021\)
Wood et al. (“Trading with the Momentum Transformer: An Intelligent and Interpretable Architecture,” 2022\)
2\.2\.2 Number of market regimes
List of references:
Gatumel and Ielpo (“The Number of Regimes Across Asset Returns: Identification and Economic Value,” 2014\)
Horvath et al. (“Clustering Market Regimes Using the Wasserstein Distance,” 2021\)
Kasahara and Shimotsu (“Testing the Number of Regimes in Markov Regime Switching Models,” 2017\)
Ma et al. (“Portfolio optimization model with regime\-switching risk factors for sector exchange traded funds,”
2011\)
Massacci (“Multivariate Regime Switching Model with Flexible Threshold Variable,” 2014\)
Nystrup et al. (“Detecting change points in VIX and S\&P 500: A new approach to dynamic asset allocation,”
2016\)
Prakash et al. (“Structural Clustering of Volatility Regimes for Dynamic Trading Strategies,” 2021\)
Stillwagon and Sullivan (“Markov switching in exchange rate models: will more regimes help?” 2020\)
Zakamulin (“Not All Bull and Bear Markets Are Alike: Insights From a Five\-State Hidden Semi\-Markov Model,”
2020\)
2\.2\.3 Market states, regimes, changepoints and structural breaks of time series within context of
QWIM
List of references:
Ahelegbey et al. (“Modeling Turning Points In Global Equity Market,” 2020\)
Akioyamen et al. (“A Hybrid Learning Approach to Detecting Regime Switches in Financial Markets,” 2021\)
Alberico et al. (“Regime identification for sovereign bond portfolio construction,” 2018\)
Ang and Timmermann (“Regime Changes and Financial Markets,” 2012\)
Angelini et al. (“Uncertainty across volatility regimes,” 2019\)
Arago and Salvador (“Non\-linear Tradeoff between Risk and Return: A Regime\-switching Multi\-factor Frame\-
work,” 2013\)
Bae et al. (“Dynamic asset allocation for varied financial markets under regime switching framework,” 2014\)
Baitinger and Flegel (“The better turbulence index? Forecasting adverse financial markets regimes with persis\-
tent homology,” 2021\)
Balcerak and Schmelzer (“Constructing trading strategy ensembles by classifying market states,” 2020\)
Baltas and Karyampas (“Forecasting the Equity Risk Premium: The Importance of Regime\-Dependent Evalu\-
ation,” 2020\)
Barkai et al. (“A Cryptocurrency Risk\-Return Analysis for Bull and Bear Regimes,” 2021\)
Benhamou et al. (“Explainable AI (XAI) Models Applied to Planning in Financial Markets,” 2021\)
Benhamouetal.(“DetectingandAdaptingtoCrisisPatternwithContextBasedDeepReinforcementLearning,”
2021\)
Benhamou et al. (“Planning in Financial Markets in Presence of Spikes: Using Machine Learning GBDT,” 2021\)
Bernhart et al. (“Asset Correlations in Turbulent Markets and the Impact of Different Regimes on Asset Man\-
agement,” 2011\)
Billio et al. (“Evaluation of Regime Switching Models for Real\-Time Business Cycle Analysis of the Euro Area,”
2013\)
Bilokon et al. (“Market regime classification with signatures,” 2021\)
Botte and Bao ( A Machine Learning Approach to Regime Modeling , 2021\)
Bucci and Ciciretti (“Market Regime Detection via Realized Covariances: A Comparison between Unsupervised
Learning and Nonlinear Models,” 2021\)
Campani et al. (“Optimal portfolio strategies in the presence of regimes in asset returns,” 2021\)
Chalkis et al. (“Modeling of crisis periods in stock markets,” 2021\)
7Chen and Tsang ( Detecting regime change in computational finance: data science, machine learning and algo\-
rithmic trading , 2020\)
Chenetal.(“Clusteringcommoditymarketsinspaceandtime: Clarifyingreturns, volatility, andtradingregimes
through unsupervised machine learning,” 2021\)
Clacher et al. (“A Practical Guide to Regime Switching in Financial Economics,” 2015\)
Corbelli et al. (“Investigating Optimal Regimes for Prediction in the Stock Market,” 2020\)
Costa and Kwon (“Risk parity portfolio optimization under a Markov regime\-switching framework,” 2019\)
Costa and Kwon (“A regime\-switching factor model for mean\-variance optimization,” 2020\)
Dal Pra et al. (“Regime Shifts in Excess Stock Return Predictability: An Out\-of\-Sample Portfolio Analysis,”
2018\)
Das et al. (“Optimal Goals\-Based Investment Strategies For Switching Between Bull and Bear Markets,” 2021\)
Dias et al. (“Clustering financial time series: New insights from an extended hidden Markov model,” 2015\)
Duprey and Klaus (“How to Predict Financial Stress? An Assessment of Markov Switching Models,” 2017\)
Edirisinghe and Zhao (“Smart Indexing Under Regime\-Switching Economic States,” 2020\)
Elouai et al. (“Bubbles and Regimes: Two Complementary Approaches,” 2013\)
Endres and Stubinger (“A flexible regime switching model with pairs trading application to the S\&P 500 high\-
frequency stock returns,” 2019\)
Filimonov et al. (“Modified profile likelihood inference and interval forecast of the burst of financial bubbles,”
2017\)
Flint et al. (“Defining and measuring portfolio diversification,” 2021\)
Fischer and Murg (“A combined regime\-switching and Black Litterman model for optimal asset allocation,”
2015\)
Fulop and Yu (“Bayesian analysis of bubbles in asset prices,” 2017\)
Gallagher et al. (“Using Smooth Transition Regressions to Model Risk Regimes,” 2020\)
Gao et al. (“Long memory or regime switching in volatility? Evidence from high\-frequency returns on the U.S.
stock indices,” 2018\)
Gatumel and Ielpo (“The Number of Regimes Across Asset Returns: Identification and Economic Value,” 2014\)
Glasserman et al. (“Dynamic information regimes in financial markets,” 2021\)
Haase and Neuenkirch (“Predictability of Bull and Bear Markets: A New Look at Forecasting Stock Market
Regimes (and Returns) in the U.S.,” 2021\)
Hao (“A Regime\-Aware Agent\-Based Framework for Financial Planning,” 2019\)
Harvey et al. (“Real\-Time Detection of Regimes of Predictability in the U.S. Equity Premium,” 2021\)
Hauptmann et al. (“Forecasting market turbulence using regime\-switching models,” 2014\)
HeckensandGuhr(“Anewattempttoidentifylong\-termprecursorsforendogenousfinancialcrisesinthemarket
correlation structures,” 2022\)
Hollstein et al. (“How Robust are Empirical Factor Models to the Choice of Breakpoints?” 2022\)
Horvath et al. (“Clustering Market Regimes Using the Wasserstein Distance,” 2021\)
Huang et al. (“Forecasting Stock Returns in Good and Bad Times: The Role of Market States,” 2017\)
Jacquier et al. (“Market regime classification with signatures,” 2021\)
Kaihatsu and Nakajima ( Has Trend Inflation Shifted? An Empirical Analysis with a Regime\-Switching Model ,
2015\)
Kashif and Leirvik (“Regime Switching Stock Returns and Hybrid Tail Risk,” 2021\)
Kaya (“Managing ambiguity in asset allocation,” 2017\)
Kim et al. (“Global Asset Allocation Strategy Using a Hidden Markov Model,” 2019\)
Koki et al. (“Exploring the predictability of cryptocurrencies via Bayesian hidden Markov models,” 2022\)
Komatsu and Makimoto (“Dynamic Investment Strategy with Factor Models Under Regime Switches,” 2015\)
Li and Zakamulin (“Stock volatility predictability in bull and bear markets,” 2020\)
Li and Mulvey (“Portfolio Optimization Under Regime Switching and Transaction Costs: Combining Neural
Networks and Dynamic Programs,” 2021\)
Massacci (“Testing for Regime Changes in Portfolios with a Large Number of Assets: A Robust Approach to
Factor Heteroskedasticity,” 2021\)
Martirosyan and Simonian (“Emerging Market Stock Momentum Returns during US Economic Regimes,” 2021\)
McGee (“Can Market Regimes Really be Timed with Historical Volatility?” 2021\)
McIndoe (“A Data Driven Approach to Market Regime Classification,” 2020\)
8McQuarrie (“New Lessons from Market History: Sometimes Bonds Win,” 2021\)
Muller and Preissler (“In Good and in Bad Times? The Relation between Anomaly Returns and Market States,”
2021\)
Mulvey et al. (“Machine learning, economic regimes and portfolio optimisation,” 2018\)
Nystrup et al. (“Regime\-Based Versus Static Asset Allocation: Letting the Data Speak,” 2015\)
Nystrup et al. (“Dynamic portfolio optimization across hidden market regimes,” 2018\)
Nystrup (“Regime\-Based Asset Allocation: Do Profitable Strategies Exist?” 2014\)
Nystrup et al. (“Dynamic Allocation or Diversification: A Regime\-Based Approach to Multiple Assets,” 2018\)
O’Cinneid (“Applications of machine learning in finance: analysis of international portfolio flows using regime\-
switching models,” 2019\)
Omerovic et al. (“Modelling Multiple Regimes in Economic Growth by Mixtures of Generalised Nonlinear
Models,” 2021\)
Omerovic et al. (“Modelling Multiple Regimes in Economic Growth by Mixtures of Generalised Nonlinear
Models,” 2021\)
Papenbrock and Schwendner (“Handling risk\-on/risk\-off dynamics with correlation regimes and correlation net\-
works,” 2015\)
Platanakis et al. (“Portfolios in a Regime Shifting Non\-Normal World: Are Alternative Assets Beneficial?” 2017\)
Peters (“Stable vs. Unstable Markets: A Tale of Two States,” 2015\)
Pharasi et al. (“Market states: A new understanding,” 2020\)
Pharasi et al. (“Dynamics of market states and risk assessment,” 2020\)
Procacci and Aste (“Forecasting market states,” 2019\)
Rebonato and El Aouadi (“How Do the Volatilities of Rates Depend on Their Level? The ”Universal Relation\-
ship” Revisited,” 2021\)
Reher and Wilfling (“A nesting framework for Markov\-switching GARCH modelling with an application to the
German stock market,” 2015\)
Sarwar et al. (“A tale of two states: asymmetries in the UK small, value and momentum premiums,” 2017\)
Satchell (“Regime\-switching in financial markets,” 2011\)
Seidl (“Markowitz versus Regime Switching: An Empirical Approach,” 2012\)
Sheikh and Sun (“Regime Change: Implications of Macroeconomic Shifts on Asset Class and Portfolio Perfor\-
mance,” 2012\)
Singh and Singh (“Risk\-Return Relationship in BRIC Equity Markets: Evidence from Markov Regime Switching
Model with Time\-varying Transition Probabilities,” 2016\)
Silveira and Oscar (“Inflation Targeting Regimes in Emerging Market Economies: To Invest or Not to Invest?”
2021\)
Simonian and Wu (“Minsky vs. Machine: New Foundations for Quant\-Macro Investing,” 2019\)
Stillwagon and Sullivan (“Markov switching in exchange rate models: will more regimes help?” 2020\)
Sueppel ( Classifying market regimes , 2021\)
Tajeuna et al. (“Modeling Regime Shifts in Multiple Time Series,” 2022\)
Tu (“Is Regime Switching in Stock Returns Important in Portfolio Decisions?” 2010\)
Uysal (“Risk Budgeting Portfolios Under a Modern Optimization and Machine Learning Lens,” 2021\)
Uysal and Mulvey (“A Machine Learning Approach in Regime\-Switching Risk Parity Portfolios,” 2021\)
Wang et al. (“Volatility forecasting revisited using Markov\-switching with time\-varying probability transition,”
2022\)
Wang and Hsieh (“Unraveling S\&P500 stock volatility and networks – An encoding\-and\-decoding approach,”
2021\)
Wu (“On the Predictive Performance of the Stock Returns by Using the Markov\-Switching Models,” 2020\)
Zakamulin (“Not All Bull and Bear Markets Are Alike: Insights From a Five\-State Hidden Semi\-Markov Model,”
2020\)
Zaremba et al. (“A Tale of Two States: An Application of a Markov Switching Model to Anomaly Returns,”
2020\)
2\.2\.4 Market states, regimes, changepoints and structural breaks of time series
List of references:
9Amini and Bayat (“hhsmm: An R package for hidden hybrid Markov/semi\-Markov models,” 2022\)
Blazquez\-Garcia et al. (“A review on outlier/anomaly detection in time series data,” 2022\)
Botte and Bao ( A Machine Learning Approach to Regime Modeling , 2021\)
Braei and Wagner (“Anomaly Detection in Univariate Time\-series: A Survey on the State\-of\-the\-Art,” 2020\)
Chalapathy and Chawla (“Deep Learning for Anomaly Detection: A Survey,” 2019\)
Chalapathy et al. (“Robust Deep Learning Methods for Anomaly Detection,” 2020\)
ChapmanandKillick(“Anassessmentofpractitionersapproachestoforecastinginthepresenceofchangepoints,”
2020\)
Das et al. (“Active Anomaly Detection via Ensembles: Insights, Algorithms, and Interpretability,” 2019\)
Dette et al. (“Change Point Analysis of Correlation in Non\-stationary Time Series,” 2019\)
Dette et al. (“Multiscale change point detection for dependent data,” 2021\)
Foorthuis (“On the Nature and Types of Anomalies: A Review,” 2021\)
Geiger et al. (“TadGAN: Time Series Anomaly Detection Using Generative Adversarial Networks,” 2020\)
Gerstenberger (“Robust discrimination between long\-range dependence and a change in mean,” 2021\)
Goswami et al. (“Abrupt transitions in time series with uncertainties,” 2018\)
Guérin et al. (“Markov\-Switching Three\-Pass Regression Filter,” 2020\)
Hallac et al. (“Greedy Gaussian segmentation of multivariate time series,” 2019\)
Jacob et al. (“Exathlon: A Benchmark for Explainable Anomaly Detection over Time Series,” 2021\)
Jacquier et al. (“Market regime classification with signatures,” 2021\)
Jewell et al. (“Testing for a Change in Mean After Changepoint Detection,” 2021\)
Jiang et al. (“Determining the number of change\-point via high\-dimensional cross\-validation,” 2020\)
Koki et al. (“Exploring the predictability of cryptocurrencies via Bayesian hidden Markov models,” 2022\)
Lee et al. (“ReRe: A Lightweight Real\-time Ready\-to\-Go Anomaly Detection Approach for Time Series,” 2020\)
Lee et al. (“Factor\-driven two\-regime regression,” 2021\)
Massacci and Kapetanios (“Forecasting in Factor Augmented Regressions under Structural Change,” 2021\)
Meitz and Saikkonen (“Testing for observation\-dependent regime switching in mixture autoregressive models,”
2021\)
Messer (“Bivariate change point detection: joint detection of changes in expectation and variance,” 2021\)
Navarro et al. (“Network Clustering for Latent State and Changepoint Detection,” 2021\)
Neto et al. (“Uncovering regimes in out of sample forecast errors,” 2021\)
Odendahl et al. (“Comparing Forecast Performance with State Dependence,” 2020\)
Pang et al. (“Unlocking the Full Potential of Small Data with Diverse Supervision,” 2021\)
Perikos et al. (“Sentiment analysis using novel and interpretable architectures of Hidden Markov Models,” 2021\)
Pinto and Castle ( A machine learning dynamic switching approach to forecasting when there are structural
breaks, 2021\)
Prakash et al. (“Structural clustering of volatility regimes for dynamic trading strategies,” 2021\)
Ruff et al. (“A Unifying Review of Deep and Shallow Anomaly Detection,” 2021\)
Shi (“A Survey of Changepoint Techniques for Time Series Data,” 2020\)
Shi et al. (“A Comparison of Single and Multiple Changepoint Techniques for Time Series Data,” 2021\)
Siliverstovs and Wochner (“State\-Dependent Evaluation of Predictive Ability,” 2021\)
Smith and Timmermann (“Break Risk,” 2021\)
Tajeuna et al. (“Modeling Regime Shifts in Multiple Time Series,” 2022\)
Tran et al. (“Model Selection for Bayesian Autoencoders,” 2021\)
van den Burg and Williams (“An Evaluation of Change Point Detection Algorithms,” 2022\)
Wang et al. (“Deep Learning for Anomaly Detection,” 2020\)
Wolchover (“Machine Learning’s ’Amazing’ Ability to Predict Chaos,” 2018\)
Wu and Keogh (“Current Time Series Anomaly Detection Benchmarks are Flawed and are Creating the Illusion
of Progress,” 2021\)
Zheng et al. (“Regime switching model estimation: spectral clustering hidden Markov model,” 2021\)
2\.2\.5 Detection and usage of bubbles, crashes and business cycles within context of QWIM
List of references:
Allaj and Sanfelici (“An Early Warning System for Identifying Financial Instability,” 2022\)
10Astill et al. (“Real\-Time Monitoring for Explosive Financial Bubbles,” 2018\)
Bianchi (“The Great Depression and the Great Recession: A view from financial markets,” 2020\)
Benhamou et al. (“Explainable AI (XAI) Models Applied to Planning in Financial Markets,” 2021\)
Benhamouetal.(“DetectingandAdaptingtoCrisisPatternwithContextBasedDeepReinforcementLearning,”
2021\)
Benhamou et al. (“Planning in Financial Markets in Presence of Spikes: Using Machine Learning GBDT,” 2021\)
Bordalo et al. (“Diagnostic bubbles,” 2021\)
Bucci and Ciciretti (“Market Regime Detection via Realized Covariances: A Comparison between Unsupervised
Learning and Nonlinear Models,” 2021\)
Bybee et al. (“Narrative Asset Pricing: Interpretable Systematic Risk Factors from News Text,” 2022\)
Chabi\-Yo et al. (“Multivariate Crash Risk,” 2022\)
Chowdhury et al. (“Bubbles and Crashes in Cryptocurrencies: Interdependence, Contagion, or Asset Rotation?”
2021\)
Cram (“Late to Recessions: Stocks and the Business Cycle,” 2020\)
Douady and Kornprobst (“An Empirical Approach to Financial Crisis Indicators Based on Random Matrices,”
2018\)
Elkind et al. (“When Do Investors Freak Out? Machine Learning Predictions of Panic Selling,” 2022\)
Engle and Ruan (“Measuring the probability of a financial crisis,” 2019\)
Gerlach et al. (“Crash\-sensitive Kelly Strategy built on a modified Kreuser\-Sornette bubble model tested over
three decades of twenty equity indices,” 2020\)
Gobel and Araujo (“Indicators of economic crises: a data\-driven clustering approach,” 2020\)
Glocker and Wegmueller (“Business cycle dating and forecasting with real\-time Swiss GDP data,” 2020\)
HeckensandGuhr(“Anewattempttoidentifylong\-termprecursorsforendogenousfinancialcrisesinthemarket
correlation structures,” 2022\)
Horváth et al. (“How to identify the different phases of stock market bubbles statistically?” 2022\)
Kabran and Unlu (“A two\-step machine learning approach to predict S\&P 500 bubbles,” 2021\)
Kole and van Dijk (“How to Identify and Forecast Bull and Bear Markets?” 2016\)
Liu et al. (“Predicting financial crises with machine learning methods,” 2022\)
Malevergne et al. (“A model of financial bubbles and drawdowns with non\-local behavioral self\-referencing,”
2021\)
Mehta (“The Mechanism behind the Bursting of Financial Bubbles and Market Crashes,” 2020\)
Min et al. (“The 2021 Bitcoin Bubbles and Crashes – Detection and Classification,” 2021\)
Mizuno et al. (“Detecting Stock Market Bubbles Based on the Cross\-Sectional Dispersion of Stock Prices,” 2020\)
Ohana et al. (“Explainable AI Models of Stock Crashes: A Machine\-Learning Explanation of the Covid March
2020 Equity Meltdown,” 2021\)
Samal et al. (“Network geometry and market instability,” 2021\)
Schatz (“Financial Modeling of Bubbles and Crashes,” 2020\)
Smug et al. (“Predicting Financial Market Crashes Using Ghost Singularities,” 2017\)
Viebig (“Exuberance in Financial Markets: Evidence from Machine Learning Algorithms,” 2020\)
Wang and Zong (“Are Crises Predictable? A Review of the Early Warning Systems in Currency and Stock
Markets,” 2020\)
Wehrli and Sornette (“Classification of flash crashes using the Hawkes(p,q) framework,” 2022\)
Yan and Huang (“Financial cycle and business cycle: An empirical analysis based on the data from the U.S,”
2020\)
Yao and Li (“A study on the bursting point of Bitcoin based on the BSADF and LPPLS methods,” 2021\)
Zhang et al. (“LPPLS bubble indicators over two centuries of the S\&P 500 index,” 2016\)
Zhang et al. (“LPPLS bubble indicators over two centuries of the S\&P 500 index,” 2016\)
Zhao and Sornette (“Bubbles for Fama from Sornette,” 2022\)
2\.2\.6 Detection and usage of bubbles, crashes and business cycles
List of references:
Chalkis et al. (“Modeling of crisis periods in stock markets,” 2021\)
Francis et al. ( Business Cycles Across Space and Time , 2021\)
11Kreuser and Sornette (“Super\-Exponential RE bubble model with efficient crashes,” 2019\)
Shu et al. (“The 2021 Bitcoin Bubbles and Crashes – Detection and Classification,” 2021\)
Smith et al. (“Equity Premium Forecasts with an Unknown Number of Structural Breaks,” 2020\)
Sornette (“Dragon\-kings and Predictions: Diagnostics and Forecasts for the World Financial Crisis,” 2014\)
Sornette and Cauwels (“Financial bubbles: mechanisms and diagnostics,” 2014\)
Sornette et al. (“Real\-time prediction and post\-mortem analysis of the Shanghai 2015 stock market bubble and
crash,” 2015\)
Sornette et al. (“Resolving Persistent Uncertainty by Self\-Organized Consensus to Mitigate Market Bubbles,”
2016\)
Sornette et al. (“Can We Use Volatility to Diagnose Financial Bubbles? Lessons from 40 Historical Bubbles,”
2017\)
2\.2\.7 Forecasting under data regimes
List of references:
Bansal et al. (“The term structure of equity risk premia,” 2021\)
Bahrami et al. (“Are advanced emerging market stock returns predictable? A regime\-switching forecast combi\-
nation approach,” 2019\)
BaltasandKaryampas(“Forecastingtheequityrisk premium: Theimportanceof regime\-dependentevaluation,”
2018\)
Beccarini (“Testing for the omission of relevant variables and regime\-switching misspecification,” 2019\)
Bel and Paap (“Modeling the impact of forecast\-based regime switches on US inflation,” 2016\)
Bianchi and Guidolin (“Can Linear Predictability Models Time Bull and Bear Real Estate Markets? Out\-of\-
Sample Evidence from REIT Portfolios,” 2014\)
Boot (“Macroeconomic Forecasting under Regime Switching, Structural Breaks and High\-dimensional Data,”
2017\)
Can (“To Switch or Not to Switch: Return Prediction and financial cycles,” 2019\)
Chang et al. (“A new approach to model regime switching,” 2017\)
Chiappa (“Unified Treatment of Hidden Markov Switching Models,” 2011\)
Chollete et al. (“Modeling International Financial Returns with a Multivariate Regime\-switching Copula,” 2009\)
Dal Pra et al. (“Regime Shifts in Excess Stock Return Predictability: An Out\-of\-Sample Portfolio Analysis,”
2018\)
Elliott and Timmermann (“Optimal forecast combination under regime switching,” 2005\)
Guidolin et al. (“How good can heuristic\-based forecasts be? A comparative performance of econometric and
heuristic models for UK and US asset returns,” 2018\)
Haase and Neuenkirch (“Predictability of Bull and Bear Markets: A New Look at Forecasting Stock Market
Regimes (and Returns) in the U.S.,” 2021\)
Hammerschmid and Lohre (“Regime Shifts and Stock Return Predictability,” 2018\)
Harvey et al. (“Real\-Time Detection of Regimes of Predictability in the U.S. Equity Premium,” 2021\)
Kim and Kang (“Bayesian Inference of Multivariate Regression Models with Endogenous Markov Regime\-
Switching Parameters,” 2022\)
Lee et al. (“Factor\-Driven Two\-Regime Regression,” 2020\)
Neto et al. (“Uncovering regimes in out of sample forecast errors,” 2021\)
Pruser (“Forecasting US inflation using Markov dimension switching,” 2021\)
Ren (“Essays in Asset Pricing and Financial Econometrics,” 2016\)
Smith (“International Stock Return Predictability and Asset Pricing Models,” 2021\)
Smith et al. (“Equity Premium Forecasts with an Unknown Number of Structural Breaks,” 2020\)
Wang et al. (“Volatility forecasting revisited using Markov\-switching with time\-varying probability transition,”
2022\)
Werge (“Predicting Risk\-adjusted Returns using an Asset Independent Regime\-switching Model,” 2021\)
Wu (“On the Predictive Performance of the Stock Returns by Using the Markov\-Switching Models,” 2020\)
122\.2\.8 Numerical methods, models and their implementations to model and analyze data regimes
List of references:
Ansari et al. (“Deep Explicit Duration Switching Models for Time Series,” 2021\)
Bazzi et al. (“Time\-Varying Transition Probabilities for Markov Regime Switching Models,” 2017\)
Bergmeir et al. (“Time Series Modeling and Forecasting Using Memetic Algorithms for Regime\-Switching Mod\-
els,” 2012\)
Bianchi (“Methods for measuring expectations and uncertainty in Markov\-switching models,” 2016\)
Chen (“Studying Regime Change using Directional Change,” 2019\)
Chuffart (“An Implementation of Markov Regime Switching GARCH Models in Matlab,” 2017\)
Ding (“An Implementation of Markov Regime Switching Model with Time Varying Transition Probabilities in
Matlab,” 2012\)
Jochmann and Koop (“Regime\-switching cointegration,” 2015\)
Kamenshchikov (“Bifurcation patterns of market regime transition,” 2016\)
Kasahara and Shimotsu (“Testing the Order of Multivariate Normal Mixture Models,” 2019\)
Khalili et al. (“Regularization in Regime\-Switching Gaussian Autoregressive Models,” 2016\)
Moreno\-Pino et al. (“PyHHMM: A Python Library for Heterogeneous Hidden Markov Models,” 2022\)
Ou et al. (“Whats for dynr: A Package for Linear and Nonlinear Dynamic Modeling in R,” 2019\)
Zheng et al. (“Regime switching model estimation: spectral clustering hidden Markov model,” 2021\)
13References
Ahelegbey, D. F., Billio, M., and Casarin, R. (2020\). “Modeling Turning Points In Global Equity Market .” In:SSRN
e\-Print.
Turning points in financial markets are often characterized by changes in the direction and/or magnitude of
market movements with short\-to\-long term impacts on investors’ decisions. This paper develops a Bayesian
technique to turning point detection in financial equity markets. We derive the interconnectedness among stock
market returns from a piece\-wise network vector autoregressive model. The empirical application examines
turning points in global equity market over the past two decades. We also compare the COVID\-19 induced
interconnectedness with that of the global financial crisis in 2008 to identify similarities and the most central
market for spillover propagation.
Ahmad,W.,Bhanumurthy,N.R.,andSehgal,S.(2015\). “RegimedependentdynamicsandEuropeanstockmarkets:
Is asset allocation really possible? ” In:Empirica 42(1\), pp. 77–107\.
In this study, we examine the regime shifts and volatility in stock market returns of eighteen European stock
marketsandtheUSAandutilizetheseregimesinassetallocationandriskmanagementcontexts.UsingaMarkov
regime switching model, the study finds strong evidence of regime switching characterized by two regimes over
the sample period from February, 1996 to January, 2012\. Smoothed probabilities and time\-varying conditional
volatilities also highlight the meaningful turning points including the recent global financial crisis (2008\) and
Eurozone crisis (2009\). Analyzing the market synchronization and Sharpe ratios, the study finally concludes
that sample markets provide very limited scope of asset allocation and risk diversification.
Ahmad, W. and Sehgal, S. (2015\). “Regime shifts and volatility in BRIICKS stock markets: an asset allocation
perspective .” In:International Journal of Emerging Markets 10(3\), pp. 383–408\.
This paper examines the regime shifts and stock market volatility in the stock market returns of seven emerging
economies popularly called as BRIICKS which stands for Brazil, Russia, India, Indonesia, China, South Korea
and South Africa, over the period from February, 1996 to January, 2012 by applying Markov regime switching in
mean\-variance model. The employed model finds two regimes in each of these markets. The identified regimes are
further utilized in formulating the asset allocation strategies based on market synchronization and Sharpe ratio.
The results suggest that BRIICKS is not a homogeneous asset class and each market should be independently
evaluated in terms of its regime switching behavior, volatility persistence and level of synchronization with other
emerging markets. The study finally concludes that Russia, India and China as the best assets to invest within
this emerging market basket which can be pooled with a mature market portfolio to achieve further benefits of
risk diversification.
Akioyamen, P., Tang, Y. Z., and Hussien, H. (2021\). “A Hybrid Learning Approach to Detecting Regime Switches
in Financial Markets .” In:arXiv e\-Print .
Financial markets are of much interest to researchers due to their dynamic and stochastic nature. With their
relations to world populations, global economies and asset valuations, understanding, identifying and forecasting
trends and regimes are highly important. Attempts have been made to forecast market trends by employing
machine learning methodologies, while statistical techniques have been the primary methods used in developing
market regime switching models used for trading and hedging. In this paper we present a novel framework for
the detection of regime switches within the US financial markets. Principal component analysis is applied for
dimensionality reduction and the k\-means algorithm is used as a clustering technique. Using a combination of
cluster analysis and classification, we identify regimes in financial markets based on publicly available economic
data. We display the efficacy of the framework by constructing and assessing the performance of two trading
strategies based on detected regimes.
Alberico, S., Coche, J., Sahakyan, V., and Zulaica, O. (2018\). “Regime identification for sovereign bond portfolio
construction .” In:Advances in the practice of public investment management: portfolio modelling, performance
attribution and governance . Ed. by N. Bulusu, J. Coche, A. Reveiz, F. Rivadeneyra, V. Sahakyan, and G. Yanou.
Springer International Publishing, pp. 247–274\.
Traditional asset allocation algorithms do not typically incorporate regime\-specific information to construct op\-
timal portfolios. In this chapter, we introduce a state\-dependent investment strategy based on a set of indicators
that we believe are useful in identifying economic and financial regimes and apply it to a universe consisting of
four of the most important and liquid developed government bond markets: the United States, the United King\-
dom, Germany, and Japan. The results show that portfolios optimised across regimes have properties markedly
different from those optimised using conventional asset allocation approaches. The findings may indicate that
14the regime\-optimised allocations are exposed to an additional risk factor that, when priced, could give rise to
an expected excess return over standard mean\-variance portfolios.
Allaj,E.andSanfelici,S.(2022\). “AnEarlyWarningSystemforIdentifyingFinancialInstability .”In:SSRN e\-Print .
Financial crises prediction is an essential topic in finance. Designing an efficient Early Warning System (EWS)
can help prevent catastrophic losses resulting from financial crises. We propose different EWSs for predicting
potential market instability conditions, where market instability refers to large asset price declines. A logit
regression EWS is employed to predict future large price losses and Early Warning Indicators (EWIs) based
on the realized variance (RV) and price\-volatility feedback rate are considered. The latter EWI is supposed
to describe the ease of the market in absorbing small price perturbations. Our study reveals that, while RV is
important in predicting future price losses in a given time series, the EWI employing the price\-volatility feedback
rate can improve prediction further.
Amini, M. and Bayat, A. (2022\). “hhsmm: An R package for hidden hybrid Markov/semi\-Markov models .” In:arXiv
e\-Print.
This paper introduces the hhsmm, which involves functions for initializing, fitting and predication of hidden
hybrid Markov/semi\-Markov models. These models are exible models with both Markovian and semi\-Markovian
states,whichareappliedtosituationswherethemodelinvolvesabsorbingormacrostates. Theleft\-to\-rightmod\-
els and the models with series/parallel networks of states are two models with Markovian and semi\-Markovian
states. The hhsmm also includes the residual useful lifetime estimation in the predict function. The commercial
modular aero\-propulsion system simulation (C\-MAPSS) data\-set is also included in the package, which is used
for illustration of the application of the package features.
Ang, A. and Bekaert, G. (2004\). “How do Regimes Affect Asset Allocation .” In:Financial Analysts Journal 60(2\),
pp. 86–99\.
International equity returns are characterized by episodes of high volatility and unusually high correlations
coinciding with bear markets. We develop models of asset returns that match these patterns and use them in
asset allocation. First, the presence of regimes with different correlations and expected returns is difficult to
exploit within a framework focused on global equities. Nevertheless, for all\-equity portfolios, a regime\-switching
strategy dominates static strategies out\-of\-sample. Second, substantial value is added when an investor chooses
between cash, bonds and equity investments. When a persistent bear market hits, the investor switches primarily
to cash. There are large market timing benefits because the bear market regimes tend to coincide with periods
of relatively high interest rates.
Ang, A. and Timmermann, A. (2012\). “Regime Changes and Financial Markets .” In:Annual Review of Financial
Economics 4(1\), pp. 313–337\.
Regime\-switching models can match the tendency of financial markets to often change their behavior abruptly
and the phenomenon that the new behavior of financial variables often persists for several periods after such a
change. Although the regimes captured by regime\-switching models are identified by an econometric procedure,
they often correspond to different periods in regulation, policy, and other secular changes. In empirical estimates,
the means, volatilities, autocorrelations, and cross\-covariances of asset returns often differ across regimes in a
mannerthatallowsregime\-switchingmodelstocapturethestylizedbehaviorofmanyfinancialseriesincludingfat
tails, heteroskedasticity, skewness, and time\-varying correlations. In equilibrium models, regimes in fundamental
processes, such as consumption or dividend growth, strongly affect the dynamic properties of equilibrium asset
pricesandcaninducenonlinearrisk\-returntrade\-offs.Regimeswitchesalsoleadtopotentiallylargeconsequences
for investors’ optimal portfolio choice.
Angelini, G., Bacchiocchi, E., Caggiano, G., and Fanelli, L. (2019\). “Uncertainty across volatility regimes .” In:
Journal of Applied Econometrics 34(3\), pp. 437–455\.
We propose a nonrecursive identification scheme for uncertainty shocks that exploits breaks in the volatility of
macroeconomic variables and is novel in the literature on uncertainty. This approach allows us to simultaneously
address two major questions in the empirical literature: Is uncertainty a cause or effect of decline in economic ac\-
tivity? Does the relationship between uncertainty and economic activity change across macroeconomic regimes?
Results based on a small\-scale vector autoregression with US monthly data suggest that (i) uncertainty is an
exogenous source of decline of economic activity, and (ii) the effects of uncertainty shocks amplify in periods of
economic and financial turmoil.
Ansari, A. F., Benidis, K., Kurle, R., Turkmen, A. C., Soh, H., Smola, A. J., Wang, Y., and Januschowski, T.
(2021\).“Deep Explicit Duration Switching Models for Time Series .” In:arXiv e\-Print .
15Many complex time series can be effectively subdivided into distinct regimes that exhibit persistent dynamics.
Discovering the switching behavior and the statistical patterns in these regimes is important for understanding
the underlying dynamical system. We propose the Recurrent Explicit Duration Switching Dynamical System
(RED\-SDS), a flexible model that is capable of identifying both state\- and time\-dependent switching dynamics.
State\-dependent switching is enabled by a recurrent state\-to\-switch connection and an explicit duration count
variable is used to improve the time\-dependent switching behavior. We demonstrate how to perform efficient
inference using a hybrid algorithm that approximates the posterior of the continuous states via an inference
network and performs exact inference for the discrete switches and counts. The model is trained by maximizing
a Monte Carlo lower bound of the marginal log\-likelihood that can be computed efficiently as a byproduct of
the inference routine. Empirical results on multiple datasets demonstrate that RED\-SDS achieves considerable
improvement in time series segmentation and competitive forecasting performance against the state of the art.
Arago, V. and Salvador, E. (2013\). “Non\-linear Tradeoff between Risk and Return: A Regime\-switching Multi\-factor
Framework .” In:Modeling and Simulation in Engineering, Economics, and Management . Ed. by M. Fernandez\-
Izquierdo, M. Munoz\-Torres, and R. Leon. Vol. 145\. Lecture Notes in Business Information Processing. Springer
Berlin Heidelberg, pp. 64–74\.
This study develops a multi\-factor framework where not only the market risk is considered but also potential
changes in the investment opportunity set. Although previous studies find no clear evidence about a positive
and significant relation between return and risk, favourable evidence can be obtained if a non\-linear relation
is established. The positive and significant tradeoff between return and risk is essentially observed during low
volatility periods suggesting a procyclical risk aversion of investors. Different patterns for the risk premium
dynamics in low and high volatility periods are obtained, both in risk prices and risk (conditional second
moments) patterns.
Astill, S., Harvey, D. I., Leybourne, S. J., Sollis, R., and Taylor, A. M. R. (2018\). “Real\-Time Monitoring for
Explosive Financial Bubbles .” In:Journal of Time Series Analysis 39(6\), pp. 863–891\.
We propose new methods for the real\-time detection of explosive bubbles in financial time series. Most extant
methods are constructed for a fixed sample of data and, as such, are appropriate only when applied as one\-shot
tests. Sequential application of these tests, declaring the presence of a bubble as soon as one of these statistics
exceeds the one\-shot critical value, would yield a detection procedure with an unknown false\-positive rate likely
tobe farin excessof thenominal level.Ourapproachsequentiallyapplies theone\-shot testsof Astillet al. (2017\),
comparing sub\-sample statistics calculated in real time during the monitoring period with the corresponding
sub\-sample statistics obtained from a prior training period. We propose two procedures: one based on comparing
the real\-time monitoring period statistics with the maximum statistic over the training period, and another that
compares the number of consecutive exceedances of a threshold value in the monitoring and training periods, the
threshold value obtained from the training period. Both allow the practitioner to determine the false\-positive
rate for any given monitoring horizon, or to ensure that this rate does not exceed a specified level by setting
a maximum monitoring horizon. Monte Carlo simulations suggest that the finite\-sample false\-positive rates lie
close to their theoretical counterparts, even in the presence of time\-varying volatility and serial correlation in
the shocks. The procedures are shown to perform well in the presence of a bubble in the monitoring period,
offering the possibility of rapid detection of an emerging bubble in a real\-time setting. An empirical application
to monthly stock market index data is considered.
Bae, G. I., Kim, W. C., and Mulvey, J. M. (2014\). “Dynamic asset allocation for varied financial markets under
regime switching framework .” In:European Journal of Operational Research 234(2\), pp. 450–458\.
Asset allocation among diverse financial markets is essential for investors especially under situations such as the
financial crisis of 2008\. Portfolio optimization is the most developed method to examine the optimal decision
for asset allocation. We employ the hidden Markov model to identify regimes in varied financial markets; a
regime switching model gives multiple distributions and this information can convert the static mean\-variance
model into an optimization problem under uncertainty, which is the case for unobservable market regimes. We
construct a stochastic program to optimize portfolios under the regime switching framework and use scenario
generation to mathematically formulate the optimization problem. In addition, we build a simple example for a
pension fund and examine the behavior of the optimal solution over time by using a rolling\-horizon simulation.
We conclude that the regime information helps portfolios avoid risk during left\-tail events.
Bahrami, A., Shamsuddin, A., and Uylangco, K. (2019\). “Are advanced emerging market stock returns predictable?
A regime\-switching forecast combination approach .” In:Pacific\-Basin Finance Journal 55, pp. 142–160\.
16Advanced emerging markets (AEMs) transitioning into developed markets experience far\-reaching economic and
institutional changes. Developing predictive models of stock returns in AEMs involves challenges of parameter
instability and model uncertainty. This study uses Markov regime switching (MRS) models to address parameter
instability and a combination forecast approach to mitigate model uncertainty. We find that the MRS model
better captures the effects of predictor variables on returns compared to models with time\-invariant parameters
and produces statistically and economically significant return forecasts. Combining return forecasts from dif\-
ferent MRS models further improves return predictability in AEMs. Consequently, employing MRS models in
conjunction with the combination forecast approach goes a long way to improving forecast accuracy in AEMs.
Baitinger, E. and Flegel, S. (2021\). “The better turbulence index? Forecasting adverse financial markets regimes
with persistent homology .” In:Financial Markets and Portfolio Management .
Persistent homology is the workhorse of modern topological data analysis, which in recent years becomes in\-
creasingly powerful due to methodological and computing power advances. In this paper, after equipping the
reader with the relevant background on persistent homology, we show how this tool can be harnessed for in\-
vestment purposes. Specifically, we propose a persistent homology\-based turbulence index for the detection of
adverse market regimes. With the help of an out\-of\-sample study, we demonstrate that investment strategies
relying on a persistent homology\-based turbulence detection outperform investment strategies based on other
popular turbulence indices. Additionally, we conduct a stability analysis of our findings. This analysis confirms
the results from the previous out\-of\-sample study, as the outperformance prevails for most configurations of the
respective investment strategy and thereby mitigating possible data mining concerns.
Balcerak, M. and Schmelzer, T. (2020\). “Constructing trading strategy ensembles by classifying market states .” In:
arXiv e\-Print .
Rather than directly predicting future prices or returns, we follow a more recent trend in asset management
and classify the state of a market based on labels. We use numerous standard labels and even construct our
own ones. The labels rely on future data to be calculated, and can be used a target for training a market state
classifier using an appropriate set of market features, e.g. moving averages. The construction of those features
relies on their label separation power. Only a set of reasonable distinct features can approximate the labels. For
each label we use a specific neural network to classify the state using the market features from our feature space.
Each classifier gives a probability to buy or to sell and combining all their recommendations (here only done
in a linear way) results in what we call a trading strategy. There are many such strategies and some of them
are somewhat dubious and misleading. We construct our own metric based on past returns but penalising for
a low number of transactions or small capital involvement. Only top score\-performance\-wise trading strategies
end up in final ensembles. Using the Bitcoin market we show that the strategy ensembles outperform both in
returns and risk\-adjusted returns in the out\-of\-sample period. Even more so we demonstrate that there is a clear
correlation between the success achieved in the past (if measured in our custom metric) and the future.
Baltas, N. and Karyampas, D. (2018\). “Forecasting the equity risk premium: The importance of regime\-dependent
evaluation .” In:Journal of Financial Markets 38(March), pp. 83–102\.
Asset allocation is critically dependent on the ability to forecast the equity risk premium (ERP) out\-of\-sample.
But, is superior econometric predictability across the business cycle synonymous with predictability at all times?
We evaluate recently introduced ERP forecasting models, which have been shown to generate econometrically
superior ERP forecasts, and find that their forecasting ability is regime\-dependent. They give rise to significant
relative losses during market downturns, when it matters the most for asset allocators to retain assets and their
client base intact. Conversely, any economic benefit occurring during market upswings is diminished for high
risk\-averse and leverage\-constrained investors.
Baltas,N.andKaryampas,D.(2020\). “ForecastingtheEquityRiskPremium:TheImportanceofRegime\-Dependent
Evaluation .” In:SSRN e\-Print .
Asset allocation is critically dependent on the ability to forecast the equity risk premium (ERP) out\-of\-sample.
But, is superior econometric predictability across the business cycle synonymous to predictability at all times?
We evaluate recently introduced ERP forecasting models, which have been shown to generate econometrically
superior ERP forecasts, and find that their forecasting ability is regime\-dependent. They give rise to significant
relative losses during market downturns, when it matters the most for asset allocators to retain assets and their
client base intact. Conversely, any economic benefit occurring during market upswings is diminished for high
risk averse and leverage constrained investors.
Bansal, R., Miller, S., Song, D., and Yaron, A. (2021\). “The term structure of equity risk premia .” In:Journal of
Financial Economics .
17We estimate a regime\-switching model for the equity term structure with Bayesian methods. Our approach
accounts for the data sample being unrepresentative of the population distribution of regimes. We find that
the term structure of expected equity dividend strip returns is downward sloping in recessions and upward
sloping in expansions, and the unconditional term structure of expected equity returns is positively sloped. Our
estimation shows that the sample unrepresentativeness induces a downward bias in the estimate of the equity
term structure slope. We present a regime\-switching consumption\-based asset\-pricing model that matches the
empirical findings.
Barkai, I., Shushi, T., and Yosef, R. (2021\). “A Cryptocurrency Risk\-Return Analysis for Bull and Bear Regimes .”
In:The Journal of Alternative Investments 24(1\), pp. 95–118\.
In this article, the authors develop a new analytical lens through which to examine the risk\-return profiles of
bitcoin, litecoin, ripple, and ethereum. Their focus is to understand better the price behavior of individual cryp\-
tocurrencies and their influence on one another. To achieve this, they segment each cryptocurrency’s time series
of returns into disparate bull and bear regimes. They then examine the nature and extent of overlap between
theseregimesandwhethertheychangeovertime.Theyalsocollectandplotseveralindicativedistributed\-denial\-
of\-service attacks against the time series to investigate their possible impact on regime change episodes. Their
findings shed light on previously unexplored systemic risk indicators within the cryptomarket as a whole and
on the relationship between specific cryptocurrency pairs. These findings enhance the risk management toolkit
for investors by revealing potential price behavior contagion patterns between cryptocurrencies pertinent to
blended portfolio management. Furthermore, the authors’ approach serves as a blueprint for additional research
into regime\-type overlap within the cryptomarket.
Bazzi, M., Blasques, F., Koopman, S. J., and Lucas, A. (2017\). “Time\-Varying Transition Probabilities for Markov
Regime Switching Models .” In:Journal of Time Series Analysis 38(3\), pp. 458–478\.
We propose a new Markov switching model with time\-varying transitions probabilities. The novelty of our model
is that the transition probabilities evolve over time by means of an observation driven model. The innovation
of the time\-varying probability is generated by the score of the predictive likelihood function. We show how
the model dynamics can be readily interpreted. We investigate the performance of the model in a Monte Carlo
study and show that the model is successful in estimating a range of different dynamic patterns for unobserved
regime switching probabilities. We also illustrate the new methodology in an empirical setting by studying the
dynamic mean and variance behaviour of US industrial production growth.
Beccarini, A. (2019\). “Testing for the omission of relevant variables and regime\-switching misspecification .” In:
Empirical economics 56(3\), pp. 775–796\.
This article shows that the interpretation of statistical evidence of regime\-switching is not unambiguous. The
usual interpretation is that some parameters switch according to the values of a predefined latent variable. An
alternativeinterpretationisthatregime\-switching,asastatisticalevidence,isalsopossiblewhenthelinearmodel
is underspecified and the omitted variable bias emerges. A formal test is proposed to verify a potentially spurious
regression with regime\-switching. Through this test, it is evident that regime\-switching estimates presented in
an academic paper, should be interpreted as a consequence of the misspecification considered here.
Bel, K. and Paap, R. (2016\). “Modeling the impact of forecast\-based regime switches on US inflation .” In:Interna\-
tional Journal of Forecasting 32(4\), pp. 1306–1316\.
Forecasts of key macroeconomic variables may lead to policy changes by governments, central banks and other
economic agents. Such policy changes in turn lead to structural changes in macroeconomic time series. We
describe this phenomenon in US inflation by introducing a logistic smooth transition autoregressive model where
the regime switches depend on the Michigan Inflation Expectation Series. Our results show that (i) forecasts
lead to regime changes and have an impact on the level of inflation; (ii) the absorption time of shocks in the
forecast of inflation is about four quarters; and (iii) a positive (negative) shock in the forecast results in actions
which increase (decrease) the inflation rate.
Benhamou, E., Ohana, J.\-J., Saltiel, D., and Guez, B. (2021a). “Explainable AI (XAI) Models Applied to Planning
in Financial Markets .” In:SSRN e\-Print .
Regime changes planning in financial markets is well known to be hard to explain and interpret. Can an asset
manager ex\-plain clearly the intuition of his regime changes prediction on equity market ? To answer this
question, we consider a gradi\-ent boosting decision trees (GBDT) approach to plan regime changes on S\&P
500 from a set of 150 technical, fundamental and macroeconomic features. We report an improved accuracy of
GBDT over other machine learning (ML) methods on the S\&P 500 futures prices. We show that retaining fewer
and carefully selected features provides improvements across all ML approaches. Shapley values have recently
18been intro\-duced from game theory to the field of ML. This approach allows a robust identification of the most
important variables planning stock market crises, and of a local explanation of the crisis probability at each
date, through a consistent features attribution. We apply this methodology to analyse in detail the March 2020
financial meltdown, for which the model of\-fered a timely out of sample prediction. This analysis unveils in
particular the contrarian predictive role of the tech equity sector before and after the crash.
Benhamou, E., Ohana, J.\-J., Saltiel, D., and Guez, B. (2021b). “Planning in Financial Markets in Presence of
Spikes: Using Machine Learning GBDT .” In:SSRN e\-Print .
lanning in financial markets is a difficult task as the method needs to dramatically change its behavior when
facing very rare black swan events like crises that shift market regime. In order to address this challenge, we
present a gradient boosting decision trees (GBDT) approach to predict large price drops in equity indexes from
a set of 150 technical, fundamental and macroeconomic features. We report an improved accuracy of GBDT over
other machine learning (ML) methods on the S\&P 500 futures prices. We show that retaining fewer and carefully
selected features provides improvements across all ML approaches. We show that this model has a strong predic\-
tive power. We train the model from 2000 to 2014, a period where various crises have been observed and use a
validation period of 3 years to find hyperparameters. The fitted model timely forecasts the Covid crisis giving
us a planning method for early detection of potential future crises.
Benhamou, E., Saltiel, D., Ohana, J.\-J., and Atif, J. (2021c). “Detecting and Adapting to Crisis Pattern with
Context Based Deep Reinforcement Learning .” In:SSRN e\-Print .
Deep reinforcement learning (DRL) has reached super human levels in complex tasks like game solving (Go,
StarCraft II, Atari Games), and autonomous driving. However, it remains an open question whether DRL can
reach human level in applications to financial problems and in particular in detecting pattern crisis and conse\-
quently dis\-investing. In this paper, we present an innovative DRL framework consisting in two subnetworks fed
respectively with portfolio strategies past performances and standard deviations as well as additional contextual
features. The second sub network plays an important role as it captures dependencies with common financial
indicators features like risk aversion, economic surprise index and correlations between assets that allows tak\-
ing into account context based information. We compare different network architectures either using layers of
convolutions to reduce network’s complexity or LSTM block to capture time dependency and whether previous
allocations is important in the modeling. We also use adversarial training to make the final model more robust.
Results on test set show this approach substantially over\-performs traditional portfolio optimization methods
like Markovitz and is able to detect and anticipate crisis like the current COVID one.
Berger, T. and Gencay, R. (2020\). “Short\-run wavelet\-based covariance regimes for applied portfolio management .”
In:Journal of Forecasting 39(4\), pp. 642–660\.
Decisions on asset allocations are often determined by covariance estimates from historical market data. In this
paper, we introduce a wavelet\-based portfolio algorithm, distinguishing between newly embedded news and long\-
run information that has already been fully absorbed by the market. Exploiting the wavelet decomposition into
short\- and long\-run covariance regimes, we introduce an approach to focus on particular covariance components.
Using generated data, we demonstrate that short\-run covariance regimes comprise the relevant information
for periodical portfolio management. In an empirical application to US stocks and other international markets
for weekly, monthly, quarterly, and yearly holding periods (and rebalancing), we present evidence that the
application of wavelet\-based covariance estimates from short\-run information outperforms portfolio allocations
that are based on covariance estimates from historical data.
Bergmeir, C., Triguero, I., Molina, D., Aznarte, J. L., and Benitez, J. M. (2012\). “Time Series Modeling and Fore\-
casting Using Memetic Algorithms for Regime\-Switching Models .” In:IEEE Transactions on Neural Networks
and Learning Systems 23(11\), pp. 1841–1847\.
In this brief, we present a novel model fitting procedure for the neuro\-coefficient smooth transition autoregressive
model (NCSTAR), as presented by Medeiros and Veiga. The model is endowed with a statistically founded
iterative building procedure and can be interpreted in terms of fuzzy rule\-based systems. The interpretability
of the generated models and a mathematically sound building procedure are two very important properties of
forecasting models. The model fitting procedure employed by the original NCSTAR is a combination of initial
parameter estimation by a grid search procedure with a traditional local search algorithm. We propose a different
fitting procedure, using a memetic algorithm, in order to obtain more accurate models. An empirical evaluation
of the method is performed, applying it to various real\-world time series originating from three forecasting
competitions. The results indicate that we can significantly enhance the accuracy of the models, making them
competitive to models commonly used in the field.
19Bernhart, G., Hocht, S., Neugebauer, M., Neumann, M., and Zagst., R. (2011\). “Asset Correlations in Turbulent
Markets and the Impact of Different Regimes on Asset Management .” In:Asia\-Pacific Journal of Operational
Research 28(01\), pp. 1–23\.
In this article, the dependence structure of the asset classes stocks, government bonds, and corporate bonds in
different market environments and its implications on asset management are investigated for the US, European,
and Asian market. Asset returns are modelled by a Markov\-switching model which allows for two market
regimes with completely different risk\-return structures. Using major stock indices from all three regions, calm
and turbulent market periods are identified for the time period between 1987 and 2009 and the correlation
structures in the respective periods are compared. It turns out that the correlations between as well as within
the asset classes under investigation are far from being stable and vary significantly between calm and turbulent
market periods as well as in time. It also turns out that the US and European markets are much more integrated
than the Asian and US/European ones. Moreover, the Asian market features more and longer turbulence phases.
Finally, the impact of these findings is examined in a portfolio optimization context. To accomplish this, a case
study using the mean\-variance and the mean\-conditional\-value\-at\-risk framework as well as two levels of risk
aversion is conducted. The results show that an explicit consideration of different market conditions in the
modelling framework yields better portfolio performance as well as lower portfolio risk compared to standard
approaches. These findings hold true for all investigated optimization frameworks and risk\-aversion levels.
Bhansali, V. and Holdom, J. (2021\). “Good States, Bad States: What Do Options Tell Us About Schizophrenic
Behavior of Mr. Market and What Can We Do About It? ” In:Journal of Investment Strategies 19(4\), pp. 79–91\.
Option prices theoretically encapsulate participants’ expectations about good state (bullish) and bad state
(bearish) market outcomes. By using a mixture of distributions and reasonable assumptions, the authors extract
time series of expected returns, volatilities and mixture probabilities of these outcomes surrounding the current
US elections. The bimodality of asset return distributions suggests important modifications for asset allocation
and risk management.
Bianchi, D. and Guidolin, M. (2014\). “Can Linear Predictability Models Time Bull and Bear Real Estate Markets?
Out\-of\-Sample Evidence from REIT Portfolios .” In:The Journal of Real Estate Finance and Economics 49(1\),
pp. 116–164\.
A recent literature has shown that REIT returns contain strong evidence of bull and bear dynamic regimes
that may be best captured using nonlinear econometric models of the Markov switching type. In fact, REIT
returns would display regime shifts that are more abrupt and persistent than in the case of other asset classes.
In this paper we ask whether and how simple linear predictability models of the vector autoregressive (VAR)
type may be extended to capture the bull and bear patterns typical of many asset classes, including REITs. We
find that nonlinearities are so deep that it is impossibile for a large family of VAR models to either produce
similar portfolio weights or to yield realized, ex\-post out\-of\-sample long\-horizon portfolio performances that may
compete with those typical of bull and bear models. A typical investor with intermediate risk aversion and a
5\-year horizon ought to be ready to pay an annual fee of up to 5\.7 percent to have access to forecasts of REIT
returns that take their bull and bear dynamics into account instead of simpler, linear forecast.
Bianchi, F. (2016\). “Methods for measuring expectations and uncertainty in Markov\-switching models .” In:Journal
of Econometrics 190(1\), pp. 79–99\.
I develop methods to analyze multivariate Markov\-switching models. Formulas for the evolution of first and sec\-
ond moments are derived and then used to characterize expectations, uncertainty, impulse responses, sources of
uncertainty, and welfare implications of regime changes in general equilibrium models. The methods can be used
to capture the link between uncertainty and the state of the economy. Campbell’s present value decomposition
is generalized to allow for parameter instability. Taking into account regime changes is shown to be important
for expectations, welfare, and uncertainty. All results are derived analytically and are therefore suitable for
structural estimation.
Bianchi, F. (2020\). “The Great Depression and the Great Recession: A view from financial markets .” In:Journal of
Monetary Economics 114, pp. 240–261\.
Similarities between the Great Depression and the Great Recession are documented with respect to the behavior
of financial markets. A Great Depression regime is identified by using a Markov\-switching VAR. The probability
of this regime has remained close to zero for many decades, but spiked for a short period during the most recent
financial crisis, the Great Recession. The Great Depression regime implies a collapse of the stock market, with
small\-growth stocks outperforming small\-value stocks. A model with financial frictions and uncertainty about
policy makers’ intervention suggests that policy intervention during the Great Recession might have avoided a
20second Great Depression. A multi\-country analysis shows that the Great Depression and Great Recession were
not like any other financial crises.
Billio, M., Ferrara, L., Guegan, D., and Mazzi, G. L. (2013\). “Evaluation of Regime Switching Models for Real\-Time
Business Cycle Analysis of the Euro Area .” In:Journal of Forecasting 32(7\), pp. 577–586\.
In this paper, we aim at assessing Markov switching and threshold models in their ability to identify turning
points of economic cycles. By using vintage data updated on a monthly basis, we compare their ability to date
ex post the occurrence of turning points, evaluate the stability over time of the signal emitted by the models
and assess their ability to detect in real\-time recession signals. We show that the competitive use of these
models provides a more robust analysis and detection of turning points. To perform the complete analysis, we
have built a historical vintage database for the euro area going back to 1970 for two monthly macroeconomic
variables of major importance for short\-term economic outlook, namely the industrial production index and the
unemployment rate.
Bilokon, P., Jacquier, A., and McIndoe, C. (2021\). “Market regime classification with signatures .” In:arXiv e\-Print .
We provide a data\-driven algorithm to classify market regimes for time series. We utilise the path signature,
encoding time series into easy\-to\-describe objects, and provide a metric structure which establishes a connection
between separation of regimes and clustering of points.
Blazquez\-Garcia, A., Conde, A., Mori, U., and Lozano, J. A. (2022\). “A review on outlier/anomaly detection in
time series data .” In:ACM Computing Surveys 54(3\), pp. 1–33\.
Recent advances in technology have brought major breakthroughs in data collection, enabling a large amount of
data to be gathered over time and thus generating time series. Mining this data has become an important task
for researchers and practitioners in the past few years, including the detection of outliers or anomalies that may
represent errors or events of interest. This review aims to provide a structured and comprehensive state\-of\-the\-
art on outlier detection techniques in the context of time series. To this end, a taxonomy is presented based on
the main aspects that characterize an outlier detection technique.
Blin, O., Ielpo, F., Lee, J., and Teiletche, J. (2017\). “A Macro Risk\-Based Approach to Alternative Risk Premia
Allocation .” In:Factor Investing . Elsevier, pp. 285–316\.
Alternativeriskpremiaareencounteringgrowinginterestfrominvestors.Thevastmajorityofacademicliterature
has been focusing on describing the alternative risk premia (typically, momentum, carry and value strategies)
individually. In this chapter, we investigate the question of the allocation across a range of cross\-asset alternative
riskpremia.Forthis,wedesignanactivemacrorisk\-basedframeworkthatnotablyaimstoexploitalternativerisk
premia’s varying behavior in different macro regimes. We build long\-term strategic portfolios across economic
regimes, which we dynamically tilt based on point\-in\-time signals related to regimes nowcasting and current
carry. We perform back tests of the allocation strategy in an out\-of\-sample setting.
Blitz,D.andVanVliet,P.(2009\). “DynamicStrategicAssetAllocation:RiskandReturnAcrossEconomicRegimes .”
In:SSRN e\-Print .
We propose a practical investment framework for dynamic asset allocation across different economic regimes,
which we illustrate using a sample of U.S. data from 1948 to 2007\. We identify four regimes in the economic
cycle and find that these regimes capture pronounced time\-variation in the risk and return properties of asset
classes. Time\-variation is also observed in the risk of a traditional, static strategic asset allocation portfolio .
In order to stabilize risk across the economic cycle we propose a dynamic strategic asset allocation approach,
which has the potential to enhance expected return as well. The proposed approach is found to be robust to
variations in the variable composition of the regime model and can easily be extended with different economic
variables and/or additional assets.
BNYMellon Research (2013\). Great expectations: regime based asset allocation seeks higher return, lower drawdowns .
Tech. rep. BNY Mellon.
Our research finds that dynamically adjusting asset class exposures as growth and inflation expectations shift
has the potential to significantly improve risk\-adjusted returns and reduce drawdowns. We analyzed more than
40 years of economic and market performance to achieve a more granular understanding of the complex pattern
of macroeconomic regime transitions and the role growth and inflation expectations play in driving asset prices.
Based on this research, we used growth and inflation expectations data to create a model that could offer insight
into the probability of certain macroeconomic regimes. Changes in these expectations pointed to macroeconomic
regimes in which assets have distinct performance characteristics. These regimes have varying lengths and occur
at varying frequencies. Our model seeks to provide a roadmap to the probabilities of future regimes based on
the evolution of our factors, and we explore structuring portfolios to take advantage of probable transitions
21among them. We extend this framework to allow clients to see which regimes their own portfolios are currently
positioned for, and provide a structure for analyzing how portfolios are aligned with the convictions of their
managers.
Boot, T. (2017\). “Macroeconomic Forecasting under Regime Switching, Structural Breaks and High\-dimensional
Data.” PhD thesis. Tinbergen Instituut.
In the first two chapters of this thesis, we consider the bias\-variance trade\-off in models subject to regime
switches and structural breaks. The non\-linearities pose a challenge to find an optimal trade\-off as the variance
term is not easily tractable. The final two chapters discuss the trade\-off in (high\-dimensional) linear models, in
which we consider estimators for which explicit bounds on their performance can be provided.
Bordalo, P., Gennaioli, N., Kwon, S. Y., and Shleifer, A. (2021\). “Diagnostic bubbles .” In:Journal of Financial
Economics 141(3\), pp. 1060–1077\.
Weintroducediagnosticexpectationsintoastandardsettingofpriceformationinwhichinvestorslearnaboutthe
fundamental value of an asset and trade it. We study the interaction of diagnostic expectations with learning
from prices and speculation (buying for resale). With diagnostic (but not with rational) expectations, these
mechanisms lead to price paths exhibiting three phases: initial underreaction, then overshooting (the bubble),
and finally a crash. With learning from prices, the model generates price extrapolation as a by\-product of
beliefs about fundamentals, lasting only as the bubble builds up. When investors speculate, even mild diagnostic
distortions generate substantial bubbles.
Botte, A. and Bao, D. (2021\). A Machine Learning Approach to Regime Modeling . Tech. rep. Two Sigma.
The authors offer a data\-driven approach to modeling market regimes by applying a Gaussian Mixture Model
(a machine learning method) to the factors in the Two Sigma Factor Lens.
Bradrania, R. and Neghab, D. P. (2022\). “State\-dependent asset allocation using neural networks .” In:The European
Journal of Finance .
Changes in market conditions present challenges for investors as they cause performance to deviate from the
ranges predicted by long\-term averages of means and covariances. The aim of conditional asset allocation strate\-
gies is to overcome this issue by adjusting portfolio allocations to hedge changes in the investment opportunity
set. This paper proposes a new approach to conditional asset allocation that is based on machine learning;
it analyzes historical market states and asset returns and identifies the optimal portfolio choice in a new pe\-
riod when new observations become available. In this approach, we directly relate state variables to portfolio
weights, rather than firstly modeling the return distribution and subsequently estimating the portfolio choice.
The method captures nonlinearity among the state (predicting) variables and portfolio weights without assuming
any particular distribution of returns and other data, without fitting a model with a fixed number of predicting
variables to data and without estimating any parameters. The empirical results for a portfolio of stock and bond
indices show the proposed approach generates a more efficient outcome compared to traditional methods and is
robust in using different objective functions across different sample periods.
Braei, M. and Wagner, S. (2020\). “Anomaly Detection in Univariate Time\-series: A Survey on the State\-of\-the\-Art .”
In:arXiv e\-Print .
Anomaly detection for time\-series data has been an important research field for a long time. Seminal work on
anomaly detection methods has been focussing on statistical approaches. In recent years an increasing number of
machine learning algorithms have been developed to detect anomalies on time\-series. Subsequently, researchers
tried to improve these techniques using (deep) neural networks. In the light of the increasing number of anomaly
detection methods, the body of research lacks a broad comparative evaluation of statistical, machine learning
and deep learning methods. This paper studies 20 univariate anomaly detection methods from the all three
categories. The evaluation is conducted on publicly available datasets, which serve as benchmarks for time\-series
anomaly detection. By analyzing the accuracy of each method as well as the computation time of the algorithms,
we provide a thorough insight about the performance of these anomaly detection approaches, alongside some
general notion of which method is suited for a certain type of data.
Bucci, A. and Ciciretti, V. (2021\). “Market Regime Detection via Realized Covariances: A Comparison between
Unsupervised Learning and Nonlinear Models .” In:arXiv e\-Print .
There is broad empirical evidence of regime switching in financial markets. The transition between different
market regimes is mirrored in correlation matrices, whose time\-varying coefficients usually jump higher in highly
volatile regimes, leading to the failure of common diversification methods. In this article, we aim to identify
market regimes from covariance matrices and detect transitions towards highly volatile regimes, hence improving
tail\-risk hedging. Starting from the time series of fractionally differentiated sentiment\-like future values, two
22models are applied on monthly realized covariance matrices to detect market regimes. Specifically, the regime
detection is implemented via vector logistic smooth transition autoregressive model (VLSTAR) and through an
unsupervised learning methodology, the agglomerative hierarchical clustering. Since market regime switches are
unobservable processes that describe the latent change of market behaviour, the ability of correctly detecting
marketregimesisvalidatedintwoways:firstly,randomlygenerateddataareusedtoassessacorrectclassification
when regimes are known; secondly, a naïve trading strategy filtered with the detected regime switches is used to
understand whether an improvement is showed when accounting for regime switches. The results point to the
VLSTAR as the best performing model for labelling market regimes.
Bybee, L., Kelly, B. T., and Su, Y. (2022\). “Narrative Asset Pricing: Interpretable Systematic Risk Factors from
News Text .” In:SSRN e\-Print .
We seek fundamental risks from news text. Conceptually, news is closely related to the idea of systematic risk,
in particular the ”state variables” in the ICAPM. News captures investors’ concerns about future investment
opportunities, and hence drives the current pricing kernel. This paper demonstrates a way to extract a parsi\-
monious set of risk factors and eventually a univariate pricing kernel from news text. The state variables are
reduced and selected from the variations in attention allocated to different news narratives. As a result, the risk
factors attain clear text\-based interpretability as well as top\-of\-the\-line asset pricing performance. The empirical
method integrates topic modeling (LDA), latent factor analysis (IPCA), and variable selection (group lasso).
Campani, C. H., Garcia, R., and Lewin, M. (2021\). “Optimal portfolio strategies in the presence of regimes in asset
returns.” In:Journal of Banking \& Finance 123, p. 106030\.
This paper analyzes optimal portfolio and consumption strategies in a regime\-switching economy with unob\-
servable states and predictability of risky asset returns. We develop approximate analytical solutions to the
unconstrained dynamic problem. The approximation is shown to be fast and accurate in a four\-regime setting
with an allocation to four assets compared to the numerical solution developed in Guidolin and Timmermann
(2007\). The computation time of the approximate solution is shown to be practically independent of the number
of assets when no predictors are present and only marginally affected by the number of predictors. While the
portfolio policy strongly depends on the current state of the economy, the consumption\-to\-wealth ratio is roughly
state\-independent. Predictability considerably changes the optimal portfolios. Hedging demands are negligible
with regimes and no predictability, but are important with predictability. On the other hand, the consumption\-
to\-wealth ratio is not very impacted by the predictor. We provide an out\-of\-sample statistical assessment of the
returns provided by a multi\-regime strategy with respect to a single\-regime and to a strategy.
Can,H.(2019\). “ToSwitchorNottoSwitch:ReturnPredictionandfinancialcycles .”MAthesis.ErasmusUniversity.
This paper emphasizes the importance of identifying changes in financial cycles when predicting monthly US
excess stock returns for the period 1977 \- 2017\. Incorporating regime switching into the predictive models
improves the quality of the excess return forecasts in terms of market timing ability, economic value and stability.
The Markov Switching models consisting of predictor variables selected based on their performance during bull
and bear markets performs especially well. A mean\-variance investor would be willing to pay several hundreds
basis points to switch from the static benchmark portfolios to one of these portfolio strategies.
Chabi\-Yo, F., Huggenberger, M., and Weigert, F. (2022\). “Multivariate Crash Risk .” In:Journal of Financial
Economics .
This paper investigates whether multivariate crash risk (MCRASH), defined as exposure to extreme realizations
of multiple systematic factors, is priced in the cross\-section of expected stock returns. We derive an extended
linear model with a positive premium for MCRASH, and we empirically confirm that stocks with high MCRASH
earn significantly higher future returns than stocks with low MCRASH. The premium is not explained by
linear factor exposures, alternative downside risk measures, or stock characteristics. Extending market\-based
definitions of crash risk to other well\-established factors helps to determine the cross\-section of expected stock
returns without further expanding the factor zoo.
Chalapathy, R. and Chawla, S. (2019\). “Deep Learning for Anomaly Detection: A Survey .” In:arXiv e\-Print .
Anomaly detection is an important problem that has been well\-studied within diverse research areas and appli\-
cation domains. The aim of this survey is two\-fold, firstly we present a structured and comprehensive overview
of research methods in deep learning\-based anomaly detection. Furthermore, we review the adoption of these
methods for anomaly across various application domains and assess their effectiveness. We have grouped state\-of\-
the\-art research techniques into different categories based on the underlying assumptions and approach adopted.
Within each category we outline the basic anomaly detection technique, along with its variants and present key
assumptions, to differentiate between normal and anomalous behavior. For each category, we present we also
23present the advantages and limitations and discuss the computational complexity of the techniques in real appli\-
cation domains. Finally, we outline open issues in research and challenges faced while adopting these techniques.
Chalapathy, R., Khoa, N. L. D., and Chawla, S. (2020\). “Robust Deep Learning Methods for Anomaly Detection .”
In:Proceedings of the 26th ACM SIGKDD International Conference on Knowledge Discovery \& Data Mining .
ACM.
Anomaly detection is an important problem that has been well\-studied within diverse research areas and ap\-
plication domains. A robust anomaly detection system identifies rare events and patterns in the absence of
labelled data. The identified patterns provide crucial insights about both the fidelity of the data and deviations
in the underlying data\-generating process. For example a surveillance system designed to monitor the emergence
of new epidemics will use a robust anomaly detection methods to separate spurious associations from genuine
indicators of an epidemic with minimal lag time. The key concept in anomaly detection is the notion of ”ro\-
bustness”, i.e., designing models and representations which are less\-sensitive to small changes in the underlying
data distribution. The canonical example is that the median is more robust than the mean as an estimator.
The tutorial will primarily help researchers and developers design deep learning architectures and loss functions
where the learnt representation behave more like the ”median” rather than the ”mean.” The tutorial will revisit
well known unsupervised learning techniques in deep learning including autoencoders and generative adversarial
networks (GANs) from the perspective of anomaly detection. This in turn will give the audience a more grounded
perspective on unsupervised deep learning methods. All the methods will be introduced in a hands\-on manner
to demonstrate how high\-level ideas and concepts get translated to practical real code.
Chalkis,A.,Christoforou,E.,Dalamagkas,T.,andEmiris,I.Z.(2021\). “Modelingofcrisisperiodsinstockmarkets .”
In:arXiv e\-Print .
We exploit a recent computational framework to model and detect financial crises in stock markets, as well
as shock events in cryptocurrency markets, which are characterized by a sudden or severe drop in prices. Our
method manages to detect all past crises in the French industrial stock market starting with the crash of 1929,
including financial crises after 1990 (e.g. dot\-com bubble burst of 2000, stock market downturn of 2002\), and
all past crashes in the cryptocurrency market, namely in 2018, and also in 2020 due to covid\-19\. We leverage
copulae clustering, based on the distance between probability distributions, in order to validate the reliability
of the framework; we show that clusters contain copulae from similar market states such as normal states, or
crises. Moreover, we propose a novel regression model that can detect successfully all past events using less than
10% of the information that the previous framework requires. We train our model by historical data on the
industry assets, and we are able to detect all past shock events in the cryptocurrency market. Our tools provide
the essential components of our software framework that offers fast and reliable detection, or even prediction,
of shock events in stock and cryptocurrency markets of hundreds of assets.
Chang, Y., Choi, Y., and Park, J. Y. (2017\). “A new approach to model regime switching .” In:Journal of Economics
196(1\), pp. 127–143\.
This paper introduces a new approach to model regime switching using an autoregressive latent factor, which
determines regimes depending upon whether it takes a value above or below some threshold level. In our
approach,thelatentfactorisallowedtobecorrelatedwiththeinnovationtotheobservedtimeseries.Ifthelatent
factor becomes exogenous, our approach reduces to the conventional Markov switching. We develop a modified
Markov switching filter to estimate the mean and volatility models with Markov switching that are frequently
analyzed, and find that the presence of endogeneity in regime switching is indeed strong and ubiquitous.
Chapman, J.\-L. and Killick, R. (2020\). “An assessment of practitioners approaches to forecasting in the presence
of changepoints .” In:Quality and Reliability Engineering International 36(8\), pp. 2676–2687\.
A common challenge in time series is to forecast data that suffer from structural breaks or changepoints which
complicate modeling. If we naively forecast using one model for the whole data, the model will be incorrect,
and thus, our forecast error will be large. There are two common practices to account for these changepoints
when the goal is forecasting: (1\) preprocess the data to identify the changepoints, incorporating them as dummy
variables in modeling the whole data, and (2\) include the changepoint estimation into the model and forecast
using the model fit to the last segment. This article examines these two practices, using the computationally
exact Pruned Exact Linear Time (PELT) algorithm for changepoint detection, comparing and contrasting them
in the context of an important Software Engineering application.
Chen, J. M., Rehman, M. U., and Vo, X. V. (2021\). “Clustering commodity markets in space and time: Clarify\-
ing returns, volatility, and trading regimes through unsupervised machine learning .” In:Resources Policy 73,
p. 102162\.
24Unsupervised machine learning can interpret logarithmic returns and conditional volatility in commodity mar\-
kets.Thisarticleappliesmachinelearninginordertovisualizeandinterpretlogreturnsandconditionalvolatility
in commodities trading. We emphasize two classes of unsupervised learning methods: clustering and manifold
learning for the reduction of dimensionality. We source daily prices from September 18, 2000 through July 31,
2020, for precious metals, base metals), energy commodities and agricultural commodities. Our results highlight
that at the very least, returns\-based clusters conform more closely to traditional boundaries between precious
metals, base metals, fuels, temperate\-climate agricultural commodities, and tropical agricultural commodities.
On the other hand, volatility\-based clustering succeeds in identifying periods of extreme market distress, such
as the global financial crisis of 2008\-09 and the Covid\-19 pandemic.
Chen, J. (2019\). “Studying Regime Change using Directional Change .” PhD thesis. University of Essex.
Financial markets reflect what is the collective trading behaviour of traders. Such behaviour is often affected
by financial crisis or political events. The term regime change is used to describe such significant change of
collective behaviour. This thesis studies how regime change can be measured and detected in financial markets.
The traditional ways to detect regime changes are based on analysis of the statistical properties of time series.
For example, researchers may have used significant changes in means, volatilities, autocorrelations and cross\-
covariances of asset returns to conclude regime changes. In this thesis, we study regime change detection using
indicators developed in Directional Change (DC). DC is an alternative way to sample financial data. Unlike
time series, which samples transaction prices at regular time intervals, DC samples prices at peaks and troughs
of the market. We propose a new method to detect regime changes under the DC framework. DC data is fed
into a Hidden Markov Model (HMM), a machine learning model, which aims to discover the hidden state of
the market. To evaluate our method, we apply it to the Forex market over a time period of uncertainty, namely
the Brexit referendum period. The timing of regime changes detected by this method is consistent with the
political developments taking place at the time. While regime changes detected by DC and time series agree
with each other most of the time, some regime changes found under DC were not found under time series. That
means our DC approach complemented the time series approach by the provision of supporting and additional
information. With the method developed, we then went on to detect normal and abnormal market regimes
(which represent regimes before and after significant events took place) in other assets. Through observation of
regimes detected in ten different markets at different times using different thresholds, we discovered that normal
and abnormal regimes are clearly separable from each other in the DC indicator space. This allowed us to
generalise and characterise what are the features of normal and abnormal market regimes using DC indicators.
We then showed that the regime characteristics established above can be used for regime tracking. As a proof
of concept, we showed that, based on the market data observed so far, one can use a simple Bayes model to
compute the probability of the current market being in the normal or abnormal regime. Preliminary results
suggested that the proposed method managed to detect regime change signals accurately and promptly. Finally,
we examined the usefulness of the detected regime change signals. Two trading algorithms are proposed to
demonstrate the practical implication of the regime tracking information. To summarise: this thesis pioneers a
new method for regime change detection under the DC framework. It showed that normal and abnormal regimes
can becharacterised using DC indicators. Once such characteristics are clearly established, this could be used for
effective market tracking, which potentially lays the foundation for a practical financial early warning system.
The regime tracking signals can be used to established valuable trading algorithms.
Chen, J. and Tsang, E. P. K. (2020\). Detecting regime change in computational finance: data science, machine
learning and algorithmic trading . Boca Raton: CRC Press, Taylor \& Francis Group. 164 pp.
Based on interdisciplinary research into ”Directional Change”, a new data\-driven approach to financial data
analysis, Detecting Regime Change in Computational Finance: Data Science, Machine Learning and Algorithmic
Trading applies machine learning to financial market monitoring and algorithmic trading. Directional Change
is a new way of summarising price changes in the market. Instead of sampling prices at fixed intervals (such as
daily closing in time series), it samples prices when the market changes direction (”zigzags”). By sampling data
in a different way, this book lays out concepts which enable the extraction of information that other market
participants may not be able to see.
The book explores the following topics:
1\)Data science: as an alternative to time series, price movements in a market can be summarised as directional
changes
2\)Machine learning for regime change detection: historical regime changes in a market can be discovered by
a Hidden Markov Model
253\)Regime characterisation: normal and abnormal regimes in historical data can be characterised using indi\-
cators defined under Directional Change
4\)Market Monitoring: by using historical characteristics of normal and abnormal regimes, one can monitor
the market to detect whether the market regime has changed
5\)Algorithmic trading: regime tracking information can help us to design trading algorithms
.
Chen, P. and Yang, H. (2011\). “Markowitz’s Mean\-Variance Asset\-Liability Management with Regime Switching:
A Multi\-Period Model .” In:Applied Mathematical Finance 18(1\), pp. 29–50\.
This paper considers an optimal portfolio selection problem under Markowitz’s mean\-variance portfolio selection
problem in a multi\-period regime\-switching model. We assume that there are n \+ 1 securities in the market.
Given an economic state which is modelled by a finite state Markov chain, the return of each security at a
fixed time point is a random variable. The return random variables may be different if the economic state is
changed even for the same security at the same time point. We start our analysis from the no\-liability case,
in the spirit of Li and Ng (2000 Li, D. and Ng, W. L. 2000\. Optimal dynamic portfolio selection: Multi\-period
mean\-variance formulation. Mathematical Finance, 10: 387\-406\. \[Crossref], \[Web of Science] , \[Google Scholar]),
both the optimal investment strategy and the efficient frontier are derived. Then we add uncontrollable liability
into the model. By direct comparison with the no\-liability case, the optimal strategy can be derived explicitly.
Cheng, E., Kostyuchyk, N., Lee, W., Liu, P., and Ma, C. (2021\). “Trending Fast and Slow .” In:The Journal of
Portfolio Management .
This article develops a methodology to combine fast and slow time\-series momentum signals using machine
learning techniques based on market volatility. Starting with the US equity market, the authors find that the
performance of a time\-series momentum strategy is determined by both its responsiveness and the market
volatility regime, among other factors. A decision tree gives a simple and insightful way to determine the
threshold in characterizing low\- and high\-volatility regimes. A slow time\-series momentum strategy tends to
outperform a fast time\-series momentum strategy when market volatility is low. The opposite tends to occur
when volatility is high. This pattern of relative performance can be attributed to market\-timing alpha and exists
in most global equity markets, including both developed and emerging markets.
Chiappa, S. (2011\). “Unified Treatment of Hidden Markov Switching Models .” In:arXiv e\-Print .
Many real\-world problems encountered in several disciplines deal with the modeling of time\-series containing
different underlying dynamical regimes, for which probabilistic approaches are very often employed. In this
paper we describe several such approaches in the common framework of graphical models. We give a unified
overview of models previously introduced in the literature, which is simpler and more comprehensive than
previous descriptions and enables us to highlight commonalities and differences among models that were not
observed in the past. In addition, we present several new models and inference routines, which are naturally
derived within this unified viewpoint.
Chollete, L., Heinen, A., and Valdesogo, A. (2009\). “Modeling International Financial Returns with a Multivariate
Regime\-switching Copula .” In:Journal of Financial Econometrics 7(4\), pp. 437–480\.
In order to capture observed asymmetric dependence in international financial returns, we construct a multivari\-
ate regime\-switching model of copulas. We model dependence with one Gaussian and one canonical vine copula
regime. Canonical vines are constructed from bivariate conditional copulas and provide a very flexible way of
characterizing dependence in multivariate settings. We apply the model to returns from the G5 and Latin Amer\-
ican regions, and document three main findings. First, we discover that models with canonical vines generally
dominate alternative dependence structures. Second, the choice of copula is important for risk management,
since it modifies the Value\-at\-Risk (VaR) of international portfolios and produces a better out\-of\-sample perfor\-
mance. Third, ignoring asymmetric dependence and regime\-switching in portfolio selection leads to significant
costs for an investor.
Chowdhury, M. S. R., Damianov, D. S., and Elsayed, A. H. (2021\). “Bubbles and Crashes in Cryptocurrencies:
Interdependence, Contagion, or Asset Rotation? ” In:SSRN e\-Print .
Using a quantile vector autoregressive model to capture return dynamics in extreme market conditions, we find
that the cryptocurrency market exhibits a high level of market connectedness. Bitcoin is a net transmitter of
returnspilloversduringbustsandanetreceiverduringbooms.Analysisofthetimingofbubbleandcrashperiods
uncovers the presence of interdependence and contagion effects. There is only limited evidence for asset rotation,
26and it involves mostly Ripple. Bubbles in Ripple occur simultaneously or are followed by crashes in other major
cryptocurrencies which highlights its unique role as a portfolio diversifier in extreme market conditions.
Chuffart, T. (2017\). “An Implementation of Markov Regime Switching GARCH Models in Matlab .” In:SSRN
e\-Print.
MSGtool is a MATLAB toolbox which provides a collection of functions for the simulation and estimation
of a large variety of Markov Switching GARCH (MSG) models. Currently, the software integrates a method
to select the best starting values for the estimation and a post\-estimation analysis to ensure the convergence.
The toolbox is very flexible a user\-friendly with a large number possible options. In this paper, we give some
illustrative examples.
Clacher, I., Freeman, M., Hillier, D., Kemp, M., and Zhang, Q. (2015\). “A Practical Guide to Regime Switching in
Financial Economics .” In:Quantitative Financial Risk Management: Theory and Practice . Ed. by C. Zopounidis
and E. Galariotis. John Wiley and Sons, Inc, pp. 71–97\.
In this chapter, we introduce the principles and applications of Markov Regime Switching Models in financial
economics. Real world asset return dynamics are complex and do not follow the standard assumptions of being
independently and identically normally distributed (i.i.n.d.). As a result, standard models with logarithmic
returns often fail to capture the underling processes in the data and the presence of time\-varying correlations.
One way in which academics and practitioners can better model these dynamics is through Markov Regime
Switching Models. We therefore introduce some of the basic concepts in this area; provide an overview of some
of the economic contexts where this modelling has been applied; and finish by providing a discussion around the
challenges in properly implementing these models in a real world context.
Corbelli,R.,Vellasco,M.,andVeiga,A.(2020\). “InvestigatingOptimalRegimesforPredictionintheStockMarket .”
In:IEEE Congress on Evolutionary Computation (CEC) . IEEE.
Forecastingstockpricesinthemarketitsknowntobeanextremelydifficulttask,whereeventhepredictabilityof
the series itself is a controversial matter. The present study investigates the existence of periods within the series
more suitable for prediction, and whether the identification and exploitation of those periods could be learned
from data. In order to do that, the Predictability Crawler (P\-Craw) framework is proposed. The technique uses
optimizations routines such as the Particle Swarm optimization (PSO) or Genetic Algorithms (GA) to select
subsets of historical data where statistical learning algorithms can be more efficiently trained. When tested
against simulated data, The P\-Craw is able to reliably identify the optimal subsets in scenarios ranging from
40% to 100% of predictable samples in the data. To access if the framework brings any improvement when used
in a real world scenario, it is tested in a dataset containing intraday data from the Brazilian stocks exchange
(BOVESPA). When benchmarked against training with all the samples for the series in the BOVESPA dataset
the use of the framework is able to significantly raise the Correct Directional Changes (CDC) of the trained
models while reducing the Mean Absolute Error (MAE) in up to 19%.
Costa,G.andKwon,R.H.(2019\). “RiskparityportfoliooptimizationunderaMarkovregime\-switchingframework .”
In:Quantitative Finance 19(33\), pp. 453–471\.
We formulate and solve a risk parity optimization problem under a Markov regime\-switching framework to
improve parameter estimation and to systematically mitigate the sensitivity of optimal portfolios to estimation
error.Aregime\-switchingfactormodelofreturnsisintroducedtoaccountfortheabruptchangesinthebehaviour
of economic time series associated with financial cycles. This model incorporates market dynamics in an effort
to improve parameter estimation. We proceed to use this model for risk parity optimization and also consider
the construction of a robust version of the risk parity optimization by introducing uncertainty structures to the
estimated market parameters. We test our model by constructing a regime\-switching risk parity portfolio based
on the Fama\-French three\-factor model. The out\-of\-sample computational results show that a regime\-switching
risk parity portfolio can consistently outperform its nominal counterpart, maintaining a similar ex post level of
risk while delivering higher\-than\-nominal returns over a long\-term investment horizon. Moreover, we present a
dynamic portfolio rebalancing policy that further magnifies the benefits of a regime\-switching portfolio.
Costa, G. and Kwon, R. H. (2020\). “A regime\-switching factor model for mean\-variance optimization .” In:Journal
of Risk22(4\), pp. 31–59\.
We formulate a novel Markov regime\-switching factor model to describe the cyclical nature of asset returns in
modern financial markets. Maintaining a factor model structure allows us to easily derive the asset expected
returns and their corresponding covariance matrix. By design, these two parameters are calibrated to better
describe the properties of the different market regimes. In turn, these regime\-dependent parameters serve as the
inputs during mean\-variance optimization, thereby constructing portfolios adapted to the current market envi\-
27ronment.Throughthisformulation,theproposedmodelallowsfortheconstructionoflarge,realisticportfoliosat
no additional computational cost during optimization. Moreover, the viability of this model can be significantly
improved by periodically rebalancing the portfolio, ensuring proper alignment between the estimated parameters
and the transient market regimes. An out\-of\-sample computational experiment over a long investment horizon
shows that the proposed regime\-dependent portfolios are better aligned with the market environment, yielding
a higher ex post rate of return and lower volatility than competing portfolios.
Cram, R. G. (2020\). “Late to Recessions: Stocks and the Business Cycle .” In:SSRN e\-Print .
I find that returns are predictably negative for several months after the onset of recessions, and only become
high thereafter. I identify business\-cycle turning points by estimating a state\-space model using macroeconomic
data. Conditioning on the business cycle further reveals that returns exhibit momentum in recessions, whereas
in expansions they display the mild reversals expected from discount rate changes. A market timing strategy
that optimally exploits this business\-cycle pattern produces a 60% increase in the buy\-and\-hold Sharpe ratio.
I find that a subset of hedge funds add value for their clients in part by avoiding stock market crashes during
recessions.
Dai, M., Jin, H., Kou, S., and Xu, Y. (2021\). “Robo\-Advising: A Dynamic Mean\-Variance Approach .” In:SSRN
e\-Print.
In contrast to traditional financial advising, robo\-advising needs to elicit investors’ risk profile via several simple
online questions and provide advice consistent with conventional investment wisdom, e.g., rich and young people
should invest more in risky assets. To meet the two challenges, we propose to do the asset allocation part of robo\-
advisingusingadynamicmean\-variancecriterionoverthetheportfolio’slog\-returns.Themodelyieldsanalytical
and time\-consistent optimal portfolio policies under jump\-diffusion models and regime\-switching models.
Dal Pra, G., Guidolin, M., Pedio, M., and Vasile, F. (2018\). “Regime Shifts in Excess Stock Return Predictability:
An Out\-of\-Sample Portfolio Analysis .” In:The Journal of Portfolio Management 44(3\), pp. 10–24\.
The authors analyze the out\-of\-sample performance of asset allocation decisions based on financial ratio pre\-
dictability of aggregate stock market returns under linear and regime\-switching models. The authors adopt both
a statistical perspective to analyze whether models based on valuation ratios can forecast excess equity returns,
and an economic approach that turns predictions into portfolio strategies. These consist of a portfolio switching
approach, a mean\-variance framework, and a long\-run dynamic model. The authors find a disconnect between
the statistical perspective, whereby the ratios yield a modest forecasting power, and a portfolio approach, by
which a moderate predictability is often sufficient to yield significant portfolio outperformance, especially be\-
fore transaction costs and when regimes are taken into account. However, also when regimes are considered,
predictability gives high payoffs only to long horizon, highly risk\-averse investors. Moreover, different strategies
deliver different performance rankings across predictors.
Dapena, J. P., Serur, J. A., and Siri, J. R. (2020\). “Risk On\-Risk Off: A Regime Switching Model for Active Portfolio
Management .” In:SSRN e\-Print .
Unlike passive management, where investors almost do not buy and sell securities, active management involves
a set of trading rules that govern investment decisions regarding mainly market timing. In this paper, we take
the basics of active management and the two fund separation approach, to exploit the fact that an investor
can switch between the market portfolio and the risk free asset according to the perceived state of the nature.
Our purpose is to evaluate if there is an active management premium by testing performance with our own
non\-conventional multifactor model, constructed with a Hidden Markov Model which depending on the market
states signaled by the level of volatility spread. We have documented that effectively, there is present a premium
for actively manage the strategies, giving evidence against the idea that managers destroy capital. We then
propose the volatility spread as the active management factor into the Carhart’s model used to evaluate trading
strategies with respect to a benchmark portfolio.
Das, S. R., Ostrov, D. N., Casanova, A., Radhakrishnan, A., and Srivastav, D. (2021\). “Optimal Goals\-Based
Investment Strategies For Switching Between Bull and Bear Markets .” In:SSRN e\-Print .
We apply dynamic programming to solve a long\-horizon fund choice problem, given that the underlying market
can switch between different regimes. The objective function is based on reaching a target level of wealth,
following the paradigm of goal\-based investing. In a world with a good regime (e.g., a bull market) and a bad
regime (e.g., a bear market), we find that an investor who is cognizant of regime switching can potentially do
much better over time than an investor who assumes there is only one regime. However, there is a caveat—an
investor must be able to predict the regime they are in with reasonable levels of confidence, and if not, they are
in fact worse off than an investor who assumes just one regime. Using data from recent history, we find that
28investors may be better off not switching from existing single\-regime models to more complex multiple\-regime
models.
Das, S. R., Ostrov, D. N., Casanova, A., Radhakrishnan, A., and Srivastav, D. (2022\). “Optimal Goals\-Based
Investment Strategies For Switching Between Bull and Bear Markets .” In:The Journal of Wealth Management
24(4\), pp. 8–36\.
We solve a dynamic, long\-horizon, goals\-based wealth management problem, given different investment regimes.
In a world with a good regime (bull market) and a bad regime (bear market), an investor who is cognizant
that regime switching occurs has the potential to do better than an investor who assumes only one regime.
However, models with more than one regime incur the additional risk of regime uncertainty. Investors must be
able to predict which regime is governing the market with reasonable levels of confidence, or they can be worse
off than investors who assume just one regime. Using data from recent history, we develop a framework that
determines how accurate regime prediction needs to be to achieve gains from a regime\-cognizant goals\-based
investing approach.
Das, S., Islam, M. R., Jayakodi, N. K., and Doppa, J. R. (2019\). “Active Anomaly Detection via Ensembles: Insights,
Algorithms, and Interpretability .” In:arXiv e\-Print .
Anomaly detection (AD) task corresponds to identifying the true anomalies from a given set of data instances.
AD algorithms score the data instances and produce a ranked list of candidate anomalies, which are then
analyzed by a human to discover the true anomalies. However, this process can be laborious for the human
analyst when the number of false\-positives is very high. Therefore, in many real\-world AD applications including
computer security and fraud prevention, the anomaly detector must be configurable by the human analyst to
minimize the effort on false positives. In this paper, we study the problem of active learning to automatically
tune ensemble of anomaly detectors to maximize the number of true anomalies discovered. We make four main
contributions towards this goal. First, we present an important insight that explains the practical successes of
AD ensembles and how ensembles are naturally suited for active learning. Second, we present several algorithms
for active learning with tree\-based AD ensembles. These algorithms help us to improve the diversity of discovered
anomalies, generate rule sets for improved interpretability of anomalous instances, and adapt to streaming data
settings in a principled manner. Third, we present a novel algorithm called GLocalized Anomaly Detection
(GLAD) for active learning with generic AD ensembles. GLAD allows end\-users to retain the use of simple
and understandable global anomaly detectors by automatically learning their local relevance to specific data
instances using label feedback. Fourth, we present extensive experiments to evaluate our insights and algorithms.
Our results show that in addition to discovering significantly more anomalies than state\-of\-the\-art unsupervised
baselines, our active learning algorithms under the streaming\-data setup are competitive with the batch setup.
Demos, G. and Sornette, D. (2017\). “Birth or burst of financial bubbles: which one is easier to diagnose? ” In:
Quantitative Finance 17(5\), pp. 657–675\.
Abreu and Brunnermeier (2003\) have argued that bubbles are not suppressed by arbitrageurs because they fail to
synchronise on the uncertain beginning of the bubble. We propose an indirect quantitative test of this hypothesis
and confront it with the alternative according to which bubbles persist due to the difficulty of agreeing on the
end of bubbles. We present systematic tests of the precision and reliability with which the beginning t1 and end
tc of a bubble can be determined.For this, we use a specific bubble model, the log\-periodic power law singularity
(LPPLS) model, which represents a bubble as a transient noisy super\-exponential price trajectory decorated by
acceleratedvolatilityoscillations.Generalisingtheestimationproceduretoendogenisethebeginningofthefitting
time interval, we quantify the uncertainty on the calibrated t1 and tc (as well as the other model parameters) via
theeigenvaluesoftheHessianmatrix,whichcharacterisetheshapeofthecalibrationcostfunctioninthedifferent
directions in parameter space, on many synthetic data and four historical bubble cases. We find overwhelming
evidence that the beginning of bubbles is much better constrained that their end. Our results are robust over
all four empirical bubbles and many synthetic tests, as well as when changing the time of analysis (the present
) during the development of the bubbles. As a bonus, we find that the two structural parameters of the LPPLS
model, the exponent m controlling the super\-exponential growth of price and the angular log\-periodic frequency
omega describing the log\-periodic acceleration of volatility, are very rigid according the Hessian matrix analysis,
which supports the LPPLS model as a reasonable candidate for describing the generating process of prices during
bubbles.
Dette,H.,Eckle,T.,andVetter,M.(2021\). “Multiscalechangepointdetectionfordependentdata .”In:Scandinavian
Journal of Statistics .
29Inthisarticlewestudythetheoreticalpropertiesofthesimultaneousmultiscalechangepointestimator(SMUCE)
in piecewise\-constant signal models with dependent error processes. Empirical studies suggest that in this case
the change point estimate is inconsistent, but it is not known if alternatives suggested in the literature for
correlated data are consistent. We propose a modification of SMUCE scaling the basic statistic by the long
run variance of the error process, which is estimated by a difference\-type variance estimator calculated from
local means from different blocks. For this modification we prove model consistency for physical\-dependent error
processes and illustrate the finite sample performance by means of a simulation study.
Dette, H., Wu, W., and Zhou, Z. (2019\). “Change Point Analysis of Correlation in Non\-stationary Time Series .” In:
Statistica Sinica (29\), pp. 611–643\.
A restrictive assumption in change point analysis is ”stationarity under the null hypothesis of no change\-point”,
which is crucial for asymptotic theory but not very realistic from a practical point of view. For example, if
change point analysis for correlations is performed, it is not necessarily clear that the mean, marginal variance
or higher order moments are constant, even if there is no change in the correlation. This paper develops change
point analysis for the correlation structures under less restrictive assumptions. In contrast to previous work, our
approach does not require that the mean, variance and fourth order joint cumulants are constant under the null
hypothesis. Moreover, we also address the problem of detecting relevant change points.
Dias, J. G., Vermunt, J. K., and Ramos, S. (2015\). “Clustering financial time series: New insights from an extended
hidden Markov model .” In:European Journal of Operational Research 243(3\), pp. 852–864\.
In recent years, large amounts of financial data have become available for analysis. We propose exploring returns
from 21 European stock markets by model\-based clustering of regime switching models. These econometric
models identify clusters of time series with similar dynamic patterns and moreover allow relaxing assumptions
of existing approaches, such as the assumption of conditional Gaussian returns. The proposed model handles
simultaneouslytheheterogeneityacrossstockmarketsandovertime,i.e.,time\-constantandtime\-varyingdiscrete
latent variables capture unobserved heterogeneity between and within stock markets, respectively. The results
showacleardistinctionbetweentwogroupsofstockmarkets,eachonecharacterizedbydifferentregimeswitching
dynamics that correspond to different expected return\-risk patterns. We identify three regimes: the so\-called bull
and bear regimes, as well as a stable regime with returns close to 0, which turns out to be the most frequently
occurring regime. This is consistent with stylized facts in financial econometrics.
Ding, Z. (2012\). “An Implementation of Markov Regime Switching Model with Time Varying Transition Probabil\-
ities in Matlab .” In:SSRN e\-Print .
This memo explains how to use the MATLAB code for estimating a Markov Regime Switching Model with time
varying transition probabilities. The code is developed by Zhuanxin Ding based on the original code by Marcelo
Perlin for estimating a Markov Regime Switching Model with constant transition probability matrix.
Dou, P. Y., Gallagher, D. R., Schneider, D., Walter, T., and Berkman, H. (2014\). “Cross\-region and cross\-sector
asset allocation with regimes .” In:Accounting and Finance 54(3\), pp. 809–846\.
Cross\-region and cross\-sector asset allocation decisions are one of the most fundamental issues in international
equity portfolio management. Equity returns exhibit higher volatilities and correlations, and lower expected
returns, in bear markets compared to bull markets. However, static mean\-variance analysis fails to capture this
salient feature of equity returns. We accommodate the nonlinearity of returns using a regime switching model
across both regions and sectors. The regime\-dependent asset allocation potentially adds value to the traditional
static mean\-variance allocation. In addition, optimal allocation across sectors provide greater benefits compared
to international diversification, which is characterized by higher returns, lower risks, lower correlations with the
world market and a higher Sharpe ratio.
Douady, R. and Kornprobst, A. (2018\). “An Empirical Approach to Financial Crisis Indicators Based on Random
Matrices .” In:International Journal of Theoretical and Applied Finance 21(03\), p. 1850022\.
The aim of this work is to build a class of financial crisis indicators based on the spectral properties of the
dynamics of market data. After choosing an appropriate size for a rolling window, the historical market data
inside this rolling window are seen every trading day as a random matrix from which a correlation matrix
is obtained. Our goal is to study the correlations between the assets that constitute this market and look for
reproducible patterns that are indicative of an impending financial crisis. A weighting of the assets in the market
is then introduced and is proportional to the daily traded volumes. This manipulation is realized in order to give
more importance to the most liquid assets. Our financial crisis indicators are based on the spectral radius of this
weighted correlation matrix. The idea behind this type of financial crisis indicators is that large eigenvalues are a
30sign of dynamic instability. The out\-of\-sample predictive power of the financial crisis indicators in this framework
is then demonstrated, in particular by using them as decision\-making tools in a protective put strategy.
Duprey, T. and Klaus, B. (2017\). “How to Predict Financial Stress? An Assessment of Markov Switching Models .”
In:SSRN e\-Print .
This paper predicts phases of the financial cycle by combining a continuous financial stress measure in a Markov
switching framework. The debt service ratio and property market variables signal a transition to a high financial
stressregime,whileeconomicsentimentindicatorsprovidesignalsforatransitiontoatranquilstate.Whereasthe
in\-sample analysis suggests that these indicators can provide an early warning signal up to several quarters prior
to the respective regime change, the out\-of\-sample findings indicate that most of this performance is due to the
data gathered during the global financial crisis. Comparing the prediction performance with a standard binary
early warning model reveals that the MS model is outperforming in the vast majority of model specifications
for a horizon up to three quarters prior to the onset of financial stress.
Edirisinghe, C. and Zhao, Y. (2020\). “Smart Indexing Under Regime\-Switching Economic States .” In:Applied
Mathematical Finance 27(5\), pp. 422–456\.
Index funds that track a benchmark, such as the market cap\-weighted S\&P 500 index, tend to have portfolio
holdings biased towards slower\-growth large\-cap equities that result in the fund’s under\-performance, especially
in economic downturns. We develop a rigorous quantitative framework that allows dynamic\-rebalancing of the
allocations such that portfolio exposure in a market segment can change periodically based on economic activity,
measured via a set of macro\-economic and financial indicators. The method incorporates potential shifts in the
economic state, and the likelihood thereof, to determine the fund’s risk orientation optimally in tracking or not
tracking the benchmark index. That is, the greater the likelihood of a stronger economic state, the higher the
degree of tracking the market index; however, a lack of confidence in the economic state results in a more index\-
neutral portfolio composition. The proposed smart indexing optimal strategy generates superior risk\-adjusted
returns consistently in out\-of\-sample testing, relative to (pure) index tracking. We test several variants and
present sensitivity analyses that support our actively\-managed smart indexing approach.
Elkamhi, R., Lee, J., and Salerno, M. (2021\). “Portfolio Tilts using Views on Macroeconomic Regimes .” In:SSRN
e\-Print.
Long\-term investors rebalance their portfolios given their views on the investment landscape. Portfolio tilting
is often implemented using investors’ views on point estimates of asset expected returns which are notoriously
difficult to estimate and lead to unstable portfolio weights. We avoid such shortcomings by providing a method\-
ology that incorporates views on the likelihood of economic regimes (e.g., growth and inflation). Using data on
equities, bonds and commodities, we show \- both in simulation and empirically \- that our approach generates
stable portfolio weights and a performance that is minimally affected by forecast errors.
Elkind, D., Kaminski, K., Lo, A. W., Siah, K. W., and Wong, C. H. (2022\). “When Do Investors Freak Out?
Machine Learning Predictions of Panic Selling .” In:The Journal of Financial Data Science 4(1\), pp. 11–39\.
Using a novel dataset of 653,455 individual brokerage accounts belonging to 298,556 households, the authors
document the frequency, timing, and duration of panic sales, which they define as a decline of 90% of a household
account’s equity assets over the course of one month, of which 50% or more is due to trades. The authors find
that a disproportionate number of households make panic sales when there are sharp market downturns, a
phenomenon they call freaking out. The authors also show that panic selling and freak\-outs are predictable and
fundamentally different from other well\-known behavioral patterns such as overtrading or the disposition effect.
Elliott, G. and Timmermann, A. (2005\). “Optimal forecast combination under regime switching .” In:International
Economic Review 46(4\), pp. 1081–1102\.
This article proposes a new forecast combination method that lets the combination weights be driven by regime
switching in a latent state variable. An empirical application that combines forecasts from survey data and
time series models finds that the proposed regime switching combination scheme performs well for a variety of
macroeconomic variables. Monte Carlo simulations shed light on the type of data\-generating processes for which
the proposed combination method can be expected to perform better than a range of alternative combination
schemes. Finally, we show how time variations in the combination weights arise when the target variable and
the predictors share a common factor structure driven by a hidden Markov process.
Elouai, H. M., Lambinet, R., and Morel, T. (2013\). “Bubbles and Regimes: Two Complementary Approaches.” In:
SSRN e\-Print .
The financial risk associated with financial bubbles (both large and small) is difficult to analyse using traditional
risk models. The ability to detect bubbles before they burst represents a major challenge in itself. We believe
31that the issue raised by financial bubbles can contribute to discussions on the risk\-on/risk\-off theory as identified
by the various regime switches. In addition to a signal indicating the presence of bubbles, we need a second
signal to help us determine the theoretical date that the bubble will burst in order to determine the optimal
exit time. Our approach is built on a combination of two quantitative models: a bubble detection model and a
Markov regime\-switching model. These signals offer two benefits: generating absolute performance and limiting
extreme risk (the tail\-risk hedging strategy). Although we only illustrate the results with the SandP 500, the
approach should be generalised to all asset classes.
Endres, S. and Stubinger, J. (2019\). “A flexible regime switching model with pairs trading application to the S\&P
500 high\-frequency stock returns .” In:Quantitative Finance , pp. 1–14\.
This paper develops the regime classification algorithm and applies it within a fully\-fledged pairs trading frame\-
work on minute\-by\-minute data of the SandP 500 constituents from 1998 to 2015\. Specifically, the highly flexible
algorithm automatically determines the number of regimes for any stochastic process and provides a complete
set of parameter estimates. We demonstrate its performance in a simulation study algorithm achieves promising
results for the general class of Levy\-driven Ornstein\-Uhlenbeck processes with regime switches. In our empirical
back\-testing study, we apply our regime classification algorithm to propose a high\-frequency pair selection and
trading strategy. The results show statistically and economically significant returns with an annualized Sharpe
ratio of 3\.92 after transaction costs remain stable even in recent years. We compare our strategy with existing
quantitative trading frameworks and find its results to be superior in terms of risk and return characteristics.
The ...
Engle, R. F. and Ruan, T. (2019\). “Measuring the probability of a financial crisis .” In:Proceedings of the National
Academy of Sciences 116(37\), pp. 18341–18346\.
This study develops quantitative estimates of the level of systemic risk in the financial sector that precipitates a
financial crisis. When financial firms are undercapitalized, they face difficulty in covering losses in a downturn.
The natural response to such vulnerability, reducing leverage through asset sales, can start a financial crisis.
Perilous excessive credit growth is reflected in the undercapitalization of the financial sector. Market\-based
indicators of systemic risk such as SRISK, which stands for systemic risk, measure such weakness in real time.
We develop a probability of crisis measure and an SRISK capacity measure for 23 developed countries. Our
analysis highlights the important global externality whereby the risk of a crisis in one country depends on the
undercapitalization of the rest of the world.
Erlwein, C., Mitra, G., and Roman, D. (2012\). “HMM based scenario generation for an investment optimisation
problem.” In:Annals of Operations Research 193(1\), pp. 173–192\.
The Geometric Brownian motion (GBM) is a standard method for modelling financial time series. An important
criticism of this method is that the parameters of the GBM are assumed to be constants; due to this fact,
important features of the time series, like extreme behaviour or volatility clustering cannot be captured. We
propose an approach by which the parameters of the GBM are able to switch between regimes, more precisely
they are governed by a hidden Markov chain. Thus, we model the financial time series via a hidden Markov
model (HMM) with a GBM in each state. Using this approach, we generate scenarios for a financial portfolio
optimisation problem in which the portfolio CVaR is minimised. Numerical results are presented.
Erlwein\-Sayer, C., Grimm, S., Sass, J., and Sayer, T. (2016\). “Portfolio Strategies and Estimation in a Hidden
Markov Model Using State Dependent, State Independent or No Correlation .” In:SSRN e\-Print .
We consider portfolio optimization in a regime\-switching market. The assets of the portfolio are modeled through
ahiddenMarkovmodel(HMM)indiscretetime,wheredriftandvolatilityareallowedtoswitchbetweendifferent
states. We consider different parametrizations of the involved asset covariances namely state\-wise uncorrelated
assets, which are though linked through the common Markov chain, assets correlated in a state\-independent
way, and assets where the correlation varies from state to state. As a control model, we also consider a model
without regime switches. We utilize a filter\-based EM\-algorithm to obtain optimal parameter estimates within
this multivariate HMM and develop parameter estimators in all three HMM settings. We discuss the impact of
these different models on the performance of several portfolio strategies. Our findings show that for simulated
returns our strategies often outperform naive investment strategies, like the equal weights strategy. Information
criteria can be used to detect the best model for estimation as well as for portfolio optimization. A second study
using real data confirms these findings.
Filimonov, V., Demos, G., and Sornette, D. (2017\). “Modified profile likelihood inference and interval forecast of
the burst of financial bubbles .” In:Quantitative Finance 17(8\), pp. 1167\-11861–20\.
32We present a detailed methodological study of the application of the modified profile likelihood method for
the calibration of nonlinear financial models characterized by a large number of parameters. We apply the
general approach to the Log\-Periodic Power Law Singularity (LPPLS) model of financial bubbles. This model is
particularlyrelevantbecauseoneofitsparameters,thecriticaltimesignallingtheburstofthebubble,isarguably
the target of choice for dynamical risk management. However, previous calibrations of the LPPLS model have
shown that the estimation of is in general quite unstable. Here, we provide a rigorous likelihood inference
approach to determine , which takes into account the impact of the other nonlinear (so\-called ?nuisance?)
parameters for the correct adjustment of the uncertainty on . This provides a rigorous interval estimation for
the critical time, rather than the point estimation in previous approaches. As a bonus, the interval estimates can
alsobeobtainedforthenuisanceparameters(,damping),whichcanbeusedtoimprovefilteringofthecalibration
results. We show that the use of the modified profile likelihood method dramatically reduces the number of local
extrema by constructing much simpler smoother log\-likelihood landscapes. The remaining distinct solutions can
be interpreted as genuine scenarios that unfold as the time of the analysis flows, which can be compared directly
via their likelihood ratio. Finally, we develop a multi\-scale profile likelihood analysis to visualize the structure
of the financial data at different scales (typically from 100 to 750 days). We test the methodology successfully
on synthetic price time series and on three well\-known historical financial bubbles.
Fischer, E. O. and Murg, M. (2015\). “A combined regime\-switching and Black Litterman model for optimal asset
allocation .” In:Journal of Investment Strategies 4(3\), pp. 1–36\.
Traditionally, portfolios are optimized with a single\-regime Markowitz model, using volatility as the risk measure
and historical return as the expected return. This paper shows what effects a regime\-switching framework,
alternative risk measures (modifiedvalue\-at\-risk and conditional value\-at\-risk) and return measures (capital asset
pricing model estimates and Black Litterman estimates) can have on asset allocation as well as the absolute
and relative performance of portfolios. We show that the combination of alternative risk and return measures
within the regime\-switching framework gives significantly better results in terms of performance and a modified
Sharpe ratio. The use of alternative risk and return measures also mitigates the issue that asset returns are not
often normally distributed or serially correlated. To eliminate the empirical shortcomings of asset returns, an
unsmoothing algorithm in combination with the Cornish\-Fisher expansion is used.
Flint, E., Seymour, A., and Chikurunhe, F. (2021\). “Defining and measuring portfolio diversification .” In:South
African Actuarial Journal 20(1\), pp. 17–48\.
It is often said that diversification is the only ’free lunch’ available to investors; meaning that a properly
diversified portfolio reduces total risk without necessarily sacrificing expected return. However, achieving true
diversification is easier said than done, especially when we do not fully know what we mean when we are talking
about diversification. While the qualitative purpose of diversification is well known, a satisfactory quantitative
definitionofportfoliodiversificationremainselusive.Inthisresearch,wesummariseawiderangeofdiversification
measures, focusing our efforts on those most commonly used in practice. We categorise each measure based on
which portfolio aspect it focuses on: cardinality, weights, returns, risk or higher moments. We then apply these
measures to a range of South African equity indices, thus giving a diagnostic review of historical local equity
diversification and, perhaps more importantly, providing a description of the investable opportunity set available
tofund managers in this space. Finally, we introduce the idea of diversification profiles. These regime dependent
profiles give a much richer description of portfolio diversification than their single\-value counterparts and also
allow one to manage diversification proactively based on one’s view of future market conditions.
Flint, E. and du Plooy, S. (2018\). “Extending risk budgeting for market regimes and quantile factor models .” In:
Journal of Investment Strategies 7(4\), pp. 51–74\.
We combine several disparate avenues in the literature to create a novel, unified risk\- based optimization frame\-
work. Specifically, we extend an existing risk\-budgeting approach to allow for changing market regimes and
factor dependence as well as a nonlinear, asymmetric market structure. We show that the existing framework
can be readily extended to include a factor\-dependent return process using standard models available in the
literature. Structural changes in the market conditions are then incorporated into the framework via the use of a
regime\-switching turbulence index, and the nonlinear and asymmetric market dependence structure is accounted
for by using quantile factor models. Most importantly, this extended framework is comprised of a series of linear
models only and is thus simple to understand and to implement. We consider two applications of the extended
framework, namely, scenario analysis and parameter uncertainty analysis, by way of a simple empirical case
study. Finally, we introduce the concept of risk maps, which provide managers with a graphical approach for
estimating and evaluating risk optimality in a multiobjective, multiscenario setting.
33Flint, E. J. and Mare, E. (2019\). “Regime\-Based Tactical Allocation for Equity Factors and Balanced Portfolios .”
In:South African Actuarial Journal 19(1\), pp. 27–52\.
It is now an accepted fact that the majority of financial markets worldwide are neither normal nor constant,
and South Africa is no exception. One idea that can be used to understand such markets and has been gain\-
ing popularity recently is that of regimes and regime\-switching models. In this research, we consider whether
regimes can add value to the asset allocation process. Four methods for regime identification – economic cycle
variables, fundamental valuation metrics, technical market indicators and statistical regime\-switching models –
are discussed and tested on two asset universes – longonly South African equity factor returns and representa\-
tive balanced portfolio asset class returns. We find several promising regime indicators and use these to create
two regime\-based tactical allocation frameworks. Out\-of\-sample testing on both the equity factor and balanced
asset class data shows very promising results, with both regime\-based tactical strategies outperforming their
respective static benchmarks on an absolute return and risk\-adjusted return basis. We also turn our attention to
a potentially major recent development in the local fund management space; namely, the introduction of Capped
Shareholder\-Weighted indices as new benchmarks. We provide comparative analysis between the capped and
uncapped Shareholder\-Weighted indices in terms of sector weights, stock concentration, currency exposure and
factor risk contributions.
Fons, E., Dawson, P., Yau, J., Zeng, X.\-j., and Keane, J. (2021\). “A novel dynamic asset allocation system using
Feature Saliency Hidden Markov models for smart beta investing .” In:Expert Systems with Applications 163,
pp. 113720\+.
The financial crisis of 2008 generated interest in more transparent, rules\-based strategies for portfolio con\-
struction, with smart beta strategies emerging as a trend among institutional investors. Whilst they perform
well in the long run, these strategies often suffer from severe short\-term drawdown (peak\-to\-trough decline)
with fluctuating performance across cycles. To manage short term risk (cyclicality and underperformance), we
build a dynamic asset allocation system using Hidden Markov Models (HMMs). We use a variety of portfolio
construction techniques to test our smart beta strategies and the resulting portfolios show an improvement in
risk\-adjusted returns, especially on more return\-oriented portfolios (up to 50% of return in excess of market
adjusted by relative risk annually). In addition, we propose a novel smart beta allocation system based on the
Feature Saliency HMM (FSHMM) algorithm that performs feature selection simultaneously with the training of
the HMM, to improve regime identification. We evaluate our systematic trading system with real life assets using
MSCI indices; further, the results (up to 60% of return in excess of market adjusted by relative risk annually)
show model performance improvement with respect to portfolios built using full feature HMMs.
Foorthuis, R. (2021\). “On the Nature and Types of Anomalies: A Review .” In:arXiv e\-Print .
Anomalies are occurrences in a dataset that are in some way unusual and do not fit the general patterns.
The concept of the anomaly is generally ill\-defined and perceived as vague and domain\-dependent. Moreover,
no comprehensive and concrete overviews of the different types of anomalies have hitherto been published.
By means of an extensive literature review this study therefore offers the first theoretically principled and
domain\-independent typology of data anomalies, and presents a full overview of anomaly types and subtypes.
To concretely define the concept of the anomaly and its different manifestations the typology employs four
dimensions: data type, cardinality of relationship, data structure and data distribution. These fundamental
and data\-centric dimensions naturally yield 3 broad groups, 9 basic types and 61 subtypes of anomalies. The
typology facilitates the evaluation of the functional capabilities of anomaly detection algorithms, contributes to
explainable data science, and provides insights into relevant topics such as local versus global anomalies.
Francis, N., Owyang, M. T., and Soques, D. (2021\). Business Cycles Across Space and Time . Tech. rep. SSRN
e\-Print.
Westudythecomovementofinternationalbusinesscyclesinatimeseriesclusteringmodelwithregime\-switching.
We extend the framework of Hamilton and Owyang (2012\) to include time\-varying transition probabilities to
determinewhatdrivessimilaritiesinbusinesscycleturningpoints.Wefindfourgroups,or”clusters”,ofcountries
which experience idiosyncratic recessions relative to the global cycle. Additionally, we find the primary indicators
of international recessions to be fluctuations in equity markets and geopolitical uncertainty. In out\-of\-sample
forecasting exercises, we find that our model is an improvement over standard benchmark models for forecasting
both aggregate output growth and country\-level recessions.
Fulop, A. and Yu, J. (2017\). “Bayesian analysis of bubbles in asset prices .” In:Econometrics 5(4\), p. 47\.
We develop a new model where the dynamic structure of the asset price, after the fundamental value is removed,
is subject to two different regimes. One regime reflects the normal period where the asset price divided by the
34dividend is assumed to follow a mean\-reverting process around a stochastic long run mean. The second regime
reflects the bubble period with explosive behavior. Stochastic switches between two regimes and non\-constant
probabilities of exit from the bubble regime are both allowed. A Bayesian learning approach is employed to
jointly estimate the latent states and the model parameters in real time. An important feature of our Bayesian
methodisthatweareabletodealwithparameteruncertaintyandatthesametime,tolearnaboutthestatesand
the parameters sequentially, allowing for real time model analysis. This feature is particularly useful for market
surveillance. Analysis using simulated data reveals that our method has good power properties for detecting
bubbles. Empirical analysis using price\-dividend ratios of SandP500 highlights the advantages of our method.
Gallagher, L. A., Hutchinson, M. C., and O’Brien, J. (2020\). “Using Smooth Transition Regressions to Model
Risk Regimes .” In:Handbook of Financial Econometrics, Mathematics, Statistics, and Machine Learning . World
Scientific, pp. 4281–4311\.
The smooth transition regression (STR) methodology was developed to model nonlinear relationships in the
business cycle. We demonstrate the methodology can be used to analyse return series where exposure to financial
market risk factors depends on market regime. The smooth transition between regimes inherent in STR is
particularly appropriate for risk models as it allows for gradual transition of risk factor exposures. Variations
in the methodology and tests its appropriateness are defined and discussed. We apply the STR methodology
to model the risk of the return series of the convertible arbitrage (CA) hedge fund strategy. CA portfolios
are comprised of instruments that have both equity and bond characteristics and alternate between the two
dependingonmarketlevel(state).ThedualcharacteristicsmaketheCAstrategyastrongcandidatefornonlinear
risk models. Using the STR model, we confirm that the strategy’s risk factor exposure changes with market
regime and, using this result, are able to account for the abnormal returns reported for the strategy in earlier
studies.
Gao, G., Ho, K.\-Y., and Shi, Y. (2018\). “Long memory or regime switching in volatility? Evidence from high\-
frequency returns on the U.S. stock indices .” In:Pacific\-Basin Finance Journal .
Recent research suggests that long memory and regime switching can be effectively distinguished, if the cause
of the confusion between them is properly controlled for. Motivated by this idea, our study aims to distinguish
between them in modelling stock return volatility. We firstly model long memory and regime switching in
volatility via the Long\-Memory GARCH (LMGARCH) and Markov Regime\-Switching GARCH (MRS\-GARCH)
models, respectively. A theoretical cause of the confusion between those processes is proposed with simulation
evidence. Adopting the ideas of existing studies, an MRS\-LMGARCH framework is further developed to control
for this cause. Our Monte Carlo studies show that this model can effectively distinguish between the pure
LMGARCH and pure MRS\-GARCH processes. Finally, empirical studies of NASDAQ and SandP 500 index
returns are conducted to demonstrate that our MRS\-LMGARCH model can provide potentially more reliable
estimates of the long\-memory parameter, identify the volatility states and outperform both the LMGARCH and
MRS\-GARCH models.
Gatumel, M. and Ielpo, F. (2014\). “The Number of Regimes Across Asset Returns: Identification and Economic
Value.” In:International Journal of Theoretical and Applied Finance 17(06\), pp. 1450040\+.
A shared belief in the financial industry is that markets are driven by two types of regimes: bull markets,
characterized by high returns and low volatility, and bear markets, characterized by low returns coupled with
high volatility. Modeling the dynamics of different asset classes (stocks, bonds, commodities and currencies)
with a Markov switching (MS) model and using a density\-based test, we reject the hypothesis that two\-regimes
are enough to capture asset return evolutions for many of the investigated assets. Once the accuracy of our test
methodology has been assessed through Monte Carlo experiments, our empirical results point out that between
two and five regimes are required to capture the features of each asset’s distribution. Moreover, we show that
only a part of the underlying number of regimes is explained by the distributional characteristics of the returns
such as kurtosis. A thorough out\-of\-sample analysis provides additional evidence that there are more than just
bulls and bears in financial markets. Finally, we highlight that taking into account the real number of regimes
allows both improved portfolio returns and density forecasts.
Geiger, A., Liu, D., Alnegheimish, S., Cuesta\-Infante, A., and Veeramachaneni, K. (2020\). “TadGAN: Time Series
Anomaly Detection Using Generative Adversarial Networks .” In:arXiv e\-Print .
Time series anomalies can offer information relevant to critical situations facing various fields, from finance
and aerospace to the IT, security, and medical domains. However, detecting anomalies in time series data is
particularlychallengingduetothevaguedefinitionofanomaliesandsaiddata’sfrequentlackoflabelsandhighly
complex temporal correlations. Current state\-of\-the\-art unsupervised machine learning methods for anomaly
35detection suffer from scalability and portability issues, and may have high false positive rates. In this paper,
we propose TadGAN, an unsupervised anomaly detection approach built on Generative Adversarial Networks
(GANs). To capture the temporal correlations of time series distributions, we use LSTM Recurrent Neural
Networks as base models for Generators and Critics. TadGAN is trained with cycle consistency loss to allow for
effective time\-series data reconstruction. We further propose several novel methods to compute reconstruction
errors, as well as different approaches to combine reconstruction errors and Critic outputs to compute anomaly
scores. To demonstrate the performance and generalizability of our approach, we test several anomaly scoring
techniques and report the best\-suited one. We compare our approach to 8 baseline anomaly detection methods
on 11 datasets from multiple reputable sources such as NASA, Yahoo, Numenta, Amazon, and Twitter. The
results show that our approach can effectively detect anomalies and outperform baseline methods in most cases
(6 out of 11\). Notably, our method has the highest averaged F1 score across all the datasets. Our code is open
source and is available as a benchmarking tool.
Gerlach, J.\-C., Kreuser, J. L., and Sornette, D. (2020\). “Crash\-sensitive Kelly Strategy built on a modified Kreuser\-
Sornette bubble model tested over three decades of twenty equity indices .” In:SSRN e\-Print .
We present a modified version of the super\-exponential rational expectations ”Efficient Crashes” bubble model of
(Kreuser and Sornette, 2019\) with a different formulation of the expected return that makes clearer the additive
nature of corrective jumps. We derive a Kelly trading strategy for the new model. We combine the strategy
with a simplified estimation procedure for the model parameters from price time series. We optimize the control
parameters of the trading strategy by maximizing the return\-weighted accuracy of trades. This enables us to
predict the out\-of\-sample optimal investment, purely based on in\-sample calibration of the model on historical
data. Our approach solves the difficult problem of selecting the portfolio rebalancing time, as we endogenize it
as an optimization parameter. We develop an ex\-ante backtest that allows us to test our strategy on twenty
equity asset indices. We find that our trading strategy achieves positive trading performance for 95% of tested
assets and outperforms the Buy\-and\-Hold\-Strategy in terms of CAGR and Sharpe Ratio in 60% of cases. In our
simulations, we do not allow for any short trading or leverage. Thus, we simply simulate allocation of 0\-100%
of one’s capital between a risk\-free and the risky asset over time. The optimal rebalancing periods are mostly of
duration around a month; thus, the model does not overtrade, ensuring reasonable trading costs. Furthermore,
during crashes, the model reduces the invested amount of capital sufficiently soon to reduce impact of price
drawdowns. In addition to the Dotcom bubble, the great financial crisis of 2008 and other historical crashes, our
study also covers the most recent crash in March 2020 that happened globally as a consequence of the economic
shutdowns that were imposed as a reaction to the spread of the Coronavirus across the world.
Gerstenberger,C.(2021\). “Robustdiscriminationbetweenlong\-rangedependenceandachangeinmean .”In:Journal
of Time Series Analysis 42(1\), pp. 34–62\.
In this article we introduce a robust to outliers Wilcoxon changepoint testing procedure, for distinguishing
between shortrange dependent time series with a change in mean at unknown time and stationary longrange
dependent time series. We establish the asymptotic distribution of the test statistic under the null hypothesis for
L1 near epoch dependent processes and show its consistency under the alternative. The Wilcoxontype testing
procedure similarly as the CUSUMtype testing procedure (of Berkes I., Horvath L., Kokoszka P. and Shao
Q. 2006\. Ann.Statist. 34:1140\-1165\), requires estimation of the location of a possible changepoint, and then
using pre and postbreak subsamples to discriminate between short and longrange dependence. A simulation
study examines the empirical size and power of the Wilcoxontype testing procedure in standard cases and with
disturbances by outliers. It shows that in standard cases the Wilcoxontype testing procedure behaves equally
well as the CUSUMtype testing procedure but outperforms it in presence of outliers. We also apply both testing
procedure to hydrologic data.
Gkatzilakis, G.\-X. and Sivasubramanian, S. (2014\). “Active Allocation of Smart Beta Indices based on Factor
Timing and Regime Switching .” MA thesis. EDHEC Risk Institute.
There has been significant evidence on the forecasting ability of Regime switching regression models. Smart
beta or alternative beta indices are gaining wide popularity among investment community. Smart beta indices
constructed based on fundamental weighing are proven to outperform cap\-weighted portfolios in the long run.
At the same time, smart beta indices have significant exposure to risk factors such as size, value, momentum
and volatility. The risk factors exhibit different behaviour in different regimes. In this research we examine and
present evidence of the presence of regimes in smart beta indices. We also examine the possibility of adding
value to a portfolio by switching between regime dependent portfolios of smart beta indices exploiting factor
exposures.
36Glasserman, P., Mamaysky, H., and Shen, Y. (2021\). “Dynamic information regimes in financial markets .” In:SSRN
e\-Print.
We develop a model of investor information choices and asset prices where the availability of information about
fundamentals is time\-varying. A competitive research sector produces more information when more investors
are willing to pay for that research. This feedback, from investor willingness to pay for information to more
information production, generates two regimes in equilibrium, one having high prices and low volatility, the other
the opposite. The low\-price, high\-volatility regime is associated with greater information asymmetry between
informed and uninformed investors. Information dynamics move the market between regimes, creating large
price drops even with no change in fundamentals. In our calibration, the model suggests an important role for
information dynamics in financial crises.
Glocker, C. and Wegmueller, P. (2020\). “Business cycle dating and forecasting with real\-time Swiss GDP data .” In:
Empirical Economics 58(1\), pp. 73–105\.
We develop a small\-scale dynamic factor model for the Swiss economy allowing for nonlinearities by means of
a two\-state Markov chain. The selection of an appropriate set of indicators utilizes a combinatorial algorithm.
The model’s forecasting performance is as good as that of peers with richer dynamics. It proves particularly
useful for a timely assessment of the business cycle stance, as the recessionary regime probabilities tend to have
a leading property. The model successfully anticipated the downturn of the 2008\-2009 recession and promptly
indicated a fall in GDP growth following the discontinuation of the exchange rate floor of the Swiss Franc.
Gobel, M. and Araujo, T. (2020\). “Indicators of economic crises: a data\-driven clustering approach .” In:Applied
Network Science 5(1\) (44\).
The determination of reliable early\-warning indicators of economic crises is a hot topic in economic sciences.
Pinning down recurring patterns or combinations of macroeconomic indicators is indispensable for adequate
policy adjustments to prevent a looming crisis. We investigate the ability of several macroeconomic variables
tellingcrisiscountriesapartfromnon\-crisiseconomies.Weintroduceaself\-calibratedclustering\-algorithm,which
accounts for both similarity and dissimilarity in macroeconomic fundamentals across countries. Furthermore,
imposing a desired community structure, we allow the data to decide by itself, which combination of indicators
would have most accurately foreseen the exogeneously defined network topology. We quantitatively evaluate the
degree of matching between the data\-generated clustering and the desired community\-structure.
Goswami, B., Boers, N., Rheinwalt, A., Marwan, N., Heitzig, J., Breitenbach, S. F. M., and Kurths, J. (2018\).
“Abrupt transitions in time series with uncertainties .” In:Nature Communications 9(1\) (48\).
Identifying abrupt transitions is a key question in various disciplines. Existing transition detection methods,
however, do not rigorously account for time series uncertainties, often neglecting them altogether or assuming
them to be independent and qualitatively similar. Here, we introduce a novel approach suited to handle uncer\-
tainties by representing the time series as a time\-ordered sequence of probability density functions. We show how
to detect abrupt transitions in such a sequence using the community structure of networks representing prob\-
abilities of recurrence. Using our approach, we detect transitions in global stock indices related to well\-known
periods of politico\-economic volatility. We further uncover transitions in the El Nino\-Southern Oscillation which
coincide with periods of phase locking with the Pacific Decadal Oscillation. Finally, we provide for the first time
an ’uncertainty\-aware’ framework which validates the hypothesis that ice\-rafting events in the North Atlantic
during the Holocene were synchronous with a weakened Asian summer monsoon.
Gu, J. and Mulvey, J. M. (2021\). “Factor Momentum and Regime\-Switching Overlay Strategy .” In:The Journal of
Financial Data Science 3(4\), pp. 101–129\.
Investorsarefacedwithchallengesindiversifyingrisksandprotectingcapitalduringcrashperiods.Inthisarticle,
the authors incorporate regime information in the portfolio optimization context by identifying regimes for
historical time periods using an l1\-trend filtering algorithm and exploring different machine learning techniques
to forecast the probability of an upcoming stock market crash. They then apply a regime\-based asset allocation
to nominal risk parity strategy. Investors can further improve their investment performance by implementing
a dollar\-neutral factor momentum strategy as an overlay in conjunction with the core portfolio. The authors
demonstrate that the time\-series factor momentum strategy generates high risk\-adjusted returns and exhibits
pronounced defensive characteristics during market crashes. A volatility scaling approach is employed to manage
the risk and further magnify the benefits of factor momentum. Empirical results suggest that the approach
improvesrisk\-adjustedreturnsbyasubstantialamountoverthebenchmarkfromboththestandaloneperspective
and the contributory perspective.
37Guérin,P.,Leiva\-Leon,D.,andMarcellino,M.(2020\). “Markov\-SwitchingThree\-PassRegressionFilter .”In:Journal
of Business \& Economic Statistics 38(2\), pp. 285–302\.
We introduce a new approach for the estimation of high\-dimensional factor models with regime\-switching factor
loadings by extending the linear three\-pass regression filter to settings where parameters can vary according to
Markov processes. The new method, denoted as Markov\-switching three\-pass regression filter (MS\-3PRF), is
suitable for datasets with large cross\-sectional dimensions, since estimation and inference are straightforward, as
opposed to existing regime\-switching factor models where computational complexity limits applicability to few
variables. In a Monte Carlo experiment, we study the finite sample properties of the MS\-3PRF and find that
it performs favorably compared with alternative modeling approaches whenever there is structural instability
in factor loadings. For empirical applications, we consider forecasting economic activity and bilateral exchange
rates, finding that the MS\-3PRF approach is competitive in both cases. Supplementary materials for this article
are available online.
Guidolin, M. (2011\). “Markov Switching in Portfolio Choice and Asset Pricing Models: A Survey .” In:Advances in
Econometrics . Emerald Group Publishing, pp. 87–178\.
I survey applications of Markov switching models to the asset pricing and portfolio choice literatures. In par\-
ticular, I discuss the potential that Markov switching models have to fit financial time series and at the same
time provide powerful tools to test hypotheses formulated in the light of financial theories, and to generate
positive economic value, as measured by risk\-adjusted performances, in dynamic asset allocation applications.
The chapter also reviews the role of Markov switching dynamics in modern asset pricing models in which the
no\-arbitrage principle is used to characterize the properties of the fundamental pricing measure in the presence
of regimes.
Guidolin, M., Orlov, A. G., and Pedio, M. (2018\). “How good can heuristic\-based forecasts be? A comparative
performance of econometric and heuristic models for UK and US asset returns .” In:Quantitative Finance 18(1\),
pp. 139–169\.
This paper systematically investigates the sources of differential out\-of\-sample predictive accuracy of heuristic
frameworks based on internet search frequencies and a large set of econometric models. The volume of internet
searches helps gauge the degree of investors’ time\-varying interest in specific assets. We use a wide range of
state\-of\-the\-art models, both of linear and nonlinear type (regime\-switching predictive regressions, threshold
autoregressive, smooth transition autoregressive), extended to capture conditional heteroskedasticity through
GARCH models. The predictor variables investigated are those typical of the literature featuring a range of
macroeconomic and market leading indicators. Our out\-of\-sample forecasting exercises are conducted with ref\-
erence to US, UK, French and German data, both stocks and bonds, and for 1\- and 12\-months\-ahead horizons.
We employ several forecast performance metrics and predictive accuracy tests. Internet\-search\-based models
are found to perform better than the average of all of the alternative models. For several country\-asset\-horizon
combinations, particularly for UK bond returns, our heuristic models compare favourably with sophisticated
econometric methods. The heuristic models are also shown to perform well in forecasting realized volatility.
The baseline results are supported by several extensions and robustness checks, such as using alternative search
keywords, controlling for Fama\-French and Cochrane\-Piazzesi factors, and implementing heuristic\-based trading
strategies.
Guidolin,M.andTimmermann,A.(2008\). “Internationalassetallocationunderregimeswitching,skew,andkurtosis
preferences .” In:The Review of Financial Studies 21(2\), pp. 889–935\.
This paper investigates the international asset allocation effects of time\-variations in higher\-order moments of
stock returns such as skewness and kurtosis. In the context of a four\-moment International Capital Asset Pricing
Model (ICAPM) specification that relates stock returns in five regions to returns on a global market portfolio
and allows for time\-varying prices of covariance, co\-skewness, and co\-kurtosis risk, we find evidence of distinct
bull and bear regimes. Ignoring such regimes, an unhedged US investor’s optimal portfolio is strongly diversified
internationally. The presence of regimes in the return distribution leads to a substantial increase in the investor’s
optimal holdings of US stocks, as does the introduction of skewness and kurtosis preferences.
Haase, F. and Neuenkirch, M. (2021\). “Predictability of Bull and Bear Markets: A New Look at Forecasting Stock
Market Regimes (and Returns) in the U.S. ” In:SSRN e\-Print .
The empirical literature of stock market predictability mainly suffers from model uncertainty and parameter
instability.Tomeetthischallenge,weproposeanovelapproachthatcombinesthedocumentedmeritsofdiffusion
indices, regime\-switching models, and forecast combination to predict the dynamics in the S\&P 500\. First, we
aggregate the weekly information of 115 popular macroeconomic and financial variables through an interaction
38of principal component analysis and shrinkage methods. Second, we estimate one\-step Markov\-switching models
with time\-varying transition probabilities using the diffusion indices as predictors. Third, we pool the forecasts
in clusters to hedge against model risk and to evaluate the usefulness of different specifications. Our results
show that we can adequately predict regime dynamics. Our forecasts provide a statistical improvement over
several benchmarks and generate economic value by boosting returns, improving the certainty equivalent return,
and reducing tail risk. Using the same approach for return forecasts, however, does not lead to a consistent
outperformance of the historical average.
Hallac, D., Nystrup, P., and Boyd, S. (2019\). “Greedy Gaussian segmentation of multivariate time series .” In:
Advances in Data Analysis and Classification 13(3\), pp. 727–751\.
We consider the problem of breaking a multivariate (vector) time series into segments over which the data is well
explained as independent samples from a Gaussian distribution. We formulate this as a covariance\-regularized
maximum likelihood problem, which can be reduced to a combinatorial optimization problem of searching over
the possible breakpoints, or segment boundaries. This problem can be solved using dynamic programming,
with complexity that grows with the square of the time series length. We propose a heuristic method that
approximately solves the problem in linear time with respect to this length, and always yields a locally optimal
choice, in the sense that no change of any one breakpoint improves the objective. Our method, which we call
greedy Gaussian segmentation (GGS), easily scales to problems with vectors of dimension over 1000 and time
series of arbitrary length. We discuss methods that can be used to validate such a model using data, and also
to automatically choose appropriate values of the two hyperparameters in the method. Finally, we illustrate our
GGS approach on financial time series and Wikipedia text data.
Hammerschmid, R. and Lohre, H. (2018\). “Regime Shifts and Stock Return Predictability .” In:International Review
of Economics and Finance 56, pp. 138–160\.
Identifying economic regimes is useful in a world of time\-varying risk premia. We apply regime switching models
to common factors proxying for the macroeconomic regime and show that the ensuing regime factor is relevant in
forecasting the equity risk premium. Moreover, the relevance of this regime factor is preserved in the presence of
fundamental variables and technical indicators which are known to predict equity risk premia. Based on multiple
predictive regressions and pooled forecasts, the macroeconomic regime factor is deemed complementary relative
to the fundamental and technical information sets. Finally, these forecasts exhibit significant out\-of\-sample
predictability that ultimately translates into considerable utility gains in a mean\-variance portfolio strategy.
Hao, H. (2019\). “A Regime\-Aware Agent\-Based Framework for Financial Planning .” PhD thesis. Princeton Univer\-
sity.
The vulnerability of individuals planning for retirement has been growing due to the conversion from defined\-
benefit plans to defined\-contribution plans, the steady increase in life longevity, and the uncertainty of asset
returns under an ever\-changing global environment. A serious problem is the lack of appropriate planning for
retirement. How much should an individual save beyond the Social Security tax in order to maintain a reasonable
lifestyle after retirement? This paper designs a framework to facilitate the process of setting realistic goals for
financial planning, featuring the concept of agent\-based simulations. The framework also provides policy\-rule
guidelines for the agent to search for an optimal strategy. Additionally, a micro\-macro analysis enables us to
analyze a cohort of representative agents and aggregate the individual results on the macro\-level. The simulation
module employs a regime\-based Monte Carlo simulation of multiple asset categories, a factor\-based diversifying
asset allocation approach, and a collection of dynamic policy\-rule\-based investment strategies. Empirical results,
consisting of a downside risk simulation for university endowments, a sustainability assessment for the Social
Security fund, and a personal goal\-based retirement planning, demonstrate stylized applications of the planning
framework.
Harvey, D. I., Leybourne, S. J., Sollis, R., and Taylor, A. M. R. (2021\). “Real\-Time Detection of Regimes of
Predictability in the U.S. Equity Premium .” In:Journal of Applied Econometrics 36, pp. 45–70\.
We propose new real\-time monitoring procedures for the emergence of end\-of\-sample predictive regimes using se\-
quential implementations of standard (heteroskedasticity\-robust) regression t\-statistics for predictability applied
over relatively short time periods. The procedures we develop can also be used for detecting historical regimes
of temporary predictability. Our proposed methods are robust to both the degree of persistence and endogeneity
of the regressors in the predictive regression and to certain forms of heteroskedasticity in the shocks. We discuss
how the monitoring procedures can be designed such that their false positive rate can be set by the practitioner
at the start of the monitoring period using detection rules based on information obtained from the data in a
training period. We use these new monitoring procedures to investigate the presence of regime changes in the
39predictability of the US equity premium at the 1\-month horizon by traditional macroeconomic and financial
variables, and by binary technical analysis indicators. Our results suggest that the 1\-month\-ahead equity pre\-
mium has temporarily been predictable, displaying so\-called ”pockets of predictability,” and that these episodes
of predictability could have been detected in real time by practitioners using our proposed methodology.
Hauptmann, J., Hoppenkamps, A., Min, A., Ramsauer, F., and Zagst, R. (2014\). “Forecasting market turbulence
using regime\-switching models .” In:Financial Markets and Portfolio Management 28(2\), pp. 139–164\.
We propose an early warning system to timely forecast turbulence in the US stock market. In a first step, a
Markov\-switching model with two regimes (a calm market and a turbulent market) is developed. Based on the
time series of the monthly returns of the SandP 500 price index, the corresponding filtered probabilities are
successively estimated. In a second step, the turbulent phase of the model is further specified to distinguish
between bullish and bearish trends. For comparison only, a Markov\-switching model with three states (a calm
market, a turbulent bullish market, and a turbulent bearish market) is examined as well. In a third step,
logistic regression models are employed to forecast the filtered probabilities provided by the Markov\-switching
models. A major advantage of the presented modeling framework is the timely identification of the factors
driving the different phases of the capital market. In a fourth step, the early warning system is applied to an
asset management case study. The results show that explicit consideration of the models’ signals yields better
portfolio performance and lower portfolio risk compared to standard buy\-and\-hold and constant proportion
portfolio insurance strategies.
Heckens, A. J. and Guhr, T. (2022\). “A new attempt to identify long\-term precursors for endogenous financial crises
in the market correlation structures .” In:Journal of Statistical Mechanics: Theory and Experiment 2022(4\),
p. 043401\.
Prediction of events in financial markets is every investor’s dream and, usually, wishful thinking. From a more
general, economic and societal viewpoint, the identification of indicators for large events is highly desirable to
assess systemic risks. Unfortunately, the very nature of financial markets, particularly the predominantly non\-
Markovian character as well as non\-stationarity, make this challenge a formidable one, leaving little hope for
fully fledged answers. Nevertheless, it is called for to collect pieces of evidence in a variety of observables to
be assembled like the pieces of a puzzle that eventually might help to catch a glimpse of long\-term indicators
or precursors for large events\-if at all in a statistical sense. Here, we present a new piece for this puzzle. We
use the quasi\-stationary market states that exist in the time evolution of the correlation structure in financial
markets. Recently, we identified such market states relative to the collective motion of the market as a whole.
We study their precursor properties in the US stock markets over 16 years, including two endogenous crises, the
dot\-com bubble burst and the pre\-phase of the Lehman Brothers crash. We identify certain interesting features
and critically discuss their suitability as indicators.
Hollstein, F., Prokopczuk, M., and Voigts, V. (2022\). “How Robust are Empirical Factor Models to the Choice of
Breakpoints? ” In:SSRN e\-Print .
We comprehensively investigate the robustness of well\-known factor models to altered factor\-formation break\-
points. Deviating from the standard 30th and 70th percentile selection, we use an extensive set of anomaly test
portfolios to uncover two main findings: First, there is a trade\-off between specification versus diversification.
More centered breakpoints tend to result in less (idiosyncratic) risk. More extreme sorts create stronger expo\-
sures to the underlying anomalies and, thus, higher average returns. Second, the models are robust to different
degrees. The Hou, Xue, and Zhang (2015\) model is much more sensitive to changes in breakpoints than the
Fama\-French models.
Horvath, B., Issa, Z., and Muguruza, A. (2021\). “Clustering Market Regimes Using the Wasserstein Distance .” In:
SSRN e\-Print .
he problem of rapid and automated detection of distinct market regimes is a topic of great interest to financial
mathematicians and practitioners alike. In this paper, we outline an unsupervised learning algorithm for clus\-
tering financial time\-series into a suitable number of temporal segments (market regimes). As a special case of
the above, we develop a robust algorithm that automates the process of classifying market regimes. The method
is robust in the sense that it does not depend on modelling assumptions of the underlying time series as our
experiments with real datasets show. This method – dubbed the Wasserstein k\-means algorithm – frames such
a problem as one on the space of probability measures with finite pthmoment, in terms of the p\-Wasserstein
distance between (empirical) distributions. We compare our WK\-means approach with a more traditional clus\-
tering algorithms by studying the so\-called maximum mean discrepancy scores between, and within clusters. In
both cases it is shown that the WK\-means algorithm vastly outperforms all considered competitor approaches.
40We demonstrate the performance of all approaches both in a controlled environment on synthetic data, and on
real data.
Horváth, L., Li, H., and Liu, Z. (2022\). “How to identify the different phases of stock market bubbles statistically? ”
In:Finance Research Letters 46 (Part A) (102366\).
EugeneFamaoncementionedin2016thatpeoplehavenotcomeupwithwaysofidentifyingbubblesstatistically.
This paper presents the nonparametric change\-point method to identify different stages of stock bubbles, and
we derive its asymptotic distribution under the null hypothesis. By simulation, we obtain the corresponding
critical value. In the empirical analysis, we employ this test and binary segmentation method to the 1990s
Nasdaq bubble and get the same result as Phillips et al. (2011\). We also apply this test to the S\&P 500 index,
the Shanghai stock index, the Nikkei 225 index, the FTSE 100 index, and the CAC 40 index respectively, and
successfully identify the bubbles’ different phases in each stock market.
Hu, Y., Shi, X., and Xu, Z. Q. (2022\). “Mean variance asset liability management with regime switching .” In:arXiv
e\-Print.
This paper is concerned with mean variance portfolio selection with liability, regime switching and random
coefficients. To tackle the problem, we first study a general non\-homogeneous stochastic linear quadratic (LQ)
control problem for which two systems of backward stochastic differential equations (BSDEs) with unbounded
coefficients are introduced. The existence and uniqueness of the solutions to these two systems of BSDEs are
proved by some estimates of BMO martingales and contraction mapping method. Then we obtain the optimal
state feedback control and optimal value for the stochastic LQ problem explicitly. Finally, closed form efficient
portfolio and efficient frontier for the original mean variance problem are presented.
Huang, D., Jiang, F., Tu, J., and Zhou, G. (2017\). “Forecasting Stock Returns in Good and Bad Times: The Role
of Market States .” In:SSRN e\-Print .
This paper proposes a two\-state predictive regression model and shows that stock market 12\-month return
(TMR), the time\-series momentum predictor of Moskowitz, Ooi, and Pedersen (2012\), forecasts the aggregate
stock market negatively in good times and positively in bad times. The out\-of\-sample R\-squares are 0\.96% and
1\.72% in good and bad times, or 1\.28% and 1\.41% in NBER economic expansions and recessions, respectively.
The TMR predictability pattern holds in the cross\-section of U.S. stocks and the international markets. Our
study shows that the absence of return predictability in good times, an important finding of recent studies, is
largely driven by the use of the popular one\-state predictive regression model.
Iqbal, J. (2018\). “Application of Regime Switching and Random Matrix Theory for Portfolio Optimization .” PhD
thesis. University of Essex.
Market economies have been characterized by boom and bust cycles. Since the seminal work of Hamilton (1989\),
these large scale fluctuations have been referred to as regime switches. Ang and Bekaert (2002\) were the first
to consider the role of regime switches for stock market returns and portfolio optimisation. The key stylized
facts regarding regime switching for stock index returns is that boom periods with positive mean stock returns
are associated with low volatility, while bear markets with negative mean returns have high volatility. The
correlation of asset returns also show asymmetry with greater correlation being found during stock market
downturns. In view of the large portfolio losses from correlated negative movements in asset returns during the
recent 2007 financial crisis, it has become imperative to incorporate regime sensitivity in portfolio management.
This thesis forms an extensive application of regime sensitive statistics for stock returns in the management of
equity portfolios for different markets. Starting with the application to a small 3 asset portfolio for UK stocks
(in Chapter 4\), the methodology is extended to large scale portfolio for the FTSE\-100\. In chapters 5 and 6,
respectively, using stock index data from the subcontinent (India, Pakistan and Bangladesh) and for the Asia
Pacific, optimal regime sensitive portfolios have been analysed with the MSCI AC Index (for Emerging and
Asia Pacific Markets) being taken as the benchmark index. Portfolio performance has been studied using a
dynamic end of month rebalancing of the portfolio on the basis of regime indicators given by market index
and relevant regime dependent portfolio statistics. The cumulative end of period returns and risk adjusted
Sharpe Ratio from this exercise is compared to the simple Markowitz mean\-variance portfolio and market value
portfolio. The regime switching optimal portfolio strategy has been found to dominate non\-regime sensitive
portfolio strategies in Asia Pacific and 3 asset portfolio for UK stocks cases but not in Subcontinent case
(for the first half of out\-sample period). In the case of the relationship of the sub\-continental indexes vis\-
a\-vis the MSCI benchmark index, the latter has negligible explanatory power for the former especially for
the first half of out\-sample period. Hence, the regime indicators based on MSCI emerging market index have
detrimental effects on portfolio selection based on the sub\-continental indexes. As regime sensitive variance\-
41covariance matrices have implications for the selection of optimal portfolio weights, the final Chapter 7 uses
the FTSE\-100 and its constituent company data to compare and contrast the implications for optimal portfolio
management of filtering the covariance matrix using Random Matrix Theory (RMT). While it is found that
filtering the variance\-covariance matrix using Marchenko\-Pasteur bounds of RMT improves optimal portfolio
choice in both non\-regime and regime dependent cases, remarkably in the latter case for Regime 2 determined
variance\-covariance matrix, the RMT filter was least needed. This result is given in Chapter 7, Table 7\.5\-1\. This
confirms the significance of using Hamilton (1989\) regime sensitive statistics for stock returns in identifying
the ’true’ non\-noisy variance\-covariance relationships. The RMT methodology is also useful for identifying the
centrality, based on eigenvector analysis, of the constituent stocks in their role in driving crisis and non\-crisis
market conditions. A fully automated suite of programs in MATLAB have been developed for regime switching
portfolio optimization with RMT filtering of the variance\-covariance matrix.
Jacob, V., Song, F., Stiegler, A., Diao, Y., andTatbul,N. (2021\). “Exathlon: A Benchmarkfor Explainable Anomaly
Detection over Time Series .” In:arXiv e\-Print .
Access to high\-quality data repositories and benchmarks have been instrumental in advancing the state of the art
in many experimental research domains. While advanced analytics tasks over time series data have been gaining
lots of attention, lack of such community resources severely limits scientific progress. In this paper, we present
Exathlon, the first comprehensive public benchmark for explainable anomaly detection over high\-dimensional
timeseriesdata.Exathlonhasbeensystematicallyconstructedbasedonrealdatatracesfromrepeatedexecutions
of large\-scale stream processing jobs on an Apache Spark cluster. Some of these executions were intentionally
disturbed by introducing instances of six different types of anomalous events (e.g., misbehaving inputs, resource
contention, process failures). For each of the anomaly instances, ground truth labels for the root cause interval
as well as those for the extended effect interval are provided, supporting the development and evaluation of
a wide range of anomaly detection (AD) and explanation discovery (ED) tasks. We demonstrate the practical
utility of Exathlon’s dataset, evaluation methodology, and end\-to\-end data science pipeline design through an
experimental study with three state\-of\-the\-art AD and ED techniques.
Jacquier, A., Bilokon, P., and McIndoe, C. (2021\). “Market regime classification with signatures .” In:SSRN e\-Print .
We provide a data\-driven algorithm to classify market regimes for time series. We utilise the path signature,
encoding time series into easy\-to\-describe objects, and provide a metric structure which establishes a connection
between separation of regimes and clustering of points.
James, N. (2021\). “Evolutionary correlation, regime switching, spectral dynamics and optimal trading strategies for
cryptocurrencies and equities .” In:arXiv e\-Print .
This paper uses new and recently established methodologies to study the evolutionary dynamics of the cryp\-
tocurrency market, and compares the findings with that of the equity market. We begin by applying random
matrix theory and principal components analysis (PCA) to correlation matrices of both collections, highlighting
clear differences in the eigenspectra exhibited. We then explore the heterogeneity of both asset classes, studying
the time\-varying dynamics of underlying sector behaviours, and determine the collective similarity within each
collection. We then turn to a study of structural break dynamics and evolutionary power spectra, where we
quantify the collective affinity in structural breaks and evolutionary behaviours of underlying sector time series.
Finally, we implement two algorithms simulating ‘portfolio choice’ dynamics to compare the effectiveness of
stock selection and sector allocation in cryptocurrency portfolios. There, we highlight the importance of both
endeavours and comment on noteworthy implications for cryptocurrency portfolio management.
Jewell, S., Fearnhead, P., and Witten, D. (2021\). “Testing for a Change in Mean After Changepoint Detection .” In:
arXiv e\-Print .
While many methods are available to detect structural changes in a time series, few procedures are available
to quantify the uncertainty of these estimates post\-detection. In this work, we fill this gap by proposing a new
framework to test the null hypothesis that there is no change in mean around an estimated changepoint. We
further show that it is possible to efficiently carry out this framework in the case of changepoints estimated by
binary segmentation and its variants, \`0segmentation, or the fused lasso. Our setup allows us to condition on
much less information than existing approaches, which yields higher powered tests. We apply our proposals in a
simulation study and on a dataset of chromosomal guanine\-cytosine content. These approaches are freely avail\-
able in the R package ChangepointInference at https://jewellsean.github.io/changepoint\-inference .
Jiang, H., Li, J., and Li, Z. (2020\). “Determining the number of change\-point via high\-dimensional cross\-validation .”
In:Stat9(1\) (e284\).
42Inmultiplechangepointanalysis,oneofthemajorchallengesisthedeterminationofthenumberofchangepoints,
which is usually cast as a model selection problem. However, for model selection methods based on the Schwarz
information criterion (SIC), it is typical that different penalization terms are required for different changepoint
problems and the optimal penalization magnitude usually varies with the model and error distributions. In order
to estimate the number of change points in high dimension, we develop a highdimensional datadriven crossvali\-
dation selection criterion. First, we define a goodnessoffit measure by incorporating the dimensionality into the
quadratic prediction error function. Second, the highdimensional crossvalidation (hCV) procedure is applied
based on an orderpreserved samplesplitting strategy. Simulation studies show that the proposed hCV criterion
has more robust performance compared with a highdimensional SIC criterion tailored for the highdimensional
changepoint problem. The selection property is also established under some mild conditions.
Jiang, P., Liu, Q., and Tse, Y. (2015\). “International Asset Allocation with Regime Switching: Evidence from the
ETFs.” In:Asia\-Pacific Journal of Financial Studies 44(5\), pp. 661–687\.
We develop a dynamic investment strategy with Markov regime switching (MRS) in asset allocation with in\-
ternational iShares exchange\-traded funds (ETFs). Using daily ETF data, we show that a portfolio based on
the dynamic MRS strategy outperforms one based on static mean\-variance strategies after transaction costs.
This dynamic investment strategy not only captures the regime shifts in the highly frequent trading process
but also can be practically used with tradable ETFs. We investigate the reasons for predictive misjudgments
and assess the contribution of each regime’s investment strategy, providing insight into the characteristics of the
MRS model and modifying our views on why the MRS strategy outperforms traditional strategies.
Jochmann, M. and Koop, G. (2015\). “Regime\-switching cointegration .” In:Studies in Nonlinear Dynamics and
Econometrics 19(1\).
We develop methods for Bayesian inference in vector error correction models which are subject to a variety of
switches in regime (e.g., Markov switches in regime or structural breaks). An important aspect of our approach
is that we allow both the cointegrating vectors and the number of cointegrating relationships to change when
the regime changes. We show how Bayesian model averaging or model selection methods can be used to deal
with the high\-dimensional model space that results. Our methods are used in an empirical study of the Fisher
effect.
Kabran, F. B. and Unlu, K. D. (2021\). “A two\-step machine learning approach to predict S\&P 500 bubbles .” In:
Journal of Applied Statistics 48(13\-15\), pp. 2776–2794\.
In this paper, we are interested in predicting the bubbles in the S\&P 500 stock market with a two\-step machine
learning approach that employs a real\-time bubble detection test and support vector machine (SVM). SVM as a
nonparametric binary classification technique is already a widely used method in financial time series forecasting.
In the literature, a bubble is often defined as a situation where the asset price exceeds its fundamental value.
As one of the early warning signals, prediction of bubbles is vital for policymakers and regulators who are
responsible to take preemptive measures against the future crises. Therefore, many attempts have been made
to understand the main factors in bubble formation and to predict them in their earlier phases. Our analysis
consists of two steps. The first step is to identify the bubbles in the S\&P 500 index using a widely recognized
right\-tailed unit root test. Then, SVM is employed to predict the bubbles by macroeconomic indicators. Also, we
compare SVM with different supervised learning algorithms by using k\-fold cross\-validation. The experimental
results show that the proposed approach with high predictive power could be a favourable alternative in bubble
prediction.
Kaihatsu, S. and Nakajima, J. (2015\). Has Trend Inflation Shifted? An Empirical Analysis with a Regime\-Switching
Model. Tech. rep. Bank of Japan.
This paper proposes a new econometric framework for estimating trend inflation and the slope of the Phillips
curve with a regime\-switching model. As a unique aspect of our approach, we assume regimes for the trend
inflation at one\- percent intervals, and estimate the probability of the trend inflation being in each regime. The
trend inflation described in the discrete manner provides for an easily interpretable explanation of estimation
results as well as a robust estimate. An empirical result indicates that Japan’s trend inflation stayed at zero
percent for about 15 years after the late 1990s, and then shifted away from zero percent after the introduction
of the price stability target and the quantitative and qualitative monetary easing. The U.S. result shows a
considerably stable trend inflation at two percent since the late 1990s.
Kamenshchikov, S. (2016\). “Bifurcation patterns of market regime transition .” In:Quantitative Finance 16(11\),
pp. 1631–1636\.
43In this paper mechanisms of reversion \- momentum transition are considered. Two basic nonlinear mechanisms
are highlighted: a slow and fast bifurcation. A slow bifurcation leads to the equilibrium evolution, preceded by
stability loss delay of a control parameter. A single order parameter is introduced by Markovian chain diffusion,
which plays a role of a precursor. A fast bifurcation is formed by a singular fusion of unstable and stable
equilibrium states. The effect of a precatastrophic range compression is observed before the discrete change of
a system. A diffusion time scaling is presented as a precursor of the fast bifurcation. The efficiency of both
precursors in a currency market was illustrated by simulation of a prototype of a trading system.
Kasahara, H. and Shimotsu, K. (2017\). “Testing the Number of Regimes in Markov Regime Switching Models.” In:
Canadian Econometric Study Group (CESG) .
Markov regime switching models have been widely used in numerous empirical applications in economics and
finance. However, the asymptotic distribution of the likelihood ratio test statistic for testing the number of
regimes in Markov regime switching models is an unresolved problem. This paper proposes the likelihood ratio
test of the null hypothesis of M0 regimes against the alternative hypothesis of M0 \+ 1 regimes for any M0 \>\=
1 and derives its asymptotic distribution.
Kasahara, H. and Shimotsu, K. (2019\). “Testing the Order of Multivariate Normal Mixture Models .” In:arXiv
e\-Print.
Finite mixtures of multivariate normal distributions have been widely used in empirical applications in diverse
fieldssuchasstatisticalgeneticsandstatisticalfinance.Testingthenumberofcomponentsinmultivariatenormal
mixture models is a long\-standing challenge even in the most important case of testing homogeneity. This paper
develops likelihood\-based tests of the null hypothesis of M0 components against the alternative hypothesis of M0
\+ 1 components for a general M0 1\. For heteroscedastic normal mixtures, we propose an EM test and derive the
asymptotic distribution of the EM test statistic. For homoscedastic normal mixtures, we derive the asymptotic
distribution of the likelihood ratio test statistic. We also derive the asymptotic distribution of the likelihood
ratio test statistic and EM test statistic under local alternatives and show the validity of parametric bootstrap.
The simulations show that the proposed test has good finite sample size and power properties.
Kashif, M. and Leirvik, T. (2021\). “Regime Switching Stock Returns and Hybrid Tail Risk .” In:SSRN e\-Print .
We investigate the relationship between hybrid tail covariance risk (HTCR) and expected return over the last
four decades. Despite a significant positive HTCR\-expected return relationship in Bali et al. (2014\) , we find that
this relationship is not significant at least during average market conditions. However, if we control for market
regime the relationship starts to appear. We find a strong link between market volatility and the relationship
between HTCR and expected returns. We analyze this relationship during two market regimes, calm and noisy,
depending on the return and return\-volatility. We find that these market regimes pose as a catalyst to HTCR
pricing in the cross\-section of expected returns because HTCR\-expected return relationship exists only during
the calm regime and it ceases to exist during the noisy regime. Firm level cross\-sectional regressions show
significant positive relation (no relation) between HTCR and expected returns during calm (noisy) regime even
after controlling for other relevant priced factors.
Kaya, H. (2017\). “Managing ambiguity in asset allocation .” In:Journal of Asset Management 18(3\), pp. 163–187\.
This paper is about the issue of input parameter uncertainty in portfolio optimization in a discrete setting with
finite states (such as the case in a world with different macroeconomic regimes). In such a setting, being unable
to assign reliable point estimates to the probabilities (or frequencies) of the states creates the ambiguity. We first
describe how this ambiguity can be modeled probabilistically. Then, we show how this added uncertainty can be
dealt with in optimal asset allocation problems. In simple\-yet\-realistic example applications we demonstrate that
without sacrificing much of the upside, ambiguity managed portfolios may enhance the uniformity of returns
across different states when compared to portfolios constructed by traditional methods. We stress that a key
conclusion to be taken from these methods builds the case for insurance\-like and potentially negative\-yielding
investments such as bonds and commodities so as to hedge the unforeseeable macrouncertainties for a smoother
portfolio performance. Finally, we offer a variety of problem domains in which ambiguity management can
be nested including macroeconomic scenario\-based asset allocation, investing with regime\-switching models,
momentum investing, and risk\-based investing.
Kelliher, C., Hazrachoudhury, A., and Irving, B. (2022\). “A Novel Approach to Risk Parity: Diversification across
Risk Factors and Market Regimes .” In:The Journal of Portfolio Management 48(3\).
In this article, the authors describe a robust approach to portfolio diversification that balances risk contributions
across risk factors and market regimes. After identifying four compensated macro risk factors\-growth, inflation,
real rates, and liquidity\-the authors construct a factor portfolio for each based on a broad set of asset classes,
44including proxies for private equity and private real estate. Next, the authors identify five distinct market
regimes characterized by unique asset class behaviors. The factor portfolios are then combined such that the
risk contributions to the resulting total portfolio are as balanced as possible, regardless of which market regime
materializes. By combining regime\-aware correlations with dynamic volatility estimates for each factor and
applying standard 1\.5x to 2x leverage, the authors demonstrate a risk\-parity portfolio with 10% ex ante volatility
andattractiveabsoluteandrisk\-adjustedreturns.Comparedwithatraditional60/40portfolio,theproposedrisk\-
parity portfolio displays greater diversification, more consistent factor\-risk contributions, and greater resilience
to economic shocks.
Khalili, A., Chen, J., and Stephens, D. A. (2016\). “Regularization in Regime\-Switching Gaussian Autoregressive
Models.” In:Advanced Statistical Methods in Data Science . Springer Singapore, pp. 13–34\.
Regime\-switching Gaussian autoregressive models form an effective platform for analyzing financial and eco\-
nomic time series. They explain the heterogeneous behaviour in volatility over time and multi\-modality of the
conditional or marginal distributions. One important task is to infer the number of regimes and regime\-specific
parsimonious autoregressive models. Information\-theoretic criteria such as aic or bic are commonly used for such
inference, and they typically evaluate each regime/autoregressive combination separately in order to choose the
optimalmodelaccordingly.However,thenumberofcombinationscanbesolargethatsuchanapproachiscompu\-
tationallyinfeasible.Inthispaper,wefirstuseacomputationallyefficientregularizationmethodforsimultaneous
autoregressive\-order and parameter estimation when the number of autoregressive regimes is pre\-detertermined.
We then use a regularized Bayesian information criterion (rbic) to select the most suitable number of regimes.
Finite sample performance of the proposed methods are investigated via extensive simulations. We also analyze
the U.S. gross domestic product growth and the unemployment rate data to demonstrate this method.
Kim, E.\-c., Jeong, H.\-w., and Lee, N.\-y. (2019\). “Global Asset Allocation Strategy Using a Hidden Markov Model .”
In:Journal of Risk and Financial Management 12(4\), p. 168\.
This study uses the hidden Markov model (HMM) to identify the phases of individual assets and proposes an
investment strategy using price trends effectively. We conducted empirical analysis for 15 years from January
2004 to December 2018 on universes of global assets divided into 10 classes and the more detailed 22 classes.
Both universes have been shown to have superior performance in strategy using HMM in common. By examining
the change in the weight of the portfolio, the weight change between the asset classes occurs dynamically. This
shows that HMM increases the weight of stocks when stock price rises and increases the weight of bonds when
stock price falls. As a result of analyzing the performance, it was shown that the HMM effectively reflects
the asset selection effect in Jensen’s alpha, Fama’s Net Selectivity and Treynor\-Mazuy model. In addition, the
strategy of the HMM has positive gamma value even in the Treynor\-Mazuy model. Ultimately, HMM is expected
to enable stable management compared to existing momentum strategies by having asset selection effect and
market forecasting ability.
Kim, Y. M. and Kang, K. H. (2022\). “Bayesian Inference of Multivariate Regression Models with Endogenous
Markov Regime\-Switching Parameters .” In:Journal of Financial Econometrics .
This study introduces a multivariate regression model with endogenous Markov regime\-switching parameters,
in which the regression disturbances and regime switches are allowed to be instantaneously correlated. For the
estimation and model comparison, we develop a posterior sampling algorithm for the parameters, regimes, and
marginal likelihood calculation. We demonstrate the reliability of the proposed method using simulation and
empirical studies. The simulation study shows that neglecting the endogeneity leads to inaccurate parameter
estimates, and that our marginal likelihood comparison chooses a correctly specified model. In the business
cycle application, we find that the joint dynamics of the U.S. industrial production index (IPI) growth and
unemployment rates are subject to three\-state endogenous regime shifts. Another application to stock and bond
return data suggests that negative shocks to the stock return seem to cause regime shifts from a low volatility
state to a high volatility state of the financial markets.
Koki, C., Leonardos, S., and Piliouras, G. (2022\). “Exploring the predictability of cryptocurrencies via Bayesian
hidden Markov models .” In:Research in International Business and Finance 59, p. 101554\.
In this paper, we consider a variety of multi\-state hidden Markov models for predicting and explaining the
Bitcoin, Ether and Ripple returns in the presence of state (regime) dynamics. In addition, we examine the
effects of several financial, economic and cryptocurrency specific predictors on the cryptocurrency return series.
Our results indicate that the non\-homogeneous hidden Markov (NHHM) model with four states has the best
one\-step\-ahead forecasting performance among all competing models for all three series. The dominance of
the predictive densities over the single regime random walk model relies on the fact that the states capture
45alternating periods with distinct return characteristics. In particular, the four state NHHM model distinguishes
bull, bear and calm regimes for the Bitcoin series, and periods with different profit and risk magnitudes for the
Ether and Ripple series. Also, conditionally on the hidden states, it identifies predictors with different linear
and non\-linear effects on the cryptocurrency returns. These empirical findings provide important benefits for
portfolio management and policy implementation.
Kole, E. and van Dijk, D. (2016\). “How to Identify and Forecast Bull and Bear Markets? ” In:Journal of Applied
Econometrics 32(1\), pp. 120–139\.
Because the state of the equity market is latent, several methods have been proposed to identify past and current
states of the market and forecast future ones. These methods encompass semi\-parametric rule\-based methods
and parametric Markov switching models. We compare the mean\-variance utilities that result when a risk\-averse
agent uses the predictions of the different methods in an investment decision. Our application of this framework
to the S\&P 500 shows that rule\-based methods are preferable for (in\-sample) identification of the state of the
market, but Markov switching models for (out\-of\-sample) forecasting. In\-sample, only the mean return of the
market index matters, which rule\-based methods exactly capture. Because Markov switching models use both
the mean and the variance to infer the state, they produce superior forecasts and lead to significantly better
out\-of\-sample performance than rule\-based methods. We conclude that the variance is a crucial ingredient for
forecasting the market state.
Komatsu,T.andMakimoto,N.(2015\). “DynamicInvestmentStrategywithFactorModelsUnderRegimeSwitches .”
In:Asia\-Pacific Financial Markets 22(2\), pp. 209–237\.
A model for dynamic investment strategy is developed where assets’ returns are represented by multiple factors.
In a mean variance framework with factor models under regime switches, we derive a semi\-analytic solution for
the optimal portfolio with transaction costs. Due to the existence of transaction costs, the optimal portfolio is
characterized as a linear combination of current and target portfolios, the latter of which maximizes the value
function in the current regime. For some special cases of interest, we also derive simplified analytical solutions.
To see the effect of regime switches, the proposed model is applied to US equity market in which small minus big
and high minus low are employed as factors. Investment strategy based on our model demonstrates empirically
thattheregimeswitchingmodelsexhibitsuperiorperformanceoverthesingleregimemodelforsuchperformance
measures as realized utility and Sharpe ratio which are of particular interest in practice. Taking a close look at
the time series of portfolio returns, the result shows the usefulness of the regime switching model as investors
flexibly optimize asset allocations depending on the state of the market.
Kreuser, J. and Sornette, D. (2019\). “Super\-Exponential RE bubble model with efficient crashes .” In:The European
Journal of Finance 25(4\), pp. 338–368\.
We propose a dynamic Rational Expectations (RE) bubble model of prices, combining a geometric random walk
with separate crash (and rally) discrete jump distributions associated with positive (and negative) bubbles.
Crashes tend to efficiently bring back excess bubble prices close to a ”normal” process. Then, the RE condition
implies that the excess risk premium of the risky asset exposed to crashes is an increasing function of the
amplitude of the expected crash, which itself grows with the bubble mispricing: hence, the larger the bubble
price, the larger its subsequent growth rate. This positive feedback of price on return is the archetype of super\-
exponential price dynamics. We use the RE condition to estimate the real\-time crash probability dynamically
through an accelerating probability function depending on the increasing expected return. After showing how
to estimate the model parameters, we obtain a closed\-form approximation for the optimal investment that
maximizes the expected log of wealth (Kelly criterion) for the risky bubbly asset and a risk\-free asset. We
demonstrate, on seven historical crashes, the promising outperformance of the method compared to a 60/40
portfolio,theclassicKellyallocation,andtheriskyasset,andhowitmitigatesjumps,bothpositiveandnegative.
Kritzman, M., Page, S., and Turkington, D. (2012\). “Regime Shifts: Implications for Dynamic Strategies .” In:
Financial Analysts Journal 68(3\).
Regime shifts present significant challenges for investors because they cause performance to depart significantly
from the ranges implied by long\-term averages of means and covariances. But regime shifts also present op\-
portunities for gain. The authors show how to apply Markov\-switching models to forecast regimes in market
turbulence, inflation, and economic growth. They found that a dynamic process outperformed static asset allo\-
cation in backtests, especially for investors who seek to avoid large losses.
Kunjal, D., Peerbhai, F., and Muzindutsi, P.\-F. (2021\). “The performance of South African exchange traded funds
under changing market conditions .” In:Journal of Asset Management 22(5\), pp. 350–359\.
46Despite the soaring popularity of exchange\-traded funds (ETFs), ETFs may find it difficult to replicate the
returns of their underlying index under changing market conditions. The objective of this study is to examine
theperformanceofSouthAfricanETFsunderbullishandbearishmarketconditions.Thispaperemploysasingle
index Markov Switching model to examine the tracking efficiency of a sample of ETFs tracking the FTSE/JSE
Top 40 (J200\) index from 27 November 2000 until 31 July 2019\. The findings suggest that, on average, ETFs
are more responsive to fluctuations in their underlying index during bullish market conditions and they display
a higher tracking error during bearish market conditions. Thus, our findings support the notion that ETF
performance differs across market regimes, implying that ETF fund managers should disclose their betas across
different market conditions so that ETF investors and traders can adequately evaluate their risk exposures in
each market condition.
Lattanzi, C. and Leonelli, M. (2019\). “A changepoint approach for the identification of financial extreme regimes .”
In:arXiv e\-Print .
Inference over tails is usually performed by fitting an appropriate limiting distribution over observations that
exceed a fixed threshold. However, the choice of such threshold is critical and can affect the inferential results.
Extreme value mixture models have been defined to estimate the threshold using the full dataset and to give
accurate tail estimates. Such models assume that the tail behavior is constant for all observations. However,
the extreme behavior of financial returns often changes considerably in time and such changes occur by sudden
shocks of the market. Here we extend the extreme value mixture model class to formally take into account
distributional extreme changepoints, by allowing for the presence of regime\-dependent parameters modelling
the tail of the distribution. This extension formally uses the full dataset to both estimate the thresholds and
the extreme changepoint locations, giving uncertainty measures for both quantities. Estimation of functions of
interest in extreme value analyses is performed via MCMC algorithms. Our approach is evaluated through a
seriesofsimulations,appliedtorealdatasetsandassessedagainstcompetingapproaches.Evidencedemonstrates
that the inclusion of different extreme regimes outperforms both static and dynamic competing approaches in
financial applications.
Lee, M.\-C., Lin, J.\-C., and Gran, E. G. (2020a). “ReRe: A Lightweight Real\-time Ready\-to\-Go Anomaly Detection
Approach for Time Series .” In:arXiv e\-Print .
Anomaly detection is an active research topic in many different fields such as intrusion detection, network mon\-
itoring, system health monitoring, IoT healthcare, etc. However, many existing anomaly detection approaches
require either human intervention or domain knowledge, and may suffer from high computation complexity,
consequently hindering their applicability in real\-world scenarios. Therefore, a lightweight and ready\-to\-go ap\-
proach that is able to detect anomalies in real\-time is highly sought\-after. Such an approach could be easily
and immediately applied to perform time series anomaly detection on any commodity machine. The approach
could provide timely anomaly alerts and by that enable appropriate countermeasures to be undertaken as early
as possible. With these goals in mind, this paper introduces ReRe, which is a Real\-time Ready\-to\-go proac\-
tive Anomaly Detection algorithm for streaming time series. ReRe employs two lightweight Long Short\-Term
Memory (LSTM) models to predict and jointly determine whether or not an upcoming data point is anoma\-
lous based on short\-term historical data points and two long\-term self\-adaptive thresholds. Experiments based
on real\-world time\-series datasets demonstrate the good performance of ReRe in real\-time anomaly detection
without requiring human intervention or domain knowledge.
Lee, S., Liao, Y., Seo, M. H., and Shin, Y. (2020b). “Factor\-Driven Two\-Regime Regression .” In:arXiv e\-Print .
We propose a novel two\-regime regression model where regime switching is driven by a vector of possibly
unobservable factors. When the factors are latent, we estimate them by the principal component analysis of
a panel data set. We show that the optimization problem can be reformulated as mixed integer optimization,
and we present two alternative computational algorithms. We derive the asymptotic distribution of the resulting
estimatorundertheschemethatthethresholdeffectshrinkstozero.Inparticular,weestablishaphasetransition
that describes the effect of first\-stage factor estimation as the cross\-sectional dimension of panel data increases
relative to the time\-series dimension. Moreover, we develop bootstrap inference and illustrate our methods via
numerical studies.
Lee, S., Liao, Y., Seo, M. H., and Shin, Y. (2021\). “Factor\-driven two\-regime regression .” In:Annals of Statistics
49(3\).
We propose a novel two\-regime regression model where regime switching is driven by a vector of possibly
unobservable factors. When the factors are latent, we estimate them by the principal component analysis of
a panel data set. We show that the optimization problem can be reformulated as mixed integer optimization,
47and we present two alternative computational algorithms. We derive the asymptotic distribution of the resulting
estimatorundertheschemethatthethresholdeffectshrinkstozero.Inparticular,weestablishaphasetransition
that describes the effect of first\-stage factor estimation as the cross\-sectional dimension of panel data increases
relative to the time\-series dimension. Moreover, we develop bootstrap inference and illustrate our methods via
numerical studies.
Lezmi, E., Malongo, H., Roncalli, T., and Sobotka, R. (2019\). “Portfolio Allocation with Skewness Risk: A Practical
Guide.” In:SSRN e\-Print .
In this article, we show how to take into account skewness risk in portfolio allocation. Until recently, this issue
has been seen as a purely statistical problem, since skewness corresponds to the third statistical moment of a
probability distribution. However, in finance, the concept of skewness is more related to extreme events that
produceportfoliolosses.Moreprecisely,theskewnessmeasurestheoutcomeresultingfrombadtimesandadverse
scenarios in financial markets. Based on this interpretation of the skewness risk, we focus on two approaches
that are closely connected. The first one is based on the Gaussian mixture model with two regimes: a normal
regime and a turbulent regime. The second approach directly incorporates a stress scenario using jump\-diffusion
modeling. This second approach can be seen as a special case of the first approach. However, it has the advantage
of being clearer and more in line with the experience of professionals in financial markets: skewness is due to
negative jumps in asset prices. After presenting the mathematical framework, we analyze an investment portfolio
that mixes risk premia, more specifically risk parity, momentum and carry strategies. We show that traditional
portfolio management based on the volatility risk measure is biased and corresponds to a short\-sighted approach
to bad times. We then propose to replace the volatility risk measure by a skewness risk measure, which is
calculated as an expected shortfall that incorporates a stress scenario. We conclude that constant\-mix portfolios
may be better adapted than actively managed portfolios, when the investment universe is composed of negatively
skewed financial assets.
Li, L. (2021\). “Risk of investing in volatility products: A regime\-switching approach .” In:Investment Analysts
Journal50(1\), pp. 1–16\.
Volatility indexes provide a tool for investors to speculate and trade on market sentiment regarding future
volatility. The risk of trading on volatility indexes can be measured by their second moments, namely, variance
and correlation. This study considers the four representative volatility indexes published by the CBOE: stock
market volatility index (VIX), crude oil volatility index (OVX), foreign exchange rate volatility index (EVZ),
and gold price volatility index (GVZ). To examine their risk, we develop an extended multivariate Markov
switching ARCH (MSARCH) model in which regime\-switching variances, correlations, and variance\-correlation
relations are designed. Our empirical sample consists of the four volatility indexes from June 2008 to April
2020 for 612 weekly observations (Wednesday to Wednesday). For the conditional variances, we find evidence of
regime\-switching processes (switching between low and high volatility regimes) for the individual volatility index
returns, with the exception of the GVZ. The estimated probability of the high volatility regime may be used to
track economic distress and uncertainty shocks. These results provide evidence for volatility\-of\-volatility risk.
For the conditional correlations, we find a regime\-switching relation between variances and correlations. That
is, the highest correlation appears when the paired volatility markets are simultaneously experiencing a state of
high volatility. By contrast, when the paired volatility markets are encountering different volatility states, the
correlation is weaker. These results indicate that the volatility\-of\-volatility risk is a factor affecting the dynamics
of correlations between volatility indexes.
Li,X.andMulvey,J.M.(2021\). “PortfolioOptimizationUnderRegimeSwitchingandTransactionCosts:Combining
Neural Networks and Dynamic Programs .” In:INFORMS Journal on Optimization 3(4\), pp. 398–417\.
Multiperiod financial models provide superior capabilities over single\-period myopic approaches but, in gen\-
eral, suffer from the curse of dimensionality. Prominent features include transaction costs, rebalancing gains,
intermediate cashflows, and short\- versus long\-term trade\-offs. In this paper, we propose and test an algorithm
combining dynamic programming with a recurrent neural network. The dynamic program provides advanced
starts for the neural network. Empirical tests show the benefits of this novel strategy with optimizing a hidden
Markov model in the presence of linear transaction costs. Test problems with 50\-250 time steps and up to 11
risky assets are solved efficiently, relative to stand\-alone dynamic programs or neural networks. The recurrent
neural network addresses transaction costs within difficult multiperiod optimization models in polynomial run
time.
Li, X. and Zakamulin, V. (2020\). “Stock volatility predictability in bull and bear markets .” In:Quantitative Finance
20(7\), pp. 1149–1167\.
48The recent literature on stock return predictability suggests that it varies substantially across economic states,
being strongest during bad economic times. In line with this evidence, we document that stock volatility pre\-
dictability is also state dependent. In particular, in this paper, we use a large data set of high\-frequency data
on individual stocks and a few popular time\-series volatility models to comprehensively examine how volatility
forecastability varies across bull and bear states of the stock market. We find that the volatility forecast horizon
is substantially longer when the market is in a bear state than when it is in a bull state. In addition, over all
but the shortest horizons, the volatility forecast accuracy is higher when the market is in a bear state. This
difference increases as the forecast horizon lengthens. Our study concludes that stock volatility predictability is
strongest during bad economic times, proxied by bear market states.
Liszewski, O. (2016\). “Asset allocation under multiple regimes .” MA thesis. Erasmus University.
In this paper we examine the performance of the Markov Switching model with intra\-regimes changes such as
the bull market correction and bear market rallies. We accommodate this short time rehearsals by imposing
restrictionsonthetransitionprobabilitymatrix.Wecomparethemodelwithclassicmean\-switchinganddynamic
VAR models in an asset allocation problem with different number of regimes, initial states choices and asset
distributions used in the estimation process. In an out\-of\-sample and bootstrap verification we give evidence
that the constrained model outperforms other models in terms of risk\-adjusted returns in the long horizon above
2 years.
Liu, L., Chen, C., and Wang, B. (2022\). “Predicting financial crises with machine learning methods .” In:Journal of
Forecasting .
Countries must establish an effective early warning system to predict financial crises in order to avoid their
catastrophic effects. To this end, we construct early warning systems based on the logistic model and seven
machine learning methods, and we also use the Shapley value decomposition and Shapley regression to explore
the causality of the machine learning methods. By comparing the performance of different early warning models
in out\-of\-sample tests, we find that the machine learning models, especially the random forest, gradient boosting
decision tree, and ensemble models, outperform the logistic model in terms of providing early predictions of
financial crises. In addition, the Shapley value can be used to find more effective predictive indicators and
analyze the causes of risks in different countries to a certain extent, enabling policymakers to supplement the
policy toolbox to deal with such crises. Thus, we suggest that machine learning methods should be considered
when establishing early warning systems to predict financial crises in the future.
Ma, Y., MacLean, L., Xu, K., and Zhao, Y. G. (2011\). “Portfolio optimization model with regime\-switching risk
factors for sector exchange traded funds .” In:Pacific Journal of Optimization 7, pp. 455–470\.
This paper develops a portfolio optimization model with a market neutral strategy under a Markov regime\-
switching framework. The selected investment instruments consist of the nine sector exchange traded funds
(ETFs) that represent the U.S. stock market. The Bayesian information criterion is used to determine the
optimal number of regimes. The investment objective is to dynamically maximize the portfolio alpha (excess
return over the T\-Bill) subject to neutralization of the portfolio sensitivities to the selected risk factors. The
portfolio risk exposures are shown to change with various style and macro factors over time. The maximization
problem in this context can be established as a regime\-dependent linear programming problem. The optimal
portfolio constructed as such is expected to outperform a naive benchmark strategy, which equally weights
the ETFs. We evaluate the in\-sample and out\-of\-sample performance of the regime\-dependent market neutral
strategy against the equally weighted strategy. We find that the former generally outperforms the latter.
Malevergne, Y., Sornette, D., and Wei, R. (2021\). “A model of financial bubbles and drawdowns with non\-local
behavioral self\-referencing .” In:SSRN e\-Print .
We propose a novel class of models in which the crash hazard rate is determined by a function of a non\-local
estimation of mispricing. Rooted in behavioral finance, the non\-local estimation embodies in particular the
characteristic of ”anchoring” on past price levels and the ”probability judgment” about the likelihood of a crash
as a function of the self\-referential mispricing, enabling us to disentangle the risk\-return relationship from its
instantaneous connection. By describing drawdowns and crashes as market regimes with correlated negative
jumps clustering over a finite period of time, our model provides a solution to the problem plaguing most crash
jump models, which are in general rejected in calibrations of real financial time series because they assume that
crashes occur in a single large negative jump, which is counterfactual. The model estimation is implemented on
synthetic time series and real markets, shedding light on the estimation of the ”true” expected return, which is
usually confounded by the entanglement between volatility and jump risks. Estimated from the daily time series
49of three stock indexes, the hidden expected return exhibits a secular increase over time and tends to be larger
than the realized return, suggesting that financial markets have been overall underpriced.
Martirosyan, A. and Simonian, J. (2021\). “Emerging Market Stock Momentum Returns during US Economic
Regimes.” In:The Journal of Portfolio Management 47(7\), pp. 27–45\.
In this article, the authors investigate the momentum exhibited by emerging market (EM) stocks in US macroe\-
conomic regimes. Although EM markets are often viewed and invested in as a basket, they comprise countries
that are distinct in terms of their response to macroeconomic dynamics. The unique behavior of EM countries
can in turn be expected to affect the momentum behavior of EM stocks. To investigate the latter hypothesis, the
authors analyze the momentum of a selection of EM markets during expansionary and contractionary regimes in
the US economy. Because the United States is arguably the anchor economy for the global economic system, it is
reasonable to assume that its dynamics influence investment strategies in EM markets. The goal of the present
article is to examine the nature and extent of that influence. The authors frame their study using Hamilton’s
well\-known regime\-switching model. Momentum returns are measured over different holding periods and are
further adjusted using the CAPM and Fama\-French asset pricing models. The results show that there is a high
degree of variation in the degree to which individual EM momentum profits are generated in different macroeco\-
nomic states. The results may therefore provide some insight into the potential efficacy of using macroeconomic
information to drive investment decisions in the EM space.
Massacci, D. (2014\). “Multivariate Regime Switching Model with Flexible Threshold Variable .” In:SSRN e\-Print .
This paper proposes a novel multivariate regime switching model that allows the threshold variable to be a
linear combination of covariates with unknown coefficients: the model is likely to be more suitable to analyze
time series of data in which regimes dynamics are driven by multiple covariates rather than by just one single
threshold variable. The paper considers least squares estimation of the model and it proposes a test for the
number of regimes based on theoretical results from multivariate statistics. Finite sample results from Monte
Carlo analysis strengthen the methodological contribution of the paper. An application to measuring regime\-
specific cross\-sectional dependence in the U.S. stock market illustrates the usefulness of the proposed model for
applied work.
Massacci, D. (2021\). “Testing for Regime Changes in Portfolios with a Large Number of Assets: A Robust Approach
to Factor Heteroskedasticity .” In:Journal of Financial Econometrics .
We develop a new test for threshold\-type regime changes in the risk exposures in portfolios with a large number
of financial assets whose returns exhibit an approximate factor structure. Unlike existing procedures to detect
discrete shifts in factor models, our test is robust to regime\-specific second moment of the common factors. We
rely on an auxiliary threshold regression: we take a weighted cross\-sectional average of the cross\-sectional units;
we estimate the factors from the original model under the null hypothesis of no regime changes; we construct
a Lagrange multiplier statistic to test for threshold effect in the auxiliary regression. Numerical results show
the good finite sample properties of our procedure. The empirical analysis uncovers the dynamics of portfolio
weights and diversification benefits in factor mimicking portfolios across different regimes.
Massacci, D. and Kapetanios, G. (2021\). “Forecasting in Factor Augmented Regressions under Structural Change .”
In:SSRN e\-Print .
Factor augmented regressions are widely used to produce out\-of\-sample forecasts of macroeconomic and financial
time series. However, these series are subject to occasional breaks. We study the effect of neglected structural
instability on the forecasts produced by factor augmented regressions when the latent factors are estimated by
cross\-sectional averages from a large panel of variables. Our results show that neglecting structural instability
can be very costly in terms of forecasting performance. We derive analytical results to show that both instability
in the factor model and in the forecasting equation have an impact on the produced forecasts. We further
provide numerical results showing that conditioning upon the most recent break tends to produce more accurate
forecasts than unconditional estimation methods based on expanding or rolling windows, although the actual
gain depends on the location and the magnitude of the breaks.
McGee, R. (2021\). “Can Market Regimes Really be Timed with Historical Volatility? ” In:SSRN e\-Print .
Recent research findings suggest long\-term investor utility benefits through scaling expected returns by recent
realized volatility. We test for utility gains to volatility timing using a utility regime\-based methodology to
classify investor\-specific market investment regimes based solely on recent realized volatility levels. Under this
framework we find limited informational content in using recent realized volatility to forecast utility regimes for
the market index. To reconcile our findings we replicate work by Moreira and Muir (2017\) and find that their
reported Sharpe ratio gains through volatility\-managing the US market factor do not appear to be statistically
50significant. We find that their scheme under\-performs buy and hold in terms of Sharpe ratio over 30 of the 70
twenty year sub\-periods in our sample (58 out of 70 for an un\-leveraged investor). Furthermore, the historical
out\-performance of volatility management for the market index is highly sensitive to the timing of re\-balancing
within a month, suggesting that the strategy may not be robust to the precise timing of key market events
relative to volatility changes. Strategy adopters should be aware that this timing is not guaranteed to line up
favorably over future investment periods.
McIndoe, C. (2020\). “A Data Driven Approach to Market Regime Classification .” MA thesis. Imperial College.
We provide a novel algorithm which attempts to classify market regimes in US equities time series. As far as
possible, manual intervention is avoided, preferring a data\-driven approach. The path signature is utilised as
a central tool; the application of which is justified. We discuss the connection between market regimes and
distributions of path signatures, and provide a metric space structure on the latter which allows for a clustering
to be formulated. The code both to reproduce the results and to develop further the clustering algorithms
presented is provided on GitHub \- mcindoe/regime\-detection.
McQuarrie, E. F. (2021\). “New Lessons from Market History: Sometimes Bonds Win .” In:SSRN e\-Print .
When Jeremy Siegel published his Stocks for the Long Run thesis, little information was available on stocks
before1871orbondsbefore1926\.Buttoday,digitalarchiveshavemadeitpossibletocomputerealtotalreturnon
stock and bond indexes back to 1793\. This paper presents that new market history and compares it to Siegel’s
narrative. The new historical record shows that over multi\-decade periods, sometimes stocks outperformed
bonds, sometimes bonds outperformed stocks, and sometimes they performed about the same. More generally,
the pattern of asset returns in the modern era, as seen in the Ibbotson SBBI and other datasets that begin in
1926, emerges as distinctly different from what came before. Contrary to Siegel, the pattern of asset returns seen
in the 20th century does not generalize to the 19th century. A regime perspective is introduced to make sense
of the augmented historical record. It argues that both common stocks and long bonds are risk assets, capable
of outperforming or underperforming over any human time horizon. \[This July revision adds more international
data.]
Mehta, P. (2020\). “The Mechanism behind the Bursting of Financial Bubbles and Market Crashes .” In:SSRN
e\-Print.
This article proposes to deliver an algorithm to envisage the distribution of the critical points of bubbles, may
it be a financial bubble or an asset bubble. The study comprehensively examines the use of Log periodic Power
law in various articles from renowned authors from the first paper that was published by Didier Sornette in
1996 to the present day. The paper scrutinizes the prerogatives and robustness of the LPPL for large market
falls and the anti\-bubbles that build in a market. The LPPL fit has been attempted to fit into various crashes
in different stock markets that were predicted previously to establish the smooth working of the model.
Meitz, M. and Saikkonen, P. (2021\). “Testing for observation\-dependent regime switching in mixture autoregressive
models.” In:Journal of Econometrics 222(1\), pp. 601–624\.
Testing for regime switching when the regime switching probabilities are specified either as constants (’mixture
models’) or are governed by a finite\-state Markov chain (’Markov switching models’) are long\-standing problems
that have also attracted recent interest. This paper considers testing for regime switching when the regime
switching probabilities are time\-varying and depend on observed data (’observation\-dependent regime switch\-
ing’). Specifically, we consider the likelihood ratio test for observation\-dependent regime switching in mixture
autoregressive models. The testing problem is highly nonstandard, involving unidentified nuisance parameters
under the null, parameters on the boundary, singular information matrices, and higher\-order approximations of
the log\-likelihood. We derive the asymptotic null distribution of the likelihood ratio test statistic in a general
mixture autoregressive setting using high\-level conditions that allow for various forms of dependence of the
regime switching probabilities on past observations, and we illustrate the theory using two particular mixture
autoregressive models. The likelihood ratio test has a nonstandard asymptotic distribution that can easily be
simulated, and Monte Carlo studies show the test to have good finite sample size and power properties.
Messer, M. (2021\). “Bivariate change point detection: joint detection of changes in expectation and variance .” In:
arXiv e\-Print .
A method for change point detection is proposed. We consider a univariate sequence of independent random
variables with piecewise constant expectation and variance, apart from which the distribution may vary peri\-
odically. We aim to detect change points in both expectation and variance. For that, we propose a statistical
test for the null hypothesis of no change points and an algorithm for change point detection. Both are based
on a bivariate moving sum approach that jointly evaluates the mean and the empirical variance. The joint
51consideration helps improve inference as compared to separate univariate approaches. We infer on the strength
and the type of changes with confidence. Nonparametric methodology supports the analysis of diverse data.
Additionally, a multi\-scale approach addresses complex patterns in change points and effects. We demonstrate
the performance through theoretical results and simulation studies. A companion R\-package jcp (available on
CRAN) is discussed.
Min, S., Song, R., and Zhu, W. (2021\). “The 2021 Bitcoin Bubbles and Crashes – Detection and Classification .” In:
SSRN e\-Print .
Inthisstudy,weadoptedtheLog\-PeriodicPowerLawSingularity(LPPLS)modelforreal\-timeidentificationand
monitoring of Bitcoin bubbles and crashes using different time scale data and proposed the modified Lagrange
regularization method to alleviate the impact of potential LPPLS model over\-fitting to better estimate bubble
start time and market regime change. We also aimed to determine the natures of the bubbles and crashes \-
be it endogenous due to its own price evolution or exogenous due to external market and/or policy influences.
We performed a systematic market event analysis and correlated which to Bitcoin bubbles detected. Based on
the daily LPPLS confidence indictor from December 1, 2019 to June 24, 2021, we found that the Bitcoin boom
from November 2020 to mid\-January 2021 is an endogenous bubble, stemming from the self\-reinforcement of
cooperative herding and imitative behaviors of market players, while the price spike from mid\-January 2021
to mid\-April 2021 is likely an exogenous bubble driven by extrinsic events including a series of large\-scale
acquisitions and adoptions by well\-known institutions such as Visa and Tesla. We have also demonstrated the
utilities of multi\-resolution LPPLS analysis in revealing both short\-term changes and long\-term states.
Mizuno, T., Ohnishi, T., and Watanabe, T. (2020\). “Detecting Stock Market Bubbles Based on the Cross\-Sectional
Dispersion of Stock Prices .” In:Proceedings of the 23rd Asia Pacific symposium on intelligent and evolutionary
systems. Ed. by H. Sato, S. Iwanaga, and A. Ishii. Vol. 12\. Springer International Publishing, pp. 194–202\.
A statistical method is proposed for detecting stock market bubbles that occur when speculative funds concen\-
trate on a small set of stocks. The bubble is defined by stock price diverging from the fundamentals. A firm
financial standing is certainly a key fundamental attribute of that firm. The law of one price would dictate that
firms of similar financial standing share similar fundamentals. We investigate the variation in market capitaliza\-
tion normalized by fundamentals that is estimated by Lasso regression of a firm financial standing. The market
capitalization distribution has a substantially heavier upper tail during bubble periods, namely, the market
capitalization gap opens up in a small subset of firms with similar fundamentals. This phenomenon suggests
that speculative funds concentrate in this subset. We demonstrated that this phenomenon could have been used
to detect the dot\-com bubble of 1998\-2000 in different stock exchanges.
Moreno\-Pino, F., Sukei, E., Olmos, P. M., and Artes\-Rodriguez, A. (2022\). “PyHHMM: A Python Library for
Heterogeneous Hidden Markov Models .” In:arXiv e\-Print .
We introduce PyHHMM, an object\-oriented open\-source Python implementation of Heterogeneous\-Hidden
Markov Models (HHMMs). In addition to HMM’s basic core functionalities, such as different initialization
algorithms and classical observations models, i.e., continuous and multinoulli, PyHHMM distinctively empha\-
sizes features not supported in similar available frameworks: a heterogeneous observation model, missing data
inference, different model order selection criterias, and semi\-supervised training. These characteristics result
in a feature\-rich implementation for researchers working with sequential data. PyHHMM relies on the numpy,
scipy, scikit\-learn, and seaborn Python packages, and is distributed under the Apache\-2\.0 License. PyHHMM’s
source code is publicly available on Github https://github.com/fmorenopino/HeterogeneousHMM to facilitate
adoptions and future contributions. A detailed documentation https://pyhhmm.readthedocs.io/en/latest ,
which covers examples of use and models’ theoretical explanation, is available. The package can be installed
through the Python Package Index (PyPI), via ’pip install pyhhmm’.
Muller, S. and Preissler, F. (2021\). “In Good and in Bad Times? The Relation between Anomaly Returns and
Market States .” In:SSRN e\-Print .
We evaluate the relation between the size of 138 return anomalies and market states using a sample of 56
countries from 1981 to 2019\. We find that the vast majority of anomalies (51 of 138 statistically significant at
the 5% level) perform better if the country’s stock market index trades below its 200\-day moving average, our
definition of a bad market state; 10 anomalies perform significantly better in good market states. On average, the
value\-weighted four\-factor alpha amounts to 46\.7 (31\.2\) bps per anomaly\-month in bad (good) times. In relative
terms, abnormal anomaly returns are 49\.8% higher in bad times. Our findings are consistent across regions
and different anomaly classifications. They are robust to alternative market state classifications and additional
52controls for investor sentiment. The evidence suggests that risk or data\-mining cannot entirely explain anomaly
returns.
Mulvey, J. M., Hao, H., and Li, N. (2018\). “Machine learning, economic regimes and portfolio optimisation .” In:
International Journal of Financial Engineering and Risk Management 2(4\), p. 260\.
In portfolio models, the depiction of future outcomes depends upon a representative accounting of economic
conditions. There is much evidence that crash periods display much different patterns than normal markets,
suggesting that forecasting models ought to be based on multiple regimes. We apply two techniques from ma\-
chine learning in our empirical study to improve robustness: 1\) trend\-filtering \- to distinguish regimes possessing
relatively homogeneous patterns; 2\) a shrinkage/cross validation approach within a factor analysis of perfor\-
mance. A scenario\-based portfolio model is proposed and designed to address multiple regimes. The worst\-case
events are well described within the framework, as compared with mean\-variance Markowitz models that treat
equally all historical performance.
Navarro, M., Allen, G. I., and Weylandt, M. (2021\). “Network Clustering for Latent State and Changepoint Detec\-
tion.” In:arXiv e\-Print .
Network models provide a powerful and flexible framework for analyzing a wide range of structured data sources.
In many situations of interest, however, multiple networks can be constructed to capture different aspects of
an underlying phenomenon or to capture changing behavior over time. In such settings, it is often useful to
cluster together related networks in attempt to identify patterns of common structure. In this paper, we propose
a convex approach for the task of network clustering. Our approach uses a convex fusion penalty to induce
a smoothly\-varying tree\-like cluster structure, eliminating the need to select the number of clusters a priori.
We provide an efficient algorithm for convex network clustering and demonstrate its effectiveness on synthetic
examples.
Neto, A. E. D., Gonzalo, J., and Pitarakis, J.\-Y. (2021\). “Uncovering regimes in out of sample forecast errors .” In:
Oxford Bulletin of Economics and Statistics 83(3\), pp. 713–741\.
We introduce a set of test statistics for assessing the presence of regimes in out of sample forecast errors produced
by recursively estimated linear multiple predictive regressions. These predictive regressions can accommodate
multiple predictors that are highly persistent with potentially different degrees of persistence. Our method is
also designed to be robust to the chosen starting window size so as to avert data mining concerns. Our tests are
shown to be consistent and to lead to null distributions that are free of nuisance parameters and hence robust
to the degree of persistence of the predictors.
Nystrup, P. (2014\). “Regime\-Based Asset Allocation: Do Profitable Strategies Exist? ” MA thesis. Technical Uni\-
versity of Denmark.
Regime shifts present a big challenge to traditional strategic asset allocation, demanding a more adaptive ap\-
proach. In the presence of time\-varying investment opportunities, portfolio weights should be adjusted as new
information arrives. Regime\-switching models can match the tendency of financial markets to change their be\-
havior abruptly and the phenomenon that the new behavior often persists for several periods after a change.
They are well suited to capture the stylized behavior of many financial series including skewness, leptokurtosis,
volatility persistence, and time\-varying correlations. This thesis builds on this empirical evidence to develop
a quantitative framework for regime\-based asset allocation. It investigates whether regime\-based investing can
effectively respond to changes in financial regimes at the portfolio level in an effort to provide better long\-term
resultswhen compared to more staticapproaches. Thethesis extends previous workbyconsidering both discrete\-
time and continuous\-time models, models with different numbers of states, different univariate and multivariate
state\-dependent distributions, and different sojourn time distributions. Out\-of\-sample success depends on de\-
veloping a way to model the non\-linear and non\-stationary behavior of asset returns. Dynamic asset allocation
strategies are shown to add value over strategies based on rebalancing to static weights with rebalancing in
itself adding value compared to buy\-and\-hold strategies in an asset universe consisting of a global stock index, a
global government bond index, and a commodity index. The tested strategies based on an adaptively estimated
two\-state Gaussian hidden Markov model outperform a rebalancing strategy out of sample after accounting for
transaction costs, assuming no knowledge of future returns, and with a realistic delay between the identification
of a regime change and the portfolio adjustment.
Nystrup, P., Hansen, B. W., Larsen, H. O., Madsen, H., and Lindstrom, E. (2018a). “Dynamic Allocation or
Diversification: A Regime\-Based Approach to Multiple Assets .” In:The Journal of Portfolio Management 44(2\),
pp. 62–73\.
53This article investigates whether regime\-based asset allocation can effectively respond to changes in financial
regimes at the portfolio level in an effort to provide better long\-term results when compared to a static 60/40
benchmark. The potential benefit from taking large positions in a few assets at a time comes at the cost
of reduced diversification. The authors analyze this trade\-off in a multi\-asset universe with great potential for
static diversification. The regime\-based approach is centered around a regime\-switching model with time\-varying
parameters that can match financial markets’ behavior and a new, more intuitive way of inferring the hidden
market regimes. The empirical results show that regime\-based asset allocation is profitable, even when compared
to a diversified benchmark portfolio. The results are robust because they are based on available market data
with no assumptions about forecasting skills.
Nystrup, P., Hansen, B. W., Madsen, H., and Lindstrom, E. (2015\). “Regime\-Based Versus Static Asset Allocation:
Letting the Data Speak .” In:The Journal of Portfolio Management 42(1\), pp. 103–109\.
Regime shifts present a big challenge to traditional strategic asset allocation. This article investigates whether
regime based asset allocation can effectively respond to changes in financial regimes at the portfolio level, in
an effort to provide better long\-term results than more static approaches can offer. The authors center their
regime\-based approach around a regime\-switching model with time\-varying parameters that can match financial
markets’ tendency to change behavior abruptly and the fact that the new behavior often persists for several
periods after a change. In an asset universe consisting of a global stock index and a global government bond
index, they show that, even without any level of forecasting skill, holding a static portfolio may not be optimal.
Nystrup, P., Lindstrom, E., and Madsen, H. (2020\). “Learning hidden Markov models with persistent states by
penalizing jumps .” In:Expert Systems with Applications 150, p. 113307\.
Hidden Markov models are applied in many expert and intelligent systems to detect an underlying sequence of
persistent states. When the model is misspecified or misestimated, however, it often leads to unrealistically rapid
switching dynamics. To address this issue, we propose a novel estimation approach based on clustering temporal
features while penalizing jumps. We compare the approach to spectral clustering and the standard approach
of maximizing the likelihood function in an extensive simulation study and an application to financial data.
The advantages of the proposed jump estimator include that it learns the hidden state sequence and model
parameters simultaneously and faster while providing control over the transition rate, it is less sensitive to
initialization, it performs better when the number of states increases, and it is robust to misspecified conditional
distributions. The value of estimating the true persistence of the state process is illustrated through a simple
trading strategy where improved estimates result in much lower transaction costs. Robustness is particularly
critical when the model is part of a system used in production. Therefore, our proposed estimator significantly
improves the potential for using hidden Markov models in practical applications.
Nystrup, P., Madsen, H., and Lindstrom, E. (2018b). “Dynamic portfolio optimization across hidden market
regimes.” In:Quantitative Finance 18(1\), pp. 83–95\.
Regime\-based asset allocation has been shown to add value over rebalancing to static weights and, in particular,
reduce potential drawdowns by reacting to changes in market conditions. The predominant approach in previous
studies has been to specify in advance a static decision rule for changing the allocation based on the state of
financial markets or the economy. In this article, model predictive control (MPC) is used to dynamically optimize
a portfolio based on forecasts of the mean and variance of financial returns from a hidden Markov model with
time\-varying parameters. There are computational advantages to using MPC when estimates of future returns
are updated every time a new observation becomes available, since the optimal control actions are reconsidered
anyway. MPC outperforms a static decision rule for changing the allocation and realizes both a higher return
and a significantly lower risk than a buy\-and\-hold investment in various major stock market indices. This is
after accounting for transaction costs, with a one\-day delay in the implementation of allocation changes, and
with zero\-interest cash as the only alternative to the stock indices. Imposing a trading penalty that reduces the
number of trades is found to increase the robustness of the approach.
Nystrup, P., William Hansen, B., Madsen, H., and Lindstrom, E. (2016\). “Detecting change points in VIX and S\&P
500: A new approach to dynamic asset allocation .” In:Journal of Asset Management 17, pp. 361–374\.
The purpose of dynamic asset allocation (DAA) is to overcome the challenge that changing market conditions
present to traditional strategic asset allocation by adjusting portfolio weights to take advantage of favorable
conditions and reduce potential drawdowns. This article proposes a new approach to DAA that is based on
detection of change points without fitting a model with a fixed number of regimes to the data, without estimating
any parameters and without assuming a specific distribution of the data. It is examined whether DAA is most
profitable when based on changes in the Chicago Board Options Exchange Volatility Index or change points
54detected in daily returns of the S\&P 500 index. In an asset universe consisting of the S\&P 500 index and cash,
it is shown that a dynamic strategy based on detected change points significantly improves the Sharpe ratio and
reduces the drawdown risk when compared with a static, fixed\-weight benchmark.
O’Cinneid, R. (2019\). “Applications of machine learning in finance: analysis of international portfolio flows using
regime\-switching models .” PhD thesis. University College Cork.
Recent advances in machine learning are finding commercial applications across many sectors, not least the
financial industry. This thesis explores applications of machine learning in quantitative finance through two
approaches. The current state of the art is evaluated through an extensive review of recent quantitative finance
literature. Themes and technologies are identified and classified, and the key use cases highlighted from the
emerging literature. Machine learning is found to enable deeper analysis of financial data and the modelling
of complex nonlinear relationships within data. The ability to incorporate alternative data in the investment
process is also enabled. Innovations in backtesting and performance metrics are also made possible through
the application of machine learning. Demonstrating a practical application of machine learning in quantitative
finance, regime\-switching models are applied to analyse and extract information from international portfolio
flows. Regime\-switching models capture properties of international portfolio flows previously found in the litera\-
ture, such as persistence in flows compared to returns, and a relationship between flows and returns. Structural
breaks and persistent regime shifts in investor behaviour are identified by the models. Regime\-switching models
infer regimes in the data which exhibit unique characteristic flows and returns. To determine whether the infor\-
mation extracted could aid in the investment process, a portfolio of global assets was constructed, with positions
determined using a flowbased regime\-switching model. The portfolio outperforms two benchmarks, a buy \& hold
strategy and the MSCI World Index in walk\-forward out\-of\-sample tests using daily and weekly data.
Odendahl, F., Rossi, B., and Sekhposyan, T. (2020\). “Comparing Forecast Performance with State Dependence .”
In:SSRN e\-Print .
We propose a novel forecast comparison methodology to evaluate models’ relative forecasting performance when
the latter is a state\-dependent function of economic variables. In our benchmark case, the relative forecasting
performance, measured by the forecast loss differential, is modeled via a threshold model. Importantly, we allow
the threshold that triggers the switch from one state to the next to be unknown, leading to a non\-standard
test statistic due to the presence of a nuisance parameter. Existing tests either assume a constant out\-of\-sample
forecast performance or use non\-parametric techniques robust to time\-variation; consequently, they may lack
power against state\-dependent predictability. Importantly, our approach is applicable to point forecasts as well
as predictive densities. Monte Carlo results suggest that our proposed test statistics perform well in finite
samples and have better power than existing tests in selecting the best forecasting model in the presence of
state dependence. Our test statistics uncover ”pockets of predictability” in U.S. equity premia forecasts; the
pockets are a state\-dependent function of stock market volatility. Models using economic predictors perform
significantly worse than a simple mean forecast in periods of high volatility, but, in periods of low volatility, the
use of economic predictors may lead to small forecast improvements.
Ohana, J.\-J., Ohana, S., Benhamou, E., Saltiel, D., and Guez, B. (2021\). “Explainable AI Models of Stock Crashes:
A Machine\-Learning Explanation of the Covid March 2020 Equity Meltdown .” In:SSRN e\-Print .
We consider a gradient boosting decision trees (GBDT) approach to predict large S\&P 500 price drops from
a set of 150 technical, fundamental and macroeconomic features. We report an improved accuracy of GBDT
over other machine learning (ML) methods on the S\&P 500 futures prices. We show that retaining fewer and
carefully selected features provides improvements across all ML approaches. Shapley values have recently been
introduced from game theory to the field of ML. They allow for a robust identification of the most important
variables predicting stock market crises, and of a local explanation of the crisis probability at each date, through
a consistent features attribution. We apply this methodology to analyze in detail the March 2020 financial
meltdown, for which the model offered a timely out of sample prediction. This analysis unveils in particular the
contrarian predictive role of the tech equity sector before and after the crash.
Oliveira, A. B. and Valls Pereira, P. L. (2018\). “Asset Allocation With Markovian Regime Switching: Efficient
Frontier and Tangent Portfolio With Regime Switching .” In:SSRN e\-Print .
Asset allocation is important for diversifying risk and realizing gains in the financial market. It involves decisions
taken under uncertainty based on statistical methods. Returns on financial assets generally present regime
switching and there are different distributions of returns in bull and bear markets. Regime switching in the data
generatingprocessforreturnsmakesitnecessarytoreformulatetheassetallocationproblem.Thispaperdevelops
asset allocation models with regime switching. Due to the comparative study of asset allocation, portfolios with
55regime switching enable the space of risk and return to be increased, reduce the risk for each level of return at
the mean variance efficient frontier, and have the best risk\-return relationship over time.
Omerovic, S., Friedl, H., and Grun, B. (2021\). “Modelling Multiple Regimes in Economic Growth by Mixtures of
Generalised Nonlinear Models .” In:Econometrics and Statistics .
The new model class of mixtures of generalised nonlinear models (GNMs) is introduced. The model is spec\-
ified, identifiability issues discussed, the fitting in a maximum likelihood framework using the expectation\-
maximisation (EM) algorithm outlined and an appropriate computational implementation introduced. The new
model class is applied to capture cross\-country heterogeneity when considering the augmented Solow model in\-
cluding human capital accumulation as underlying model structure. The inherent heterogeneity is attributed to
multiple regimes being present within the selected country data set. The results highlight that country\-specific
differences lead to distinct components. Countries belonging to the same component exhibit convergence to a
homogeneous steady state. The components differ in the initial technological endowment and the contribution
of the economic variables to economic growth.
Oprisor, R. and Kwon, R. (2021\). “Multi\-Period Portfolio Optimization with Investor Views under Regime Switch\-
ing.” In:Journal of Risk and Financial Management 14(1\), p. 3\.
We propose a novel multi\-period trading model that allows portfolio managers to perform optimal portfolio
allocation while incorporating their interpretable investment views. This model’s significant advantage is its
intuitive and reactive design that incorporates the latest asset return regimes to quantitatively solve managers’
question: how certain should one be that a given investment view is occurring? First, we describe a framework for
multi\-period portfolio allocation formulated as a convex optimization problem that trades off expected return,
risk and transaction costs. Using a framework borrowed from model predictive control introduced by Boyd et
al., we employ optimization to plan a sequence of trades using forecasts of future quantities, only the first
set being executed. Multi\-period trading lends itself to dynamic readjustment of the portfolio when gaining
new information. Second, we use the Black\-Litterman model to combine investment views specified in a simple
linear combination based format with the market portfolio. A data\-driven method to adjust the confidence in
the manager’s views by comparing them to dynamically updated regime\-switching forecasts is proposed. Our
contribution is to incorporate both multi\-period trading and interpretable investment views into one framework
and offer a novel method of using regime\-switching to determine each view’s confidence. This method replaces
portfoliomanagers’ need to provideestimated confidence levelsfor their views, substituting themwith a dynamic
quantitative approach. The framework is reactive, tractable and tested on 15 years of daily historical data. In a
numerical example, this method’s benefits are found to deliver higher excess returns for the same degree of risk
in both the case when an investment view proves to be correct, but, more notably, also the case when a view
proves to be incorrect. To facilitate ease of use and future research, we also developed an open\-source software
library that replicates our results.
Ou, L., Hunter, M. D., and Chow, S.\-M. (2019\). “Whats for dynr: A Package for Linear and Nonlinear Dynamic
Modeling in R .” In:The R Journal .
Intensive longitudinal data in the behavioral sciences are often noisy, multivariate in nature, and may involve
multiple units undergoing regime switches by showing discontinuities interspersed with continuous dynamics.
Despite increasing interest in using linear and nonlinear differential/difference equation models with regime
switches, there has been a scarcity of software packages that are fast and freely accessible. We have created an R
package called dynr that can handle a broad class of linear and nonlinear discreteand continuous\-time models,
with regime\-switching properties and linear Gaussian measurement functions, in C, while maintaining simple
and easy\-to learn model specification functions in R. We present the mathematical and computational bases
used by the dynr R package, and present two illustrative examples to demonstrate the unique features of dynr.
Pang, Z., Hu, Z., Tokmakov, P., Wang, Y.\-X., and Hebert, M. (2021\). “Unlocking the Full Potential of Small Data
with Diverse Supervision .” In:arXiv e\-Print .
Virtually all of deep learning literature relies on the assumption of large amounts of available training data.
Indeed, even the majority of few\-shot learning methods rely on a large set of ”base classes” for pretraining.
This assumption, however, does not always hold. For some tasks, annotating a large number of classes can be
infeasible, and even collecting the images themselves can be a challenge in some scenarios. In this paper, we
study this problem and call it ”Small Data” setting, in contrast to ”Big Data”. To unlock the full potential of
small data, we propose to augment the models with annotations for other related tasks, thus increasing their
generalizationabilities.Inparticular,weusetherichlyannotatedsceneparsingdatasetADE20Ktoconstructour
realistic Long\-tail Recognition with Diverse Supervision (LRDS) benchmark by splitting the object categories
56into head and tail based on their distribution. Following the standard few\-shot learning protocol, we use the
head classes for representation learning and the tail classes for evaluation. Moreover, we further subsample the
head categories and images to generate two novel settings which we call ”Scarce\-Class” and ”Scarce\-Image”,
respectively corresponding to the shortage of samples for rare classes and training images. Finally, we analyze
the effect of applying various additional supervision sources under the proposed settings. Our experiments
demonstrate that densely labeling a small set of images can indeed largely remedy the small data constraints.
Papenbrock, J. and Schwendner, P. (2015\). “Handling risk\-on/risk\-off dynamics with correlation regimes and cor\-
relation networks .” In:Financial Markets and Portfolio Management 29(2\), pp. 125–147\.
In this paper, we present a framework for detecting distinct correlation regimes and analyzing the emerging
state dependences for a multi\-asset futures portfolio from 1998 to 2013\. These correlation regimes have been
significantly different since the financial crisis of 2008 than they were previously; cluster tracking shows that
asset classes are now less separated. We identify distinct risk\-on and risk\-off assets with the help of correlation
networks. In addition to visualizing, we quantify these observations using suitable metrics for the clusters and
correlation networks. The framework will be useful for financial risk management, portfolio construction, and
asset allocation.
Perikos, I., Kardakis, S., and Hatzilygeroudis, I. (2021\). “Sentiment analysis using novel and interpretable architec\-
tures of Hidden Markov Models .” In:Knowledge\-Based Systems 229, p. 107332\.
Sentiment analysis aims to formulate automated methods to recognize sentiments, opinions and emotions in
text. Many methods and approaches have been utilized but most of them do not disclose the way that decisions
are made and operate as black boxes. Hidden Markov Models (HMMs) constitute a quite suitable and potent
approach for sentiment analysis, since they can utilize the sequential nature of the text, a piece of information
that machine learning methods cannot properly utilize. However, little attention has been paid to formulating
and applying sophisticated HMM\-based methods and advanced training approaches for accomplishing sentiment
analysistasks.Inthisarticle,weintroducenovel,interpretableHMM\-basedmethodsforrecognizingsentimentsin
text and we examine their performance under variousarchitectures, training methods, orders and ensembles. The
introduced models possess interpretability, they can indicate the sentimental parts of a sentence and illustrate
the way that the overall sentiment evolves from the start to the end of it. A concrete experimental study is
conducted and the results show that the introduced HMMs methods and the training approaches are quite
competitive with machine learning methods and that they outperform traditional HMMs. Furthermore, the
designed HMMs methods possess great interpretability and can be an efficient approach for sentiment analysis.
Peters, E. (2015\). “Stable vs. Unstable Markets: A Tale of Two States .” In:SSRN e\-Print .
One of the bedrocks of modern capital market theory is that market risk and related statistics are stable over the
long run. Nobel prizes have been won for this insight, and it is taught in the best business schools. Regulations
have also been written based upon this assumption. Yet, experience does not support this idea. We know that
often markets have periods of relative stability, but they can also be followed by years where it seems that
all is chaos (and not in the physics sense of the word). In academia, there are theories that compete with the
Capital Asset Pricing Model (CAPM), the main proponent of stable markets, but these competing theories are
generally considered impractical since they don’t lend themselves to easy solutions. The answers we often receive
from the usable models, however, go horribly wrong when markets go south. Could it be that we’re using those
models simply because the light is better here? But how can we use the models that are impractical? In this
paper, we show convincing evidence that there are actually two separate market states, each corresponding to
these competing models. In essence, the CAPM and its critics are both right, but only part of the time. The
implications from this for asset allocation and plan management are profound. There will be periods where
using standard techniques for asset allocation or investment management will work well. When the environment
changes, however, those processes may no longer work with reliability. This is particularly true of diversifi cation
because assets that diversify one another in one state fail in the other state when they are truly needed. The
rules change, and if investors hope to adapt successfully, they will need to know the new rules when the change
occurs. This paper offers an explanation for that problem \- two different market states causing assets to behave
very differently. A subsequent paper will provide a roadmap to help asset owners anticipate and navigate deftly
through the changes in market states.
Pharasi, H. K., Seligman, E., Sadhukhan, S., and Seligman, T. H. (2020a). “Dynamics of market states and risk
assessment .” In:arXiv e\-Print .
Based on previous developments of the concept of market states using correlation matrices, in the present paper
we address the dynamical evolution of correlation matrices in time. This will imply minor modifications to
57the market states themselves, due to increased attention to the transition matrix between the states. We will
introduce trajectories of the correlation matrices by considering one day shifts for the epoch used to calculate
the correlation matrices and will visualize both the states and the trajectories after dimensional scaling. This
approach using dynamics improves the options of risk assessment and opens the door to dynamical treatments
of markets and shows noise suppression in a new light.
Pharasi, H. K., Seligman, E., and Seligman, T. H. (2020b). “Market states: A new understanding .” In:arXiv e\-Print .
We present the clustering analysis of the financial markets of S\&P 500 (USA) and Nikkei 225 (JPN) markets
over a period of 2006\-2019 as an example of a complex system. We investigate the statistical properties of
correlation matrices constructed from the sliding epochs. The correlation matrices can be classified into different
clusters, named as market states based on the similarity of correlation structures. Wecluster the S\&P 500 market
into four and Nikkei 225 into six market states by optimizing the value of intracluster distances. The market
shows transitions between these market states and the statistical properties of the transitions to critical market
states can indicate likely precursors to the catastrophic events. We also analyze the same clustering technique
on surrogate data constructed from average correlations of market states and the fluctuations arise due to the
white noise of short time series. We use the correlated Wishart orthogonal ensemble for the construction of
surrogate data whose average correlation equals the average of the real data.
Pinto, J. M. and Castle, J. (2021\). A machine learning dynamic switching approach to forecasting when there are
structural breaks . Tech. rep. University of Oxford.
Forecasting economic indicators is an important task for analysts. However, many indicators suffer from struc\-
tural breaks leading to forecast failure. Methods that are robust following a structural break have been proposed
in the literature but they come at a cost: an increase in forecast error variance. We propose a method to select
between a set of robust and non\-robust forecasting models. Our method uses time\-series clustering to identify
possible structural breaks in a time series, and then switches between forecasting models depending on the
series dynamics. We perform a rigorous empirical evaluation with 400 simulated series with an artificial struc\-
tural break and with real data economic series: Industrial Production and Consumer Prices for all Western
European countries available from the OECD database. Our results show that the proposed method statistically
outperforms benchmarks in forecast accuracy for most case scenarios, particularly at short horizons.
Platanakis, E., Sakkas, A., and Sutcliffe, C. (2017\). “Portfolios in a Regime Shifting Non\-Normal World: Are
Alternative Assets Beneficial? ” In:European Financial Management Association Annual Meeting Athens .
Adding five alternative assets to equity and bond portfolios is harmful for US investors. We use nineteen portfolio
modelsinconjunctionwithdummyvariableregression,andmeasureout\-of\-sampleperformancebybothcertainly
equivalent ratios and Sharpe ratios. The presence of harmful diversification is robust to different estimation
periods and levels of risk aversion, and to the use of two regimes. Harmful diversification is not primarily due
to transactions costs or non\-normal returns, but to estimation risk. Large estimation errors during the credit
crisis (2007\-09\) account for the harmful diversification of three of the five alternative assets over the 1997\-2015
period.
Prakash, A., James, N., Menzies, M., and Francis, G. (2021a). “Structural Clustering of Volatility Regimes for
Dynamic Trading Strategies .” In:Applied Mathematical Finance 28(3\), pp. 236–274\.
We develop a new method to find the number of volatility regimes in a nonstationary financial time series by
applying unsupervised learning to its volatility structure. We use change point detection to partition a time
series into locally stationary segments and then compute a distance matrix between segment distributions.
The segments are clustered into a learned number of discrete volatility regimes via an optimization routine.
Using this framework, we determine the volatility clustering structure for financial indices, large\-cap equities,
exchange\-traded funds and currency pairs. Our method overcomes the rigid assumptions necessary to implement
many parametric regime\-switching models while effectively distilling a time series into several characteristic
behaviours. Our results provide a significant simplification of these time series and a strong descriptive analysis
of prior behaviours of volatility. Finally, we create and validate a dynamic trading strategy that learns the
optimal match between the current distribution of a time series and its past regimes, thereby making online
risk\-avoidance decisions at present.
Prakash,A.,James,N.,Menzies,M.,andFrancis,G.(2021b). “Structuralclusteringofvolatilityregimesfordynamic
trading strategies .” In:arXiv e\-Print .
We develop a new method to find the number of volatility regimes in a nonstationary financial time series by
applying unsupervised learning to its volatility structure. We use change point detection to partition a time
series into locally stationary segments and then compute a distance matrix between segment distributions. The
58segments are clustered into a learned number of discrete volatility regimes via an optimization routine. Using this
framework,wedetermineavolatilityclusteringstructureforfinancialindices,large\-capequities,exchange\-traded
funds and currency pairs. Our method overcomes the rigid assumptions necessary to implement many parametric
regime\-switching models, while effectively distilling a time series into several characteristic behaviours. Our
results provide significant simplification of these time series and a strong descriptive analysis of prior behaviours
of volatility. This empirical analysis could be used with other regime\-switching implementations, justifying the
parametric structure encoded in any candidate model. Finally, we create and validate a dynamic trading strategy
that learns the optimal match between the current distribution of a time series and its past regimes, thereby
making online risk\-avoidance decisions in the present.
Procacci, P. F. and Aste, T. (2019\). “Forecasting market states .” In:Quantitative Finance 19(9\), pp. 1491–1498\.
We propose a novel methodology to define, analyze and forecast market states. In our approach, market states
are identified by a reference sparse precision matrix and a vector of expectation values. In our procedure, each
multivariate observation is associated to a given market state accordingly to a minimization of a penalized
Mahalanobis distance. The procedure is made computationally very efficient and can be used with a large
number of assets. We demonstrate that this procedure is successful at clustering different states of the markets
in an unsupervised manner. In particular, we describe an experiment with one hundred log\-returns and two
states in which the methodology automatically associates states prevalently to pre\- and post\-crisis periods with
one state gathering periods with average positive returns and the other state periods with average negative
returns, therefore discovering spontaneously the common classification of ”bull” and ”bear” markets. In another
experiment, with again one hundred log\-returns and two states, we demonstrate that this procedure can be
efficientlyusedtoforecastoff\-samplefuturemarketstateswithsignificantpredictionaccuracy.Thismethodology
opens the way to a range of applications in risk management and trading strategies in the context where the
correlation structure plays a central role.
Pruser, J. (2021\). “Forecasting US inflation using Markov dimension switching .” In:Journal of Forecasting 40(3\),
pp. 481–499\.
This study considers Bayesian variable selection in the Phillips curve context by using the Bernoulli approach
of Korobilis (Journal of Applied Econometrics, 2013, 28(2\), 204\-230\). The Bernoulli model, however, is unable
to account for model change over time, which is important if the set of relevant predictors changes. To tackle
this problem, this paper extends the Bernoulli model by introducing a novel modeling approach called Markov
dimension switching (MDS). MDS allows the set of predictors to change over time. It turns out that only a small
set of predictors is relevant and that the relevant predictors exhibit a sizable degree of time variation for which
the Bernoulli approach is not able to account, stressing the importance and benefit of the MDS approach. In
addition, this paper provides empirical evidence that allowing for changing predictors over time is crucial for
forecasting inflation.
Rebonato, R. and El Aouadi, A. (2021\). “How Do the Volatilities of Rates Depend on Their Level? The ”Universal
Relationship” Revisited .” In:The Journal of Fixed Income 30(4\), pp. 17–31\.
The authors present a straightforward extension valid in the current negative\-rate regime of the ”universal
relationship” uncovered in De Guillaume, Rebonato, and Pogudin (2013\) between the level of rates and their
volatility. They also provide an explanation of the origin of this relationship by showing the existence of two
sharply distinct regimes for the volatility of real rates as a function of real rate levels, and by linking periods of
high inflation with periods of high real rates. Finally, they provide evidence that the ”volatility of volatility” also
displays a ”universal” behavior, with a significant linear dependence on the level of rates (and of the volatility
itself).
Reher, G. and Wilfling, B. (2015\). “A nesting framework for Markov\-switching GARCH modelling with an appli\-
cation to the German stock market .” In:Quantitative Finance , pp. 1–16\.
Inthispaper,weestablishageneralizedtwo\-regimeMarkov\-switchingGARCHmodelwhichenablesustospecify
complex (symmetric and asymmetric) GARCH equations that may differ considerably in their functional forms
acrossthetwoMarkovregimes.WeshowhowpreviouslyproposedcollapsingproceduresfortheMarkov\-switching
GARCH model can be extended to estimate our general specification by means of classical maximum\-likelihood
methods. We estimate several variants of the generalized Markov\-switching GARCH model using daily excess
returns of the German stock market index DAX sampled during the last decade. Our empirical study has two
major findings. First, our generalized model outperforms all nested specifications in terms of (a) statistical fit
(when model selection is based on likelihood ratio tests) and (b) out\-of\-sample volatility forecasting performance.
59Second,wefindsignificantMarkov\-switchingstructuresinGermanstockmarketdata,withsubstantiallydiffering
volatility equations across the regimes.
Ren, D. (2016\). “Essays in Asset Pricing and Financial Econometrics .” PhD thesis. University of Guelph.
In the first chapter, we compare the finite sample power of short and long\-horizon tests in nonlinear predictive
regression models of regime switching between bull and bear markets, allowing for time varying transition
probabilities. As a point of reference, we also provide a similar comparison in a linear predictive regression
model without regime switching. Overall, our results do not support the contention of higher power in longer
horizon tests in either the linear or nonlinear regime switching models. Nonetheless, it is possible that other
plausible nonlinear models provide stronger justification for long\-horizon tests. Using finite sample simulation
methods, we assess the power of long\-horizon predictive tests and compare them to their short\-run counterparts,
when the true underlying model contains financial asset bubbles. Our results indicate that long\-run predictive
testusingvaluationpredictors–specificallythedividendpriceratio–dopickupthereturnpredictabilityinherent
in the asset bubbles. However, after size\-adjustment, the long\-run predictive framework has a small advantage
over its short\-run counterpart when the predictor is highly persistent and provides a larger, yet still modest
power improvement when the predictor is moderately persistent. The third chapter proposes a simple Bayesian
learning framework to assess leverage ratios in the presence of parameter uncertainty about mean log cash flow.
In particular it can explain why firm’s leverage ratios have been observed to increase with firm age. Market
values are increasing in uncertainty about mean cash flow and leverage ratios are decreasing with market values.
Over the life period of firm, the managers and investors rationally learn from realized cash flows. Due to the
convex relationship between cash flow and firm value, ceteris paribus, this results in a decrease in market value
and an increase in the leverage ratio. Firm level panel data provides empirical evidence consistent with the
model predictions after correcting for the endogeneity of the book to market and profitability control variates.
The empirical results suggest that the firm leverage ratio increases over firm age due to learning.
Reus, L. and Mulvey, J. M. (2016\). “Dynamic allocations for currency futures under switching regimes signals .” In:
European Journal of Operational Research 253(1\), pp. 85–93\.
Exchange carry trade returns can be classified in regimes by a Hidden Markov Model. Regime identification
allows to construct outstanding carry trade strategies. Optimal mean\-semivariance currency portfolio enhances
carry trade strategies. Over the last decades, speculative investors in the FX market have profited in the well
known currency carry trade strategy (CT). However, during currencies or global financial crashes, CT produces
substantial losses. In this work we present a methodology that enhances CT performance significantly. For our
final strategy, constructed backtests show that the mean\-semivolatility ratio can be more than doubled with
respect to benchmark CT. To do the latter, we first identify and classify CT returns according to their behavior
in different regimes, using a Hidden Markov Model (HMM). The model helps to determine when to open and
close positions, depending whether the regime is favorable to CT or not. Finally we employ a mean\-semivariance
allocation model to improve allocations when positions are opened.
Ruff, L., Kauffmann, J. R., Vandermeulen, R. A., Montavon, G., Samek, W., Kloft, M., Dietterich, T. G., and
Muller, K.\-R. (2021\). “A Unifying Review of Deep and Shallow Anomaly Detection .” In:arXiv e\-Print .
Deep learning approaches to anomaly detection have recently improved the state of the art in detection perfor\-
mance on complex datasets such as large collections of images or text. These results have sparked a renewed
interest in the anomaly detection problem and led to the introduction of a great variety of new methods. With
the emergence of numerous such methods, including approaches based on generative models, one\-class classifi\-
cation, and reconstruction, there is a growing need to bring methods of this field into a systematic and unified
perspective. In this review we aim to identify the common underlying principles as well as the assumptions that
are often made implicitly by various methods. In particular, we draw connections between classic ’shallow’ and
novel deep approaches and show how this relation might cross\-fertilize or extend both directions. We further
provide an empirical assessment of major existing methods that is enriched by the use of recent explainability
techniques, and present specific worked\-through examples together with practical advice. Finally, we outline
critical open challenges and identify specific paths for future research in anomaly detection.
Samal, A., Pharasi, H. K., Ramaia, S. J., Kannan, H., Saucan, E., Jost, J., and Chakraborti, A. (2021\). “Network
geometry and market instability .” In:Royal Society Open Science 8(2\).
The complexity of financial markets arise from the strategic interactions among agents trading stocks, which
manifest in the form of vibrant correlation patterns among stock prices. Over the past few decades, complex
financial markets have often been represented as networks whose interacting pairs of nodes are stocks, connected
by edges that signify the correlation strengths. However, we often have interactions that occur in groups of
60three or more nodes, and these cannot be described simply by pairwise interactions but we also need to take the
relations between these interactions into account. Only recently, researchers have started devoting attention to
the higher\-order architecture of complex financial systems, that can significantly enhance our ability to estimate
systemic risk as well as measure the robustness of financial systems in terms of market efficiency. Geometry\-
inspired network measures, such as the Ollivier\-Ricci curvature and Forman\-Ricci curvature, can be used to
capture the network fragility and continuously monitor financial dynamics. Here, we explore the utility of such
discrete Ricci curvatures in characterizing the structure of financial systems, and further, evaluate them as
generic indicators of the market instability. For this purpose, we examine the daily returns from a set of stocks
comprising the USA S\&P\-500 and the Japanese Nikkei\-225 over a 32\-year period, and monitor the changes in
the edge\-centric network curvatures. We find that the different geometric measures capture well the system\-level
features of the market and hence we can distinguish between the normal or ’business\-as\-usual’ periods and all
the major market crashes. This can be very useful in strategic designing of financial systems and regulating the
markets in order to tackle financial instabilities.
Sarwar, G., Mateus, C., and Todorovic, N. (2017\). “A tale of two states: asymmetries in the UK small, value and
momentum premiums .” In:Applied Economics 49(5\), pp. 456–476\.
This article performs comparative analysis of the asymmetries in size, value and momentum premium and their
macroeconomic determinants over the UK economic cycles, using Markov switching approach. We associate
Markov switching regime 1 with economic upturn and regime 2 with economic downturn. We find clear evidence
of cyclical variations in the three premiums, most notable being that in the size premium, which changes from
positive in expansions to negative in recessions. Macroeconomic indicators prompting such cyclicality the most
are variables that proxy credit market conditions, namely the interest rates, term structure and credit spread.
Overall, macro factors tend to have more significant impact on the three premiums during economic downturns.
The results are robust to the choice of information variable used in modelling transition probabilities of the two\-
stage Markov switching model. We show that exploiting cyclicality in premiums proves particularly profitable
for portfolios featuring small cap stocks in recessions at a feasible level of transaction costs.
Satchell, S. (2011\). “Regime\-switching in financial markets .” In:Journal of Asset Management 12(5\), p. 309\.
This issue looks at a number of studies of regime\-switching in financial markets; a hardy perennial of a research
topic, much loved by academics and central bankers, but rather underused by practitioners. The reasons for this
unpopularity are many. These reasons are not based on ignorance but on very real difficulties in implementation.
Furthermore, the structure of these models sits uncomfortably with the assumptions made by conventional
optimisers. Converting these regime structures into global stock selection models with universes of, say, 5000
stocks seems not to be currently feasible. The first paper, by Bulla and co\-authors, looks at a Markov\-switching
asset allocation model, which uses current information on volatility to adjust the market exposure. They show
that, compared with buy\-and\-hold, there are increased returns and reduced volatility. The second paper, by
Guidolin and Ria, converts regime\-switching in first and second moments into regime\-switching in mean variance
frontiers. The data used here are Morgan Stanley investable indices for five countries/regions. The third article,
by Haque, provides a theoretical contribution, in that it generalises the famous Barberis and Shleifer model
of style switching. It is known that this model leads to small order ARMA models in relative style returns
and current research looks at this structure as a way of forecasting when the switch may occur. This paper,
by focusing on leaders and followers, may help in forecasting style switching and lead to new implementations
of dynamic style allocation. The final paper, by van Vliet and Blitz, looks at asset allocation across different
phases in the business cycle and identifies four phases, expressible in terms of time variation and risk and returns.
Concluding this issue provides a thorough examination of current research ideas on regime\-switching. A point
that comes through three of the papers very clearly is that, if we can implement regime\-switching successfully, it
is going to be with respect to asset classes or a small number of factors. For those of our readers who may wish to
apply these ideas to stock selection models, it is clear that the only way forward is to regime\-switch some of the
key factors in the model. If a typical model has as factors market indices, style variables and possibly statistical
factors, then it is not clear as yet which of these should be the most important ones for regime\-switching. This
may be a good topic for future research.
Schatz, M. (2020\). “Financial Modeling of Bubbles and Crashes .” PhD thesis. ETH Zurich.
The aim of this thesis is to develop and study mathematical models of financial markets experiencing bubbles
and crashes. Our study is based on a model structure that combines increasingly positive returns (the build\-up
of a bubble) with a sudden reversal and an accumulation of large negative returns (the crash). The occurrence
of financial crashes, fueled by bubbles, are widely recognized as disruptive events that have significant adverse
61effects on the performance of mathematical tools in many financial problem settings. However, models that
explicitly incorporate the stylized features of bubble\-and\-crash dynamics are yet to permeate most areas of
(mathematical) finance.
To address this shortcoming, in the first part of the thesis we develop a general stochastic model framework
based on the dialectic view that build\-up and implosion of financial bubbles are inherently linked. We show that
the framework encompasses a wide range of models from the bubble literature in (financial) economics that focus
on market failure as a driver of financial distress. As such, it functions both as a tool to compare the various
assumptions underlying such models and as a good starting point to robustify financial problem settings that
are affected by bubbles and crashes. Based on this general framework, we pick several specific models combining
(possibly explosive) diffusions and single jump processes, study their stochastic and statistical properties and
show how they can be applied to a common problem in mathematical finance, the pricing and hedging of
European options. Where indicated, we apply our methods to financial data sets.
The second part of the thesis introduces a class of point processes that combines two wellestablished cluster
mechanisms, a self\-exciting structure commonly referred to as Hawkes process, and a shot\-noise structure known
as Neyman\-Scott process. As such, these processes are useful in modeling the accumulation of points \- for
example, the clustering of negative returns during financial crashes within the framework mentioned above.
However, given that such point processes transcend the mostly diffusive setting of the first part and show a
similarity to ARMA time series of counts, which confirms their wide potential applicability beyond finance, this
line of work deserves a distinct part in this thesis. In many cases, missing data complicates statistical estimation
forthistypeofprocess,andexplicitmathematicalexpressionsexistonlyfor(Markovian)specialcases.Toaddress
this, we derive an Expectation\-Maximization (EM) algorithm that allows us to estimate general inhomogeneous
and non\-parametric specifications and marks. We test the algorithm in a range of simulation and case studies.
Scherer,B.andApel,M.(2020\). “Businesscycle\-relatedtimingofalternativeriskpremiastrategies .”In:The Journal
of Alternative Investments 22(4\), pp. 8–24\.
Time variation in risk premia is not a violation of market efficiency but rather a reflection of time\-varying
economic rewards. By analyzing macroeconomic sensitivities (proxying for good and bad times), the authors
show that time\-varying returns of certain alternative risk premia strategies are significantly related to economic
conditions. On the basis of identified return patterns, the authors construct a risk premia timing strategy that
adds statistically significant marginal performance with low turnover. They confront data mining concerns by
successfully cross validating their model across various investment universes.
Seidl, I. (2012\). “Markowitz versus Regime Switching: An Empirical Approach .” In:The Review of Finance and
Banking 04(1\), pp. 033–043\.
This article discusses an adjusted regime switching model in the context of portfolio optimization and com\-
pares the attained portfolio weights and the performance to a classical mean\-variance set\-up as introduced by
Markowitz (1952\). The model postulates different asset price dynamics under different regimes, and jumps be\-
tween regimes are driven by a Markov process. For examples, ’bear’ and ’bull’ markets could be such regimes.
Given a particular regime, portfolio weights are set based on the conditional means and variance\-covariance
structure of the asset dynamics. The model is evaluated in an out\-of\-sample period of the last three years with a
moving window and a forecast of only one period. It is found that with the adjusted regime switching portfolio
selection algorithm as applied here, the performance of the optimal portfolio is highly improved even where
portfolio weights are constrained to realistic values.
Sharaiha, Y. M. and Johansson, K. K. (2014\). “The state\-dependent time variation in the value premium .” In:
Journal of Asset Management 15(2\), pp. 150–161\.
It is well documented that asset and strategy returns are generally exposed to identifiable risk factors. Moreover,
the exposure to these systematic risk factors tends to be time varying. Examples of strategies that exhibit such
regime\-dependent variability include value investing in equity markets and carry in foreign exchange markets.
The literature proposes several macro\-based explanations for this time variation such as liquidity or cyclicality
risk depending on the strategy and horizon under consideration. This project relies on developments in the
academic literature in the area of state\-dependent asset pricing models (see, for example, survey by van Dijk
et al, 2002\). Under such a framework, a strategy return is modelled using a multi\-factor asset pricing equation
where the risk sensitivities (or betas) to the pre\-defined factors are allowed to vary according to one or multiple
statevariables. The approachconsidered here uses a logistic smooth transitionregression methodology applied to
the value strategy, where the state variables have an economic meaning (see Christiansen et al, 2011 application
to foreign exchange carry strategy). By distinguishing between low and high state regimes (in a continuous
62space), the aim is to first investigate improvements in the explanatory power of the model relative to the linear
(no\-state dependency) approach. In particular, we study the performance of the value factor during turbulent
periods, and identify economic variables driving its time\-varying behaviour. We also present an algorithm that
allocates dynamically to a long short value overlay portfolio conditioned on regime transitions. We show that
the performance of this dynamic portfolio is superior to a portfolio with a static value overlay.
Sheikh, A. Z. and Sun, J. (2012\). “Regime Change: Implications of Macroeconomic Shifts on Asset Class and
Portfolio Performance .” In:The Journal of Investing 21(3\), pp. 36–54\.
It is a well\-recognized empirical observation that different asset classes respond differently to different economic
drivers. It is also well recognized that asset class behavior can vary significantly over shifting economic scenarios.
This article builds on this empirical evidence to develop a quantitative framework for regime\-based asset alloca\-
tion. It investigates whether regime\-based investing can effectively respond to changes in economic regimes at the
portfolio level in an effort to provide better long\-term results when compared to a more static approach. Results
indicate that it is both possible and practical to develop a regime\-based investing approach that can potentially
add value over time. Success depends on identifying key factors that influence asset class performance, and then
developing a way to model those non\-linear relationships. Regime\-based investing also requires a healthy degree
of economic forecasting skill, which need not be perfect to add value. Based on the authors’ analysis, regime
based investing can offer investors a compelling alternative to a more static approach.
Shi, X. (2020\). “A Survey of Changepoint Techniques for Time Series Data .” PhD thesis. Clemson University.
Changepoint analysis has played an important role in modern time series study. Detection of changepoints
helps modelling and prediction of time series and is found in applications of many fields. This dissertation
focuses on the detection of mean structure changes in correlated time series. It consists of the results of three
research projects on changepoint problems: (1\) the comparison of changepoint techniques; (2\) autocovariance
estimation of an AR(p) time series with changepoints; and (3\) L1\-regularization in changepoint analysis. In
chapter 2 the single changepoint techniques, or At\-Most\-One\-Changepoint (AMOC) tests are reviewed. A new
AMOC test, Sum of Squared CUSUMz is developed and is shown to be the most powerful AMOC test through
simulation studies on the time series with various ARMA(p,q) structures. Multiple changepoint techniques that
are applicable to correlated time series are discussed in chapter 3, which includes an in\-depth discussion on the
wild binary segmentation. A new distance metric is also proposed in this chapter for comparing the multiple
changepoint techniques. Next in the chapter 4 a Yule\-Walk moment estimator based on the first order difference
is proposed for autocovariance estimation of an AR(p) time series with a small number of changepoints. The
last chapter simply reviews the L1\- regularization and its application to changepoint analysis.
Shi, X., Gallagher, C., Lund, R., and Killick, R. (2021\). “A Comparison of Single and Multiple Changepoint
Techniques for Time Series Data .” In:arXiv e\-Print .
This paper describes and compares several prominent single and multiple changepoint techniques for time series
data. Due to their importance in inferential matters, changepoint research on correlated data has accelerated
recently. Unfortunately, small perturbations in model assumptions can drastically alter changepoint conclusions;
for example, heavy positive correlation in a time series can be misattributed to a mean shift should correlation be
ignored. This paper considers both single and multiple changepoint techniques. The paper begins by examining
cumulative sum (CUSUM) and likelihood ratio tests and their variants for the single changepoint problem;
here, various statistics, boundary cropping scenarios, and scaling methods (e.g., scaling to an extreme value or
Brownian Bridge limit) are compared. A recently developed test based on summing squared CUSUM statistics
over all times is shown to have realistic Type I errors and superior detection power. The paper then turns to the
multiple changepoint setting. Here, penalized likelihoods drive the discourse, with AIC, BIC, mBIC, and MDL
penalties being considered. Binary and wild binary segmentation techniques are also compared. We introduce a
new distance metric specifically designed to compare two multiple changepoint segmentations. Algorithmic and
computational concerns are discussed and simulations are provided to support all conclusions. In the end, the
multiple changepoint setting admits no clear methodological winner, performance depending on the particular
scenario. Nonetheless, some practical guidance will emerge.
Shu, M., Song, R., and Zhu, W. (2021\). “The 2021 Bitcoin Bubbles and Crashes – Detection and Classification .”
In:SSRN e\-Print .
Inthisstudy,weadoptedtheLog\-PeriodicPowerLawSingularity(LPPLS)modelforreal\-timeidentificationand
monitoring of Bitcoin bubbles and crashes using different time scale data and proposed the modified Lagrange
regularization method to alleviate the impact of potential LPPLS model over\-fitting to better estimate bubble
start time and market regime change. We also aimed to determine the natures of the bubbles and crashes \-
63be it endogenous due to its own price evolution or exogenous due to external market and/or policy influences.
We performed a systematic market event analysis and correlated which to Bitcoin bubbles detected. Based on
the daily LPPLS confidence indictor from December 1, 2019 to June 24, 2021, we found that the Bitcoin boom
from November 2020 to mid\-January 2021 is an endogenous bubble, stemming from the self\-reinforcement of
cooperative herding and imitative behaviors of market players, while the price spike from mid\-January 2021
to mid\-April 2021 is likely an exogenous bubble driven by extrinsic events including a series of large\-scale
acquisitions and adoptions by well\-known institutions such as Visa and Tesla. We have also demonstrated the
utilities of multi\-resolution LPPLS analysis in revealing both short\-term changes and long\-term states.
Siliverstovs, B. and Wochner, D. (2021\). “State\-Dependent Evaluation of Predictive Ability .” In:Journal of Fore\-
casting40(3\), pp. 547–574\.
This study systematically broadens the relevance of possible model performance asymmetries across business
cycles in the spirit of the recent state\-dependent forecast evaluation literature (e.g. Chauvet and Potter, 2013\) to
hundreds of macroeconomic indicators and deepens the forecast evaluation of the recent factor model literature
on hundreds of target variables (e.g. Stock and Watson, 2012b) in a state\-dependent manner. Our results are
consistent with both strands of the literature and generalize the former to over 200 macroeconomic indicators
and differentiate the latter across three levels of temporal granularity: We document systematic model perfor\-
mance differences in both absolute and relative terms across business cycles (longitudinal) as well as across
variable groups (cross\-sectional) and find these performance differences to be robust across several alternative
specifications. The cross\-sectional prevalence and robustness of state\-dependency shown in this article encour\-
ages economic forecasters to complement model performance assessments with a state\-dependent evaluation of
predictive ability.
Silveira, D. and Oscar, R. B. L. M. (2021\). “Inflation Targeting Regimes in Emerging Market Economies: To Invest
or Not to Invest? ” In:SSRN e\-Print .
WeproposeastochasticlearningrulethroughanAgent\-basedModel(ABM)tounderstandhowemergingmarket
economies (EMEs) can achieve high levels of investment, given the announced inflation target rate. The central
banks act as a pseudo\-player, choosing between the pursued target inflation rate or a negative inflation rate.
By taking this action as given, bounded\-rational firms and workers iteratively play a two\-population well\-mixed
evolutionary game to make investment decisions. Our findings show that when inflation converges to its target,
lessthecentralplanners’efforttoreachthesteady\-statewithinvestmentcoordination.Whencentralbankstarget
a negative inflation rate, it can speed up the EMEs’ convergence to a steady\-state with agents coordinating their
investment strategies. It shed some light on central banks’ transparency and credibility to avoid the so\-called
debt\-deflationspiral,whichtypicallyincreasestheuncertaintyinEMEs,limitingtheinvestmentsintheeconomy.
Simonian, J. (2020\). “Mixed Ag: A Regime\-Based Analysis of Multi\-Asset Agriculture Portfolios .” In:The Journal
of Portfolio Management 46(6\), pp. 135–146\.
For some time now, the prospect that the world is entering a new epoch of elevated prices for agricultural
commodities has been a focus of both policymakers concerned with the food security of their citizens and
investors looking to benefit from a potential secular uptrend in the demand for food. Investors most commonly
access agriculture in public markets through funds that invest in agricultural commodity futures or the common
stock of companies that engage in agribusiness. In general, funds that invest in agricultural commodities are
either dedicated equity or futures managers. However, there are potentially significant performance benefits
to investing in agricultural commodities through a single multi\-asset vehicle composed of both agricultural
commodity futures and agribusiness stocks. To that end, in this article the author examines the performance
of a multi\-asset agriculture portfolio in periods of high and low economic growth and compares it with the
performanceofitsindividualequityandfuturescomponents,aswellasthebroaderstockmarketandinvestment\-
grade bonds. The author finds that in terms of return generation, risk mitigation, and diversification potential
relative to core stocks and bonds, the multi\-asset agriculture strategy makes a compelling case for inclusion
alongside traditional strategies within institutional investors portfolios.
Simonian, J. and Wu, C. (2019a). “Factors in Time: Fine\-Tuning Hedge Fund Replication .” In:The Journal of
Portfolio Management 45 (3\), pp. 159–164\.
Hedge fund replication has become a cottage industry in investing. Among the most popular hedge fund repli\-
cation frameworks are factor models based on ordinary least squares (OLS) regression, a development that is
no doubt due to its simplicity and familiarity among investment practitioners. Despite their widespread use,
the OLS regression\-based factor models that form the basis for many hedge fund replication programs are of\-
ten overfitted to a single sample, severely undercutting their predictive effectiveness. As a remedy to the latter
64shortcoming, in this article the authors apply the regularization method known as regression to the replication of
hedge fund strategies. Ridge regression works by formally imbuing a regression with additional bias in exchange
for a reduction in the variance between training and test samples. Using a simple yet robust methodology, the
authors show how to dynamically calibrate the predictively optimal level of bias without significantly reducing
the backward\-looking explanatory power of a given model. In doing so, the authors demonstrate that ridge
regression can help produce generalizable models that are useful in both the ex post risk analysis and ex ante
replication of hedge fund strategies.
Simonian, J. and Wu, C. (2019b). “Minsky vs. Machine: New Foundations for Quant\-Macro Investing .” In:The
Journal of Financial Data Science 1(2\), pp. 94–110\.
Systematic macro investors use of the regime\-switching models that have been developed in academia over the
last several decades is infrequent at best and, when used, generally tangential to their core investment process.
The roots of this less\-than\-enthusiastic uptake can be found in two familiar sources: models that possess an
overly complex formal structure and poor predictive ability. As a remedy to the current state of affairs, the
authors present a new foundation for regime\-based investing, one based on spectral clustering, a graph theoretic
approach to classifying data. Drawing inspiration from the work of Hyman Minsky and John Geanakoplos, the
authors present a macro framework that uses measures of growth, inflation, and leverage to define regimes and
drive portfolio decisions. To the latter end, the authors show how the framework can be used to build portfolios
using information about regimes as defined, to outperform a no\-information equal\-weight portfolio both out\-of\-
sample and in bootstrapped and cross\-validated simulations. The authors thus show that spectral clustering can
provide both an elegant mathematical description of the leverage cycle and a robust foundation for quant\-macro
investing.
Singh, A. and Singh, M. (2016\). “Risk\-Return Relationship in BRIC Equity Markets: Evidence from Markov Regime
Switching Model with Time\-varying Transition Probabilities.” In: Metamorphosis : A Journal of Management
Research .
A rich literature supports the existence of both positive and negative relationship between the risk and return in
the developed equity markets. However, the present study attempts to capture the risk\-return relationship in the
most promising and opportunities\-instilled emerging market club, the ”BRIC” equity markets, by employing a
Markov regime switching model with time\-varying transition probabilities, further taking St. Louis Fed Financial
Stress Index (the US financial market stress) as an economic variable. The weekly benchmark index values are
used in the analysis, spanning from the year 2004 to 2013\. The results report the existence of time\-varying
transition probabilities with respect to the Brazilian and Indian markets only and fixed transition probabilities
for the other countries undertaken. The Markov results support the existence of two regimes, wherein regime\-1
reports a positive risk\-return relationship, and regime\-2 reports a negative relationship between the risk and
return. Ironically, the Chinese equity market is found to be the riskiest but a perfect hedge instrument amongst
others, considering its risk\-return interactions in both the regimes. Furthermore, a lower level of financial stress
in the US financial market is associated with a higher probability of remaining in the ”Bullish” regime\-1 in the
Indian market as well as Brazilian market. Moreover, there is a positive co\-movement between the US financial
stress and the expected time\-varying duration of remaining in the ”Bearish” regime. This shows that due to the
growing interdependence among the worldwide economies, a financial stress in one economy does have an impact
on the other markets and risk\-return relationship in their equity markets. An understanding of the risk\-return
dynamics coupled with the impact of exogenous variables is an imperative task that a portfolio manager must
undertake so as to justify and manage the investments made in the equity markets.
Smith, S. (2021\). “International Stock Return Predictability and Asset Pricing Models .” In:SSRN e\-Print .
We propose a new methodology for predicting international stock returns and evaluating international asset
pricing models. Our Bayesian framework performs probabilistic selection of predictors and factors that can shift
at multiple unknown structural break dates. The approach generates significantly more accurate forecasts of
international stock returns than a range of popular models that are economically meaningful for a risk\-averse
mean\-variance investor. Allowing for regime\-specific variable selection reduces considerably the international
diversification of an unhedged U.S. investor’s portfolio. Our framework improves the ability of international
asset pricing models to explain the cross\-section of expected returns.
Smith, S. C., Bulkley, G., and Leslie, D. S. (2020\). “Equity Premium Forecasts with an Unknown Number of
Structural Breaks .” In:Journal of Financial Econometrics 18(1\), pp. 59–94\.
Estimation of models with structural breaks usually assumes a pre\-specified number of breaks. Previous models
which do allow an endogenously determined number of breaks require a simple structural model, and rarely
65allow for information transfer across the break. We introduce a methodology that allows the number of breaks
to be determined endogenously and including an economically motivated model of transition regimes between
each break. We demonstrate the usefulness of our approach for forecasts of the equity premium. We find the
demonstratedsuccessofthehistoricalaveragecanbeimproveduponbyaneconomicmodelwiththeoryinformed
priors estimated using our methodology.
Smith, S. C. and Timmermann, A. (2021\). “Break Risk .” In:The Review of Financial Studies 34(4\), pp. 2045–2100\.
We develop a new approach to modeling and predicting stock returns in the presence of breaks that simultane\-
ously affect a large cross\-section of stocks. Exploiting information in the cross\-section enables us to detect breaks
in return prediction models with little delay and to generate out\-of\-sample return forecasts that are significantly
more accurate than those from existing approaches. To identify the economic sources of breaks, we explore the
asset pricing restrictions implied by a present value model which links breaks in return predictability to breaks
in the cash flow growth and discount rate processes.
Smug, D., Ashwin, P., and Sornette, D. (2017\). “Predicting Financial Market Crashes Using Ghost Singularities .”
In:SSRN e\-Print .
We analyse the behaviour of a non\-linear model of coupled stock and bond prices exhibiting periodically collaps\-
ing bubbles. By using the formalism of dynamical system theory, we explain what drives the bubbles and how
foreshocks or aftershocks are generated. A dynamical phase space representation of that system coupled with
standard multiplicative noise rationalises the log\-periodic power law singularity pattern documented in many
historical financial bubbles. The notion of ’ghosts of finite\-time singularities’ is introduced and used to estimate
the end of an evolving bubble, using finite\-time singularities of an approximate normal form near the bifurcation
point. We test the forecasting skill of this method on different stochastic price realisations and compare with
Monte Carlo simulations of the full system. Remarkably, the former is significantly more precise and less biased.
Moreover, the method of ghosts of singularities is less sensitive to the noise realisation, thus providing more
robust forecasts.
Sornette, D. (2014\). “Dragon\-kings and Predictions: Diagnostics and Forecasts for the World Financial Crisis .” In:
SSRN e\-Print .
We develop the concept of ”dragon\-kings” corresponding to meaningful outliers, which are found to coexist with
power laws in the distributions of event sizes under a broad range of conditions in a large variety of systems.
These dragon\-kings reveal the existence of mechanisms of self\-organization that are not apparent otherwise
from the distribution of their smaller siblings. We present a generic phase diagram to explain the generation
of dragon\-kings and document their presence in six different examples (distribution of city sizes, distribution
of acoustic emissions associated with material failure, distribution of velocity increments in hydrodynamic tur\-
bulence, distribution of financial drawdowns, distribution of the energies of epileptic seizures in humans and in
model animals, distribution of the earthquake energies). We emphasize the importance of understanding dragon\-
kings as being often associated with a neighborhood of what can be called equivalently a phase transition, a
bifurcation, a catastrophe (in the sense of Rene Thom), or a tipping point. The presence of a phase transition
is crucial to learn how to diagnose in advance the symptoms associated with a coming dragon\-king. Several ex\-
amples of predictions using the derived log\-periodic power law method are discussed, including material failure
predictions and the forecasts of the end of financial bubbles.
Sornette, D., Andraszewicz, S., Murphy, R. O., Rindler, P. B., and Sanadgol, D. (2016\). “Resolving Persistent
Uncertainty by Self\-Organized Consensus to Mitigate Market Bubbles .” In:SSRN e\-Print .
We propose a new paradigm to study coordination in complex social systems, such as financial markets, that
accounts for fundamental uncertainty. This new context has features from prediction markets that have been
shown previously to mitigate price bubbles in classical asset market experiments. Our setup is more realistic as
it offers multiple securities that are continuously traded over days and, importantly, there is no true underlying
price. Nonetheless, the market is designed such that its rationality can be evaluated. Quick consensus emerges
earlyyieldingpronouncedmarketbubbles.Theoverpricingdiminishesovertime,indicatinglearning,butdoesnot
disappearcompletely.Traders’priceestimatesbecomeprogressivelymoreindependentviaacollectiverealization
ofcommunalignorance,pushingthemarketmuchclosertorationality,withforecaststhatareclosetotherealized
outcomes.
Sornette, D. and Cauwels, P. (2014\). “Financial bubbles: mechanisms and diagnostics .” In:arXiv e\-Print .
We define a financial bubble as a period of unsustainable growth, when the price of an asset increases ever more
quickly,inaseriesofacceleratingphasesofcorrectionsandrebounds.Moretechnically,duringabubblephase,the
price follows a faster\-than\-exponential power law growth process, often accompanied by log\-periodic oscillations.
66This dynamic ends abruptly in a change of regime that may be a crash or a substantial correction. Because they
leave such specific traces, bubbles may be recognised in advance, that is, before they burst. In this paper, we will
explain the mechanism behind financial bubbles in an intuitive way. We will show how the log\-periodic power
law emerges spontaneously from the complex system that financial markets are, as a consequence of feedback
mechanisms, hierarchical structure and specific trading dynamics and investment styles. We argue that the risk
of a major correction, or even a crash, becomes substantial when a bubble develops towards maturity, and that
it is therefore very important to find evidence of bubbles and to follow their development from as early a stage
as possible. The tools that are explained in this paper actually serve that purpose. They are at the core of the
Financial Crisis Observatory at the ETH Zurich, where tens of thousands of assets are monitored on a daily
basis. This allow us to have a continuous overview of emerging bubbles in the global financial markets. The
companion report available as part of the Notenstein white paper series (2014\) with the title “Financial bubbles:
mechanism, diagnostic and state of the World (Feb. 2014\)” presents a practical application of the methodology
outlines in this article and describes our view of the status concerning positive and negative bubbles in the
financial markets, as of the end of January 2014\.
Sornette,D.,Cauwels,P.,andSmilyanov,G.(2017\). “CanWeUseVolatilitytoDiagnoseFinancialBubbles?Lessons
from 40 Historical Bubbles .” In:SSRN e\-Print .
We inspect the price volatility before, during, and after financial asset bubbles in order to uncover possible
commonalities and check empirically whether volatility might be used as an indicator or an early warning
signal of an unsustainable price increase and the associated crash. Some researchers and finance practitioners
believe that historical and/or implied volatility increase before a crash, but we do not see this as a consistent
behavior. We examine forty well\-known bubbles and, using creative graphical representations to capture robustly
the transient dynamics of the volatility, find that the dynamics of the volatility would not have been a useful
predictor of the subsequent crashes. In approximately two\-third of the studied bubbles, the crash follows a period
of lower volatility, reminiscent of the idiom of a ”lull before the storm”. This paradoxical behavior, from the
lenses of traditional asset pricing models, further questions the general relationship between risk and return.
Sornette, D., Demos, G., Zhang, Q., Cauwels, P., Filimonov, V., and Zhang, Q. (2015\). “Real\-time prediction and
post\-mortem analysis of the Shanghai 2015 stock market bubble and crash .” In:Journal of Investment Strategies
4(4\).
The authors assess the performance of the real\-time diagnostic, available to the public on the website of the
Financial Crisis Observatory (FCO) at ETH Zurich, of the bubble regime that began developing in Chinese
stock markets in mid\-2014 and started to burst in June 2015\. The analysis is based on (i) the economic theory
of rational expectation bubbles; (ii) the behavioral mechanisms of imitation and the herding of investors and
traders; (iii) the mathematical formulation of the log\-periodic power lawsingularity (LPPLS), which describes
the critical approach toward a tipping point in complex systems. The authors document how the real\-time
predictions were presented in the automated analysis of the FCO, as well as in their FCO Cockpit report of
June 2015\. A complementary post\-mortem analysis of the nature and value of the LPPLS methodology in
diagnosing the Shanghai Composite Index bubble and its termination is also given.
SSgA Research (2015\). Optimizing asset allocations to market regimes . Tech. rep. State Street Global Advisors.
One of the greatest challenges investors face is finding an investment strategy that provides competitive returns
while reducing downside risk in both stable and changing market environments. The past two decades have
shown the limitations of traditional, static portfolio approaches and the weakness of diversification alone as a
loss protection strategy. Many investors found that their supposedly diversified portfolios had correlations that
moved to one in times of crisis and fell in lockstep. On the other hand, excessive caution over asset allocation in
more favorable markets may well equate to less upside participation, also leading to a less than optimal return.
But what if a strategy could help reduce a portfolio’s risk exposure before a downside event took place? What
if a strategy could continually and dynamically re\-allocate assets for optimal returns? Is there a reliable way of
determining safer market conditions in which it makes more sense to invest more heavily in aggressive assets,
providing optimized growth? We think there is. Look Forward, Not Backward We’ve found that recent crises
have caused many investors to ask what they could have done differently and to consider if there were signals,
triggers or data points that may have foreshadowed the chaos that followed. They’re looking to avoid damaging
downsides but also to time increasing their market participation at the most favorable times. We recognized that
retro\-fitting signals from previous crises and opportunities may not mean that we will spot the next ones. So,
we set out to build a framework that had effective signaling power across a number of prior events, while also
recognizing the need to continually adjust its influences over time. Our goal was to develop and design a market\-
67aware framework and dynamic investment process that would give us a systematic approach for identifying
market environments and which used forward\-looking factors to indicate which type of environment the market
was moving into.
Stillwagon, J. and Sullivan, P. (2020\). “Markov switching in exchange rate models: will more regimes help? ” In:
Empirical Economics , pp. 413–436\.
This paper examines the performance of Markov switching models of the exchange rate using a data\-driven ap\-
proach to determine the number of regimes rather than simply assuming twostates. The analysis is conducted for
the British pound, Canadian dollar, and Japanese yen exchange rates against the US dollar over the last 30 years
with alternative specifications including a simple segmented trends model and Markov switching autoregressive
models with monetary fundamentals. A noteworthy finding is that the number of regimes that minimizes mean
square forecast errors tends to correspond to the number of regimes selected by Bayesian information criteria
(but not Markov\-switching\-specific information criteria). For the monetary models, the number of regimes that
minimizes forecast errors also tends to correspond to the most parsimonious model with well\-behaved residu\-
als. Although allowing for more regimes yields forecasting improvement over single\- or two\-regime models, the
Markov switching model is still unable to outperform a random walk. This suggests that exchange rate models
need to allow for novel, as opposed to repetitive or predetermined, structural change.
Sueppel, R. (2021\). Classifying market regimes . Tech. rep. Systematic Risk and Systematic Value.
Market regimes are clusters of persistent market conditions. They affect the relevance of investment factors
and the success of trading strategies. The practical challenge is to detect market regime changes quickly and
to backtest methods that may do the job. Machine learning offers a range of approaches to that end. Recent
proposals include \[1] supervised ensemble learning with random forests, which relate the market state to values of
regime\-relevant time series, \[2] unsupervised learning with Gaussian mixture models, which fit various distinct
Gaussian distributions to capture states of the data, \[3] unsupervised learning with hidden Markov models,
which relate observable market data, such as volatility, to latent state vectors, and \[4] unsupervised learning
with Wasserstein k\-means clustering, which classifies market regimes based on the distance of observed points
in a metric space.
Tachibana, M. (2020\). “Flight\-to\-quality in the stock\-bond return relation: a regime\-switching copula approach .”
In:Financial Markets and Portfolio Management 34, pp. 429–470\.
This paper examines the existence, intensity and international dependence of flight\-to\-quality from stocks to
government bonds. To this end, we develop a two\-state regime\-switching bivariate copula model and apply it
to the domestic and cross\-country stock\-bond return pairs of six developed countries (France, Germany, Japan,
Switzerland, the UK and the US) over the period 1999\-2019\. We find that US and UK government bonds have
played a primary role of safe\-haven assets during stock market downturns. The remaining government bond
markets show the evidence of flight\-to\-quality, but its intensity is relatively weak. Further, we find that although
flight\-to\-quality tends to occur simultaneously in multiple countries, the frequency of the joint occurrence varies
across government bond markets.
Tajeuna, E. G., Bouguessa, M., and Wang, S. (2022\). “Modeling Regime Shifts in Multiple Time Series .” In:arXiv
e\-Print.
We investigate the problem of discovering and modeling regime shifts in an ecosystem comprising multiple time
series known as co\-evolving time series. Regime shifts refer to the changing behaviors exhibited by series at
different time intervals. Learning these changing behaviors is a key step toward time series forecasting. While
advances have been made, existing methods suffer from one or more of the following shortcomings: (1\) failure to
takerelationshipsbetweentimeseriesintoconsiderationfordiscoveringregimesinmultipletimeseries;(2\)lackof
an effective approach that models time\-dependent behaviors exhibited by series; (3\) difficulties in handling data
discontinuities which may be informative. Most of the existing methods are unable to handle all of these three
issues in a unified framework. This, therefore, motivates our effort to devise a principled approach for modeling
interactions and time\-dependency in co\-evolving time series. Specifically, we model an ecosystem of multiple time
series by summarizing the heavy ensemble of time series into a lighter and more meaningful structure called a
mapping grid . By using the mapping grid, our model first learns time series behavioral dependencies through
a dynamic network representation, then learns the regime transition mechanism via a full time\-dependent Cox
regression model. The originality of our approach lies in modeling interactions between time series in regime
identification and in modeling time\-dependent regime transition probabilities, usually assumed to be static in
existing work.
68Tran, B.\-H., Rossi, S., Milios, D., Michiardi, P., Bonilla, E. V., and Filippone, M. (2021\). “Model Selection for
Bayesian Autoencoders .” In:arXiv e\-Print .
We develop a novel method for carrying out model selection for Bayesian autoencoders (BAEs) by means of
prior hyper\-parameter optimization. Inspired by the common practice of type\-II maximum likelihood optimiza\-
tion and its equivalence to Kullback\-Leibler divergence minimization, we propose to optimize the distributional
sliced\-Wasserstein distance (DSWD) between the output of the autoencoder and the empirical data distribu\-
tion. The advantages of this formulation are that we can estimate the DSWD based on samples and handle
high\-dimensional problems. We carry out posterior estimation of the BAE parameters via stochastic gradient
Hamiltonian Monte Carlo and turn our BAE into a generative model by fitting a flexible Dirichlet mixture
model in the latent space. Consequently, we obtain a powerful alternative to variational autoencoders, which
are the preferred choice in modern applications of autoencoders for representation learning with uncertainty.
We evaluate our approach qualitatively and quantitatively using a vast experimental campaign on a number of
unsupervised learning tasks and show that, in small\-data regimes where priors matter, our approach provides
state\-of\-the\-art results, outperforming multiple competitive baselines.
Tu, J. (2010\). “Is Regime Switching in Stock Returns Important in Portfolio Decisions? ” In:Management Science
56, pp. 1198–1215\.
The stock market displays regime switching between upturns and downturns. This paper provides a Bayesian
framework for making portfolio decisions that takes this regime switching into account, together with asset
pricing model uncertainty and parameter uncertainty. The findings reveal that the economic value of accounting
for regimes is substantially independent of whether or not model and parameter uncertainties are incorporated:
the certainty\-equivalent losses associated with ignoring regime switching are generally above 2 percent per year,
and can be as high as 10 percent. These results suggest that the more realistic regime switching model is
fundamentally different from the commonly used single\-state model, and hence should be employed instead in
portfolio decisions irrespective of concerns about model or parameter uncertainty.
Uysal, A. S. and Mulvey, J. M. (2021\). “A Machine Learning Approach in Regime\-Switching Risk Parity Portfolios .”
In:The Journal of Financial Data Science 3(2\), pp. 87–108\.
The authors present a machine learning approach to regime\-based asset allocation. The framework consists of
two primary components: (1\) regime modeling and prediction and (2\) identifying a regime\-based strategy to
enhance the performance of a risk parity portfolio. For the former, they apply supervised learning algorithms,
includingtherandomforest,basedonalargemacroeconomicdatabasetoestimatetheprobabilityofanupcoming
recession or a stock market contraction. Out\-of\-sample tests show the reliability of these predictions, especially
for recessions in the United States, over the period 1973 to 2020\. The probability estimates are linked to a
dynamic investment overlay strategy. The combined approach improves risk\-adjusted returns by a substantial
amount over nominal risk parity in two\-asset and multi\-asset test cases, even during rising interest rates in the
late 1970s.
Uysal, S. (2021\). “Risk Budgeting Portfolios Under a Modern Optimization and Machine Learning Lens .” PhD
thesis. Princeton University.
The mean\-variance optimization framework has been the traditional approach to decide portfolio allocations
based on return\-risk trade\-offs. However, it faces practical drawbacks, including sensitivity to estimated input
parameters and concentration of portfolio risk. Risk budgeting portfolio optimization is a popular risk\-based
asset allocation technique where risk budgets are assigned to each assets’ risk contribution, and equalizing all risk
budgets in the portfolio is known as risk parity strategy. Unlike mean\-variance, the risk parity strategy provides
a balanced risk concentration in the portfolio and does not require expected asset return estimates as input.
However, its performance can depend on the selected asset universe. Furthermore, its mathematical formulation
imposes some computational challenges due to the non\-convex structure. In this thesis, the risk budgeting
problem is studied with modern optimization and machine learning approaches to enhance the portfolio model
andaddresstheaforementionedchallenges.Thesecondchapterintroducesregime\-switchingriskparityportfolios
with two primary components: regime modeling and prediction with supervised learning methods and identifying
a regime\-based strategy to improve the performance of a nominal risk parity portfolio. In the third chapter,
we formulate a multi\-period risk parity portfolio optimization problem in a transaction cost environment with
a model predictive control approach. We provide a successive convex program algorithm that provides faster
and more robust solutions. Lastly, we present an end\-to\-end portfolio allocation method by embedding the
risk budget optimization problem as an implicit layer in a neural network. This approach combines prediction
and optimization tasks in a single decision\-making pipeline and constructs dynamic risk budgeting portfolios.
69Furthermore, we introduce a novel asset selection property with stochastic gates that protects the risk budgeting
portfolio against the unprofitable assets.
van den Burg, G. J. J. and Williams, C. K. I. (2022\). “An Evaluation of Change Point Detection Algorithms .” In:
arXiv e\-Print .
Change point detection is an important part of time series analysis, as the presence of a change point indicates an
abrupt and significant change in the data generating process. While many algorithms for change point detection
exist, little attention has been paid to evaluating their performance on real\-world time series. Algorithms are
typically evaluated on simulated data and a small number of commonly\-used series with unreliable ground truth.
Clearly this does not provide sufficient insight into the comparative performance of these algorithms. Therefore,
instead of developing yet another change point detection method, we consider it vastly more important to
properly evaluate existing algorithms on real\-world data. To achieve this, we present the first data set specifically
designed for the evaluation of change point detection algorithms, consisting of 37 time series from various
domains. Each time series was annotated by five expert human annotators to provide ground truth on the
presence and location of change points. We analyze the consistency of the human annotators, and describe
evaluation metrics that can be used to measure algorithm performance in the presence of multiple ground truth
annotations. Subsequently, we present a benchmark study where 14 existing algorithms are evaluated on each of
the time series in the data set. This study shows that binary segmentation (Scott and Knott, 1974\) and Bayesian
online change point detection (Adams and MacKay, 2007\) are among the best performing methods. Our aim is
that this data set will serve as a proving ground in the development of novel change point detection algorithms.
van Vliet, P. and Blitz, D. (2011\). “Dynamic strategic asset allocation: Risk and return across the business cycle .”
In:Journal of Asset Management 12(5\), pp. 360–375\.
We propose a practical investment framework for dynamic asset allocation across different phases in the business
cycle, which we illustrate using a sample of US data from 1948 to 2007\. We identify four phases in the business
cycle and find that these capture pronounced time variation in the risk and return properties of asset classes.
Time variation is also observed in the risk of a traditional, static strategic asset mix. In order to stabilize risk
across the business cycle, we propose a dynamic strategic asset allocation approach, which has the potential to
enhance expected return as well. The proposed investment framework is found to be robust to variations in the
variable composition of the business cycle indicator and can easily be extended with different economic variables
and/or additional assets.
Viebig, J. (2020\). “Exuberance in Financial Markets: Evidence from Machine Learning Algorithms .” In:Journal of
Behavioral Finance 21(2\), pp. 128–135\.
Motivated by Campbell and Shiller (1998\), we show that the probability that abnormally low returns over long\-
term investment horizons occur in the future is disproportionately high when equity markets trade at extremely
high valuation levels. Support vector machines are able to learn patterns from fundamental data with high
precision rates. Decision boundaries calculated with machine learning algorithms can help investors to detect
irrational exuberance in financial markets followed by abnormally low returns.
Vo, H. T. and Maurer, R. (2013\). “Dynamic Asset Allocation under Regime Switching, Predictability and Parameter
Uncertainty .” In:SSRN e\-Print .
This paper solves the dynamic asset allocation problem under stock return predictability based on the dividend
price ratio with regime shifts and parameter uncertainty in a fully Bayesian framework. Intertemporal hedging
demands are simultaneously induced by predictability, regime shifts, parameter uncertainty, and learning about
theregimes.Optimalpoliciesdisplaynon\-monotonichorizoneffectswherebyregimeshiftstendtoinducenegative
hedge demands in the short\-run, while predictability induces positive hedge demands in the long\-run. The
economic costs of ignoring regime switching and predictability are high even in the light of regime and parameter
uncertainty.
Wang, J., Ma, F., Liang, C., and Chen, Z. (2022\). “Volatility forecasting revisited using Markov\-switching with
time\-varying probability transition .” In:International Journal of Finance \& Economics .
This study proposes a novel model, Markov\-switching Heterogeneous Autoregressive (MS\-HAR) model with
jump\-driven time\-varying transition probabilities (TVTP), to forecast the future volatility in Chinese stock
market. The in\-sample results show that MS\-HAR models are more powerful than HAR\-RV\-type models; fur\-
thermore,thehigh\-volatilityregimeisshort\-lived.Moreover,theout\-of\-sampleresultsindicatethattheMS\-HAR
with TVTP model can achieve a superior forecasting performance and increase the economic value than the
competing models including the simple HAR model and the MS\-HAR with fixed transition probabilities (FTP)
70model. The results are robust to several robustness checks including alternative forecast window, alternative
evaluation method, alternative predictive model, sub\-sample analysis and alternative representative index.
Wang, P. and Zong, L. (2020\). “Are Crises Predictable? A Review of the Early Warning Systems in Currency and
Stock Markets .” In:arXiv e\-Print .
The study efforts to explore and extend the crisis predictability by synthetically reviewing and comparing a
full mixture of early warning models into two constitutions: crisis identifications and predictive models. Given
empirical results on Chinese currency and stock markets, three\-strata findings are concluded as (i) the SWARCH
model conditional on an elastic thresholding methodology can most accurately classify crisis observations and
greatly contribute to boosting the predicting precision, (ii) stylized machine learning models are preferred given
higher precision in predicting and greater benefit in practicing, (iii) leading factors sign the crisis in a diversified
way for different types of markets and varied prediction periods.
Wang, R., Nie, K., Chang, Y.\-J., Gong, X., Wang, T., Yang, Y., and Long, B. (2020\). “Deep Learning for Anomaly
Detection .” In:Proceedings of the 26th ACM SIGKDD International Conference on Knowledge Discovery \& Data
Mining. ACM.
Anomaly detection has been widely studied and used in diverse applications. Building an effective anomaly de\-
tection system requires researchers and developers to learn complex structure from noisy data, identify dynamic
anomaly patterns, and detect anomalies with limited labels. Recent advancements in deep learning techniques
have greatly improved anomaly detection performance, in comparison with classical approaches, and have ex\-
tended anomaly detection to a wide variety of applications. This tutorial will help the audience gain a com\-
prehensive understanding of deep learning based anomaly detection techniques in various application domains.
First, we give an overview of the anomaly detection problem, introducing the approaches taken before the deep
model era and listing out the challenges they faced. Then we survey the state\-of\-the\-art deep learning models
that range from building block neural network structures such as MLP, CNN, and LSTM, to more complex
structures such as autoencoder, generative models (VAE, GAN, Flow\-based models), to deep one\-class detection
models, etc. In addition, we illustrate how techniques such as transfer learning and reinforcement learning can
help amend the label sparsity issue in anomaly detection problems and how to collect and make the best use of
user labels in practice. Second to last, we discuss real world use cases coming from and outside LinkedIn. The
tutorial concludes with a discussion of future trends.
Wang, X. and Hsieh, F. (2021\). “Unraveling S\&P500 stock volatility and networks – An encoding\-and\-decoding
approach .” In:arXiv e\-Print .
Volatility of financial stock is referring to the degree of uncertainty or risk embedded within a stock’s dynamics.
Such risk has been received huge amounts of attention from diverse financial researchers. By following the
concept of regime\-switching model, we proposed a non\-parametric approach, named encoding\-and\-decoding,
to discover multiple volatility states embedded within a discrete time series of stock returns. The encoding is
performed across the entire span of temporal time points for relatively extreme events with respect to a chosen
quantile\-based threshold. As such the return time series is transformed into Bernoulli\-variable processes. In the
decoding phase, we computationally seek for locations of change points via estimations based on a new searching
algorithm in conjunction with the information criterion applied on the observed collection of recurrence times
upon the binary process. Besides the independence required for building the Geometric distributional likelihood
function, the proposed approach can functionally partition the entire return time series into a collection of
homogeneous segments without any assumptions of dynamic structure and underlying distributions. In the
numerical experiments, our approach is found favorably compared with parametric models like Hidden Markov
Model. In the real data applications, we introduce the application of our approach in forecasting stock returns.
Finally, volatility dynamic of every single stock of S\&P500 is revealed, and a stock network is consequently
established to represent dependency relations derived through concurrent volatility states among S\&P500\.
Wehrli, A. and Sornette, D. (2022\). “Classification of flash crashes using the Hawkes(p,q) framework .” In:Quanti\-
tative Finance 22(2\), pp. 213–240\.
Weintroduceanovelmodelingframework\-theHawkes(p,q)process\-whichallowsustoparsimoniouslydisentangle
andquantifythetime\-varyingshareofhighfrequencyfinancialpricechangesthatareduetoendogenousfeedback
processes and not exogenous impulses. We show how both flexible exogenous arrival intensities, as well as a time\-
dependent feedback parameter can be estimated in a structural manner using an Expectation Maximization
algorithm. We use this approach to investigate potential characteristic signatures of anomalous market regimes
in the vicinity of ’flash crashes’\-events where prices exhibit highly irregular and cascading dynamics. Our study
covers some of the most liquid electronic financial markets, in particular equity and bond futures, foreign
71exchange and cryptocurrencies. Systematically balancing the degrees of freedom of both exogenously driving
processes and endogenous feedback variation using information criteria, we show that the dynamics around
such events are not universal, highlighting the usefulness of our approach: (i) post\-mortem, for developing
remedies and better future processes\-e.g. improving circuit breakers or latency floor designs\-and potentially (ii)
ex\-ante, for short\-term forecasts in the case of endogenously driven events. Finally, we test our proposed model
against a process with refined treatment of exogenous clustering dynamics in the spirit of the recently proposed
autoregressive moving\-average (ARMA) point process.
Werge, N. (2021\). “Predicting Risk\-adjusted Returns using an Asset Independent Regime\-switching Model .” In:
arXiv e\-Print .
Financial markets tend to switch between various market regimes over time, making stationarity\-based models
unsustainable. We construct a regime\-switching model independent of asset classes for risk\-adjusted return
predictions based on hidden Markov models. This framework can distinguish between market regimes in a wide
range of financial markets such as the commodity, currency, stock, and fixed income market. The proposed
method employs sticky features that directly affect the regime stickiness and thereby changing turnover levels.
An investigation of our metric for risk\-adjusted return predictions is conducted by analyzing daily financial
market changes for almost twenty years. Empirical demonstrations of out\-of\-sample observations obtain an
accurate detection of bull, bear, and high volatility periods, improving risk\-adjusted returns while keeping a
preferable turnover level.
Wheatley, S., Sornette, D., Huber, T., Reppen, M., and Gantner, R. N. (2018\). “Are bitcoin bubbles predictable?
combining a generalized metcalfe’s law and the LPPLS model .” In:SSRN e\-Print .
We develop a strong diagnostic for bubbles and crashes in bitcoin, by analyzing the coincidence (and its absence)
of fundamental and technical indicators. Using a generalized Metcalfe’s law based on network properties, a
fundamental value is quantified and shown to be heavily exceeded, on at least four occasions, by bubbles that
grow and burst. In these bubbles, we detect a universal super\-exponential unsustainable growth. We model this
universal pattern with the Log\-Periodic Power Law Singularity (LPPLS) model, which parsimoniously captures
diverse positive feedback phenomena, such as herding and imitation. The LPPLS model is shown to provide an
ex\-ante warning of market instabilities, quantifying a high crash hazard and probabilistic bracket of the crash
time consistent with the actual corrections; although, as always, the precise time and trigger (which straw breaks
the camel’s back) being exogenous and unpredictable. Looking forward, our analysis identifies a substantial but
not unprecedented overvaluation in the price of bitcoin, suggesting many months of volatile sideways bitcoin
prices ahead (from the time of writing, March 2018\).
Wolchover, N. (2018\). “Machine Learning’s ’Amazing’ Ability to Predict Chaos .” In:Quanta Magazine .
In new computer experiments, artificial\-intelligencealgorithms can tell the future of chaoticsystems. Researchers
have used machine learning to predict the chaotic evolution of a model flame front.
Wood, K., Giegerich, S., Roberts, S., and Zohren, S. (2022\). “Trading with the Momentum Transformer: An Intel\-
ligent and Interpretable Architecture .” In:arXiv e\-Print .
We introduce the Momentum Transformer, an attention\-based deep learning architecture which outperforms
benchmark momentum and mean\-reversion trading strategies. Unlike state\-of\-the\-art Long Short\-Term Memory
(LSTM) architectures, which are sequential in nature, the attention mechanism provides our architecture with
a direct connection to all previous time\-steps. Our architecture enables us to learn longer\-term dependencies,
improves performance when considering returns net of transaction costs and naturally adapts to new market
regimes, such as during the SARS\-CoV\-2 crisis. The Momentum Transformer is inherently interpretable, provid\-
ing us with greater insights into our deep learning momentum trading strategy, including how it blends different
classical strategies and the past time\-steps which are of the greatest significance to the model.
Wu, R. and Keogh, E. J. (2021\). “Current Time Series Anomaly Detection Benchmarks are Flawed and are Creating
the Illusion of Progress .” In:arXiv e\-Print .
Time series anomaly detection has been a perennially important topic in data science, with papers dating back
to the 1950s. However, in recent years there has been an explosion of interest in this topic, much of it driven by
the success of deep learning in other domains and for other time series tasks. Most of these papers test on one or
more of a handful of popular benchmark datasets, created by Yahoo, Numenta, NASA, etc. In this work we make
a surprising claim. The majority of the individual exemplars in these datasets suffer from one or more of four
flaws. Because of these four flaws, we believe that many published comparisons of anomaly detection algorithms
may be unreliable, and more importantly, much of the apparent progress in recent years may be illusionary. In
addition to demonstrating these claims, with this paper we introduce the UCR Time Series Anomaly Datasets.
72We believe that this resource will perform a similar role as the UCR Time Series Classification Archive, by
providing the community with a benchmark that allows meaningful comparisons between approaches and a
meaningful gauge of overall progress.
Wu, Y. (2020\). “On the Predictive Performance of the Stock Returns by Using the Markov\-Switching Models .”
MA thesis. University of Uppsala.
ThispaperproposesthebasicpredictiveregressionandMarkovRegime\-Switchingregressiontopredicttheexcess
stock returns in both US and Sweden stock markets. The analysis shows that the Markov Regime\-Switching
regression models out perform the linear ones in out\-of\-sample forecasting, which is due to the fact that the
regime\-switching models capture the economic expansion and recession better.
Yan, C. and Huang, K. X. D. (2020\). “Financial cycle and business cycle: An empirical analysis based on the data
from the U.S .” In:Economic Modelling 93, pp. 693–701\.
In this paper, we first study the relationship between the financial cycle and the business cycle in the time and
frequency domain. Then we also explore the interactions and dynamic mechanisms of the financial cycle, the
business cycle, real interest rate and exchange rate by the VAR model. The empirical results show that the
financial cycle is closely related to the business cycle, especially at medium\-term frequencies (8\-30 years), the
business cycle leads the financial cycle with a high positive correlation. However, the relationship between them
is not significant during the Great Moderation at business\-cycle (2\-4 years). In addition, the financial cycle not
only becomes a main driver of real interest rate, the financial cycle and the business cycle, but also serves as an
important source of the business cycle fluctuations. In general, our results lay some theoretical foundation for
the policy practice of financial and economic stability.
Yao, C.\-Z. and Li, H.\-Y. (2021\). “A study on the bursting point of Bitcoin based on the BSADF and LPPLS
methods.” In:The North American Journal of Economics and Finance (101280\).
We aim to reveal the characteristics and mechanism of the Bitcoin bubble in 2019\. First, we identify the period
during which two important Bitcoin bubbles occurred based on the generalized supremum augmented Dickey\-
Fuller (GSADF) method. There are two significant bubble cycles. The first bubble lasted approximately 26
days from November 25, 2017, to December 21, 2017, while the second bubble lasted approximately one week
from June 22 to June 29, 2019\. The occurrence of the first bubble was related to the considerable expansion
of initial coin offerings (ICOs) in 2017, while the formation of the second bubble was affected by the release of
Libra. Second, as the GSADF method cannot be used to accurately infer the time at which a bubble bursts,
we employ the log\-periodic power law singularity (LPPLS) model for this purpose. We verify that the LPPLS
method can not only infer the timing of a bubble burst but also shows stable results. Finally, we demonstrate
the implications of the 2019 bubble. During the 2019 bubble, due to the increased supervision of European and
American governments and the impact of hedging assets, the bubble’s duration was shorter, and the positive
feedback mechanism was not as strong as that of the 2017 bubble. In addition, the oscillating frequency of the
bubble in 2019 was low and unstable, which means that it would be more beneficial for investors to hold the
currency for a long time.
Zakamulin, V. (2020\). “Not All Bull and Bear Markets Are Alike: Insights From a Five\-State Hidden Semi\-Markov
Model.” In:SSRN e\-Print .
This paper employs the hidden semi\-Markov model and a novel model selection procedure to detect different
states in the US stock market. The empirical results suggest that the market is switching between five states
that can be classified into three bull states and two bear states. The three bull states are categorized as a low
volatility bull market, a high volatility bull market, and a stock market bubble. One of the bear states represents
a regular bear market, while the other one corresponds to either a stock market crash or a market correction. The
paper demonstrates that the five\-state model is consistent with a number of stylized facts and provides many
valuable insights into the dynamics of the US stock market. Besides, the five\-state model has clear implications
for the success of some active strategies that aim to enhance returns and reduce losses.
Zaremba, A., Czapkiewicz, A., and Kambouris, G. D. (2020\). “A Tale of Two States: An Application of a Markov
Switching Model to Anomaly Returns .” In:Eurasian Studies in Business and Economics . Springer International
Publishing, pp. 227–240\.
Thetime\-varyingprofitabilityofequityanomaliescallsforausefultooltoselectthewinninginvestmentstrategies
from the loser investment strategies. We offer a new framework for dynamic asset allocation across the anomalies
basedonaMarkovregimeswitchingmodel.UsingasampleofelevenequityanomaliesfromtheUSequitymarket
from the years 1963 to 2016 we demonstrate the predictability of their performance. The anomalies forecasted to
73be profitable significantly outperform the remaining anomalies by 0\.15\-0\.43% per month. The results are robust
to many considerations.
Zhang,Q.,Sornette,D.,Balcilar,M.,Gupta,R.,Ozdemir,Z.A.,andYetkiner,H.(2016\). “LPPLSbubbleindicators
over two centuries of the S\&P 500 index .” In:Physica A: Statistical Mechanics and its Applications 458, pp. 126–
139\.
Novel tests for early causal diagnostic of bubbles in the US S\&P 500 index. Large testing period of more than two
hundred years. Construction of efficient end\-of\-bubble signals. Horse\-race between LPPLS versus exponential
curve fitting and generalized sup ADF test approaches. Detection of eight positive bubbles and two negative
bubbles from January 1814 to August 2014\. The aim of this paper is to present novel tests for the early causal
diagnostic of positive and negative bubbles in the S\&P 500 index and the detection of End\-of\-Bubble signals
with their corresponding confidence levels. We use monthly S\&P 500 data covering the period from August 1791
to August 2014\. This study is the first work in the literature showing the possibility to develop reliable ex\-ante
diagnostics of the frequent regime shifts over two centuries of data. We show that the DS LPPLS (log\-periodic
power law singularity) approach successfully diagnoses positive and negative bubbles, constructs efficient End\-
of\-Bubble signals for all of the well\-documented bubbles, and obtains for the first time new statistical evidence
of bubbles for some other events. We also compare the DS LPPLS method to the exponential curve fitting
and the generalized sup ADF test approaches and find that DS LPPLS system is more accurate in identifying
well\-known bubble events, with significantly smaller numbers of false negatives and false positives.
Zhao, D. and Sornette, D. (2022\). “Bubbles for Fama from Sornette .” In:SSRN e\-Print .
Galvanized by the claims of Greenwood et al. in Bubbles for Fama that ”a sharp price increase of an industry
portfolio does not, on average, predict unusually low returns going forward”, and Fama’s quote (June, 2016\)
that ”Statistically, people have not come up with ways of identifying bubbles”, we present significant evidence to
the contrary of both statements. Using a methodology called logperiodic power law singularity (LPPLS), which
has been developed by the Sornette group over more than two decades, we show that a LPPLS\-based ”bubble
confidence indicator” allows one to diagnose ex\-ante the presence of a bubble. Using superposed epoch analysis,
we find an excellent timing performance of price regime shifts, and more so, the larger the bubble confidence
indicator. Moreover, we identify two classes of regime shifts following an accelerated price growth qualified
by LPPLS: (i) bubbles followed by a large drawdown or crash, and (ii) price catch\-up followed by a plateau,
associated with the convergence to a stable price level. Indiscriminately mixing these two types of accelerated
transient price increases may explain in part previous failures to diagnose bubbles and their aftermath. While the
existence of the first class of transient accelerated price increases followed by crashes is a long\-standing puzzle,
the existence of the second class of transient accelerated price increases followed by a plateau poses a challenge
to the efficient market hypothesis, thus constituting a new puzzle: the convergence to a stable price level, while
accelerating, is slow, with investors and the market taking weeks to months to digest available information and
to progressively converge to the final higher valuation consensus.
Zheng, K., Li, Y., and Xu, W. (2021\). “Regime switching model estimation: spectral clustering hidden Markov
model.” In:Annals of Operations Research 303(1\-2\), pp. 297–319\.
We propose a novel method for Markov regime switching (MRS) model estimations by spectral clustering hidden
Markov model (SC\-HMM). The proposed SC\-HMM exploits the Markov property of hidden states and utilizes
pairwise feature similarities for latent state identifications. It can be applied to general hidden Markov models
(HMMs) with continuous observations. In contrast to the maximum likelihood estimation (MLE), SC\-HMM
predicts latent states and yields conditional distribution statistics without knowledge of types of conditional
distributions. To illustrate, SC\-HMM is first applied to a simple HMM with discrete observations. We consider
the MRS model estimation with continuous observations to further demonstrate SC\-HMM. Specifically, based on
local observations, we propose a set of features for the MRS estimation. A similarity matrix is determined from
derived features and spectral clustering predicts latent states. Conditional distribution statistics and transitional
probabilities are estimated based on identified latent states. By conducting simulation studies on both two\-state
and three\-state MRS estimations, we demonstrate that, in comparison with MLE, the proposed SC\-HMM is
more robust. Furthermore, we demonstrate the validity of SC\-HMM by estimating a two\-state MRS from the
S\&P/TSX Composite Index daily and monthly data from 1977 to 2014\.
74