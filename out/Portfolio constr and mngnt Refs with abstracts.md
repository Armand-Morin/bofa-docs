References with abstracts for QWIMproject: Constructing and
managing portfolios in quantitative wealth and investment management
Cristian Homescu
December 2022
Abstract
This document includes the list of references (including abstracts) for this QWIM project
Contents
1 Motivation for the project 2
2 Relevant references 3
2\.1 Main references . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
2\.2 Comprehensive list of references . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
2\.2\.1 Covariances, correlations and volatilities: estimation, modeling, and analysis . . . . . . . . . 4
2\.2\.2 Regime\-based portfolio optimization . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
2\.2\.3 Robust portfolio optimization . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
2\.2\.4 Mean variance portfolio optimization . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
2\.2\.5 Black\-Literman portfolio optimization . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
2\.2\.6 Bayesian portfolio optimization . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
2\.2\.7 Effect of estimation error on portfolio optimization . . . . . . . . . . . . . . . . . . . . . . . . 10
2\.2\.8 Portfolio optimization based on risk budgeting . . . . . . . . . . . . . . . . . . . . . . . . . . 11
2\.2\.9 Regularized portfolio optimization . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
2\.2\.10 Taxation incorporated into portfolio optimization . . . . . . . . . . . . . . . . . . . . . . . . . 12
2\.2\.11 Network\-based and clustering\-based portfolio optimization . . . . . . . . . . . . . . . . . . . . 13
2\.2\.12 Machine learning for portfolio construction and portfolio management . . . . . . . . . . . . . 14
2\.2\.13 Scenario\-based portfolio optimization . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
2\.2\.14 Goals\-based portfolio optimization . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
2\.2\.15 Surveys and best practices in portfolio construction and management . . . . . . . . . . . . . 15
2\.2\.16 Other topics in portfolio construction and management . . . . . . . . . . . . . . . . . . . . . 16
2\.2\.17 Testing and comparison procedures for investment portfolios . . . . . . . . . . . . . . . . . . 16
2\.2\.18 Portfolio rebalancing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
2\.2\.19 Software packages and codes for portfolio optimization and management . . . . . . . . . . . . 18
References 19
11 Motivation for the project
While modern portfolio construction theory has a solid theoretical foundation (starting with groundbreaking arti\-
cles authrored by Markowitz), the practical application of this framework in the asset management industry has
been disappointing Yin et al. (“A practical guide to robust portfolio optimization,” 2021\) . The inputs (expected
returns and covariance matrix) for Mean Variance Optimization (MVO) need to be estimated, either statistically
from historical data or with a factor or valuation model. While uncertainty is present in both expected returns and
expected covariance matrix, although uncertainty in expected returns was found to be more significant than uncer\-
tainty in the covariance matrix for the sensitivity of the solution Yam et al. (“Optimal asset allocation: Risk and
information uncertainty,” 2016\) ,Chopra and Ziemba (“The Effect of Errors in Means, Variances, and Covariances
on Optimal Portfolio Choice,” 1993\) .
Yin et al. (“A practical guide to robust portfolio optimization,” 2021\) : The main problem of MVO is that it not
only fails to take into account the uncertainty in the estimation process of expected returns but also tends to amplify
them. In the portfolio optimization literature, a host of approaches have been proposed to mitigate the previously
mentioned drawbacks suffered by MVO. One approach, embodied by Bayesian shrinkage approaches, proposes using
a shrinkage estimator of the covariance matrix or expected returns. Another approach (see Jagannathan and Ma
(“Risk Reduction in Large Portfolios: Why Imposing the Wrong Constraints Helps,” 2003\) ,DeMiguel et al. (“A
generalized approach to portfolio optimization: Improving performance by constraining portfolio norms,” 2009\) )
tries to mitigate the drawbacks of MVO by adding constraints to the optimization problems. A third approach Yin
et al. (“A practical guide to robust portfolio optimization,” 2021\) uses robust optimization to take into account the
uncertainty in the optimization objective function without altering the inputs of the optimization.
Toaddressotherdrawbacksidentifiedduringpracticalconstructionandmanagementofoptimalportfolios, many
other approaches were considered in the literature, including:
•regime\-based portfolio optimization
•network\-based portfolio optimization
•clustering\-based portfolio optimization
•portfolio optimization based on risk budgeting
•Bayesian portfolio optimization
•scenario\-based portfolio optimization
•goals\-based portfolio optimization
•portfolio optimization based on machine learning
22 Relevant references
2\.1 Main references
List of references:
Al Janabi (“Is optimum always optimal? A revisit of the mean\-variance method under nonlinear measures of
dependence and non\-normal liquidity constraints,” 2021\)
Barroso and Saxena (“Lest we forget: Using Out\-Of\-Sample Errors in Portfolio Optimization,” 2022\)
Baz et al. (“A Framework for Constructing Equity\-Risk\-Mitigation Portfolios,” 2020\)
Choi et al. (“Alpha go everywhere: machine learning and international stock returns,” 2022\)
Ciliberti and Gualdi (“Portfolio Construction Matters,” 2020\)
Clemente et al. (“Asset allocation: new evidence through network approaches,” 2021\)
Cong et al. (“AlphaPortfolio: Direct Construction Through Deep Reinforcement Learning and Interpretable
AI,” 2022\)
Costa and Kwon (“A regime\-switching factor model for mean\-variance optimization,” 2020\)
Costa and Kwon (“Data\-driven distributionally robust risk parity portfolio optimization,” 2021\)
Das et al. (“Dynamic optimization for multi\-goals wealth management,” 2022\)
Das et al. (“Optimal Goals\-Based Investment Strategies For Switching Between Bull and Bear Markets,” 2022\)
De Nard et al. (“Factor Models for Portfolio Selection in Large Dimensions: The Good, the Better and the
Ugly,” 2021\)
De Nard and Zhao (“Using, Taming or Avoiding the Factor Zoo? A Double\-Shrinkage Estimator for Covariance
Matrices,” 2021\)
Denault and Simonato (“A note on a dynamic goal\-based wealth management problem,” 2022\)
Flint et al. (“Defining and measuring portfolio diversification,” 2021\)
Fusai et al. (“Equally Diversified or Equally Weighted?” 2020\)
Giudici et al. (“Network models to improve robot advisory portfolios,” 2022\)
Jaeger et al. (“Interpretable Machine Learning for Diversified Portfolio Construction,” 2021\)
Jaeger et al. (“Adaptive Seriational Risk Parity and other Extensions for Heuristic Portfolio Construction using
Machine Learning and Graph Theory,” 2021\)
Kelliher et al. (“A Novel Approach to Risk Parity: Diversification across Risk Factors and Market Regimes,”
2022\)
Kim et al. (“Personalized goal\-based investing via multi\-stage stochastic goal programming,” 2020\)
Kinlaw et al. (“The Myth of Diversification Reconsidered,” 2021\)
Kolm and Ritter (“Factor Investing with Black\-Litterman\-Bayes: Incorporating Factor Views and Priors in
Portfolio Construction,” 2021\)
Kritzman et al. ( Asset Allocation: From Theory to Practice and Beyond , 2021\)
Lezmi et al. (“Portfolio Allocation with Skewness Risk: A Practical Guide,” 2019\)
Li et al. (“Investable and Interpretable Machine Learning for Equities,” 2022\)
Li et al. (“Multi\-period portfolio optimization using model predictive control with mean\-variance and risk parity
frameworks,” 2022\)
Laur (“Portfolio Optimization \- Can Optimizing Portfolio Outperform Naive Diversification?” 2020\)
Lohre et al. (“Hierarchical Risk Parity: Accounting for Tail Dependencies in Multi\-asset Multi\-factor Alloca\-
tions,” 2020\)
Molyboga (“A Modified Hierarchical Risk Parity Framework for Portfolio Management,” 2020\)
Olmo (“Optimal portfolio allocation and asset centrality revisited,” 2021\)
Page and Panariello (“When Diversification Fails,” 2018\)
Papenbrock et al. (“Matrix Evolutions: Synthetic Correlations and Explainable Machine Learning for Con\-
structing Robust Investment Portfolios,” 2021\)
Pedersen et al. (“Enhanced Portfolio Optimization,” 2021\)
Perrin and Roncalli (“Machine Learning Optimization Algorithms \& Portfolio Allocation,” 2020\)
Roncalli (“Advanced Course in Asset Management,” 2021\)
Schwendner et al. (“Adaptive Seriational Risk Parity and Other Extensions for Heuristic Portfolio Construction
Using Machine Learning and Graph Theory,” 2021\)
Serur and Avellaneda (“Hierarchical PCA and Modeling Asset Correlations,” 2021\)
Snow (“Machine Learning in Asset Management \- Part 2: Portfolio Construction \- Weight Optimization,” 2020\)
3Uysal and Mulvey (“A Machine Learning Approach in Regime\-Switching Risk Parity Portfolios,” 2021\)
van Staden et al. (“The surprising robustness of dynamic Mean\-Variance portfolio optimization to model mis\-
specification errors,” 2021\)
Wang et al. (“Portfolio Selection in Goals\-Based Wealth Management,” 2011\)
Yin et al. (“A practical guide to robust portfolio optimization,” 2021\)
Zaimovic et al. (“How Many Stocks Are Sufficient for Equity Portfolio Diversification? A Review of the Litera\-
ture,” 2021\)
2\.2 Comprehensive list of references
2\.2\.1 Covariances, correlations and volatilities: estimation, modeling, and analysis
References:
Adams et al. (“Are correlations constant? Empirical and theoretical results on popular correlation models in
finance,” 2017\)
Agrawal et al. (“Covariance Matrix Estimation under Total Positivity for Portfolio Selection,” 2021\)
Albanese et al. (“A Comparative Analysis of Correlation Approaches in Finance,” 2013\)
Aldridge (“Big data in portfolio allocation: A new approach to successful portfolio optimization,” 2019\)
Avella\-Medina (“Robust Methods for High\-Dimensional Regression and Covariance Matrix Estimation,” 2020\)
Barroso and Saxena (“Lest we forget: Using Out\-Of\-Sample Errors in Portfolio Optimization,” 2022\)
Bartz (“Advances in high\-dimensional covariance matrix estimation,” 2016\)
Begusic and Kostanjcar (“Cluster\-Based Shrinkage of Correlation Matrices for Portfolio Optimization,” 2019\)
Benaych\-Georges et al. (“Optimal cleaning for singular values of cross\-covariance matrices,” 2021\)
Berger and Gencay (“Short\-run wavelet\-based covariance regimes for applied portfolio management,” 2020\)
Boileau et al. (“Cross\-Validated Loss\-Based Covariance Matrix Estimator Selection in High Dimensions,” 2021\)
Bollerslev et al. (“Risk Everywhere: Modeling and Managing Volatility,” 2018\)
Bongiorno and Challet (“Covariance matrix filtering with bootstrapped hierarchies,” 2020\)
Bongiorno and Challet (“Reactive Global Minimum Variance Portfolios with k\-BAHC covariance cleaning,”
2020\)
Bongiorno and Challet (“The Oracle estimator is suboptimal for global minimum variance portfolio optimisa\-
tion,” 2021\)
Bun et al. (“Cleaning large correlation matrices: Tools from Random Matrix Theory,” 2017\)
Chang (“Double shrinkage estimators for large sparse covariance matrices,” 2015\)
Choi et al. (“High\-dimensional Markowitz portfolio optimization problem: empirical comparison of covariance
matrix estimators,” 2019\)
Clements and Doolan (“Combining multivariate volatility forecasts using weighted losses,” 2020\)
Coqueret and Milhau (“Estimating Covariance Matrices for Portfolio Optimisation,” 2014\)
Deshmukh and Dubey (“Improved Covariance Matrix Estimation With an Application in Portfolio Optimiza\-
tion,” 2020\)
DeMiguel et al. (“Size matters: Optimal calibration of shrinkage estimators for portfolio selection,” 2013\)
De Nard (“Oops! I Shrunk the Sample Covariance Matrix Again: Blockbuster Meets Shrinkage,” 2020\)
De Nard et al. (“Factor Models for Portfolio Selection in Large Dimensions: The Good, the Better and the
Ugly,” 2021\)
De Nard and Zhao (“Using, Taming or Avoiding the Factor Zoo? A Double\-Shrinkage Estimator for Covariance
Matrices,” 2021\)
De Nard et al. (“Subsampled factor models for asset pricing: the rise of VASA,” 2020\)
Dey and Stephens (“CorShrink : Empirical Bayes shrinkage estimation of correlations, with applications,” 2018\)
Ding and Zhou (“Estimation and inference for precision matrices of nonstationary time series,” 2020\)
Ehling and Heyerdahl\-Larsen (“Correlations,” 2017\)
Engle et al. (“Large Dynamic Covariance Matrices,” 2019\)
Fan et al. (“Precision Matrix Estimation with Noisy and Missing Data,” 2019\)
Bernardi et al. (“Volatility Forecasting in a Data Rich Environment,” 2020\)
Fan et al. (“An overview of the estimation of large covariance and precision matrices,” 2016\)
Gortz and Yeromonahos (“Asymmetries in Risk Premia, Macroeconomic Uncertainty and Business Cycles,”
2019\)
4Harutyunyan et al. (“Efficient Covariance Estimation from Temporal Data,” 2021\)
Higham et al. (“Restoring Definiteness via Shrinking, with an Application to Correlation Matrices with a Fixed
Block,” 2016\)
Huang and Yu (“A new procedure for resampled portfolio with shrinkaged covariance matrix,” 2020\)
Husmann et al. (“Cross\-validated covariance estimators for high\-dimensional minimum\-variance portfolios,”
2020\)
Jain and Jain (“Can Machine Learning\-Based Portfolios Outperform Traditional Risk\-Based Portfolios? The
Need to Account for Covariance Misspecification,” 2019\)
Jay et al. (“Robust Covariance Matrix Estimation and Portfolio Allocation: The Case of Non\-Homogeneous
Assets,” 2020\)
Jay et al. (“Improving portfolios global performance using a cleaned and robust covariance matrix estimate,”
2020\)
Ke et al. (“User\-Friendly Covariance Estimation for Heavy\-Tailed Distributions,” 2019\)
Ke et al. (“High\-Dimensional Dynamic Covariance Matrices With Homogeneous Structure,” 2021\)
Lam (“High\-dimensional covariance matrix estimation,” 2020\)
Lancewicki and Aladjem (“Multi\-Target Shrinkage Estimation for Covariance Matrices,” 2014\)
Ledoit and Wolf (“Nonlinear Shrinkage of the Covariance Matrix for Portfolio Selection: Markowitz Meets
Goldilocks,” 2017\)
Ledoit and Wolf ( Shrinkage Estimation of Large Covariance Matrices: Keep it Simple, Statistician? 2020\)
Ledoit and Wolf (“Analytical nonlinear shrinkage of large\-dimensional covariance matrices,” 2020\)
LedoitandWolf(“ThePowerof(Non\-)LinearShrinking: AReviewandGuidetoCovarianceMatrixEstimation,”
2022\)
Li and Zakamulin (“The term structure of volatility predictability,” 2019\)
Li and Zakamulin (“Stock volatility predictability in bull and bear markets,” 2020\)
Ma et al. (“Volatility forecasting: long memory, regime switching and heteroscedasticity,” 2019\)
Marti et al. (“A review of two decades of correlations, hierarchies, networks and clustering in financial markets,”
2020\)
Molstad and Rothman (“Shrinking characteristics of precision matrix estimators,” 2018\)
Mouraetal.(“Comparinghigh\-dimensionalconditionalcovariancematrices: Implicationsforportfolioselection,”
2020\)
Munro and Bradfield (“Putting the squeeze on the sample covariance matrix for portfolio construction,” 2016\)
Ng et al. (“Comparison of several covariance matrix estimators for portfolio optimization,” 2011\)
Nguyen et al. (“The memory of stock return volatility: Asset pricing implications,” 2020\)
Packham and Woebbeking (“Correlation scenarios and correlation stress testing,” 2021\)
Pantaleo et al. (“When do improved covariance matrix estimators enhance portfolio optimization? An empirical
comparative study of nine estimators,” 2011\)
Pollak (“Covariance estimation and related problems in portfolio optimization,” 2012\)
Posch and Ullmann (“Estimation of Large Correlation Matrix with Shrinking Methods,” 2016\)
Reinikainen (“Strategic Asset Allocation Using Robust Covariance Estimation and PortfolioOptimization Meth\-
ods,” 2020\)
Schadner (“Feasible Implied Correlation Matrices from Factor Structures,” 2021\)
Senneret et al. (“Covariance versus Precision Matrix Estimation for Efficient Asset Allocation,” 2016\)
Shaik and Maheswaran (“A new unbiased additive robust volatility estimation using extreme values of asset
prices,” 2020\)
Shin (“Forecasting realized volatility: A review,” 2018\)
Simon and Turkay (“Hunting high and low: visualising shifting correlations in financial markets,” 2018\)
Su (“Volatility of S\&P500: Estimation and Evaluation,” 2021\)
Sun et al. (“Improved covariance matrix estimation for portfolio risk measurement: A review,” 2019\)
Tchernister and Rubisov (“Robust estimation of historical volatility and correlations in risk management,” 2009\)
Tong et al. (“Tuning the Parameters for Precision Matrix Estimation Using Regression Analysis,” 2019\)
Tran et al. (“Voting shrinkage algorithm for Covariance Matrix Estimation and its application to portfolio
selection,” 2020\)
Trucios et al. (“On the robustness of the principal volatility components,” 2019\)
5Wang et al. (“Volatility forecasting revisited using Markov\-switching with time\-varying probability transition,”
2022\)
Watagoda and Olive (“Comparing six shrinkage estimators with large sample theory and asymptotically optimal
prediction intervals,” 2021\)
Yuan and Yuan (“A Monte Carlo synthetic sample based performance evaluation method for covariance matrix
estimators,” 2021\)
Zakamulin (“A Test of Covariance\-Matrix Forecasting Methods,” 2015\)
Zitelli (“Random matrix models for datasets with fixed time horizons,” 2020\)
2\.2\.2 Regime\-based portfolio optimization
References:
Ahmad et al. (“Regime dependent dynamics and European stock markets: Is asset allocation really possible?”
2015\)
Bae et al. (“Dynamic asset allocation for varied financial markets under regime switching framework,” 2014\)
Berger and Gencay (“Short\-run wavelet\-based covariance regimes for applied portfolio management,” 2020\)
Blin et al. (“A Macro Risk\-Based Approach to Alternative Risk Premia Allocation,” 2017\)
Briere and Signori (“Inflation\-Hedging Portfolios: Economic Regimes Matter,” 2012\)
Costa and Kwon (“Risk parity portfolio optimization under a Markov regime\-switching framework,” 2019\)
Costa and Kwon (“A regime\-switching factor model for mean\-variance optimization,” 2020\)
Dai et al. (“Robo\-advising: a dynamic mean\-variance approach,” 2021\)
Flint and Mare (“Regime\-Based Tactical Allocation for Equity Factors and Balanced Portfolios,” 2019\)
Fons et al. (“A novel dynamic asset allocation system using Feature Saliency Hidden Markov models for smart
beta investing,” 2021\)
GuidolinandHyde(“Linearpredictabilityvs. bullandbearmarketmodelsinstrategicassetallocationdecisions:
evidence from UK data,” 2014\)
Hu et al. (“Mean variance asset liability management with regime switching,” 2022\)
Kelliher et al. (“A Novel Approach to Risk Parity: Diversification across Risk Factors and Market Regimes,”
2022\)
Kritzman et al. (“Regime Shifts: Implications for Dynamic Strategies,” 2012\)
Kaya (“Managing ambiguity in asset allocation,” 2017\)
Lezmi et al. (“Portfolio Allocation with Skewness Risk: A Practical Guide,” 2019\)
Li and Mulvey (“Portfolio Optimization Under Regime Switching and Transaction Costs: Combining Neural
Networks and Dynamic Programs,” 2021\)
Liszewski (“Asset allocation under multiple regimes,” 2016\)
Nystrup et al. (“Dynamic portfolio optimization across hidden market regimes,” 2018\)
Nystrup et al. (“Regime\-Based Versus Static Asset Allocation: Letting the Data Speak,” 2015\)
Nystrup et al. (“Dynamic Allocation or Diversification: A Regime\-Based Approach to Multiple Assets,” 2018\)
Oliveira and Valls Pereira (“Asset Allocation With Markovian Regime Switching: Efficient Frontier and Tangent
Portfolio With Regime Switching,” 2018\)
Oprisor and Kwon (“Multi\-Period Portfolio Optimization with Investor Views under Regime Switching,” 2021\)
Sheikh and Sun (“Regime Change: Implications of Macroeconomic Shifts on Asset Class and Portfolio Perfor\-
mance,” 2012\)
Uysal and Mulvey (“A Machine Learning Approach in Regime\-Switching Risk Parity Portfolios,” 2021\)
2\.2\.3 Robust portfolio optimization
References:
Bardakci and Lagoa (“Distributionally Robust Portfolio Optimization,” 2019\)
Bertsimas et al. (“Theory and Applications of Robust Optimization,” 2011\)
Cajas (“Robust Portfolio Selection with Near Optimal Centering,” 2019\)
Costa and Kwon (“Data\-driven distributionally robust risk parity portfolio optimization,” 2021\)
Darolles et al. (“Robust Portfolio Allocation with Systematic Risk Contribution Restrictions,” 2015\)
DeMiguel and Nogales (“Portfolio Selection with Robust Estimation,” 2009\)
Ding et al. (“Robust mean variance optimization problem under Renyi divergence information,” 2018\)
6Fabozzi et al. (“Robust Portfolio: Optimization and Management,” 2012\)
Gabrel et al. (“Recent advances in robust optimization: An overview,” 2014\)
Geelen (“Optimization in an uncertain world \- The impact of uncertainty on portfolio allocation,” 2020\)
Georgantas (“Robust Optimization Approaches for Portfolio Selection: A Computational and Comparative
Analysis,” 2020\)
Ghahtarani et al. (“Robust Portfolio Selection Problems: A Comprehensive Review,” 2022\)
Gotoh et al. (“Robust empirical optimization is almost the same as mean\-variance optimization,” 2018\)
Guastaroba et al. (“Investigating the effectiveness of robust portfolio optimization techniques,” 2011\)
Gulliksson and Mazur (“An Iterative Approach to Ill\-Conditioned Optimal Portfolio Selection,” 2020\)
Han and Li (“Robust Portfolio Selection Using Vine Copulas,” 2020\)
Heckel et al. (“Insights into robust optimization: decomposing into mean\-variance and risk\-based portfolios,”
2016\)
Kakouris and Rustem (“Robust portfolio optimization with copulas,” 2014\)
Kapsos et al. (“Robust risk budgeting,” 2018\)
Kim et al. (“Deciphering robust portfolios,” 2014\)
Kim et al. (“What do robust equity portfolio models really do?” 2013\)
Kim et al. (“Robust equity portfolio performance,” 2018\)
Kim et al. (“Recent advancements in robust optimization for investment management,” 2018\)
Kolm et al. (“60 Years of portfolio optimization: Practical challenges and current trends,” 2014\)
Langlois (“A New Benchmark for Dynamic Mean\-Variance Portfolio Allocations,” 2020\)
Lee et al. (“Sparse and robust portfolio selection via semi\-definite relaxation,” 2020\)
Leyffer et al. (“A survey of nonlinear robust optimization,” 2020\)
Lopez de Prado (“A robust estimator of the efficient frontier,” 2020\)
Marandi et al. (“Extending the Scope of Robust Quadratic Optimization,” 2019\)
Martin et al. (“Robust portfolio construction,” 2010\)
Oberoi et al. (“Can robust optimization offer improved portfolio performance? An empirical study of Indian
market,” 2019\)
Pandolfo et al. (“Robust mean\-variance portfolio through the weighted Lp depth function,” 2020\)
Pedersen et al. (“Enhanced Portfolio Optimization,” 2021\)
Perchetetal.(“InsightsintoRobustPortfolioOptimization: DecomposingRobustPortfoliosintoMean\-Variance
and Risk\-Based Portfolios,” 2015\)
Pinar (“On robust mean\-variance portfolios,” 2016\)
Plachel (“A unified model for regularized and robust portfolio optimization,” 2019\)
Reinikainen (“Strategic Asset Allocation Using Robust Covariance Estimation and PortfolioOptimization Meth\-
ods,” 2020\)
Scherer (“Can robust portfolio optimisation help to build better portfolios?” 2007\)
Schussler (“Robust Dynamic Portfolio Choice Based on Out\-Of\-Sample Performance,” 2019\)
Simoes (“Robust portfolio optimisation with filtering uncertainty,” 2017\)
Simoes et al. (“Relative Robust Portfolio Optimization with benchmark regret,” 2018\)
Simonian (“Causal Uncertainty in Capital Markets: A Robust Noisy\-Or Framework for Portfolio Management,”
2021\)
Supandi et al. (“An empirical comparison between robust estimation and robust optimization to mean\-variance
portfolio,” 2017\)
Toma and Leoni\-Aubin (“Robust Portfolio Optimization Using Pseudodistances,” 2015\)
van Pelt (“Constructing Robust Portfolios, the Role of Parameter Uncertainty in Dynamic Optimal Portfolio
Allocations,” 2020\)
Xidonas et al. (“Robust portfolio optimization: a categorized bibliographic review,” 2020\)
Yin et al. (“A practical guide to robust portfolio optimization,” 2021\)
Yu (“Comparing Classical Portfolio Optimization and Robust Portfolio Optimization on Black Swan Events,”
2021\)
Zhao (“Essays on data\-driven optimization,” 2019\)
72\.2\.4 Mean variance portfolio optimization
References:
Al Janabi (“Is optimum always optimal? A revisit of the mean\-variance method under nonlinear measures of
dependence and non\-normal liquidity constraints,” 2021\)
Allen et al. (“In defense of portfolio optimization: what if we can forecast?” 2019\)
Bauderetal.(“Bayesianmean\-varianceanalysis: optimalportfolioselectionunderparameteruncertainty,” 2021\)
Becker et al. (“Markowitz versus Michaud: portfolio optimization strategies reconsidered,” 2015\)
Bessler et al. (“Multi\-asset portfolio optimization and out\-of\-sample performance: an evaluation of Black Lit\-
terman, mean\-variance, and naive diversification approaches,” 2017\)
Bielstein and Hanauer (“Mean\-variance optimization using forward\-looking return estimates,” 2019\)
Brodie et al. (“Sparse and Stable Markowitz Portfolios,” 2009\)
Butler and Kwon (“Integrating Prediction in Mean\-Variance Portfolio Optimization,” 2021\)
Butler and Kwon (“Data\-driven integration of regularized mean\-variance portfolios,” 2021\)
Cai and Schmidt (“Comparing mean\-variance portfolios and equal\-weight portfolios for major US equity in\-
dexes,” 2020\)
Choi et al. (“High\-dimensional Markowitz portfolio optimization problem: empirical comparison of covariance
matrix estimators,” 2019\)
Chopra and Ziemba (“The Effect of Errors in Means, Variances, and Covariances on Optimal Portfolio Choice,”
1993\)
Dai and Wang (“Sparse and robust mean\-variance portfolio optimization problems,” 2019\)
Forsyth and Vetzal (“Dynamic mean variance asset allocation: Tests for robustness,” 2017\)
Hu et al. (“Mean variance asset liability management with regime switching,” 2022\)
Hurley and Brimberg (“A note on the sensitivity of the strategic asset allocation problem,” 2015\)
Jagannathan and Ma (“Risk Reduction in Large Portfolios: Why Imposing the Wrong Constraints Helps,” 2003\)
Kalayci et al. (“A comprehensive review of deterministic models and applications for mean\-variance portfolio
optimization,” 2019\)
Kim et al. (“Mean\-Variance Optimization for Asset Allocation,” 2021\)
Kritzman (“The graceful aging of mean variance optimization,” 2011\)
Kritzman et al. ( A Practitioner’s Guide to Asset Allocation , 2017\)
Kolm et al. (“60 Years of portfolio optimization: Practical challenges and current trends,” 2014\)
Lai et al. (“Mean variance portfolio optimization when means and covariances are unknown,” 2011\)
Langlois (“A New Benchmark for Dynamic Mean\-Variance Portfolio Allocations,” 2020\)
Lassance (“Reconciling mean\-variance portfolio theory with non\-Gaussian returns,” 2022\)
Li et al. (“Multi\-period portfolio optimization using model predictive control with mean\-variance and risk parity
frameworks,” 2022\)
Low et al. (“Enhancing mean\-variance portfolio selection by modeling distributional asymmetries,” 2016\)
Marakbi (“Mean\-Variance Portfolio Optimization: Challenging the role of traditional covariance estimation,”
2017\)
Markowitz (“Portfolio Theory: As I Still See It,” 2010\)
Messica (“Loopholes in Modern Portfolio Theory,” 2018\)
Pandolfo et al. (“Robust mean\-variance portfolio through the weighted Lp depth function,” 2020\)
Paskaramoorthy et al. (“The efficient frontiers of mean\-variance portfolio rules under distribution misspecifica\-
tion,” 2021\)
Pedersen et al. (“Enhanced Portfolio Optimization,” 2020\)
Platanakis et al. (“Horses for Courses: Mean\-Variance for Asset Allocation and 1/N for Stock Selection,” 2021\)
Rigamonti (“Mean\-Variance Optimization Is a Good Choice, But for Other Reasons than You Might Think,”
2020\)
Schuhmacher et al. (“Justifying Mean\-Variance Portfolio Selection when Asset Returns Are Skewed,” 2021\)
Supandi et al. (“An empirical comparison between robust estimation and robust optimization to mean\-variance
portfolio,” 2017\)
Van Staden (“Numerical methods for mean\-risk portfolio optimization,” 2020\)
van Staden et al. (“On the Distribution of Terminal Wealth under Dynamic Mean\-Variance Optimal Investment
Strategies,” 2021\)
8van Staden et al. (“The surprising robustness of dynamic Mean\-Variance portfolio optimization to model mis\-
specification errors,” 2021\)
Wang and Zhou (“Continuous\-time mean\-variance portfolio selection: A reinforcement learning framework,”
2020\)
Zhang et al. (“Portfolio selection problems with Markowitz mean\-variance framework: a review of literature,”
2018\)
Zhou et al. (“Incorporating time\-varying jump intensities in the mean\-variance portfolio decisions,” 2020\)
Zumbach (“Stochastic regularization for the mean\-variance allocation scheme,” 2019\)
2\.2\.5 Black\-Literman portfolio optimization
References:
Allaj (“The Black\-Litterman model and views from a reverse optimization procedure: an out\-of\-sample perfor\-
mance evaluation,” 2020\)
Bessler et al. (“Multi\-asset portfolio optimization and out\-of\-sample performance: an evaluation of Black Lit\-
terman, mean\-variance, and naive diversification approaches,” 2017\)
Chincarini and Kim (“Uses and Misuses of the Black\-Litterman Model in Portfolio Construction,” 2012\)
Cheung (“The Black Litterman model explained,” 2010\)
Chen and Lim (“A Generalized Black\-Litterman Model,” 2020\)
Cooper and Molyboga (“Black\-Litterman, exotic beta and varying efficient portfolios: an integrated approach,”
2017\)
Fischer and Murg (“A combined regime\-switching and Black Litterman model for optimal asset allocation,”
2015\)
Fuhrer and Hock (“Uncertainty in the Black\-Litterman model: A practical note,” 2019\)
Giacometti et al. (“Stable distributions in the Black Litterman approach to asset allocation,” 2007\)
Geyer and Lucivjanska (“The Black\-Litterman Approach and Views from Predictive Regressions: Theory and
Implementation,” 2016\)
Harris et al. (“The dynamic Black\-Litterman approach to asset allocation,” 2017\)
Kocuk and Cornuejols (“Incorporating Black\-Litterman views in portfolio construction when stock returns are
a mixture of normals,” 2020\)
Kolm and Ritter (“On the Bayesian interpretation of Black\-Litterman,” 2017\)
Lin et al. (“A Heteroskedastic Black\-Litterman Portfolio Optimization Model with Views Derived from a Pre\-
dictive Regression,” 2020\)
Martin and Sankaran (“Using the Black\-Litterman Model: A View on Opinions,” 2019\)
Meucci (“Enhancing the Black Litterman and related approaches: Views and stress\-test on risk factors,” 2009\)
Meyer\-Bullerdiek (“Out\-of\-sample performance of the Black\-Litterman model,” 2021\)
O’Toole (“The Black Litterman model: A risk budgeting perspective,” 2013\)
Sahamkhadam et al. (“Copula\-Based Black\-Litterman Portfolio Optimization,” 2020\)
Schepel (“Bayesian Extensions of the Black\-Litterman Model,” 2019\)
Subekti et al. (“Combining Black\-Litterman model with clustering on portfolio construction,” 2019\)
van der Schans and Steehouwer (“Time\-Dependent Black\-Litterman,” 2016\)
Walters (“The Black\-Litterman Model in Detail,” 2014\)
Xiao and Valdez (“A Black\-Litterman asset allocation model under Elliptical distributions,” 2015\)
2\.2\.6 Bayesian portfolio optimization
References:
Anderson and Cheng (“Robust Bayesian Portfolio Choices,” 2016\)
Andrei and Hsu (“Bayesian Alternatives to the Black\-Litterman Model,” 2018\)
Bade et al. (“A general approach to Bayesian portfolio optimization,” 2009\)
Bauderetal.(“Bayesianmean\-varianceanalysis: optimalportfolioselectionunderparameteruncertainty,” 2021\)
Bessler et al. (“Hedge Funds and Optimal Asset Allocation: Bayesian Expectations, Time\-Varying Investment
Opportunities and Mean\-Variance Spanning,” 2011\)
Bodnar et al. (“Bayesian estimation of the global minimum variance portfolio,” 2017\)
Carvalho et al. (“Optimal Asset Allocation with Multivariate Bayesian Dynamic Linear Models,” 2018\)
9Croessmann (“Gaussian process priors for Bayesian portfolio selection,” 2018\)
De Franco et al. (“Bayesian learning for the Markowitz portfolio selection problem,” 2018\)
De Franco et al. (“Dealing with Drift Uncertainty: A Bayesian Learning Approach,” 2019\)
Kolm and Ritter (“Factor Investing with Black\-Litterman\-Bayes: Incorporating Factor Views and Priors in
Portfolio Construction,” 2021\)
Meucci (“Robust Bayesian allocation,” 2014\)
Vamvakas (“Fixed income portfolio construction: a Bayesian approach for the allocation of risk factors,” 2015\)
Singh (“Bayesian Dynamic Interactions and Predictions: U.S., BRIC, and Frontier Equity Markets,” 2018\)
Sokolov and Polson (“Strategic Bayesian Asset Allocation,” 2019\)
Xing et al. (“Discovering Bayesian Market Views for Intelligent Asset Allocation,” 2018\)
2\.2\.7 Effect of estimation error on portfolio optimization
References:
Barroso and Saxena (“Lest we forget: Using Out\-Of\-Sample Errors in Portfolio Optimization,” 2022\)
Becker et al. (“Markowitz versus Michaud: portfolio optimization strategies reconsidered,” 2015\)
Bjerring et al. (“Feature selection for portfolio optimization,” 2017\)
Baz et al. (“A Framework for Constructing Equity\-Risk\-Mitigation Portfolios,” 2020\)
Chen and Yuan (“Efficient Portfolio Selection in a Large Market,” 2016\)
Chopra and Ziemba (“The Effect of Errors in Means, Variances, and Covariances on Optimal Portfolio Choice,”
1993\)
DeMiguel and Nogales (“Portfolio Selection with Robust Estimation,” 2009\)
du Plessis and van Rensburg (“Risk\-based portfolio sensitivity to covariance estimation,” 2020\)
Fuss et al. (“Diversifying Estimation Errors: An Efficient Averaging Rule for Portfolio Optimization,” 2021\)
Hurley and Brimberg (“A note on the sensitivity of the strategic asset allocation problem,” 2015\)
Jain and Jain (“Can Machine Learning\-Based Portfolios Outperform Traditional Risk\-Based Portfolios? The
Need to Account for Covariance Misspecification,” 2019\)
Kalyagin and Slashchinin (“Impact of error in parameter estimations on large scale portfolio optimization,”
2019\)
Kim and Kim (“Reduction of estimation error impact in the risk parity strategies,” 2021\)
Kinn (“Reducing Estimation Risk in Mean\-Variance Portfolios with Machine Learning,” 2018\)
Kritzman and Turkington (“Stability\-Adjusted Portfolios,” 2016\)
Kritzman et al. ( A Practitioner’s Guide to Asset Allocation , 2017\)
Lopez de Prado (“A robust estimator of the efficient frontier,” 2020\)
Mandigers (“Portfolio Performance With High\-Dimensional Inverse Covariance Matrix,” 2020\)
Michaud (“Comment on: Kritzman, M. 2006, ’are optimizers error maximizers?”’ 2019\)
Michaud and Michaud (“Estimation Error and Portfolio Optimization: A Resampling Solution,” 2015\)
Michaud et al. (“Estimation error and the fundamental law of active management: is quant fundamentally
flawed?” 2020\)
Michaud et al. (“Comment: Allen, D., C. Lizieri, S. Satchell 2019\. ’In Defense of Portfolio Optimization: What
If We Can Forecast?”’ 2020\)
Paskaramoorthy et al. (“The efficient frontiers of mean\-variance portfolio rules under distribution misspecifica\-
tion,” 2021\)
Pedersen et al. (“Enhanced Portfolio Optimization,” 2020\)
Santos (“Disentangling the role of variance and covariance information in portfolio selection problems,” 2019\)
Simaan et al. (“Estimation error in mean returns and the mean\-variance efficient frontier,” 2018\)
Stivers and Sun (“Mitigating Estimation Risk in Asset Allocation: Diagonal Models Versus 1/N Diversification,”
2016\)
Supandi et al. (“An empirical comparison between robust estimation and robust optimization to mean\-variance
portfolio,” 2017\)
van Staden et al. (“The surprising robustness of dynamic Mean\-Variance portfolio optimization to model mis\-
specification errors,” 2021\)
Zhao et al. (“Portfolio Construction by Mitigating Error Amplification: The Bounded\-Noise Portfolio,” 2019\)
102\.2\.8 Portfolio optimization based on risk budgeting
References:
Alankar et al. (“An Introduction to Tail Risk Parity: Balancing Risk to Achieve Downside Protection,” 2013\)
Alkafri and Frey (“Shrinkage Estimation in Risk Parity Portfolios,” 2022\)
Alonso and Qian (“Risk Parity Equity Strategy with Flexible Risk Targets,” 2013\)
Bai et al. (“Least\-squares approach to risk parity in portfolio selection,” 2016\)
Baitinger et al. (“Extending the Risk Parity Approach to Higher Moments: Is There Any Value Added?” 2017\)
Bechis (“Machine Learning Portfolio Optimization: Hierarchical Risk Parity and Modern Portfolio Theory,”
2020\)
Bellini et al. (“Risk Parity with Expectiles,” 2021\)
Benichou et al. (“Agnostic risk parity: taming known and unknown unknowns,” 2017\)
Bernardi et al. (“Second\-order risk of alternative risk parity strategies,” 2019\)
Bhansali et al. (“The Risk in Risk Parity: A Factor\-Based Analysis of Asset\-Based Risk Parity,” 2012\)
Bruder and Roncalli (“Managing Risk Exposures Using the Risk Budgeting Approach,” 2012\)
Burggraf(“Beyondriskparity\-Amachinelearning\-basedhierarchicalriskparityapproachoncryptocurrencies,”
2020\)
Cesarone and Tardella (“Equal Risk Bounding is better than Risk Parity for portfolio selection,” 2017\)
Chakravorty et al. (“Active Risk Budgeting is better than the Tangency Portfolio,” 2019\)
Choi et al. (“Alpha go everywhere: machine learning and international stock returns,” 2022\)
Costa and Kwon (“Risk parity portfolio optimization under a Markov regime\-switching framework,” 2019\)
Costa and Kwon (“A robust framework for risk parity portfolios,” 2020\)
Costa and Kwon (“Generalized Risk Parity Portfolio Optimization: An ADMM Approach,” 2020\)
de Carvalho et al. (“Multi\-Alpha Equity Portfolios: An Integrated Risk Budgeting Approach for Robust Con\-
strained Portfolios,” 2014\)
Fabozzi et al. (“Risk Parity: The Democratization of Risk in Asset Allocation,” 2021\)
Feng and Palomar (“Portfolio optimization with asset selection and risk parity control,” 2016\)
Fernandes et al. (“Saving Markowitz: A Risk Parity Approach Based on the Cauchy Interlacing Theorem,”
2020\)
Flint and du Plooy (“Extending risk budgeting for market regimes and quantile factor models,” 2018\)
Haesen et al. (“Enhancing Risk Parity by Including Views,” 2017\)
Haugh et al. (“A generalized risk budgeting approach to portfolio construction,” 2017\)
Husmann et al. (“Sparsity and Stability for Minimum\-Variance Portfolios,” 2019\)
Jacobsen and Lee (“Risk Parity Optimality Even with Negative Sharpe Ratio Assets,” 2020\)
Jurczenko and Teiletche (“Expected Shortfall Asset Allocation: A Multi\-Dimensional Risk Budgeting Frame\-
work,” 2019\)
Kaya and Lee (“Risk Parity: Common Fallacies,” 2014\)
Kelliher et al. (“A Novel Approach to Risk Parity: Diversification across Risk Factors and Market Regimes,”
2022\)
Kim and Kim (“Reduction of estimation error impact in the risk parity strategies,” 2021\)
Li et al. (“Multi\-period portfolio optimization using model predictive control with mean\-variance and risk parity
frameworks,” 2022\)
Lohre et al. (“Hierarchical Risk Parity: Accounting for Tail Dependencies in Multi\-asset Multi\-factor Alloca\-
tions,” 2020\)
Martellinietal.(“TowardConditionalRiskParity: ImprovingRiskBudgetingTechniquesinChangingEconomic
Environments,” 2015\)
Meucci et al. (“Risk budgeting and diversification based on optimised uncorrelated factors,” 2015\)
Molyboga (“A Modified Hierarchical Risk Parity Framework for Portfolio Management,” 2020\)
Perchet et al. (“Inter\-temporal risk parity: a constant volatility framework for factor investing,” 2014\)
Qian (“Are Risk\-Parity Managers at Risk Parity?” 2013\)
Richard and Roncalli (“Constrained Risk Budgeting Portfolios: Theory, Algorithms, Applications and Puzzles,”
2019\)
Rudin et al. (“Adaptive optimal risk budgeting,” 2020\)
Scherer ( Portfolio Construction and Risk Budgeting (Fifth Edition) , 2015\)
Shah and Parikh (“Does the number of holdings in a risk parity portfolio matter?” 2019\)
11Stagnol (“The Risk Parity Principle Applied to a Corporate Bond Index,” 2017\)
Uysal (“Risk Budgeting Portfolios Under a Modern Optimization and Machine Learning Lens,” 2021\)
Uysal and Mulvey (“A Machine Learning Approach in Regime\-Switching Risk Parity Portfolios,” 2021\)
Yam et al. (“Optimal asset allocation: Risk and information uncertainty,” 2016\)
Wu et al. (“General sparse risk parity portfolio design via successive convex optimization,” 2020\)
2\.2\.9 Regularized portfolio optimization
References:
Aldridge (“Big data in portfolio allocation: A new approach to successful portfolio optimization,” 2019\)
Bruder et al. (“Regularization of Portfolio Allocation,” 2016\)
Caccioli et al. (“Lp regularized portfolio optimization,” 2014\)
Lioui (“Understanding Regularization for Portfolio Construction,” 2021\)
Pagnoncelli et al. (“The effect of regularization in portfolio selection problems,” 2021\)
Plachel (“A unified model for regularized and robust portfolio optimization,” 2019\)
2\.2\.10 Taxation incorporated into portfolio optimization
References:
Aked et al. (“Tactical and Tax Aware GTAA,” 2019\)
Anastasov (“Tax\-efficient asset management via loss harvesting,” 2017\)
Arnott et al. (“Is Your Alpha Big Enough to Cover Its Taxes? A Quarter\-Century Retrospective,” 2018\)
Arnott et al. (“The management and mismanagement of taxable assets,” 2001\)
Aw et al. (“The art of losing in investing: harvesting tax losses for a positive impact,” 2018\)
Blay and Markowitz (“Tax\-Cognizant Portfolio Analysis: A Methodology for Maximizing After\-Tax Wealth,”
2016\)
Chaudhuri et al. (“An Empirical Evaluation of Tax\-Loss Harvesting Alpha,” 2020\)
Davis et al. (“The Efficient Frontier and International Portfolio Diversification in Taxable and Tax\-Privileged
Accounts,” 2020\)
DiLellio and Ostrov ( Constructing Tax Efficient Withdrawal Strategies for Retirees , 2018\)
Domian et al. (“Is Your Tax\-Managed Fund Manager Hiding in the Closet?” 2015\)
Fischer and Gallmeyer (“Taxable and Tax\-Deferred Investing with the Limited Use of Losses,” 2017\)
Haugh et al. (“Tax\-Aware Dynamic Asset Allocation,” 2016\)
Horan and Adler (“Tax\-Aware Investment Management Practice,” 2009\)
Jaconetti et al. ( From assets to income: A goals\-based approach to retirement spending , 2020\)
Lei et al. (“Two Birds, One Stone: Joint Timing of Returns and Capital Gains Taxes,” 2020\)
Liberman et al. (“The Tax Benefits of Separating Alpha from Beta,” 2020\)
Lucas and Sanz (“Pick Your Battles: The Intersection of Investment Strategy, Tax, and Compounding Returns,”
2016\)
Mladina (“Refining After\-Tax Return and Risk Parameters,” 2020\)
Moehle et al. (“Tax\-Aware Portfolio Construction via Convex Optimization,” 2021\)
Shalett et al. ( Tax Efficiency: Getting to What You Need by Keeping More of What You Earn , 2017\)
Sialm and Sosner (“Taxes, Shorting, and Active Management,” 2017\)
Sosner and Krasner (“Tax\-Efficient Portfolio Transition: A Tax\-Aware Relaxed\-Constraint Approach to Switch\-
ing Equity Managers,” 2020\)
Sialm and Zhang (“Tax\-Efficient Asset Management: Evidence from Equity Mutual Funds,” 2020\)
Sosner et al. (“The Tax Benefits of Relaxing the Long\-Only Constraint: Do They Come from Character or
Deferral?” 2019\)
Sosner et al. (“Multi\-Period After\-Tax Reporting: A Practical Solution,” 2018\)
Stein and Garland (“Investment Management for Taxable Investors,” 2008\)
Turvey et al. (“Embedded Tax Liabilities and Portfolio Choice,” 2013\)
122\.2\.11 Network\-based and clustering\-based portfolio optimization
References:
Aghabozorgi et al. (“Time\-series clustering \- A decade review,” 2015\)
Akansu et al. (“Quant investing in cluster portfolios,” 2021\)
Augustynski and Laskos\-Grabowski (“Clustering Macroeconomic Time Series,” 2018\)
Avellaneda and Serur (“Hierarchical PCA and Modeling Asset Correlations,” 2020\)
Baitinger and Papenbrock (“Interconnectedness Risk and Active Portfolio Management,” 2017\)
Bandara et al. (“Forecasting across time series databases using recurrent neural networks on groups of similar
series: A clustering approach,” 2020\)
Begusic and Kostanjcar (“Cluster\-Based Shrinkage of Correlation Matrices for Portfolio Optimization,” 2019\)
Bnouachir and Mkhadri (“Efficient cluster\-based portfolio optimization,” 2021\)
Boginski et al. (“A network\-based data mining approach to portfolio selection via weighted clique relaxations,”
2014\)
Bokde et al. (“PSF: introduction to R package for pattern sequence based forecasting algorithm,” 2017\)
Cai et al. (“Hierarchy, cluster, and time\-stable information structure of correlations between international finan\-
cial markets,” 2017\)
Clemente et al. (“Smart network based portfolios,” 2019\)
Clemente et al. (“Asset allocation: new evidence through network approaches,” 2021\)
Dees et al. (“Portfolio Cuts: A Graph\-Theoretic Framework to Diversification,” 2019\)
Dose and Cincotti (“Clustering of financial time series with application to index and enhanced index tracking
portfolio,” 2005\)
Eom and Park (“Effects of common factors on stock correlation networks and portfolio diversification,” 2017\)
Fragkiskos and Bauman (“Factor Based Clustering,” 2018\)
Fucik (“Portfolio Construction Using Hierarchical Clustering,” 2017\)
Giudici et al. (“Network models to improve robot advisory portfolios,” 2022\)
Guijo\-Rubio et al. (“Time series clustering based on the characterisation of segment typologies,” 2018\)
Holst et al. (“Interactive clustering for exploring multiple data streams at different time scales and granularity,”
2019\)
Huttner et al. (“Portfolio selection based on graphs: Does it align with Markowitz\-optimal portfolios?” 2018\)
Iori and Mantegna (“Empirical analyses of networks in finance,” 2018\)
Iorio et al. (“A P\-spline based clustering approach for portfolio selection,” 2018\)
Kaya (“Eccentricity in Asset Management,” 2015\)
Konstantinov et al. (“A network and machine learning approach to factor, asset, and blended allocation,” 2020\)
Kukreti et al. (“A Perspective on Correlation\-Based Financial Networks and Entropy Measures,” 2020\)
Leon et al. (“Clustering algorithms for Risk\-Adjusted Portfolio Construction,” 2017\)
Li et al. (“Transaction Costs of Factor\-Investing Strategies,” 2019\)
Lohre et al. (“Hierarchical Risk Parity: Accounting for Tail Dependencies in Multi\-asset Multi\-factor Alloca\-
tions,” 2020\)
Lopez de Prado (“Building Diversified Portfolios that Outperform Out of Sample,” 2016\)
Lopez de Prado ( Machine learning for asset managers , 2020\)
Maharaj et al. ( Time Series Clustering and Classification , 2019\)
Markovic et al. (“A Hybrid Model for Financial Portfolio Optimization Based on LS\-SVM and a Clustering
Algorithm,” 2019\)
Marti et al. (“Clustering Financial Time Series: How Long is Enough?” 2016\)
Marti et al. (“On Clustering Financial Time Series: A Need for Distances Between Dependent Random Vari\-
ables,” 2017\)
Marti et al. (“A review of two decades of correlations, hierarchies, networks and clustering in financial markets,”
2020\)
Mikalsen et al. (“Time Series Cluster Kernel for Learning Similarities between Multivariate Time Series with
Missing Data,” 2018\)
Mitra et al. (“Portfolio management by time series clustering using correlation for stocks,” 2019\)
Nanakorn and Palmgren (“Hierarchical Clustering in Risk\-Based Portfolio Construction,” 2021\)
Olmo (“Optimal portfolio allocation and asset centrality revisited,” 2021\)
Paparrizos and Gravano (“Fast and Accurate Time\-Series Clustering,” 2017\)
13Pichler et al. (“Systemic\-risk\-efficient asset allocation: Minimization of systemic risk as a network optimization
problem,” 2018\)
Park (“Clustering Approaches for Global Minimum Variance Portfolio,” 2020\)
Peralta and Zareei (“A network approach to portfolio selection,” 2016\)
Raffinot (“Hierarchical Clustering\-Based Asset Allocation,” 2017\)
Raffinot (“The Hierarchical Equal Risk Contribution Portfolio,” 2018\)
Ren et al. (“Dynamic Portfolio Strategy Using Clustering Approach,” 2017\)
Sass and Thos (“Risk reduction and portfolio optimization using clustering methods,” 2022\)
Shirota and Murakami (“Long\-term Time Series Data Clustering of Stock Prices for Portfolio Selection,” 2021\)
Simonian and Wu (“Minsky vs. Machine: New Foundations for Quant\-Macro Investing,” 2019\)
Sjostrand and Behnejad (“Exploration of Hierarchical Clustering in Long\-only Risk\-based Portfolio Optimiza\-
tion,” 2020\)
Subekti et al. (“Combining Black\-Litterman model with clustering on portfolio construction,” 2019\)
Tola et al. (“Cluster analysis for portfolio optimization,” 2008\)
Vaquez et al. (“A preliminary study on multivariate time series clustering,” 2019\)
Vyrost et al. (“Network\-based asset allocation strategies,” 2019\)
Wang et al. (“A Portfolio Diversification Strategy via Tail Dependence Clustering,” 2017\)
Wang and Aste (“Dynamic Portfolio Optimization with Inverse Covariance Clustering,” 2022\)
Zareei (“Network origins of portfolio risk,” 2019\)
Zhang and Maringer (“Distributing weights under hierarchical clustering: A way in reducing performance break\-
down,” 2011\)
Zhang and Maringer ( Asset Allocation under Hierarchical Clustering , 2010\)
2\.2\.12 Machine learning for portfolio construction and portfolio management
References:
Aydemir (“Portfolio Construction Using First Principles Preference Theory and Machine Learning,” 2020\)
Benhamou et al. (“AAMDRL: Augmented Asset Management With Deep Reinforcement Learning,” 2021\)
Benhamou et al. (“Bridging the Gap Between Markowitz Planning and Deep Reinforcement Learning,” 2021\)
Benhamou et al. (“Deep Reinforcement Learning (DRL) for Portfolio Allocation,” 2021\)
Benhamou et al. (“DRLPS: Deep Reinforcement Learning for Portfolio Selection (Presentation Slides ECML
PKDD),” 2021\)
Benhamou et al. (“Deep Reinforcement Learning (DRL) for Portfolio Allocation,” 2021\)
Carta et al. (“Ensembling and Dynamic Asset Selection for Risk\-Controlled Statistical Arbitrage,” 2021\)
Chevalier et al. (“Supervised portfolios,” 2022\)
Cong et al. (“AlphaPortfolio: Direct Construction Through Deep Reinforcement Learning and Interpretable
AI,” 2022\)
Conlon et al. (“Machine Learning and Factor\-Based Portfolio Optimization,” 2021\)
DeMiguel et al. (“Crowding and Liquidity Provision in Factor Investing,” 2021\)
Huang et al. (“Dynamic Portfolio Management with Machine Learning,” 2021\)
Irlam (“Machine learning for retirement planning,” 2020\)
Li et al. (“Investable and Interpretable Machine Learning for Equities,” 2022\)
Li and Rossi (“Selecting Mutual Funds from the Stocks They Hold: A Machine Learning Approach,” 2021\)
Li and Mulvey (“Portfolio Optimization Under Regime Switching and Transaction Costs: Combining Neural
Networks and Dynamic Programs,” 2021\)
Lee and Seregina (“Optimal Portfolio Using Factor Graphical Lasso,” 2022\)
Papenbrock et al. (“Matrix Evolutions: Synthetic Correlations and Explainable Machine Learning for Con\-
structing Robust Investment Portfolios,” 2021\)
Perrin and Roncalli (“Machine Learning Optimization Algorithms \& Portfolio Allocation,” 2020\)
Schwendner et al. (“Adaptive Seriational Risk Parity and Other Extensions for Heuristic Portfolio Construction
Using Machine Learning and Graph Theory,” 2021\)
Uysal and Mulvey (“A Machine Learning Approach in Regime\-Switching Risk Parity Portfolios,” 2021\)
Yang et al. (“Asset Allocation via Machine Learning and Applications to Equity Portfolio Management,” 2021\)
Zhang et al. (“Deep Learning for Portfolio Optimisation,” 2021\)
14Zolotareva (“Aiding Long\-Term Investment Decisions with XGBoost Machine Learning Model,” 2021\)
2\.2\.13 Scenario\-based portfolio optimization
References:
Adler and Kritzman (“Mean\-variance versus full\-scale optimisation: In and out of sample,” 2007\)
Hagstromer et al. (“Mean\-Variance vs. Full\-Scale Optimization: Broad Evidence for the UK,” 2007\)
Seymour et al. (“Full\-Scale Optimization: A Flexible Framework for Hedge Design,” 2014\)
Hagstromer and Binner (“Stock portfolio selection with full\-scale optimization and differential evolution,” 2009\)
Jacobs et al. (“Portfolio Optimization with Factors, Scenarios, and Realistic Short Positions,” 2005\)
Sironi (Modern Portfolio Management: from Markowitz to Probabilistic Scenario Optimisation , 2015\)
Beraldi et al. (“Scenario\-based dynamic corporate bond portfolio management,” 2012\)
Kaya (“Intuitive Ambiguity Management,” 2016\)
Kaya (“Managing ambiguity in asset allocation,” 2017\)
Vilkkumaa et al. (“Scenario\-based portfolio model for building robust and proactive strategies,” 2018\)
2\.2\.14 Goals\-based portfolio optimization
References:
Brunel (Goals\-Based Wealth Management , 2015\)
Chhabra ( The Aspirational Investor: Taming the Markets to Achieve Your Life’s Goals , 2015\)
Cvitanic et al. (“Pi portfolio management: reaching goals while avoiding drawdowns,” 2020\)
Das et al. (“Dynamic portfolio allocation in goals\-based wealth management,” 2020\)
Das et al. (“Dynamic optimization for multi\-goals wealth management,” 2022\)
Das et al. (“Optimal Goals\-Based Investment Strategies For Switching Between Bull and Bear Markets,” 2022\)
Dempster et al. (“Lifecycle Goal Achievement or Portfolio Volatility Reduction?” 2016\)
Denault and Simonato (“A note on a dynamic goal\-based wealth management problem,” 2022\)
Dixon and Halperin (“Goal\-based wealth management with generative reinforcement learning,” 2021\)
Kim et al. (“Personalized goal\-based investing via multi\-stage stochastic goal programming,” 2020\)
Parker (“Portfolio Selection in a Goal\-Based Setting,” 2016\)
Parker (“Goal\-Based Portfolio Optimization,” 2016\)
Parker (“Multi\-Period Goals\-Based Portfolio Optimization,” 2021\)
Parker (“Achieving Goals While Making an Impact: Balancing Financial Goals with Impact Investing,” 2021\)
Wang et al. (“Portfolio Selection in Goals\-Based Wealth Management,” 2011\)
Wang and Spinney (“Strategic Asset Allocation: Combining Science and Judgment to Balance Short\-Term and
Long\-Term Goals,” 2017\)
Zanella (“Risk Capacity over the Life Cycle: The Role of Human Capital, High Priority Goals, and Discretionary
Wealth,” 2015\)
2\.2\.15 Surveys and best practices in portfolio construction and management
References:
Bianchi and Tassinari (“Forward\-looking portfolio selection with multivariate non\-Gaussian models,” 2020\)
Blay et al. (“Multi\-Period Portfolio Selection: A Practical Simulation\-Based Framework,” 2020\)
Ciliberti and Gualdi (“Portfolio Construction Matters,” 2020\)
Deguest et al. (“An Empirical Analysis of the Benefits of Corporate Bond Portfolio Optimization in the Presence
of Duration Constraints,” 2022\)
Fabozzi and Fabozzi ( Fundamentals of Institutional Asset Management , 2020\)
Fabozzi et al. ( Asset Management: Tools and Issues , 2021\)
Harvey et al. ( Strategic risk management : designing portfolios and managing risk , 2021\)
Ielpo et al. ( Engineering Investment Process: Making Value Creation Repeatable , 2017\)
Kritzman et al. ( A Practitioner’s Guide to Asset Allocation , 2017\)
Kolm et al. (“60 Years of portfolio optimization: Practical challenges and current trends,” 2014\)
Roy (“Examining the drivers of optimal portfolio construction,” 2021\)
Su (“The Implementation of Asset Allocation Approaches: Theory and Evidence,” 2020\)
15Xidonas et al. (“Robust portfolio optimization: a categorized bibliographic review,” 2020\)
Zhang et al. (“Portfolio selection problems with Markowitz mean\-variance framework: a review of literature,”
2018\)
2\.2\.16 Other topics in portfolio construction and management
References:
Allan et al. (“Model\-free Portfolio Theory: A Rough Path Approach,” 2022\)
deCastroetal.(“ExperimentsonPortfolioSelection: AComparisonbetweenQuantilePreferencesandExpected
Utility Decision Models,” 2021\)
Ehsani and Linnainmaa (“Time\-Series Efficient Factors,” 2021\)
Lassance and Vrins (“Portfolio selection with parsimonious higher comoments estimation,” 2021\)
Le (“International portfolio allocation: The role of conditional higher moments,” 2021\)
Lehalle and Simon (“Portfolio selection with active strategies: how long only constraints shape convictions,”
2021\)
Lezmi et al. (“Portfolio Allocation with Skewness Risk: A Practical Guide,” 2019\)
Lohre et al. (“Hierarchical Risk Parity: Accounting for Tail Dependencies in Multi\-asset Multi\-factor Alloca\-
tions,” 2020\)
Meucci et al. (“Portfolio Construction and Systematic Trading with Factor Entropy Pooling,” 2020\)
Pawar and Rathi (“An Ensemble Approach to Portfolio Optimization,” 2021\)
Paolella (“The Univariate Collapsing Method for Portfolio Optimization,” 2017\)
Paolella and Polak (“COBra: Copula\-Based Portfolio Optimization,” 2018\)
Pedersen et al. (“Enhanced Portfolio Optimization,” 2021\)
Procacci and Aste (“Portfolio Optimization with Sparse Multivariate Modelling,” 2021\)
Rudin and Farley (“Dual\-Horizon Strategic Asset Allocation,” 2022\)
Schuhmacher et al. (“Justifying Mean\-Variance Portfolio Selection when Asset Returns Are Skewed,” 2021\)
Tuck et al. (“Portfolio Construction Using Stratified Models,” 2021\)
Yang et al. (“The alpha Tail Distance with an Application to Portfolio Optimization Under Different Market
Conditions,” 2021\)
2\.2\.17 Testing and comparison procedures for investment portfolios
References:
Adcock et al. (“Portfolio Performance Measurement: Monotonicity with Respect to the Sharpe Ratio and
Multivariate Tests of Correlation,” 2017\)
Arnott et al. (“A backtesting protocol in the era of machine learning,” 2019\)
Bailey et al. (“Stock Portfolio Design and Backtest Overfitting,” 2017\)
Bessler and Wolff (“Portfolio Optimization with Industry Return Prediction Models,” 2017\)
Bessler et al. (“Multi\-asset portfolio optimization and out\-of\-sample performance: an evaluation of Black Lit\-
terman, mean\-variance, and naive diversification approaches,” 2017\)
Bjerring et al. (“Feature selection for portfolio optimization,” 2017\)
Bruni et al. (“On exact and approximate stochastic dominance strategies for portfolio selection,” 2017\)
Bruni et al. (“Real\-world datasets for portfolio selection and solutions of some stochastic dominance portfolio
models,” 2016\)
Bryzgalova et al. (“Bayesian solutions for the factor zoo: we just ran two quadrillion models,” 2021\)
Cesarone et al. (“On the stability of portfolio selection models,” 2019\)
Cesarone et al. (“Why Small Portfolios Are Preferable and How to Choose Them,” 2018\)
Chaudhuri and Lo (“Dynamic Alpha: A Spectral Decomposition of Investment Performance Across Time Hori\-
zons,” 2019\)
Diris et al. (“Long\-Term Strategic Asset Allocation: An Out\-of\-Sample Evaluation,” 2015\)
Fabozzi and Lopez de Prado (“Being Honest in Backtest Reporting: A Template for Disclosing Multiple Tests,”
2018\)
Greiner and Stoyanov (“Portfolio scoring by expected risk premium,” 2019\)
Guidolin et al. (“Portfolio performance of linear SDF models: an out\-of\-sample assessment,” 2018\)
Guo (“A Statistical Response to Challenges in Vast Portfolio Selection,” 2019\)
16Guo et al. (“When Does The 1/N Rule Work?” 2019\)
Haley (“K\-fold cross validation performance comparisons of six naive portfolio selection rules: how naive can
you be and still have successful out\-of\-sample portfolio performance?” 2017\)
Harvey et al. (“An Evaluation of Alternative Multiple Testing Methods for Finance Applications,” 2020\)
Hens et al. (“Escaping the backtesting illusion,” 2020\)
Hsu et al. ( Do Cross\-Sectional Stock Return Predictors Pass the Test without Data\-Snooping Bias? 2017\)
Hsu et al. (“Asset allocation strategies, data snooping, and the 1 / N rule,” 2018\)
Huang and Yu (“A new procedure for resampled portfolio with shrinkaged covariance matrix,” 2020\)
Hwang et al. (“Naive versus optimal diversification: Tail risk and performance,” 2018\)
Ielpo et al. ( Engineering Investment Process: Making Value Creation Repeatable , 2017\)
Jaeger et al. (“Understanding machine learning for diversified portfolio construction by explainable AI,” 2020\)
Kazak and Pohlmeier (“Testing out\-of\-sample portfolio performance,” 2019\)
Kazak and Pohlmeier ( Portfolio Pretesting with Machine Learning , 2020\)
Kuntz (“Portfolio Strategies with Classical and Alternative Benchmarks,” 2018\)
Lohre et al. (“Hierarchical Risk Parity: Accounting for Tail Dependencies in Multi\-asset Multi\-factor Alloca\-
tions,” 2020\)
Lopez de Prado (“A Data Science Solution to the Multiple\-Testing Crisis in Financial Research,” 2019\)
Lopez de Prado and Lewis (“Detection of false investment strategies using unsupervised learning methods,”
2019\)
Malavasi et al. (“Second order of stochastic dominance efficiency vs mean variance efficiency,” 2021\)
Mooney et al. (“Dynamic Regime Strategy for Stress Testing and Optimizing Institutional Investor Portfolios,”
2020\)
Platanakis et al. (“Horses for Courses: Mean\-Variance for Asset Allocation and 1/N for Stock Selection,” 2021\)
Radovanov and Marcikic (“Testing The Performance Of The Investment Portfolio Using Block Bootstrap
Method,” 2014\)
Rebonato (“A financially justifiable and practically implementable approach to coherent stress testing,” 2019\)
Schumann (“Backtesting,” 2019\)
Seymour et al. (“Dynamic portfolio management strategies: A framework for historical analysis,” 2018\)
Suhonen et al. (“Quantifying Backtest Overfitting in Alternative Beta Strategies,” 2017\)
Taljaard and Maré (“Why has the equal weight portfolio underperformed and what can we do about it?” 2021\)
Tayali (“A novel backtesting methodology for clustering in mean–variance portfolio optimization,” 2020\)
Traccucci et al. (“A Triptych Approach for Reverse Stress Testing of Complex Portfolios,” 2019\)
Valentine et al. (“Beyond p values: utilizing multiple methods to evaluate evidence,” 2019\)
Vincent et al. (“Analyzing the Performance of Multifactor Investment Strategies under a Multiple Testing
Framework,” 2018\)
Vovk and Wang (“True and false discoveries with e\-values,” 2020\)
Vovk and Wang (“E\-values: Calibration, combination, and applications,” 2021\)
Wiecki et al. (“All That Glitters Is Not Gold: Comparing Backtest and Out\-of\-Sample Performance on a Large
Cohort of Trading Algorithms,” 2016\)
Yu (“Comparing Classical Portfolio Optimization and Robust Portfolio Optimization on Black Swan Events,”
2021\)
Yuan and Zhou (“Why Naive 1/N Diversification Is Not So Naive, and How to Beat It?” 2022\)
Zhang et al. (“DoubleEnsemble: A New Ensemble Method Based on Sample Reweighting and Feature Selection
for Financial Data Analysis,” 2020\)
Zhang et al. (“Information Coefficient as a Performance Measure of Stock Selection Models,” 2020\)
Zhang et al. (“Deep Learning for Portfolio Optimization,” 2020\)
2\.2\.18 Portfolio rebalancing
References:
Abeysekera and Rosenbloom (“Optimal Rebalancing for Taxable Portfolios,” 2002\)
Almadi et al. (“Return Predictability and Dynamic Asset Allocation: How Often Should Investors Rebalance?”
2014\)
Boscaljon et al. (“Rebalancing strategies for creating efficient portfolios,” 2008\)
17Brown (“Intelligent Rebalancing,” 2018\)
Carl (“Understanding Rebalancing and Portfolio Reconstitution,” 2017\)
Dichtl et al. (“Where is the value added of rebalancing? A systematic comparison of alternative rebalancing
strategies,” 2014\)
Driessen and Kuiper (“Rebalancing for Long Term Investors: Why It Pays to Do Less,” 2019\)
Edesess (“Rebalancing: A Comprehensive Reassessment,” 2017\)
El Bernoussi and Rockinger (“Rebalancing with transaction costs: theory, simulations, and actual data,” 2019\)
Garivaltis (“Exact replication of the best rebalancing rule in hindsight,” 2019\)
Hallerbach (“Disentangling rebalancing return,” 2014\)
Harvey et al. (“Strategic Risk Management: Out\-of\-Sample Evidence from the COVID\-19 Equity Selloff,” 2020\)
Hight and Haley (“Low\-Risk Benchmarking Transcends Rebalancing Methods,” 2021\)
Hilliard and Hilliard (“Rebalancing versus Buy and Hold: Theory, Simulation and Empirical Analysis,” 2015\)
Hoffstein et al. (“Rebalance Timing Luck: The (Dumb) Luck of Smart Beta,” 2020\)
Horn and Oehler (“Automated portfolio rebalancing: Automatic erosion of investment performance?” 2020\)
Ilmanen and Maloney (“Portfolio Rebalancing, Part 1: Strategic Asset Allocation,” 2015\)
Israelov and Tummala (“An Alternative Option to Portfolio Rebalancing,” 2018\)
Jennings and Payne (“Corrections Should Trigger Rebalancing,” 2020\)
Khang and Picca (“Waiting for the Next Factor Wave: Daily Rebalancing around Market Cycle Transitions,”
2021\)
Lee and Liu (“Work Harder: Diligent Rebalancing and Investment Horizon,” 2021\)
Liu (“Analytical solutions of optimal portfolio rebalancing,” 2019\)
Liu and Viswanathan (“The term structure of the rebalancing premium,” 2020\)
Maeso and Martellini (“Measuring portfolio rebalancing benefits in equity markets,” 2020\)
McNamee et al. ( Getting back on track: A guide to smart rebalancing , 2019\)
Qian (Portfolio Rebalancing , 2018\)
Rattray et al. (“Strategic Rebalancing,” 2020\)
Rietz et al. (“Analyzing Retirement Withdrawal Strategies,” 2018\)
Serbin et al. (“Robust Portfolio Rebalancing with Transaction Cost Penalty an Empirical Analysis,” 2011\)
Skallsjo (“Simple formulas for portfolio rebalancing rules,” 2019\)
Taljaard and Mare (“Too Much Rebalancing Is Not a Good Thing,” 2019\)
Zhao et al. (“Robust portfolio rebalancing with cardinality and diversification constraints,” 2021\)
Zilbering et al. ( Best practices for portfolio rebalancing , 2015\)
2\.2\.19 Software packages and codes for portfolio optimization and management
References:
Boileau et al. (“Cross\-Validated Loss\-Based Covariance Matrix Estimator Selection in High Dimensions,” 2021\)
Irlam (“Machine learning for retirement planning,” 2020\)
Martin (“PyPortfolioOpt: portfolio optimization in Python,” 2021\)
Sarmas et al. ( Multicriteria Portfolio Construction with Python , 2020\)
Snow (“Machine Learning in Asset Management \- Part 2: Portfolio Construction \- Weight Optimization,” 2020\)
18References
Abeysekera, S. P. and Rosenbloom, E. S. (2002\). “Optimal Rebalancing for Taxable Portfolios .” In:The Journal of
Wealth Management 5(3\), pp. 42–49\.
The authors focus on the issue of rebalancing taxable portfolios and overcoming the capital gains lock\-in effect.
They propose an integer linear program, developed to maximize the expected after\-tax return over a desired
planning horizon, given an initial portfolio with unrealized gains and losses. They then offer an integer quadratic
program, developed for minimizing the variance of the return given an initial portfolio with unrealized gains
and losses. They conclude by suggesting that these models allow investors to explicitly take into consideration
their personal tax situation when rebalancing their portfolios.
Adams, Z., Fuss, R., and Gluck, T. (2017\). “Are correlations constant? Empirical and theoretical results on popular
correlation models in finance .” In:Journal of Banking and Finance 84, pp. 9–24\.
Multivariate GARCH models have been designed as an extension of their univariate counterparts. Such a view
is appealing from a modeling perspective but imposes correlation dynamics that are similar to time\-varying
volatility. In this paper, we argue that correlations are quite different in nature. We demonstrate that the highly
unstable and erratic behavior that is typically observed for the correlation among financial assets is to a large
extentastatisticalartifact.Weprovideevidencethatspuriouscorrelationdynamicsoccurinresponsetofinancial
events that are sufficiently large to cause a structural break in the time\-series of correlations. A measure for the
autocovariance structure of conditional correlations allows us to formally demonstrate that the volatility and the
persistence of daily correlations are not primarily driven by financial news but by the level of the underlying true
correlation. Our results indicate that a rolling\-window sample correlation is often a better choice for empirical
applications in finance.
Adcock, C., Areal, N., Armada, M. R., Cortez, M. C., Oliveira, B., and Silva, F. (2017\). “Portfolio Performance
Measurement: Monotonicity with Respect to the Sharpe Ratio and Multivariate Tests of Correlation .” In:SSRN
e\-Print.
This paper reports an investigation into methods of portfolio performance measurement. The work is motivated
first by equivocal empirical evidence reported by several authors about the correlation of performance measures
with the Sharpe ratio. Secondly it is motivated by recent work which specifies that performance measures will
be monotone functions of the Sharpe ratio if portfolio returns follow the same location\-scale distribution. The
paper demonstrates that the class of location\-scale distributions is broader than previously reported. It presents
conditions under which monotonicity with respect to the Sharpe ratio will fail. The paper shows that for large
sample sizes the correlation between pairs of performance measures that are functions of the Sharpe ratio is
unity. The correct null hypothesis for tests of correlation is therefore rho\=1\. Two multivariate tests of this
null hypothesis are presented. The new tests are used to carry out of a comprehensive study of performance
measurement for a set over ninety UK investment trusts.
Adler, T. and Kritzman, M. (2007\). “Mean\-variance versus full\-scale optimisation: In and out of sample .” In:Journal
of Asset Management 7(5\), pp. 302–311\.
We present a recent innovation to portfolio construction called full\-scale optimisation. In contrast to mean\-
variance analysis, which assumes that returns are normally distributed or that investors have quadratic utility,
full\-scale optimisation identifies the optimal portfolio given any set of return distributions and any description
of investor preferences. It therefore yields the truly optimal portfolio in sample, whereas mean\-variance analysis
provides an approximation to the in\-sample truth. Both approaches, however, suffer from estimation error. We
employ a bootstrapping procedure to compare the estimation error of full\-scale optimisation to the combined
approximationandestimationerrorofmean\-varianceanalysis.Wefindthat,toasignificantdegree,thein\-sample
superiority of full\-scale optimisation prevails out of sample.
Aghabozorgi, S., Seyed, A. S., and Wah, T. Y. (2015\). “Time\-series clustering \- A decade review .” In:Information
Systems 53, pp. 16–38\.
Anatomy of time\-series clustering is revealed by introducing its 4 main component. Research works in each of
the four main components are reviewed in detail and compared. Analysis of research works published in the
last decade. Enlighten new paths for future works for time\-series clustering and its components. Clustering is
a solution for classifying enormous data when there is not any early knowledge about classes. With emerging
new concepts like cloud computing and big data and their vast applications in recent years, research works have
been increased on unsupervised solutions like clustering algorithms to extract knowledge from this avalanche of
data. Clustering time\-series data has been used in diverse scientific areas to discover patterns which empower
19data analysts to extract valuable information from complex and massive datasets. In case of huge datasets,
using supervised classification solutions is almost impossible, while clustering can solve this problem using un\-
supervised approaches. In this research work, the focus is on time\-series data, which is one of the popular data
types in clustering problems and is broadly used from gene expression data in biology to stock market analysis
in finance. This review will expose four main components of time\-series clustering and is aimed to represent an
updated investigation on the trend of improvements in efficiency, quality and complexity of clustering time\-series
approaches during the last decade and enlighten new paths for future works.
Agrawal, R., Roy, U., and Uhler, C. (2021\). “Covariance Matrix Estimation under Total Positivity for Portfolio
Selection .” In:Journal of Financial Econometrics .
Selecting the optimal Markowitz porfolio depends on estimating the covariance matrix of the returns of N assets
fromT periods of historical data. Problematically, N is typically of the same order as T, which makes the sample
covariance matrix estimator perform poorly, both empirically and theoretically. While various other general
purpose covariance matrix estimators have been introduced in the financial economics and statistics literature
for dealing with the high dimensionality of this problem, we here propose an estimator that exploits the fact
that assets are typically positively dependent. This is achieved by imposing that the joint distribution of returns
be multivariate totally positive of order 2, MTP2\. This constraint on the covariance matrix not only enforces
positive dependence among the assets, but also regularizes the covariance matrix, leading to desirable statistical
properties such as sparsity. Based on stock\-market data spanning over thirty years, we show that estimating the
covariance matrix under MTP2 outperforms previous state\-of\-the\-art methods including shrinkage estimators
and factor models.
Ahmad,W.,Bhanumurthy,N.R.,andSehgal,S.(2015\). “RegimedependentdynamicsandEuropeanstockmarkets:
Is asset allocation really possible? ” In:Empirica 42(1\), pp. 77–107\.
In this study, we examine the regime shifts and volatility in stock market returns of eighteen European stock
marketsandtheUSAandutilizetheseregimesinassetallocationandriskmanagementcontexts.UsingaMarkov
regime switching model, the study finds strong evidence of regime switching characterized by two regimes over
the sample period from February, 1996 to January, 2012\. Smoothed probabilities and time\-varying conditional
volatilities also highlight the meaningful turning points including the recent global financial crisis (2008\) and
Eurozone crisis (2009\). Analyzing the market synchronization and Sharpe ratios, the study finally concludes
that sample markets provide very limited scope of asset allocation and risk diversification.
Akansu, A., Avellaneda, M., and Xiong, A. (2021\). “Quant investing in cluster portfolios .” In:The Journal of
Investment Strategies 9(4\), pp. 61–78\.
This paper discusses portfolio construction for investing in N given assets, eg, constituents of the Dow Jones
Industrial Average (DJIA) or large cap stocks, based on partitioning the investment universe into clusters. The
clusters are determined from the trailing correlation matrix via an information theoretic algorithm that uses
thresholding of high\-correlation pairs. We calculate the principal eigenvector of each cluster from its correlation
matrix and the corresponding eigenportfolio. The cluster portfolios are combined into a single N\-asset portfolio
based on a weighting scheme for the clusters. Various tests conducted on components of the DJIA and a 30\-stock
basket of large cap stocks indicate that the new portfolios are superior to the DJIA and other mean\-variance
portfolios in terms of their risk\-adjusted returns from 2009 to 2019\. We also tested the cluster portfolios for a
larger basket of 373 Standard \& Poor’s 500 components from 2001 to 2019\. The test results provide convincing
evidence that a cluster\-based portfolio can outperform passive investing.
Aked, M., Arnott, R., Bouchey, P., Li, T., and Shakernia, O. (2019\). “Tactical and Tax Aware GTAA .” In:The
Journal of Portfolio Management 45(2\), pp. 23–37\.
Global tactical asset allocation (GTAA) has rarely been associated with tax\-aware investing. Although GTAA
can improve returns over a buy\-and\-hold strategy, more tactical trading (when profitable) typically leads to
higher tax bills. If investors are careless about tax management, the GTAA alpha can easily be swamped by
increased taxes. In response, many investors have been quick to embrace passive buy\-and\-hold strategies for
which low turnover results in a lower tax bill. However, rather than abandoning GTAA in favor of lower taxes,
investors can apply well\-documented tax management methods of loss harvesting and tax\-lot selection in their
tactical trading. The authors show that investors can capture most of the benefits of GTAA, and even provide
a boost to their after\-tax returns, if they view the proactive management of tax consequences as an important
part of the quest for asset allocation alpha.
Al Janabi, M. A. M. (2021\). “Is optimum always optimal? A revisit of the mean\-variance method under nonlinear
measures of dependence and non\-normal liquidity constraints .” In:Journal of Forecasting 40(3\), pp. 387–415\.
20We develop a model for optimizing multiple\-asset portfolios with semi\-parametric liquidity\-adjusted value\-at\-
risk (LVaR), whereby linear correlations are substituted by the multivariate nonlinear Kendall’s tau dependence
measure, under multiple credible operational and budget constraints. When considering a diversified large port\-
folio of international stock markets of both developed and emerging economies and commodities, under both
regular and stressed market perspectives, the obtained results consistently confirm the dominance of our mod\-
eling algorithms relative to other competing portfolio strategies, including the traditional mean\-variance VaR
approach and global minimum\-variance portfolios. The obtained results are robust to different trading scenarios
and promising for practical optimization techniques in large multiple\-asset portfolios and operation research
models in financial institution management.
Alankar, A., DePalma, M., and Scholes, M. (2013\). “An Introduction to Tail Risk Parity: Balancing Risk to Achieve
Downside Protection .” In:SSRN e\-Print .
Tail Risk Parity (TRP) adapts the risk balancing techniques of Risk Parity in an attempt to protect the
portfolio at times of economic crisis and reduce the cost of the protection in the absence of a crisis. In measuring
expected tail loss we use a proprietary implied expected tail loss (ETL) measure distilled from options market
information.
Whereas Risk Parity focuses on volatility, Tail Risk Parity defines risk as expected tail loss, something that
hurts investors more than volatility. Risk Parity is a subset of Tail Risk Parity when asset returns are normally
distributed and or volatility adequately captures tail loss risk. Hence, when the risk of tail events is negligible,
Tail Risk Parity allocations will resemble Risk Parity allocations.
Tail Risk Parity seeks to reduce tail losses significantly while retaining more upside than Risk Parity or other
mean variance optimization techniques. It is very difficult to construct portfolios under symmetric risk measures
(such as volatility as used in Risk Parity) that do not penalize both large losses and, unfortunately, large gains.
Tail Risk Parity aims to protect investments against large losses when investors can least afford them, when
systemic crises unfold and correlations spike unexpectedly. This is exactly when the marginal utility of an extra
dollar is highest.
Our research suggests that a Tail Risk Parity approach hedges the risk of large losses more cheaply than using
the options market (historically we estimate savings of about 50\.
We believe that Tail Risk Parity offers an attractive solution for investors seeking balanced investment portfolios
that can cost effectively reduce exposures to tail losses.
Albanese,C.,Li,D.,Lobachevskiy,E.,andMeissner,G.(2013\). “AComparativeAnalysisofCorrelationApproaches
in Finance .” In:The Journal of Derivatives 21(2\), pp. 42–66\.
Although volatility is the key parameter for plain vanilla option pricing, many kinds of credit derivatives and
exotic options involve multiple risk factors, so correlations must also be modeled. Different types of derivatives
entail different types of correlation, from the basic Pearson correlation used in ordinary futures hedging and
equity portfolio calculations, to copula methods that allow a wide range of tail dependence properties, to the
ubiquitous Gaussian copula of credit risk modeling. Models of stochastically time\-varying correlations have been
developed, and for the correlation structure within a credit portfolio that may contain thousands of individual
loans, top\-down methods like Vasicek’s large homogeneous portfolio approximation may be required. This article
provides a comprehensive review of the many correlation concepts and models that are increasingly necessary
for modern derivatives researchers.
Aldridge, I. (2019\). “Big data in portfolio allocation: A new approach to successful portfolio optimization .” In:The
Journal of Financial Data Science 1(1\), pp. 45–63\.
In the classic mean\-variance portfolio theory as proposed by Harry Markowitz, the weights of the optimized
portfolios are directly proportional to the inverse of the asset correlation matrix. However, most contemporary
portfolio optimization research focuses on optimizing the correlation matrix itself, and not its inverse. In this
article, the author demonstrates that this is a mistake. Specifically, from the Big Data perspective, she proves
that the inverse of the correlation matrix is much more unstable and sensitive to random perturbations than
is the correlation matrix itself. As such, optimization of the inverse of the correlation matrix adds more value
to optimal portfolio selection than does optimization of the correlation matrix. The author further shows the
empirical results of portfolio reallocation under different common portfolio composition scenarios. The technique
outperforms traditional portfolio allocation techniques out of sample, delivering nearly 400% improvement over
the equally weighted allocation over a 20\-year investment period on the SandP 500 portfolio with monthly
reallocation.Ingeneral,theauthordemonstratesthatthecorrelationinverseoptimizationproposedinthisarticle
significantlyoutperformstheothercoreportfolioallocationstrategies,suchasequallyweightedportfolios,vanilla
21mean\-variance optimization, and techniques based on the spectral decomposition of the correlation matrix. The
results presented in this article are novel in the data science space, extend far beyond financial data, and are
applicable to any data correlation matrixes and their inverses, whether in advertising, healthcare, or genomics.
Alkafri, N. and Frey, C. (2022\). “Shrinkage Estimation in Risk Parity Portfolios .” In:SSRN e\-Print .
We investigate the impact of shrinkage estimation techniques for the moments of asset returns on risk\-parity
portfolios. In contrast to mean\-variance portfolios, the risk contributions of individual assets in risk\-parity
portfolios are fixed a priori. This additional restriction stabilizes empirical portfolio weights in time. We show
that the marginal risk budget for each portfolio asset indeed serves as a natural shrinkage target. Hence, we
provide a new perspective on risk\-parity portfolios. In an extensive empirical application, we compare and
combine the various shrinkage strategies to popular risk\-based approaches from the literature. We find that
while using shrinkage estimators in risk\-parity portfolios enhances out\-of\-sample performance based on several
criteria, traditional covariance shrinkage estimators dominate all other strategies in high\-dimensional settings.
Allaj, E. (2020\). “The Black\-Litterman model and views from a reverse optimization procedure: an out\-of\-sample
performance evaluation .” In:Computational Management Science 17, pp. 465–492\.
The Black\-Litterman (BL) model has been proposed as a valid solution to the problem of the estimation error
in the mean\-variance (MV) model. However, very little research has been done in order to empirically test the
performance of the model. The paper contributes to the existing literature by empirically examining the out\-of\-
sample performance of the BL model with respect to other asset allocation strategies. As another contribution
of the paper, we suggest a novel approach to specify the investor’s views in the BL model. Overall our results
suggest that the BL model is a valid asset allocation strategy.
Allan, A. L., Cuchiero, C., Liu, C., and Promel, D. J. (2022\). “Model\-free Portfolio Theory: A Rough Path Ap\-
proach.” In:arXiv e\-Print .
Based on a rough path foundation, we develop a model\-free approach to stochastic portfolio theory (SPT).
Our approach allows to handle significantly more general portfolios compared to previous model\-free approaches
basedonFöllmerintegration.Withouttheassumptionofanyunderlyingprobabilisticmodel,weproveapathwise
formula for the relative wealth process which reduces in the special case of functionally generated portfolios to
a pathwise version of the so\-called master formula of classical SPT. We show that the appropriately scaled
asymptotic growth rate of a far reaching generalization of Cover’s universal portfolio based on controlled paths
coincides with that of the best retrospectively chosen portfolio within this class. We provide several novel results
concerning rough integration, and highlight the advantages of the rough path approach by considering (non\-
functionally generated) log\-optimal portfolios in an ergodic Itô diffusion setting.
Allen, D., Lizieri, C., and Satchell, S. (2019\). “In defense of portfolio optimization: what if we can forecast? ” In:
Financial Analysts Journal 75(3\), pp. 20–38\.
We challenge the academic consensus that estimation error makes mean\-variance portfolio strategies inferior to
passive equal\-weighted approaches. We demonstrate analytically, via simulation, and empirically that investors
endowed with modest forecasting ability benefit substantially from a mean\-variance approach. An investor with
some forecasting ability improves expected utility by increasing the number of assets considered. We frame our
study realistically using budget constraints, transaction costs, and out\-of\-sample testing for a wide range of
investments. We derive practical decision rules to choose between passive and mean\-variance optimization and
generate results consistent with much financial market practice and the original Markowitz formulation.
Almadi, H., Rapach, D. E., and Suri, A. (2014\). “Return Predictability and Dynamic Asset Allocation: How Often
Should Investors Rebalance? ” In:The Journal of Portfolio Management 40(4\), pp. 16–27\.
To exploit return predictability via dynamic asset allocation, investors face the important practical issue of how
oftentorebalancetheirportfolios.Morefrequentrebalancingusesstatisticallyandeconomicallysignificantshort\-
horizon return predictability to aggressively pursue the dynamic investment opportunities afforded by changes
in expected returns. However, the degree of return predictability typically appears stronger at longer horizons,
which, along with lower transaction costs, favors less frequent rebalancing. The authors analyze the performance
effects of rebalancing frequency in the context of dynamic portfolios constructed from monthly, quarterly, semi\-
annual, and annual return forecasts for U.S. stocks, bonds, and bills, where the dynamic portfolios rebalance at
the same frequency as the forecast horizon. Along the transaction\-cost/rebalancing frontier, monthly (annual)
rebalancing provides the greatest outperformance when unit transaction costs are below (above) approximately
50 basis points, and dynamic portfolios based on annual rebalancing typically outperform the benchmarks for
unit transaction costs well in excess of 400 basis points.
22Alonso, N. and Qian, E. (2013\). “Risk Parity Equity Strategy with Flexible Risk Targets .” In:The Journal of
Investing 22(3\), pp. 99–106\.
Risk\-based investment strategies such as Risk Parity and minimum variance tend to have better long term risk\-
adjusted returns but lower risks than traditional capital\-based investment strategies. In order to either derive
higher return or to better manage risk, it is often desirable to design risk\-based strategies with higher risk
targets. We discuss the ways to do so for Risk Parity equity portfolios. The targeted portfolio is long\-only with a
130/0 \-like structure. We show that a synthetic portfolio with stocks and equity index futures can closely mimic
the target portfolio with minimal tracking error and similar Sharpe ratio.
Anastasov, A. G. (2017\). “Tax\-efficient asset management via loss harvesting .” MA thesis. MIT.
In this thesis, we study loss\-harvesting–an investment strategy that realizes capital losses immediately but defers
realizing capital gains as long as possible. We begin by describing a computational framework for studying the
properties of loss\-harvesting empirically. The main advantage of our framework is flexibility. In particular, our
framework is independent of any particular choice of a source for stock return time series. After combining
the framework with the Capital Asset Pricing Model as a source for simulated stock returns data, we perform
a thorough sensitivity analysis and study the performance of loss\-harvesting under various conditions of the
financial market. By combining the framework with historical stock return time series from the S\&P 500 Index,
we study the performance of loss\-harvesting from a different and more practical, point of view. Through this
empirical exploration, we identify three new findings about loss\-harvesting: (1\) introducing a transaction cost
rate of 1% reduces alpha by about 50% after taxes; (2\) introducing regular cash contributions reduces alpha after
taxes; and (3\) under specific market conditions, a simple passive buy\-and\-hold investment strategy outperforms
loss\-harvesting.
Anderson, E. W. and Cheng, A.\-R. M. (2016\). “Robust Bayesian Portfolio Choices .” In:The Review of Financial
Studies29(5\), pp. 1330–1375\.
We propose a Bayesian\-averaging portfolio choice strategy with excellent out\-of\-sample performance. Every
period a new model is born that assumes means and covariances are constant over time. Each period we
estimate model parameters, update model probabilities, and compute robust portfolio choices by taking into
account model uncertainty, parameter uncertainty, and non\-stationarity. The portfolio choices achieve higher
out\-of\-sample Sharpe ratios and certainty equivalents than rolling window schemes, the 1/N approach, and
other leading strategies do on a majority of 24 datasets.
Andrei, M. S. and Hsu, J. S. J. (2018\). “Bayesian Alternatives to the Black\-Litterman Model .” In:arXiv e\-Print .
The Black\-Litterman model combines investors’ personal views with historical data and gives optimal portfolio
weights. In this paper we will introduce the original Black\-Litterman model (section 1\), we will modify the
model such that it fits in a Bayesian framework by considering the investors’ personal views to be a direct prior
on the means of the returns and by adding a typical Inverse Wishart prior on the covariance matrix of the
returns (section 2\). Lastly, we will use Leonard and Hsu’s (1992\) idea of adding a prior on the logarithm of the
covariance matrix (section 3\). Sensitivity simulations for the level of confidence that the investor has in their
own personal views were performed and performance of the models was assessed on a test data set consisting of
returns over the month of January 2018\.
Arnott, R., Kalesnik, V., and Schuesler, T. (2018\). “Is Your Alpha Big Enough to Cover Its Taxes? A Quarter\-
Century Retrospective .” In:The Journal of Portfolio Management 44(5\), pp. 78–102\.
This article revisits the findings (published in this journal) of Jeffrey and Arnott, who reported that over 95%
of active managers underperformed a capitalization\-weighted index fund on an after\-tax basis. The authors
posit that much has changed in the quarter century since the publishing of that article, including increased tax
awareness on the part of investors and advancements in the tax efficiency of some investment funds and vehicles;
thus, investors may now have a better opportunity to generate alpha that is big enough to cover its taxes. The
authors measure the degree to which fund characteristics affect a fund tax burden and compare the tax efficiency
of investing in exchange\-traded funds and mutual funds. The authors calculate the after\-tax returns of funds
and examine whether new categories of funds (e.g., smart beta) are better at generating after\-tax alpha than
their active and passive fund peers.
Arnott, R. D., Berkin, A. L., and Ye, J. (2001\). “The management and mismanagement of taxable assets .” In:The
Journal of Investing 10(1\), pp. 15–21\.
Although the aggregate amount of taxable money under management actually exceeds the value of tax\-exempt
money such as in pensions and endowments, far too often these assets are invested without proper consideration
for taxes. The authors identify sources of taxable asset mismanagement and give methods of improvement.
23They also describe considerations for selecting a tax\-efficient manager and give details of actually effecting a
tax\-efficient strategy. Lastly, the authors close with a roster of actions a taxable investor should and should not
do.
Arnott, R. D., Harvey, C. R., and Markowitz, H. (2019\). “A backtesting protocol in the era of machine learning .”
In:The Journal of Financial Data Science 1(1\), pp. 64–74\.
Machine learning offers a set of powerful tools that holds considerable promise for investment management. As
with most quantitative applications in finance, the danger of misapplying these techniques can lead to disap\-
pointment. One crucial limitation involves data availability. Many of machine learning early successes originated
in the physical and biological sciences, in which truly vast amounts of data are available. Machine learning
applications often require far more data than are available in finance, which is of particular concern in longer\-
horizon investing. Hence, choosing the right applications before applying the tools is important. In addition,
capital markets reflect the actions of people, which may be influenced by others actions and by the findings
of past research. In many ways, the challenges that affect machine learning are merely a continuation of the
long\-standing issues researchers have always faced in quantitative finance. While investors need to be cautious,
more cautious than in past applications of quantitative methods new tools offer many potential applications in
finance. In this article, the authors develop a research protocol that pertains both to the application of machine
learning techniques and to quantitative finance in general.
Augustynski, I. and Laskos\-Grabowski, P. (2018\). “Clustering Macroeconomic Time Series .” In:Econometrics 22(2\),
pp. 74–88\.
Thedataminingtechniqueoftimeseriesclusteringiswellestablishedinmanyfields.However,asanunsupervised
learning method, it requires making choices that are nontrivially influenced by the nature of the data involved.
The aim of this paper is to verify usefulness of the time series clustering method for macroeconomics research,
and to develop the most suitable methodology. By extensively testing various possibilities, we arrive at a choice
of a dissimilarity measure (compression\-based dissimilarity measure, or CDM) which is particularly suitable
for clustering macroeconomic variables. We check that the results are stable in time and reflect large\-scale
phenomena such as crises. We also successfully apply our findings to analysis of national economies, specifically
to identifying their structural relations.
Avella\-Medina, M. (2020\). “Robust Methods for High\-Dimensional Regression and Covariance Matrix Estimation .”
In:Macroeconomic Forecasting in the Era of Big Data . Springer International Publishing, pp. 625–653\.
We review some basic ideas of the robust statistics literature and define tools that allows us to construct robust
statistical procedures. We show how these ideas, originally developed for fixed dimensional settings, can also
be applied to high\-dimensional problems where the number of unknown parameters can be larger than the
sample size. In particular, we build on the theory of M\-estimators and adapt it to handle the problems of
high\-dimensional regression and covariance matrix estimation via regularization. For the former problem we
show that penalized M\-estimators for high\-dimensional generalized linear models can lead to estimators that
are consistent when the data is nice and contains no contaminated observations, while importantly remaining
stable in the presence of a small fraction of outliers. For the problem of covariance estimation we show that
M\-estimators be used to significantly weaken the typical requirement of having sub\-Gaussian distributions to
assuming only a few finite moments. This relaxation cannot be achieved by regularizing the sample covariance
as in classical fixed dimensional regimes.
Avellaneda, M. and Serur, J. A. (2020\). “Hierarchical PCA and Modeling Asset Correlations .” In:arXiv e\-Print .
Modeling cross\-sectional correlations between thousands of stocks, across countries and industries, can be chal\-
lenging. In this paper, we demonstrate the advantages of using Hierarchical Principal Component Analysis
(HPCA) over the classic PCA. We also introduce a statistical clustering algorithm for identifying of homoge\-
neous clusters of stocks, or ”synthetic sectors”. We apply these methods to study cross\-sectional correlations in
the US, Europe, China, and Emerging Markets.
Aw, E. N. W., Chen, S., Dornick, C. R., and Jiang, J. Q. (2018\). “The art of losing in investing: harvesting tax
losses for a positive impact .” In:The Journal of Wealth Management 21(1\), pp. 18–26\.
Paying taxes is universally disliked. Tax\-loss harvesting strategies help offset the capital gains tax investors
incur. Tax\-loss harvesting involves selling stocks that have returned negative over a recent time period. These
recognized losses can offset investment gains and therefore lower the investor capital gains tax bill. The authors
argue that tax\-loss harvesting strategies are smart beta momentum strategies in disguise. They also argue that
just as momentum strategies are managed year\-round, tax\-loss harvesting strategies should be too, not just in
December.
24Aydemir, Z. (2020\). “Portfolio Construction Using First Principles Preference Theory and Machine Learning .” In:
The Journal of Financial Data Science 2(4\), pp. 105–123\.
The author develops a novel approach to portfolio construction that builds on the first principles preference
theory, incorporating characteristics of portfolios beyond the mean and variance of returns typical of the state\-
of\-the art mean\-variance optimization. Specifically, the author adds skewness and kurtosis of return distributions
to the framework. This portfolio framework is proposed with the intent to make it easily accessible conceptually
and easily implementable in practice so that it will be of pragmatic value to investment professionals. This
imperative of practical feasibility leads to the utilization of standard machine learning techniques that proved
effective in overcoming the methodological intricacies associated with mean\-variance optimization. Furthermore,
theauthorallowsforamultiplicityofoptimalportfoliooutcomes,leavingtotheinvestorsome\-albeitconstrained
\- discretion in portfolio choice within a class of similarly optimal portfolios. In a Monte Carlo setting that is
rich enough to incorporate co\-skewness and tail dependencies aside from simple correlation structures between
returns, the suggested framework generates more realistic portfolio solutions than mean\-variance optimization.
Bade, A., Frahm, G., and Jaekel, U. (2009\). “A general approach to Bayesian portfolio optimization .” In:Mathe\-
matical Methods of Operations Research 70 (3337\).
We develop a general approach to portfolio optimization taking account of estimation risk and stylized facts of
empirical finance. This is done within a Bayesian framework. The approximation of the posterior distribution
of the unknown model parameters is based on a parallel tempering algorithm. The portfolio optimization is
done using the first two moments of the predictive discrete asset return distribution. For illustration purposes
we apply our method to empirical stock market data where daily asset log\-returns are assumed to follow an
orthogonal MGARCH process with t\-distributed perturbations. Our results are compared with other portfolios
suggested by popular optimization strategies.
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
Bai, X., Scheinberg, K., and Tutuncu, R. (2016\). “Least\-squares approach to risk parity in portfolio selection .” In:
Quantitative Finance 16(3\), pp. 357–376\.
The risk parity portfolio selection problem aims to find such portfolios for which the contributions of risk from
all assets are equally weighted. Portfolios constructed using the risk parity approach are a compromise between
two well\-known diversification techniques: minimum variance optimization and the equal weighting approach.
In this paper, we discuss the problem of finding portfolios that satisfy risk parity over either individual assets
or groups of assets. We describe the set of all risk parity solutions by using convex optimization techniques
over orthants and we show that this set may contain an exponential number of solutions. We then propose an
alternative non\-convex least\-squares model whose set of optimal solutions includes all risk parity solutions, and
propose a modified formulation which aims at selecting the most desirable risk parity solution according to a
given criterion. When general bounds are considered, a risk parity solution may not exist. In this case, the non\-
convex least\-squares model seeks a feasible portfolio which is as close to risk parity as possible. Furthermore, we
propose an alternating linearization framework to solve this non\-convex model. Numerical experiments indicate
the effectiveness of our technique in terms of both speed and accuracy.
Bailey, D. H., Borwein, J. M., and Lopez de Prado, M. (2017\). “Stock Portfolio Design and Backtest Overfitting .”
In:Journal of Investment Management 15(1\), pp. 75–87\.
In mathematical finance, backtest overfitting connotes the usage of historical market data to develop an invest\-
ment strategy, where too many variations of the strategy are tried, relative to the amount of data available.
Backtest overfitting is now thought to be a primary reason why investment models and strategies that look
good on paper often disappoint in practice. Models and strategies suffering from overfitting typically target the
specific idiosyncrasies of a limited dataset, rather than any general behavior, and, as a result, often perform
25erratically when presented with new data. In this study, we address overfitting in the context of designing a
mutual fund or investment portfolio as a weighted collection of stocks. Very often a newly minted equity\-based
fund of this type has been designed by an exhaustive computer\-based search of some sort to obtain an optimal
weighting that exhibits excellent performance based, say, on the past 10 or 20 years’ historical market data, and
the fund often highlights this backtest performance.
Baitinger, E., Dragosch, A., and Topalova, A. (2017\). “Extending the Risk Parity Approach to Higher Moments: Is
There Any Value Added? ” In:The Journal of Portfolio Management 43(2\), pp. 27–36\.
The popular risk parity approach is based on volatility as the sole risk measure and therefore lacks the consid\-
eration of tail risk. This fact makes risk parity portfolios vulnerable to tail events. In this article, the authors
address this issue by showing how higher\-risk\-moment terms can be consistently incorporated into risk parity
optimization.Inaddition,theypresentanoveloptimizationapproachinwhichoptimalmomentweightings(pref\-
erences) in the risk parity optimization are imputed from the data. In a broad\-based empirical out\-of\-sample
study and simulation analysis, the authors find superior performance of higher\-moment risk parity portfolios
when the underlying data exhibit significant higher moments and co\-moments. According to the authors, this
makes higher\-moment risk parity portfolios ideal candidates for worst\-case regimes.
Baitinger, E. and Papenbrock, J. (2017\). “Interconnectedness Risk and Active Portfolio Management .” In:Journal
of Investment Strategies 6(2\), pp. 63–90\.
Interconnectedness is an alternative risk concept that so far has earned little attention in the asset management
academia and industry. In this paper, we show that this neglect is not justified, as interconnectedness risk (i) has
onlymoderateornoconnectiontoconventionalportfoliooptimizationinputsand(ii)activeinvestmentstrategies
based on interconnectedness information outperform their conventional peers. Utilizing a multi asset dataset, we
measure interconnectedness risk by the embeddedness intensity, i.e. centrality, of assets in a correlation network,
a concept from graph theory. Using the most common centrality measures, we first conduct empirical similarity
studies analyzing how different centrality scores relate to each other and to conventional portfolio optimization
inputs. Next, we outline how centrality can be incorporated in a risk\-based as well as in a risk\-return\-based
framework. Out\-of\-sample performance studies of centrality\-optimized portfolios prove their competitiveness.
Bandara, K., Bergmeir, C., and Smyl, S. (2020\). “Forecasting across time series databases using recurrent neu\-
ral networks on groups of similar series: A clustering approach .” In:Expert Systems with Applications 140,
pp. 112896\+.
WiththeadventofBigData,nowadaysinmanyapplicationsdatabasescontaininglargequantitiesofsimilartime
series are available. Forecasting time series in these domains with traditional univariate forecasting procedures
leaves great potentials for producing accurate forecasts untapped. Recurrent neural networks (RNNs), and in
particular Long Short Term Memory (LSTM) networks, have proven recently that they are able to outperform
state\-of\-the\-art univariate time series forecasting methods in this context, when trained across all available time
series. However, if the time series database is heterogeneous, accuracy may degenerate, so that on the way
towards fully automatic forecasting methods in this space, a notion of similarity between the time series needs
to be built into the methods. To this end, we present a prediction model that can be used with different types
of RNN models on subgroups of similar time series, which are identified by time series clustering techniques. We
assess our proposed methodology using LSTM networks, a widely popular RNN variant, together with various
clustering algorithms, such as kMeans, DBScan, Partition Around Medoids (PAM), and Snob. Our method
achieves competitive results on benchmarking datasets under competition evaluation procedures. In particular,
in terms of mean sMAPE accuracy it consistently outperforms the baseline LSTM model, and outperforms all
other methods on the CIF2016 forecasting competition dataset.
Bardakci,I.E.andLagoa,C.M.(2019\). “DistributionallyRobustPortfolioOptimization .”In:IEEE 58th Conference
on Decision and Control (CDC) . IEEE.
In this paper we consider the problem of portfolio optimization involving uncertainty in the probability distri\-
bution of the assets returns. Starting with an estimate of the mean and covariance matrix of the returns of the
assets, we define a class of admissible distributions for the returns and show that optimizing the worst\-case risk
of loss can be done in a numerically efficient way. More precisely, we show that determining the asset allocation
that minimizes the distributionally robust risk can be done using quadratic programming and a one line search.
Effectiveness of the proposed approach is shown using academic examples.
Barroso, P. and Saxena, K. (2022\). “Lest we forget: Using Out\-Of\-Sample Errors in Portfolio Optimization .” In:
The Review of Financial Studies 35(3\), pp. 1222–1278\.
26Portfolio optimization often struggles in realistic out\-of\-sample contexts. We deconstruct this stylized fact by
comparing historical forecasts of portfolio optimization inputs with subsequent out\-of\-sample values. We confirm
that historical forecasts are imprecise guides of subsequent values, but we discover the resultant forecast errors
are not entirely random. They have predictable patterns and can be partially reduced using their own history.
Learning from past forecast errors to calibrate inputs (akin to empirical Bayesian learning) generates portfolio
performance that reinforces the case for optimization. Furthermore, the portfolios achieve performance that
meets expectations, a desirable yet elusive feature of optimization methods.
Bartz, D. (2016\). “Advances in high\-dimensional covariance matrix estimation .” PhD thesis. Technical University
Berlin.
Many applications require precise estimates of high\-dimensional covariance matrices. The standard estimator is
the sample covariance matrix, All which is conceptually simple, fast to compute and has favorable properties
in the limit of infinitely many observations. The picture changes When the dimensionality is of the same order:
as the number of observations. In examined cases, the eigenvalues of the sample covariance matrix are highly
biased, the condition number Becomes large and the inversion of the matrix gets numerically unstable. A number
of alternative estimators are superior in the high\-dimensional setting, Which include as subcategories structured
estimators, regularized estimators and spectrum correction methods. In this thesis I contribute to all three areas.
In the area of structured estimation, I focus on models with low intrinsic dimensionality. I analyze the bias in
Factor Analysis, the state\-of\-the\-art factor model and propose Directional Variance Adjustment DVA Factor
Analysis, which Reduces bias and yields improved estimates of the covariance matrix. Analytical shrinkage of
Ledoit and Wolf LW Shrinkage is the most popular regularized estimator. I contribute in three aspects: first,
I Provide A theoretical analysis of the behavior of EV Shrinkage in the presence of pronounced intrinsically
directions, a case of great practical relevance. I did show LW Shrinkage does not perform well in this setting and
propose AOC Shrinkage Which yields significant improvements. Second, I discuss the effect of autocorrelation
on LW Shrinkage and review the Sancetta estimator, to extension of LW Shrinkage to autocorrelated data. I
show, dass die Sancetta estimator is biased and propose a Theoretically and empirically superior estimator with
reduced bias. Third, I propose to extension of shrinkage to shrinkage multiple targets. Multi\-Target Shrinkage is
not restricted to covariance estimation and Allows for many interesting applications Which go beyond regular\-
ization, Including transfer learning. I Provide a detailed theoretical and empirical analysis. Spectrum correction
Approaches the Problem of covariance estimation by Improving the estimates of the eigenvalues of the sample
covariance matrix. I discuss the state\-of\-the\-art approach, Nonlinear Shrinkage, and propose a cross\-validation
based covariance CVC estimator Which yields competitive performance at Increased numerical stability and
greatly reduced complexity and computational cost. On all datasets Considered, CVC is on par or superior in
comparison to the regularized and structured estimators. In the load\-chapter, I conclude with a discussion of
the advantages and disadvantages of all covariance estimators presented in this thesis and give situation\-specific
recommendations. In addition, the appendix contains a systematic analysis of linear discriminant analysis as
a model application, Which sheds light on the interdependency between the generative model of the data and
various covariance estimators. Many applications require high\-dimensional covariance estimates. The standard
estimator is the sample covariance. The sample covariance is conceptually easy to calculate quickly and has good
properties in the limit of infinitely many observations. This changes when the dimensionality has the same order
of magnitude as the number of observations. Then, the eigenvalues of the sample covariance to a high bias, the
condition is great and the inverse numerically unstable. There are numerous alternative estimator that are better
in this application. This can usually be in the subgroups structured estimator divided regularized estimators and
methods for spectrum correction. In this dissertation, I contribute to all of these areas. In structured estimator
I focus on models with low intrinsic dimensionality. I analyzed the systematic error of the factor analysis, the
prior art in the field factor models, and propose Directional Variance Adjustment DVA before which corrects
the systematic errors and improved covariance estimation supplies. Analytical Shrinkage of Ledoit and Wolf
LW Shrinkage is the most widely used regularized estimator. To this end, I provide three contributions: First
I run a theoretical analysis of the behavior of EV Shrinkage in presence of strong eigendirections ago, a case
of great practical relevance. I show that LW Shrinkage unfavorable behavior in this situation and propose the
more powerful AOC Shrinkage before. Second, I discuss the effect of autocorrelation on Shrinkage and adjust
the Sancetta estimator front, an extension of LW Shrinkage for autocorrelated data. I show that the Sancetta
estimator has a bias and suggest a theoretically and empirically superior estimator which has a lower bias. Third,
I propose an extension of Shrinkage Shrinkage for multiple targets.
27Bauder, D., Bodnar, T., Parolya, N., and Schmid, W. (2021\). “Bayesian mean\-variance analysis: optimal portfolio
selection under parameter uncertainty .” In:Quantitative Finance 21(2\), pp. 221–242\.
The paper solves the problem of optimal portfolio choice when the parameters of the asset returns distribution,
for example the mean vector and the covariance matrix, are unknown and have to be estimated by using his\-
torical data on asset returns. Our new approach employs the Bayesian posterior predictive distribution which is
the distribution of future realizations of asset returns given the observable sample. The parameters of posterior
predictive distributions are functions of the observed data values and, consequently, the solution of the opti\-
mization problem is expressed in terms of data only and does not depend on unknown quantities. By contrast,
the optimization problem of the traditional approach is based on unknown quantities which are estimated in
the second step, and lead to a suboptimal solution. We also derive a very useful stochastic representation of the
posterior predictive distribution whose application not only gives the solution of the considered optimization
problem, but also provides the posterior predictive distribution of the optimal portfolio return which can be
used to construct a prediction interval. A Bayesian efficient frontier, the set of optimal portfolios obtained by
employing the posterior predictive distribution, is constructed as well. Theoretically and using real data we show
that the Bayesian efficient frontier outperforms the sample efficient frontier, a common estimator of the set of
optimal portfolios which is known to be overoptimistic.
Baz, J., Davis, J., Sapra, S., Gillmann, N., and Tsai, J. (2020\). “A Framework for Constructing Equity\-Risk\-
Mitigation Portfolios .” In:Financial Analysts Journal 76(3\), pp. 81–98\.
The key trade\-off among equity\-risk\-mitigation strategies is their expected return versus their ability to diversify
equity risk. In particular, the more reliable a strategy’s equity\-hedging properties, the lower its expected return,
and vice versa. This article proposes a framework for optimal equity\-risk\-mitigation portfolio construction. In
our model, the investor maximizes the portfolio’s unconditional expected return, subject to a constraint on its
conditional equity beta. We show that the return to a risk\-mitigation portfolio can be decomposed into hedging
and return\- generating components. We then demonstrate that optimal risk\-mitigation portfolios exhibit better
return\-defensiveness properties relative to the underlying strategies.
Bechis, L. (2020\). “Machine Learning Portfolio Optimization: Hierarchical Risk Parity and Modern Portfolio The\-
ory.” In:ResearchGate e\-Print .
The paper aims at highlighting and analyzing the development of the main portfolio allocation approaches. The
de Prado discovery of the Hierarchical Risk Parity (HRP) algorithm for optimizing a financial portfolio, deeply
questions the efficiency of the Markowitz efficient frontier theory as well as the traditional portfolio allocation
strategies. Adopting a machine learning technique in the asset allocation process, allows to develop a more
robust portfolio in terms of risk minimization and performance metrics. The HRP methodology helps building
a diversified portfolio based on the information contained in the covariance matrix. In the empirical analysis,
the HRP portfolio stands out in the out\-of\-sample test, achieving lower risk indicators compared with other
traditional portfolio construction models.
Becker, F., Gurtler, M., and Hibbeln, M. (2015\). “Markowitz versus Michaud: portfolio optimization strategies
reconsidered .” In:The European Journal of Finance 21(4\), pp. 269–291\.
Several attempts have been made to reduce the impact of estimation errors on the optimal portfolio composi\-
tion. On the one hand, improved estimators of the necessary moments have been developed, and on the other
hand, heuristic methods have been generated to enhance the portfolio performance, for instance, the resampled
efficiency of Michaud. We compare the out\-of\-sample performance of traditional mean variance optimization by
Markowitz with Michaud’s resampled efficiency in a comprehensive simulation study for a large number of rele\-
vant estimators appearing in the literature. In addition, we perform an empirical study to confirm the simulation
results. Within the framework of the analyses we consider different estimation periods as well as unconstrained
and constrained portfolio optimization problems. The main findings are that Markowitz outperforms Michaud
on average but the impact of different estimators and constraints is significantly larger. Precisely, in most sit\-
uations, the estimator of Frost and Savarino proves to work excellent. However, if the variance of estimators is
large, for example, for short observation periods or large samples, it is recommendable to additionally implement
constraints or to use the estimator of Ledoit and Wolf .
Begusic, S. and Kostanjcar,Z. (2019\). “Cluster\-Based Shrinkage of Correlation Matrices for Portfolio Optimization .”
In:11th International Symposium on Image and Signal Processing and Analysis (ISPA) . IEEE, pp. 301–305\.
The estimation of correlation and covariance matrices from asset return time series is a critical step in financial
portfolio optimization. Although sample estimates are reliable when the length of time series is very large
compared to the number of assets, in high\-dimensional settings estimation issues arise. To reduce estimation
28errors and mitigate their propagation to out\-of\-sample performance of portfolios based on noisy estimates,
shrinkage methods are applied. In this paper we consider several shrinkage methods for correlation matrix
estimation and define a cluster\-based shrinkage procedure which introduces information about the structures
of communities identified in asset dependence graphs. To test the considered shrinkage methods we apply them
in a portfolio optimization scenario using the global minimum variance portfolio, and perform backtests on a
large sample of NYSE daily stock return data. We find that shrinkage methods generally improve out\-of\-sample
portfolio performance, and the proposed cluster\-based method yields improved results and portfolios which
outperform other considered methods.
Bellini, F., Cesarone, F., Colombo, C., and Tardella, F. (2021\). “Risk Parity with Expectiles .” In:European Journal
of Operational Research .
A recent popular approach to portfolio selection aims at diversifying risk by looking for the so called Risk Parity
portfolios. These are defined by the condition that the risk contributions of all assets to the global risk of the
portfolioareequal.TheRiskParityapproachhasbeenoriginallyintroducedforthevolatilityriskmeasure.Inthis
paper we consider expectiles as risk measures, we refine results on their differentiability and additivity, and we
show how to define Risk Parity portfolios when the expectiles are used. Furthermore, we propose three different
classes of methods for practically finding Risk Parity portfolios with respect to expectiles, and we compare the
accuracy and efficiency of these methods on real\-world data. Expectiles are also used as risk measures in the
classical risk\-return approach to portfolio selection, where we present a new linear programming formulation.
Benaych\-Georges, F., Bouchaud, J.\-P., and Potters, M. (2021\). “Optimal cleaning for singular values of cross\-
covariance matrices .” In:arXiv e\-Print .
We give a new algorithm for the estimation of the cross\-covariance matrix EXY0of two large dimensional signals
X2Rn,Y2Rpin the context where the number Tof observations of the pair (X; Y )is large but n/Tand
p/Tare not supposed to be small. In the asymptotic regime where n; p; Tare large, with high probability, this
algorithm is optimal for the Frobenius norm among rotationally invariant estimators, i.e. estimators derived
from the empirical estimator by cleaning the singular values, while letting singular vectors unchanged.
Benhamou, E., Saltiel, D., Ohana, J.\-J., Atif, J., and Laraki, R. (2021a). “Deep Reinforcement Learning (DRL)
for Portfolio Allocation .” In:Joint European Conference on Machine Learning and Knowledge Discovery in
Databases , pp. 527–531\.
Deep reinforcement learning (DRL) has reached an unprecedent level on complex tasks like game solving (Go or
StarCraft II), and autonomous driving. However, applications to real financial assets are still largely unexplored
and it remains an open question whether DRL can reach super human level. In this ECML PKKDD demo, we
showcase state\-of\-the\-art DRL methods for selecting portfolios according to financial environment, with a final
network concatenating three individual networks using layers of convolutions to reduce network’s complexity.
The multi entries of our network enables capturing dependencies from common financial indicators features like
risk aversion, citigroup index surprise, portfolio specific features and previous portfolio allocations. Results on
test set show this approach can overperform traditional portfolio optimization methods, with results available
at our demo website http://www.aisquareconnect.com/deeprl/models.html .
Benhamou, E., Saltiel, D., Ohana, J.\-J., Atif, J., and Laraki, R. (2021b). “Deep Reinforcement Learning (DRL) for
Portfolio Allocation .” In:SSRN e\-Print .
Deep reinforcement learning (DRL) has reached an unprecedent level on complex tasks like game solving (Go or
StarCraft II), and autonomous driving. However, applications to real financial assets are still largely unexplored
and it remains an open question whether DRL can reach super human level. In this ECML PKKDD demo, we
showcase state\-of\-the\-art DRL methods for selecting portfolios according to financial environment, with a final
network concatenating three individual networks using layers of convolutions to reduce network’s complexity.
The multi entries of our network enables capturing dependencies from common financial indicators features like
risk aversion, citigroup index surprise, portfolio specific features and previous portfolio allocations. Results on
test set show this approach can overperform traditional portfolio optimization methods.
Benhamou, E., Saltiel, D., Ohana, J.\-J., Atif, J., and Laraki, R. (2021c). “DRLPS: Deep Reinforcement Learning
for Portfolio Selection (Presentation Slides ECML PKDD) .” In:SSRN e\-Print .
Deep reinforcement learning (DRL) has reached an unprecedent level on complex tasks like game solving (Go or
StarCraft II), and autonomous driving. However, applications to real financial assets are still largely unexplored
and it remains an open question whether DRL can reach super human level. In this presentation for the ECML
PKDD demo track, we showcase state\-of\-the\-art DRL methods for selecting portfolios according to financial
environment, with a final network concatenating three individual networks using layers of convolutions to reduce
29network’s complexity. The multi entries of our network enables capturing dependencies from common financial
indicators features like risk aversion, citigroup index surprise, portfolio specific features and previous portfolio
allocations. Results on test set show this approach can overperform traditional portfolio optimization methods.
Benhamou, E., Saltiel, D., Ungari, S., Atif, J., and Mukhopadhyay, A. (2021d). “AAMDRL: Augmented Asset
Management With Deep Reinforcement Learning .” In:SSRN e\-Print .
Can an agent learn efficiently in a noisy and self adapting environment with sequential, non\-stationary and
non\-homogeneous observations? Through trading bots, we illustrate how Deep Reinforcement Learning (DRL)
can tackle this challenge. Our contributions are threefold: (i) the use of contextual information also referred to
as augmented state in DRL, (ii) the impact of a one period lag between observations and actions that is more
realistic for an asset management environment, (iii) the implementation of a new repetitive train test method
called walk forward analysis, similar in spirit to cross validation for time series. Although our experiment is on
trading bots, it can easily be translated to other bot environments that operate in sequential environment with
regime changes and noisy data. Our experiment for an augmented asset manager interested in finding the best
portfolio for hedging strategies shows that AAMDRL achieves superior returns and lower risk.
Benhamou, E., Saltiel, D., Ungari, S., and Mukhopadhyay, A. (2021e). “Bridging the Gap Between Markowitz
Planning and Deep Reinforcement Learning .” In:SSRN e\-Print .
While researchers in the asset management industry have mostly focused on techniques based on financial and
risk planning techniques like Markowitz efficient frontier, minimum variance, maximum diversification or equal
risk parity, in parallel, another community in machine learning has started working on reinforcement learning
and more particularly deep reinforcement learning to solve other decision making problems for challenging task
like autonomous driving, robot learning, and on a more conceptual side games solving like Go. This paper aims
to bridge the gap between these two approaches by showing Deep Reinforcement Learning (DRL) techniques
can shed new lights on portfolio allocation thanks to a more general optimization setting that casts portfolio
allocation as an optimal control problem that is not just a one\-step optimization, but rather a continuous control
optimization with a delayed reward. The advantages are numerous: (i) DRL maps directly market conditions to
actions by design and hence should adapt to changing environment, (ii) DRL does not rely on any traditional
financial risk assumptions like that risk is represented by variance, (iii) DRL can incorporate additional data and
be a multi inputs method as opposed to more traditional optimization methods. We present on an experiment
some encouraging results using convolution networks.
Benichou, R., Lemperiere, Y., Serie, E., Kockelkoren, J., Seager, P., Bouchaud, J. P., and Potters, M. (2017\).
“Agnostic risk parity: taming known and unknown unknowns .” In:Journal of Investment Strategies 6(3\), pp. 1–
12\.
Markowitz’ celebrated optimal portfolio theory generally fails to deliver out\-of\-sample diversification. In this
note, we propose a new portfolio construction strategy based on symmetry arguments only, leading to ”Eigenrisk
Parity”portfolios that achieve equal realized risk on all the principal components of the covariance matrix. This
holds true for any other definition of uncorrelated factors. We then specialize our general formula to the most
agnostic case where the indicators of future returns are assumed to be uncorrelated and of equal variance. This
”Agnostic Risk Parity”(AGP) portfolio minimizes unknown\-unknown risks generated by over\-optimistic hedging
of the different bets. AGP is shown to fare quite well when applied to standard technical strategies such as trend
following.
Beraldi, P., De Simone, F., Violi, A., Consigli, G., and Iaquinta, G. (2012\). “Scenario\-based dynamic corporate
bond portfolio management .” In:IMA Journal of Management Mathematics 23(4\), pp. 341–364\.
The 2008 credit crisis has deeply affected the price of corporate liabilities in both equity and fixed income
secondary markets leading to unprecedented portfolio losses by financial investors. A coordinated intervention by
monetary institutions limited the systemic consequences of the crisis, without, however, avoiding a significant fall
ofcorporatebondpricesacrossinternationalmarkets.Inthisarticle,weanalysealternativeportfoliooptimization
approaches in the fixed income market over the 2008 2009 period, a time in which credit derivative markets
became very illiquid. All policies are analysed relying on a unique set of market and credit scenarios generated
by common and idiosyncratic risk factors on an extended investment universe. The crisis provides an interesting
test period to analyse in particular the potential of dynamic versus static portfolio selection approaches. We
also consider dynamic portfolio strategies based on multistage stochastic programming versus policy rule\-based
methods and analyse their relative performance against a corporate bond index widely adopted in practice as a
market benchmark.
30Berger, T. and Gencay, R. (2020\). “Short\-run wavelet\-based covariance regimes for applied portfolio management .”
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
Bernardi, M., Bonaccolto, G., Caporin, M., and Costola, M. (2020\). “Volatility Forecasting in a Data Rich Envi\-
ronment.” In:Macroeconomic Forecasting in the Era of Big Data . Springer International Publishing, pp. 127–
160\.
This Chapter reviews the main classes of models that incorporate volatility, with a focus on the most recent
advancements in the financial econometrics literature and on the challenges posed by the increased availability
of data. There are limits to the feasibility of all models when the cross\-sectional dimension diverges, unless
strong restrictions are imposed on the model’s dynamics. In the latter case, the models might become feasible
at the expense of reduced economic intuition that can be recovered from the model fit. In turn, this could have
a negative impact on the forecast and the identification of its drivers.
Bernardi, S., Leippold, M., and Lohre, H. (2019\). “Second\-order risk of alternative risk parity strategies .” In:Journal
of Risk21(3\), pp. 1–25\.
The concept of second\-order risk operationalizes the estimation risk induced by model uncertainty in portfolio
construction. We study its contribution to the realized volatility of recently developed alternative risk parity
strategies that invest in an uncorrelated decomposition of the asset universe. For each strategy, we derive closed\-
form solutions for the second\-order risk, subsequently illustrated in empirical analysis based on real market data.
Our results suggest a relation between the contribution of second\-order risk and the sensitivity of a portfolio
to single eigenvectors of the covariance matrix of assets returns. Among the strategies considered, we find the
principal risk parity strategy that invests equally in each eigenvector underlying the variance\-covariance matrix
to be immune to second\-order risk. For the other strategies, second\-order risk can be partially mitigated by
means of statistical methods. In particular, we provide evidence for the eigenvalue adjustment being the most
effective method for correcting the second\-order risk bias.
Bertsimas, D., Brown, D. B., and Caramanis, C. (2011\). “Theory and Applications of Robust Optimization .” In:
SIAM Review 53(3\), pp. 464–501\.
In this paper we survey the primary research, both theoretical and applied, in the area of robust optimization
(RO). Our focus is on the computational attractiveness of RO approaches, as well as the modeling power and
broad applicability of the methodology. In addition to surveying prominent theoretical results of RO, we also
present some recent results linking RO to adaptable models for multistage decision\-making problems. Finally,
we highlight applications of RO across a wide spectrum of domains, including finance, statistics, learning, and
various areas of engineering.
Bessler, W., Holler, J., and Kurmann, P. (2011\). “Hedge Funds and Optimal Asset Allocation: Bayesian Expecta\-
tions, Time\-Varying Investment Opportunities and Mean\-Variance Spanning .” In:SSRN e\-Print .
In this paper we analyze the contribution of hedge funds in optimal asset allocations for different investor
clienteles. The preferences of specific institutional investors are captured by implementing a Bayesian asset
allocation framework that incorporates heterogeneous expectations regarding alpha. Mean\-variance spanning
tests are used to draw inferences on the ability of hedge funds to enhance the efficient frontier. A novel variance
decomposition procedure is employed for analyzing the co\-movement of hedge fund returns with the benchmark
assets. The empirical findings strongly indicate that portfolio benefits of hedge funds are time\-varying and
crucially depend on investor optimism regarding hedge fund alpha. Allocations to hedge funds improve the
globalminimumvarianceportfolioevenaftercontrollingforshort\-sellingrestrictionsandminimumdiversification
constraints.However,thefactorstructureofhedgefundreturnshasbecomemoresimilartothebenchmarkassets
due to dynamics underlying the composition of the aggregate hedge fund universe.
Bessler, W., Opfer, H., and Wolff, D. (2017\). “Multi\-asset portfolio optimization and out\-of\-sample performance: an
31evaluation of Black Litterman, mean\-variance, and naive diversification approaches .” In:The European Journal
of Finance 23(1\), pp. 1–30\.
The Black Litterman model aims to enhance asset allocation decisions by overcoming the problems of mean\-
varianceportfoliooptimization.Weproposeasample\-basedversionoftheBlackLittermanmodelandimplement
it on a multi\-asset portfolio consisting of global stocks, bonds, and commodity indices, covering the period from
January 1993 to December 2011\. We test its out\-of\-sample performance relative to other asset allocation models
and find that Black Litterman optimized portfolios significantly outperform na ive\-diversified portfolios (1/N
rule and strategic weights), and consistently perform better than mean\-variance, Bayes Stein, and minimum\-
variance strategies in terms of out\-of\-sample Sharpe ratios, even after controlling for different levels of risk
aversion, investment constraints, and transaction costs. The BL model generates portfolios with lower risk, less
extreme asset allocations, and higher diversification across asset classes. Sensitivity analyses indicate that these
advantages are due to more stable mixed return estimates that incorporate the reliability of return predictions,
smaller estimation errors, and lower turnover.
Bessler, W. and Wolff, D. (2017\). “Portfolio Optimization with Industry Return Prediction Models .” In:SSRN
e\-Print.
We postulate that utilizing return prediction models with fundamental, macroeconomic, and technical indica\-
tors instead of using historical averages should result in superior asset allocation decisions. We investigate the
predictive power of individual variables for forecasting industry returns in\-sample and out\-of\-sample and then
analyze multivariate predictive regression models including OLS, a regularization technique, principal compo\-
nents, a target\-relevant latent factor approach, and forecast combinations. The gains from using industry return
predictionsareevaluatedinanout\-of\-sampleBlack\-Littermanportfoliooptimizationframework.Weprovideem\-
pirical evidence that portfolio optimization utilizing industry return prediction models significantly outperform
portfolios using historical averages and those being passively managed.
Bhansali, V., Davis, J., Rennison, G., Hsu, J., and Li, F. (2012\). “The Risk in Risk Parity: A Factor\-Based Analysis
of Asset\-Based Risk Parity .” In:The Journal of Investing 21(3\), pp. 102–110\.
The risks embedded in asset\-based risk parity portfolios are explored using a simple, economically motivated
approach. Such an approach can go a long way toward demystifying and making more explicit the drivers of
performance and risks of asset\-based risk parity portfolios. Investors in risk parity can use this approach for
more robust portfolio construction and for benchmarking and differentiating various risk parity approaches.
Bianchi, M. L. and Tassinari, G. L. (2020\). “Forward\-looking portfolio selection with multivariate non\-Gaussian
models.” In:Quantitative Finance 20(10\), pp. 1645–1661\.
In this study, we suggest a portfolio selection framework based on time series of stock log\-returns, option\-
implied information, and multivariate non\-Gaussian processes. We empirically assess a multivariate extension
of the normal tempered stable (NTS) model and of the generalized hyperbolic (GH) one by implementing
an estimation method that simultaneously calibrates the multivariate time series of log\-returns and, for each
margin, the univariate observed one\-month implied volatility smile. To extract option\-implied information, the
connection between the historical measure P and the risk\-neutral measure Q, needed to price options, is provided
by the multivariate Esscher transform. The method is applied to fit a 50\-dimensional series of stock returns,
to evaluate widely known portfolio risk measures and to perform a forward\-looking portfolio selection analysis.
The proposed models are able to produce asymmetries, heavy tails, both linear and non\-linear dependence and,
to calibrate them, there is no need for liquid multivariate derivative quotes.
Bielstein, P. and Hanauer, M. X. (2019\). “Mean\-variance optimization using forward\-looking return estimates .” In:
Review of Quantitative Finance and Accounting 52(3\), pp. 815–840\.
Despite its theoretical appeal, Markowitz mean\-variance portfolio optimization is plagued by practical issues.
It is especially difficult to obtain reliable estimates of a stock expected return. Recent research has therefore
focused on minimum volatility portfolio optimization, which implicitly assumes that expected returns for all
assets are equal. We argue that investors are better off using the implied cost of capital based on analysts
earnings forecasts as a forward\-looking return estimate. Correcting for predictable analyst forecast errors, we
demonstrate that mean\-variance optimized portfolios based on these estimates outperform on both an absolute
and a risk\-adjusted basis the minimum volatility portfolio as well as naive benchmarks, such as the value\-
weighted and equally\-weighted market portfolio. The results continue to hold when extending the sample to
international markets, using different methods for estimating the forward\-looking return, including transaction
costs, and using different optimization constraints.
32Bjerring, T., Ross, O., and Weissensteiner, A. (2017\). “Feature selection for portfolio optimization .” In:Annals of
Operations Research 256, pp. 21–40\.
Most portfolio selection rules based on the sample mean and covariance matrix perform poorly out\-of\-sample.
Moreover, there is a growing body of evidence that such optimization rules are not able to beat simple rules
of thumb, such as 1/N. Parameter uncertainty has been identified as one major reason for these findings. A
strand of literature addresses this problem by improving the parameter estimation and/or by relying on more
robust portfolio selection methods. Independent of the chosen portfolio selection rule, we propose using feature
selection first in order to reduce the asset menu. While most of the diversification benefits are preserved, the
parameter estimation problem is alleviated. We conduct out\-of\-sample back\-tests to show that in most cases
different well\-established portfolio selection rules applied on the reduced asset universe are able to improve alpha
relative to different prominent factor models.
Blay, K., Ghosh, A., Kusiak, S., Markowitz, H., Savoulides, N., and Zheng, Q. (2020\). “Multi\-Period Portfolio
Selection: A Practical Simulation\-Based Framework .” In:Journal Of Investment Management 18(4\).
The topic of optimal portfolio selection over time has garnered significant attention from investment researchers
since the introduction of portfolio theory in 1952\. While computational, theoretical, and numerical methods have
advanced, solutions introduced to date have yet to effectively address many practical aspects of the multi\-period
portfolio selection problem. In this paper, we propose three key requisites for practical multi\-period portfolio
selection solutions that highlight the central challenges of managing portfolios across a multi\- period investment
horizon: effective duration management, incorporating real\-world asset dynamics, and considering investment
frictions and illiquidities. Based on these criteria, we detail an analytical framework for multi\-period portfolio
selection that provides intuition and yields guiding principles that describe how allocations and duration should
evolve across a multi\-period investment horizon, given specific investor objectives. We then introduce a practical
simulation\-based portfolio selection (SBPS) framework and present solutions for common investor objectives
that are not only aligned with intuitive principles but also demonstrate the flexibility afforded by SBPS in
allowing us to address the three stated requisites for practical multi\-period solutions.
Blay, K. A. and Markowitz, H. M. (2016\). “Tax\-Cognizant Portfolio Analysis: A Methodology for Maximizing
After\-Tax Wealth .” In:Journal of Investment Management 14(1\).
The most prevalent methods of incorporating taxes into the portfolio construction process are the preliminary
adjustment of asset allocation inputs for taxes and the post\-optimization application of asset location heuristics.
We argue that these methods are unsatisfactory in that they fail to address taxation dynamics that result from
investment and consumption\-dependent illiquidities. Tax\-Cognizant Portfolio Analysis (TCPA) is proposed as
a methodology that addresses these issues while seeking to maximize expected after\-tax wealth for given levels
of risk. TCPA achieves this through the use of simulation methods to assess the impact of portfolio turnover,
sequence of investment returns, and wealth consumption decisions on after\-tax wealth outcomes from taxable,
tax\-deferred, and tax\-exempt accounts.
Blin, O., Ielpo, F., Lee, J., and Teiletche, J. (2017\). “A Macro Risk\-Based Approach to Alternative Risk Premia
Allocation .” In:Factor Investing . Elsevier, pp. 285–316\.
Alternativeriskpremiaareencounteringgrowinginterestfrominvestors.Thevastmajorityofacademicliterature
has been focusing on describing the alternative risk premia (typically, momentum, carry and value strategies)
individually. In this chapter, we investigate the question of the allocation across a range of cross\-asset alternative
riskpremia.Forthis,wedesignanactivemacrorisk\-basedframeworkthatnotablyaimstoexploitalternativerisk
premia’s varying behavior in different macro regimes. We build long\-term strategic portfolios across economic
regimes, which we dynamically tilt based on point\-in\-time signals related to regimes nowcasting and current
carry. We perform back tests of the allocation strategy in an out\-of\-sample setting.
Bnouachir, N. and Mkhadri, A. (2021\). “Efficient cluster\-based portfolio optimization .” In:Communications in
Statistics \- Simulation and Computation 50, pp. 3241–3255\.
The sample mean and covariance matrix of historical data provide a disappointing out\-of\-sample performance in
mean\-variance portfolio rules. This poor performance is certainly due to the high estimation error incurred in the
optimization model. Our purpose in this article is to find a method that enhances the out\-of\-sample performance
of the portfolio weights. Using hierarchical clustering, we propose an alternative cluster\-based portfolio to obtain
a sequence of cluster assets. On the basis of Gram\-Schmidt orthogonalization, the estimation risk of the data
set becomes the sum of the estimations of the clusters in the sequence. The performance of our method and its
competitors is compared empirically and via some simulations in high dimension.
33Bodnar, T., Mazur, S., and Okhrin, Y. (2017\). “Bayesian estimation of the global minimum variance portfolio .” In:
European Journal of Operational Research 256(1\), pp. 292–307\.
The weights of optimal portfolios are estimated from the Bayesian point. The posterior distributions for the
weights of the GMV portfolio are derived. (Non\-)informative prior is constructed directly for the weights of
the GMV portfolio. The models are compared by using the coverage probabilities of credible intervals. An
empirical illustration about the weights of an international portfolio is provided. In this paper we consider the
estimation of the weights of optimal portfolios from the Bayesian point of view under the assumption that the
conditional distributions of the logarithmic returns are normal. Using the standard priors for the mean vector
and the covariance matrix, we derive the posterior distributions for the weights of the global minimum variance
portfolio. Moreover, we reparameterize the model to allow informative and non\-informative priors directly for
the weights of the global minimum variance portfolio. The posterior distributions of the portfolio weights are
derived in explicit form for almost all models. The models are compared by using the coverage probabilities of
credible intervals. In an empirical study we analyze the posterior densities of the weights of an international
portfolio.
Boginski, V., Butenko, S., Shirokikh, O., Trukhanov, S., and Gil Lafuente, J. (2014\). “A network\-based data mining
approachtoportfolioselectionviaweightedcliquerelaxations .”In:Annals of Operations Research 216(1\),pp.23–
34\.
We introduce a new network\-based data mining approach to selecting diversified portfolios by modeling the
stock market as a network and utilizing combinatorial optimization techniques to find maximum\-weight s\-plexes
in the obtained networks. The considered approach is based on the weighted market graph model, which is used
for identifying clusters of stocks according to a correlation\-based criterion. The proposed techniques provide a
new framework for selecting profitable diversified portfolios, which is verified by computational experiments on
historical data over the past decade. In addition, the proposed approach can be used as a complementary tool
for narrowing down a set of \- candidate\- stocks for a diversified portfolio, which can potentially be analyzed
using other known portfolio selection techniques.
Boileau, P., Hejazi, N. S., Laan, M. J. van der, and Dudoit, S. (2021\). “Cross\-Validated Loss\-Based Covariance
Matrix Estimator Selection in High Dimensions .” In:arXiv e\-Print .
The covariance matrix plays a fundamental role in many modern exploratory and inferential statistical proce\-
dures, including dimensionality reduction, hypothesis testing, and regression. In low\-dimensional regimes, where
the number of observations far exceeds the number of variables, the optimality of the sample covariance matrix
as an estimator of this parameter is well\-established. High\-dimensional regimes do not admit such a convenience,
however. As such, a variety of estimators have been derived to overcome the shortcomings of the sample co\-
variance matrix in these settings. Yet, the question of selecting an optimal estimator from among the plethora
available remains largely unaddressed. Using the framework of cross\-validated loss\-based estimation, we develop
the theoretical underpinnings of just such an estimator selection procedure. In particular, we propose a general
class of loss functions for covariance matrix estimation and establish finite\-sample risk bounds and conditions
for the asymptotic optimality of the cross\-validated estimator selector with respect to these loss functions. We
evaluate our proposed approach via a comprehensive set of simulation experiments and demonstrate its prac\-
tical benefits by application in the exploratory analysis of two single\-cell transcriptome sequencing datasets. A
free and open\-source software implementation of the proposed methodology, the cvCovEst R package, is briefly
introduced.
Bokde, N., Asencio\-Cortes, G., Martinez\-Alvarez, F., and Kulat, K. (2017\). “PSF: introduction to R package for
pattern sequence based forecasting algorithm .” In:The R Journal 9(1\), p. 324\.
This paper discusses about an R package that implements the Pattern Sequence based Forecasting (PSF)
algorithm, which was developed for univariate time series forecasting. This algorithm has been successfully
applied to many different fields. The PSF algorithm consists of two major parts: clustering and prediction. The
clustering part includes selection of the optimum number of clusters. It labels time series data with reference
to such clusters. The prediction part includes functions like optimum window size selection for specific patterns
and prediction of future values with reference to past pattern sequences. The PSF package consists of various
functions to implement the PSF algorithm. It also contains a function which automates all other functions
to obtain optimized prediction results. The aim of this package is to promote the PSF algorithm and to ease
its implementation with minimum efforts. This paper describes all the functions in the PSF package with
their syntax. It also provides a simple example of usage. Finally, the usefulness of this package is discussed by
comparing it to auto.arima and ets, well\-known time series forecasting functions available on CRAN repository.
34Bollerslev,T.,Hood,B.,Huss,J.,andPedersen,L.H.(2018\). “RiskEverywhere:ModelingandManagingVolatility .”
In:The Review of Financial Studies 31(7\), pp. 2729–2773\.
Based on high\-frequency data for more than fifty commodities, currencies, equity indices, and fixed\-income
instruments spanning more than two decades, we document strong similarities in realized volatility patterns
within and across asset classes. Exploiting these similarities through panel\-based estimation of new realized
volatility models results in superior out\-of\-sample risk forecasts, compared to forecasts from existing models
and conventional procedures that do not incorporate the similarities in volatilities. We develop a utility\-based
framework for evaluating risk models that shows significant economic gains from our new risk model. Lastly, we
evaluate the effects of transaction costs and trading speed in implementing different risk models.
Bongiorno, C. and Challet, D. (2020a). “Covariance matrix filtering with bootstrapped hierarchies .” In:arXiv e\-
Print.
Statistical inference of the dependence between objects often relies on covariance matrices. Unless the number
of features (e.g. data points) is much larger than the number of objects, covariance matrix cleaning is necessary
to reduce estimation noise. We propose a method that is robust yet flexible enough to account for fine details of
the structure covariance matrix. Robustness comes from using a hierarchical ansatz and dependence averaging
between clusters; flexibility comes from a bootstrap procedure. This method finds several possible hierarchical
structures in DNA microarray gene expression data, and leads to lower realized risk in global minimum variance
portfolios than current filtering methods when the number of data points is relatively small.
Bongiorno, C. and Challet, D. (2020b). “Reactive Global Minimum Variance Portfolios with k\-BAHC covariance
cleaning.” In:arXiv e\-Print .
We introduce a k\-fold boosted version of our Boostrapped Average Hierarchical Clustering cleaning procedure
for correlation and covariance matrices. We then apply this method to global minimum variance portfolios
for various values of k and compare their performance with other state\-of\-the\-art methods. Generally, we find
that our method yields better Sharpe ratios after transaction costs than competing filtering methods, despite
requiring a larger turnover.
Bongiorno, C. and Challet, D. (2021\). “The Oracle estimator is suboptimal for global minimum variance portfolio
optimisation .” In:arXiv e\-Print .
A common misconception is that the Oracle eigenvalue estimator of the covariance matrix yields the best
realized portfolio performance. In reality, the Oracle estimator simply modifies the empirical covariance matrix
eigenvalues so as to minimize the Frobenius distance between the filtered and the realized covariance matrices.
This leads to the best portfolios only when the in\-sample eigenvectors coincide with the out\-of\-sample ones. In all
theother cases,the optimal eigenvaluecorrection canbe obtainedfrom thesolution ofa Quadratic\-Programming
problem. Solving it shows that the Oracle estimators only yield the best portfolios in the limit of infinite data
points per asset and only in stationary systems.
Boscaljon, B., Filbeck, G., and Ho, C.\-C. (2008\). “Rebalancing strategies for creating efficient portfolios .” In:The
Journal of Investing 17(2\), pp. 93–103\.
This article applies an annual rebalancing strategy to create portfolios of industry leaders and compares the
efficiency of these portfolios with the S\&P 500 Index and the CRSP market index portfolios. For the last four
decades, value\-weighted portfolios consisting of as few as eight or nine securities formed from industry leaders
are more efficient with annual rebalancing than the S\&P 500 and are indistinguishable from the CRSP market
index portfolio. The findings suggest important implications for choosing appropriate benchmarks for measuring
tracking error.
Briere, M. and Signori, O. (2012\). “Inflation\-Hedging Portfolios: Economic Regimes Matter .” In:The Journal of
Portfolio Management 38(4\), pp. 43–58\.
The exceptional rise in government deficits following the subprime crisis, the recent commodity price spikes
and the increase in inflation volatility have revived the debate on medium to long\-term resurgence of inflation.
Using a vector\-autoregressive model, this paper investigates the relationships between asset returns and inflation
and the optimal strategic asset allocation for investors seeking to hedge inflation risk in two different types of
macroeconomic regimes. In a volatile macroeconomic environment marked by countercyclical supply shocks,
cash, inflation\-linked bonds and precious metals play an essential role, while in a more stable environment (
Great Moderation ) with procyclical demand shocks, cash and nominal bonds play the most significant role,
followed by precious metals, real estate and equities. An ambitious investor in terms of required real returns
should have a larger weighting in equities, real estate and precious metals.
35Brodie, J., Daubechies, I., Mol, C. D., Giannone, D., and Loris., I. (2009\). “Sparse and Stable Markowitz Portfolios .”
In:The Proceedings of the National Academy of Sciences 106(30\), pp. 12267–12272\.
We consider the problem of portfolio selection within the classical Markowitz mean\-variance framework, refor\-
mulated as a constrained least\-squares regression problem. We propose to add to the objective function a penalty
proportional to the sum of the absolute values of the portfolio weights. This penalty regularizes (stabilizes) the
optimization problem, encourages sparse portfolios (i.e., portfolios with only few active positions), and allows
accounting for transaction costs. Our approach recovers as special cases the no\-short\-positions portfolios, but
does allow for short positions in limited number. We implement this methodology on two benchmark data sets
constructed by Fama and French. Using only a modest amount of training data, we construct portfolios whose
out\-of\-sample performance, as measured by Sharpe ratio, is consistently and significantly better than that of
the naive evenly weighted portfolio.
Brown, R. A. (2018\). “Intelligent Rebalancing .” In:The Journal of Investing 27(1\), pp. 31–42\.
The rebalancing rule applied to a multiasset class portfolio will have significant impact on both risk and return.
All portfolios managed to a fixed\-weight policy asset allocation using non\-market\-cap weights require periodic
rebalancing because failure to rebalance drives realized asset weights further and further away from policy with
the passage of time. The most common approach to rebalancing adopted by the registered investment advisor,
broker/dealer, and bank trust department segments of the investment industry is fixed time (e.g., monthly or
quarterly). This article demonstrates that frequent fixed\-time rebalancing rules are the most harmful to both
risk and return, serving to increase risk and to reduce return. Improvements can be made by rebalancing less
frequently. Additional enhancements to both risk and return can be obtained by following rebalancing rules that
reflect recent market behaviors (i.e., are path dependent).
Bruder, B., Gaussel, N., Richard, J.\-C., and Roncalli, T. (2016\). “Regularization of Portfolio Allocation .” In:SSRN
e\-Print.
The mean\-variance optimization (MVO) theory of Markowitz (1952\) for portfolio selection is one of the most
important methods used in quantitative finance. This portfolio allocation needs two input parameters, the vector
of expected returns and the covariance matrix of asset returns. This process leads to estimation errors, which
may have a large impact on portfolio weights. In this paper we review different methods which aim to stabilize
the mean\-variance allocation. In particular, we consider recent results from machine learning theory to obtain
more robust allocation.
Bruder, B. and Roncalli, T. (2012\). “Managing Risk Exposures Using the Risk Budgeting Approach .” In:SSRN
e\-Print.
The ongoing economic crisis has profoundly changed the industry of the asset management, by putting risk
management at the heart of most investment processes. This new risk\-based investment style does not rely
on returns forecasts and is therefore assumed to be more robust. In 2011, it has particularly encountered a
great success with the achievement of minimum variance, ERC and risk parity strategies in portfolios of several
large institutional investors. These portfolio constructions are special cases of a more general class of allocation
models, known as the risk budgeting approach. In a risk budgeting portfolio, the risk contribution from each
components is equal to the budget of risk defined by the portfolio manager. Unfortunately, even if risk budgeting
techniques are widely used by market practitioners, they are few results about the behavior of such portfolios
in the academic literature. In this paper, we derive the theoretical properties of the risk budgeting portfolio and
show that its volatility is located between those of minimum variance and weight budgeting portfolios. We also
discuss the existence, uniqueness and optimality of such a portfolio. In a second part of the paper, we propose
several applications of risk budgeting techniques for risk\-based allocation, like risk parity funds and strategic
asset allocation, and equity and bond alternative indexations.
Brunel, J. L. P. (2015\). Goals\-Based Wealth Management . Hoboken, NJ, USA: Wiley. 212 pp.
Goals\-Based Wealth Management is a manual for protecting and growing client wealth in a way that changes
both the services and profitability of the firm. Written by a 35\-year veteran of international wealth education
and analysis, this informative guide explains a new approach to wealth management that allows individuals to
take on a more active role in the allocation of their assets. Coverage includes a detailed examination of the
goals\-based approach, including what works and what needs to be revisited, and a clear, understandable model
that allows advisors to help individuals to navigate complex processes. The companion website offers ancillary
readings, practice management checklists, and assessments that help readers secure a deep understanding of the
key ideas that make goals\-based wealth management work. The goals\-based wealth management approach was
pioneered in 2002, but has seen a slow evolution and only modest refinements largely due to a lack of wide\-
36scale adoption. This book takes the first steps toward finalizing the approach, by delineating the effective and
ineffective aspects of traditional approaches, and proposing changes that could bring better value to practitioners
and their clients. (1\) Understand the challenges faced by the affluent and wealthy (2\) Examine strategic asset
allocation and investment policy formulation (3\) Learn a model for dealing with the asset allocation process
(4\) Learn why the structure of the typical advisory firm needs to change High\-net\-worth individuals face very
specific challenges. Goals\-Based Wealth Management focuses on how those challenges can be overcome while
adhering to their goals, incorporating constraints, and working within the individual’s frame of reference to drive
strategic allocation of their financial assets.
Bruni, R., Cesarone, F., Scozzari, A., and Tardella, F. (2016\). “Real\-world datasets for portfolio selection and
solutions of some stochastic dominance portfolio models .” In:Data in Brief 8, pp. 858–862\.
A large number of portfolio selection models have appeared in the literature since the pioneering work of
Markowitz. However, even when computational and empirical results are described, they are often hard to
replicate and compare due to the unavailability of the datasets used in the experiments. We provide here several
datasets for portfolio selection generated using real\-world price values from several major stock markets. The
datasets contain weekly return values, adjusted for dividends and for stock splits, which are cleaned from errors
asmuchaspossible.Thedatasetsareavailableindifferentformats,andcanbeusedasbenchmarksfortestingthe
performances of portfolio selection models and for comparing the efficiency of the algorithms used to solve them.
We also provide, for these datasets, the portfolios obtained by several selection strategies based on Stochastic
Dominance models (see ”On Exact and Approximate Stochastic Dominance Strategies for Portfolio Selection”
(Bruni et al. \[2])). We believe that testing portfolio models on publicly available datasets greatly simplifies the
comparison of the different portfolio selection strategies.
Bruni, R., Cesarone, F., Scozzari, A., and Tardella, F. (2017\). “On exact and approximate stochastic dominance
strategies for portfolio selection .” In:European Journal of Operational Research 259(1\), pp. 322–329\.
New type of approximate stochastic dominance designed for portfolio selection. Equivalent to minimizing the
expected shortfall of the portfolio below the benchmark. An easily solvable LP model for the practical implemen\-
tation of our approach. Extensive empirical comparison of stochastic dominance models for portfolio selection.
One recent and promising strategy for Enhanced Indexation is the selection of portfolios that stochastically
dominate the benchmark. We propose here a new type of approximate stochastic dominance rule which implies
other existing approximate stochastic dominance rules. We then use it to find the portfolio that approximately
stochastically dominates a given benchmark with the best possible approximation. Our model is initially for\-
mulated as a Linear Program with exponentially many constraints, and then reformulated in a more compact
manner so that it can be very efficiently solved in practice. This reformulation also reveals an interesting finan\-
cial interpretation. We compare our approach with several exact and approximate stochastic dominance models
for portfolio selection. An extensive empirical analysis on real and publicly available datasets shows very good
out\-of\-sample performances of our model.
Bryzgalova, S., Huang, J., and Julliard, C. (2021\). “Bayesian solutions for the factor zoo: we just ran two quadrillion
models.” In:SSRN e\-Print .
We propose a novel, and simple, Bayesian estimation and model selection procedure for cross\-sectional asset
pricing. Our approach, that allows for both tradable and non\-tradable factors, and is applicable to high dimen\-
sional cases, has several desirable properties. First, weak and spurious factors lead to diffuse, and centered at
zero, posteriors for their market price of risk, making such factors easily detectable. Second, posterior inference is
robust to the presence of such factors. Third, we show that flat priors for risk premia lead to improper marginal
likelihoods, rendering model selection invalid. Therefore, we provide a novel prior, that is diffuse for strong
factors but shrinks away useless ones, under which posterior probabilities are well behaved, and can be used
for factor and (non necessarily nested) model selection, as well as model averaging, in large scale problems. We
apply our method to a very large set of factors proposed in the literature, and analyse 2\.25 quadrillion possible
models, gaining novel insights on the empirical drivers of asset returns.
Bun, J., Bouchaud, J.\-P., and Potters, M. (2017\). “Cleaning large correlation matrices: Tools from Random Matrix
Theory.” In:Physics Reports 666, pp. 1–109\.
This review covers recent results concerning the estimation of large covariance matrices using tools from Random
Matrix Theory (RMT). We introduce several RMT methods and analytical techniques, such as the Replica
formalism and Free Probability, with an emphasis on the Marenko\-Pastur equation that provides information
on the resolvent of multiplicatively corrupted noisy matrices. Special care is devoted to the statistics of the
eigenvectors of the empirical correlation matrix, which turn out to be crucial for many applications. We show in
37particular how these results can be used to build consistent ”Rotationally Invariant”estimators (RIE) for large
correlation matrices when there is no prior on the structure of the underlying process. The last part of this review
is dedicated to some real\-world applications within financial markets as a case in point. We establish empirically
the efficacy of the RIE framework, which is found to be superior in this case to all previously proposed methods.
The case of additively (rather than multiplicatively) corrupted noisy matrices is also dealt with in a special
Appendix. Several open problems and interesting technical developments are discussed throughout the paper.
Burggraf, T. (2020\). “Beyond risk parity \- A machine learning\-based hierarchical risk parity approach on cryptocur\-
rencies.” In:Finance Research Letters , p. 101523\.
It has long been known that estimating large empirical covariance matrices can lead to very unstable solutions,
with estimation errors more than offsetting the benefits of diversification. In this study, we employ the Hierarchi\-
cal Risk Parity approach, which applies state\-of\-the\-art mathematics including graph theory and unsupervised
machine learning to a large portfolio of cryptocurrencies. An out\-of\-sample comparison with traditional risk\-
minimization methods reveals that Hierarchical Risk Parity outperforms in terms of tail risk\-adjusted return,
thereby working as a potential risk management tool that can help cryptocurrency investors to better man\-
age portfolio risk. The results are robust to different rebalancing intervals, covariance estimation windows and
methodologies.
Butler, A. and Kwon, R. (2021a). “Integrating Prediction in Mean\-Variance Portfolio Optimization .” In:SSRN
e\-Print.
Many problems in quantitative finance involve both predictive forecasting and decision\-based optimization.
Traditionally, predictive models are optimized with unique prediction\-based objectives and constraints, and
are therefore unaware of how those predictions will ultimately be used in the context of their final decision\-
based optimization. We present a stochastic optimization framework for integrating regression based predictive
models in a mean\-variance portfolio optimization setting. Closed\-form analytical solutions are provided for
the unconstrained and equality constrained case. For the general inequality constrained case, we make use of
recent advances in neural\-network architecture for efficient optimization of batch quadratic\-programs. To our
knowledge, this is the first rigorous study of integrating prediction in a mean\-variance portfolio optimization
setting. We present several historical simulations using global futures data and demonstrate the benefits of the
integrated approach in comparison to the decoupled alternative.
Butler, A. and Kwon, R. H. (2021b). “Data\-driven integration of regularized mean\-variance portfolios .” In:arXiv
e\-Print.
Mean\-variance optimization (MVO) is known to be highly sensitive to estimation error in its inputs. Recently,
normpenalizationofMVOprogramshasproventobeaneffectiveregularizationtechniquethatcanhelpmitigate
the adverse effects of estimation error. In this paper, we augment the standard MVO program with a convex
combination of parameterized L1andL2norm penalty functions. The resulting program is a parameterized
penalized quadratic program (PPQP) whose primal and dual form are shown to be constrained quadratic pro\-
grams (QPs). We make use of recent advances in neural\-network architecture for differentiable QPs and present
a novel, data\-driven stochastic optimization framework for optimizing parameterized regularization structures
in the context of the final decision\-based MVO problem. The framework is highly flexible and capable of jointly
optimizing both prediction and regularization model parameters in a fully integrated manner. We provide sev\-
eral historical simulations using global futures data and highlight the benefits and flexibility of the stochastic
optimization approach.
Caccioli, F., Kondor, I., Marsili, M., and Still, S. (2014\). “Lp regularized portfolio optimization .” In:arXiv e\-Print .
Investors who optimize their portfolios under any of the coherent risk measures are naturally led to regularized
portfolio optimization when they take into account the impact their trades make on the market. We show here
that the impact function determines which regularizer is used. We also show that any regularizer based on
the norm Lp with p\>1 makes the sensitivity of coherent risk measures to estimation error disappear, while
regularizers with p1 do not. The L1 norm represents a border case: its soft implementation does not remove the
instability, but rather shifts its locus, whereas its hard implementation (equivalent to a ban on short selling)
eliminates it. We demonstrate these effects on the important special case of Expected Shortfall (ES) that is on
its way to becoming the next global regulatory market risk measure.
Cai, H. and Schmidt, A. B. (2020\). “Comparing mean\-variance portfolios and equal\-weight portfolios for major US
equity indexes .” In:Journal of Asset Management 21, pp. 326–332\.
We compared performance of mean\-variance portfolios (MVPs) based on Pearson correlations (PeMVPs) and
partial correlations (PaMVPs) with equal\-weight portfolios (EWPs) for several tradable US equity index ETFs.
38We found that performance of MVPs and EWPs depends on two factors: the constituents of the underlying
equity index and its holding period. When a market\-wide index contained super\-high growth technology stocks,
such as FAANNG in the SPDR S\&P 500 ETF, PeMVP being a concentrated growth portfolio unsurprisingly
outperformed more diversified PaMVP and EWP. However, when FAANNG were dropped from the SPDR S\&P
500 ETF, and even in the case of the SPDR S\&P 500 Growth ETF (that does not have relatively low\-performing
value stocks), PaMVP outperformed PeMVP at one\-month holding period. For other US equity index SPDR
ETFs (S\&P 500 Value, S\&P MidCap 400, and S\&P 600 SmallCap), PaMVP was always superior, and EWP
could outperform PeMVP at shorter holding periods.
Cai, Y., Cui, X., Huang, Q., and Sun, J. (2017\). “Hierarchy, cluster, and time\-stable information structure of
correlations between international financial markets .” In:International Review of Economics \& Finance 51,
pp. 562–573\.
This paper investigates the correlations between 52 financial markets located in different countries or regions
from July 2004 through June 2011\. By using a correlation matrix time series and a participation frequency
method based on the random matrix theory, we show that a time\-stable information structure is contained
in the correlations between global financial markets. We further find that the information structure is closely
associated with global market and global geographical factors, and that each financial index’s participation in
the global market factor varies over time and presents dynamics. Two patterns, hierarchy and cluster effects, are
found to be in the dynamics of the indices’ participation in the global market factor. The cluster effect implies
a more concentrated participation during the 2008 financial crisis.
Cajas, D. (2019\). “Robust Portfolio Selection with Near Optimal Centering .” In:SSRN e\-Print .
Quantitative asset allocation models have not been widely adopted by practitioners because they suffer from two
problems: the lack of robustness and diversification of portfolios obtained through these models. To solve these
problems, I developed a new portfolio selection method that can be applied to any convex risk measure. The
procedure begins selecting an optimal portfolio in the efficient frontier, then I define a near optimal region and
finally I define the analytic center as the new optimal portfolio. I com\- pare 30 portfolio optimization models
for 4 asset samples, and the results suggest that the new method overcomes traditional methods in robustness
and diversification.
Carl, U. (2017\). “Understanding Rebalancing and Portfolio Reconstitution .” In:SSRN e\-Print .
This paper analyses the impact of rebalancing and portfolio reconstitution on portfolio returns and factor
exposures.Varyingtherebalancingfrequencyandtheportfolioreconstitutionfrequencyleadstodistinctpatterns
in relative factor exposures. These patterns are symmetric for rebalancing and portfolio reconstitution. Short
term reversal drives the returns at high frequencies, momentum at intermediate frequencies, while value and
long term reversal stand out at low frequencies. The variation in returns at different frequencies can be linked
to macro\-economic variables, in particular the cross\-sectional volatility.
Carta, S. M., Consoli, S., Podda, A. S., Recupero, D. R., and Stanciu, M. M. (2021\). “Ensembling and Dynamic
Asset Selection for Risk\-Controlled Statistical Arbitrage .” In:IEEE Access 9, pp. 29942–29959\.
In recent years, machine learning algorithms have been successfully employed to leverage the potential of iden\-
tifying hidden patterns of financial market behavior and, consequently, have become a land of opportunities
for financial applications such as algorithmic trading. In this paper, we propose a statistical arbitrage trading
strategy with two key elements: an ensemble of regression algorithms for asset return prediction, followed by a
dynamic asset selection. More specifically, we construct an extremely heterogeneous ensemble ensuring model
diversity by using state\-of\-the\-art machine learning algorithms, data diversity by using a feature selection pro\-
cess, and method diversity by using individual models for each asset, as well models that learn cross\-sectional
across multiple assets. Then, their predictive results are fed into a quality assurance mechanism that prunes
assets with poor forecasting performance in the previous periods. We evaluate the approach on historical data
of component stocks of the S\&P500 index. By performing an in\-depth risk\-return analysis, we show that this
setup outperforms highly competitive trading strategies considered as baselines. Experimentally, we show that
the dynamic asset selection enhances overall trading performance both in terms of return and risk. Moreover,
the proposed approach proved to yield superior results during both financial turmoil and massive market growth
periods, and it showed to have general application for any risk\-balanced trading strategy aiming to exploit
different asset classes.
Carvalho, C. M., Fisher, J., and Pettenuzzo, D. (2018\). “Optimal Asset Allocation with Multivariate Bayesian
Dynamic Linear Models .” In:SSRN e\-Print .
39We introduce a simulation\-free method to model and forecast multiple asset returns and employ it to investigate
the optimal ensemble of features to include when jointly predicting monthly stock and bond excess returns. Our
approach builds on the Bayesian Dynamic Linear Models of West and Harrison (1997\), and it can objectively
determine, through a fully automated procedure, both the optimal set of regressors to include in the predictive
system and the degree to which the model coefficients, volatilities, and covariances should vary over time. When
appliedtoaportfoliooffivestockandbondreturns,wefindthatourmethodleadstolargeforecastgains,bothin
statisticalandeconomicterms.Inparticular,wefindthatrelativetoastandardno\-predictabilitybenchmark,the
optimal combination of predictors, stochastic volatility, and time\-varying covariances increases the annualized
certainty equivalent returns of a leverage\-constrained power utility investor by more than 500 basis points.
Cesarone, F., Moretti, J., and Tardella, F. (2018\). “Why Small Portfolios Are Preferable and How to Choose Them .”
In:SSRN e\-Print .
One of the fundamental principles in portfolio selection models is minimization of risk through diversification of
the investment. However, this principle does not necessarily translate into a request for investing in all the assets
of the investment universe. Indeed, following a line of research started by Evans and Archer almost 50 years
ago, we provide here further evidence that small portfolios are sufficient to achieve almost optimal in\-sample
risk reduction with respect to variance and to some other popular risk measures, and very good out\-of\-sample
performances. While leading to similar results, our approach is significantly different from the classical one
pioneered by Evans and Archer. Indeed, we describe models for choosing the portfolio of a prescribed size with
the smallest possible risk, as opposed to the random portfolio choice investigated in most of the previous works.
We find that the smallest risk portfolios generally require no more than 15 assets. Furthermore, it is almost
always possible to find portfolios that are just 1% more risky than the smallest risk portfolios and contain no
more than 10 assets. The preference for small optimal portfolios is also justified by recent theoretical results on
the estimation errors for the parameters required by portfolio selection models. Our empirical analysis is based
on some new and on some publicly available benchmark data sets often used in the literature.
Cesarone, F., Mottura, C., Ricci, J. M., and Tardella, F. (2019\). “On the stability of portfolio selection models .” In:
SSRN e\-Print .
One of the main issues in portfolio selection models consists in assessing the effect of the estimation errors of the
parameters required by the models on the quality of the selected portfolios. Several studies have been devoted to
this topic for the minimum variance and for several other minimum risk models. However, no sensitivity analysis
seems to have been reported for the recent popular Risk Parity diversification approach, nor for other portfolio
selection models requiring maximum gain\-risk ratios.Based on artificial and real\-world data, we provide here
empirical evidence showing that the Risk Parity model is always the most stable one in all the cases analyzed.
Furthermore, the minimum risk models are typically more stable than the maximum gain\-risk models, with the
minimum variance model often being the preferable one.
Cesarone, F. and Tardella, F. (2017\). “Equal Risk Bounding is better than Risk Parity for portfolio selection .” In:
Journal of Global Optimization 68(2\), pp. 439–461\.
Risk Parity (RP), also called equally weighted risk contribution, is a recent approach to risk diversification for
portfolio selection. RP is based on the principle that the fractions of the capital invested in each asset should be
chosen so as to make the total risk contributions of all assets equal among them. We show here that the Risk
Parity approach is theoretically dominated by an alternative similar approach that does not actually require
equally weighted risk contribution of all assets but only an equal upper bound on all such risks. This alternative
approach, called Equal Risk Bounding (ERB), requires the solution of a nonconvex quadratically constrained
optimization problem. The ERB approach, while starting from different requirements, turns out to be strictly
linked to the RP approach. Indeed, when short selling is allowed, we prove that an ERB portfolio is actually
an RP portfolio with minimum variance. When short selling is not allowed, there is a unique RP portfolio and
it contains all assets in the market. In this case, the ERB approach might lead to the RP portfolio or it might
lead to portfolios with smaller variance that do not contain all assets, and where the risk contributions of each
asset included in the portfolio is strictly smaller than in the RP portfolio. We define a new riskiness index for
assets that allows to identify those assets that are more likely to be excluded from the ERB portfolio. With these
tools we then provide an exact method for small size nonconvex ERB models and a very efficient and accurate
heuristic for larger problems of this type. In the case of a common constant pairwise correlation among all assets,
a closed form solution to the ERB model is obtained and used to perform a parametric analysis when varying
the level of correlation. The practical advantages of the ERB approach over the RP strategy are illustrated with
some numerical examples. Computational experience on real\-world and on simulated data confirms accuracy
40and efficiency of our heuristic approach to the ERB model also in comparison with some state\-of\-the\-art local
and global optimization codes.
Chakravorty, G., Awasthi, A., Singhal, M., Gupta, S., and Srivastava, S. (2019\). “Active Risk Budgeting is better
than the Tangency Portfolio .” In:SSRN e\-Print .
In this paper, we show empirically that Active Risk Budgeting is a superior portfolio construction methodology
to the tangency portfolio method postulated by Mean Variance Optimization. We compare the performance of
Active Risk Budgeting and Tangency Portfolio in a series of systematic experiments as we gradually increase the
predictive accuracy of the input signal. We find that almost always Active Risk Budgeting has better returns.
Only when the signal used for portfolio construction perfectly knows the Sharpe Ratio of the securities in the
next five days does the performance of the tangency portfolio catch up to Active Risk Budgeting. Given the
results, we would recommend the use of Active Risk Budgeting in portfolio construction for active investment
strategies on derivatives.
Chang, S. M. (2015\). “Double shrinkage estimators for large sparse covariance matrices .” In:Journal of Statistical
Computation and Simulation 85(8\), pp. 1497–1511\.
Covariance matrices play an important role in many multivariate techniques and hence a good covariance
estimation is crucial in this kind of analysis. In many applications a sparse covariance matrix is expected
due to the nature of the data or for simple interpretation. Hard thresholding, soft thresholding, and generalized
thresholdingwerethereforedevelopedtothisend.However,theseestimatorsdonotalwaysyieldwell\-conditioned
covariance estimates. To have sparse and well\-conditioned estimates, we propose doubly shrinkage estimators:
shrinking small covariances towards zero and then shrinking covariance matrix towards a diagonal matrix.
Additionally,arichnessindexisdefinedtoevaluatehowrichacovariancematrixis.Accordingtooursimulations,
the richness index serves as a good indicator to choose relevant covariance estimator.
Chaudhuri, S., Burnham, T. C., and Lo, A. W. (2020\). “An Empirical Evaluation of Tax\-Loss Harvesting Alpha .”
In:Financial Analysts Journal 76(3\), pp. 99–108\.
Advances in financial technology have made tax\-loss harvesting strategies potentially more feasible for retail
investors. We evaluate the magnitude of this ”tax alpha” work using historical data from the Center for Research
in Securities Prices monthly database for the 500 securities with the largest market capitalization from 1926 to
2018\. We fin d that a tax\-loss harvesting strategy yields a geometric average of 51 basis points per year from 1926
to 2018\. However, this tax alpha is highly variable: over four successive 23\-year periods, the tax alpha ranged
from 26 to 88 basis points per annum, hence investors will need to factor in this variability in their assessment
of the tax alpha. Three market factors contribute to these returns: higher volatility, higher dispersion of the
individual returns, and lower overall return for the market. Also, although tax alphas are mostly positive, the
largest magnitudes occur in years when investors are least likely to be able to make use of them immediately,
i.e., when most equity investments are down, in which case their value must be discounted by the impact of
having to carry forward those losses.
Chaudhuri, S. E. and Lo, A. W. (2019\). “Dynamic Alpha: A Spectral Decomposition of Investment Performance
Across Time Horizons .” In:Management Science 65(9\), pp. 4440–4450\.
The value added by an active investor is traditionally measured using alpha, tracking error, and the information
ratio. However, these measures do not characterize the dynamic component of investor activity, nor do they
consider the time horizons over which weights are changed. In this paper, we propose a technique to measure the
valueofactiveinvestmentthatcapturesboththestaticanddynamiccontributionsofaninvestmentprocess.This
dynamicalphaisbasedonthedecompositionofaportfolio’sexpectedreturnintoitsfrequencycomponentsusing
spectral analysis. The result is a static component that measures the portion of a portfolio’s expected return
resulting from passive investments and security selection and a dynamic component that captures the manager’s
timing ability across a range of time horizons. Our framework can be universally applied to any portfolio and
is a useful method for comparing the forecast power of different investment processes. Several analytical and
empirical examples are provided to illustrate the practical relevance of this decomposition.
Chen, J. and Yuan, M. (2016\). “Efficient Portfolio Selection in a Large Market .” In:Journal of Financial Econo\-
metrics14(3\), pp. 496–524\.
Recent empirical studies show that the estimated Markowitz mean\-variance portfolios oftentimes perform rather
poorly when there are more than several assets in the investment universe. In this article, we argue that such
disappointing performance can be largely attributed to the estimation error incurred in sample mean\-variance
portfolios, and therefore could be improved by utilizing more efficient estimating strategies. In particular, we
show that this ”Markowitz optimization enigma”( Michaud, 1989 ) could be resolved by carefully balancing
41the tradeoff between the estimation error and systematic error through the so\-called subspace mean\-variance
analysis.Inadditiontotheconsistentimprovementobservedonrealandsimulateddatasets,weprovethat,under
an approximate factor model, it is possible to use this strategy to construct portfolio rules whose performance
closely resemble that of theoretical mean\-variance efficient portfolios in a large market.
Chen, S. D. and Lim, A. E. B. (2020\). “A Generalized Black\-Litterman Model .” In:Operations Research 68(2\),
pp. 381–410\.
The Black\-Litterman model provides a framework for combining the forecasts of a backward\-looking equilibrium
model with the views of (several) forward\-looking experts in a portfolio allocation decision. The classical version
uses the capital asset pricing model to specify expected returns, and assumes that expert views are unbiased
noisy observations of future returns. It combines the two using Bayes’ rule and the portfolio allocation decision
is made on the basis of the updated forecast. The classical Black\-Litterman model assumes that the equilibrium
and expert models are accurately specified. This is generally not the case, however, and there may be substantial
efficiency loss if misspecification is ignored. In this paper, we formulate a generalized Black\-Litterman model that
accounts for both misspecification and bias in the equilibrium and expert models. We show how to calibrate
this model using historical view and return data, and study the value of our generalized model for portfolio
construction. More generally, this paper shows how the views of multiple experts can be modeled as a Bayesian
graphical model and estimated using historical data, which may be of interest in applications that involve the
aggregation of expert opinions for the purpose of decision making.
Cheung, W. (2010\). “The Black Litterman model explained .” In:Journal of Asset Management 11(4\), pp. 229–243\.
Active portfolio management is about leveraging information. The Black and Litterman Global Portfolio Op\-
timisation Model (BL) sets information processing in a Bayesian analytic framework. In this framework, the
portfolio manager needs only produce views and the model translates the views into security return forecasts.
As a portfolio construction tool, the BL model is appealing both in theory and in practice. Although there
has been no shortage of literature exploring it, the model still appears somehow mysterious, and suffers from
practical issues. This article is dedicated to enabling a better understanding of this model, and features: an
economic interpretation; a clarification of the model’s assumptions and formulation; implementation guidance;
a dimension\-reduction technique to enable large portfolio applications; a full proof of the main result in the
Appendix. We also provide a checklist of other practical issues that we aim to address in our forthcoming
articles.
Chevalier, G., Coqueret, G., and Raffinot, T. (2022\). “Supervised portfolios .” In:SSRN e\-Print .
Weproposeanassetallocationstrategythatengineersoptimalweightsbeforefeedingthemtoasupervisedlearn\-
ing algorithm. In contrast to the traditional approaches, the machine is able to learn risk measures, preferences
and constraints beyond simple expected returns, within a flexible, forward\-looking and non\-linear framework.
Our empirical analysis illustrates that predicting the optimal weights directly instead of the traditional two step
approach leads to more stable portfolios with statistically better risk\-adjusted performance measures.
Chhabra, A. B. (2015\). The Aspirational Investor: Taming the Markets to Achieve Your Life’s Goals . HarperBusi\-
ness. 245 pp.
The Chief Investment Officer of Merrill Lynch Wealth Management explains why goals, not markets, should be
the primary focus of your investment strategy\-and offers a practical, innovative framework for making smarter
choices about aligning your goals to your investment strategy. The Aspirational Investor is a practical, innovative
approach to managing wealth based on key goals and the careful allocation of risks rather than responding to the
whims of the financial markets. Chhabra introduces his ”Wealth Allocation Framework,” which accommodates
the three seemingly incompatible objectives that must underpin every sound wealth management plan: the need
for financial security in the face of known and unknowable risks; the need to maintain current living standards
over time despite inflation; and the need to pursue aspirational goals for wealth creation.
Chincarini, L. B. and Kim, D. (2012\). “Uses and Misuses of the Black\-Litterman Model in Portfolio Construction .”
In:SSRN e\-Print .
The Black\-Litterman model has gained popularity in applications in the area of quantitative equity portfolio
management. Unfortunately, many recent applications of the Black\-Litterman to novel aspects of quantitative
portfolio management have neglected the rigor of the original Black\-Litterman modelling. In this article, we
critically examine some of these applications from a Bayesian perspective. We identify three reasons why these
applications may create losses to investors. These three reasons are: (1\) Using a prior without anchoring the
prior to an equilibrium model (2\) Using a prior and an equilibrium model that conflict with one another (3\)
Ignoring the implications of the estimation error of the variance\-covariance matrix. We also quantify the loss
42first analytically, and also numerically based on historical data on 10 major world stock market indices. Our
conservative estimate of the loss is around a 1 percent reduction in the annualized return of the portfolio.
Choi,D.,Jiang,W.,andZhang,C.(2022\). “Alphagoeverywhere:machinelearningandinternationalstockreturns .”
In:SSRN e\-Print .
We apply machine learning techniques and use stock characteristics to predict the cross\-section of stock returns
in 33 international markets. We conduct a stringent test to allay concerns about overfitting: the models are
trained with past U.S. data and used to predict international stock returns. With fewer variables (based on
past returns, size, volume, and accounting information) as inputs, we arrive at a conclusion similar to that
in previous studies predicting U.S. stock returns with hundreds of stock characteristics and macroeconomic
variables; complex methods outperform linear models in terms of both predicting returns and generating profits.
We achieve even stronger results when the models are trained separately for each market, allowing for country\-
specific return\-characteristic relationships. In most markets, we obtain out\-of\-sample R2 and Sharpe ratios that
are comparable to those in previous studies. Neural network models, which can handle complicated interactions
among the predictors, produce the best results among various machine learning methods.
Choi, Y.\-G., Lim, J., and Choi, S. (2019\). “High\-dimensional Markowitz portfolio optimization problem: empirical
comparison of covariance matrix estimators .” In:Journal of Statistical Computation and Simulation 89(7\),
pp. 1278–1300\.
We compare the performance of recently developed regularized covariance matrix estimators for Markowitz’s
portfolio optimization and of the minimum variance portfolio (MVP) problem in particular. We focus on seven
estimators that are applied to the MVP problem in the literature; three regularize the eigenvalues of the sample
covariance matrix, and the other four assume the sparsity of the true covariance matrix or its inverse. Compar\-
isons are made with two sets of long\-term S\&P 500 stock return data that represent two extreme scenarios of
active and passive management. The results show that the MVPs with sparse covariance estimators have high
Sharpe ratios but that the naive diversification (also known as the (on market share) portfolio) still performs
well in terms of wealth growth.
Chopra, V. K. and Ziemba, W. T. (1993\). “The Effect of Errors in Means, Variances, and Covariances on Optimal
Portfolio Choice .” In:The Journal of Portfolio Management 19(22\), pp. 6–11\.
For investors with moderate to high risk tolerance, the cash equivalent loss for errors in means is an order of
magnitude greater than that for errors in variances or covariances.
Ciliberti, S. and Gualdi, S. (2020\). “Portfolio Construction Matters .” In:The Journal of Portfolio Management
46(7\), pp. 46–57\.
The role of portfolio construction in the implementation of equity market neutral factors is often underestimated.
Taking the classical momentum strategy as an example, the authors show that one can significantly improve
the main strategy’s features by properly taking care of this key step. More precisely, an optimized portfolio
construction algorithm allows one to significantly improve the Sharpe ratio, reduce sector exposures and volatil\-
ity fluctuations, and mitigate the strategy’s skewness and tail correlation with the market. These results are
supported by long\-term, worldwide simulations and are shown to be universal. The authors’ findings are also
general and hold true for a number of other equity factors. Finally, the authors discuss the details of a more
realistic setup in which they also deal with transaction costs.
Clemente, G. P., Grassi, R., and Hitaj, A. (2019\). “Smart network based portfolios .” In:arXiv e\-Print .
In this article we deal with the problem of portfolio allocation by enhancing network theory tools. We use
the dependence structure of the correlations network in constructing some well\-known risk\-based models in
which the estimation of correlation matrix is a building block in the portfolio optimization. We formulate and
solve all these portfolio allocation problems using both the standard approach and the network\-based approach.
Moreover, in constructing the network\-based portfolios we propose the use of two different estimators for the
covariance matrix: the sample estimator and the shrinkage toward constant correlation one. All the strategies
under analysis are implemented on two high\-dimensional portfolios having different characteristics, covering
the period from January 2001 to December 2017\. We find that the network\-based portfolio consistently better
performs and has lower risk compared to the corresponding standard portfolio in an out\-of\-sample perspective.
Clemente, G. P., Grassi, R., and Hitaj, A. (2021\). “Asset allocation: new evidence through network approaches .”
In:Annals of Operations Research 299, pp. 61–80\.
The main contribution of the paper is to unveil the role of the network structure in the financial markets
to improve the portfolio selection process, where nodes indicate securities and edges capture the dependence
structure of the system. Three different methods are proposed in order to extract the dependence structure
43between assets in a network context. Starting from this modified structure, we formulate and then we solve
the asset allocation problem. We find that the optimal portfolios obtained through a network\-based approach
are composed mainly of peripheral assets, which are poorly connected with the others. These portfolios, in
the majority of cases, are characterized by an higher trade\-off between performance and risk with respect
to the traditional global minimum variance portfolio. Additionally, this methodology benefits of a graphical
visualization of the selected portfolio directly over the graphic layout of the network, which helps in improving
our understanding of the optimal strategy.
Clements, A. and Doolan, M. B. (2020\). “Combining multivariate volatility forecasts using weighted losses .” In:
Journal of Forecasting 39(4\), pp. 628–641\.
The ability to improve out\-of\-sample forecasting performance by combining forecasts is well established in the
literature. This paper advances this literature in the area of multivariate volatility forecasts by developing two
combination weighting schemes that exploit volatility persistence to emphasise certain losses within the combi\-
nation estimation period. A comprehensive empirical analysis of the out\-of\-sample forecast performance across
varying dimensions, loss functions, sub\-samples and forecast horizons show that new approaches significantly
outperform their counterparts in terms of statistical accuracy. Within the financial applications considered, sig\-
nificant benefits from combination forecasts relative to the individual candidate models are observed. Although
the more sophisticated combination approaches consistently rank higher relative to the equally weighted ap\-
proach, their performance is statistically indistinguishable given the relatively low power of these loss functions.
Finally, within the applications, further analysis highlights how combination forecasts dramatically reduce the
variability in the parameter of interest, namely the portfolio weight or beta.
Cong, L., Tang, K., Wang, J., and Zhang, Y. (2022\). “AlphaPortfolio: Direct Construction Through Deep Rein\-
forcement Learning and Interpretable AI .” In:SSRN e\-Print .
We directly optimize the objectives of portfolio management via reinforcement learning—an alternative to con\-
ventional supervised\-learning\-based paradigms that entail first\-step estimations of return distributions, pricing
kernels, or risk premia. Building upon breakthroughs in AI, we develop multi\-sequence neural network models
tailored to distinguishing features of economic and financial data, while allowing training without labels and po\-
tential market interactions. The resulting AlphaPortfolio yields stellar out\-of\-sample performances (e.g., Sharpe
ratio above two and over 13% risk\-adjusted alpha with monthly re\-balancing) that are robust under various
economic restrictions and market conditions (e.g., exclusion of small stocks and short\-selling). Moreover, we
project AlphaPortfolio onto simpler modeling spaces (e.g., using polynomial\-feature\-sensitivity) to uncover key
drivers of investment performance, including their rotation and nonlinearity. More generally, we highlight the
utility of deep reinforcement learning in finance and invent ”economic distillation” tools for interpreting AI and
big data models.
Conlon, T., Cotter, J., and Kynigakis, I. (2021\). “Machine Learning and Factor\-Based Portfolio Optimization .” In:
arXiv e\-Print .
Weexaminemachinelearningandfactor\-basedportfoliooptimization.Wefindthatfactorsbasedonautoencoder
neural networks exhibit a weaker relationship with commonly used characteristic\-sorted portfolios than popular
dimensionality reduction techniques. Machine learning methods also lead to covariance and portfolio weight
structures that diverge from simpler estimators. Minimum\-variance portfolios using latent factors derived from
autoencoders and sparse methods outperform simpler benchmarks in terms of risk minimization. These effects
are amplified for investors with an increased sensitivity to risk\-adjusted returns, during high volatility periods
or when accounting for tail risk.
Cooper,R.A.andMolyboga,M.(2017\). “Black\-Litterman,exoticbetaandvaryingefficientportfolios:anintegrated
approach .” In:The Journal of Investment Strategies 6(3\), pp. 13–30\.
This paper brings Black\-Litterman optimization, exotic betas and varying starting portfolios together into one
complete,symbioticframework.Theapproachisuniquebecausethesetechniquesareoftenviewedasalternatives
rather than as complements to each other. We first demonstrate the approach using exotic beta as the ”views”
in the Black\-Litterman optimization. This framework benefits investors who already utilize the classic Black\-
Litterman approach and appreciate advances in the exotic beta research, and also those who focus on practical
implementation of exotic betas. We then explore the framework using the risk\-parity portfolio as an efficient
starting portfolio for Black\-Litterman optimization on both theoretical and practical grounds. We demonstrate
that risk parity is a highly effective starting point in many situations. Finally, as part of our discussion, we
derive conditions under which almost any completely diversified portfolio may be used as a starting portfolio in
44the Black\-Litterman process. The integrated methodology developed is robust, flexible and easily implemented,
which means that a wide range of investors can benefit from this framework.
Coqueret,G.andMilhau,V.(2014\). “EstimatingCovarianceMatricesforPortfolioOptimisation .”In:SSRN e\-Print .
We compare 12 estimators of the covariance matrix: the sample covariance matrix, the identity matrix, the
constant\-correlation estimator, three estimators derived from an explicit factor model, three obtained from an
implicit factor model, and three shrunk estimators. Following the literature, we conduct the comparison by
computing the volatility of estimated Minimum Variance portfolios. We do this in two frameworks: first, an
ideal situation where the true covariance matrix would be known, and second, a real\-world situation where it
is unknown. In each of these two cases, we perform the tests with and without short\-sale constraints, and we
assess the impact of the universe and sample sizes on the results. Our findings are in line with those of Ledoit
and Wolf (2003\), in that we confirm that in the absence of short\-sale constraints, shrunk estimators lead, in
general, to the lowest volatilities. With long\-only constraints, however, their performance is similar to that of
principal component estimators. Moreover, the latter estimators tend to imply lower levels of turnover, which is
an important practical consideration.
Costa, G. and Kwon, R. (2020a). “A robust framework for risk parity portfolios .” In:Journal of Asset Management
21(5\), pp. 447–466\.
We propose a robust formulation of the traditional risk parity problem by introducing an uncertainty structure
specifically tailored to capture the intricacies of risk parity. Typical minimum variance portfolios attempt to
introduce robustness by computing the worst\-case estimate of the risk measure, which is not intuitive for risk
parity. Instead, our motivation is to shield the risk parity portfolio against noise in the estimated asset risk
contributions. Thus, we present a novel robust risk parity model that introduces robustness around both the
overall portfolio risk and the assets’ marginal risk contributions. The proposed robust model is highly tractable
and is able to retain the same level of complexity as the original problem. We provide a general procedure
by which to create an uncertainty structure around the asset covariance matrix. We quantify this uncertainty
as a perturbation on the nominal covariance estimate, which allows us to intuitively embed robustness during
optimization. We then propose a specific procedure to construct a robust risk parity portfolio through a factor
modelofassetreturns.Computationalexperimentsshowthattherobustformulationyieldsahigherrisk\-adjusted
rate of return than the nominal model while maintaining a sufficiently risk\-diverse portfolio.
Costa, G. and Kwon, R. (2020b). “Generalized Risk Parity Portfolio Optimization: An ADMM Approach .” In:SSRN
e\-Print.
The risk parity solution to the asset allocation problem yields portfolios where the risk contribution from each
asset is made equal. We consider a generalized approach to this problem. First, we set an objective that seeks
to maximize the portfolio expected return while minimizing portfolio risk. Second, we relax the risk parity
condition and instead bound the risk dispersion of the constituents within a predefined limit. This allows an
investor to prescribe a desired risk dispersion range, yielding a portfolio with an optimal risk\-return profile that
is still well\-diversified from a risk\-based standpoint. We add robustness to our framework by introducing an
ellipsoidal uncertainty structure around our estimated asset expected returns to mitigate estimation error. Our
proposed framework does not impose any restrictions on short selling. A limitation of risk parity is that allowing
of short sales leads to a non\-convex problem. However, we propose an approach that relaxes our generalized risk
parity model into a convex semi\-definite program. We proceed to tighten this relaxation sequentially through the
alternating direction method of multipliers. This procedure iterates between the convex optimization problem
and the non\-convex problem with a rank constraint. In addition, we can exploit this structure to solve the non\-
convex problem analytically and efficiently during every iteration. Numerical results suggest that this algorithm
converges to a higher quality optimal solution when compared to the competing non\-convex problem, and can
also yield a higher ex post risk\-adjusted rate of return.
Costa,G.andKwon,R.H.(2019\). “RiskparityportfoliooptimizationunderaMarkovregime\-switchingframework .”
In:Quantitative Finance 19(33\), pp. 453–471\.
We formulate and solve a risk parity optimization problem under a Markov regime\-switching framework to
improve parameter estimation and to systematically mitigate the sensitivity of optimal portfolios to estimation
error.Aregime\-switchingfactormodelofreturnsisintroducedtoaccountfortheabruptchangesinthebehaviour
of economic time series associated with financial cycles. This model incorporates market dynamics in an effort
to improve parameter estimation. We proceed to use this model for risk parity optimization and also consider
the construction of a robust version of the risk parity optimization by introducing uncertainty structures to the
estimated market parameters. We test our model by constructing a regime\-switching risk parity portfolio based
45on the Fama\-French three\-factor model. The out\-of\-sample computational results show that a regime\-switching
risk parity portfolio can consistently outperform its nominal counterpart, maintaining a similar ex post level of
risk while delivering higher\-than\-nominal returns over a long\-term investment horizon. Moreover, we present a
dynamic portfolio rebalancing policy that further magnifies the benefits of a regime\-switching portfolio.
Costa, G. and Kwon, R. H. (2020c). “A regime\-switching factor model for mean\-variance optimization .” In:Journal
of Risk22(4\), pp. 31–59\.
We formulate a novel Markov regime\-switching factor model to describe the cyclical nature of asset returns in
modern financial markets. Maintaining a factor model structure allows us to easily derive the asset expected
returns and their corresponding covariance matrix. By design, these two parameters are calibrated to better
describe the properties of the different market regimes. In turn, these regime\-dependent parameters serve as the
inputs during mean\-variance optimization, thereby constructing portfolios adapted to the current market envi\-
ronment.Throughthisformulation,theproposedmodelallowsfortheconstructionoflarge,realisticportfoliosat
no additional computational cost during optimization. Moreover, the viability of this model can be significantly
improved by periodically rebalancing the portfolio, ensuring proper alignment between the estimated parameters
and the transient market regimes. An out\-of\-sample computational experiment over a long investment horizon
shows that the proposed regime\-dependent portfolios are better aligned with the market environment, yielding
a higher ex post rate of return and lower volatility than competing portfolios.
Costa, G. and Kwon, R. H. (2021\). “Data\-driven distributionally robust risk parity portfolio optimization .” In:arXiv
e\-Print.
We propose a distributionally robust formulation of the traditional risk parity portfolio optimization problem.
Distributional robustness is introduced by targeting the discrete probabilities attached to each observation
used during parameter estimation. Instead of assuming that all observations are equally likely, we consider an
ambiguity set that provides us with the flexibility to find the most adversarial probability distribution based
on the investor’s desired degree of robustness. This allows us to derive robust estimates to parametrize the
distribution of asset returns without having to impose any particular structure on the data. The resulting
distributionally robust optimization problem is a constrained convex\-concave minimax problem. Our approach
is financially meaningful and attempts to attain full risk diversification with respect to the worst\-case instance of
theportfolioriskmeasure. Wepropose anovelalgorithmic approachtosolvethisminimaxproblem, whichblends
projected gradient ascent with sequential convex programming. By design, this algorithm is highly flexible and
allows the user to choose among alternative statistical distance measures to define the ambiguity set. Moreover,
the algorithm is highly tractable and scalable. Our numerical experiments suggest that a distributionally robust
risk parity portfolio can yield a higher risk\-adjusted rate of return when compared against the nominal portfolio.
Croessmann, R. (2018\). “Gaussian process priors for Bayesian portfolio selection .” In:SSRN e\-Print .
This article shows how asset characteristics can be incorporated into the Bayesian portfolio selection framework.
We use Gaussian process priors to model the belief that assets with similar characteristics are likely to have
similar expected returns. The resulting Bayesian shrinkage estimator biases expected return estimates of assets
with similar characteristics towards each other. A closed\-form solution of the optimal portfolio weights in the
Gaussian process prior framework is derived. Our simulation results and our empirical analysis suggest that
portfolio selection with Gaussian process priors is a competitive alternative to benchmark portfolio selection
approaches from the literature.
Cvitanic, J., Kou, S., Wan, X., and Williams, K. L. (2020\). “Pi portfolio management: reaching goals while avoiding
drawdowns .” In:SSRN e\-Print .
We propose an approach to portfolio selection that explicitly takes into account investors simultaneous in\-
vestment objectives, such as achieving target return levels and avoiding specific drawdowns. Our approach is
consistent with both standard and non\-standard risk preferences, such as those of prospect theory. Instead of
asking the investor to choose between lotteries, transforming this into an estimate of the risk preferences, and
then selecting the portfolio accordingly, we propose to directly offer investors a choice between lotteries” with
varying probabilities of experiencing target levels of profits and losses. Our approach enables investors to flexibly
assess the effectiveness of portfolio choices under various conditions. We discuss implementation considerations
and compare our approach to traditional mean\-variance portfolio selection.
Dai, M., Jin, H., Kou, S., and Xu, Y. (2021\). “Robo\-advising: a dynamic mean\-variance approach .” In:Digital
Finance 3(2\), pp. 81–97\.
In contrast to traditional financial advising, robo\-advising needs to elicit investors’ risk profile via several simple
online questions and provide advice consistent with conventional investment wisdom, e.g., rich and young people
46should invest more in risky assets. To meet the two challenges, we propose to do the asset allocation part of
robo\-advising using a dynamic mean\-variance criterion over the portfolio’s log returns. We obtain analytical and
time\-consistent optimal portfolio policies under jump\-diffusion models and regime\-switching models.
Dai, Z. and Wang, F. (2019\). “Sparse and robust mean\-variance portfolio optimization problems .” In:Physica A:
Statistical Mechanics and its Applications 523, pp. 1371–1378\.
Abstract Mean\-variance portfolios have been criticized because of unsatisfying out\-of\-sample performance and
the presence of extreme and unstable asset weights. The bad performance is caused by estimation errors in
inputs parameters, that is the covariance matrix and the expected return vector, especially the expected return
vector. This topic has attracted wide attention. In this paper, we aim to find better portfolio optimization
model to reduce the undesired impact of parameter uncertainty and estimation errors of mean\-variance portfolio
model. Firstly, we introduce a sparse mean\-variance portfolio model, and give some insight about sparsity.
Secondly, we propose two sparse and robust portfolio models by using objective function regularization and
robust optimization. Finally, three empirical studies are proposed with real market data.
Darolles, S., Gourieroux, C., and Jay, E. (2015\). “Robust Portfolio Allocation with Systematic Risk Contribution
Restrictions .” In:Risk\-Based and Factor Investing . Elsevier, pp. 123–146\.
The standard mean\-variance approach can imply extreme weights in some assets in the optimal allocation and
a lack of stability of this allocation over time. In order to not only improve the robustness of the portfolio
allocation, but also to better control the portfolio turnover and the sensitivity of the portfolio to systematic risk,
it is proposed in this chapter to introduce additional constraints on both the total systematic risk contribution
of the portfolio and its turnover. Our chapter extends the existing literature on risk parity in three directions:
(1\) we consider other risk criteria than the variance, such as the value\-at\-risk (VaR), or the expected shortfall;
(2\) we manage separately the systematic and idiosyncratic components of the portfolio risk; (3\) we introduce a
set of portfolio management approaches which control the degree of market neutrality of the portfolio, for the
strength of the constraint on systematic risk contribution and for the turnover.
Das, S. R., Ostrov, D., Radhakrishnan, A., and Srivastav, D. (2020\). “Dynamic portfolio allocation in goals\-based
wealth management .” In:Computational Management Science 17, pp. 613–640\.
We report a dynamic programming algorithm which, given a set of efficient (or even inefficient) portfolios,
constructsanoptimalportfoliotradingstrategythatmaximizestheprobabilityofattaininganinvestor’sspecified
target wealth at the end of a designated time horizon. Our algorithm also accommodates periodic infusions or
withdrawals of cash with no degradation to the dynamic portfolio’s performance or runtime. We explore the
sensitivity of the terminal wealth distribution to restricting the segment of the efficient frontier available to the
investor. Since our algorithm’s optimal strategy can be on the efficient frontier and is driven by an investor’s
wealth and goals, it soundly beats the performance of target date funds in attaining investors’ goals. These
optimal goals\-based wealth management strategies are useful for independent financial advisors to implement
behavioral\-based FinTech offerings and for robo\-advisors.
Das, S. R., Ostrov, D., Radhakrishnan, A., and Srivastav, D. (2022a). “Dynamic optimization for multi\-goals wealth
management .” In:Journal of Banking \& Finance 140 (106192\).
We develop a dynamic programming methodology that seeks to maximize investor outcomes over multiple,
potentially competing goals (such as upgrading a home, paying college tuition, or maintaining an income stream
in retirement), even when financial resources are limited. Unlike Monte Carlo approaches currently in wide use
in the wealth management industry, our approach uses investor preferences to dynamically make the optimal
determinationforfulfillingornotfulfillingeachgoalandforselectingtheinvestor’sinvestmentportfolio.Thiscan
be computed quickly, even for numerous investor goals spread over different or concurrent time periods, where
each goal may be all\-or\-nothing or may allow for partial fulfillment. The probabilities of attaining each (full or
partial) goal under the optimal scenario are also computed, so the investor can ensure the algorithm accurately
reflects their preference for the relative importance of each of their goals. This approach vastly outperforms
static portfolio strategies and target\-date funds, widely used in the wealth management industry.
Das, S. R., Ostrov, D. N., Casanova, A., Radhakrishnan, A., and Srivastav, D. (2022b). “Optimal Goals\-Based
Investment Strategies For Switching Between Bull and Bear Markets .” In:The Journal of Wealth Management
24(4\), pp. 8–36\.
We solve a dynamic, long\-horizon, goals\-based wealth management problem, given different investment regimes.
In a world with a good regime (bull market) and a bad regime (bear market), an investor who is cognizant
that regime switching occurs has the potential to do better than an investor who assumes only one regime.
However, models with more than one regime incur the additional risk of regime uncertainty. Investors must be
47able to predict which regime is governing the market with reasonable levels of confidence, or they can be worse
off than investors who assume just one regime. Using data from recent history, we develop a framework that
determines how accurate regime prediction needs to be to achieve gains from a regime\-cognizant goals\-based
investing approach.
Davis, J., Hagelstein, P., Lackner, I., and Piziak, R. (2020\). “The Efficient Frontier and International Portfolio
Diversification in Taxable and Tax\-Privileged Accounts .” In:Journal of Finance and Investment Analysis 9(2\),
pp. 59–78\.
In this paper, we consider efficient frontiers associated to two and three fund portfolios consisting of total
domestic bond funds, total domestic equity funds, and total international equity funds. These frontiers are
intended to help inform investment decisions regarding international exposure in taxable and tax\-privileged
accounts.
de Carvalho, R. L., Xiao, L., and Moulin, P. (2014\). “Multi\-Alpha Equity Portfolios: An Integrated Risk Budgeting
Approach for Robust Constrained Portfolios .” In:SSRN e\-Print .
We propose a robust optimization approach to construct realistic constrained multi\-strategy portfolios which
starts with the identification of different sources of alpha and the risk\-budgeting exercise to optimally combine
them. We show how systematic alpha\-capture strategies can be combined with judgmental strategies and how
bottom\-up based strategies for stock picking can be combined with top\-down sector and country allocation
strategies. The approach is shown to be fully transparent for both unconstrained and constrained portfolios
with a discussion of how constraints impact the final optimal portfolio allocation. In particular we show that
the constrained portfolios retain the exposures to systematic risk in the unconstrained target solution as much
as possible, and that specific risk takes the toll of portfolio constraints. Through a realistic back\-tested example
combining different well\-known alpha capture strategies we demonstrate the robustness and transparency of the
approach. Finally we also discuss the advantages of this approach over the alternative process based on selecting
and investing in a mix of different index\-funds implementing off\-the\-shelf active strategies for alpha capture. We
believe that our approach is particularly suited for institutional investors interested in risk budgeting the alpha
in their portfolios while fully understanding the final allocation in their constrained portfolios.
de Castro, L. I., Galvao, A. F., Kim, J. Y., Montes\-Rojas, G., and Olmo, J. (2021\). “Experiments on Portfolio
Selection: A Comparison between Quantile Preferences and Expected Utility Decision Models .” In:SSRN e\-
Print.
’his paper conducts a laboratory experiment to assess the optimal portfolio allocation under quantile preferences
(QP) and compare the model’s predictions with those of the expected utility theory using a mean\-variance (MV)
utility function. We estimate the risk aversion coefficients associated to the individuals’ empirical portfolio
choices under the QP and MV theories, and evaluate the relative predictive performance of each theory. The
experiment assesses individuals’ preferences through a portfolio choice experiment constructed from two assets
thatmayincludearisk\-freeasset. Theresultsofthe experimentconfirmthesuitabilityofboth theoriestopredict
individuals’ optimal choices. Furthermore, the aggregation of results by individual choices offers support to the
MV theory. However, the aggregation of results by task, which is far more informative, provides more support
to the QP theory. The overall message that emerges from this experiment is that individuals’ behavior is better
predicted by the MV model when it is difficult to assess the differences in the lotteries’ payoff distributions but
better described as QP maximizers, otherwise.
De Franco, C., Nicolle, J., and Pham, H. (2018\). “Bayesian learning for the Markowitz portfolio selection problem .”
In:arXiv e\-Print .
We study the Markowitz portfolio selection problem with unknown drift vector in the multidimensional frame\-
work. The prior belief on the uncertain expected rate of return is modeled by an arbitrary probability law,
and a Bayesian approach from filtering theory is used to learn the posterior distribution about the drift given
the observed market data of the assets. The Bayesian Markowitz problem is then embedded into an auxiliary
standard control problem that we characterize by a dynamic programming method and prove the existence
and uniqueness of a smooth solution to the related semi\-linear partial differential equation (PDE). The optimal
Markowitz portfolio strategy is explicitly computed in the case of a Gaussian prior distribution. Finally, we mea\-
sure the quantitative impact of learning, updating the strategy from observed data, compared to non\-learning,
using a constant drift in an uncertain context, and analyze the sensitivity of the value of information w.r.t.
various relevant parameters of our model.
De Franco, C., Nicolle, J., and Pham, H. (2019\). “Dealing with Drift Uncertainty: A Bayesian Learning Approach .”
In:Risks7(1\), p. 5\.
48One of the main challenges investors have to face is model uncertainty. Typically, the dynamic of the assets is
modeled using two parameters: the drift vector and the covariance matrix, which are both uncertain. Since the
variance/covariance parameter is assumed to be estimated with a certain level of confidence, we focus on drift
uncertainty in this paper. Building on filtering techniques and learning methods, we use a Bayesian learning
approach to solve the Markowitz problem and provide a simple and practical procedure to implement optimal
strategy. To illustrate the value added of using the optimal Bayesian learning strategy, we compare it with an
optimal nonlearning strategy that keeps the drift constant at all times. In order to emphasize the prevalence of
the Bayesian learning strategy above the nonlearning one in different situations, we experiment three different
investment universes: indices of various asset classes, currencies and smart beta strategies.
De Nard, G. (2020\). “Oops! I Shrunk the Sample Covariance Matrix Again: Blockbuster Meets Shrinkage .” In:
Journal of Financial Econometrics .
Existingshrinkagetechniquesstruggletomodelthecovariancematrixofassetreturnsinthepresenceofmultiple\-
asset classes. Therefore, we introduce a Blockbuster shrinkage estimator that clusters the covariance matrix
accordingly. Besides the definition and derivation of a new asymptotically optimal linear shrinkage estimator,
we propose an adaptive Blockbuster algorithm that clusters the covariance matrix even if the (number of) asset
classes are unknown and change over time. It displays superior all\-around performance on historical data against
a variety of state\-of\-the\-art linear shrinkage competitors. Additionally, we find that for small\- and medium\-sized
investment universes the proposed estimator outperforms even recent nonlinear shrinkage techniques. Hence,
this new estimator can be used to deliver more efficient portfolio selection and detection of anomalies in the
cross\-section of asset returns. Furthermore, due to the general structure of the proposed Blockbuster shrinkage
estimator, the application is not restricted to financial problems.
De Nard, G., Hediger, S., and Leippold, M. (2020\). “Subsampled factor models for asset pricing: the rise of VASA .”
In:SSRN e\-Print .
We propose a new method, VASA, based on variable subsample aggregation of model predictions for equity
returns using a large\-dimensional set of factors. To demonstrate the effectiveness, robustness, and dimension
reduction power of VASA, we perform a comparative analysis between state\-of\-the\-art machine learning algo\-
rithms. As a performance measure, we explore not only the global predictive but also the stock\-specific R2’s and
their distribution. While the global R2 indicates the average forecasting accuracy, we find that high variability
in the stock\-specific R2’s can be detrimental for the portfolio performance, due to the higher prediction risk.
Since VASA shows minimal variability, portfolios formed on this method outperform the portfolios based on
more complicated methods like random forests and neural nets.
De Nard, G., Ledoit, O., and Wolf, M. (2021\). “Factor Models for Portfolio Selection in Large Dimensions: The
Good, the Better and the Ugly .” In:Journal of Financial Econometrics 19(2\), pp. 236–257\.
This paper injects factor structure into the estimation of time\-varying, large\-dimensional covariance matrices
of stock returns. Existing factor models struggle to model the covariance matrix of residuals in the presence
of time\-varying conditional heteroskedasticity in large universes. Conversely, rotation\-equivariant estimators of
large\-dimensional time\-varying covariance matrices forsake directional information embedded in market\-wide
risk factors. We introduce a new covariance matrix estimator that blends factor structure with time\-varying
conditional heteroskedasticity of residuals in large dimensions up to 1000 stocks. It displays superior all\-around
performance on historical data against a variety of state\-of\-the\-art competitors, including static factor models,
exogenous factor models, sparsity\-based models, and structure\-free dynamic models. This new estimator can be
used to deliver more efficient portfolio selection and detection of anomalies in the cross\-section of stock returns.
De Nard, G. and Zhao, Z. (2021\). “Using, Taming or Avoiding the Factor Zoo? A Double\-Shrinkage Estimator for
Covariance Matrices .” In:SSRN e\-Print .
Existing factor models struggle to model the covariance matrix for a large number of stocks and factors. There\-
fore, we introduce a new covariance matrix estimator that first shrinks the factor model coefficients and then
applies nonlinear shrinkage to the residuals and factors. The estimator blends a regularized factor structure with
conditional heteroskedasticity of residuals and factors and displays superior all\-around performance against vari\-
ous competitors. We show that for the proposed double\- shrinkage estimator, it is enough to use only the market
factor or the most important latent factor(s). Thus there is no need for laboriously taking into account the factor
zoo. Supplementary material for this article is available online.
Dees, B. S., Stankovic, L., Constantinides, A. G., and Mandic, D. P. (2019\). “Portfolio Cuts: A Graph\-Theoretic
Framework to Diversification .” In:arXiv e\-Print .
49Investment returns naturally reside on irregular domains, however, standard multivariate portfolio optimization
methodsareagnostictodatastructure.Tothisend,weinvestigatewaysfordomainknowledgetobeconveniently
incorporated into the analysis, by means of graphs. Next, to relax the assumption of the completeness of graph
topology and to equip the graph model with practically relevant physical intuition, we introduce the portfolio
cut paradigm. Such a graph\-theoretic portfolio partitioning technique is shown to allow the investor to devise
robust and tractable asset allocation schemes, by virtue of a rigorous graph framework for considering smaller,
computationally feasible, and economically meaningful clusters of assets, based on graph cuts. In turn, this
makes it possible to fully utilize the asset returns covariance matrix for constructing the portfolio, even without
the requirement for its inversion. The advantages of the proposed framework over traditional methods are
demonstrated through numerical simulations based on real\-world price data.
Deguest, R., Martellini, L., and Milhau, V. (2022\). “An Empirical Analysis of the Benefits of Corporate Bond
Portfolio Optimization in the Presence of Duration Constraints .” In:The Journal of Fixed Income 31(4\), pp. 50–
82\.
This article analyzes the out\-of\-sample performance of portfolio optimization models in the US corporate bond
universe. In our empirical study, we measure the benefits of naive diversification and find that it eventually
reaches a limit as the number of bonds increases. Also, we observe substantial improvements in the risk\-adjusted
performance of scientific portfolio constructions when compared to simple barbell strategies for the same given
duration.Whenduration constraintsarerelaxed,wefindthatbothnaivelyand scientificallydiversifiedportfolios
outperform cap\-weighted benchmarks in terms of Sharpe ratio.
DeMiguel, V., Garlappi, L., Nogales, F. J., and Uppal, R. (2009\). “A generalized approach to portfolio optimization:
Improving performance by constraining portfolio norms .” In:Management Science 55(5\), pp. 798–812\.
We provide a general framework for finding portfolios that perform well out\-of\-sample in the presence of esti\-
mation error. This framework relies on solving the traditional minimum\-variance problem but subject to the
additional constraint that the norm of the portfolio\-weight vector be smaller than a given threshold. We show
that our framework nests as special cases the shrinkage approaches of Jagannathan and Ma (Jagannathan,
R., T. Ma. 2003\. Risk reduction in large portfolios: Why imposing the wrong constraints helps. J. Finance 58
165\-1684\) and Ledoit and Wolf (Ledoit, O., M. Wolf. 2003\. Improved estimation of the covariance matrix of
stock returns with an application to portfolio selection. J. Empirical Finance 10 603\-621, and Ledoit, O., M.
Wolf. 2004\. A well\-conditioned estimator for large\-dimensional covariance matrices. J. Multivariate Anal. 88
365\-411\) and the 1/N portfolio studied in DeMiguel et al. (DeMiguel, V., L. Garlappi, R. Uppal. 2009\. Optimal
versus naive diversification: How inefficient is the 1/N portfolio strategy? Rev. Financial Stud. 22 191\-1953\).
We also use our framework to propose several new portfolio strategies. For the proposed portfolios, we pro\-
vide a moment\-shrinkage interpretation and a Bayesian interpretation where the investor has a prior belief on
portfolio weights rather than on moments of asset returns. Finally, we compare empirically the out\-of\-sample
performance of the new portfolios we propose to 10 strategies in the literature across five data sets. We find that
the norm\-constrained portfolios often have a higher Sharpe ratio than the portfolio strategies in Jagannathan
and Ma (2003\), Ledoit and Wolf (2003, 2004\), the 1/N portfolio, and other strategies in the literature, such as
factor portfolios.
DeMiguel, V., Martin\-Utrera, A., and Nogales, F. J. (2013\). “Size matters: Optimal calibration of shrinkage esti\-
mators for portfolio selection .” In:Journal of Banking and Finance 37(8\), pp. 3018–3034\.
We carry out a comprehensive investigation of shrinkage estimators for asset allocation, and we find that size
mattersthe shrinkage intensity plays a significant role in the performance of the resulting estimated optimal port\-
folios. We study both portfolios computed from shrinkage estimators of the moments of asset returns (shrinkage
moments), as well as shrinkage portfolios obtained by shrinking the portfolio weights directly. We make several
contributions in this field. First, we propose two novel calibration criteria for the vector of means and the inverse
covariance matrix. Second, for the covariance matrix we propose a novel calibration criterion that takes the con\-
dition number optimally into account. Third, for shrinkage portfolios we study two novel calibration criteria.
Fourth, we propose a simple multivariate smoothed bootstrap approach to construct the optimal shrinkage in\-
tensity. Finally, we carry out an extensive out\-of\-sample analysis with simulated and empirical datasets, and we
characterize the performance of the different shrinkage estimators for portfolio selection.
DeMiguel, V. and Nogales, F. J. (2009\). “Portfolio Selection with Robust Estimation .” In:Operations Research
57(3\), pp. 560–577\.
Mean\-variance portfolios constructed using the sample mean and covariance matrix of asset returns perform
poorly out of sample due to estimation error. Moreover, it is commonly accepted that estimation error in the
50sample mean is much larger than in the sample covariance matrix. For this reason, researchers have recently
focused on the minimum\-variance portfolio, which relies solely on estimates of the covariance matrix, and thus
usually performs better out of sample. However, even the minimum\-variance portfolios are quite sensitive to
estimation error and have unstable weights that fluctuate substantially over time. In this paper, we propose a
class of portfolios that have better stability properties than the traditional minimum\-variance portfolios. The
proposed portfolios are constructed using certain robust estimators and can be computed by solving a single
nonlinear program, where robust estimation and portfolio optimization are performed in a single step. We show
analytically that the resulting portfolio weights are less sensitive to changes in the asset\-return distribution than
those of the traditional portfolios. Moreover, our numerical results on simulated and empirical data confirm that
the proposed portfolios are more stable than the traditional minimum\-variance portfolios, while preserving (or
slightly improving) their relatively good out\-of\-sample performance.
DeMiguel, V., Utrera, A. M., and Uppal, R. (2021\). “Crowding and Liquidity Provision in Factor Investing .” In:
SSRN e\-Print .
The growing number of institutions exploiting factor\-investing strategies raises concerns that crowding may
increase price\-impact costs and erode profits. We identify a mechanism that alleviates crowding–trading diver\-
sification: institutions exploiting different characteristics can reduce each other’s price\-impact costs even when
their rebalancing trades are not negatively correlated. Empirically, trading diversification increases capacity
by 45%, optimal investment by 43%, and profits by 22%. Using a game\-theoretic model, we show that, while
competition to exploit a characteristic erodes its profits because of crowding, competition among institutions
exploiting other characteristics alleviates crowding. Using mutual\-fund holdings, we provide empirical support
for the model’s predictions.
Dempster, M. A. H., Kloppers, D., Medova, E., Osmolovsky, I., and Ustinov, P. (2016\). “Lifecycle Goal Achievement
or Portfolio Volatility Reduction? ” In:The Journal of Portfolio Management 42(2\), pp. 99–117\.
This article is concerned with the use of currently available technology to offer individuals, financial advisors,
and pension fund financial planners detailed prospective financial plans tailored to an individual’s financial
goals and obligations. By taking account of all an individual’s prospective cash flows, including servicing current
liabilities, and simultaneously optimizing prospective spending, saving, asset allocation, tax, and insurance,
etc. using dynamic stochastic optimization, the authors compare the results of their goal\-based fully dynamic
strategy with the financial advisory industry’s representative current best practices. These include piecemeal
fixed\-allocation portfolios for specific goals, target\-date retirement funds, and fixed real\-income post\-retirement
financial products, all using Markowitz mean\-variance optimization based on the very general goal of minimizing
portfolio volatility for a specific portfolio expected return over a finite horizon. Making use of the same data and
marketcalibrated Monte Carlo stochastic simulation for all the alternative portfolio strategies, the authors find
that flexibility is of key importance for both individual portfolio and spending decisions. The authors measure
superiority by the certainty\-equivalent increase in expected utility of individual lifetime consumption (gamma)
and the extra initial capital required by an individual to put the dominated strategy on the same expected\-
utility footing as the optimal dynamic strategy (initial capital gap). They find that the adaptive dynamic goal\-
based portfolio strategy’s performance is far superior to all the industry’s Markowitz\-based approaches. These
empirical results should put paid to the commonly held view that the extra complexity of holistic dynamic
stochastic models is not worth the marginal extra value obtained from their use.
Denault, M. and Simonato, J.\-G. (2022\). “A note on a dynamic goal\-based wealth management problem .” In:
Finance Research Letters 46 (Part B) (102404\).
This short note suggests two improvements for solving the goal\-based wealth management problem proposed by
Das, Ostrov, Radhakrishnan and Srivastav (2020\). The first suggestion smoothes and improves the convergence
of the approximate solutions towards the underlying, continuous solution either by using analytic solutions at the
penultimate time point or by adjusting the wealth grid. The second suggestion pertains to fast matrix products
and is purely computational but has a large impact on the time required to solve the problem. We also propose
a more consistent approximation for the calculation of the return parameters.
Deshmukh, S. and Dubey, A. (2020\). “Improved Covariance Matrix Estimation With an Application in Portfolio
Optimization .” In:IEEE Signal Processing Letters 27, pp. 985–989\.
One of the major challenges in multivariate analysis is the estimation of population covariance matrix from the
sample covariance matrix (SCM). Most recent covariance matrix estimators use either shrinkage transformations
or asymptotic results from Random Matrix Theory (RMT). Both of these techniques try to achieve a similar goal
which is to remove noisy correlations and add structure to SCM to overcome the bias\-variance trade\-off. Both
51methods have their respective pros and cons. In this paper, we propose an improved estimator which exploits
the advantages of these techniques by taking optimally weighted convex combination of covariance matrices
estimated by shrinkage transformation and a filter based on RMT. It is a generalized estimator which can adapt
to changing sampling noise conditions by performing hyperparameter optimization. Using data from six of the
world’s biggest stock exchanges, we show that the proposed estimator outperforms the existing estimators in
minimizing the out\-of\-sample risk of the portfolio and hence predicts population statistics more precisely. The
proposed estimator can be useful in a wide range of machine learning and signal processing applications.
Dey, K. K. and Stephens, M. (2018\). “CorShrink : Empirical Bayes shrinkage estimation of correlations, with
applications .” In:BioRxiv e\-Print .
Estimation of correlation matrices and correlations among variables is a ubiquitous problem in statistics. In
many cases – especially when the number of observations is small relative to the number of variables – some
kind of shrinkage or regularization is necessary to improve estimation accuracy. Here, we propose an Empirical
Bayes shrinkage approach, CorShrink, which adaptively learns how much to shrink correlations by combining
information across all pairs of variables. One key feature of CorShrink, which distinguishes it from most existing
methods, is its flexibility in dealing with missing data. Indeed, CorShrink explicitly accounts for varying amounts
of missingness among pairs of variables. Numerical studies suggest CorShrink is competitive with other popular
correlation shrinkage methods, even when there is no missing data. We illustrate CorShrink on gene expression
datafromGTExproject,whichsuffersfromextensivemissingobservations,andwhereexistingmethodsstruggle.
We also illustrate its flexibility by applying it to estimate cosine similarities between word vectors from word2vec
models, thereby generating more accurate word similarity rankings.
Dichtl, H., Drobetz, W., and Wambach, M. (2014\). “Where is the value added of rebalancing? A systematic com\-
parison of alternative rebalancing strategies.” In: Financial Markets and Portfolio Management .
This study compares the performance of different rebalancing strategies under realistic market conditions by
reportingstatisticalsignificancelevels.OuranalysisisbasedonhistoricaldatafromtheUnitedStates,theUnited
Kingdom, and Germany and comprises three different classes of rebalancing (periodic, threshold, and range
rebalancing). Despite cross\-country differences, our history\-based simulation results show that all rebalancing
strategies outperform a buy\-and\-hold strategy in terms of Sharpe ratios, Sortino ratios, and Omega measures.
The differences in risk\-adjusted performance are not only statistically significant, but also economically relevant.
However, the choice of a particular rebalancing strategy is of only minor economic importance.
DiLellio, J. A. and Ostrov, D. N. (2018\). Constructing Tax Efficient Withdrawal Strategies for Retirees . Tech. rep.
Pepperdine University.
We establish an algorithm that produces an optimal strategy for retirees to withdraw funds between their tax\-
deferred accounts (TDAs), like traditional IRA/401(k) accounts, and their Roth IRA/401(k) accounts, in the
context of a financial model based on American tax law. This optimal strategy follows a geometrically simple,
intuitive approach that can be used to maximize the size of a retiree’s bequest to an heir or, alternatively,
to maximize a retiree’s portfolio longevity. We give examples where retirees following the approach currently
implemented by major investment firms, like Fidelity and Vanguard, will reduce their bequests by approximately
10% or lose 18 months of portfolio longevity compared to our optimal approach. Further, our strategy and
algorithm can be extended to many cases where the retiree has additional, known yearly sources of money, such
as income from part\-time work, taxable investment accounts, and Social Security.
Ding, K.\-w., Chen, Z.\-y., and Huang, N.\-j. (2018\). “Robust mean variance optimization problem under Renyi
divergence information .” In:Optimization 67(2\), pp. 287–307\.
In this paper, we consider the robust mean variance optimization problem where the probability distribution
of assets’ returns is multivariate normal and the uncertain mean and covariance are controlled by a constraint
involving Renyi divergence. We present the closed\-form solutions for the robust mean variance optimization
problem and find that the choice of order parameter which is related to the Renyi divergence measure will not
impact optimal portfolio strategy under the cases that the mean vector and the covariance matrix are uncertain,
respectively. Moreover, we obtain the closed\-form solution for the robust mean variance optimization problem
under the case that the mean vector and the covariance matrix are both uncertain. We illustrate the efficiency
of our results with an example.
Ding, X. and Zhou, Z. (2020\). “Estimation and inference for precision matrices of nonstationary time series .” In:
Annals of Statistics 48(4\), pp. 2455–2477\.
We consider the estimation of and inference on precision matrices of a rich class of univariate locally stationary
linear and nonlinear time series, assuming that only one realization of the time series is observed. Using a
52Cholesky decomposition technique, we show that the precision matrices can be directly estimated via a series
of least squares linear regressions with smoothly time\-varying coefficients. The method of sieves is utilized for
the estimation and is shown to be optimally adaptive in terms of estimation accuracy and efficient in terms of
computational complexity. We establish an asymptotic theory for a class of L2 tests based on the nonparametric
sieve estimators. The latter are used for testing whether the precision matrices are diagonal or banded. A
Gaussian approximation result is established for a wide class of quadratic forms of nonstationary and possibly
nonlinear processes of diverging dimensions which is of interest by itself.
Diris,B.,Palm,F.,andSchotman,P.(2015\). “Long\-TermStrategicAssetAllocation:AnOut\-of\-SampleEvaluation .”
In:Management Science 61(9\), pp. 2185–2202\.
We evaluate the out\-of\-sample performance of a long\-term investor who follows an optimized dynamic trading
strategy.Althoughthedynamicstrategyisabletobenefitfrompredictabilityout\-of\-sample,ashort\-terminvestor
using a single\-period market timing strategy would have realized an almost identical performance. The value
of intertemporal hedge demands in strategic asset allocation appears negligible. The result is caused by the
estimation error in predicting the predictors. A myopic investor only needs to predict one\-period\-ahead expected
returns, but hedge demands also require accurate predictions of the predictor variables. To reduce the problem
of errors in optimized portfolio weights, we consider Bayesian procedures. Myopic and dynamic portfolios are
similarly affected by such modifications, and differences in performance become even smaller.
Dixon, M. F. and Halperin, I. (2021\). “Goal\-based wealth management with generative reinforcement learning .” In:
Risk (Cutting edge) .
A combination of machine learning techniques provides multi\-period portfolio optimisation. Matthew Dixon
and Igor Halperin develop a reinforcement learning (RL) approach to goal\-based wealth management problems
such as optimisation of retirement plans or target date funds. They present G\-Learner: a reinforcement learning
algorithm that does not assume a data generation process and is suitable for noisy data. Their approach is
based on G\-learning, a probabilistic extension of the Q\-learning method of reinforcement learning. In addition
to G\-Learners, which solves the direct RL problem, they develop GIRL, a G\-learning inverse RL algorithm to
infer the investor reward function from the observed trading actions.
Domian, D., Gibson, P., and Nanigian, D. (2015\). “Is Your Tax\-Managed Fund Manager Hiding in the Closet? ” In:
The Journal of Wealth Management 18(2\), pp. 67–76\.
Our study examines the performance, expense, and tax efficiency of domestic equity mutual funds that have
a stated goal of minimizing the taxes paid by their shareholders. We arrive at three main findings. First, on
average, over 95 percent of the variability in the returns on these funds is explained by common factors in
stock returns. Second, there is little difference between the mean values of their expenses and those of their
actively managed counterparts. Third, when compared to their inherently tax\-advantaged passively managed
counterparts, the tax\-managed funds fail to save their investors more money on taxes than their incremental
expenses.
Dose, C. and Cincotti, S. (2005\). “Clustering of financial time series with application to index and enhanced index
tracking portfolio .” In:Physica A: Statistical Mechanics and its Applications 355(1\), pp. 145–151\.
A stochastic\-optimization technique based on time series cluster analysis is described for index tracking and
enhanced index tracking problems. Our methodology solves the problem in two steps, i.e., by first selecting a
subset of stocks and then setting the weight of each stock as a result of an optimization process (asset allocation).
Present formulationtakesinto account constraintson the number of stocksand on the fraction of capital invested
in each of them, whilst not including transaction costs. Computational results based on clustering selection are
compared to those of random techniques and show the importance of clustering in noise reduction and robust
forecasting applications, in particular for enhanced index tracking.
Driessen, J. and Kuiper, I. (2019\). “Rebalancing for Long Term Investors: Why It Pays to Do Less .” In:SSRN
e\-Print.
Inthisstudyweshowthattherebalancefrequencyofamulti\-assetportfoliohasonlylimitedimpactontheutility
of a long\-term passive investor. Although continuous rebalancing is optimal, the loss of a suboptimal strategy
corresponds to up to only 30 basis points of the initial wealth of the investor, assuming market returns are
unpredictable and transaction costs can be ignored. Our results suggest that reducing transaction costs clearly
outweighs the benefit of frequent rebalancing. When we study a setting where asset returns are predictable,
we find that a long\-term investor that ignores this predictability underestimates the benefit of less frequent
rebalancing. In this setting, limiting the frequency to at least once every quarter results in significant higher
utility, even without transaction costs.
53duPlessis,H.andvanRensburg,P.(2020\). “Risk\-basedportfoliosensitivitytocovarianceestimation .”In:Investment
Analysts Journal 49(3\), pp. 243–268\.
Risk\-based portfolio construction methods focus on optimally extracting information from the covariance matrix
ofassetreturns,asopposedtoutilisingforecastsofexpectedreturns,indeterminingtheportfolioallocation.This
improves their robustness to estimation error in means, but this does not mean that they are immune to errors in
estimatingvolatilitiesandcorrelations.Usingacovariancematrixdecompositionthatallowsseparatelyestimated
volatility and correlation models to be recomposed into different models of the covariance matrix, this study
examines the empirical performance impact of using an enhanced estimator of the covariance matrix, relative
to using the historical sample covariance estimator in the context of six risk\-based portfolio optimisations, in a
long\-only constrained equity market setting. It finds that sensitivity to covariance estimation varies significantly
among risk\-based portfolio types and that outperformance of the sample historical covariance estimator is
possible, but rare. As components of the covariance estimate, among volatility models the EWMA volatilities
perform best and GARCH models, poorly. Among correlation models, the Rotationally Invariant Estimator of
Bouchaud, Bun, and Potters (2016\) shows strong performance, along with the classic Ledoit and Wolf (2003\)
Single Market Model Estimator.
Edesess, M. (2017\). “Rebalancing: A Comprehensive Reassessment .” In:SSRN e\-Print .
Investmentadvisors,investmentbooks,andinvestmentcolumnsalmostneverfailtoadviseinvestorstorebalance
their portfolios. Numerous academic articles have been written about it, most of them arguing that it adds
value. Yet the existence and precise nature of that value have remained a subject of intense debate. Most past
articles on rebalancing have reduced the comparison of rebalancing with alternatives such as buy\-and\-hold to a
single summary statistic, either expected return or median return. Due to the different skews in the probability
distributions, however, comparing a single summary statistic does not support the overly broad conclusions that
have often been reached. Comparisons that take the entire distributions into account provide better insight.
Resultsofthosecomparisonsaremixedastowhetherrebalancingaddsvalue.Thisarticleanalyzesthearguments
thathavebeenadvancedforrebalancing,identifyingtheirpointsofvalidityandtheirflaws.Itpresentstheresults
of original empirical research, simulations, and mathematical derivations that together identify how often and
to what extent rebalancing enhances or degrades the performance of an investment portfolio.
Ehling, P. and Heyerdahl\-Larsen, C. (2017\). “Correlations .” In:Management Science 63(6\), pp. 1919–1937\.
Correlations of equity returns have varied substantially over time and remain a source of continuing policy
debate. This paper studies stock market correlations in an equilibrium model with heterogeneous risk aversion.
In the model, preference heterogeneity causes variations in the volatility of aggregate risk aversion from good
to bad states. At times of high volatility in aggregate risk aversion, which is a common factor in returns,
we see high correlations. The model matches average industry return correlations and changes in correlations
from business cycle peaks to troughs and replicates the dynamics of expected excess returns and standard
deviations.Model\-impliedaggregateriskaversionexplainsaverageindustrycorrelations,expectedexcessreturns,
standard deviations, and turnover volatility in the data. We find supportive evidence for the model’s prediction
that industries with low dividend\-consumption correlation have low average return correlation but experience
disproportional increases in return correlations in recessions.
Ehsani, S. and Linnainmaa, J. T. (2021\). “Time\-Series Efficient Factors .” In:SSRN e\-Print .
Factors in prominent asset pricing models are positively serially correlated. We derive the optimal allocation that
transforms an auto\-correlated factor to a ”time\-series efficient” factor. The key determinant of the value of factor
timing is the ratio of a factor’s auto\-correlation to its Sharpe ratio. Time\-series efficient factors earn significantly
higher Sharpe ratios than the original factors and contain all the information found in the original factors.
Momentum strategies profit by timing auto\-correlated factors; they pick up factor ”inefficiencies.” We show
that, rather than augmenting models with the momentum factor, each factor can instead be made time\-series
efficient. An asset pricing model with time\-series efficient factors, such as an efficient Fama\-French five\-factor
model, prices momentum. Time\-series efficient factors also explain more of the co\-variance structure of returns;
they describe the cross section better than the standard factors and align more closely with the true SDF.
El Bernoussi, R. and Rockinger, G. M. (2019\). “Rebalancing with transaction costs: theory, simulations, and actual
data.” In:SSRN e\-Print .
In the absence of transaction costs and the presence of independent returns, a buy\-and\-hold strategy can be
shown to generate higher expected returns than a fixed\-weight strategy, where the portfolio weights are regu\-
larly readjusted/rebalanced to some initial level. This higher expected return comes, however, at a cost: higher
volatility. The resulting trade\-off leads to different rankings of the Sharpe ratio depending on the statistical
54moments of the assets. We theoretically discuss causes affecting the ranking of the Sharpe ratio, and we intro\-
duce an easy\-to\-implement methodology to deal with proportional transaction costs. Under transaction costs,
the buy\-and\-hold strategy as the cheaper approach should be the winner. In various simulation experiments,
we investigate the relevance of transaction costs on rebalancing strategies. Eventually, we consider a realistic
portfolio with a risk\-free asset, bonds, and various stock indices that allows us to demonstrate that in practice,
as long as transaction costs remain small, rebalancing has value for realistic portfolios.
Engle, R. F., Ledoit, O., and Wolf, M. (2019\). “Large Dynamic Covariance Matrices .” In:Journal of Business and
Economic Statistics 37(2\), pp. 363–375\.
AbstractSecond moments of asset returns are important for risk management and portfolio selection. The prob\-
lem of estimating second moments can be approached from two angles: time series and the cross\-section. In time
series, the key is to account for conditional heteroskedasticity; a favored model is Dynamic Conditional Corre\-
lation (DCC), derived from the ARCH/GARCH family started by Engle (1982\). In the cross\-section, the key
is to correct in\-sample biases of sample covariance matrix eigenvalues; a favored model is nonlinear shrinkage,
derived from Random Matrix Theory (RMT). The present paper marries these two strands of literature in order
to deliver improved estimation of large dynamic covariance matrices.
Eom, C. and Park, J. W. (2017\). “Effects of common factors on stock correlation networks and portfolio diversifi\-
cation.” In:International Review of Financial Analysis 49, pp. 1–11\.
Common factors significantly affect the connectivity of the network among stocks. Common factors significantly
affect the distribution of investment weight for stocks. The devised method substantially assist in constructing a
more diversified portfolio. This diversified portfolio achieves better out\-of\-sample performance. These results are
robust in both the Korean and the U.S. stock markets. This study empirically investigates the effects of common
factors on the connectivity of the network among stocks and on the distribution of the investment weights
for stocks. The network is defined as a stock correlation network from the minimal spanning tree (MST), and
portfolio is defined as an efficient portfolio from the Markowitz mean\-variance (MV) optimization function
(MVOF). For these research goals, we devise a method using the comparative correlation matrix (C\-CM), which
does not have the property of a single common factor included in the sample correlation matrix (S\-CM). The
results reveal that common factors clearly affect the changes of connectivity among stocks in the networks, and
that their influence is much greater on stocks with many links to other stocks in the network. Further, common
factors significantly affect the determination of the investment weight’s distribution for stocks from the MVOF.
In particular, among the common factors, a market factor plays a dominant role in both structuring the network
among stocks and in constructing the well\-diversified portfolio. In addition, the devised method of the C\-CM
without the property of the market factor in the S\-CM plays a crucial role in constructing a more diversified
portfolio with better out\-of\-sample performance in the future period. These results are robust in both the Korean
and the U.S. stocks markets.
Fabozzi, F. A., Simonian, J., and Fabozzi, F. J. (2021a). “Risk Parity: The Democratization of Risk in Asset
Allocation .” In:The Journal of Portfolio Management 47(5\), pp. 41–50\.
The risk parity investment model for asset allocation offers an alternative to the mean\-variance framework.
The fundamental idea is that the allocation to different asset classes should not be based on an optimization
that targets a specific return with a minimal level of risk but, rather, should generate a portfolio in which the
contribution to portfolio risk of each asset class is equal, regardless of its expected returns. In this article, the
authors explain the fundamentals of the risk parity investment model and the variants in risk parity strategies
due to the selection of the asset classes to be included in the portfolio, the choice of the risk metric, the
portfolio risk target, how to obtain leverage, associated leverage, whether the selection of the specific investments
within an asset class is made using an active or passive approach, and the tactical risk allocation strategy. In
addition to describing the practical aspects of implementing risk parity strategies, the authors identify the
various shortcomings of the model and some extensions of the basic risk parity model that attempt to address
some of the issues identified by the model’s critics.
Fabozzi, F. J. and Fabozzi, F. A. (2020\). Fundamentals of Institutional Asset Management . World Scientific. 616 pp.
This book provides the fundamentals of asset management. It takes a practical perspective in describing asset
management. Besides the theoretical aspects of investment management, it provides in\-depth insights into the
actual implementation issues associated with investment strategies. The 19 chapters combine theory and practice
based on the experience of the authors in the asset management industry. The book starts off with describing
the key activities involved in asset management and the various forms of risk in managing a portfolio. There is
then coverage of the different asset classes (common stock, bonds, and alternative assets), collective investment
55vehicles, financial derivatives, common stock analysis and valuation, bond analytics, equity beta strategies
(including smart beta), equity alpha strategies (including quantitative/systematic strategies), bond indexing
and active bond portfolio strategies, and multi\-asset strategies. The methods of using financial derivatives
(equity derivatives, interest rate derivatives, and credit derivatives) in managing the risks of a portfolio are
clearly explained and illustrated.
Fabozzi, F. J., Fabozzi, F. A., Lopez de Prado, M., and Stoyanov, S. (2021b). Asset Management: Tools and Issues .
World Scientific. 516 pp.
Long gone are the times when investors could make decisions based on intuition. Modern asset management
draws on a wide\-range of fields beyond financial theory: economics, financial accounting, econometrics/statistics,
management science, operations research (optimization and Monte Carlo simulation), and more recently, data
science (Big Data, machine learning, and artificial intelligence). The challenge in writing an institutional asset
management book is that when tools from these different fields are applied in an investment strategy or an
analytical framework for valuing securities, it is assumed that the reader is familiar with the fundamentals of
these fields. Attempting to explain strategies and analytical concepts while also providing a primer on the tools
from other fields is not the most effective way of describing the asset management process. Moreover, while
an increasing number of investment models have been proposed in the asset management literature, there are
challenges and issues in implementing these models. This book provides a description of the tools used in asset
management as well as a more in\-depth explanation of specialized topics and issues covered in the companion
book, Fundamentals of Institutional Asset Management. The topics covered include the asset management
businessanditschallenges,thebasicsoffinancialaccounting,securitizationtechnology,analyticaltools(financial
econometrics, Monte Carlo simulation, optimization models, and machine learning), alternative risk measures for
assetallocation,securitiesfinance,implementingquantitativeresearch,quantitativeequitystrategies,transaction
costs,multifactormodelsappliedtoequityandbondportfoliomanagement,andbacktestingmethodologies.This
pedagogic approach exposes the reader to the set of interdisciplinary tools that modern asset managers require
in order to extract profits from data and processes.
Fabozzi, F. J., Kolm, P. N., Pachamanova, D. A., and Focardi, S. M. (2012\). “Robust Portfolio: Optimization
and Management .” In:Robust Portfolio . John Wiley and Sons, Inc. Chap. Robust Frameworks for Estimation:
Shrinkage, Bayesian Approaches, and the Black\-Litterman Model, pp. 207–253\.
The simplicity and the intuitive appeal of portfolio construction using modern portfolio theory have attracted
significant attention, but unfortunately, there are many problems with it, and practitioners consider portfolio
optimization to be difficult to apply. One can make the classical mean variance framework more robust by
improving the accuracy of the inputs, using constraints for the portfolio weights, opting portfolio resampling to
calculate the portfolio weights, and by applying the robust optimization framework to the portfolio allocation
process. One can also improve the estimates of expected return and covariances simply by using shrinkage
and Bayesian estimators. Shrinkage is a kind of averaging different estimators, which typically consists of an
estimator with little or no structure, an estimator with a lot of structure, and the shrinkage intensity. The
Bayesian approach, in contrast, assumes that the true expected returns are unknown and random. Its approach
is based on the subjective interpretation of probability. This chapter further explains that Black\-Litterman is a
model that combines an investor’s views with the market equilibrium.
Fabozzi, F. J. and Lopez de Prado, M. (2018\). “Being Honest in Backtest Reporting: A Template for Disclosing
Multiple Tests .” In:The Journal of Portfolio Management 45(1\), pp. 141–147\.
Selection bias under multiple testing is a serious problem. From a practitioner perspective, failure to disclose
the impact of multiple tests of a proposed investment strategy to clients and senior management can lead to
the adoption of a false discovery. Clients will lose money, senior management will misallocate resources, and
the firm may be exposed to reputational, legal, and regulatory risks. From the perspective of academic journals
that publish evidence supporting an investment strategy, the failure to address selection bias under multiple
testing threatens to invalidate large portions of the literature in empirical finance. In this article, the authors
propose a template that practitioners should use to fairly disclose multiple tests involved in an alleged discovery
when pitching strategies to clients and senior management. The same template could be used by contributors to
academic journals so that referees, and ultimately readers, can assess the strategy. By disclosing this information,
those who are charged with making the final decision about a discovery can evaluate the probability that the
purported discovery is false.
Fan, J., Liao, Y., and Liu, H. (2016\). “An overview of the estimation of large covariance and precision matrices .”
In:The Econometrics Journal 19(1\), pp. C1–C32\.
56The estimation of large covariance and precision matrices is fundamental in modern multivariate analysis. How\-
ever, problems arise from the statistical analysis of large panel economic and financial data. The covariance
matrix reveals marginal correlations between variables, while the precision matrix encodes conditional corre\-
lations between pairs of variables given the remaining variables. In this paper, we provide a selective review
of several recent developments on the estimation of large covariance and precision matrices. We focus on two
general approaches: a rank\-based method and a factor\-model\-based method. Theories and applications of both
approaches are presented. These methods are expected to be widely applicable to the analysis of economic and
financial data.
Fan, R., Jang, B., Sun, Y., and Zhou, S. (2019\). “Precision Matrix Estimation with Noisy and Missing Data .” In:
Proceedings of Machine Learning Research 89, pp. 2810–2819\.
Estimating conditional dependence graphs and precision matrices are some of the most common problems in
modern statistics and machine learning. When data are fully observed, penalized maximum likelihood\-type
estimators have become standard tools for estimating graphical models under sparsity conditions. Extensions
of these methods to more complex settings where data are contaminated with additive or multiplicative noise
have been developed in recent years. In these settings, however, the relative performance of different methods is
not well understood and algorithmic gaps still exist. In particular, in high\-dimensional settings these methods
require using non\-positive semidefinite matrices as inputs, presenting novel optimization challenges. We develop
an alternating direction method of multipliers (ADMM) algorithm for these problems, providing a feasible
algorithm to estimate precision matrices with indefinite input and potentially nonconvex penalties. We compare
this method with existing alternative solutions and empirically characterize the tradeoffs between them. Finally,
we use this method to explore the networks among US senators estimated from voting records data.
Feng, Y. and Palomar, D. P. (2016\). “Portfolio optimization with asset selection and risk parity control .” In:IEEE
International Conference on Acoustics, Speech and Signal Processing (ICASSP) .Shanghai:IEEE,pp.6585–6589\.
After the 2008 financial crisis, risk management has become more important than performance management and
an alternative portfolio design, referred to as risk parity portfolio, has been receiving significant attention from
both theoretical and practical fields due to its advantage in diversification of (ex\-ante) risk contributions among
assets. Usually, this approach results in a portfolio with nonzero weights in all the assets. Investors, however,
could not lay out the capital among all the assets listed on the markets, which results in unrealistically high
transaction costs, and therefore, reduction of the return of the designed portfolio. To overcome this drawback,
in this paper, we propose a method to jointly select only some of the assets and distribute the capital among
the selected assets such that the risk is diversified enough.
Fernandes, F., Oliveira, R., De\-Losso, R., Soto, A. J. D., Cavalcanti, P. D., and Campos, G. M. S. (2020\). “Saving
Markowitz: A Risk Parity Approach Based on the Cauchy Interlacing Theorem .” In:SSRN e\-Print .
It is well known that Markowitz Portfolio Optimization often leads to unreasonable and unbalanced portfolios
that are optimal in\-sample but perform very poorly out\-of\-sample. There is a strong relationship between these
poorreturnsandthefactthatcovariancematricesthatareusedwithintheMarkowitzframeworkaredegenerated
and ill\-posed, leading to unstable results by inverting them, as a consequence of very small eigenvalues. In this
paper we circumvent this problem in two steps: the enhancement of traditional risk parity techniques, which
consider only volatility, aiming to avoid matrix inversions (including the widespread Naive Risk Parity model)
within the Markowitz framework; the preservation of the correlation structure, as much as possible, aiming to
isolate a ”healthy” portion of the correlation matrix, that can be inverted without generating unstable and
risky portfolios, aiming to rescue the original Markowitz framework, by means of using the Cauchy Interlacing
Theorem. Using Brazilian and US market data, we show that the discussed framework enables one to build
portfolios that outperform the traditional and the newest risk parity techniques.
Fischer, E. O. and Murg, M. (2015\). “A combined regime\-switching and Black Litterman model for optimal asset
allocation .” In:Journal of Investment Strategies 4(3\), pp. 1–36\.
Traditionally, portfolios are optimized with a single\-regime Markowitz model, using volatility as the risk measure
and historical return as the expected return. This paper shows what effects a regime\-switching framework,
alternative risk measures (modifiedvalue\-at\-risk and conditional value\-at\-risk) and return measures (capital asset
pricing model estimates and Black Litterman estimates) can have on asset allocation as well as the absolute
and relative performance of portfolios. We show that the combination of alternative risk and return measures
within the regime\-switching framework gives significantly better results in terms of performance and a modified
Sharpe ratio. The use of alternative risk and return measures also mitigates the issue that asset returns are not
57often normally distributed or serially correlated. To eliminate the empirical shortcomings of asset returns, an
unsmoothing algorithm in combination with the Cornish\-Fisher expansion is used.
Fischer, M. and Gallmeyer, M. (2017\). “Taxable and Tax\-Deferred Investing with the Limited Use of Losses .” In:
Review of Finance 21(5\), pp. 1847–1873\.
We study the impact of the different tax treatment of capital gains and losses on the optimal location of assets in
taxable and tax\-deferred accounts. The classical result of Black (1980\) and Tepper (1981\) suggests that investors
should follow a strict pecking order asset location rule and hold those assets that are subject to the highest tax
rate preferentially in tax\-deferred accounts. We show that with the different tax treatment of realized gains and
losses, only tax\-efficient equity mutual funds are optimally held in taxable accounts, whereas mutual funds with
average tax\-(in)efficiency are preferentially held in tax\-deferred accounts.
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
Flint, E. J. and Mare, E. (2019\). “Regime\-Based Tactical Allocation for Equity Factors and Balanced Portfolios .”
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
58Feature Saliency Hidden Markov models for smart beta investing .” In:Expert Systems with Applications 163,
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
Forsyth, P. A. and Vetzal, K. R. (2017\). “Dynamic mean variance asset allocation: Tests for robustness .” In:Inter\-
national Journal of Financial .
We consider a portfolio consisting of a risk\-free bond and an equity index which follows a jump diffusion
process. Parameters for the inflation\-adjusted return of the stock index and the risk\-free bond are determined
by examining 89 years of data. The optimal dynamic asset allocation strategy for a long\-term pre\-commitment
mean variance (MV) investor is determined by numerically solving a Hamilton\-Jacobi\-Bellman partial integro\-
differential equation. The MV strategy is mathematically equivalent to minimizing the quadratic shortfall of
the target terminal wealth. We incorporate realistic constraints on the strategy: discrete rebalancing (yearly),
maximum leverage, and no trading if insolvent. Extensive synthetic market tests and resampled backtests of
historical data indicate that the multi\-period MV strategy achieves approximately the same expected terminal
wealth as a constant weight strategy, but with much smaller variance and probability of shortfall.
Fragkiskos, A. and Bauman, E. (2018\). “Factor Based Clustering .” In:SSRN e\-Print .
We propose a novel approach to cluster funds based on their factor exposures. The approach uses investment
returns as input data and calculates similarity scores across funds, which are then used to form clusters. The
derived clusters avoid common pitfalls that correlation based or other cluster methods fall into. They can be
used as peer group alternatives to what vendors provide or to further refine existing categories that might be
too obscure to make sense of. When tested against long/short equity funds, we find that we can form clusters
with relatively high levels of stability across time.
Fucik, V. (2017\). “Portfolio Construction Using Hierarchical Clustering .” MA thesis. Charles University.
Themainobjectiveofthisthesisistosummarizeandmainlyinterconnecttheexistingmethodologyoncorrelation
matrix filtering, graph algorithms utilized in the minimum spanning trees, hierarchical clustering and principal
components analysis in order to create quantitative investment strategies. Instead of traditional usage of stocks
returns series, factor models residuals are utilized. Residuals are then an ultimate input for all the algorithms to
arrive at probability of centrality (PoC) \- an impure probability where values near 1 signalize high probability
of a stock being central in the network. Several investment strategies are created based on PoC and tested on
data from major US stock market indices. It cannot be imperatively argued that peripheralbased strategies are
always better than central\-based strategies. Both central and peripheral\-based strategies share high upside profit
potential at the cost of high volatility whereas traditional Markowitz’s optimization process yields stable profits
with moderate upside potential.
Fuhrer, A. and Hock, T. (2019\). “Uncertainty in the Black\-Litterman model: A practical note .” In:Econstor e\-Print .
Deriving an optimal asset allocation for institutional investors hinges crucially on the quality of inputs used in
the optimization. If the mean vector and the covariance matrix are known with certainty, the classical mean\-
variance optimization of Markowitz (1952\) produces optimal portfolios. If, however, both and are estimated
with uncertainty, mean\-variance optimization tends to maximize estimation error, as shown in Michaud (1989\).
The Black\-Litterman model (Black and Litterman (1991, 1992\)), a derivation of the Bayesian methods de\-
veloped in academia, has particular practical appeal for institutional investors. It allows the specification of
views and an uncertainty about these views, which are combined with equilibrium returns and incorporated
consistently to arrive at and .These new parameters can then be used in the portfolio optimization process.
In the Black\-Litterman model, however, uncertainty about the equilibrium returns is specified with an overall
scalar uncertainty parameter, which is difficult to set and introduces rigidity.We propose a slight modification
59of the Black\-Litterman model to allow the specification of uncertainty in a flexible way not only in individual
views, but also in the equilibrium returns of every asset entering the model. Our modification is an ”add\-on”
to the traditional framework, which allows to adjust the uncertainty individually and is still permitting the
Black\-Litterman approach as a special case.
Fusai, G., Mignacca, D., Nardon, A., and Human, B. (2020\). “Equally Diversified or Equally Weighted? ” In:Risk
(Cutting Edge) .
GianlucaFusai,DomenicoMignacca,AndreaNardonandBenHumanshowhowtodecomposeportfoliovolatility
into undiversified volatility and a diversification component. The authors’ decomposition has a clear statistical
interpretationbecauseitrelatesthediversificationcomponenttopartialcovariances.Onthisbasis,theyadvocate
the construction of an equally diversified portfolio. An empirical analysis illustrates the superior out\-of\-sample
performance of the equally diversified portfolio with respect to an equally weighted portfolio.
Fuss, R., Koeppel, C., and Miebs, F. (2021\). “Diversifying Estimation Errors: An Efficient Averaging Rule for
Portfolio Optimization .” In:SSRN e\-Print .
We propose an averaging rule that combines established minimum\-variance strategies to minimize the expected
out\-of\-sample variance. Our rule overcomes the problem of selecting the ”best” strategy ex\-ante and diversifies
remaining estimation errors of the single strategies included in the averaging. Extensive simulations show that
the contributions of estimation errors to the out\-of\-sample variances are uncorrelated between the considered
strategies. This implies that averaging over multiple strategies offers sizable diversification benefits. Our rule
leverages these benefits and compares favorably to eleven strategies in terms of out\-of\-sample variance on both
simulated and empirical data sets. The Sharpe ratio is across all data sets at least 25% higher than for the 1/N
portfolio.
Gabrel, V., Murat, C., and Thiele, A. (2014\). “Recent advances in robust optimization: An overview .” In:European
Journal of Operational Research 235(3\), pp. 471–483\.
This paper provides an overview of developments in robust optimization since 2007\. It seeks to give a representa\-
tive picture of the research topics most explored in recent years, highlight common themes in the investigations
of independent research teams and highlight the contributions of rising as well as established researchers both
to the theory of robust optimization and its practice. With respect to the theory of robust optimization, this
paper reviews recent results on the cases without and with recourse, i.e., the static and dynamic settings, as
well as the connection with stochastic optimization and risk theory, the concept of distributionally robust opti\-
mization, and findings in robust nonlinear optimization. With respect to the practice of robust optimization, we
consider a broad spectrum of applications, in particular inventory and logistics, finance, revenue management,
but also queueing networks, machine learning, energy systems and the public good. Key developments in the
period from 2007 to present include: (i) an extensive body of work on robust decision\-making under uncertainty
with uncertain distributions, i.e., robustifying stochastic optimization, (ii) a greater connection with decision
sciences by linking uncertainty sets to risk theory, (iii) further results on nonlinear optimization and sequential
decision\-making and (iv) besides more work on established families of examples such as robust inventory and
revenue management, the addition to the robust optimization literature of new application areas, especially
energy systems and the public good.
Garivaltis, A. (2019\). “Exact replication of the best rebalancing rule in hindsight .” In:Journal of Derivatives 26(4\),
pp. 35–53\.
This article prices and replicates the financial derivative whose payoff at T is the wealth that would have accrued
to a 1USD deposit into the best continuously\-rebalanced portfolio (or fixed\-fraction betting scheme) determined
in hindsight.
Geelen, J. M. H. (2020\). “Optimization in an uncertain world \- The impact of uncertainty on portfolio allocation .”
MA thesis. Erasmus University.
Inthispaper,weinvestigatetheimpactofuncertaintyonportfolioallocationandhowincorporatingstochasticity
in the investment strategy improves performance. We use both stochastic programming and robust optimiza\-
tion to maximize return with constrained risk measured by Conditional Value\-at\-Risk (CVaR), using scenarios
generated via Filtered Historical Simulation (FHS). We compare the results based on return, risk, stability of
the weights over time, and a newly introduced dispersion measure. We find that incorporating uncertainty only
slightly enhances performance. In an expanding window estimation, the effect of incorporating uncertainty in
returns disappears and the inclusion of parameter uncertainty has a negative impact. Also, managerial and
legislative restrictions have much influence on the optimization outcomes and induce the stochasticity in the risk
60constraint to have little impact. When we exclude these supplementary restrictions, incorporating uncertainty
becomes more effective.
Georgantas, A. (2020\). “Robust Optimization Approaches for Portfolio Selection: A Computational and Compara\-
tive Analysis .” In:arXiv e\-Print .
The field of portfolio selection is an active research topic, which combines elements and methodologies from
various fields, such as optimization, decision analysis, risk management, data science, forecasting, etc. The
modeling and treatment of deep uncertainties for future asset returns is a major issue for the success of analytical
portfolio selection models. Recently, robust optimization (RO) models have attracted a lot of interest in this
area. RO provides a computationally tractable framework for portfolio optimization based on relatively general
assumptions on the probability distributions of the uncertain risk parameters. Thus, RO extends the framework
oftraditionallinearandnon\-linearmodels(e.g.,thewell\-knownmean\-variancemodel),incorporatinguncertainty
through a formal and analytical approach into the modeling process. Robust counterparts of existing models can
be considered as worst\-case re\-formulations as far as deviations of the uncertain parameters from their nominal
values are concerned. Although several RO models have been proposed in the literature focusing on various risk
measures and different types of uncertainty sets about asset returns, analytical empirical assessments of their
performance have not been performed in a comprehensive manner. The objective of this study is to fill in this
gap in the literature. More specifically, we consider different types of RO models based on popular risk measures
and conduct an extensive comparative analysis of their performance using data from the US market during the
period 2005\-2016\.
Geyer, A. and Lucivjanska, K. L. (2016\). “The Black\-Litterman Approach and Views from Predictive Regressions:
Theory and Implementation .” In:The Journal of Portfolio Management 42(4\), pp. 38–48\.
A major attraction of the Black\-Litterman approach for portfolio optimization is the potential for integrating
subjective views on expected returns. In this article, the authors provide a new approach for deriving the views
and their uncertainty using predictive regressions estimated in a Bayesian framework. The authors show that
the Bayesian estimation of predictive regressions fits perfectly with the idea of Black\-Litterman. The subjective
element is introduced in terms of the investors’ belief about the degree of predictability of the regression. In
this setup, the uncertainty of views is derived naturally from the Bayesian regression, rather than by using the
covariance of returns. Finally, the authors show that this approach of integrating uncertainty about views is the
main reason this method outperforms other strategies.
Ghahtarani, A., Saif, A., and Ghasemi, A. (2022\). “Robust Portfolio Selection Problems: A Comprehensive Review .”
In:arXiv e\-Print .
In this paper, we provide a comprehensive review of recent advances in robust portfolio selection problems and
their extensions, from both operational research and financial perspectives. A multi\-dimensional classification
of the models and methods proposed in the literature is presented, based on the types of financial problems,
uncertainty sets, robust optimization approaches, and mathematical formulations. Several open questions and
potential future research directions are identified.
Giacometti, R., Bertocchi, M., Rachev, S. T., and Fabozzi, F. J. (2007\). “Stable distributions in the Black Litterman
approach to asset allocation .” In:Quantitative Finance 7(4\), pp. 423–433\.
The integration of quantitative asset allocation models and the judgment of portfolio managers and analysts (i.e.
qualitative view) dates back to a series of papers by Black and Litterman in the early 1990s. In this paper we
improve the classical Black?Litterman model by applying more realistic models for asset returns (the normal, the
t\-student, and the stable distributions) and by using alternative risk measures (dispersion\-based risk measures,
value at risk, conditional value at risk). Results are reported for monthly data and goodness of the models are
tested through a rolling window of fixed size along a fixed horizon. Finally, we find that incorporation of the
views of investors into the model provides information as to how the different distributional hypotheses can
impact the optimal composition of the portfolio.
Giudici, P., Polinesi, G., and Spelta, A. (2022\). “Network models to improve robot advisory portfolios .” In:Annals
of Operations Research 313, pp. 965–989\.
Robotadvisoryservicesarerapidlyexpanding,respondingtoagrowinginterestpeoplehaveindirectlymanaging
their savings. Robot\-advisors may reduce costs and improve the quality of asset allocation services, making
user’s involvement more transparent. Against this background, there exists the possibility that robot advisors
underestimate market risks, especially during crisis times, when high order interconnections arise. This may lead
to a mismatch between investors’ expected and actual risk. The aim of this paper is to overcome this issue, taking
into account not only investors’ risk preference but also their attitude towards interconnectdness. To achieve
61this aim, we combine random matrix theory with correlation networks and extend the Markowitz’ optimisation
problem to a third dimension. To demonstrate the practical advantage of our proposed approach we employ daily
returns of a large set of Exchange Traded Funds, which are representative of the financial products employed
by robot\-advisors.
Gortz, C. and Yeromonahos, M. (2019\). “Asymmetries in Risk Premia, Macroeconomic Uncertainty and Business
Cycles.” In:CESifo(7959\).
A large literature suggests that the expected equity risk premium is countercyclical. Using a variety of different
measures for this risk premium, we document that it also exhibits growth asymmetry, i.e. the risk premium
rises sharply in recessions and declines much more gradually during the following recoveries. We show that a
model with recursive preferences, in which agents cannot perfectly observe the state of current productivity,
can generate the observed asymmetry in the risk premium. Key for this result are endogenous fluctuations in
uncertainty which induce procyclical variations in agent’s nowcast accuracy. In addition to matching moments of
the risk premium, the model is also successful in generating the growth asymmetry in macroeconomic aggregates
observed in the data, and in matching the cyclical relation between quantities and the risk premium.
Gotoh, J.\-y., Kim, M. J., and Lim, A. E. B. (2018\). “Robust empirical optimization is almost the same as mean\-
variance optimization .” In:Operations Research Letters 46(4\), pp. 448–452\.
Abstract We formulate a distributionally robust optimization problem where the deviation of the alternative
distribution is controlled by a phi \-divergence penalty in the objective, and show that a large class of these
problems are essentially equivalent to a mean\-variance problem. We also show that while a amount of robustness
always reduces the in\-sample expected reward, the reduction in the variance, which is a measure of sensitivity
to model misspecification, is an order of magnitude larger.
Greiner, S. P. and Stoyanov, S. V. (2019\). “Portfolio scoring by expected risk premium .” In:The Journal of Portfolio
Management 45(4\), pp. 83–90\.
In this article, the authors discuss a general method for ranking portfolios that places few limitations on the
portfolio constituents other than using publicly traded assets. The ranking scores reflect the expected reward
investors would require for accepting the risks of the portfolio in the context of an asset pricing framework.
The scores are computed through a factor model that acknowledges the factor return correlations. The authors
illustrate the approach with a large universe of exchange\-traded funds assuming a linear model with Fama\-
French\-Carhart factors wherein factor premiums (i.e., expected returns) are proportional to factor volatilities.
The empirical analysis implies that the most significant factors from the Fama\-French\-Carhart factor set driving
the premiums are the market and the momentum factors.
Guastaroba, G., Mitra, G., and Speranza, M. G. (2011\). “Investigating the effectiveness of robust portfolio opti\-
mization techniques .” In:Journal of Asset Management 12(4\), pp. 260–280\.
Data uncertainty is a common feature in most of the real\-life optimization problems. Despite that, the usual
approachinmathematicaloptimizationistoassumethatalltheinputdataareknowndeterministicallyandequal
to some nominal values. Nevertheless, the optimal solution of the nominal problem can reveal itself suboptimal
or even infeasible. An area where data uncertainty is a natural concern is portfolio optimization. As a matter of
fact, in portfolio selection every optimization model deals with the estimate of the portfolio rate of return, and
of either a risk or a safety measure. In the literature several techniques that are immune to data uncertainty
have been proposed. These techniques are called robust. In this article we investigate two well\-known robust
techniques when applied to a specific portfolio selection problem, and compare the portfolios selected by the
respective robust counterparts. Both the approaches allow the modeler to adjust the level of conservatism of the
solution. We carried out extensive computational results based on real\-life data from London Stock Exchange
Market under different market behaviors.
Guidolin, M., Hansen, E., and Lozano\-Banda, M. (2018\). “Portfolio performance of linear SDF models: an out\-of\-
sample assessment .” In:Quantitative Finance 18(8\), pp. 1425–1436\.
We evaluate linear stochastic discount factor models using an ex\-post portfolio metric: the realized out\-of\-
sample Sharpe ratio of mean\-variance portfolios backed by alternative linear factor models. Using a sample of
monthlyUSportfolioreturnsspanningtheperiod1968\-2016,wefindevidencethatmultifactorlinearmodelshave
better empirical properties than the CAPM, not only when the cross\-section of expected returns is evaluated in\-
sample, but also when they are used to inform one\-month ahead portfolio selection. When we compare portfolios
associated to multifactor models with mean\-variance decisions implied by the single\-factor CAPM, we document
statistically significant differences in Sharpe ratios of up to 10 percent. Linear multifactor models that provide
the best in\-sample fit also yield the highest realized Sharpe ratios.
62Guidolin,M.andHyde,S.(2014\). “Linearpredictabilityvs.bullandbearmarketmodelsinstrategicassetallocation
decisions: evidence from UK data .” In:Quantitative Finance 14(12\), pp. 2135–2153\.
Most papers in the portfolio choice literature have examined linear predictability frameworks based on the idea
that simple but flexible Vector Autoregressive (VAR) models can be expanded to produce portfolio allocations
that hedge against the bull and bear dynamics typical of financial markets through careful selection of predictor
variables that capture business cycles and market sentiment. Yet, a distinct literature exists that shows that non\-
linear econometric frameworks, such as Markov switching, are also natural tools to compute optimal portfolios
arising from the existence of good and bad market states. This paper examines whether and how simple VARs
can produce portfolio rules similar to those obtained under a simple Markov switching, by studying the effects
of expanding both the order of the VAR and the number/selection of predictor variables included. In a typical
stock\-bond strategic asset allocation problem for UK data, we compute the out\-of\-sample certainty equivalent
returns for a wide range of VARs and compare these measures of performance with those of non\-linear models.
We conclude that most VARs cannot produce portfolio rules, hedging demands or (net of transaction costs)
out\-of\-sample performances that approximate those obtained from simple non\-linear frameworks.
Guijo\-Rubio, D., Duran\-Rosal, A. M., Gutierrez, P. A., Troncoso, A., and Hervas\-Martinez, C. (2018\). “Time series
clustering based on the characterisation of segment typologies .” In:arXiv e\-Print .
Time series clustering is the process of grouping time series with respect to their similarity or characteristics.
Previous approaches usually combine a specific distance measure for time series and a standard clustering
method. However, these approaches do not take the similarity of the different subsequences of each time series
into account, which can be used to better compare the time series objects of the dataset. In this paper, we
propose a novel technique of time series clustering based on two clustering stages. In a first step, a least squares
polynomial segmentation procedure is applied to each time series, which is based on a growing window technique
that returns different\-length segments. Then, all the segments are projected into same dimensional space, based
on the coefficients of the model that approximates the segment and a set of statistical features. After mapping,
a first hierarchical clustering phase is applied to all mapped segments, returning groups of segments for each
time series. These clusters are used to represent all time series in the same dimensional space, after defining
another specific mapping process. In a second and final clustering stage, all the time series objects are grouped.
We consider internal clustering quality to automatically adjust the main parameter of the algorithm, which
is an error threshold for the segmenta\- tion. The results obtained on 84 datasets from the UCR Time Series
Classification Archive have been compared against two state\-of\-the\-art methods, showing that the performance
of this methodology is very promising.
Gulliksson, M. and Mazur, S. (2020\). “An Iterative Approach to Ill\-Conditioned Optimal Portfolio Selection .” In:
Computational Economics 56, pp. 773–794\.
Covariance matrix of the asset returns plays an important role in the portfolio selection. A number of papers is
focused on the case when the covariance matrix is positive definite. In this paper, we consider portfolio selection
with a singular covariance matrix. We describe an iterative method based on a second order damped dynamical
systems that solves the linear rank\-deficient problem approximately. Since the solution is not unique, we suggest
one numerical solution that can be chosen from the iterates that balances the size of portfolio and the risk.
The numerical study confirms that the method has good convergence properties and gives a solution as good as
or better than the solutions that are based on constrained least norm Moore\-Penrose, Lasso, and naive equal\-
weighted approaches. Finally, we complement our result with an empirical study where we analyze a portfolio
with actual returns listed in S\&P 500 index.
Guo, D. (2019\). “A Statistical Response to Challenges in Vast Portfolio Selection .” PhD thesis. University of
Waterloo.
The thesis is written in response to emerging issues brought about by an increasing number of assets allocated
in a portfolio and seeks answers to puzzling empirical findings in the portfolio management area. Over the years,
researchers and practitioners working in the portfolio optimization area have been concerned with estimation
errors in the first two moments of asset returns. The thesis comprises several related chapters on our statistical
inquiry into this subject. Chapter 1 of the thesis contains an introduction to what will be reported in the
remaining chapters. A few well\-known covariance matrix estimation methods in the literature involve adjustment
of sample eigenvalues. Chapter 2 of the thesis examines the effects of sample eigenvalue adjustment on the out\-
of\-sample performance of a portfolio constructed from the sample covariance matrix.
Guo, D., Boyle, P. P., Weng, C., and Wirjanto, T. S. (2019\). “When Does The 1/N Rule Work? ” In:SSRN e\-Print .
63We propose a ”1/N favorability index” to measure how favorable a market is to holding a 1/N portfolio. This
index reflects the extent of difficulty for an optimized portfolio to outperform the 1/N portfolio in a specific
market. A single\-factor model predicts that bull markets are accompanied by a high 1/N favorability index and
vice versa. We validate the model implication that the 1/N portfolio is more difficult to beat in bull markets
using stock return datasets from a number of countries as well as the classic datasets used by DeMiguel et al.
(2009\). Our results imply that the reported good performance of the 1/N portfolio in the US equity market can
be partially attributed to the long\-run bullish trend in the market which gives rise to the high favorability of
the market to the 1/N portfolio.
Haesen, D., Hallerbach, W. G., Markwat, T., and Molenaar, R. (2017\). “Enhancing Risk Parity by Including Views .”
In:The Journal of Investing 26(4\), pp. 53–68\.
Within the finance literature, there is an apparent gap between the inherent ignorance of expected returns of
a risk parity approach on the one hand, and the assumed certainty of expected returns in a mean\-variance
approach on the other. The authors propose a portfolio selection framework that allows an investor to position
herself between these two extremes. Depending on the confidence in one’s expected return estimates, the optimal
portfoliowillbetiltedmoretowardtheriskparityportfolioorthemean\-varianceportfolio.Theauthorsillustrate
the framework for an investor in an asset allocation context.
Hagstromer, B., Anderson, R. G., Binner, J. M., Elger, T., and Nilsson, B. (2007\). “Mean\-Variance vs. Full\-Scale
Optimization: Broad Evidence for the UK .” In:SSRN e\-Print .
Portfolio choice by full\-scale optimization applies the empirical return distribution to a parameterized utility
function, and the maximum is found through numerical optimization. Using a portfolio choice setting of three
UK equity indices we identify several utility functions featuring loss aversion and prospect theory, under which
full\-scale optimization is a substantially better approach than the mean\-variance approach. As the equity indices
have return distributions with small deviations from normality, the findings indicate much broader usefulness of
full\-scale optimization than has earlier been shown. The results hold in and out of sample, and the performance
improvements are given in terms of utility as well as certainty equivalents.
Hagstromer, B. and Binner, J. M. (2009\). “Stock portfolio selection with full\-scale optimization and differential
evolution .” In:Applied Financial Economics 19(19\), pp. 1559–1571\.
Full\-Scale Optimization (FSO) is a utility maximization approach to portfolio choice problems that has theoret\-
ical appeal but that suffers from computational burden in large scale problems. We apply the heuristic technique
differential evolution to solve FSO\-type asset selection problems of 97 assets under complex utility functions
rendering rough utility search surfaces. We show that this problem is computationally feasible and that solutions
retrieved with random starting values are converging to one optimum. Furthermore, the study constitutes the
first FSO application to stock portfolio optimization. The results indicate that when investors are loss averse,
FSO improves stock portfolio performance compared to Mean Variance (MV) portfolios. This finding widens
the scope of applicability of FSO, but it is also stressed that out\-of\-sample success will always be dependent on
the forecasting ability of the input return distributions.
Haley, M. R. (2017\). “K\-fold cross validation performance comparisons of six naive portfolio selection rules: how
naive can you be and still have successful out\-of\-sample portfolio performance? ” In:Annals of Finance 13,
pp. 341–353\.
Recent research reports that optimal portfolio selection models often perform worse than equal\-weight naive
diversification in out\-of\-sample testing. This paper extends this line of inquiry by comparing the out\-of\-sample
performance of the equal\-weight naive strategy to the out\-of\-sample performance of five alternative naive strate\-
gies,eachofwhichderivesfromasimpleheuristicthatdoesnotrequireanyoptimization.Out\-of\-sampleportfolio
performance is assessed by mean, standard deviation, skewness, and Sharpe ratio; k\-fold cross validation is used
as the out\-of\-sample testing mechanism. The results indicate that the proposed naive heuristic rules exhibit
strong out\-of\-sample performance, in most cases superior to the equal\-weight naive strategy. These findings are
consequential for at least two reasons: first, if these simple heuristic\-based rules outperform the equal\-weight
naive strategy, then by transitivity they can outperform the mean\-variance\- and shortfall\-optimal portfolio rules
that have been shown in the literature to be inferior to the equal\-weight naive rule, which further emphasizes the
out\-of\-sample fragility of ”optimal”methods; and second, among naive diversification strategies, some appear
more robust in out\-of\-sample testing than others, hence the proposed methods may be useful when forming
mixed portfolio selection models wherein a naive strategy is combined with an optimal strategy to improve
performance.
Hallerbach, W. G. (2014\). “Disentangling rebalancing return .” In:Journal of Asset Management 15(5\), pp. 301–316\.
64The use of portfolio rebalancing as a profitable strategy (or volatility harvesting ) is a hot topic. Indeed, it is
interesting to know what the impact of periodic rebalancing is on the growth rate of a portfolio. Unfortunately,
the terminology used in the literature is confusing. Terms such as diversification return and rebalancing return
are used interchangeably to indicate the growth rate that a rebalanced portfolio can earn in excess of a buy\-
and\-hold portfolio. The literature is also confused in specifying this excess growth rate from rebalancing. In
this paper, we investigate the full return from rebalancing and decompose it into the volatility return and
the dispersion discount. We prove some general results regarding these components and present some simple
approximations which provide direct insight into the driving forces behind these building blocks. We consider a
pro forma US asset portfolio over the period 1974\-2013, which allows us to investigate the relative magnitude
of the discussed effects and their time variation.
Han, Y. and Li, P. (2020\). “Robust Portfolio Selection Using Vine Copulas .” In:SSRN e\-Print .
Portfolio optimization problems involving Conditional Value\-at\-Risk (CVaR) are often computationally in\-
tractableandrequirecompleteinformationaboutthedistributionofreturns,whichisrarelyavailableinpractice.
These difficulties are compounded when the portfolio contains a lot of assets. In this paper, we consider the
worst\-case CVaR (WCVaR) under mixture of vine copulas distribution uncertainty, which can capture complex
and hidden dependence patterns in multivariate data.We compare the out\-of\-sample performance of the robust
strategies based on the mixture of R\-vine copulas, mixture of C\-vine copulas, mixture of D\-vine copulas and
nominal CVaR method. The experimental study shows that the robust models based on mixture of R\-Vine
copulas and mixture of C\-Vine copulas perform the best in terms of average returns, Sharpe ratio and cumu\-
lative returns. The performance of robust mixture of D\-Vine copulas model might be advantageous when the
correlation between assets is low.
Harris, R. D. F., Stoja, E., and Tan, L. (2017\). “The dynamic Black\-Litterman approach to asset allocation .” In:
European Journal of Operational Research 259(3\), pp. 1085–1096\.
We generalize the Black\-Litterman portfolio management framework. We incorporate time\-variation in the con\-
ditional distribution of returns in the asset allocation process. The dynamic Black\-Litterman model outperforms
a range of different benchmarks. The choice of volatility model has a considerable impact on the performance of
the dynamic model. We generalize the Black\-Litterman (BL) portfolio management framework to incorporate
time\-variation in the conditional distribution of returns in the asset allocation process. We evaluate the per\-
formance of the dynamic BL model using both standard performance ratios as well as other measures that are
designed to capture tail risk in the presence of non\-normally distributed asset returns. We find that the dynamic
BL model outperforms a range of different benchmarks. Moreover, we show that the choice of volatility model
has a considerable impact on the performance of the dynamic BL model.
Harutyunyan, H., Moyer, D., Khachatrian, H., Steeg, G. V., and Galstyan, A. (2021\). “Efficient Covariance Esti\-
mation from Temporal Data .” In:arXiv e\-Print .
Estimating the covariance structure of multivariate time series is a fundamental problem with a wide\-range of
real\-world applications – from financial modeling to fMRI analysis. Despite significant recent advances, current
state\-of\-the\-artmethodsare stillseverelylimitedin termsof scalability,and donot workwellin high\-dimensional
undersampled regimes. In this work we propose a novel method called Temporal Correlation Explanation, or
T\-CorEx, that (a) has linear time and memory complexity with respect to the number of variables, and can scale
to very large temporal datasets that are not tractable with existing methods; (b) gives state\-of\-the\-art results
in highly undersampled regimes on both synthetic and real\-world datasets; and (c) makes minimal assumptions
about the character of the dynamics of the system. T\-CorEx optimizes an information\-theoretic objective func\-
tion to learn a latent factor graphical model for each time period and applies two regularization techniques to
induce temporal consistency of estimates. We perform extensive evaluation of T\-Corex using both synthetic and
real\-world data and demonstrate that it can be used for detecting sudden changes in the underlying covariance
matrix, capturing transient correlations and analyzing extremely high\-dimensional complex multivariate time
series such as high\-resolution fMRI data.
Harvey, C. R., Hoyle, E., Rattray, S., and van Hemert, O. (2020a). “Strategic Risk Management: Out\-of\-Sample
Evidence from the COVID\-19 Equity Selloff .” In:SSRN e\-Print .
Over the 2016\-2019 period, we released a series of research papers on the topic of ”strategic risk management”,
or the embedding of risk management into investment strategy design. We show that key risk controls that we
introduced materially helped during the sharp equity market selloff in February\-March 2020, when the COVID\-
19 pandemic accelerated. First, faster trend following and long\-short profitability stock strategies performed well
during the equity market selloff. Second, responsive volatility targeting reduced positions dramatically ahead of
65the most volatile period in March 2020, and so improved both the return and risk profile at that time. Third,
strategicrebalancingruleshelpfullycalledforkeepinganunderweightinequities(notrebalancingbacktotarget)
at the end of February 2020, regardless of using 1\-, 3\-, or 12\-month trend systems to base the rebalancing rule
on.
Harvey,C.R.,Liu,Y.,andSaretto,A.(2020b). “AnEvaluationofAlternativeMultipleTestingMethodsforFinance
Applications .” In:The Review of Asset Pricing Studies 10(2\), pp. 199–248\.
In almost every area of empirical finance, researchers confront multiple tests. One high\-profile example is the
identification of outperforming investment managers, many of whom beat their benchmarks purely by luck.
Multiple testing methods are designed to control for luck. Factor selection is another glaring case in which
multiple tests are performed, but numerous other applications do not receive as much attention. One important
example is a simple regression model testing five variables. In this case, because five variables are tried, a t\-
statistic of 2\.0 is not enough to establish significance. Our paper provides a guide to various multiple testing
methods and details a number of applications. We provide simulation evidence on the relative performance of
different methods across a variety of testing environments. The goal of our paper is to provide a menu that
researchers can choose from to improve inference in financial economics.
Harvey, C. R., Rattray, S., and Van Hemert, O. (2021\). Strategic risk management : designing portfolios and
managing risk . Hoboken, New Jersey: Wiley. 256 pp.
Having just experienced a global pandemic that sent equity markets into a tailspin in March 2020, risk manage\-
ment is a more relevant topic than ever. It remains, however, an often poorly understood afterthought. Many
portfolios are designed without any thought given to risk management before they are handed off to a dedicated
– but separate – risk management team.
In Strategic Risk Management: Designing Portfolios and Managing Risk, Campbell R. Harvey, Sandy Rattray,
and Otto Van Hemert deliver a reimagining of the risk management process. The book envisions a marriage
between the investment and risk processes, an approach that has proven successful at the world’s largest publicly
listed hedge fund, Man Group.
The authors provide readers with a new framework for portfolio design that includes defensive strategies, draw\-
down risk controls, volatility targeting, and actively timing rebalancing trades. You will learn about how the
book’s new approach to risk management fared during the recent market drawdown at the height of the COVID\-
19 pandemic. You will also discover why the traditional risk weighting approach only works on certain classes
of assets.
The book shows you how to accurately evaluate the costs of defensive strategies and which ones offer the best and
most cost\-effective protection against market downturns. Finally, you will learn how to obtain a more balanced
return stream by targeting volatility rather than a constant notional exposure and gain a deeper understanding
of concepts like portfolio rebalancing.
Perfect for people working in the asset management industry and financial policy makers, Strategic Risk Man\-
agement: Designing Portfolios and Managing Risk will also earn a place in the libraries of economics and finance
scholars, as well as casual readers who take an active approach to investing in their savings or pension assets.
Haugh, M., Iyengar, G., and Wang, C. (2016\). “Tax\-Aware Dynamic Asset Allocation .” In:Operations Research
64(4\), pp. 849–866\.
We consider dynamic asset allocation problems where the agent is required to pay capital gains taxes on her
investment gains. This is a very challenging problem because the tax owed whenever a security is sold depends on
the cost\-basis, i.e. the price(s) at which the shares of the security was originally purchased. This feature results
in high\-dimensional and path\-dependent problems which cannot be solved exactly except in the case of very
stylized problems with just one or two securities and relatively few time periods. The asset allocation problem
withtaxeshasseveralvariationsdependingon:(i)whetherweusetheexactoraveragecost\-basisand(ii)whether
we allow the full use of losses (FUL) or the limited use of losses (LUL). In this paper we focus on the exact and
average cost\-basis LUL cases since these problems are the most realistic and challenging to solve. We develop
simple heuristic trading policies for these problems when there are differential tax rates for long\- and short\-
term gains/losses. We then use duality techniques based on information relaxations to assess the performance
of these trading policies by constructing unbiased lower and upper bounds on the (unknown) optimal value
function. In numerical experiments with as many as 80 time periods and 25 securities we find our best sub\-
optimal policy is within 3 to 10 basis points of optimality on a certainty\-equivalent annualized return basis. The
principal contribution of this paper is in demonstrating that much larger problems can now be tackled through
the use of sophisticated optimization techniques and duality methods based on information\-relaxations. More
66specifically, while the primal problem remains very challenging to solve exactly, we can easily solve very large
dual problem instances. Moreover, dual tractability extends to standard problem variations including problems
with random time horizons, no wash\-sales constraints, inter\-temporal consumption and recursive utility, and the
step\-up feature of the U.S. tax code, among others.
Haugh, M., Song, I., and Iyengar, G. (2017\). “A generalized risk budgeting approach to portfolio construction .” In:
Journal of Computational Finance 21(2\), pp. 29–60\.
Risk\-basedassetallocationmodelshavereceivedconsiderableattentioninrecentyears.Thisincreasedpopularity
is due in part to the difficulty in estimating expected returns, as well as to the 2008 financial crisis, which helped
reinforce the key role of risk in asset allocation. We propose a generalized risk budgeting (GRB) approach to
portfolio construction. In a GRB portfolio, assets are grouped into possibly overlapping subsets, and each subset
is allocated a prespecified risk budget. Minimum variance, risk parity and risk budgeting portfolios are all special
instancesofaGRBportfolio.TheGRBportfoliooptimizationproblemistofindaGRBportfoliowithanoptimal
risk\-return profile, where risk is measured using any positively homogeneous risk measure. When the subsets
form a partition, the assets all have the same expected return, and we restrict ourselves to long\-only portfolios;
then, the GRB problem can in fact be solved as a convex optimization problem. In general, however, the GRB
problem is a constrained nonconvex problem, for which we propose two solution approaches. The first approach
uses a semidefinite programming relaxation to obtain an (upper) bound on the optimal objective function value.
In the second approach, we develop a numerical algorithm that integrates augmented Lagrangian and Markov
chain Monte Carlo methods in order to find a point in the vicinity of a very good local optimum. This point
is then supplied to a standard nonlinear optimization routine with the goal of finding this local optimum. The
merit of this second approach is in its generic nature: in particular, it provides a strategy for choosing a starting
point for any nonlinear optimization algorithm.
Heckel, T., de Carvalho, R. L., Lu, X., and Perchet, R. (2016\). “Insights into robust optimization: decomposing into
mean\-variance and risk\-based portfolios .” In:Journal of Investment Strategies 6(1\), pp. 1–24\.
For a number of different formulations of robust portfolio optimization, quadratic and absolute, we show that
(a) in the limit of low uncertainty in estimated asset mean returns, the robust portfolio converges toward the
mean\-variance portfolio obtained with the same inputs, and (b) in the limit of high uncertainty, the robust
portfolio converges toward a risk\-based portfolio, which is a function of how the uncertainty in estimated asset
mean returns is defined. We give examples in which the robust portfolio converges toward the minimum variance,
inverse variance, equal\-risk budget and equally weighted portfolios in the limit of sufficiently large uncertainty
in asset mean returns. At intermediate levels of uncertainty, we find that a weighted average of the mean\-
variance portfolio and the respective limiting risk\-based portfolio offers a good representation of the robust
portfolio, particularly in the case of the quadratic formulation. The results remain valid even in the presence of
portfolio constraints, in which case the limiting portfolios are the corresponding constrained mean\-variance and
constrained risk\-based portfolios. We believe our results are important, particularly for risk\-based investors who
wish to take expected returns into account in order to gently tilt away from their current allocations, eg, risk
parity or minimum variance.
Hens, T., Schenk\-Hoppe, K. R., and Woesthoff, M.\-H. (2020\). “Escaping the backtesting illusion .” In:The Journal
of Portfolio Management 46(4\), pp. 81–93\.
Two tests can help asset managers to develop more robust investment strategies: an impact test and a survival
test. Both tests complement the backtest, in which one checks how a proposed investment strategy would have
performed in the past. The impact test considers the performance of the strategy when assets under management
grow (crowdedness), and it checks the impact that growth in assets under management in competing strategies
has on the proposed strategy (cross impact). The survival test considers the effect of the long\-term evolution
of assets under management in competition for market capital. Using Shiller S\&P 500 index and bond market
data, we show that time\-series momentum (relative strength) performs best in the backtest and the impact test
but that an expected relative cash\-flow rule (relative dividend yield) has the best long\-term survival properties.
Higham, N. J., Strabic, N., and Sego, V. (2016\). “Restoring Definiteness via Shrinking, with an Application to
Correlation Matrices with a Fixed Block .” In:SIAM Review 58(2\), pp. 245–263\.
Indefinite approximations of positive semidefinite matrices arise in various data analysis applications involving
covariance matrices and correlation matrices. We propose a method for restoring positive semidefiniteness of
an indefinite matrix M0 that constructs a convex linear combination S(alpha) \= alpha\*M1 \+ (1\-alpha)\*M0
of M0 and a positive semidefinite target matrix M1\. In statistics, this construction for improving an estimate
M0 by combining it with new information in M1 is known as shrinking. We make no statistical assumptions
67about M0 and define the optimal shrinking parameter as alphaStar \= min (alpha in \[0,1] such that S(alpha)
is positive semidefinite). We describe three algorithms for computing alphaStar. One algorithm is based on
the bisection method, with the use of Cholesky factorization to test definiteness; a second employs Newton’s
method; and a third finds the smallest eigenvalue of a symmetric definite generalized eigenvalue problem. We
show that weights that reflect confidence in the individual entries of M0 can be used to construct a natural
choice of the target matrix M1\. We treat in detail a problem variant in which a positive semidefinite leading
principal submatrix of M0 remains fixed, showing how the fixed block can be exploited to reduce the cost of
the bisection and generalized eigenvalue methods. Numerical experiments show that when applied to indefinite
approximations of correlation matrices shrinking can be at least an order of magnitude faster than computing
the nearest correlation matrix.
Hight, G. N. and Haley, J. D. (2021\). “Low\-Risk Benchmarking Transcends Rebalancing Methods .” In:The Journal
of Investing 30(2\), pp. 7–30\.
The dismal performance of managed investment and the success of equal allocation and minimum variance
models prompt these questions: Can rebalancing driven by minimum variance and maximum diversification
rebalancing outperform naive models? Can a minimum variance model produce higher risk\-adjusted returns
than a maximum diversification model when security selection favors low\-correlated assets? This study uses
expected shortfall to measure risk, bootstrapping to transform fat\-tailed distributions so they are suitable for
t\-tests, and factor analysis to help explain the relative performance of the models. The minimum variance and
maximum diversification models outperformed naive models, and the minimum variance models produced higher
risk\-adjusted returns than the maximum diversification model. Market factors adequately explained differences
in returns between rebalancing models, but adding a factor for the effect of rebalancing procedures improved
all models. All models constrained by the lower risk benchmark produced higher risk\-adjusted returns than
correspondingmodelsconstrainedbythehigherriskbenchmark.Thisoutcomesuggestsmanyrebalancingmodels
– perhaps even return\-based models – could produce superior risk\-adjusted returns if lower risk benchmarks
constrain risk.
Hilliard, J. E. and Hilliard, J. (2015\). “Rebalancing versus Buy and Hold: Theory, Simulation and Empirical Anal\-
ysis.” In:SSRN e\-Print .
We consider returns from rebalanced and buy and hold portfolios consisting of the same stocks. Theoretical
properties are derived using Jensen’s inequality and the H older’s Defect Formula. Simulations are used to
confirm theory and to investigate ambiguous cases where theory is silent. Rebalancing generally increases the
Sharpe Ratios and decreases total return volatility. Buy and hold produces greater expected return. Results are
more opaque with respect to expected geometric means. Our empirical tests are based on portfolios composed of
the risk\-free asset and market valued weighted CRSP total returns. While rebalancing reduces volatility, these
tests largely favor the buy and hold strategy due to the high relative returns of the index vis\-a\-vis the risk\-free
asset.
Hoffstein, C., Faber, N., and Braun, S. (2020\). “Rebalance Timing Luck: The (Dumb) Luck of Smart Beta .” In:
SSRN e\-Print .
Prior research and empirical investment results have shown that portfolio construction choices related to re\-
balance schedules may have non\-trivial impacts on realized performance. We construct long\-only indices that
provide exposures to popular U.S. equity factors (value, size, momentum, quality, and low volatility) and vary
their rebalance schedules to isolate the effects of ”rebalance timing luck.” Our constructed indices exhibit high
levels of rebalance timing luck, often exceeding 100 basis points annualized, with total impact dependent upon
the frequency of rebalancing, portfolio concentration, and the nature of the underlying strategy. As a case study,
we replicate popular factor\-based index funds and similarly find meaningful performance impacts due to rebal\-
ance timing luck. For example, a strategy replicating the S\&P Enhanced Value index saw calendar year return
differentials above 40% strictly due to the rebalance schedule implemented. Our results suggest substantial
problems for analyzing any investment when the strategy, its peer group, or its benchmark is susceptible to
performance impacts driven by the choice of rebalance schedule.
Holst, A., Bae, J., Karlsson, A., and Bouguelia, M.\-R. (2019\). “Interactive clustering for exploring multiple data
streams at different time scales and granularity .” In:Proceedings of the Workshop on Interactive Data Mining \-
WIDM’19 . New York, New York, USA: ACM Press, pp. 1–7\.
We approach the problem of identifying and interpreting clusters over different time scales and granularity in
multivariate time series data. We extract statistical features over a sliding window of each time series, and
then use a Gaussian mixture model to identify clusters which are then projected back on the data streams.
68The human analyst can then further analyze this projection and adjust the size of the sliding window and the
number of clusters in order to capture the different types of clusters over different time scales. We demonstrate
the effectiveness of our approach in two different application scenarios: (1\) fleet management and (2\) district
heating, wherein each scenario, several different types of meaningful clusters can be identified when varying over
these dimensions.
Horan, S. M. and Adler, D. (2009\). “Tax\-Aware Investment Management Practice .” In:The Journal of Wealth
Management 12(2\), pp. 71–88\.
The authors examine the tax\-aware investment practices of investment managers managing taxable accounts.
Their sample of mostly well\-experienced CFA charter holders exhibits a high degree of tax awareness in invest\-
ment practices. Specifically, those managers surveyed adjust clients’ return requirements and expected portfolio
returns for taxes. They consider a security’s holding period when making a decision to sell and engage in periodic
tax\-loss harvesting. Moreover, they consider taxes when making investment selections, allocating assets among
different taxable entities and managing multiple managers. In contrast, relatively few managers report portfolio
performance on a tax\-adjusted basis or present their performance relative to a tax\-adjusted benchmark.
Horn, M. and Oehler, A. (2020\). “Automated portfolio rebalancing: Automatic erosion of investment performance? ”
In:Journal of Asset Management 21(6\), pp. 489–505\.
Robo\-advisers enable investors to establish an automated rebalancing strategy for a portfolio usually consisting
of stocks and bonds. Since households’ portfolios additionally include further frequently tradable assets like
real estate funds, articles of great value and cash(\-equivalents), we analyze whether households would benefit
from a service that automatically rebalances a portfolio which additionally includes the latter assets. In contrast
to previous studies, this paper relies on real\-world household portfolios, which are derived from the German
central bank’s (Deutsche Bundesbank) Panel on Household Finances (PHF)\-Survey. We compute the portfolio
performance increase/decrease that households would have achieved by employing rebalancing strategies instead
of a buy\-and\-hold strategy in the period from September 2010 to July 2015 and analyze whether subsamples
of households with certain sociodemographic and socioeconomic characteristics would have benefited more from
portfolio rebalancing than other household subsamples. The empirical analysis shows that the analyzed German
households would not have benefited from an automated rebalancing service and that no subgroup of households
would have significantly outperformed another subgroup in the presence of rebalancing strategies.
Hsu, Y.\-C., Lin, H.\-W., and Vincent, K. (2017\). Do Cross\-Sectional Stock Return Predictors Pass the Test without
Data\-Snooping Bias? Tech. rep. Institute of Economics Academia Sinica.
This study examines the possible data\-snooping bias as a competing explanation for the anomalies in the cross\-
section of stock returns. We posit that the exhaustive standalone searches for profitable strategies could lead
to recommending spuriously predictive variables. In order to explore the severity of this problem, we use a
multiple testing method to evaluate the profitability of portfolios constructed by these predictors. Our empirical
analyses suggest that over half of the findings based on individual testing method are no longer statistically
significant after we adjust for data\-snooping bias. Excluding the micro\-cap stocks before portfolios construction
and applying the notion of economic significance in this study further weaken the evidence for predictability.
Hsu, P.\-H., Han, Q., Wu, W., and Cao, Z. (2018\). “Asset allocation strategies, data snooping, and the 1 / N rule .”
In:Journal of Banking \& Finance 97, pp. 257–269\.
Using a series of advanced tests from White’s (2000\) Check to correct for data\-snooping bias, we assess the out\-
of\-sample performance of various portfolio strategies relative to the naive 1/N rule. When we analyze 16 basic
portfolio strategies, 126 learning strategies, and nearly 2,000 extended strategies, we find that some strategies
outperform the 1/N rule in conventional tests that do not account for data\-snooping bias. However, after we use
the new tests that control for such bias, we find that none or very few of these strategies outperform the 1/N
rule. Thus, our finding underscores the necessity to control for data\-snooping bias when making asset allocation
decisions.
Hu, Y., Shi, X., and Xu, Z. Q. (2022\). “Mean variance asset liability management with regime switching .” In:arXiv
e\-Print.
This paper is concerned with mean variance portfolio selection with liability, regime switching and random
coefficients. To tackle the problem, we first study a general non\-homogeneous stochastic linear quadratic (LQ)
control problem for which two systems of backward stochastic differential equations (BSDEs) with unbounded
coefficients are introduced. The existence and uniqueness of the solutions to these two systems of BSDEs are
proved by some estimates of BMO martingales and contraction mapping method. Then we obtain the optimal
69state feedback control and optimal value for the stochastic LQ problem explicitly. Finally, closed form efficient
portfolio and efficient frontier for the original mean variance problem are presented.
Huang, M. and Yu, S. (2020\). “A new procedure for resampled portfolio with shrinkaged covariance matrix .” In:
Journal of Applied Statistics 47(44\), pp. 642–652\.
Dealingwithestimationerrorisanimportantissuewhenweimplementthemean\-varianceparadigmforportfolio
construction.Totackletheproblem,twoapproachesareproposedinliterature,theportfolioresamplingtechnique
introducedbyMichuadandthewell\-knownshrinkagedcovariancematrixmethod.Therearecertainevidenceson
theadvantagesofshrinkagedcovarianceoverportfolioresampling,however,itisunclearwhetheracombinationof
thetwoapproachescouldproduceabetterperformancecomparedwithusingshrinkagedcovariancealone.Inthis
paper,weproposeanewalgorithmtointegratedlinearornonlinearshrinkageestimationwithresampledportfolio
to achieve a further improvement. Our method are demonstrated via extensive simulation and application in
active portfolio management process.
Huang, X., Guidolin, M., Platanakis, E., and Newton, D. (2021\). “Dynamic Portfolio Management with Machine
Learning .” In:SSRN e\-Print .
We present a structured portfolio optimization framework with sparse inverse covariance estimation and an
attention\-based LSTM network that exploits machine learning (deep learning) techniques. We shrink Wishart
volatility towards a Graphical Lasso initial covariance estimator and solve the portfolio optimization using a fast
coordinate descent algorithm with regularization determined using a genetic algorithm. We further introduce a
novel portfolio shrinkage rule using an attention\-based Long\-Short\-Term\-Memory (LSTM) network, allowing a
formal selection of reference portfolios where the network forecasts future performance based on predetermined
out\-of\-sample monthly certainty equivalent return. We reduce the dimension of successful candidates and then
linearly combine them. When nested within a minimum\-variance, Bayes\-Stein shrinkage, Black\-Litterman port\-
folioframeworkwithfourtypesofweightconstraintsbasedonno\-short\-selling,upper,lower\-generalizedvariance\-
based restrictions, our approach delivers a clear improvement over the baseline sample\-based minimum\-variance
portfolio and claims superiority over 11 GARCH models used to forecast covariances, as well as a minimum\-
variance combination of all dynamic optimization models. We provide an illustrative example based on optimal
diversification across hedge fund strategies. Robustness checks show our application of sparse covariance domi\-
nates the use of a dimension reduction algorithm for Wishart covariance forecasting.
Hurley, W. J. and Brimberg, J. (2015\). “A note on the sensitivity of the strategic asset allocation problem .” In:
Operations Research Perspectives 2, pp. 133–136\.
The Markowitz meanvariance portfolio optimization problem is a quadratic programming problem whose first\-
order conditions require the solution of a linear system. It is well known that the optimal portfolio weights are
sensitive to parameter estimates, particularly the mean return vector. This has generally been attributed to
the interaction of estimation error and optimization. In this paper we present some examples that suggest the
linear system produced by the first\-order conditions is ill\-conditioned and it is this property that gives rise to
the sensitivity of the optimal weights.
Husmann, S., Shivarova, A., and Steinert, R. (2019\). “Sparsity and Stability for Minimum\-Variance Portfolios .” In:
arXiv e\-Print .
The popularity of modern portfolio theory has decreased among practitioners because of its unfavorable out\-of\-
sample performance. Estimation errors tend to affect the optimal weight calculation noticeably, especially when
a large number of assets is considered. To overcome these issues, many methods have been proposed in recent
years, although most only address a small set of practically relevant questions related to portfolio allocation.
This study therefore sheds light on different covariance estimation techniques, combines them with sparse model
approaches, and includes a turnover constraint that induces stability. We use two datasets \- comprising 319
and 100 companies of the S\&P 500, respectively \- to create a realistic and reproducible data foundation for our
empirical study. To the best of our knowledge, this study is the first to show that it is possible to maintain the
low\-risk profile of efficient estimation methods while automatically selecting only a subset of assets and further
inducing low portfolio turnover. Moreover, we provide evidence that using the LASSO as the sparsity\-generating
model is insufficient to lower turnover when the involved tuning parameter can change over time.
Husmann, S., Shivarova, A., and Steinert, R. (2020\). “Cross\-validated covariance estimators for high\-dimensional
minimum\-variance portfolios .” In:arXiv e\-Print .
The global minimum\-variance portfolio is a typical choice for investors because of its simplicity and broad
applicability. Although it requires only one input, namely the covariance matrix of asset returns, estimating the
optimal solution remains a challenge. In the presence of high\-dimensionality in the data, the sample estimator
70becomesill\-conditioned,whichnegatesthepositiveeffectofdiversificationinanout\-of\-samplesetting.Toaddress
this issue, we review recent covariance matrix estimators and extend the literature by suggesting a multi\-
fold cross\-validation technique. In detail, conducting an extensive empirical analysis with four datasets based
on the S\&P 500, we evaluate how the data\-driven choice of specific tuning parameters within the proposed
cross\-validation approach affects the out\-of\-sample performance of the global minimum\-variance portfolio. In
particular, for cases in which the efficiency of a covariance estimator is strongly influenced by the choice of
a tuning parameter, we detect a clear relationship between the optimality criterion for its selection within
the cross\-validation and the evaluated performance measure. Finally, we show that using cross\-validation can
improve the performance of highly efficient estimators even when the data\-driven covariance parameter deviates
from its theoretically optimal value.
Huttner, A., Mai, J.\-F., and Mineo, S. (2018\). “Portfolio selection based on graphs: Does it align with Markowitz\-
optimal portfolios? ” In:Dependence Modeling 6(1\), pp. 63–87\.
Some empirical studies suggest that the computation of certain graph structures from a (large) historical cor\-
relation matrix can be helpful in portfolio selection. In particular, a repeated finding is that information about
the portfolio weights in the minimum variance portfolio (MVP) from classical Markowitz theory can be inferred
from measurements of centrality in such graph structures. The present article compares the two concepts from
a purely algebraic perspective. It is demonstrated that this heuristic relationship between graph centrality and
the MVP does not originate from a structural similarity between the two portfolio selection mechanisms, but
instead is due to specific features of observed correlation matrices. This means that empirically found relations
between both concepts depend critically on the underlying historical data. Repeated empirical evidence for a
strong relationship is hence shown to constitute a stylized fact of financial return time series.
Hwang, I., Xu, S., and In, F. (2018\). “Naive versus optimal diversification: Tail risk and performance .” In:European
Journal of Operational Research 265(1\), pp. 372–388\.
It is well documented in portfolio optimization that naive diversification outperforms optimal mean\-variance
diversification because the latter is subject to severe estimation error. Our study provides an alternative expla\-
nation for the outperformance of naive diversification by examining the tail risk of naive diversification relative
to optimal mean\-variance diversification. We utilize a rolling\-sample approach and compare the out\-of\-sample
performance and tail risk of various optimal strategies to that of the naive diversification strategy. Using port\-
folios consisting of individual stocks, we show that for portfolios containing relatively small number of stocks,
naive diversification outperforms optimal mean\-variance diversification and is less exposed to tail risk. However,
for relatively large number of stocks in the portfolio, naive diversification maintains its superior performance but
increases tail risk and results in more concave portfolio returns. These results imply that the outperformance of
naive diversification acts as compensation for the increase in tail risk and concavity.
Ielpo, F., Merhy, C., and Simon, G. (2017\). Engineering Investment Process: Making Value Creation Repeatable .
Elsevier. 430 pp.
The book explores the quantitativesteps of a financial investment process. The authors study how these steps are
articulated in order to make any value creation, whatever the asset class, consistent and robust. The discussion
includesfactors,portfolioallocation,statisticalandeconomicbacktesting,butalsotheinfluenceofnegativerates,
dynamical trading, state\-space models, stylized facts, liquidity issues, or data biases. Besides the quantitative
concepts detailed here, the reader will find useful references to other works to develop an in\-depth understanding
of an investment process.
Ilmanen, A. and Maloney, T. (2015\). “Portfolio Rebalancing, Part 1: Strategic Asset Allocation .” In:SSRN e\-Print .
This paper shows that many reasonable rebalancing processes may achieve similar benefits of maintaining a
portfolio’sriskcharacteristics,butalsothatpricemomentumeffectscanbenefitsomeprocessesmorethanothers.
The authors seek to confirm that rebalancing to target allocations helps to maintain more stable portfolio risk
characteristics and improved diversification, and to show that many different methods confer similar long\-term
risk benefits. Rebalancing can be considered an active contrarian strategy when compared to a buy\-and\-hold
benchmark. The authors discuss the main considerations when designing a rebalancing process, and use a simple
empirical analysis to demonstrate the drivers of relative performance over four decades. Asset prices have tended
to exhibit trending behavior, and this has favored less\-frequent rebalancing schedules or wider tolerance bands,
which allow trends to play out between rebalances . When designing a rebalancing process, investors should
balance their tolerance for short\-term variations in portfolio weights against their expectation or belief that
multi\-month price momentum effects will continue in the future. For liquid portfolios, cost considerations may
be secondary.
71Iori, G. and Mantegna, R. N. (2018\). “Empirical analyses of networks in finance .” In:Handbook of Computational
Economics . Vol. 4\. Elsevier, pp. 637–685\.
The recent global financial crisis has triggered a huge interest in the use of network concepts and network tools
to better understand how instabilities can propagate through the financial system. The literature is today quite
vast, covering both theoretical and empirical aspects. This review concentrates on empirical work, and associated
methodologies, concerned with the evaluation of the fragility and resilience of financial and credit markets. The
first part of the review examines the literature on systemic risk that arise from banks mutual exposures. These
exposures stem primarily from interbank lending and derivative positions, but also, indirectly, from common
holdingsofotherassetclasses,thatcanleadtocommonshocksininstancesoffiresales,andfromwidespreadnon\-
performing loans to the real sector during period of economic downturns. We survey (a) studies that characterize
the structure of national interbank networks, in some cases using a multiplex representations, (b) studies that
introduce novel methods to quantify systemic risk and identify systemically important institutions, such as via
stress test scenarios, (c) studies that assess which regulatory measures can help mitigate the propagation of
contagion and distress in the financial system, and (d) studies that explore which location advantages may arise
from holding privileged positions in the interbank network, such as via preferential lending relationships, or
because of occupying a more central node, and if such advantages can provide an early indication of the build
up of systemic risk. The second part of the review is dedicated to the analysis of indirect networks, specifically
(e) proximity based network, i.e. networks obtained starting from a proximity measure sometime filtered with a
network filtering methodology, (f) association network, i.e. networks where a link between two financial actors
is set if a statistical test again a null hypothesis is rejected, and (g) statistically validated networks, i.e. event
or relationship networks where a subset of links is selected according to a statistical validation associated with
the rejection of a random null hypothesis. The need for a joint consideration of direct and indirect channels of
contagion is briefly discussed.
Iorio, C., Frasso, G., D’Ambrosio, A., and Siciliano, R. (2018\). “A P\-spline based clustering approach for portfolio
selection.” In:Expert Systems with Applications 95, pp. 88–103\.
In the last years, many clustering techniques dealing with time course data have been proposed due to recent
interests in studying phenomena that change over time. A new clustering method suitable for time series appli\-
cations has been recently proposed by exploiting the properties of the P\-splines approach. This semi\-parametric
tool has several advantages, i.e. it facilitates the removal of noise from time series and it ensures a computa\-
tional time saving. In this paper, we propose to use this clustering approach on financial data with the aim of
building a financial portfolio. Our proposal works directly on time series without any pre\-processing, except for
the computation of the spline coefficients and, eventually, normalizing the series. We show that our strategy is
useful to support the investment decisions of financial practitioners.
Irlam, G. (2020\). “Machine learning for retirement planning .” In:The Journal of Retirement 8(1\), pp. 32–29\.
Machine learning provides a new approach to solving problems in many fields. This article explores the use of
machine learning to solve the retirement portfolio problem: deciding how much wealth to consume and how to
allocate the remainder. After first reviewing existing approaches to the portfolio problem, this article looks in
detail at the use of reinforcement learning. For simple financial scenarios where the optimal solution is known,
reinforcement learning is found to deliver to within a few percent of the optimal solution. For more compli\-
cated financial scenarios, with no known optimal solution, reinforcement learning outperforms other common
approaches. Reinforcement learning proves capable of optimizing highly complex financial models, including the
effects of income taxes, mean\-reverting asset classes, and time\-varying bond yield curves, all of which other
approaches cannot handle. Reinforcement learning appears to be the first fundamentally new approach to the
portfolio problem in over 50 years.
Israelov, R. and Tummala, H. (2018\). “An Alternative Option to Portfolio Rebalancing .” In:The Journal of Deriva\-
tives25(3\), pp. 7–32\.
Portfolio managers, whether running a passive or an active strategy, typically select target weights on the various
asset classes and securities they hold. The prime example is choosing the mix between stocks and bonds. But as
marketpricesevolve,actualweightsdriftawayfromthetargets.Thisleadstotrackingerrorandtransactioncosts
in order to rebalance positions to the desired levels. Rebalancing entails selling assets that have gone up in value
and increasing exposure to those whose prices have dropped. As Israelov and Tummala point out, this is how a
short position in a call option behaves, and they show how to design a hedging strategy based on writing calls
that offsets much of the basis risk in trying to run a portfolio with fixed asset weights. An empirical illustration
shows that their proposed overlay strategy would have performed well historically in reducing unintended timing
72risk in a 60/40 stock/bond portfolio. An additional benefit of the plan is that by selling options, it harvests the
volatility risk premium embedded in their prices, which enhances returns at the same time risk is being reduced.
Jacobs, B. I., Levy, K. N., and Markowitz, H. M. (2005\). “Portfolio Optimization with Factors, Scenarios, and
Realistic Short Positions .” In:Operations Research 53(4\), pp. 586–599\.
This paper presents fast algorithms for calculating mean\-variance efficient frontiers when the investor can sell
securities short as well as buy long, and when a factor and/or scenario model of covariance is assumed. Currently,
fast algorithms for factor, scenario, or mixed (factor and scenario) models exist, but (except for a special case of
the results reported here) apply only to portfolios of long positions. Factor and scenario models are used widely
in applied portfolio analysis, and short sales have been used increasingly as part of large institutional portfolios.
Generally, the critical line algorithm (CLA) traces out mean\-variance efficient sets when the investor’s choice is
subject to any system of linear equality or inequality constraints. Versions of CLA that take advantage of factor
and/or scenario models of covariance gain speed by greatly simplifying the equations for segments of the efficient
set. These same algorithms can be used, unchanged, for the long\-short portfolio selection problem provided a
certain condition on the constraint set holds. This condition usually holds in practice.
Jacobsen,B. and Lee, W.(2020\). “RiskParityOptimalityEvenwith NegativeSharpe RatioAssets .” In:The Journal
of Portfolio Management 46(6\), pp. 110–119\.
A stopped clock is right twice a day. Similarly, any portfolio allocation is likely to be optimal at least at some
point. Risk parity is no stopped clock. The authors derive a general result regarding when and why risk parity is
Sharpe ratio optimal, even with negative\-Sharpe\-ratio assets. This derivation goes beyond the simple observation
that risk parity is Sharpe ratio optimal when asset correlations and Sharpe ratios are identical. Based on the
analytical result, the authors develop an indicator to describe when risk\-parity strategies are likely to be more
or less optimal. They also explain how negative\-Sharpe\-ratio assets can still be an important part of a portfolio\-
whether it is a risk\-parity portfolio or not. Although risk parity and risk balancing in general do not require
assumptions about returns, the authors provide guidance regarding how to infer returns that are consistent with
the portfolios built from targeting risk.
Jaconetti, C. M., DiJoseph, M. A., Jr., F. M. K., Pakula, D., and Lobel, H. (2020\). From assets to income: A
goals\-based approach to retirement spending . Tech. rep. Vanguard.
Although the population and life expectancies of U.S. retirees are increasing, portfolio yields remain at histor\-
ically low levels. As defined benefit income becomes less commonly available, the need for informed retirement
portfolio spending strategies is more critical, and yet more complex, than ever. The stakes are high, and the
impact of subpar decisions can be severe. Because every investor’s financial situation is unique, there is no
one\-size\-fits\-all solution. But developing and implementing a personal spending strategy can reduce anxiety and
stress about the ability to meet retirement income goals. Retirees who hold the majority of their assets in tax\-
deferred accounts can turn thoseassets into income by setting up an automatic withdrawal plan. They can also
purchase an investment specifically designed to provide regular distributions. Those whose portfolios contain a
significant portion of taxable assets can add value by working with an advisor to develop a goals\-based strategy.
Whatever spending strategy you choose, the complexity and consequences of the process underscore the need
for and value of skillful guidance.
Jaeger, M., Krugel, S., Marinelli, D., Papenbrock, J., and Schwendner, P. (2020\). “Understanding machine learning
for diversified portfolio construction by explainable AI .” In:SSRN e\-Print .
In this paper, we construct a pipeline to investigate heuristic diversification strategies in asset allocation. We
use machine learning concepts (”explainable AI”) to compare the robustness of different strategies and back
out implicit rules for decision making.In a first step, we augment the asset universe (the empirical dataset)
with a range of scenarios generated with a block bootstrap from the empirical dataset.Second, we backtest the
candidate strategies over a long period of time, checking their performance variability. Third, we use XGBoost
as a regression model to connect the difference between the measured performances between two strategies to
a pool of statistical features of the portfolio universe tailored to the investigated strategy. Finally, we employ
the concept of Shapley values to extract the relationships that the model could identify between the portfolio
characteristics and the statistical properties of the asset universe. We test this pipeline for studying risk\-parity
strategies with a volatility target, and in particular, comparing the machine learning\-driven Hierarchical Risk
Parity (HRP) to the classical Equal Risk Contribution (ERC) strategy.In the augmented dataset built from
a multi\-asset investment universe of commodities, equities and fixed income futures, we find that HRP better
matches the volatility target, and shows better risk\-adjusted performances. Finally, we train XGBoost to learn
the difference between the realized Calmar ratios of HRP and ERC and extract explanations.The explanations
73provide fruitful ex\-post indications of the connection between the statistical properties of the universe and
the strategy performance in the training set. For example, the model confirms that features addressing the
hierarchical properties of the universe are connected to the relative performance of HRP respect to ERC.
Jaeger, M., Krugel, S., Marinelli, D., Papenbrock, J., and Schwendner, P. (2021a). “Interpretable Machine Learning
for Diversified Portfolio Construction .” In:The Journal of Financial Data Science 3(3\), pp. 31–51\.
In this paper, the authors construct a pipeline to benchmark Hierarchical Risk Parity (HRP) relative to Equal
Risk Contribution (ERC) as examples of diversification strategies allocating to liquid multi\-asset futures markets
with dynamic leverage (”volatility target”). The authors use interpretable machine learning concepts (”explain\-
able AI”) to compare the robustness of the strategies and to back out implicit rules for decision making. The
empirical dataset consists of 17 equity index, government bond and commodity futures markets across 20 years.
The two strategies are backtested for the empirical dataset and for about 100 000 bootstrapped datasets. XG\-
Boost is used to regress the Calmar ratio spread between the two strategies against features of the bootstrapped
datasets. Compared to ERC, HRP shows higher Calmar ratios and better matches the volatility target. Using
Shapley values, the Calmar ratio spread can be attributed especially to univariate drawdown measures of the
asset classes.
Jaeger, M., Krugel, S., Papenbrock, J., and Schwendner, P. (2021b). “Adaptive Seriational Risk Parity and other
Extensions for Heuristic Portfolio Construction using Machine Learning and Graph Theory .” In:SSRN e\-Print .
In this article, the authors present a conceptual framework named Adaptive Seriational Risk Parity (ASRP)
to extend Hierarchical Risk Parity (HRP) as an asset allocation heuristic. The first step of HRP (quasi\-
diagonalization) determining the hierarchy of assets is required for the actual allocation in the second step
of HRP (recursive bisectioning). In the original HRP scheme, this hierarchy is found using the single\-linkage
hierarchical clustering of the correlation matrix, which is a static tree\-based method. The authors of this paper
compare the performance of the standard HRP with other static and also adaptive tree\-based methods, but
also seriation\-based methods that do not rely on trees. Seriation is a broader concept allowing to reorder the
rows or columns of a matrix to best express similarities between the elements. Each discussed variation leads
to a different time series reflecting portfolio performance using a 20\-year backtest of a multi\-asset futures uni\-
verse. An unsupervised representation learning based on this time series data creates a taxonomy that groups
the strategies in high correspondence to the structure of the various types of ASRP. The performance analysis
of the variations shows that most of the static tree\-based alternatives of HRP outperform the single linkage
clustering used in HRP on a risk\-adjusted basis. Adaptive tree methods show mixed results and most generic
seriation\-based approaches underperform.
Jagannathan, R. and Ma, T. (2003\). “Risk Reduction in Large Portfolios: Why Imposing the Wrong Constraints
Helps.” In:Journal of Finance 58, pp. 1561–1583\.
Green and Hollifield (1992\) argue that the presence of a dominant factor would result in extreme negative
weights in mean\-variance efficient portfolios even in the absence of estimation errors. In that case, imposing
no\-short\-sale constraints should hurt, whereas empirical evidence is often to the contrary. We reconcile this
apparent contradiction. We explain why constraining portfolio weights to be nonnegative can reduce the risk in
estimated optimal portfolios even when the constraints are wrong. Surprisingly, with no\-short\-sale constraints
in place, the sample covariance matrix performs as well as covariance matrix estimates based on factor models,
shrinkage estimators, and daily data.
Jain,P.andJain,S.(2019\). “CanMachineLearning\-BasedPortfoliosOutperformTraditionalRisk\-BasedPortfolios?
The Need to Account for Covariance Misspecification .” In:Risks7(3\), pp. 74\+.
TheHierarchicalriskparity(HRP)approachofportfolioallocation,introducedbyLopezdePrado(2016\),applies
graph theory and machine learning to build a diversified portfolio. Like the traditional risk\-based allocation
methods, HRP is also a function of the estimate of the covariance matrix, however, it does not require its
invertibility. In this paper, we first study the impact of covariance misspecification on the performance of
the different allocation methods. Next, we study under an appropriate covariance forecast model whether the
machine learning based HRP outperforms the traditional risk\-based portfolios. For our analysis, we use the
test for superior predictive ability on out\-of\-sample portfolio performance, to determine whether the observed
excess performance is significant or if it occurred by chance. We find that when the covariance estimates are
crude, inverse volatility weighted portfolios are more robust, followed by the machine learning\-based portfolios.
Minimum variance and maximum diversification are most sensitive to covariance misspecification. HRP follows
the middle ground; it is less sensitive to covariance misspecification when compared with minimum variance
or maximum diversification portfolio, while it is not as robust as the inverse volatility weighed portfolio. We
74also study the impact of the different rebalancing horizon and how the portfolios compare against a market\-
capitalization weighted portfolio.
Jay, E., Soler, T., Ovarlez, J.\-P., Peretti, P. D., and Chorro, C. (2020a). “Robust Covariance Matrix Estimation
and Portfolio Allocation: The Case of Non\-Homogeneous Assets .” In:ICASSP 2020 \- 2020 IEEE International
Conference on Acoustics, Speech and Signal Processing (ICASSP) . IEEE.
This paper presents how the most recent improvements made on covariance matrix estimation and model order
selection can be applied to the portfolio optimization problem. Our study is based on the case of the Maximum
Variety Portfolio and may be obviously extended to other classical frameworks with analogous results. We focus
on the fact that the assets should preferably be classified in homogeneous groups before applying the proposed
methodology which is to whiten the data before estimating the covariance matrix using the robust Tyler M\-
estimator and the Random Matrix Theory (RMT). The proposed procedure is applied and compared to standard
techniques on real market data showing promising improvements.
Jay, E., Soler, T., Terreaux, E., Ovarlez, J.\-P., Pascal, F., Peretti, P. D., and Chorro, C. (2020b). “Improving
portfolios global performance using a cleaned and robust covariance matrix estimate .” In:Soft Computing 24(12\),
pp. 8643–8654\.
This paper presents how the use of a cleaned and robust covariance matrix estimate can improve significantly the
overall performance of maximum variety and minimum variance portfolios. We assume that the asset returns are
modelled through a multi\-factor model where the error term is a multivariate and correlated elliptical symmetric
noise extending the classical Gaussian assumptions. The factors are supposed to be unobservable and we focus
on a recent method of model order selection, based on the random matrix theory to identify the most informative
subspace and then to obtain a cleaned (or de\-noised) covariance matrix estimate to be used in the maximum
variety and minimum variance portfolio allocation processes. We apply our methodology on real market data
and show the improvements it brings if compared with other techniques especially for non\-homogeneous asset
returns.
Jennings, W. W. and Payne, B. C. (2020\). “Corrections Should Trigger Rebalancing .” In:The Journal of Wealth
Management 23(33\), pp. 37–49\.
We start from the provocative contention that if an investor did not rebalance earlier this year (2020\), then that
investor does not have an asset allocation policy. More specifically, that investor does not have a rebalancing
policy to preserve their asset allocation. We then work backward from a presumption that a correction needs to
induce a rebalancing trade and develop an algebraic solution for the width of the rebalancing range to ensure it
does so. Across a range of reasonable assumptions, rebalancing ranges need to be tighter than traditional norms.
Jurczenko, E. and Teiletche, J. (2019\). “Expected Shortfall Asset Allocation: A Multi\-Dimensional Risk Budgeting
Framework .” In:The Journal of Alternative Investments 22(2\), pp. 7–22\.
In this article, we propose a generalized expected shortfall risk\-budgeting investing framework, which offers a
simple and flexible way to deal with various risks beyond volatility, namely valuation, asymmetry, tail, and
illiquidity risks. We empirically illustrate the methodology by proposing a risk\-based strategic allocation for a
multi\-asset portfolio made of traditional and alternative assets with different degrees of liquidity.
Kakouris, I. and Rustem, B. (2014\). “Robust portfolio optimization with copulas .” In:European Journal of Opera\-
tional Research 235(1\), pp. 28–37\.
We provide the copula formulation for Value at Risk. We extend Value at Risk to Conditional Value at Risk
for copulas. Linear optimization problem for Worst Case Conditional Value at Risk with copulas. Numerical
applications in portfolio optimization of stock markets. Conditional Value at Risk (CVaR) is widely used in
portfolio optimization as a measure of risk. CVaR is clearly dependent on the underlying probability distribution
of the portfolio. We show how copulas can be introduced to any problem that involves distributions and how
they can provide solutions for the modeling of the portfolio. We use this to provide the copula formulation of
the CVaR of a portfolio. Given the critical dependence of CVaR on the underlying distribution, we use a robust
framework to extend our approach to Worst Case CVaR (WCVaR). WCVaR is achieved through the use of rival
copulas. These rival copulas have the advantage of exploiting a variety of dependence structures, symmetric
and not. We compare our model against two other models, Gaussian CVaR and Worst Case Markowitz. Our
empirical analysis shows that WCVaR can asses the risk more adequately than the two competitive models
during periods of crisis.
Kalayci, C. B., Ertenlice, O., and Akbay, M. A. (2019\). “A comprehensive review of deterministic models and
applications for mean\-variance portfolio optimization .” In:Expert systems with applications 125, pp. 345–368\.
75Portfolio optimization is the process of determining the best combination of securities and proportions with
the aim of having less risk and obtaining more profit in an investment. Utilizing covariance as a risk measure,
mean\-variance portfolio optimization model has brought a revolutionary approach to quantitative finance. Since
then, along with the advancements in computational power and algorithmic enhancements, a lot of efforts have
been made on improving this model by considering real\-life conditions and solving model variants with various
methodologies tested on various data and performance measures. A comprehensive literature review of recent
and novel papers is crucial to establish a pattern of the past, and to pave the way on future directions. In this
paper, a total of 175 papers published in the last two decades are selected within the scope of operations research
community and reviewed in detail. Thus, a comprehensive survey on the deterministic models and applications
suggested for mean\-variance portfolio optimization in which several variants of this model as well as additional
real\-life constraints are studied. The review classifies the approaches according to exact and approximate at\-
tempts and analyzes the proposed algorithms based on various data and performance indicators in depth. Areas
of future research are outlined.
Kalyagin, V. A. and Slashchinin, S. V. (2019\). “Impact of error in parameter estimations on large scale portfo\-
lio optimization .” In:Approximation and optimization: algorithms, complexity and applications . Ed. by I. C.
Demetriou and P. M. Pardalos. Vol. 145\. Springer optimization and its applications. Springer International
Publishing, pp. 151–184\.
Portfolio selection is construction of portfolios that maximize level of the expected returns from investments, but
at the same time have low involved risks. One fundamental approach for quantifying the risk\-return trade\-off of
assets is mean\-variance analysis. In this case, it is crucial to accurately estimate parameters of the model. We
examine how estimation error for means and covariance matrix of stock returns may affect the results of selected
portfolios. One of the main contributions of this research are different experiments conducted using both the
real data from different stock markets and generated samples to compare the out\-of\-sample performance of the
estimators and how estimation error may affect results of portfolio selection. A new surprising phenomenon is
observed for large scale portfolio optimization: efficiency of obtained optimal portfolio is biased with respect to
the true optimal portfolio. Different aspects of this phenomenon and possible ways to reduce its negative effect
are discussed.
Kapsos, M., Christofides, N., and Rustem, B. (2018\). “Robust risk budgeting .” In:Annals of Operations Research
266, pp. 199–221\.
Risk based portfolio construction and particular risk parity or equally weighted risk contribution became popular
among practitioners. These approaches focus only on risk and are agnostic with respect to the expected returns.
In this paper, we consider risk budgeting; a generalization of risk parity. We propose an alternative formulation
that is more efficient computationally. We introduce the robust risk budgeting, a robust variant of the standard
risk budgeting that deals with the uncertainty in the input parameters. We show that the problem remains
tractable under different types of uncertainty. We evaluate the proposed framework on real data and we observe
a positive premium associated with the robust variant.
Kaya, H. and Lee, W. (2014\). “Risk Parity: Common Fallacies .” In:SSRN e\-Print .
The concentration in certain types of risk, such as equity risk, coupled with drawdowns that were on par with
the equity markets as a whole, turned the spotlight onto alternative approaches to asset allocation such as
risk parity. To simply define such approaches, risk parity strategies seek to build more diversified and more
efficient portfolios by allocating capital to assets based on an asset’s expected contribution to the total risk of
the portfolio, rather than on forecasts of the asset’s returns. Using this approach, the expectation is that the
risk/return profile of a risk parity portfolio would be more attractive over the long term and less subject to
drawdowns and other risk concentrations than other asset allocation approaches where risk is not an explicit
consideration. Given the attractiveness of this notion, it is not surprising that investments in these strategies
have mushroomed in recent years. But with this influx of investor interest has come an increasing amount of
criticism of certain aspects of these strategies. While numerous criticisms exist, one of the most common is that
risk parity strategies have only performed well due to a bull market for bonds and that the leverage employed
subjects investors to increased risks. We believe these criticisms warrant a deeper look, as they often reflect a
lack of understanding of the underpinnings, process, and management of risk parity strategies. In this paper, we
seek to address several of the most common misconceptions.
Kaya, H. (2015\). “Eccentricity in Asset Management .” In:Journal of Network Theory in Finance 1(1\), pp. 1–32\.
We describe how networks based on information theory can help measure and visualize systemic risk, enhance
diversification, and help price assets. To do this, we first define a distance measure based on the mutual informa\-
76tion between asset pairs and use this measure in the construction of minimum spanning trees. The dynamics of
the shape and the descriptive statistics of these trees are analyzed in various investment domains. The method
provides evidence of regime changes in dependency structures prior to market sell\-offs, and as such, it is a
potential candidate for monitoring systemic risk. We also provide empirical evidence that the assets that are
located towards the center of the network tend to have higher returns. Finally, an investment strategy that
utilizes network centrality information is shown to add value historically.
Kaya, H. (2016\). “Intuitive Ambiguity Management .” In:SSRN e\-Print .
This paper is about the issue of input parameter uncertainty in portfolio optimization in a discrete setting with
finite states (such as the case in a world with different macroeconomic regimes). In such a setting, being unable
to assign reliable point estimates to the probabilities (or frequencies) of the states creates the ambiguity. We first
describe how this ambiguity can be modeled probabilistically. Then, we show how this added uncertainty can be
dealt with in optimal asset allocation problems. In simple\-yet\-realistic example applications we demonstrate that
without sacrificing much of the upside, ambiguity managed portfolios enhance the uniformity of returns across
differentstateswhencomparedtoportfoliosconstructedbytraditionalmethods.Westressthatakeyadvicefrom
these methods builds the case for insurance\-like and potentially negative yielding investments such as bonds and
commodities so as to hedge the unforeseeable macro uncertainties for a smoother portfolio performance. Finally,
we offer a variety of problem domains in which ambiguity management can be nested including macroeconomic
scenario based asset allocation, investing with regime switching models, momentum investing, and risk\-based
investing.
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
Kazak, E. and Pohlmeier, W. (2019\). “Testing out\-of\-sample portfolio performance .” In:International Journal of
Forecasting 35(2\), pp. 540–554\.
This paper studies the quality of portfolio performance tests based on out\-of\-sample returns. By disentangling
the components of the out\-of\-sample performance, we show that the observed differences are driven largely by
the differences in estimation risk. Our Monte Carlo study reveals that the puzzling empirical findings of inferior
performancesoftheoreticallysuperiorstrategiesresultmainlyfromthelowpowerofthesetests.Thus,ourresults
provide an explanation as to why the null hypothesis of equal performance of the simple equally\-weighted
portfolio compared to many theoretically\-superior alternative strategies cannot be rejected in many out\-of\-
sample horse races. Our findings turn out to be robust with respect to different designs and the implementation
strategies of the tests. For the applied researcher, we provide some guidance as to how to cope with the problem
of low power. In particular, we make use of a novel pretest\-based portfolio strategy to show how the information
regarding performance tests can be used optimally.
Kazak,E.andPohlmeier,W.(2020\). Portfolio Pretesting with Machine Learning .Tech.rep.UniversityofLancaster.
This paper exploits the idea of pretesting to choose between competing portfolio strategies. We propose an
estimator for a portfolio weight vector, which optimally trades off between Type I and Type II errors when
choosing the best investment strategy. Furthermore we accommodate the idea of bagging in the portfolio testing
problems, which helps to avoid sharp thresholding and reduces the amount of portfolio turnover. Our approach
borrows from both shrinkage and forecast combination literature. The portfolio weights of our strategy are
weighted averages of the portfolio weights from a set of stand\-alone strategies. More specifically, the weights are
generated from a pseudo out\-of\-sample portfolio pretesting, such that they reflect the probability that a given
strategy will be overall best performing. Contrary to previous approaches, the shrinkage intensity is continuously
updated to incorporate the most recent information in the rolling window forecasting set\-up. We show that the
77bagged pretest estimator performs exceptionally well, especially when combined with adaptive smoothing. The
resulting strategy allows for a flexible and smooth switch between the underlying strategies and is shown to
outperform the corresponding stand\-alone strategies.
Ke, Y., Lian, H., and Zhang, W. (2021\). “High\-Dimensional Dynamic Covariance Matrices With Homogeneous
Structure .” In:Journal of Business \& Economic Statistics .
High\-dimensional covariance matrices appear in many disciplines. Much literature has devoted to the research
in high\-dimensional constant covariance matrices. However, constant covariance matrices are not sufficient in
applications, for example, in portfolio allocation, dynamic covariance matrices would be more appropriate. As
arguedinthisarticle,therearetwodifficultiesintheintroductionofdynamicstructuresintocovariancematrices:
(1\) simply assuming each entry of a covariance matrix is a function of time to introduce the dynamic needed
would not work; (2\) there is a risk of having too many unknowns to estimate due to the high dimensionality. In
this article, we propose a dynamic structure embedded with a homogeneous structure. We will demonstrate the
proposed dynamic structure makes more sense in applications and avoids, in the meantime, too many unknown
parameters/functions to estimate, due to the embedded homogeneous structure. An estimation procedure is also
proposed to estimate the proposed high\-dimensional dynamic covariance matrices, and asymptotic properties
are established to justify the proposed estimation procedure. Intensive simulation studies show the proposed
estimation procedure works very well when the sample size is finite. Finally, we apply the proposed high\-
dimensional dynamic covariance matrices to portfolio allocation. It is interesting to see the resulting portfolio
yields much better returns than some commonly used ones.
Ke, Y., Minsker, S., Ren, Z., Sun, Q., and Zhou, W.\-X. (2019\). “User\-Friendly Covariance Estimation for Heavy\-
Tailed Distributions .” In:Statistical Science 34(3\), pp. 454–471\.
We provide a survey of recent results on covariance estimation for heavy\-tailed distributions. By unifying ideas
scatteredintheliterature,weproposeuser\-friendlymethodsthatfacilitatepracticalimplementation.Specifically,
we introduce elementwise and spectrumwise truncation operators, as well as their M\-estimator counterparts, to
robustify the sample covariance matrix. Different from the classical notion of robustness that is characterized
by the breakdown property, we focus on the tail robustness which is evidenced by the connection between
nonasymptotic deviation and confidence level. The key insight is that estimators should adapt to the sample
size, dimensionality and noise level to achieve optimal tradeoff between bias and robustness. Furthermore, to
facilitate practical implementation, we propose data\-driven procedures that automatically calibrate the tuning
parameters. We demonstrate their applications to a series of structured models in high dimensions, including
the bandable and low\-rank covariance matrices and sparse precision matrices. Numerical studies lend strong
support to the proposed methods.
Kelliher, C., Hazrachoudhury, A., and Irving, B. (2022\). “A Novel Approach to Risk Parity: Diversification across
Risk Factors and Market Regimes .” In:The Journal of Portfolio Management 48(3\).
In this article, the authors describe a robust approach to portfolio diversification that balances risk contributions
across risk factors and market regimes. After identifying four compensated macro risk factors\-growth, inflation,
real rates, and liquidity\-the authors construct a factor portfolio for each based on a broad set of asset classes,
including proxies for private equity and private real estate. Next, the authors identify five distinct market
regimes characterized by unique asset class behaviors. The factor portfolios are then combined such that the
risk contributions to the resulting total portfolio are as balanced as possible, regardless of which market regime
materializes. By combining regime\-aware correlations with dynamic volatility estimates for each factor and
applying standard 1\.5x to 2x leverage, the authors demonstrate a risk\-parity portfolio with 10% ex ante volatility
andattractiveabsoluteandrisk\-adjustedreturns.Comparedwithatraditional60/40portfolio,theproposedrisk\-
parity portfolio displays greater diversification, more consistent factor\-risk contributions, and greater resilience
to economic shocks.
Khang, K. and Picca, A. (2021\). “Waiting for the Next Factor Wave: Daily Rebalancing around Market Cycle
Transitions .” In:The Journal of Portfolio Management 47(2\), pp. 127–144\.
To deliver historically observed factor premiums, long\-only factor investing relied heavily on a small number of
periods, when factors realized outsized returns in the midst of changing market leadership. This article shows
that by rebalancing factor funds more frequently during these periods – rebalancing on a daily basis instead of
monthly or biannually – investors would have achieved significantly higher factor premiums, effectively doubling
the historically observed premiums of many factors. These findings indicate that to harvest factor premiums to
their maximal potential, skill is needed on the part of the fund manager\-an ability to tell the right moment to
aggressively rebalance.
78Kim, H. and Kim, S. (2021\). “Reduction of estimation error impact in the risk parity strategies .” In:Quantitative
Finance.
We consider the risk parity strategy in the presence of estimation errors. We show that risk contributions from
constituentsofthisportfoliocanbeconsiderablysensitivetoestimationerrorsinthesensethatriskcontributions
are highly uneven on an ex post basis. In particular, we demonstrate that the sensitivity becomes exaggerated if
Fama\-French factors constitute the portfolio because of their characteristic of having low pairwise correlations.
Our work demonstrates that the instability of the out\-of\-sample risk contributions is associated with a local
property with statistical significance near to the constructed portfolio. Based on this observation, we propose a
new algorithm for the risk parity strategy to mitigate the sensitivity of the optimized portfolio’s out\-of\-sample
risk contributions from estimation errors. Through empirical study, we find that the portfolio constructed by the
proposed algorithm consistently outperforms its competitors in terms of the out\-of\-sample risk contributions.
Kim, J. H., Kim, W. C., and Fabozzi, F. J. (2018a). “Recent advancements in robust optimization for investment
management .” In:Annals of Operations Research 266, pp. 183–198\.
Robust optimization has become a widely implemented approach in investment management for incorporating
uncertainty into financial models. The first applications were to asset allocation and equity portfolio construc\-
tion. Significant advancements in robust portfolio optimization took place since it gained popularity almost
two decades ago for improving classical models on portfolio optimization. Recently, studies applying the worst\-
case framework to bond portfolio construction, currency hedging, and option pricing have appeared in the
practitioner\-oriented literature. Our focus in this paper is on recent advancements to categorize robust opti\-
mization models into asset allocation at the asset class level and portfolio selection at the individual asset level,
and we further separate robust portfolio selection approaches specific to each asset class. This organization
provides a clear overview on how robust optimization is extensively implemented in investment management.
Kim, J. H., Kim, W. C., Kwon, D.\-G., and Fabozzi, F. J. (2018b). “Robust equity portfolio performance .” In:Annals
of Operations Research 266, pp. 1559–1579\.
The earliest documented analytical approach to portfolio selection is Markowitz mean\-variance analysis, which
attempts to find the portfolio with optimal performance by considering the tradeoff between return and risk. The
performance of mean\-variance analysis has been the subject of many studies and compared to other portfolio
construction approaches such as a naive equally\-weighted allocation scheme. In recent years, several approaches
have been proposed to improve the mean\-variance model by reducing the sensitivity of the portfolio selection
process in order achieve robust performance. Although robust portfolio optimization has been one of the most
researched methods for improving portfolio robustness, the performance of robust portfolios has not been the
major focus of studies. In this paper, a comprehensive analysis on robust portfolio performance is presented
for equity portfolios constructed in the U.S. market during the period 1980 and 2014, and results confirm the
advantage of robust portfolio optimization for controlling uncertainty while efficiently allocating investments.
Kim, J. H., Lee, Y., Kim, W. C., and Fabozzi, F. J. (2021\). “Mean\-Variance Optimization for Asset Allocation .”
In:The Journal of Portfolio Management 47(4\).
The mean\-variance model is widely acknowledged as the foundation of portfolio allocation because it provides
a framework for analyzing the trade\-off between risk and return for gaining diversification benefits. Despite the
well\-known shortcomings of the model, it is often the starting point for making asset allocation decisions. In
this article, the authors briefly review mean\-variance optimization and approaches for resolving its limitations
by demonstrating backtest results on asset allocation. Feedback from asset managers is also included to explain
how optimization methods are applied in practice.
Kim, W. C., Kim, J. H., and Fabozzi, F. J. (2014\). “Deciphering robust portfolios .” In:Journal of Banking \&
Finance 45, pp. 1–8\.
Robust portfolio optimization has been developed to resolve the high sensitivity to inputs of the Markowitz
mean variance model. Although much effort has been put into forming robust portfolios, there have not been
many attempts to analyze the characteristics of portfolios formed from robust optimization. We investigate the
behavior of robust portfolios by analytically describing how robustness leads to higher dependency on factor
movements. Focusing on the robust formulation with an ellipsoidal uncertainty set for expected returns, we show
that as the robustness of a portfolio increases, its optimal weights approach the portfolio with variance that is
maximally explained by factors.
Kim, W. C., Kwon, D.\-G., Lee, Y., Kim, J. H., and Lin, C. (2020\). “Personalized goal\-based investing via multi\-stage
stochastic goal programming .” In:Quantitative Finance 20(3\) (3\), pp. 515–526\.
79In this paper, we propose a goal\-based investment model that is suitable for personalized wealth management.
The model only requires a few intuitive inputs such as size of wealth, investment amount, and consumption goals
from individual investors. In particular, a priority level can be assigned to each consumption goal and the model
provides a holistic solution based on a sequential approach starting with the highest priority. This allows strict
prioritization by maximizing the probability of achieving higher priority goals that are not affected by goals
with lower priorities. Furthermore, the proposed model is formulated as a linear program that efficiently finds
the optimal financial plan. With its simplicity, flexibility, and computational efficiency, the proposed goal\-based
investment model provides a new framework for automated investment management services.
Kim, W., Kim, J., Ahn, S., and Fabozzi, F. (2013\). “What do robust equity portfolio models really do? ” In:Annals
of Operations Research 205(1\), pp. 141–168\.
Most of previous work on robust equity portfolio optimization has focused on its formulation and performance.
In contrast, in this paper we analyze the behavior of robust equity portfolios to determine whether reducing the
sensitivity to input estimation errors is all robust models do and investigate any side\-effects of robust formu\-
lations. Therefore, our focus is on the relationship between fundamental factors and robust models in order to
determine if robust equity portfolios are consistently investing more in the factors opposed to individual asset
movements. To do so, we perform regressions with factor returns to explain how robust portfolios behave com\-
pared to portfolios generated from the Markowitz’s mean\-variance model. We find that robust equity portfolios
consistently show higher correlation with the three fundamental factors used in the Fama\-French factor model.
Furthermore, more robustness among robust portfolios results in a higher correlation with the Fama\-French
three factors. In fact, we show that as equity portfolios under no constraints on portfolio weights become more
robust, they consistently depend more on the market and large factors. These results show that robust models
are betting on the fundamental factors instead of individual asset movements.
Kinlaw, W. B., Kritzman, M., Page, S., and Turkington, D. (2021\). “The Myth of Diversification Reconsidered .”
In:The Journal Of Portfolio Management 47(8\).
That investors should diversify their portfolios is a core principle of modern finance. Yet there are some periods
where diversification is undesirable. When the portfolio’s main growth engine performs well, investors prefer
the opposite of diversification. An ideal complement to the growth engine would provide diversification when it
performs poorly and unification when it performs well. Numerous studies have presented evidence of asymmetric
correlations between assets. Unfortunately, this asymmetry is often of the undesirable variety: it is characterized
by downside unification and upside diversification. In other words, diversification often disappears when it is
most needed. In this article we highlight a fundamental flaw in the way that some prior studies have measured
correlation asymmetry. Because they estimate downside correlations from subsamples where both assets perform
poorly, they ignore instances of ”successful” diversification; that is, periods where one asset’s gains offset the
other’s losses. We propose instead that investors measure what matters: the degree to which a given asset
diversifies the main growth engine when it underperforms. This approach yields starkly different conclusions,
particularly for asset pairs with low full sample correlation. In this paper we review correlation mathematics,
highlight the flaw in prior studies, motivate the correct approach, and present an empirical analysis of correlation
asymmetry across major asset classes.
Kinn, D. (2018\). “Reducing Estimation Risk in Mean\-Variance Portfolios with Machine Learning .” In:arXiv e\-Print .
In portfolio analysis, the traditional approach of replacing population moments with sample counterparts may
lead to suboptimal portfolio choices. In this paper I show that selecting asset positions to maximize expected
quadratic utility is equivalent to a machine learning (ML) problem, where the asset weights are chosen to
minimize out of sample mean squared error. It follows that ML specifically targets estimation risk when choosing
the asset weights, and that ”off\-the\-shelf” ML algorithms obtain optimal portfolios taking parameter uncertainty
into account. Linear regression is a special case of the proposed ML framework, equivalent to the traditional
approach. Standard results from the machine learning literature may be used to derive conditions for when
ML algorithms improve upon linear regression. Based on simulation studies and several datasets, I find that
ML significantly reduce estimation risk compared to the traditional approach and several shrinkage approaches
proposed in the literature.
Kocuk, B. and Cornuejols, G. (2020\). “Incorporating Black\-Litterman views in portfolio construction when stock
returns are a mixture of normals .” In:Omega91 (102008\).
Abstract In this paper, we consider the basic problem of portfolio construction in financial engineering, and
analyze how market\-based and analytical approaches can be combined to obtain efficient portfolios. As a first
stepinouranalysis,wemodeltheassetreturnsasarandomvariabledistributedaccordingtoamixtureofnormal
80random variables. We then discuss how to construct portfolios that minimize the Conditional Value\-at\-Risk
(CVaR)underthisprobabilisticmodelviaaconvexprogram.Wealsoconstructasecond\-orderconerepresentable
approximation of the CVaR under the mixture model, and demonstrate its theoretical and empirical accuracy.
Furthermore, we incorporate the market equilibrium information into this procedure through the well\-known
Black\-Litterman approach via an inverse optimization framework by utilizing the proposed approximation.
Our computational experiments on a real dataset show that this approach with an emphasis on the market
equilibrium typically yields less risky portfolios than a purely market\-based portfolio while producing similar
returns on average.
Kolm, P. and Ritter, G. (2017\). “On the Bayesian interpretation of Black\-Litterman .” In:European Journal of
Operational Research 258(2\), pp. 564–572\.
The duality between Black\-Litterman optimization and regression is clarified. Generalized to allow views on any
parameter that appears in any asset return model. Our generalization is a special case of a Bayesian network or
graphical model. Allows for views on factor risk premia in Ross’ Arbitrage Pricing Theory (APT). We present
the most general model of the type considered by Black and Litterman (1991\) after fully clarifying the duality
between Black\-Litterman optimization and Bayesian regression. Our generalization is itself a special case of a
Bayesian network or graphical model. As an example, we work out in full detail the treatment of views on factor
risk premia in the context of APT. We also consider a more speculative example in which the portfolio manager
specifies a view on realized volatility by trading a variance swap.
Kolm, P. N. and Ritter, G. (2021\). “Factor Investing with Black\-Litterman\-Bayes: Incorporating Factor Views and
Priors in Portfolio Construction .” In:The Journal of Portfolio Management 47(2\), pp. 113–126\.
The authors propose a general framework referred to as Black\-Litterman\-Bayes (BLB) for constructing optimal
portfolios for factor\-based investing. In the spirit of the classical Black\-Litterman model, the framework allows
for the incorporation of investor views and priors on factor risk premiums, including data\-driven and benchmark
priors. Computationally efficient closed\-form formulas are provided for the (posterior) expected returns and
return covariance matrix that result from integrating factor views into an arbitrage pricing theory multifactor
model. In a step\-by\-step procedure, the authors show how to build the prior and incorporate the factor views,
demonstrating in a realistic empirical example and using a number of well\-known cross\-sectional US equity
factors, that the BLB approach can add value to mean\-variance\-optimal multifactor risk premium portfolios.
Kolm, P. N., Tutuncu, R., and Fabozzi, F. J. (2014\). “60 Years of portfolio optimization: Practical challenges and
current trends .” In:European Journal of Operational Research 234(2\), pp. 356–371\.
We review approaches for implementing Markowitz mean variance analysis in practice. Review covers inclusion
of transaction costs, constraints, sensitivity to inputs. We selectively highlight new trends and developments.
The concepts of portfolio optimization and diversification have been instrumental in the development and un\-
derstanding of financial markets and financial decision making. In light of the 60 year anniversary of Harry
Markowitz’s paper Portfolio Selection, we review some of the approaches developed to address the challenges
encountered when using portfolio optimization in practice, including the inclusion of transaction costs, portfolio
management constraints, and the sensitivity to the estimates of expected returns and covariances. In addition,
we selectively highlight some of the new trends and developments in the area such as diversification methods,
risk\-parity portfolios, the mixing of different sources of alpha, and practical multi\-period portfolio optimization.
Konstantinov, G., Chorus, A., and Rebmann, J. (2020\). “A network and machine learning approach to factor, asset,
and blended allocation .” In:The Journal of Portfolio Management 46 (6\), pp. 54–71\.
The main idea of this article is to approach and compare factor and asset allocation portfolios using both tradi\-
tional and alternative allocation techniques: inverse variance optimization, minimum\-variance optimization, and
centrality\-based techniques from network science. Analysis of the interconnectedness between assets and factors
shows that their relationship is strong. The authors compare the allocation techniques, considering centrality
and hierarchal\-based networks. They demonstrate the advantages of graph theory to explain the advantages to
portfolio management and the dynamic nature of assets and factors with their importance score. They find that
asset allocation can be efficiently derived using directed networks, dynamically driven by both US Treasuries
and currency returns with significant centrality scores. Alternatively, the inverse variance weight estimation and
correlation\-based networks generate factor allocation with favorable risk\-return parameters. Furthermore, factor
allocation is driven mostly by the importance scores of the Fama\-French\-Carhart factors: SMB, HML, CMA,
RMW, and MOM. The authors confirm previous results and argue that both factors and assets are intercon\-
nected with different value and momentum factors. Therefore, a blended strategy comprising factors and assets
can be defensible for investors. As argued in previous research, factors are much more overcrowded than assets.
81Therefore, the centrality scores help to identify the crowded exposure and build diversified allocation. The au\-
thors run LASSO regressions and show how the network\-based allocation can be implemented using machine
learning.
Kritzman, M. (2011\). “The graceful aging of mean variance optimization .” In:The Journal of Portfolio Management
37(2\), pp. 3–5\.
My take on the current relevance of mean\-variance optimization is that although it is nearly 60 years old, it is a
long way from retirement.The criticism of ”garbage in, garbage out” is no more an indictment of mean\-variance
optimization than it is of calculators, spreadsheets, and cooking recipes. The allegation that optimizers are
hypersensitive to small input errors is also vastly overstated. Small input errors do lead to large misallocations
across assets that are close substitutes for one another, but misallocations across close substitutes hardly reduce
efficiency. And small errors across dissimilar assets do not lead to significant misallocations. Mean\-variance
optimization does assume elliptical distributions or quadratic utility, but it fails only when both assumptions
are jointly and significantly violated, which seldom occurs.
Kritzman, M., Kinlaw, W., and Turkington, D. (2017\). A Practitioner’s Guide to Asset Allocation . Wiley. 256 pp.
A Practitioner’s Guide to Asset Allocation fills a void in the literature by offering a hands\-on resource that
describes the many important innovations that address key challenges to asset allocation and dispels common
fallacies about asset allocation. The authors cover the fundamentals of asset allocation, including a discussion of
the attributes that qualify a group of securities as an asset class and a detailed description of the conventional
application of mean\-variance analysis to asset allocation.. The authors review a number of common fallacies
about asset allocation and dispel these misconceptions with logic or hard evidence. The fallacies debunked
include such notions as: asset allocation determines more than 90% of investment performance; time diversifies
risk; optimization is hypersensitive to estimation error; factors provide greater diversification than assets and
are more effective at reducing noise; and that equally weighted portfolios perform more reliably out of sample
than optimized portfolios. A Practitioner’s Guide to Asset Allocation also explores the innovations that address
key challenges to asset allocation and presents an alternative optimization procedure to address the idea that
some investors have complex preferences and returns may not be elliptically distributed. Among the challenges
highlighted, the authors explain how to overcome inefficiencies that result from constraints by expanding the
optimization objective function to incorporate absolute and relative goals simultaneously. The text also explores
the challenge of currency risk, describes how to use shadow assets and liabilities to unify liquidity with expected
return and risk, and shows how to evaluate alternative asset mixes by assessing exposure to loss throughout
the investment horizon based on regime\-dependent risk. This practical text contains an illustrative example of
asset allocation which is used to demonstrate the impact of the innovations described throughout the book. In
addition, the book includes supplemental material that summarizes the key takeaways and includes information
on relevant statistical and theoretical concepts, as well as a comprehensive glossary of terms.
Kritzman, M., Page, S., and Turkington, D. (2012\). “Regime Shifts: Implications for Dynamic Strategies .” In:
Financial Analysts Journal 68(3\).
Regime shifts present significant challenges for investors because they cause performance to depart significantly
from the ranges implied by long\-term averages of means and covariances. But regime shifts also present op\-
portunities for gain. The authors show how to apply Markov\-switching models to forecast regimes in market
turbulence, inflation, and economic growth. They found that a dynamic process outperformed static asset allo\-
cation in backtests, especially for investors who seek to avoid large losses.
Kritzman, M. and Turkington, D. (2016\). “Stability\-Adjusted Portfolios .” In:The Journal of Portfolio Management
42(5\), pp. 113–122\.
The conventional approach for addressing estimation error in portfolio construction is to devise techniques for
reducing the errors, such as compressing all the estimates toward a cross\-sectional average or some other prior
belief. In this article, the authors propose an alternative approach for dealing with estimation error, arguing
that some estimates may be more or less stable than others. The authors propose that rather than attempting to
mitigate estimation error by making the estimates more similar to each other, portfolio managers should measure
their relative stability and form portfolios that explicitly account for this feature, thus potentially making them
less similar to each other. The authors focus on measures of risk rather than means, because portfolio managers
typically extrapolate historical covariances but estimate expected returns based on subjective views rather
than historical averages. Moreover, many important investment applications, such as index replication, focus
exclusively on risk mitigation. The authors show that portfolios that explicitly account for stability in their
82construction have substantially different allocations and more stable risk profiles than portfolios that are blind
to estimation error, as well as those that rely on Bayesian shrinkage.
Kritzman, M. P., Kinlaw, W., and Turkington, D. (2021\). Asset Allocation: From Theory to Practice and Beyond .
WILEY. 368 pp.
In Asset Allocation: From Theory to Practice and Beyond \- the newly and substantially revised Second Edition
of A Practitioner’s Guide to Asset Allocation \- accomplished finance professionals William Kinlaw, Mark P.
Kritzman, and David Turkington deliver a robust and insightful exploration of the core tenets of asset allocation.
Drawing on their experience working with hundreds of the world’s largest and most sophisticated investors, the
authors review foundational concepts, debunk fallacies, and address cutting\-edge themes like factor investing
and scenario analysis. The new edition also includes references to related topics at the end of each chapter and
a summary of key takeaways to help readers rapidly locate material of interest.
The book also incorporates discussions of:
1\)The characteristics that define an asset class, including stability, investability, and similarity
2\)The fundamentals of asset allocation, including definitions of expected return, portfolio risk, and diversifi\-
cation
3\)Advanced topics like factor investing, asymmetric diversification, fat tails, long\-term investing, and en\-
hanced scenario analysis as well as tools to address challenges such as liquidity, rebalancing, constraints,
and within\-horizon risk.
.
Kukreti, V., Pharasi, H. K., Gupta, P., and Kumar, S. (2020\). “A Perspective on Correlation\-Based Financial
Networks and Entropy Measures .” In:Frontiers in Physics 8\.
Inthismini\-review,wecriticallyexaminetherecentworkdoneoncorrelation\-basednetworksinfinancialsystems.
The structure of empirical correlation matrices constructed from the financial market data changes as the
individual stock prices fluctuate with time, showing interesting evolutionary patterns, especially during critical
events such as market crashes, bubbles, etc. We show that the study of correlation\-based networks and their
evolution with time is useful for extracting important information of the underlying market dynamics. Also,
we present our perspective on the use of recently\-developed entropy measures, such as structural entropy and
eigen\-entropy, for continuous monitoring of correlation\-based networks.
Kuntz, L.\-C. (2018\). “Portfolio Strategies with Classical and Alternative Benchmarks .” PhD thesis. Georg August
University of Gottingen.
This dissertation addresses different key elements in portfolio management. It intends to improve and analyze
influences on portfolio strategies and their performance. Likewise, it aims at the systematization and extension of
benchmark specifications as well as their effect on portfolio strategies. Each chapter focuses on a different aspect
of developing and implementing portfolio strategies. The dissertation seeks to contribute to the advancement of
portfolio strategies by making the performance generating process and influences on it more comprehensible and
transparent. In doing so, it attempts to strengthen the awareness of the impact of the exact design of portfolio
strategies and benchmarks on the resulting portfolio and its performance. The key findings of this dissertation
can be summarized as follows: The benchmark specification, especially in terms of the investible universe and the
inherent risk conception, has substantial influence on the explicit design and performance of portfolio strategies.
In general, the specification of the benchmark and design of portfolio strategies should be carefully considered
and the implementation should be well thought out. Alternative risk conceptions, such as regret risk, can be
applied to portfolio selection and lead to clearly different portfolio compositions. Moreover, timing strategies can
be improved by choosing a careful investment approach on the basis of distributional regressions. All empirical
work 3 of this thesis has in common that it pursues different ideas to set up portfolio strategies while explicitly
addressing the benchmark specification used for the implementation and evaluation of said strategies.
Lai, T. L., Xing, H., and Chen, Z. (2011\). “Mean variance portfolio optimization when means and covariances are
unknown .” In:The Annals of Applied Statistics 5(2A), pp. 798–823\.
Markowitz’s celebrated mean0variance portfolio optimization theory assumes that the means and covariances
of the underlying asset returns are known. In practice, they are unknown and have to be estimated from
historical data. Plugging the estimates into the efficient frontier that assumes known parameters has led to
portfolios that may perform poorly and have counter\-intuitive asset allocation weights; this has been referred to
as the Markowitz optimization enigma. After reviewing different approaches in the literature to address these
difficulties, we explain the root cause of the enigma and propose a new approach to resolve it. Not only is the
83new approach shown to provide substantial improvements over previous methods, but it also allows flexible
modeling to incorporate dynamic features and fundamental analysis of the training sample of historical data, as
illustrated in simulation and empirical studies.
Lam, C. (2020\). “High\-dimensional covariance matrix estimation .” In:WIREs Computational Statistics 12(22\),
e1485\+.
Covariance matrix estimation plays an important role in statistical analysis in many fields, including (but not
limited to) portfolio allocation and risk management in finance, graphical modeling, and clustering for genes
discovery in bioinformatics, Kalman filtering and factor analysis in economics. In this paper, we give a selective
review of covariance and precision matrix estimation when the matrix dimension can be diverging with, or even
larger than the sample size. Two broad categories of regularization methods are presented. The first category
exploitsanassumedstructureofthecovarianceorprecisionmatrixforconsistentestimation.Thesecondcategory
shrinks the eigenvalues of a sample covariance matrix, knowing from random matrix theory that such eigenvalues
are biased from the population counterparts when the matrix dimension grows at the same rate as the sample
size.
Lancewicki, T. and Aladjem, M. (2014\). “Multi\-Target Shrinkage Estimation for Covariance Matrices .” In:IEEE
Transactions on Signal Processing 62(24\), pp. 6380–6390\.
Covariance matrix estimation is problematic when the number of samples is relatively small compared with the
number of variables. One way to tackle this problem is through the use of shrinkage estimators that offer a com\-
promise between the sample covariance matrix and a well\-conditioned matrix (also known as the \-target\-) with
the aim of minimizing the mean\-squared error (MSE). The use of only one target limits the shrinkage estimators’
flexibility when minimizing the MSE. In this paper, we propose a multi\-target shrinkage estimator (MTSE) for
covariance matrices that exploits the Lediot\-Wolf (LW) method by utilizing several targets simultaneously. This
greatly increases the estimator’s flexibility and enables it to attain a lower MSE. We also offer a general target
that serves as a framework for designing a wide variety of targets. In consequence, instead of studying individual
targets, the general framework can be utilized. We then show that the framework encompasses several targets
that already exist in the literature. Numerical simulations demonstrate that the MTSE significantly reduces the
MSE and is highly effective in classification tasks.
Langlois, H. (2020a). “A New Benchmark for Dynamic Mean\-Variance Portfolio Allocations .” In:SSRN e\-Print .
We propose a new methodology to implement unconditionally optimal dynamic mean\-variance portfolios. We
model portfolio allocations using an auto\-regressive process in which the shock to the portfolio allocation is
the gradient of the investor’s realized certainty equivalent with respect to the allocation. Our methodology can
accommodate transaction costs, short\-selling and leverage constraints, and a large number of assets. In out\-of\-
sample tests using equity portfolios, long\-short factors, government bonds, and commodities, we find that its
risk\-adjusted performance, net of transaction costs, is on average more than double that of other benchmark
allocations.
Langlois, H. (2020b). “A New Benchmark for Dynamic Mean\-Variance Portfolio Allocations .” In:SSRN e\-Print .
We propose a new methodology to implement unconditionally optimal dynamic mean\-variance portfolios. We
model portfolio allocations using an auto\-regressive process in which the shock to the portfolio allocation is the
gradient of the investor’s realized certainty equivalent with respect to the allocation. Our methodology accounts
for transaction costs, short\-selling and leverage constraints, and a large number of assets. In out\-of\-sample tests
using equity portfolios, long\-short factors, government bonds, and commodities, we find that its risk\-adjusted
performance, net of transaction costs, is on average more than double that of other benchmark allocations.
Lassance, N. (2022\). “Reconciling mean\-variance portfolio theory with non\-Gaussian returns .” In:European Journal
of Operational Research 297(2\), pp. 729–740\.
Mean\-variance portfolio theory remains frequently used as an investment rationale because of its simplicity,
its closed\-form solution, and the availability of well\-performing robust estimators. At the same time, it is also
frequently rejected on the grounds that it ignores the higher moments of non\-Gaussian returns. However, higher\-
moment portfolios are associated with many different objective functions, are numerically more complex, and
exacerbate estimation risk. In this paper, we reconcile mean\-variance portfolio theory with non\-Gaussian returns
byidentifying,amongallportfoliosonthemean\-varianceefficientfrontier,theonethatoptimizesachosenhigher\-
moment criterion. Numerical simulations and an empirical analysis show, for three higher\-moment objective
functions and adjusting for transaction costs, that the proposed portfolio strikes a favorable tradeoff between
specification and estimation error. Specifically, in terms of out\-of\-sample Sharpe ratio and higher moments, it
84outperforms the global\-optimal portfolio, and also the global\-minimum\-variance portfolio except when using
monthly returns for which estimation error is more prominent.
Lassance, N. and Vrins, F. (2021\). “Portfolio selection with parsimonious higher comoments estimation .” In:Journal
of Banking \& Finance 126, p. 106115\.
Large investment universes are usually fatal to portfolio strategies optimizing higher moments because of com\-
putational and estimation issues resulting from the number of parameters involved. In this paper, we introduce
a parsimonious method to estimate higher moments that consists of projecting asset returns onto a small set
of maximally independent factors found via independent component analysis (ICA). In contrast to principal
component analysis (PCA), we show that ICA resolves the curse of dimensionality affecting the comoment ten\-
sors of asset returns. The method is easy to implement, computationally efficient, and makes portfolio strategies
optimizing higher moments appealing in large investment universes. Considering the value\-at\-risk as a risk mea\-
sure, an investment universe of up to 500 stocks and adjusting for transaction costs, we show that our ICA
approach leads to superior out\-of\-sample risk\-adjusted performance compared with PCA, equally weighted, and
minimum\-variance portfolios.
Laur, B. (2020\). “Portfolio Optimization \- Can Optimizing Portfolio Outperform Naive Diversification? ” In:SSRN
e\-Print.
In this study we examined the performances of mean\-variance and tangency portfolio investment strategies in
order to determine if optimal diversification has benefits over 1/N strategy.
Le, T. H. (2021\). “International portfolio allocation: The role of conditional higher moments .” In:International
Review of Economics \& Finance .
I explore the benefits of incorporating conditional higher moments in the international portfolio allocation.
The quantile\-based conditional higher moments are robust to outliers and exhibit considerable time\-variation
and heterogeneity across countries. My empirical evidence shows that emerging market returns have favourable
conditionalskewnessbutaremoreexposedtoextremereturnswithhigherkurtosis.Intheinternationalportfolio,
the investor tilts her portfolio towards countries with higher skewness and less kurtosis, consistent with her
moment preference in theory. An investor with moderate risk aversion would be willing to pay 210 basis points
per year to switch from a three\-moment portfolio to the portfolio that employs both conditional skewness and
kurtosis. The portfolio policy is robust to real\-time investing strategy and incorporating transaction costs, but
the optimised portfolios underperform the naive value\-weighted portfolio out\-of\-sample.
Ledoit, O. and Wolf, M. (2017\). “Nonlinear Shrinkage of the Covariance Matrix for Portfolio Selection: Markowitz
Meets Goldilocks .” In:The Review of Financial Studies 30(12\), pp. 4349–4388\.
Markowitz (1952\) portfolio selection requires an estimator of the covariance matrix of returns. To address
this problem, we promote a nonlinear shrinkage estimator that is more flexible than previous linear shrinkage
estimators and has just the right number of free parameters (i.e., the Goldilocks principle). This number is the
same as the number of assets. Our nonlinear shrinkage estimator is asymptotically optimal for portfolio selection
when the number of assets is of the same magnitude as the sample size. In backtests with historical stock return
data, it performs better than previous proposals and, in particular, it dominates linear shrinkage.
Ledoit, O. and Wolf, M. (2020a). “Analytical nonlinear shrinkage of large\-dimensional covariance matrices .” In:
Annals of Statistics 48(5\), pp. 3043–3065\.
This paper establishes the first analytical formula for nonlinear shrinkage estimation of large\-dimensional co\-
variance matrices. We achieve this by identifying and mathematically exploiting a deep connection between
nonlinear shrinkage and nonparametric estimation of the Hilbert transform of the sample spectral density. Pre\-
vious nonlinear shrinkage methods were of numerical nature: QuEST requires numerical inversion of a complex
equation from random matrix theory whereas NERCOME is based on a sample\-splitting scheme. The new an\-
alytical method is more elegant and also has more potential to accommodate future variations or extensions.
Immediate benefits are (i) that it is typically 1000 times faster with basically the same accuracy as QuEST and
(ii) that it accommodates covariance matrices of dimension up to 10,000 and more. The difficult case where the
matrix dimension exceeds the sample size is also covered.
Ledoit, O. and Wolf, M. (2020b). Shrinkage Estimation of Large Covariance Matrices: Keep it Simple, Statistician?
Tech. rep. University of Zurich.
Under rotation\-equivariant decision theory, sample covariance matrix eigenvalues can be optimally shrunk by re\-
combining sample eigenvectors with a (potentially nonlinear) function of the unobservable population covariance
matrix. The optimal shape of this function reflects the loss/risk that is to be minimized. We solve the problem
of optimal covariance matrix estimation under a variety of loss functions motivated by statistical precedent,
85probability theory, and differential geometry. A key ingredient of our nonlinear shrinkage methodology is a new
estimator of the angle between sample and population eigenvectors, without making strong assumptions on the
population eigenvalues. We also introduce a broad family of covariance matrix estimators that can handle all
regular functional transformations of the population covariance matrix under large\-dimensional asymptotics. In
addition, we compare via Monte Carlo simulations our methodology to two simpler ones from the literature,
linear shrinkage and shrinkage based on the spiked covariance model.
Ledoit, O. and Wolf, M. (2022\). “The Power of (Non\-)Linear Shrinking: A Review and Guide to Covariance Matrix
Estimation .” In:Journal of Financial Econometrics 20(1\), pp. 187–218\.
Many econometric and data\-science applications require a reliable estimate of the covariance matrix, such as
Markowitz portfolio selection. When the number of variables is of the same magnitude as the number of ob\-
servations, this constitutes a difficult estimation problem; the sample covariance matrix certainly will not do.
In this article, we review our work in this area, going back 15plus years. We have promoted various shrinkage
estimators, which can be classified into linear and nonlinear. Linear shrinkage is simpler to understand, to derive,
and to implement. But nonlinear shrinkage can deliver another level of performance improvement, especially if
overlaid with stylized facts such as time\-varying co\-volatility or factor models.
Lee, T.\-H. and Seregina, E. (2022\). “Optimal Portfolio Using Factor Graphical Lasso .” In:arXiv e\-Print .
Graphical models are a powerful tool to estimate a high\-dimensional inverse covariance (precision) matrix, which
has been applied for a portfolio allocation problem. The assumption made by these models is a sparsity of the
precision matrix. However, when stock returns are driven by common factors, such assumption does not hold.
We address this limitation and develop a framework, Factor Graphical Lasso (FGL), which integrates graphical
models with the factor structure in the context of portfolio allocation by decomposing a precision matrix into
low\-rank and sparse components. Our theoretical results and simulations show that FGL consistently estimates
the portfolio weights and risk exposure and also that FGL is robust to heavy\-tailed distributions which makes
our method suitable for financial applications. FGL\-based portfolios are shown to exhibit superior performance
over several prominent competitors including equal\-weighted and Index portfolios in the empirical application
for the S\&P500 constituents.
Lee, W. and Liu, P. (2021\). “Work Harder: Diligent Rebalancing and Investment Horizon .” In:The Journal of
Portfolio Management .
In an age of constant information flow, investors have to strike the right balance between incorporating incre\-
mental information into a portfolio and managing turnover before the end of the investment horizon. Using a
tractable yet realistic model of asset and signaldynamics, the authors provide analytical rigor to justify the opti\-
mality of the common practice of updating investment views and portfolio positions as new information arrives.
In analyzing different approaches to rebalancing, their results indicate that regularly updating the conditional
information set achieves a higher information ratio than either waiting to rebalance until after the investment
horizon is reached or using regular rebalancing based on a moving average of the past information set. The
authors provide guidance on turnover management in conjunction with the information horizon of the signal.
Lee, Y., Kim, M. J., Kim, J. H., Jang, J. R., and Chang Kim, W. (2020\). “Sparse and robust portfolio selection via
semi\-definite relaxation .” In:Journal of the Operational Research Society 71(5\), pp. 687–699\.
In investment management, especially for automated investment services, it is critical for portfolios to have
a manageable number of assets and robust performance. First, portfolios should not contain too many assets
in order to reduce the management fees, transaction costs, and taxes. Second, portfolios should be robust as
investment environments change rapidly. In this study, therefore, we propose two convex portfolio selection
models that provide portfolios that are sparse and robust. We first perform semi\-definite relaxation to develop a
sparse mean\-variance portfolio selection model, and further extend the model by using L2\-norm regularization
and worst\-case optimization to formulate two sparse and robust portfolio selection models. Empirical analyses
with historical stock returns demonstrate the effectiveness of the proposed models in forming sparse and robust
portfolios.
Lehalle, C.\-A. and Simon, G. (2021\). “Portfolio selection with active strategies: how long only constraints shape
convictions .” In:Journal of Asset Management 22, pp. 443–463\.
In the recent years, an intense effort has been dedicated to the research on equity factors. If the academic
literaturequestionstheirrewardingnature,thefinancialindustrycompetesforthebestportfolioimplementation,
either in long\-short or in long only vehicles. While both solutions try to exploit the same factors while controlling
risk, two kinds of managers co\-exist in the meantime: fundamental, discretionary stock\-pickers, and quantitative,
systematic managers. The contribution of this paper is twofold. The core message is that a quantitative long
86only portfolio, built with any factor as a future returns’ proxy and a risk control, ends up to be high conviction
portfolios: the long only constraint polarizes naturally the portfolio on a concentrated set of nonzero positions.
In this respect, actively managed, quantitative long only portfolios share some similarity with discretionary
stock pickers. Beyond this message, and backed by numerical experiments, we derive theoretical results and
closed\-form formulas to show in addition that: (i) selected stocks are those that realize a trade\-off between a
low beta and a high loading on the factor; (ii) the thresholds driving this selection are endogenous, leading to a
recursive procedure to select the stocks. In other words: the portfolio selection problem may be solved linearly
instead of using an optimizer. We highlight in particular the crucial role played by low beta stocks and by the
co\-linearity of the risk model with the factor used to forecast returns.
Lei, Y., Li, Y., and Xu, J. (2020\). “Two Birds, One Stone: Joint Timing of Returns and Capital Gains Taxes .” In:
Management Science 66(2\), pp. 823–843\.
In asset return predictability, realized returns and future expected returns tend to move in opposite directions.
This generates a tension between tax\- and market\-timing incentives. In this study, a portfolio choice problem in
the presence of both return predictability and capital gains tax is examined. We characterize various features
of the optimal trading strategy, and demonstrate that the optimal strategy helps mitigate the tension between
market\- and tax\-timing. The calibrated model suggests that return predictability can significantly increase both
the utility loss due to capital gains tax and the value of deferring capital gains realization. Overall, our results
suggest that the nature of the asset return process can have important implications for the welfare effects of
capital gains tax.
Leon, D., Aragon, A., Sandoval, J., Hernandez, G., Arevalo, A., and Nino, J. (2017\). “Clustering algorithms for
Risk\-Adjusted Portfolio Construction .” In:Procedia Computer Science 108, pp. 1334–1343\.
This paper presents the performance of seven portfolios created using clustering analysis techniques to sort
out assets into categories and then applying classical optimization inside every cluster to select best assets
inside each asset category. The proposed clustering algorithms are tested constructing portfolios and measuring
their performances over a two month dataset of 1\-minute asset returns from a sample of 175 assets of the
Russell 1000 index. A three\-week sliding window is used for model calibration, leaving an out of sample period
of five weeks for testing. Model calibration is done weekly. Three different rebalancing periods are tested:
every 1, 2 and 4 hours. The results show that all clustering algorithms produce more stable portfolios with
similar volatility. In this sense, the portfolios volatilities generated by the clustering algorithms are smaller
when compare to the portfolio obtained using classical Mean\-Variance Optimization (MVO) over all the dataset.
Hierarchicalclusteringalgorithmsachievethebestfinancialperformanceobtaininganadequatetrade\-offbetween
accumulated financial returns and the risk\-adjusted measure, Omega Ratio, during the out of sample testing
period.
Leyffer, S., Menickelly, M., Munson, T., Vanaret, C., and Wild, S. M. (2020\). “A survey of nonlinear robust
optimization .” In:INFOR: Information Systems and Operational Research 58(2\), pp. 342–373\.
Robust optimization (RO) has attracted much attention from the optimization community over the past decade.
RO is dedicated to solving optimization problems subject to uncertainty: design constraints must be satisfied
for all the values of the uncertain parameters within a given uncertainty set. Uncertainty sets may be modeled
as deterministic sets (boxes, polyhedra, ellipsoids), in which case the RO problem may be reformulated via
worst\-case analysis, or as families of distributions. The challenge of RO is to reformulate or approximate robust
constraints so that the uncertain optimization problem is transformed into a tractable deterministic optimization
problem. Most reformulation methods assume linearity of the robust constraints or uncertainty sets of favorable
shape, which represents only a fraction of real\-world applications. This survey addresses nonlinear RO and
includes problem formulations and applications, solution approaches, and available software with code samples.
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
87of being clearer and more in line with the experience of professionals in financial markets: skewness is due to
negative jumps in asset prices. After presenting the mathematical framework, we analyze an investment portfolio
that mixes risk premia, more specifically risk parity, momentum and carry strategies. We show that traditional
portfolio management based on the volatility risk measure is biased and corresponds to a short\-sighted approach
to bad times. We then propose to replace the volatility risk measure by a skewness risk measure, which is
calculated as an expected shortfall that incorporates a stress scenario. We conclude that constant\-mix portfolios
may be better adapted than actively managed portfolios, when the investment universe is composed of negatively
skewed financial assets.
Li,B.andRossi,A.G.(2021\). “SelectingMutualFundsfromtheStocksTheyHold:AMachineLearningApproach .”
In:SSRN e\-Print .
We select mutual funds in real time by combining individual fund holdings and a large number (94\) of stock
characteristics to compute fund\-level characteristics on the basis of the stocks they hold. We show that, first,
the majority of funds are largely exposed—both positively and negatively—to approximately 40\-50 character\-
istics. Second, fund performance is non\-linearly related to fund characteristics and there are significant degrees
of interaction between different fund characteristics and fund performance. Third, when we predict fund per\-
formance, these non\-linearities and interactions prove important as machine learning methods such as Boosted
Regression Trees (BRT) outperform significantly standard linear frameworks and the BRT\-generated forecasts
encompass the ones generated by the predictors of mutual fund performance that have been proposed in the
literature so far. Fourth, while in our setting BRT outperform the LASSO, elastic nets, random forests, and
neural networks with 1 through 5 hidden layers, these other machine learning methods deliver good performance
and they all outperform ordinary least squares models. Finally, while we detect significant predictability using
machine learning methods, it is short\-lived and time\-varying—both in terms of which fund characteristics matter
the most and in terms of the functional relation connecting fund characteristics and fund performance.
Li, F., Chow, T.\-M., Pickard, A., and Garg, Y. (2019\). “Transaction Costs of Factor\-Investing Strategies .” In:
Financial Analysts Journal 75, pp. 62–78\.
Althoughhidden,theimplicitmarketimpactcostsoffactorinvestingmaysubstantiallyerodeastrategyexpected
excess returns. The rebalancing data of a suite of large and long\-standing factor\-investing indexes are used in
this study to model these market impact costs. A framework to assess the costs of rebalancing activities is
introduced. These costs are then attributed to characteristics that intuitively describe the strategies demands
on liquidity, such as rate of turnover and the concentration of turnover. A number of popular factor\-investing
implementationsareidentified,andtheauthorsdiscusshowtheirindexconstructionmethods,whenthoughtfully
designed, can reduce market impact costs.
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
Li, X., Uysal, A. S., and Mulvey, J. M. (2022a). “Multi\-period portfolio optimization using model predictive control
with mean\-variance and risk parity frameworks .” In:European Journal of Operational Research 299(3\), pp. 1158–
1176\.
We employ model predictive control for a multi\-period portfolio optimization problem. In addition to the mean\-
variance objective, we construct a portfolio whose allocation is given by model predictive control with a risk\-
parity objective, and provide a successive convex program algorithm that provides 30 times faster and robust
solutions in the experiments. We provide a comprehensive comparison of the models in regard of planning
horizon, parameter estimation, as well as objective function choice. Computational results on a multi\-asset
universe show that multi\-period models perform better than their single period counterparts in out\-of\-sample
period, 2006\-2020, in the presence of market impact costs. The out\-of\-sample risk\-adjusted performance of
both mean\-variance and risk\-parity formulations beat the fix\-mix benchmarks, and achieve Sharpe ratio of 0\.64
88and 0\.97, respectively. We also include tests on different asset universes (Fama French industry portfolios) and
alternative parameter estimation methods (Bayes\-Stein and Black\-Litterman) with consistent findings.
Li, X. and Zakamulin, V. (2019\). “The term structure of volatility predictability .” In:SSRN e\-Print .
Volatility forecasting is crucial for portfolio management, risk management, and pricing of derivative securities.
Still, little is known about the accuracy of volatility forecasts and the horizon of volatility predictability. This
paper aims to fill these gaps in the literature. We begin this paper by introducing the notions of the spot and
forward predicted volatilities and propose to describe the term structure of volatility predictability by the spot
and forward forecast accuracy curves. Then we perform a comprehensive study on the term structure of volatility
predictability in the stock and foreign exchange markets. Our results quantify the volatility forecast accuracy
across horizons in the two major markets and suggest that the horizon of volatility predictability is significantly
longer than that reported in the earlier studies. Nevertheless, the horizon of volatility predictability is found to
be much shorter than the longest maturity of traded derivative contracts.
Li, X. and Zakamulin, V. (2020\). “Stock volatility predictability in bull and bear markets .” In:Quantitative Finance
20(7\), pp. 1149–1167\.
The recent literature on stock return predictability suggests that it varies substantially across economic states,
being strongest during bad economic times. In line with this evidence, we document that stock volatility pre\-
dictability is also state dependent. In particular, in this paper, we use a large data set of high\-frequency data
on individual stocks and a few popular time\-series volatility models to comprehensively examine how volatility
forecastability varies across bull and bear states of the stock market. We find that the volatility forecast horizon
is substantially longer when the market is in a bear state than when it is in a bull state. In addition, over all
but the shortest horizons, the volatility forecast accuracy is higher when the market is in a bear state. This
difference increases as the forecast horizon lengthens. Our study concludes that stock volatility predictability is
strongest during bad economic times, proxied by bear market states.
Li, Y., Simon, Z., and Turkington, D. (2022b). “Investable and Interpretable Machine Learning for Equities .” In:
The Journal of Financial Data Science 4(1\).
The authors propose three principles for evaluating the practical efficacy of machine learning for stock selection,
and they compare the performance of various models and investment goals using this framework. The first
principle is investability. To this end, the authors focus on portfolios formed from highly liquid US stocks,
and they calibrate models to require a reasonable amount of trading. The second principle is interpretability.
Investors must understand a model’s output well enough to trust it and extract some general insight from it.
To this end, the authors choose a concise set of predictor variables, and they apply a novel method called
the model fingerprint to reveal the linear, nonlinear, and interaction effects that drive a model’s predictions.
The third principle is that a model’s predictions should be interesting – they should convincingly outperform
simpler models. To this end, the authors evaluate out\-of\-sample performance compared to linear regressions.
In addition to these three principles, the authors also consider the important role people play by imparting
domain knowledge and preferences to a model. The authors argue that adjusting the prediction goal is one
of the most powerful ways to do this. They test random forest, boosted trees, and neural network models for
multiple calibrations that they conclude are investable, interpretable, and interesting.
Liberman, J., Sialm, C., Sosner, N., and Wang, L. (2020\). “The Tax Benefits of Separating Alpha from Beta .” In:
Financial Analysts Journal 76(1\), pp. 38–61\.
Using both simulated and historical data, we show that separating active returns (i.e., alpha) from market
exposure(i.e.,beta)mayhavesignificanttaxbenefits.Wefindthataninvestmentstrategythatinvestsseparately
in a passive index portfolio and an actively managed long\-short portfolio is more tax efficient than a long\-only
actively managed strategy with similar risk and style exposures. The turnover of a traditional active strategy
causes capital gain realizations in both the active and passive portfolio components. In contrast, the turnover
of a strategy that separates alpha from beta is concentrated in the long\-short component and enables the
deferral of capital gain realizations in the passive market component. Separating alpha from beta is different
from systematic tax management as described in the literature. Our approach provides a practical solution for
taxable investors in a world dominated by tax\-agnostic managers.
Lin, W.\-H., Teng, H.\-W., and Yang, C.\-C. (2020\). “A Heteroskedastic Black\-Litterman Portfolio Optimization
Model with Views Derived from a Predictive Regression .” In:Handbook of Financial Econometrics, Mathematics,
Statistics, and Machine Learning . World Scientific, pp. 563–581\.
The modern portfolio theory in Markowitz (1952\) is a cornerstone for investment management, but its imple\-
mentations are challenging in that the optimal portfolio weight is extremely sensitive to the estimation for the
89mean and covariance of the asset returns. As a sophisticate modification, the Black\-Litterman portfolio model
allows the optimal portfolio’s weight to rely on a combination of the implied market equilibrium returns and
investors’ views (Black and Litterman, 1991\). However, the performance of a Black\-Litterman model is closely
related to investors’ views and the estimated covariance matrix. To overcome these problems, we first propose a
predictive regression to form investors’ views, where asset returns are regressed against their lagged values and
the market return. Second, motivated by stylized features of volatility clustering, heavy\-tailed distribution, and
leverage effects, we estimate the covariance of asset returns via heteroscedastic models. Empirical analysis using
five industry indexes in the Taiwan stock market shows that the proposed portfolio outperforms existing ones
in terms of cumulative returns.
Lioui, A. (2021\). “Understanding Regularization for Portfolio Construction .” In:SSRN e\-Print .
Regularization for portfolio construction is shown to be equivalent to combining the unconstrained portfolio with
a long \- short portfolio. The latter is not correlated with the unconstrained portfolio which leads the constrained
portfolio to have a beta of one with respect to the unconstrained portfolio. Regularization aiming at controlling
for estimation risk makes thus investors tilt their original portfolio with noise. The noise portfolio is reminiscent
of factor investing or reverse factor investing. Thus the benefits of regularization strongly depend on the test
assets and the new decomposition provides forward guidance on why and when estimation risk management
through regularization may or may not work.
Liszewski, O. (2016\). “Asset allocation under multiple regimes .” MA thesis. Erasmus University.
In this paper we examine the performance of the Markov Switching model with intra\-regimes changes such as
the bull market correction and bear market rallies. We accommodate this short time rehearsals by imposing
restrictionsonthetransitionprobabilitymatrix.Wecomparethemodelwithclassicmean\-switchinganddynamic
VAR models in an asset allocation problem with different number of regimes, initial states choices and asset
distributions used in the estimation process. In an out\-of\-sample and bootstrap verification we give evidence
that the constrained model outperforms other models in terms of risk\-adjusted returns in the long horizon above
2 years.
Liu, D. (2019\). “Analytical solutions of optimal portfolio rebalancing .” In:Quantitative Finance 19(4\) (683\-697\),
pp. 1–15\.
We study optimal portfolio rebalancing in a mean\-variance type framework and present new analytical results
for the general case of multiple risky assets. We first derive the equation of the no\-trade region, and then
provide analytical solutions and conditions for the optimal portfolio under several simplifying yet important
models of asset covariance matrix: uncorrelated returns, same non\-zero pairwise correlation, and a one\-factor
model. In some cases, the analytical conditions involve one or two parameters whose values are determined by
combinatorial, rather than numerical, algorithms. Our results provide useful and interesting insights on portfolio
rebalancing, and sharpen our understanding of the optimal portfolio.
Liu, X. and Viswanathan, V. (2020\). “The term structure of the rebalancing premium .” In:The Journal of Investing
29(4\), pp. 116–125\.
The optimal rebalance interval that maximizes the expected geometric return of passive strategies decreases in
relation to increasing asset volatility, increasing dispersion in asset volatility, and increasing negative 1\-month
autocorrelation of asset returns. Conversely, the optimal rebalance interval increases in relation to increasing
positive 1\-month return autocorrelation and increasing dispersion in expected return of the underlying assets.
Much of the literature on the rebalancing premium has focused on the effect of asset volatility. But empirically,
the positive autocorrelation of asset returns and the dispersion in asset expected returns have a much larger
impact on the rebalancing premium. Depending on the set of assets chosen, the optimal rebalance frequency
can vary between 6 months for an equal\-weighted portfolio of multiple asset classes and 10 years for an equal\-
weighted portfolio of regional indices. The large variation in optimal rebalance frequency challenges the notion
of a universal rebalancing premium.
Lohre, H., Rother, C., and Schafer, K. A. (2020\). “Hierarchical Risk Parity: Accounting for Tail Dependencies
in Multi\-asset Multi\-factor Allocations .” In:Machine Learning for Asset Management: New Developments and
Financial Applications . Ed. by E. Jurczenko. Wiley, pp. 329–368\.
This chapter examines the use and merits of hierarchical clustering techniques in the context of multi\-asset
multi\-factor investing. In particular, it contrasts these techniques with several competing risk\-based allocation
paradigms, such as 1/N, minimum\-variance, standard risk parity and diversified risk parity. The chapter intro\-
duces hierarchical risk parity (HRP) strategies based on the Pearson correlation coefficient and also introduces
hierarchical clustering based on the lower tail dependence coefficient. The chapter provides an overview of tradi\-
90tional risk\-based allocation strategies and outlines a framework to measure and manage portfolio diversification.
It examines the performance of the introduced HRP strategies relative to the traditional alternatives. The chap\-
ter discusses Meucci’s approach to managing diversification, which serves to construct a diversified risk parity
strategy based on economic factors.
Lopez de Prado, M. (2016\). “Building Diversified Portfolios that Outperform Out of Sample .” In:The Journal of
Portfolio Management 42(4\), pp. 59–69\.
In this article, the author introduces the Hierarchical Risk Parity (HRP) approach to address three major con\-
cerns of quadratic optimizers, in general, and Markowitz’s critical line algorithm (CLA), in particular: instability,
concentration, and underperformance. HRP applies modern mathematics (graph theory and machine\-learning
techniques) to build a diversified portfolio based on the information contained in the covariance matrix. How\-
ever, unlike quadratic optimizers, HRP does not require the invertibility of the covariance matrix. In fact,
HRP can compute a portfolio on an ill\-degenerated or even a singular covariance matrix an impossible feat for
quadratic optimizers. Monte Carlo experiments show that HRP delivers lower out\-ofsample variance than CLA,
even though minimum variance is CLA’s optimization objective. HRP also produces less risky portfolios out of
sample compared to traditional risk parity methods.
Lopez de Prado, M. (2019\). “A Data Science Solution to the Multiple\-Testing Crisis in Financial Research .” In:The
Journal of Financial Data Science 1(1\), pp. 99–110\.
Mostdiscoveriesinempiricalfinancearefalse,asaconsequenceofselectionbiasundermultipletesting.Although
many researchers are aware of this problem, the solutions proposed in the literature tend to be complex and hard
toimplement.Inthisarticle,theauthorreducestheproblemofselectionbiasinthecontextofinvestmentstrategy
development to two sub\-problems: determining the number of essentially independent trials and determining
the variance across those trials. The author explains what data researchers need to report to allow others to
evaluate the effect that multiple testing has had on reported performance. He applies his method to a real case
of strategy development and estimates the probability that a discovered strategy is false.
Lopez de Prado, M. (2020a). “A robust estimator of the efficient frontier .” In:SSRN e\-Print .
Convex optimization solutions tend to be unstable, to the point of entirely offsetting the benefits of optimization.
For example, in the context of financial applications, it is known that portfolios optimized in\-sample often
underperform the naive (equal weights) allocation out\-of\-sample. This instability can be traced back to two
sources: (i) noise in the input variables; and (ii) signal structure that magnifies the estimation errors in the
input variables. A first innovation of this paper is to introduce the nested clustered optimization algorithm
(NCO), a method that tackles both sources of instability.Over the past 60 years, various approaches have been
developed to address these two sources of instability. These approaches are flawed in the sense that different
methods may be appropriate for different input variables, and it is unrealistic to expect that one method will
dominate all the rest under all circumstances. Accordingly, a second innovation of this paper is to introduce
MCOS, a Monte Carlo approach that estimates the allocation error produced by various optimization methods
on a particular set of input variables. The result is a precise determination of what method is most robust to
a particular case. Thus, rather than relying always on one particular approach, MCOS allows users to apply
opportunistically whatever optimization method is best suited in a particular setting.Presentation materials are
available at: https://ssrn.com/abstract\=3469964\.
Lopez de Prado, M. (2020b). Machine learning for asset managers . Cambridge University Press. 190 pp.
Successful investment strategies are specific implementations of general theories. An investment strategy that
lacks a theoretical justification is likely to be false. Hence, an asset manager should concentrate her efforts
on developing a theory rather than on backtesting potential trading rules. The purpose of this Element is to
introduce machine learning (ML) tools that can help asset managers discover economic and financial theories.
ML is not a black box, and it does not necessarily overfit. ML tools complement rather than replace the classical
statistical methods. Some of ML’s strengths include (1\) a focus on out\-of\-sample predictability over variance
adjudication; (2\) the use of computational methods to avoid relying on (potentially unrealistic) assumptions;
(3\) the ability to learn complex specifications, including nonlinear, hierarchical, and noncontinuous interaction
effects in a high\-dimensional space; and (4\) the ability to disentangle the variable search from the specification
search, robust to multicollinearity and other substitution effects.
Lopez de Prado, M. and Lewis, M. J. (2019\). “Detection of false investment strategies using unsupervised learning
methods.” In:Quantitative Finance 19(9\), pp. 1555–1565\.
In this paper we address the problem of selection bias under multiple testing in the context of investment strate\-
gies. We introduce an unsupervised learning algorithm that determines the number of effectively uncorrelated
91trials carried out in the context of a discovery. This estimate is critical for computing the familywise false positive
probability, and for filtering out false investment strategies.
Low,R.K.Y.,Faff,R.,andAas,K.(2016\). “Enhancingmean\-varianceportfolioselectionbymodelingdistributional
asymmetries .” In:Journal of Economics and Business 85, pp. 49–72\.
Model\-based estimates that incorporate return asymmetries are applied to 18 meanvariance optimization rules.
Model\-based estimates are a significant improvement over use of historical\-based estimates. Model\-based esti\-
mates result in out\-performance of the basic mean\-variance optimization strategy after transaction costs. Out\-
performing the 1/N portfolio after transaction costs remains an elusive task even with model\-based estimates.
Why do mean\-variance (MV) models perform so poorly? In searching for an answer to this question, we estimate
expected returns by sampling from a multivariate probability model that explicitly incorporates distributional
asymmetries. Specifically, our empirical analysis shows that an application of copulas using marginal models
that incorporate dynamic features such as autoregression, volatility clustering, and skewness to reduce estima\-
tion error in comparison to historical sampling windows. Using these copula\-based models, we find that several
MV\-based rules exhibit statistically significant and superior performance improvements even after accounting
for transaction costs. However, we find that outperforming the na ive equally\-weighted (1/N) strategy after
accounting for transactions costs still remains an elusive task.
Lucas, S. and Sanz, A. (2016\). “Pick Your Battles: The Intersection of Investment Strategy, Tax, and Compounding
Returns.” In:The Journal of Wealth Management 19(2\), pp. 9–16\.
In the hunt for investment value added, taxable investors need to think differently. A low\-cost, low\-turnover,
equity\-oriented strategy with broad, consistent exposure to the market is the most likely to succeed over long
periods. The power of this simple approach lies in the interaction of investment strategy, tax management, and
long\-term compounding. After taking into consideration taxes, the cost of being wrong, and loss\-harvesting
capabilities, active strategies must generate 160 to 380 basis points of value added per year just to break even
with this approach. If you want to fight the active management battle, do so in the knowledge that the odds are
stacked against you.
Ma, F., Lu, X., Yang, K., and Zhang, Y. (2019\). “Volatility forecasting: long memory, regime switching and het\-
eroscedasticity .” In:Applied Economics 51(38\), pp. 4151–4163\.
In this article, we account for the first time for long memory, regime switching and the conditional time\-
varyingvolatilityofvolatility(heteroscedasticity)tomodelandforecastmarketvolatilityusingtheheterogeneous
autoregressive model of realized volatility (HAR\-RV) and its extensions. We present several interesting and
notable findings. First, existing models exhibit significant nonlinearity and clustering, which provide empirical
evidence on the benefit of introducing regime switching and heteroscedasticity. Second, out\-of\-sample results
indicate that combining regime switching and heteroscedasticity can substantially improve predictive power
from a statistical viewpoint. More specifically, our proposed models generally exhibit higher forecasting accuracy.
Third,theseresultsarewidelyconsistentacrossavarietyofrobustnesstestssuchasdifferentforecastingwindows,
forecastingmodels,realizedmeasures,andstockmarkets.Consequently,thisstudyshedsnewlightonforecasting.
Maeso,J.\-M.andMartellini,L.(2020\). “Measuringportfoliorebalancingbenefitsinequitymarkets .”In:The Journal
of Portfolio Management 46(4\), pp. 94–109\.
The potential source of additional performance because of the simple act of resetting portfolio weights back
to the original weights is referred as the rebalancing premium. It is also sometimes known as the volatility
pumping effect or diversification bonus because volatility and diversification turn out to be key components
of the rebalancing premium. The purpose of this article is to provide a thorough empirical analysis of the
volatility pumping effect in equity markets and to examine the conditions under which it can be maximized.
The authors main contribution to the understanding of the rebalancing premium is an effort to disentangle
and separately measure the isolated impact of various components of the total effect. Using the Fama\-French\-
Carhart four\-factor model, they find that, after controlling for factor exposures, the average outperformance
of the rebalanced strategy with respect to the corresponding buy\-and\-hold strategy remains substantial at an
annualized level above 100 basis points over a 5\-year time horizon for stocks in the S\&P 500 universe. They also
find that size, value, momentum, and volatility are sorting characteristics that have a significant out\-of\-sample
impact on the rebalancing premium. In particular, the selection of small\-cap, low book\-to\-market, past loser, and
high\-volatility stocks generates a higher out\-of\-sample rebalancing premium compared to random portfolios for
time horizons from 1 year to 5 years. They also show that the initial weighting scheme has a significant impact
on the size of the rebalancing premium. Taken together, these results suggest that a substantial rebalancing
92premium can potentially be harvested in equity markets over reasonably long horizons for suitably selected
types of stocks.
Maharaj, E. A., D’Urso, P., and Caiado, J. (2019\). Time Series Clustering and Classification . CRC Press. 244 pp.
TimeSeriesClusteringandClassificationincludesrelevantdevelopmentsonobservation\-based,feature\-basedand
model\-based traditional and fuzzy clustering methods, feature\-based and model\-based classification methods,
and machine learning methods. It presents a broad and self\-contained overview of techniques for both researchers
and students.
Malavasi, M., Lozza, S. O., and Truck, S. (2021\). “Second order of stochastic dominance efficiency vs mean variance
efficiency .” In:European Journal of Operational Research 290(3\), pp. 1192–1206\.
In this paper, we compare two of the main paradigms of portfolio theory: mean variance analysis and expected
utility. In particular, we show empirically that mean variance efficient portfolios are typically sub\-optimal for
non satiable and risk averse investors. We illustrate that the second order stochastic dominance (SSD) efficient
set is the solution of a multi\-objective optimization problem. We further show that the market portfolio is not
necessarily a solution to this optimization problem. We also conduct an empirical analysis, examining the ex
ante and ex post performance of SSD and mean variance efficient portfolios, using a bootstrap approach. In an
ex ante analysis, we compare empirical moments, the level of diversification and set distances of mean variance
and SSD efficient sets. We also show that the global minimum variance (GMV) portfolio and the part of the
mean variance efficient frontier (MVEF) composed of highly diversified portfolios is second order stochastically
dominated. This result also provides a possible alternative explanation for the diversification puzzle. Conducting
an ex post analysis, we construct second order stochastic dominating strategies that outperform the GMV
portfolio in terms of wealth and various other performance measures, producing a positive ex post opportunity
cost.
Mandigers, T. (2020\). “Portfolio Performance With High\-Dimensional Inverse Covariance Matrix .” MA thesis. Eras\-
mus University.
High\-dimensional inverse covariance estimation is a big problem for portfolio managers that want to create
portfolios with a high number of assets. Recent research in this area delivered multiple shrinkage techniques
that enable for the estimation of these high\-dimensional inverse covariance matrices. We analyze the outof\-
sample performance of portfolios constructed by high\-dimensional inverse covariance matrices, created with a
shrinkage technique, and we also evaluate the robustness of the shrinkage technique. Out of the 5 shrinkage
technique analyzed the POET, Ledoit and Wolf and Graphical Lasso shrinkage technique prove to be good
performers against the equally weighted portfolio. However, only the Ledoit and Wolf, and the Graphical Lasso
are a reasonable choice for real world use. They are the only two, out of the investigated techniques, that give
comparable inverse covariance estimates for similarly distributed data sets. The performance of all techniques
are investigated in combination with different mean\-variance portfolios. Generally, the Graphical Lasso is the
highest risk adjusted performer and the most robust in creating the inverse covariance matrix.
Marakbi, Z. (2017\). “Mean\-Variance Portfolio Optimization: Challenging the role of traditional covariance estima\-
tion.” MA thesis. KTH Royal institute of technology.
Eversinceitsintroductionin1952,theMean\-Variance(MV)portfolioselectiontheoryhasremainedacenterpiece
within the realm of efficient asset allocation. However, in scientific circles, the theory has stirred controversy. A
strand of criticism has emerged that points to the phenomenon that Mean\-Variance Optimization suffers from
the severe drawback of estimation errors contained in the expected return vector and the covariance matrix,
resulting in portfolios that may significantly deviate from the true optimal portfolio. While a substantial amount
of effort has been devoted to estimating the expected return vector in this context, much less is written about the
covariancematrixinput.Inrecenttimes,however,researchthatpointstotheimportanceofthecovariancematrix
in MV optimization has emerged. As a result, there has been a growing interest whether MV optimization can
be enhanced by improving the estimate of the covariance matrix. Hence, this thesis was set forth by the purpose
to investigate whether nancial practitioners and institutions can allocate portfolios consisting of assets in a more
efficient manner by changing the covariance matrix input in mean\-variance optimization. In the quest of chieving
this purpose, an out\-of\-sample analysis of MV optimized portfolios was performed, where the performance of ve
prominent covariance matrix estimators were compared, holding all other things equal in the MV optimization.
The optimization was performed under realistic investment constraints, taking incurred transaction costs into
account, and for an investment asset universe ranging from equity to bonds. The empirical findings in this
study suggest one dominant estimator: the covariance matrix estimator implied by the Gerber Statistic (GS).
Specifically, by using this covariance matrix estimator in lieu of the traditional sample covariance matrix, the
93MV optimization rendered more efficient portfolios in terms of higher Sharpe ratios, higher risk\-adjusted returns
and lower maximum drawdowns. The outperformance was protruding during recessionary times. This suggests
that an investor that employs traditional MVO in quantitative asset allocation can improve their asset picking
abilities by changing to the, in theory, more robust GS covariance matrix estimator in times of volatile financial
markets.
Marandi, A., Ben\-Tal, A., Hertog, D. d., and Melenberg, B. (2019\). “Extending the Scope of Robust Quadratic
Optimization .” In:arXiv e\-Print .
We derive computationally tractable formulations of the robust counterparts of convex quadratic and conic
quadratic constraints that are concave in matrix\-valued uncertain parameters. We do this for a broad range of
uncertainty sets. In particular, we show how to reformulate the support functions of uncertainty sets represented
in terms of matrix norms and cones. Our results provide extensions to known results from the literature. We
also consider hard quadratic constraints; those that are convex in uncertain matrix\-valued parameters. For the
robust counterpart of such constraints we derive inner and outer tractable approximations. As application, we
show how to construct a natural uncertainty set based on a statistical confidence set around a sample mean
vector and covariance matrix and use this to provide a tractable reformulation of the robust counterpart of an
uncertain portfolio optimization problem. We also apply the results of this paper to a norm approximation and
a regression line problem.
Markovic, I. P., Stankovic, J. Z., Stojanovic, M. B., and Stankovic, J. M. (2019\). “A Hybrid Model for Financial
Portfolio Optimization Based on LS\-SVM and a Clustering Algorithm .” In:ICT innovations 2019\. big data
processing and mining: 11th international conference . Ed. by S. Gievska and G. Madjarov. Vol. 1110\. Springer
International Publishing, pp. 173–186\.
An investment decision is one of the most important financial decisions. With the aim of optimizing investment
in securities from the aspect of return and risk, investors usually diversify their portfolio securities. This paper
presents a hybrid model for portfolio optimization, which consist of two steps. The first step predicts future
returns on the shares, and the second step, by applying hierarchical clustering algorithm, identifies various
groups of shares. The test results indicate that the suggested model is suitable for optimization of a financial
portfolio as a hybrid model based on selected shares, which if included in the portfolio, enable the diversification
of risk.
Markowitz, H. M. (2010\). “Portfolio Theory: As I Still See It .” In:Annual Review of Financial Economics 2(1\),
pp. 1–23\.
This essay summarizes my views on (a) the foundations of portfolio theory and its applications to current issues,
such as the choice of criteria for practical risk\-return analysis, and whether some form of risk\-return analysis
should be used in fact; (b) hypotheses about actual financial behavior, as opposed to idealized rational behavior,
including two proofs of the fact that expected\-utility maximizers would never prefer a multiple\-prize lottery to
all single\-prize lotteries, as asserted in one of my 1952 papers; and (c) a simple proof of the theorem (which was
initially greeted with some skepticism, especially by referees) that investors in capital asset pricing models do
not get paid for bearing risk.
Martellini, L., Milhau, V., and Tarelli, A. (2015\). “Toward Conditional Risk Parity: Improving Risk Budgeting
Techniques in Changing Economic Environments .” In:The Journal of Alternative Investments 18(1\), pp. 48–64\.
Risk parity portfolios are traditionally constructed by choosing historical volatility as the risk measure. In an
asset allocation context, this results in a substantial overweighting of bonds versus more volatile asset classes
such as stocks: this is a concern in a low bond yield environment, since the presence of mean reversion in the yield
implies that bonds are likely to perform poorly in the next future. In this article, we introduce three distinct
risk parity strategies, explicitly designed to respond to changes in interest rate levels. Our results indicate that
these strategies deliver higher returns when interest rates start to increase back to their long\-term levels, and
that the maximum Sharpe ratio portfolio, which also incorporates information on expected returns, is a less
robust alternative.
Marti, G., Andler, S., Nielsen, F., and Donnat, P. (2016\). “Clustering Financial Time Series: How Long is Enough? ”
In:arXiv e\-Print .
Researchers have used from 30 days to several years of daily returns as source data for clustering financial
time series based on their correlations. This paper sets up a statistical framework to study the validity of such
practices. We first show that clustering correlated random variables from their observed values is statistically
consistent. Then, we also give a first empirical answer to the much debated question: How long should the time
series be? If too short, the clusters found can be spurious; if too long, dynamics can be smoothed out.
94Marti, G., Nielsen, F., Bihkowski, M., and Donnat, P. (2020\). “A review of two decades of correlations, hierarchies,
networks and clustering in financial markets .” In:arXiv e\-Print .
This document is a preliminary version of an in\-depth review on the state of the art of clustering financial
time series and the study of correlation networks. This preliminary document is intended for researchers in this
field so that they can feedback to allow amendments, corrections and addition of new material unknown to the
authors of this review. The aim of the document is to gather in one place the relevant material that can help the
researcher in the field to have a bigger picture, the quantitative researcher to play with this alternative modeling
of the financial time series, and the decision maker to leverage the insights obtained from these methods. We
hope that this document will form a basis for implementation of an open toolbox of standard tools to study
correlations, hierarchies, networks and clustering in financial markets. We also plan to maintain pointers to
online material and an updated version of this work at www.datagrapple.com/Tech.
Marti, G., Nielsen, F., Donnat, P., and Andler, S. (2017\). “On Clustering Financial Time Series: A Need for
Distances Between Dependent Random Variables .” In:Computational Information Geometry . Ed. by F. Nielsen,
F. Critchley, and C. T. J. Dodson. Signals and Communication Technology. Springer International Publishing,
pp. 149–174\.
This artilce summarizes our work on the clustering of financial time series. It was written for a workshop
on information geometry and its application for image and signal processing. This workshop brought several
experts in pure and applied mathematics together with applied researchers from medical imaging, radar signal
processingandfinance.Theauthorsbelongtothelattergroup.Thisdocumentwaswrittenasalongintroduction
to further development of geometric tools in financial applications such as risk or portfolio analysis. Indeed, risk
and portfolio analysis essentially rely on covariance matrices. Besides that the Gaussian assumption is known to
be inaccurate, covariance matrices are difficult to estimate from empirical data. To filter noise from the empirical
estimate, Mantegna proposed using hierarchical clustering. In this work, we first show that this procedure is
statistically consistent. Then, we propose to use clustering with a much broader application than the filtering
of empirical covariance matrices from the estimated correlation coefficients. To be able to do that, we need
to obtain distances between the financial time series that incorporate all the available information in these
cross\-dependent random processes.
Martin, K. J. and Sankaran, H. (2019\). “Using the Black\-Litterman Model: A View on Opinions .” In:The Journal
of Investing 28(1\), pp. 112–122\.
We provide evidence on using the Black\-Litterman (1991, 1992\) asset allocation model and show that if investors
form even partially correct opinions on small\-cap and emerging market stocks, portfolio performance would have
improved vis\-a\-vis no opinions. For the period 2006\-2011, we show that the Black\-Litterman expected returns
for large\-cap US stocks, the EAFE index, and the Bloomberg Barclays US aggregate bond index are highly
correlated with future five\-year returns in each of those assets. Expected returns on US small\-cap and emerging
market stocks have a low correlation with future returns. If an opinion was only partially correct on the latter
assets, the resulting portfolios would have outperformed a market\-cap\-weighted benchmark portfolio. Thus, we
conclude that investors may benefit more from investing resources in forming opinions on the future direction
of small\-cap and emerging market stocks relative to large\-cap stocks.
Martin, R. D., Clark, A., and Green, C. G. (2010\). “Robust portfolio construction .” In:Handbook of Portfolio
Construction: Contemporary Applications of Markowitz Techniques . Springer.
Outliers in asset returns factors are a frequently occurring phenomenon across all asset classes and can have an
adverse influence on the performance of mean\-variance optimized (MVO) portfolios. This occurs by virtue of the
unbounded influence that outliers can have on the mean returns and covariance matrix estimates (alternatively,
correlations and variances estimates) that are inputs are optimizer inputs. A possible solution to the problem of
such outlier sensitivity of MVO is to use robust estimates of mean returns and covariance matrices in place of
the classical estimates of these quantities thereby providing robust MVO portfolios. We show that the differences
occurring between classical and robust estimates for these portfolios are such as to be of considerable concern to
a portfolio manager. It turns out that robust distances based on a robust covariance matrix can provide reliable
identification of multidimensional outliers in both portfolio returns and the exposures matrix of a fundamental
factor model, something that is not possible with one\-dimensional Winsorization. Multidimensional visualization
combined with clustering methods is also useful for returns outlier identification. The question of using robust
and classical MVO vs. optimization\-based fat\-tailed skewed distribution fits and downside risk measure is briefly
discussed. Some other applications of robust methods in portfolio management are described, and we point out
some future research that is needed on the topic.
95Martin, R. (2021\). “PyPortfolioOpt: portfolio optimization in Python .” In:Journal of Open Source Software 6(61\),
p. 3066\.
Portfolio construction is a critically important aspect of investment management. Even after an investor selects
a set of assets or return streams to invest in, it is a nontrivial task to decide how much should be allocated
to each. The expected return of the asset is certainly an important factor, but the investor may also wish to
consider the investment risks and the co\-dependence of asset returns. Modern Portfolio Theory, introduced by
Markowitz (1952\), presents a mathematical framework for maximizing a portfolio’s expected returns subject
to a risk constraint (measuring risk with the covariance matrix of asset returns). While optimization problems
are difficult in general, many portfolio optimization tasks can be framed as convex optimization problems,
inviting the use of a large body of theory and several efficient solving routines (Boyd \& Vandenberghe, 2004\).
PyPortfolioOpt is a python package that implements financial portfolio optimization tech\- niques, including
classical mean\-variance optimization (MVO) methods, Black\-Litterman allo\- cation (Black \& Litterman, 1991\),
and modern methods such as the machine learning\-inspired Hierarchical Risk Parity algorithm (Lopez de Prado,
2016\). PyPortfolioOpt is currently being used by several financial services companies; it has been downloaded
over 160,000 times, cited in academic publications (Jansen, 2020; Snow, 2020\), and used in numerous online
courses and tutorials (Putkov, 2019; Werger, 2021\).
McNamee, J. L., Paradise, T., and Bruno, M. A. (2019\). Getting back on track: A guide to smart rebalancing .
Tech. rep. Vanguard.
A portfolio’s asset allocation reflects an investor’s goals and temperament – the need for return and ability to
withstand the financial markets’ inevitable turbulence. Over time, as the returns of higher\- and lower\-risk assets
diverge, a portfolio can take on exposures that are inconsistent with the investor’s risk and return objectives.
Rebalancing from one asset class to another can put the portfolio back on track. We review the benefits of
rebalancing, analyze the impact of different rebalancing frequencies and thresholds, and highlight strategies
to minimize rebalancing costs. Our analysis suggests three best practices when setting expectations for and
executing a rebalancing strategy: 1\) rebalance to manage risk and emotion 2\) set a rebalancing trigger 3\)
minimize the transaction and tax costs of rebalancing.
Messica, A. (2018\). “Loopholes in Modern Portfolio Theory .” In:SSRN e\-Print .
This paper points out to loopholes in Modern Portfolio Theory (MPT) and fundamental flaws that question
its validity and applicability not only for investment but for education as well. Using theoretical analysis,
Monte Carlo simulations and market data I present and discuss theoretical, as well as conceptual, loopholes in
the formulation of MPT and its complementing Capital Asset Pricing Model and Tobin’s separation theorems.
Issueswithestimationofportfolio’smeanreturnandvariance,Mean\-Varianceoptimization,failureofthemutual
fund and two\-fund theorems, portfolio size, and capital allocation are analyzed and discussed among others.
Misperception of volatility as representative of portfolio’s risk is confronted against the actual portfolio risk that
was not addressed in MPT’s formulation. These loopholes are inherent to MPT even when assuming that all
of its assumptions are valid and that real\-life aspects such as non\-stationarity and heteroskedasticity could be
ignored.
Meucci, A. (2014\). “Robust Bayesian allocation .” In:The Journal of Investment Strategies 1(2\), pp. 119–131\.
Using the Bayesian posterior distribution of the market parameters we define self\-adjusting uncertainty regions
for the robust mean\-variance problem. Under a normal\-inverse\-Wishart conjugate assumption for the market,
the ensuing robust Bayesian mean\-variance optimal portfolios are shrunk by the aversion to estimation risk
toward the global minimum variance portfolio. After discussing the theory, we test robust Bayesian allocations
in a simulation study and in an application to the management of sectors of the SandP 500\.
Meucci, A. (2009\). “Enhancing the Black Litterman and related approaches: Views and stress\-test on risk factors .”
In:Journal of Asset Management 10(2\), pp. 89–96\.
The Black Litterman and related approaches modify the return distribution of a normally distributed market
according to views or stress\-test scenarios. We discuss how to broaden the range of applications of these ap\-
proaches significantly by letting them act on the risk factors underlying the market, instead of the returns of
the securities.
Meucci, A., Ardia, D., and Keel, S. (2020\). “Portfolio Construction and Systematic Trading with Factor Entropy
Pooling.” In:SSRN e\-Print .
The Entropy Pooling approach is a versatile theoretical framework to process market views and generalized
stress\-testsintoanoptimal”posterior”marketdistribution,whichisthenusedforriskmanagementandportfolio
management. Entropy Pooling can be implemented non\-parametrically or parametrically. The non\-parametric
96implementation with historical scenarios is more suitable for risk management applications. Here introduce
the parametric implementation of Entropy Pooling under a factor structure, which we name Factor Entropy
Pooling. The factor structure reduces the dimension of the problem and linearizes the parameter space, allowing
for fast computation of the posterior market distribution. We apply Factor Entropy Pooling to two portfolio
construction problems. First, we use the Factor Entropy Pooling to construct the ”implied returns”, i.e. a market
distributionconsistentwithatargetoptimalportfolio,suchasmaximumdiversification/riskparity,ortheCAPM
equilibrium. Our approach improves on the implied returns a\-la\-Black\-Litterman, and the ensuing distribution
can be used as the starting point for further portfolio construction. Second, we use Factor Entropy Pooling to
construct and backtest quantitative systematic trading strategies based on ranking views, or ”portfolios from
sorts”. Unlike standard approaches, Factor Entropy Pooling closely ties to the actual empirical data.
Meucci, A., Santangelo, A., and Deguest, R. (2015\). “Risk budgeting and diversification based on optimised uncor\-
related factors .” In:Risk.
We measure the contributions to risk of a set of factors, strategies, or investments, based on ”Minimum\-Torsion
Bets”, namely a set of uncorrelated factors, optimized to closely track the factors used to allocate the portfolio.
We then introduce a novel definition of contributions to risk, which generalizes the ”marginal contributions to
risk”, traditionally used in banks for risk budgeting and in asset management to build risk parity strategies.
The Minimum\-Torsion Bets allow us to also introduce a natural diversification score, the Effective Number
of Minimum\-Torsion Bets, which we use to measure and manage diversification. We discuss the advantages of
the Minimum\-Torsion Bets over the traditional approach to diversification based on marginal contributions to
risk. We present two case studies, a security\-based investment in the stocks of the S\&P 500, and a factor\-based
investment in the five Fama\-French factors.
Meyer\-Bullerdiek, F. (2021\). “Out\-of\-sample performance of the Black\-Litterman model .” In:Journal of Finance
and Investment Analysis 10(2\), pp. 29–51\.
In this paper, we consider the historical real returns of fixed and dynamic allocation portfolios consisting of
equities and short term bonds over thirty year time horizons, where fixed real contributions are made to the
portfoliosannually.Inparticular,weconsiderboththescenariowheretheinvestorannuallyrebalancesaportfolio
to a fixed ratio as well as the scenario where the investor’s annual contribution has a fixed ratio but the portfolio
is never subsequently rebalanced. These results provide investors in the accumulation phase historical data that
may provide a useful guide to asset allocation decisions. Of particular interest is that, over the 88 thirty\-year
time intervals considered, dynamic allocation portfolios had a better overall performance than fixed allocation
portfolios,andthatbothfixedanddynamicallocationportfoliosstronglybenefitedfromaheavyequityexposure.
Michaud, R. O. (2019\). “Comment on: Kritzman, M. 2006, ’are optimizers error maximizers?’ ” In:SSRN e\-Print .
Kritzman (2006\) asserts that the widely cited Michaud (1989\) study characterizing the impact of estimation
error on Markowitz (1952\) mean\-variance (MV) optimization as maximization is hype. His paper consists of
two examples of MV portfolio optimizations: an eight\-country index asset allocation with near identical returns
and four\-indices with very different estimates. In spite of the absence of standard references in estimation error,
authors continue to cite the paper. In this brief note we demonstrate that even in these stylized and unrealistic
examples, Kritzman MV optimized portfolios perform on average worse than equal weighting out\-of\-sample. A
MV optimization worse than equal weighting has little practical investment value or interest. The impact of
optimizer error maximization properly measured appears alive and very well.
Michaud, R. O., Esch, D., and Michaud, R. (2020a). “Comment: Allen, D., C. Lizieri, S. Satchell 2019\. ’In Defense
of Portfolio Optimization: What If We Can Forecast?’ ” In:SSRN e\-Print .
Allen et al (ALS) (2019\) claim that a CAPM based theoretical framework for Markowitz (1952\) mean\-variance
(MV) efficiency and a small level of forecast information (IC) can beat equal weighted portfolios. A portfolio
optimization procedure worse than equal weighting would have little practical investment value or interest. They
challenge the 1/N empirical results in DeMiguel et al (DGU) (2009\) and, implicitly, the ”error maximization”
characterization of MV optimization in Michaud (1989\). However, their conclusions are inconsistent with canon\-
ical Monte Carlo simulation studies of estimation error in MV optimization. This is because their theoretical
CAPM\-like framework ignores the bulk of estimation error \- model error and covariance matrix estimation \-
by assumption. Our extension of classic Monte Carlo studies indicates that many times the level of forecast
information assumed in ALS is likely required to outperform equal weight in theoretical budget\-constrained MV
optimized portfolios in practice.
Michaud, R. O., Esch, D. N., and Michaud, R. O. (2020b). “Estimation error and the fundamental law of active
management: is quant fundamentally flawed? ” In:The Journal of Investing 29(4\), pp. 20–30\.
97According to widely referenced applications of the Grinold (1989\) Fundamental Law theory, simply adding
securities to an optimization universe, adding factors to a forecast return model, trading more frequently, or
reducing constraints can add investment value to an optimized investment strategy. We show with intuitive
discussion followed by Monte Carlo simulation that many applications of Grinold theory for optimized portfolio
design are often unreliable and self\-defeating. Critical limitations of the theory are due to ignoring estimation
error (Michaud 1989\) and constraints required in practical applications. A substantial fraction of professional
actively managed funds may be negatively impacted.
Michaud, R. O. and Michaud, R. (2015\). “Estimation Error and Portfolio Optimization: A Resampling Solution .”
In:SSRN e\-Print .
Markowitz(1959\)mean\-variance(MV)portfoliooptimizationhasbeenthepracticalstandardforassetallocation
and equity portfolio management for almost fifty years. However, it is known to be overly sensitive to estimation
errorinrisk\-returnestimatesandhavepoorout\-of\-sampleperformancecharacteristics.TheResampledEfficiency
(RE) techniques presented in Michaud (1998\) introduce Monte Carlo methods to properly represent investment
informationuncertaintyincomputingMVportfoliooptimalityandindefiningtradingandmonitoringrules.This
paper reviews and updates the literature on estimation error and RE portfolio optimization and rebalancing.
We resolve several open issues and misunderstandings that have emerged since Michaud (1998\). In particular,
we show RE optimization to be a Bayesian\-based generalization and enhancement of Markowitz’s solution.
Mikalsen, K. O., Bianchi, F. M., Soguero\-Ruiz, C., and Jenssen, R. (2018\). “Time Series Cluster Kernel for Learning
Similarities between Multivariate Time Series with Missing Data .” In:Pattern Recognition 76, pp. 569–581\.
Similarity\-based approaches represent a promising direction for time series analysis. However, many such meth\-
ods rely on parameter tuning, and some have shortcomings if the time series are multivariate (MTS), due to
dependencies between attributes, or the time series contain missing data. In this paper, we address these chal\-
lenges within the powerful context of kernel methods by proposing the robust time series cluster kernel (TCK).
The approach taken leverages the missing data handling properties of Gaussian mixture models (GMM) aug\-
mented with informative prior distributions. An ensemble learning approach is exploited to ensure robustness to
parameters by combining the clustering results of many GMM to form the final kernel. We evaluate the TCK on
synthetic and real data and compare to other state\-of\-the\-art techniques. The experimental results demonstrate
that the TCK is robust to parameter choices, provides competitive results for MTS without missing data and
outstanding results for missing data.
Mitra, A., Das, A., Goswami, S., Mustafi, J., and Jalan, A. K. (2019\). “Portfolio management by time series
clustering using correlation for stocks .” In:Computational intelligence, communications, and business analytics:
second international conference, CICBA 2018 . Ed. by J. K. Mandal, S. Mukhopadhyay, P. Dutta, and K.
Dasgupta. Vol. 1031\. Singapore: Springer Singapore, pp. 134–144\.
Investment diversification and portfolio building has been a great interest for share market investors, so as to
minimize risk and maximize profit in a sensitive stock market. This paper gives an inside view of application of
clustering for grouping 79 stocks (NSE), which can be used to build a diversified portfolio. Manually trying out
different groupings to diversify portfolio is a computationally expensive task. In this paper, the closing price,
time series of the stocks have been considered. Common effect due to market has been discounted using partial
correlation, and a correlation based dissimilarity measure has been used for clustering. An equal investment
strategy has been adopted to compare the portfolio performance with SENSEX. The empirical results of the
portfolios have been studied and presented in details.
Mladina, P. (2020\). “Refining After\-Tax Return and Risk Parameters .” In:The Journal of Wealth Management
23(2\), pp. 8–17\.
Taxes introduce certain complexities, requiring proper adjustments to return and risk parameters. The author
offers a refined set of after\-tax return and risk equations for use in practice and validates them with a stochas\-
tic future value cash flow model. The refined after\-tax return and risk parameters can be used in portfolio
optimization, Monte Carlo simulation, and deterministic present/future value portfolio modeling with inter\-
nally consistent results. The refinements improve the discovery of the optimal after\-tax portfolio and enhance
long\-term wealth planning in the presence of risk.
Moehle, N., Kochenderfer, M. J., Boyd, S., and Ang, A. (2021\). “Tax\-Aware Portfolio Construction via Convex
Optimization .” In:arXiv e\-Print .
We describe an optimization\-based tax\-aware portfolio construction method that adds tax liability to standard
Markowitz\-based portfolio construction. Our method produces a trade list that specifies the number of shares
to buy of each asset and the number of shares to sell from each tax lot held. To avoid wash sales (in which
98some realized capital losses are disallowed), we assume that we trade monthly, and cannot simultaneously buy
and sell the same asset. The tax\-aware portfolio construction problem is not convex, but it becomes convex
when we specify, for each asset, whether we buy or sell it. It can be solved using standard mixed\-integer convex
optimization methods at the cost of very long solve times for some problem instances. We present a custom
convex relaxation of the problem that borrows curvature from the risk model. This relaxation can provide a
good approximation of the true tax liability, while greatly enhancing computational tractability. This method
requires the solution of only two convex optimization problems: the first determines whether we buy or sell each
asset, and the second generates the final trade list. In our numerical experiments, our method almost always
solves the nonconvex problem to optimality, and when it does not, it produces a trade list very close to optimal.
Backtests show that the performance of our method is indistinguishable from that obtained using a globally
optimal solution, but with significantly reduced computational effort.
Molstad, A. J. and Rothman, A. J. (2018\). “Shrinking characteristics of precision matrix estimators .” In:Biometrika
105(3\), pp. 563–574\.
We propose a framework to shrink a user\-specified characteristic of a precision matrix estimator that is needed
to fit a predictive model. Estimators in our framework minimize the Gaussian negative loglikelihood plus an
L1L1L1penaltyonalinearoraffinefunctionevaluatedattheoptimizationvariablecorrespondingtotheprecision
matrix. We establish convergence rate bounds for these estimators and propose an alternating direction method
of multipliers algorithm for their computation. Our simulation studies show that our estimators can perform
better than competitors when they are used to fit predictive models. In particular, we illustrate cases where our
precisionmatrixestimatorsperformworseatestimatingthepopulationprecisionmatrixbutbetteratprediction.
Molyboga, M. (2020\). “A Modified Hierarchical Risk Parity Framework for Portfolio Management .” In:The Journal
of Financial Data Science 2(3\), pp. 128–139\.
This article introduces a modified hierarchical risk parity (MHRP) approach that extends the HRP approach
by incorporating three intuitive elements commonly used by practitioners. The new approach (1\) replaces the
sample covariance matrix with an exponentially weighted covariance matrix with Ledoit\-Wolf shrinkage; (2\)
improves diversification across portfolio constituents both within and across clusters by relying on an equal
volatility, rather than an inverse variance, allocation approach; and (3\) improves diversification across time by
applying volatility targeting to portfolios. The author examines the impact of the enhancements on portfolios
of commodity trading advisors within a large\-scale Monte Carlo simulation framework that accounts for the
realistic constraints of institutional investors. The author finds a striking improvement in the out\-of\-sample
Sharpe ratio of 50%, on average, along with a reduction in downside risk.
Mooney, T., Rapaka, R., and Vera, T. (2020\). “Dynamic Regime Strategy for Stress Testing and Optimizing
Institutional Investor Portfolios .” In:SSRN e\-Print .
Our work aims to develop a stand\-alone trading system to construct portfolios that show the benefits of value
and momentum style integration and presents the effectiveness of alternative integration methods for long\-only
absolute return funds, which seeks absolute returns that are not highly correlated to traditional assets such
as stocks and bonds. Our approach uses the CRoss Industry Standard Process for Data Mining (CRISP\-DM)
model to guide the necessary steps, processes, and workflows for executing our project.
Moura, G. V., Santos, A. A. P., and Ruiz, E. (2020\). “Comparing high\-dimensional conditional covariance matrices:
Implications for portfolio selection .” In:Journal of Banking \& Finance 118, p. 105882\.
Portfolio selection based on high\-dimensional covariance matrices is a key challenge in data\-rich environments
with the curse of dimensionality severely affecting most of the available covariance models. We challenge several
multivariate Dynamic Conditional Correlation (DCC)\-type and Stochastic Volatility (SV)\-type models to obtain
minimum\-variance and mean\-variance portfolios with up to 1000 assets. We conclude that, in a realistic context
in which transaction costs are taken into account, although DCC\-type models lead to portfolios with lower
variance, modeling the covariance matrices as latent Wishart processes with a shrinkage towards the diagonal
covariance matrix delivers more stable optimal portfolios with lower turnover and higher information ratios. Our
results reconcile previous findings in the portfolio selection literature as those claiming for equicorrelations, a
smooth dynamic evolution of correlations or correlations close to zero.
Munro,B.andBradfield,D.(2016\). “Puttingthesqueezeonthesamplecovariancematrixforportfolioconstruction .”
In:Investment Analysts Journal 45(1\), pp. 47–62\.
ABSTRACTPortfolio construction plays a critical role in adding performance to a fund. Central to portfolio
construction are the two primary inputs: the vector of forecast returns and the covariance matrix. Our focus is
on the covariance matrix. With guidance from the literature we consider the suitability of two simple estimators,
99four shrinkage estimators and three blended estimators for mean\-variance portfolio construction in the South
African environment. Our assessment frameworks comprise a risk\-centric framework based on minimum variance
portfolios (MVPs) as well as a return\-centric framework. Our findings based on a South African equity setting
reveal that there are notable differences between the compositions of the MVPs of the covariance estimators.
Furthermore, we find that alternative covariance estimators do yield better out\-of\-period performance in terms of
lower realised risks than the sample covariance matrix. In our return\-based assessment framework, we considered
scenarios of perfect skill and less\-than\-perfect skill at forecasting returns. In the former case, we found that all of
the estimators produced optimal portfolios that substantially outperformed the optimal portfolio derived from
the sample covariance matrix. Considering the MVP framework, as well as the return\-based framework, we
conclude that all of the estimators considered performed better than the sample covariance matrix, effectively
reducing the sampling error in the sample covariance without introducing too much specification error. However,
no one estimator could be singled out as consistently superior in the South African setting over a range of test
metrics considered.
Nanakorn, N. and Palmgren, E. (2021\). “Hierarchical Clustering in Risk\-Based Portfolio Construction .” MA thesis.
KTH.
Following the global financial crisis, both risk\-based and heuristic portfolio construction methods have received
much attention from both academics and practitioners since these methods do not rely on the estimation
of expected returns and as such are assumed to be more stable than Markowitz’s traditional mean\-variance
portfolio. In 2016, Lopez de Prado presented the Hierarchical Risk Parity (HRP), a new approach to portfolio
construction which combines hierarchical clustering of assets with a heuristic risk\-based allocation strategy in
order to increase stability and improve out\-of\-sample performance. Using Monte Carlo simulations, Lopez de
Prado was able to demonstrate promising results.
This thesis attempts to evaluate HRP using walk\-forward analysis and historical data from equity index and
bond futures, against more realistic benchmark methods and using additional performance measures relevant to
practitioners. The main conclusion is that applying hierarchical clustering to risk\-based portfolio construction
doesindeedimprovetheout\-of\-samplereturnandSharperatio.However,theresultingportfolioisalsoassociated
with a remarkably high turnover, which may indicate numerical instability and sensitivity to estimation errors.
It is also identified that Lopez de Prado’s original HRP approach has an undesirable property and alternative
approaches to HRP have consequently been developed. Compared to Lopez de Prado’s original HRP approach,
these alternative approaches increase the Sharpe ratio with 10% and reduce the turnover with 60\-65%. However,
it should be noted that compared to more mainstream portfolios the turnover is still rather high, indicating that
these alternative approaches to HRP are still somewhat unstable and sensitive to estimation errors.
Ng, K. K., Agarwal, P., Mullen, N., Du, D., and Pollak, I. (2011\). “Comparison of several covariance matrix estima\-
tors for portfolio optimization .” In:IEEE International Conference on Acoustics, Speech and Signal Processing
(ICASSP) . IEEE, pp. 5752–5755\.
Modern portfolio theory dates back to a seminal 1952 paper by H. Markowitz and has been very influential
both in academic finance and among practitioners in the financial industry. Given a set of assets, the theory
can be used to compute the amount to be invested in each asset in order to construct an optimally diversified
portfolio. One of the parameters required in this calculation is the covariance matrix of asset returns which, in
any practical application, is unknown and must be estimated from historical data. Due to the fact that financial
data is often nonstationary, basing the estimates on historical data over a very long time period may not be
advisable. This renders the problem of covariance estimation difficult, especially for large portfolios. A large
body of literature exists proposing different covariance estimators. We focus on one frequently cited paper by
Ledoit and Wolf \[5] which proposes a covariance estimation method and purports to show that this method
leads to statistically significant improvements over several other methods. We show that this is not the case: in
fact, their method does not exhibit statistically significant differences from three other methods.
Nguyen, D. B. B., Prokopczuk, M., and Sibbertsen, P. (2020\). “The memory of stock return volatility: Asset pricing
implications .” In:Journal of Financial Markets 47, p. 100487\.
We examine long memory volatility in the cross\-section of stock returns. We show that long memory volatility
is widespread in the United States and that the degree of memory can be related to firm characteristics, such
as market capitalization, book\-to\-market ratio, prior performance, and price jumps. Long memory volatility is
negatively priced in the cross\-section. Buying stocks with shorter memory and selling stocks with longer memory
in volatility generates significant excess returns of 1\.71% per annum. Consistent with theory, we find that the
100volatility of stocks with longer memory is more predictable than stocks with shorter memory. This makes the
latter more uncertain, which is compensated for with higher average returns.
Nystrup, P., Hansen, B. W., Larsen, H. O., Madsen, H., and Lindstrom, E. (2018a). “Dynamic Allocation or
Diversification: A Regime\-Based Approach to Multiple Assets .” In:The Journal of Portfolio Management 44(2\),
pp. 62–73\.
This article investigates whether regime\-based asset allocation can effectively respond to changes in financial
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
O’Toole, R. (2013\). “The Black Litterman model: A risk budgeting perspective .” In:Journal of Asset Management
14(1\), pp. 2–13\.
The Black Litterman model of expected returns is well\-known throughout the investment management industry.
Despite the model’s familiarity, elucidating exactly what it does in a straightforward manner has proved to be
a challenge, as evidenced by a number of publications aimed at intuiting, explaining or demystifying the model.
Part of the lack of clarity is likely due to the fact that the model is derived with an emphasis on Bayesian
statistics, and as a result, key concepts and equations are expressed in terms that may obfuscate the practical
workings of the model for many prospective users. This article shows that Black Litterman expected returns can
also be derived in the context of a widely used mean\-variance optimization approach to active investing known as
risk budgeting. The risk budgeting derivation clearly illustrates the mean\-variance mechanics of the model, and
offers a simple framework for understanding how Black Litterman expected returns generate portfolio weights
that accurately reflect underlying investment views when used in unconstrained optimization. Viewing Black
Litterman from a risk budgeting perspective helps clarify the practicalities of the model in a way that may be
more familiar and insightful to a wider audience, and should be helpful in promoting Black Litterman as a useful
tool for investment managers.
Oberoi, S., Girach, M. B., and Chakrabarty, S. P. (2019\). “Can robust optimization offer improved portfolio per\-
formance? An empirical study of Indian market .” In:arXiv e\-Print .
101The emergence of robust optimization has been driven primarily by the necessity to address the demerits of the
Markowitz model. There has been a noteworthy debate regarding consideration of robust approaches as superior
or at par with the Markowitz model, in terms of portfolio performance. In order to address this skepticism, we
perform empirical analysis of three robust optimization models, namely the ones based on box, ellipsoidal and
separable uncertainty sets. We conclude that robust approaches can be considered as a viable alternative to the
Markowitz model, not only in simulated data but also in a real market setup, involving the Indian indices of S\&P
BSE 30 and S\&P BSE 100\. Finally, we offer qualitative and quantitative justification regarding the practical
usefulness of robust optimization approaches from the point of view of number of stocks, sample size and types
of data.
Oliveira, A. B. and Valls Pereira, P. L. (2018\). “Asset Allocation With Markovian Regime Switching: Efficient
Frontier and Tangent Portfolio With Regime Switching .” In:SSRN e\-Print .
Asset allocation is important for diversifying risk and realizing gains in the financial market. It involves decisions
taken under uncertainty based on statistical methods. Returns on financial assets generally present regime
switching and there are different distributions of returns in bull and bear markets. Regime switching in the data
generatingprocessforreturnsmakesitnecessarytoreformulatetheassetallocationproblem.Thispaperdevelops
asset allocation models with regime switching. Due to the comparative study of asset allocation, portfolios with
regime switching enable the space of risk and return to be increased, reduce the risk for each level of return at
the mean variance efficient frontier, and have the best risk\-return relationship over time.
Olmo, J. (2021\). “Optimal portfolio allocation and asset centrality revisited .” In:Quantitative Finance 21(9\),
pp. 1475–1490\.
This paper revisits the relationship between eigenvector asset centrality and optimal asset allocation in a mini\-
mum variance portfolio. We show that the standard definition of eigenvector centrality is misleading when the
adjacency matrix in a network can take negative values. This is, for example, the case when the network topology
is induced by the correlation matrix between assets in a portfolio. To correct for this, we introduce the concept
of positive and negative eigenvector centrality. Our results show that the loss function associated to the mini\-
mum variance portfolio is positively/negatively related to the positive and negative eigenvector centrality under
short\-selling constraints but cannot be generalized beyond that. Furthermore, in contrast to what is claimed
in the related literature, this relationship does not imply any monotonic relationship between the centrality of
an asset and its optimal portfolio allocation. These theoretical insights are illustrated empirically in a portfolio
allocation exercise with assets from U.S. and U.K. financial markets.
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
Packham, N. and Woebbeking, F. (2021\). “Correlation scenarios and correlation stress testing .” In:SSRN e\-Print .
We develop a general approach for stress testing correlations of financial asset portfolios. The correlation matrix
of asset returns is specified in a parametric form, where correlations are represented as a function of risk factors,
102such as country and industry factors. A sparse factor structure linking assets and risk factors is built using
Bayesian variable selection methods. Regular calibration yields a joint distribution of economically meaningful
stress scenarios of the factors. As such, the method also lends itself as a reverse stress testing framework: using
the Mahalanobis distance or highest density regions (HDR) on the joint risk factor distribution allows to infer
worst\-case correlation scenarios. We give examples of stress tests on a large portfolio of European and North
American stocks.
Page, S. and Panariello, R. A. (2018\). “When Diversification Fails .” In:Financial Analysts Journal 74(3\), pp. 19–32\.
One of the most vexing problems in investment management is that diversification seems to disappear when
investors need it the most. We surmise that many investors still do not fully appreciate the impact of extreme
correlations on portfolio efficiency particular, on exposure to loss. We take an in\-depth look at what drives the
stock\-to\-credit, stock\-to\-hedge fund, stock\-to\-private asset, stock\-to\-risk factors, and stock\-to\-bond correlations
during tail events. We introduce a data\-augmentation technique to improve the robustness of tail correlation
estimates. Finally, we discuss implications for multi\-asset investing.
Pagnoncelli, B. K., del Canto, F., and Cifuentes, A. (2021\). “The effect of regularization in portfolio selection
problems .” In:TOP.
Portfolio selection problems have been thoroughly studied under the risk and return paradigm introduced by
Markowitz. However, the usefulness of this approach has been hindered by some practical considerations that
have resulted in poorly diversified portfolios, or, solutions that are extremely sensitive to parameter estimation
errors.Inthiswork,weusesamplingmethodstocopewiththisissueandcomparethemeritsoftwoapproaches:a
sample average approximation approach and a performance\-based regularization (PBR) method that appeared
recently in the literature. We extend PBR by incorporating three different risk metrics – integrated chance\-
constraints, quantile deviation, and absolute semi\-deviation – and deriving the corresponding regularization
formulas. Additionally, a numerical comparison using index\-based portfolios is presented using historic data
that includes the subprime crisis.
Pandolfo, G., Iorio, C., Siciliano, R., and D’Ambrosio, A. (2020\). “Robust mean\-variance portfolio through the
weighted Lp depth function .” In:Annals of Operations Research 292(1\), pp. 519–531\.
Portfolios constructed by the classical mean\-variance model are very sensitive to outliers. We propose the use
of a non\-parametric estimation method based on statistical data depth functions. Specifically, we exploit the
notion of the weighted Lp depth function to obtain robust estimates of the mean and covariance matrix of the
asset returns. This approach has the advantage to be independent of parametric assumptions, and less sensitive
to changes in the asset return distribution than traditional techniques. The proposed procedure is evaluated and
compared with standard and other robust techniques through simulated and real data. Results indicate effective
improvements of the proposed method in terms of out\-of\-sample performance.
Pantaleo, E., Tumminello, M., Lillo, F., and Mantegna, R. N. (2011\). “When do improved covariance matrix
estimators enhance portfolio optimization? An empirical comparative study of nine estimators .” In:Quantitative
Finance 11(7\), pp. 1067–1080\.
The use of improved covariance matrix estimators as an alternative to the sample estimator is considered an
important approach for enhancing portfolio optimization. Here we empirically compare the performance of nine
improved covariance estimation procedures using daily returns of 90 highly capitalized US stocks for the period
1997?2007\. We find that the usefulness of covariance matrix estimators strongly depends on the ratio between
the estimation period T and the number of stocks N, on the presence or absence of short selling, and on the
performance metric considered. When short selling is allowed, several estimation methods achieve a realized risk
that is significantly smaller than that obtained with the sample covariance method. This is particularly true
when T/N is close to one. Moreover, many estimators reduce the fraction of negative portfolio weights, while
little improvement is achieved in the degree of diversification. On the contrary, when short selling is not allowed
and T?\>?N, the considered methods are unable to outperform the sample covariance in terms of realized risk,
but can give much more diversified portfolios than that obtained with the sample covariance. When T?N, the
use of the sample covariance matrix and of the pseudo\-inverse gives portfolios with very poor performance.
Paolella,M.(2017\). “TheUnivariateCollapsingMethodforPortfolioOptimization .”In:Econometrics 5(2\),pp.18\+.
The univariate collapsing method (UCM) for portfolio optimization is based on obtaining the predictive mean
and a risk measure such as variance or expected shortfall of the univariate pseudo\-return series generated from
a given set of portfolio weights and multivariate set of assets under interest and, via simulation or optimization,
repeating this process until the desired portfolio weight vector is obtained. The UCM is well\-known conceptually,
straightforward to implement, and possesses several advantages over use of multivariate models, but, among
103other things, has been criticized for being too slow. As such, it does not play prominently in asset allocation and
receives little attention in the academic literature. This paper proposes use of fast model estimation methods
combined with new heuristics for sampling, based on easily\-determined characteristics of the data, to accelerate
and optimize the simulation search. An extensive empirical analysis confirms the viability of the method.
Paolella, M. S. and Polak, P. (2018\). “COBra: Copula\-Based Portfolio Optimization .” In:Predictive Econometrics
and Big Data . Ed. by V. Kreinovich, S. Sriboonchitta, and N. Chakpitak. Vol. 753\. Studies in Computational
Intelligence. Springer International Publishing, pp. 36–77\.
The meta\-elliptical t copula with noncentral t GARCH univariate margins is studied as a model for asset al\-
location. A method of parameter estimation is deployed that is nearly instantaneous for large dimensions. The
expected shortfall of the portfolio distribution is obtained by combining simulation with a parametric approx\-
imation for speed enhancement. A simulation\-based method for mean\-expected shortfall portfolio optimization
is developed. An extensive out\-of\-sample backtest exercise is conducted and comparisons made with common
asset allocation techniques.
Paparrizos, J. and Gravano, L. (2017\). “Fast and Accurate Time\-Series Clustering .” In:ACM Transactions on
Database Systems 42(2\).
The proliferation and ubiquity of temporal data across many disciplines has generated substantial interest
in the analysis and mining of time series. Clustering is one of the most popular data\-mining methods, not
only due to its exploratory power but also because it is often a preprocessing step or subroutine for other
techniques. In this article, we present k\-Shape and k\-MultiShapes (k\-MS), two novel algorithms for time\-series
clustering. k\-Shape and k\-MS rely on a scalable iterative refinement procedure. As their distance measure, k\-
Shape and k\-MS use shape\-based distance (SBD), a normalized version of the cross\-correlation measure, to
consider the shapes of time series while comparing them. Based on the properties of SBD, we develop two
new methods, namely ShapeExtraction (SE) and MultiShapesExtraction (MSE), to compute cluster centroids
that are used in every iteration to update the assignment of time series to clusters. k\-Shape relies on SE to
compute a single centroid per cluster based on all time series in each cluster. In contrast, k\-MS relies on MSE
to compute multiple centroids per cluster to account for the proximity and spatial distribution of time series in
each cluster. To demonstrate the robustness of SBD, k\-Shape, and k\-MS, we perform an extensive experimental
evaluation on 85 datasets against state\-of\-the\-art distance measures and clustering methods for time series using
rigorous statistical analysis. SBD, our efficient and parameter\-free distance measure, achieves similar accuracy
to Dynamic Time Warping (DTW), a highly accurate but computationally expensive distance measure that
requires parameter tuning. For clustering, we compare k\-Shape and k\-MS against scalable and non\-scalable
partitional, hierarchical, spectral, density\-based, and shapelet\-based methods, with combinations of the most
competitive distance measures. k\-Shape outperforms all scalable methods in terms of accuracy. Furthermore,
k\-Shape also outperforms all non\-scalable approaches, with one exception, namely k\-medoids with DTW, which
achieves similar accuracy. However, unlike k\-Shape, this approach requires tuning of its distance measure and is
significantly slower than k\-Shape. k\-MS performs similarly to k\-Shape in comparison to rival methods, but k\-MS
is significantly more accurate than k\-Shape. Beyond clustering, we demonstrate the effectiveness of k\-Shape to
reduce the search space of one\-nearest\-neighbor classifiers for time series. Overall, SBD, k\-Shape, and k\-MS
emerge as domain\-independent, highly accurate, and efficient methods for time\-series comparison and clustering
with broad applications.
Papenbrock, J., Schwendner, P., Jaeger, M., and Krugel, S. (2021\). “Matrix Evolutions: Synthetic Correlations and
Explainable Machine Learning for Constructing Robust Investment Portfolios .” In:The Journal of Financial
Data Science 3(2\), pp. 51–69\.
In this article, the authors present a novel and highly flexible concept to simulate correlation matrixes of financial
markets. It produces realistic outcomes regarding stylized facts of empirical correlation matrixes and requires
no asset return input data. The matrix generation is based on a multiobjective evolutionary algorithm, so the
authors call the approach matrix evolutions. It is suitable for parallel implementation and can be accelerated by
graphics processing units and quantum\-inspired algorithms. The approach is useful for backtesting, pricing, and
hedging correlation\-dependent investment strategies and financial products. Its potential is demonstrated in a
machine learning case study for robust portfolio construction in a multi\-asset universe: An explainable machine
learning program links the synthetic matrixes to the portfolio volatility spread of hierarchical risk parity versus
equal risk contribution.
Park, J. (2020\). “Clustering Approaches for Global Minimum Variance Portfolio .” In:arXiv e\-Print .
104The only input to attain the portfolio weights of global minimum variance portfolio (GMVP) is the covariance
matrix of returns of assets being considered for investment. Since the population covariance matrix is not known,
investors use historical data to estimate it. Even though sample covariance matrix is an unbiased estimator of
the population covariance matrix, it includes a great amount of estimation error especially when the number
of observed data is not much bigger than number of assets. As it is difficult to estimate the covariance matrix
with high dimensionality all at once, clustering stocks is proposed to come up with covariance matrix in two
steps: firstly, within a cluster and secondly, between clusters. It decreases the estimation error by reducing the
number of features in the data matrix. The motivation of this dissertation is that the estimation error can
still remain high even after clustering, if a large amount of stocks is clustered together in a single group. This
research proposes to utilize a bounded clustering method in order to limit the maximum cluster size. The result
of experiments shows that not only the gap between in\-sample volatility and out\-of\-sample volatility decreases,
but also the out\-of\-sample volatility gets reduced. It implies that we need a bounded clustering algorithm so
that maximum clustering size can be precisely controlled to find the best portfolio performance.
Parker, F. J. (2016a). “Goal\-Based Portfolio Optimization .” In:The Journal of Wealth Management 19(3\), pp. 22–
30\.
The article presents a goal\-based portfolio optimization approach that is truly native to the goal\-based environ\-
ment. It begins by redefining risk as the probability of failing to attain a specified goal and redefining reward as
the excess wealth over and above what is required by the goal. It then presents an optimization procedure that
seeks to minimize goal failure and maximize excess return. In preliminary tests, it finds that this goal\-based
procedure lowers the probability of failing to achieve a specified goal while delivering higher excess wealth than
the procedures currently available.
Parker, F. J. (2016b). “Portfolio Selection in a Goal\-Based Setting .” In:The Journal of Wealth Management 19(2\),
pp. 41–46\.
Usingdifferentportfolioratios,weillustratethedeficienciesofusingonlymodernportfoliotheory(MPT)metrics
and assumptions when selecting portfolios in a goal\-based setting. Through the lenses of the ratios, we show
how MPT can choose the wrong, albeit efficient, portfolio to accomplish a goal. These facts illustrate the need
for goal\-based practitioners to factor in other variables, such as time to a goal and maximum loss thresholds,
when managing a portfolio to a goal\-oriented mandate.
Parker,F.J.(2021a). “AchievingGoalsWhileMakinganImpact:BalancingFinancialGoalswithImpactInvesting .”
In:The Journal of Impact and ESG Investing 1(3\), pp. 27–38\.
For investors who wish to engage in impact investing and who have specific goals to achieve, there exists the
potential for a trade\-off. When impact investments yield lower returns than nonimpact portfolios, how much
return should an investor be willing to give up to incorporate it? Using recent advances in goals\-based utility
theory, this article explores an answer to that question and offers practical and concrete advice for advisors
to individual investors and fiduciaries of trusts. Using the goals\-based framework, the author shows how an
investor’s willingness to sacrifice return for an impact investing mandate changes in response to market and
portfolio conditions.
Parker, F. J. (2021b). “Multi\-Period Goals\-Based Portfolio Optimization .” In:SSRN e\-Print .
Portfolio managers regularly have views on capital markets that span multiple periods. A portfolio manager,
for example, may expect a recession with high probability over the coming period, followed by a recovery in the
subsequentperiod.Currently,therearefewmethodsforoptimalportfolioallocationacrossthesemultipleperiods
that match how practitioners operate in the real world. Herein, we present a multi\-period optimization method
using a goals\-based framework that allows practitioners to develop multi\-period capital market expectations and
optimize their portfolios across those periods.
Paskaramoorthy, A., Gebbie, T., and van Zyl, T. (2021\). “The efficient frontiers of mean\-variance portfolio rules
under distribution misspecification .” In:arXiv e\-Print .
Mean\-variance portfolio decisions that combine prediction and optimisation have been shown to have poor
empiricalperformance.Here,weconsidertheperformanceofvariousshrinkagemethodsbytheirefficientfrontiers
under different distributional assumptions to study the impact of reasonable departures from Normality. Namely,
we investigate the impact of first\-order auto\-correlation, second\-order auto\-correlation, skewness, and excess
kurtosis. We show that the shrinkage methods tend to re\-scale the sample efficient frontier, which can change
based on the nature of local perturbations from Normality. This re\-scaling implies that the standard approach
of comparing decision rules for a fixed level of risk aversion is problematic, and more so in a dynamic market
setting.Ourresultssuggestthatcomparingefficientfrontiershasseriousimplicationswhichopposetheprevailing
105thinking in the literature. Namely, that sample estimators out\-perform Stein type estimators of the mean, and
that improving the prediction of the covariance has greater importance than improving that of the means.
Pawar, A. and Rathi, A. (2021\). “An Ensemble Approach to Portfolio Optimization .” In:SSRN e\-Print .
Markowitz’ optimization relies on correct estimates of expected returns and covariance matrix. However, a very
long time series of returns is required to get reliable sample estimates, and such data is usually unavailable.
Literature suggests cleaning either the sample estimates before employing them as inputs or imposing some
structure on portfolio weights. We suggest a strategy similar to the latter based on an ensemble technique. Our
approach blends weights from four popular strategies namely \- Volatility Minimisation, Sharpe Maximisation,
Geometric Mean Maximisation and Equally\-Weighted portfolio. By only employing a structure on the covariance
matrix, we find that such a strategy reduces the likelihood of extreme allocation leading to lower variance in
weights and hence lower estimation risk. An empirical study using Indian data finds that the suggested strategy
exhibits larger Sharpe ratios and smaller drawdown out\-of\-sample compared to naive equally weighted strategy.
Pedersen, L. H., Babu, A., and Levine, A. (2020\). “Enhanced Portfolio Optimization .” In:SSRN e\-Print .
We show how to identify the portfolios that cause problems in standard mean\-variance optimization (MVO)
and develop an enhanced portfolio optimization (EPO) method that addresses the problems. The EPO solution
encompasses existing methods such as standard MVO, reverse\-MVO, a Bayesian estimator, Black\-Litterman,
robust optimization, a form of generalized ridge regression used in machine learning, and random matrix theory.
Nevertheless, the closed\-form EPO is extremely simple. Applying EPO on several realistic datasets, we find
significant gains relative to standard benchmarks. In equities, EPO significantly outperforms the market, the
1/N portfolio, and standard asset pricing factors. Similarly in global asset allocation, EPO delivers economically
significant increases in the Sharpe ratio and statistically significant alpha to standard time series momentum
strategies and other benchmarks.
Pedersen,L.H.,Babu,A.,andLevine,A.(2021\). “EnhancedPortfolioOptimization .”In:Financial Analysts Journal
77(2\), pp. 14–151\.
We show how to identify the portfolios that cause problems in standard mean\-variance optimization (MVO)
and develop an enhanced portfolio optimization (EPO) method that addresses the problems. The EPO solution
encompasses existing methods such as standard MVO, reverse\-MVO, a Bayesian estimator, Black\-Litterman,
robust optimization, a form of generalized ridge regression used in machine learning, and random matrix theory.
Nevertheless, the closed\-form EPO is extremely simple. Applying EPO on several realistic datasets, we find
significant gains relative to standard benchmarks. In equities, EPO significantly outperforms the market, the
1/N portfolio, and standard asset pricing factors. Similarly in global asset allocation, EPO delivers economically
significant increases in the Sharpe ratio and statistically significant alpha to standard time series momentum
strategies and other benchmarks.
Peralta, G. and Zareei, A. (2016\). “A network approach to portfolio selection .” In:Journal of Empirical Finance
38, pp. 157–180\.
Low\-central stocks receive higher weights in optimal allocation. Financial and market variables are major drivers
of stocks’ centrality. We construct a network\-based investment strategy that performs well out\-of\-sample. Our
network\-based strategy results in positive and significant Carhart’s alphas. In this study, a financial market
is conceived as a network where the securities are nodes and the links account for returns’ correlations. We
theoretically prove the negative relationship between the centrality of assets in this financial market network
and their optimal weights under the Markowitz framework. Therefore, optimal portfolios overweight low\-central
securities to avoid the large variances that result when highly influential stocks are included in the investor’s
opportunity set. Next, we empirically investigate the major financial and market determinants of stock’s cen\-
tralities. The evidence indicates that highly central nodes tend to coincide with older, larger\-cap, cheaper and
financially riskier securities. Finally, we explore by means of in\-sample and out\-of\-sample analysis the extent to
which the structure of the stock market network can be employed to improve the portfolio selection process.
We propose a network\-based investment strategy that outperforms well\-known benchmarks while presenting
positive and significant Carhart alphas. The major contribution of the paper is to employ the financial market
network as a useful device to improve the portfolio selection process by targeting a group of assets according to
their centrality.
Perchet, R., Carvalho, R. L. d., and Moulin, P. (2014\). “Inter\-temporal risk parity: a constant volatility framework
for factor investing .” In:Journal of Investment Strategies 4(1\).
Inter\-temporal risk parity is a strategy that rebalances risky assets and cash in order to target a constant
level of ex\-ante risk over time. When applied to equities and compared to a buy\-and\-hold portfolio it is known
106to improve the Sharpe ratio and reduce drawdowns. We apply inter\-temporal risk parity strategies to factor
investing, namely value and momentum investing in equities, government bonds and foreign exchange. Value
andmomentumfactorsgenerateapremiumwhichistraditionallycapturedbydollar\-neutrallong\-shortportfolios
rebalanced every month to take into account changes in stock factor exposures and keep leverage constant. An
inter\-temporal risk parity strategy re\-balances the portfolio to the level of leverage required to target a constant
ex\-ante risk over time. Value and momentum risk\-adjusted premiums increase, sometimes significantly, when an
inter\-temporal risk parity strategy is applied. Volatility clustering and fat tails are behind this improvement of
risk\-adjusted premiums. Drawdowns are, however, not smoothed when applying the strategy to factor investing.
The benefits of the inter\-temporal risk parity strategy are more important for equity and foreign\-exchange
factors, with the strongest volatility clustering and fat tails. For government bond factors, with little volatility
clustering, the benefits of the strategy appear less significant.
Perchet, R., Xiao, L., Carvalho, R. L., and Heckel, T. (2015\). “Insights into Robust Portfolio Optimization: Decom\-
posing Robust Portfolios into Mean\-Variance and Risk\-Based Portfolios .” In:SSRN e\-Print .
For a number of different formulations of robust portfolio optimization, quadratic and absolute, we show that
in the limit of low uncertainty in estimated asset mean returns the robust portfolio converges towards the
mean\-variance portfolio obtained with the same inputs; and in the limit of high uncertainty the robust portfolio
converges towards a risk\-based portfolio, which is a function of how the uncertainty in estimated asset mean
returns is defined. We give examples in which the robust portfolio converges toward the minimum variance,
the inverse variance, the equal\-risk budget and the equally weighted portfolio in the limit of sufficiently large
uncertainty in asset mean returns. At intermediate levels of uncertainty we find that a weighted average of the
mean\-variance portfolio and the respective limiting risk\-based portfolio offer a good representation of the robust
portfolio, in particular in the case of the quadratic formulation. The results remain valid even in the presence of
portfolio constraints, in which case the limiting portfolios are the corresponding constrained mean\-variance and
constrained risk\-based portfolios. We believe our results are important in particular for risk\-based investors who
wish to take into account expected returns to gently tilt away from their current allocations, e.g. risk parity or
minimum variance.
Perrin,S.andRoncalli,T.(2020\). “MachineLearningOptimizationAlgorithms\&PortfolioAllocation .”In:Machine
Learning for Asset Management: New Developments and Financial Applications . Ed. by E. Jurczenko. Wiley,
pp. 261–328\.
This chapter shows how portfolio allocation can benefit from the development of large\-scale portfolio optimiza\-
tion algorithms such as the coordinate descent, the alternating direction method of multipliers, the proximal
gradient method, and Dykstra’s algorithm. With these optimization algorithms, it considers more complex port\-
folio optimization programs with non\-quadratic objective function, regularization with penalty functions and
nonlinear constraints. The chapter discusses three main models of smart beta portfolios: the equal risk contri\-
bution portfolio, the risk budgeting portfolio, and the most diversified portfolio. A robo\-advisor has two main
objectives. The first objective is to know the investor better than a traditional asset manager. Because of this
better knowledge, the robo\-advisor may propose a more appropriate asset allocation. The second objective is to
perform the task in a systematic way and to build an automated rebalancing process.
Pichler, A., Poledna, S., and Thurner, S. (2018\). “Systemic\-risk\-efficient asset allocation: Minimization of systemic
risk as a network optimization problem .” In:arXiv e\-Print .
Systemic risk arises as a multi\-layer network phenomenon. Layers represent direct financial exposures of various
types, including interbank liabilities, derivative\- or foreign exchange exposures. Another network layer of sys\-
temic risk emerges through common asset holdings of financial institutions. Strongly overlapping portfolios lead
to similar exposures that are caused by price movements of the underlying financial assets. Based on the knowl\-
edge of portfolio holdings of financial agents we quantify systemic risk of overlapping portfolios. We present an
optimizationprocedure,whereweminimizethesystemicriskinagivenfinancialmarketbyoptimallyrearranging
overlapping portfolio networks, under the constraints that the expected returns and risks of the individual port\-
folios are unchanged. We explicitly demonstrate the power of the method on the overlapping portfolio network of
sovereign exposure between major European banks by using data from the European Banking Authority stress
test of 2016\. We show that systemic\-risk\-efficient allocations are accessible by the optimization. In the case of
sovereign exposure, systemic risk can be reduced by more than a factor of two, with\- out any detrimental effects
for the individual banks. These results are confirmed by a simple simulation of fire sales in the government bond
market. In particular we show that the contagion probability is reduced dramatically in the optimized network.
Pinar, M. (2016\). “On robust mean\-variance portfolios .” In:Optimization 65(5\), pp. 1039–1048\.
107We derive closed\-form portfolio rules for robust mean?variance portfolio optimization where the return vector
is uncertain or the mean return vector is subject to estimation errors, both uncertainties being confined to an
ellipsoidal uncertainty set. We consider different mean?variance formulations allowing short sales, and derive
closed\-form optimal portfolio rules in static and dynamic settings.
Plachel, L. (2019\). “A unified model for regularized and robust portfolio optimization .” In:Journal of Economic
Dynamics and Control 109, p. 103779\.
Mean\-variance optimization severely suffers from model\- and estimation errors. Two commonly isolated but com\-
plementary concepts to overcome the corresponding limitations are problem regularization and robustification.
I introduce a joint method for covariance regularization and robust optimization which exploits this comple\-
mentarity and I show that both the regularization\- as well as the robust optimization part can be achieved
through systematic manipulations of the correlation matrix eigenvalues. An application of the method to eq\-
uity markets reveals similarly attractive behavior as pure covariance regularization during normal times and
improved performance if a jump in systematic risk occurs. Furthermore, the model constitutes a framework for
the logically consistent incorporation of systematic risk expectations into the portfolio selection problem and
thereby complements similar models for individual return expectations, such as the Black and Litterman model.
Platanakis, E., Sutcliffe, C. M., and Ye, X. (2021\). “Horses for Courses: Mean\-Variance for Asset Allocation and
1/N for Stock Selection .” In:European Journal of Operational Research 288(1\), pp. 302–317\.
For various organizational reasons, large investors typically split their portfolio decision into two stages \- asset
allocation and stock selection. We hypothesise that mean\-variance models are superior to equal weighting for
asset allocation, while the reverse applies for stock selection, as estimation errors are less of a problem for
mean\-variance models when used for asset allocation than for stock selection. We confirm this hypothesis in
separate analyses of US and international equities using four different types of mean\-variance model (Bayes\-
Stein, Black\-Litterman, Bayesian diffuse prior and Markowitz), a range of parameter settings, and a simulation
analysis calibrated to US data.
Pollak, I. (2012\). “Covariance estimation and related problems in portfolio optimization .” In:Sensor Array and
Multichannel Signal Processing Workshop .
This overview paper reviews covariance estimation problems and related issues arising in the context of portfo\-
lio optimization. Given several assets, a portfolio optimizer seeks to allocate a fixed amount of capital among
these assets so as to optimize some cost function. For example, the classical Markowitz portfolio optimization
framework defines portfolio risk as the variance of the portfolio return, and seeks an allocation which minimizes
the risk subject to a target expected return. If the mean return vector and the return covariance matrix for
the underlying assets are known, the Markowitz problem has a closed\-form solution. In practice, however, the
expected returns and the covariance matrix of the returns are unknown and are therefore estimated from histor\-
ical data. This introduces several problems which render the Markowitz theory impracticable in real portfolio
management applications. This paper discusses these problems and reviews some of the existing literature on
methods for addressing them.
Posch, P. N. and Ullmann, D. (2016\). “Estimation of Large Correlation Matrix with Shrinking Methods .” In:SSRN
e\-Print.
An exact estimation of the true correlation matrix is highly desirable in many applications. In practice there
will always be an estimation error which, however, can be not only minimized using the shrinking approach
but also an invertible correlation matrix can be calculated when there are fewer observations than assets. We
compare several shrinking methods regarding their correlation matrix estimation using several data generating
processes. We calculate the distance of the estimator to the true matrix and check, if improvements transfer
to economic improvement, measured by the Sharpe ratio. Firstly, we find that a more accurate estimation of
the covariance matrix leads to a better estimation of the correlation matrix and secondly, better estimations of
the correlation matrix lead to significant economic improvements. Although each shrinking estimator performs
differently regarding the shape of the return distribution, the general usage of shrinking estimators leads to a
better estimation of the correlation matrix than the standard estimator.
Procacci, P. F. and Aste, T. (2021\). “Portfolio Optimization with Sparse Multivariate Modelling .” In:arXiv e\-Print .
Portfolio optimization approaches inevitably rely on multivariate modeling of markets and the economy. In this
paper, we address three sources of error related to the modeling of these complex systems: 1\. oversimplifying
hypothesis; 2\. uncertainties resulting from parameters’ sampling error; 3\. intrinsic non\-stationarity of these
systems. For what concerns point 1\. we propose a L0\-norm sparse elliptical modeling and show that sparsification
is effective. The effects of points 2\. and 3\. are quantifified by studying the models’ likelihood in\- and out\-of\-
108sample for parameters estimated over train sets of different lengths. We show that models with larger off\-sample
likelihoods lead to better performing portfolios up to when two to three years of daily observations are included
in the train set. For larger train sets, we found that portfolio performances deteriorate and detach from the
models’ likelihood, highlighting the role of non\-stationarity. We further investigate this phenomenon by studying
the out\-of\-sample likelihood of individual observations showing that the system changes significantly through
time. Larger estimation windows lead to stable likelihood in the long run, but at the cost of lower likelihood in
the short\-term: the ‘optimal’ fit in finance needs to be defined in terms of the holding period. Lastly, we show
that sparse models outperform full\-models in that they deliver higher out of sample likelihood, lower realized
portfolio volatility and improved portfolios’ stability, avoiding typical pitfalls of the Mean\-Variance optimization.
Qian, E. (2013\). “Are Risk\-Parity Managers at Risk Parity? ” In:The Journal of Portfolio Management Fall, pp. 20–
26\.
Risk parity has become an accepted investment strategy, to some degree. Its main advantage is its use of risk
allocation, as opposed to the capital allocation used by the traditional asset allocation approach. A balanced
risk allocation provides true diversification; therefore risk parity should deliver better risk\-adjusted return over
time. Despite the acceptance and the fact that the term risk parity has been in use for almost ten years, the
investment community seems confused about risk parity’s true definition. Is it just a quantitative risk\-budgeting
technique? Is it about operational leverage? Or is it about high exposures to fixed income and low exposures
to equities? In this paper, the author aims to define the principle of risk parity investing. He then examines a
sample of risk parity managers, using the return\-based style analysis pioneered by William Sharpe. The results
show that, according to the defined principle, a number of risk parity managers in our sample are not using true
risk parity.
Qian, E. E. (2018\). Portfolio Rebalancing . Chapman and Hall/CRC. 262 pp.
The goal of Portfolio Rebalancing is to provide mathematical and empirical analysis of the effects of portfolio
rebalancing on portfolio returns and risks. The mathematical analysis answers the question of when and why
fixed\-weight portfolios might outperform buy\-and\-hold portfolios based on volatilities and returns. The empirical
analysis, aided by mathematical insights, will examine the effects of portfolio rebalancing in capital markets for
asset allocation portfolios and portfolios of stocks, bonds, and commodities.
Radovanov, B. and Marcikic, A. (2014\). “Testing The Performance Of The Investment Portfolio Using Block Boot\-
strap Method .” In:Economic Themes 52(2\).
The aim of this paper is to create a stable model of investment portfolio optimization through a high degree
of diversification and reduction of sudden changes in the allocation with monitoring of the dynamics of the
impact factor. In this sense, there is bootstrap application procedure, which, without an excessive number of
constraints involved in the optimization process provides solutions based on uncertain information. Thus defined,
the optimization method has been patented by Michaud (1999\) entitled re\-sampled efficiency. Accordingly, this
paper offers a comparison of the performance block bootstrap optimization models and traditional Markowitz’s
model inside and outside of the sample by applying the most frequently traded stocks on the BSE. The results
show a better performance out of the sample and the presence of a larger number of shares forming the portfolio
through bootstrap methodology. However, only through the traditional optimization process could be attained
optimum according to the required limits. Such effects can be observed by comparing the limits of efficiency
obtained through these optimization models. However, optimization\-based methods bootstrap finds its place in
reducing errors of assessment resulting from the limited sample size.
Raffinot, T. (2017\). “Hierarchical Clustering\-Based Asset Allocation .” In:The Journal of Portfolio Management
44(2\), pp. 89–99\.
This article proposes a hierarchical clustering\-based asset allocation method, which uses graph theory and
machine learning techniques. Hierarchical clustering refers to the formation of a recursive clustering, suggested
by the data, not defined a priori. Several hierarchical clustering methods are presented and tested. Once the
assets are hierarchically clustered, the authors compute a simple and efficient capital allocation within and
across clusters of assets, so that many correlated assets receive the same total allocation as a single uncorrelated
one. The out\-of\-sample performances of hierarchical clustering\-based portfolios and more traditional risk\-based
portfolios are evaluated across three disparate datasets, which differ in term of the number of assets and the
assets’ composition. To avoid data snooping, the authors assess the comparison of profit measures using the
bootstrap\-based model confidence set procedure. Their empirical results indicate that hierarchical clustering\-
based portfolios are robust and truly diversified and achieve statistically better risk\-adjusted performances than
commonly used portfolio optimization techniques.
109Raffinot, T. (2018\). “The Hierarchical Equal Risk Contribution Portfolio .” In:SSRN e\-Print .
Building upon the fundamental notion of hierarchy, the ”Hierarchical Risk Parity” (HRP) and the ”Hierarchical
Clustering based Asset Allocation” (HCAA), the Hierarchical Equal Risk Contribution Portfolio (HERC) aims
at diversifying capital allocation and risk allocation. HERC merges and enhances the machine learning approach
of HCAA and the Top\-Down recursive bisection of HRP. In more detail, the modified Top\-Down recursive
division is based on the shape of dendrogram, follows an Equal Risk Contribution allocation and is extended to
downside risk measures such as conditional value at risk (CVaR) and Conditional Drawdown at Risk (CDaR).
The out\-of\-sample performances of hierarchical clustering based portfolios are evaluated across two empirical
datasets, which differ in terms of number of assets and composition of the universe (multi\-assets and individual
stocks). Empirical results highlight that HERC Portfolios based on downside risk measures achieve statistically
better risk\-adjusted performances, especially those based on the CDaR.
Rattray, S., Granger, N., Harvey, C. R., and Hemert, O. V. (2020\). “Strategic Rebalancing .” In:The Journal of
Portfolio Management 46(6\), pp. 10–31\.
A mechanical rebalancing strategy, such as a monthly or quarterly reallocation toward fixed portfolio weights,
is an active strategy. Winning asset classes are sold, and losers are bought. During crises, when markets are
often trending, this can lead to substantially larger drawdowns than a buy\-and\-hold strategy. This article shows
that the negative convexity induced by rebalancing can be substantially mitigated, taking the popular 60\-40
stock\-bond portfolio as the use case. One alternative is an allocation to a trend\-following strategy. The positive
convexity of this overlay tends to counter the impact on drawdowns of the mechanical rebalancing strategy. The
second alternative is called strategic rebalancing, which uses smart rebalancing timing based on trend\-following
signals, without a direct allocation to a trend\-following strategy. For example, if the trend\-following model
suggests that stock markets are in a negative trend, rebalancing is delayed.
Rebonato, R. (2019\). “A financially justifiable and practically implementable approach to coherent stress testing .”
In:Quantitative Finance 19(5\), pp. 827–842\.
We present an approach to stress testing that is both practically implementable and solidly rooted in well\-
established financial theory. We present our results in a Bayesian\-net context, but the approach can be extended
to different settings. We show (i) how the consistency and continuity conditions are satisfied; (ii) how the result
of a scenario can be consistently cascaded from a small number of macrofinancial variables to the constituents
of a granular portfolio; and (iii) how an approximate but robust estimate of the likelihood of a given scenario
can be estimated. This is particularly important for regulatory and capital\-adequacy applications.
Reinikainen,K.(2020\). “StrategicAssetAllocationUsingRobustCovarianceEstimationandPortfolioOptimization
Methods .” MA thesis. Aalto University.
Strategic asset allocation is the single most important determinant of portfolio returns. While the drawbacks
of using mean\-variance optimization and the sample covariance matrix for strategic asset allocation are well\-
documented in the literature, they are still broadly applied among investment professionals. In this thesis
we study two robust alternatives for the sample covariance matrix, shrinkage and hierarchical clustering, and
two robust alternatives for mean\-variance optimization, resampling optimization and regularized optimization.
We develop a generalisable testing framework for comparing the out\-of\-sample risk\-return characteristics of a
broad range of covariance estimation and portfolio optimization methods. The testing framework is applied
to provide an empirical comparison of the performance of the traditional and robust methods in two testing
samples, when asset class volatilities, correlations and expected returns contain uncertainty. The choice of the
portfolio optimization method clearly dominated the choice of covariance estimation method as a determinant of
out\-of\-sample portfolio risk\-return characteristics. Out of the three portfolio optimization methods, resampling
optimization provided the investor portfolios with superior ratios of portfolio return and volatility as well as
portfolio return and maximum drawdown. Mean\-variance optimization and regularized optimization performed
more inconsistently, demonstrating sensitivity to the underlying assumptions made regarding the structure of
uncertainty in expected returns. As a non\-robust method, the realized returns of portfolios obtained using
mean\-variance optimization also deteriorated as the level of uncertainty in expected returns was increased.
Ren, F., Lu, Y.\-N., Li, S.\-P., Jiang, X.\-F., Zhong, L.\-X., and Qiu, T. (2017\). “Dynamic Portfolio Strategy Using
Clustering Approach .” In:PLOS ONE 12(1\), e0169299\+.
The problem of portfolio optimization is one of the most important issues in asset management. We here
propose a new dynamic portfolio strategy based on the time\-varying structures of MST networks in Chinese
stockmarkets,wherethemarketconditionisfurtherconsideredwhenusingtheoptimalportfoliosforinvestment.
A portfolio strategy comprises two stages: First, select the portfolios by choosing central and peripheral stocks
110in the selection horizon using five topological parameters, namely degree, betweenness centrality, distance on
degree criterion, distance on correlation criterion and distance on distance criterion. Second, use the portfolios
for investment in the investment horizon. The optimal portfolio is chosen by comparing central and peripheral
portfolios under different combinations of market conditions in the selection and investment horizons. Market
conditions in our paper are identified by the ratios of the number of trading days with rising index to the total
number of trading days, or the sum of the amplitudes of the trading days with rising index to the sum of
the amplitudes of the total trading days. We find that central portfolios outperform peripheral portfolios when
the market is under a drawup condition, or when the market is stable or drawup in the selection horizon and
is under a stable condition in the investment horizon. We also find that peripheral portfolios gain more than
central portfolios when the market is stable in the selection horizon and is drawdown in the investment horizon.
Empirical tests are carried out based on the optimal portfolio strategy. Among all possible optimal portfolio
strategies based on different parameters to select portfolios and different criteria to identify market conditions,
65 percent of our optimal portfolio strategies outperform the random strategy for the Shanghai A\-Share market
while the proportion is 70 percent for the Shenzhen A\-Share market.
Richard, J.\-C. and Roncalli, T. (2019\). “Constrained Risk Budgeting Portfolios: Theory, Algorithms, Applications
and Puzzles .” In:arXiv e\-Print .
This article develops the theory of risk budgeting portfolios, when we would like to impose weight constraints.
It appears that the mathematical problem is more complex than the traditional risk budgeting problem. The
formulation of the optimization program is particularly critical in order to determine the right risk budgeting
portfolio. We also show that numerical solutions can be found using methods that are used in large\-scale
machinelearningproblems.Indeed,wedevelopanalgorithmthatmixesthemethodofcyclicalcoordinatedescent
(CCD), alternating direction method of multipliers (ADMM), proximal operators and Dykstra’s algorithm. This
theoretical body is then applied to some investment problems. In particular, we show how to dynamically control
the turnover of a risk parity portfolio and how to build smart beta portfolios based on the ERC approach by
improving the liquidity of the portfolio or reducing the small cap bias. Finally, we highlight the importance of
the homogeneity property of risk measures and discuss the related scaling puzzle.
Rietz, R., Blumenschein, T., Crough, S., and Cohen, A. (2018\). “Analyzing Retirement Withdrawal Strategies .” In:
Preprints .
An optimal withdrawal strategy beginning at age 65 provides a lifetime income from a portfolio, adjusted
annually for inflation, while reducing the probability of living in financial ruin to an ac\-ceptable level. This
paper analyzes the probability of living in financial ruin, potentially for multiple years, rather than just the
event of ruin. A stochastic Excel model was developed to simulate the effect of varying investment returns on
a portfolio with two asset classes; large company stocks and long\-term government bonds. A stochastic model
is also applied to retiree mortality. The following variables were analyzed to determine their relative impact
on withdrawal strategies: Withdrawing a constant percentage of the portfolio, Gender, Initial asset allocation,
Asset allocation rebalancing methods, and Low investment return environments. For both genders and most
withdrawal rates, an approximately equal initial asset allocation of stocks and bonds, combined with a level
rebalancing function, provided the lowest probability of living in financial ruin. Because each investment return
followed its own probability distribution function, some retirees experienced financial ruin even in the most
conservative simulations.
Rigamonti, A. (2020\). “Mean\-Variance Optimization Is a Good Choice, But for Other Reasons than You Might
Think.” In:Risks8(1\), p. 29\.
Mean\-variance portfolio optimization is more popular than optimization procedures that employ downside risk
measures such as the semivariance, despite the latter being more in line with the preferences of a rational
investor. We describe strengths and weaknesses of semivariance and how to minimize it for asset allocation
decisions. We then apply this approach to a variety of simulated and real data and show that the traditional
approach based on the variance generally outperforms it. The results hold even if the CVaR is used, because
all downside risk measures are difficult to estimate. The popularity of variance as a measure of risk appears
therefore to be rationally justified.
Roncalli, T. (2021\). “Advanced Course in Asset Management .” In:SSRN e\-Print .
These presentation slides have been written for the Advanced Course in Asset Management (theory and appli\-
cations) given at the University of Paris\-Saclay. They contain 15 tutorial exercises and 5 main lectures:
1\)Portfolio Optimization
2\)Risk Budgeting
1113\)Smart Beta, Factor Investing and Alternative Risk Premia
4\)Green and Sustainable Finance, ESG Investing and Climate Risk
5\)Machine Learning in Asset Management
The Table of contents is the following:
Part 1\. Portfolio Optimization 1\. Theory of portfolio optimization 1\.a. The Markowitz framework 1\.b. Capital
asset pricing model (CAPM) 1\.c. Portfolio optimization in the presence of a benchmark 1\.d. Black\-Litterman
model 2\. Practice of portfolio optimization 2\.a. Covariance matrix 2\.b. Expected returns 2\.c. Regularization of
optimized portfolios 2\.d. Adding constraints 3\. Tutorial exercises 3\.a. Variations on the efficient frontier 3\.b.
Beta coefficient 3\.c. Black\-Litterman model
Part 2\. Risk Budgeting 1\. The ERC portfolio 1\.a. Definition 1\.b. Special cases 1\.c. Properties 1\.d. Numerical
solution2\.Extensionstoriskbudgetingportfolios2\.a.DefinitionofRBportfolios2\.b.PropertiesofRBportfolios
2\.c. Diversification measures 2\.d. Using risk factors instead of assets 3\. Risk budgeting, risk premia and the risk
parity strategy 3\.a. Diversified funds 3\.b. Risk premium 3\.c. Risk parity strategies 3\.d. Performance budgeting
portfolios 4\. Tutorial exercises 4\.a. Variation on the ERC portfolio 4\.b. Weight concentration of a portfolio 4\.c.
The optimization problem of the ERC portfolio 4\.d. Risk parity funds
Part 3\. Smart Beta, Factor Investing and Alternative Risk Premia 1\. Risk\-based indexation 1\.a. Capitalization\-
weighted indexation 1\.b. Risk\-based portfolios 1\.c. Comparison of the four risk\-based portfolios 1\.d. The case
of bonds 2\. Factor investing 2\.a. Factor investing in equities 2\.b. How many risk factors? 2\.c. Construction of
risk factors 2\.d. Risk factors in other asset classes 3\. Alternative risk premia 3\.a. Definition 3\.b. Carry, value,
momentum and liquidity 3\.c. Portfolio allocation with ARP 4\. Tutorial exercises 4\.a. Equally\-weighted portfolio
4\.b. Most diversified portfolio 4\.c. Computation of risk\-based portfolios 4\.d. Building a carry trade exposure
Part 4\. Green and Sustainable Finance, ESG Investing and Climate Risk 1\. ESG investing 1\.a. Introduction to
sustainable finance 1\.b. ESG scoring 1\.c. Performance in the stock market 1\.d. Performance in the corporate
bond market 2\. Climate risk 2\.a. Introduction to climate risk 2\.b. Climate risk modeling 2\.c. Regulation of
climate risk 2\.d. Portfolio management with climate risk 3\. Sustainable financing products 3\.a. SRI Investment
funds 3\.b. Green bonds 3\.c. Social bonds 3\.d. Other sustainability\-linked strategies 4\. Impact investing 4\.a.
Definition 4\.b. Sustainable development goals (SDG) 4\.c. Voting policy, shareholder activism and engagement
4\.d. The challenge of reporting 5\. Tutorial exercises 5\.a. Probability distribution of an ESG score 5\.b. Enhanced
ESG score and tracking error control
Part 5\. Machine Learning in Asset Management 1\. Portfolio optimization 1\.a. Standard optimization algorithms
1\.b. Machine learning optimization algorithms 1\.c. Application to portfolio allocation 2\. Pattern learning and
self\-automated strategies 3\. Market generators 4\. Tutorial exercises 4\.a. Portfolio optimization with CCD and
ADMM algorithms 4\.b. Regularized portfolio optimization.
Roy, R. (2021\). “Examining the drivers of optimal portfolio construction .” PhD thesis. City University of London.
Markowitz advanced the theory of portfolio construction, dividing the work into two stages of security selection
and capital allocation. He did not address security selection, but established a new method to allocate capital.
Since then, much has been written regarding each stage while the investment industry grew and its performance
was examined through a variety of lenses. This thesis contributes to the literature by examining the interaction
between these two stages of portfolio construction. Each stage impacts performance, but an examination of
the interaction is missing from the literature. A deeper understanding of the interaction provides opportunity
for practitioners to improve portfolios and gives a base for future research to refine the understanding. The
research begins by holding 1,000 US large capitalization stocks constant while applying a panel of capital
allocation methods. Despite starting a fixed set of securities, differences in performance and risk characteristics
are documented. Markowitz identified the objective superiority of risk adjusted returns over just returns, so my
work applies the Sharpe ratio as the measurement unit. Differences in Sharpe ratios across the panel of allocation
methods are tested for robustness using a bootstrap test. With a hierarchy of Sharpe ratios established, the next
step varies the security selection and observes the change in Sharpe ratios. Security selection is implemented
with one year perfect foresight which is a limit condition for the potential of stock picking. When applying
good and bad security selection it is observed that the hierarchy of Sharpe ratios is unstable in the presence
of security selection. The bootstrap robustness test shows the hierarchy can invert with statistical significance.
This is the first step in understanding the dependence of the optimal capital allocation method in the presence of
security selection skill. Toward the goal of optimal Sharpe ratio portfolios, I examine portfolios constructed with
perfect foresight into return, volatility, and correlations. Optimized portfolios are dominated by low correlation
112securities, not by high returning securities. Conversely, by first selecting the highest returning securities possible,
you crowd out the optimal Sharpe solution. Reward curves are built for selecting securities based on returns,
volatility, and correlation. The shape of the correlation reward curve is like the low volatility anomaly. Because
low correlation securities dominate optimized Sharpe ratio portfolios, perfect correlation selection is applied.
Stock level and portfolio level characteristics are documented in the cross section of years. Then the method
is applied to the panel of allocation methods to create return time series and Sharpe ratios. The bootstrap
robustness test applied to the Sharpe ratios of the allocation methods shows that even in the absence of perfect
correlation selection, nearly any level of success achieved in correlation selection creates robust improvements in
the Sharpe ratio.
Rudin, A. and Farley, D. (2022\). “Dual\-Horizon Strategic Asset Allocation .” In:The Journal of Portfolio Manage\-
ment48(3\), pp. 59–72\.
In this article, the authors propose a new dual\-horizon asset allocation framework that balances desire for long\-
term portfolio optimality with the requirement for short\-term risk control. The framework leverages evidence
that for many core asset classes, price patterns can be effectively decomposed into a long\-term, persistent
component and a transient, cyclical one. This decomposition is particularly helpful when applied to private and
public sister\-asset classes (e.g., private and public equity or debt) because it allows harmonization of private
and public risk\-adjusted returns without resorting to artificial adjustments.
Rudin, A., Mor, V., and Farley, D. (2020\). “Adaptive optimal risk budgeting .” In:The Journal of Portfolio Man\-
agement 46(6\), pp. 147–158\.
In this article, the authors suggest Bayesian\-style adaptive enhancement to a popular equal risk contribution
(ERC) portfolio construction technique they call adaptive optimal risk budgeting (AORB). The enhancement
has the potential to bring portfolios closer to mean\-variance efficiency when Sharpe ratios and correlations of
assets vary while retaining some of the ERC robustness to estimation errors. The authors test AORB viability by
putting it in competition with ERC itself and with a version of the Bayesian shrinkage mean\-variance technique
in a carefully simulated setting. They find that the new method appears to deliver measurable advantages over
its competition in a broad range of realistic settings. Multiple possible applications to portfolios of risk premia
strategies and a multi\-asset universe more generally are discussed by the authors.
Sahamkhadam, M., Stephan, A., and Ostermark, R. (2020\). “Copula\-Based Black\-Litterman Portfolio Optimiza\-
tion.” In:SSRN e\-Print .
We extend the Black\-Litterman (BL) approach to incorporate tail dependency in portfolio optimization and
estimate the posterior joint distribution of returns using vine copulas. Our novel copula\-based BL (CBL) model
leads to flexibility in modeling returns symmetric and asymmetric multivariate distribution from a range of
copula families. Based on a sample of 30 stocks, we evaluate the performance of the suggested CBL approach
and portfolio optimization technique using out\-of\-sample back\-testing. Our empirical analysis and robustness
check indicate better performance for the CBL portfolios in terms of lower tail risk and higher risk\-adjusted
returns, compared to the benchmark strategies.
Santos, A. A. P. (2019\). “Disentangling the role of variance and covariance information in portfolio selection prob\-
lems.” In:Quantitative Finance 19(1\), pp. 57–76\.
The covariation among financial asset returns is often a key ingredient used in the construction of optimal
portfolios. Estimating covariances from data, however, is challenging due to the potential influence of estimation
error, specially in high\-dimensional problems, which can impact negatively the performance of the resulting
portfolios. We address this question by putting forward a simple approach to disentangle the role of variance
and covariance information in the case of mean\-variance efficient portfolios. Specifically, mean\-variance portfolios
can be represented as a two\-fund rule: one fund is a fully invested portfolio that depends on diagonal covariance
elements, whereas the other is a long\-short, self financed portfolio associated with the presence of non\-zero off\-
diagonal covariance elements. We characterize the contribution of each of these two components to the overall
performance in terms of out\-of\-sample returns, risk, risk\-adjusted returns and turnover. Finally, we provide an
empirical illustration of the proposed portfolio decomposition using both simulated and real market data.
Sarmas, E., Xidonas, P., and Doukas, H. (2020\). Multicriteria Portfolio Construction with Python . Springer Inter\-
national Publishing.
This book covers topics in portfolio management and multicriteria decision analysis (MCDA), presenting a
transparent and unified methodology for the portfolio construction process. The most important feature of the
book includes the proposed methodological framework that integrates two individual subsystems, the portfolio
selection subsystem and the portfolio optimization subsystem. An additional highlight of the book includes the
113detailed, step\-by\-step implementation of the proposed multicriteria algorithms in Python. The implementation is
presented in detail; each step is elaborately described, from the input of the data to the extraction of the results.
Algorithms are organized into small cells of code, accompanied by targeted remarks and comments, in order to
help the reader to fully understand their mechanics. Readers are provided with a link to access the source code
through GitHub. https://github.com/epu\-ntua/Multicriteria\-Portfolio\-Construction\-with\-Python
This Work may also be considered as a reference which presents the state\-of\-art research on portfolio construc\-
tion with multiple and complex investment objectives and constraints. The book consists of eight chapters. A
brief introduction is provided in Chapter 1\. The fundamental issues of modern portfolio theory are discussed
in Chapter 2\. In Chapter 3, the various multicriteria decision aid methods, either discrete or continuous, are
concisely described. In Chapter 4, a comprehensive review of the published literature in the field of multicriteria
portfolio management is considered. In Chapter 5, an integrated and original multicriteria portfolio construc\-
tion methodology is developed. Chapter 6 presents the web\-based information system, in which the suggested
methodological framework has been implemented. In Chapter 7, the experimental application of the proposed
methodology is discussed and in Chapter 8, the authors provide overall conclusions.
The readership of the book aims to be a diverse group, including fund managers, risk managers, investment ad\-
visors, bankers, private investors, analytics scientists, operations researchers scientists, and computer engineers,
to name just several. Portions of the book may be used as instructional for either advanced undergraduate
or post\-graduate courses in investment analysis, portfolio engineering, decision science, computer science, or
financial engineering.
Sass, J. and Thos, A.\-K. (2022\). “Risk reduction and portfolio optimization using clustering methods .” In:Econo\-
metrics and Statistics .
Diversification is one of the main pillars of investment strategies. The prominent equal weight or one\-over\-N
portfolio,whichputsequalweightoneachasset,isapartfromitssimplicityastrategywhichishardtooutperform
in realistic settings. But depending on the number of considered assets it can lead to very large portfolios.
An approach to reduce the number of chosen assets based on clustering is proposed and its advantages and
disadvantagesareinvestigated.Usingclusteringtechniquesthepossibleassetsareseparatedintonon\-overlapping
clusters and the assets within a cluster are ordered by their Sharpe ratio. Then the best asset of each portfolio
is chosen to be a member of the new portfolio with equal weights, the cluster portfolio. It is shown that this
portfolio inherits the advantages of the equal weight portfolio and that it can even outperform it empirically.
To this end different performance measures are used to compare the portfolios on simulated and real data. To
explain the observations on real data, explanatory results are derived in an extreme model setting and analyzed
in several simulation studies.
Schadner, W. (2021\). “Feasible Implied Correlation Matrices from Factor Structures .” In:arXiv e\-Print .
Forward\-looking correlations are of interest in different financial applications, including factor\-based asset pric\-
ing, forecasting stock\-price movements or pricing index options. With a focus on non\-FX markets, this paper
defines necessary conditions for option implied correlation matrices to be mathematically and economically feasi\-
ble and argues, that existing models are typically not capable of guaranteeing so. To overcome this difficulty, the
problem is addressed from the underlying factor structure and introduces two approaches to solve it. Under the
quantitative approach, the puzzle is reformulated into a nearest correlation matrix problem which can be used
either as a stand\-alone estimate or to re\-establish positive\-semi\-definiteness of any other model’s estimate. From
an economic approach, it is discussed how expected correlations between stocks and risk factors (like CAPM,
Fama\-French) can be translated into a feasible implied correlation matrix. Empirical experiments are carried
out on monthly option data of the S\&P 100 and S\&P 500 index (1996\-2020\).
Schepel, J. F. (2019\). “Bayesian Extensions of the Black\-Litterman Model .” MA thesis. Erasmus University.
To reduce the estimation error portfolio managers encounter when determining their portfolio allocation, this
paper focuses on the application of the Black\-Litterman model within a more extensive Bayesian framework.
This framework allows to extend the existing Black\- Litterman models to include prior specifications on the
covariance matrix, hierarchical scaling parameter and non\-normal data. Applying these models to a S\&P 500
data set, the models using a Bayesian framework, taking into account additional parameter uncertainty, are
in some challenging environments able to obtain a superior result compared to the benchmarks, making it a
useful framework for portfolio managers. However, the models can not consistently outperform the less complex
benchmark models.
Scherer, B. (2007\). “Can robust portfolio optimisation help to build better portfolios? ” In:Journal of Asset Man\-
agement 7(6\), pp. 374–387\.
114Estimation error has always been acknowledged as a substantial problem in portfolio construction. Various
approaches exist that range from Bayesian methods with a very strong rooting in decision theory to practitioner\-
based heuristics with no rooting in decision theory at all as portfolio resampling. Robust optimisation is the
latest attempt to address estimation error directly in the portfolio construction process. It will be shown that
robust optimisation is equivalent to Bayesian shrinkage estimators and offer no marginal value relative to the
former. The implied shrinkage that comes with robust optimisation is difficult to control. Consistent with the
ad hoc treatment of uncertainty aversion in robust optimisation, it can be seen that out of sample performance
largely depends on the appropriate choice of uncertainty aversion, with no guideline on how to calibrate this
parameter or how to make it consistent with the more well\-known risk aversion.
Scherer, B. (2015\). Portfolio Construction and Risk Budgeting (Fifth Edition) . Risk Books. 350 pp.
Completely updated and extended to cover the rapid expansion of the literature since the financial crises, this
new edition of Portfolio Construction and Risk Budgeting provides the reader with a clear overview of the
subject. The author presents quantitative methods and comprehensive and up\-to\-date coverage of alternative
portfolio construction techniques, ranging from traditional methods based on mean\- variance and lower\-partial
moments approaches, through Bayesian techniques, to more recent developments such as portfolio re\-sampling
and stochastic programming solutions using scenario optimisation.
Schuhmacher, F., Kohrs, H., and Auer, B. R. (2021\). “Justifying Mean\-Variance Portfolio Selection when Asset
Returns Are Skewed .” In:Management Science .
We show that, in the presence of a risk\-free asset, the return distribution of every portfolio is determined by
its mean and variance if and only if asset returns follow a specific skew\-elliptical distribution. Thus, contrary
to common belief among academics and practitioners, skewed returns do not allow a rejection of mean\-variance
analysis. Our work differs from Chamberlain’s \[Chamberlain G (1983\) A characterization of the distributions
that imply mean\-variance utility functions. J. Econom. Theory 29(1\):185\-201\.] by focusing on the returns of
portfolios, where the weights over the risk\-free asset and the risky assets sum to unity. Furthermore, it extends
Meyer’s \[Meyer J, Rasche RH (1992\) Sufficient conditions for expected utility to imply mean\-standard deviation
rankings:Empirical evidenceconcerningthelocation andscalecondition. Econom. J. (London)102(410\):91\-106\.]
by introducing elliptical noise into their generalized location\-scale framework. To emphasize the relevance of our
skew\-elliptical model, we additionally provide empirical evidence that it cannot be rejected for the returns of
typical portfolios of common stocks or popular alternative investments.
Schumann, E. (2019\). “Backtesting .” In:SSRN e\-Print .
We discuss the backtesting of investment and trading strategies. We start with the challenges and pitfalls:
overfitting, data preparation, and the effects of randomness. Then, we introduce and describe R software for
backtesting. We demonstrate how to use the software for univariate and multivariate strategies (i.e. portfolio
strategies) for two equity data sets. Specifically, we discuss the implementation and testing of momentum and
portfolio optimization models. Throughout, we stress the analysis of sensitivity and robustness checks. Since
such analyses require to run many backtests, we also discuss how backtests can be run in parallel.
Schussler, R. A. (2019\). “Robust Dynamic Portfolio Choice Based on Out\-Of\-Sample Performance .” In:SSRN
e\-Print.
We introduce a novel dynamic portfolio choice method, focusing on robust out\-of\-sample performance rather
than on optimal in\-sample performance. We therefore devise a strategy that rigorously tackles the problem
of estimation error. The method involves defining a discrete set of single\-period portfolio allocation policies
(candidate portfolio strategies) that accommodate time\-varying predictability of individual assets and choosing
between them at portfolio revision dates based on bootstrapped out\-of\-sample portfolio returns. Our approach
can handle an extensive menu of important features, in particular, arbitrarily complex types of conditional
predictability, a large asset universe, parameter uncertainty, model uncertainty and downside risk aversion. We
demonstrate the method’s feasibility and usefulness in dynamic investment problems in futures trading, strategic
asset allocation and a cross\-sectional momentum strategy in equity markets.
Schwendner, P., Papenbrock, J., Jaeger, M., and Krugel, S. (2021\). “Adaptive Seriational Risk Parity and Other
Extensions for Heuristic Portfolio Construction Using Machine Learning and Graph Theory .” In:The Journal
of Financial Data Science 3(4\), pp. 65–83\.
In this article, the authors present a conceptual framework named adaptive seriational risk parity (ASRP) to ex\-
tendhierarchicalriskparity(HRP)asanassetallocationheuristic.ThefirststepofHRP(quasi\-diagonalization),
determining the hierarchy of assets, is required for the actual allocation done in the second step (recursive bisec\-
tioning). In the original HRP scheme, this hierarchy is found using single\-linkage hierarchical clustering of the
115correlation matrix, which is a static tree\-based method. The authors compare the performance of the standard
HRP with other static and adaptive tree\-based methods, as well as seriation\-based methods that do not rely
on trees. Seriation is a broader concept allowing reordering of the rows or columns of a matrix to best express
similarities between the elements. Each discussed variation leads to a different time series reflecting portfolio
performance using a 20\-year backtest of a multi\-asset futures universe. Unsupervised learningbased on these
time\-series creates a taxonomy that groups the strategies in high correspondence to the construction hierarchy
of the various types of ASRP. Performance analysis of the variations shows that most of the static tree\-based
alternatives to HRP outperform the single\-linkage clustering used in HRP on a risk\-adjusted basis. Adaptive
tree methods show mixed results, and most generic seriation\-based approaches underperform.
Senneret, M., Malevergne, Y., Abry, P., Perrin, G., and Jaffres, L. (2016\). “Covariance versus Precision Matrix
Estimation for Efficient Asset Allocation .” In:IEEE Journal of Selected Topics in Signal Processing 10(6\),
pp. 982–993\.
Asset allocation constitutes one of the most crucial and most challenging tasks in financial engineering, which
often requires the estimation of large covariance or precision matrices, from short time span multivariate ob\-
servations, a mandatory yet difficult step. The present contribution reviews and compares a large selection of
estimators for covariance and precision matrices, organized into classes of estimation principles (Direct, Factor,
Shrinkage, Sparsity). This includes the theoretical derivation of several additional estimators not available in the
literature. Rather than assessing estimation performance from synthetic data based on a priori selected models
of questionable practical interest, it is chosen here to evaluate practically the quality of these estimators directly
from portfolio selection performance, quantified by financial criteria. Portfolio selection is conducted over two
datasets of different natures: a 15\-year large subset (within Stoxx Europe 600\) of 244 European stock returns,
and a 50\-year benchmark dataset of 90 US equity portfolios. This large scale comparative study addresses issues
such as the relative benefits and difficulties of using robust versus direct estimates, of choosing precision or
covariance estimates, of quantifying the impacts of constraints.
Serbin,V.,Borkovec,M.,andChigirinskiy,M.(2011\). “RobustPortfolioRebalancingwithTransactionCostPenalty
an Empirical Analysis .” In:Journal of Investment Management .
The goal of this paper is to study and compare two popular techniques used by practitioners to reduce the
sensitivity of optimal portfolios to uncertainty in expected return for a typical portfolio optimization problem.
Specifically, we investigate whether including transaction costs into the optimization problems objective func\-
tion addresses the robustness issue.We weight this approach against the robust optimization method described
in Goldfarb and Iyengar (2003\). The latter directly incorporates the distribution of estimation errors in the
optimization problem and determines the optimal portfolio allocation by selecting the least favorable realization
of the expected returns in the investors uncertainty region.Our analysis focuses on the return maximization
problem with constraints on total risk or tracking error and a transaction cost penalty in the objective function.
We demonstrate that not only are the effects of incorporating a transaction cost penalty into the optimization
problem similar to those of modeling uncertainty in expected returns, but that there are also some interesting
differences. We offer some insights into the observed interplay between modeling transaction costs and modeling
return uncertainty.
Serur, J. A. and Avellaneda, M. (2021\). “Hierarchical PCA and Modeling Asset Correlations .” In:SSRN e\-Print .
Modeling cross\-sectional correlations between thousands of stocks, acrosscountries and industries, can be chal\-
lenging. In this paper, we demonstratethe advantages of using Hierarchical Principal Component Analysis
(HPCA)over the classic PCA. We also introduce a statistical clustering algorithmto identify homogeneous clus\-
ters of stocks or ”synthetic sectors”. We apply these methods to study cross\-sectional correlations in the US,
Europe, China,and Emerging Markets.
Seymour, A., Flint, E. J., and Chikurunhe, F. (2018\). “Dynamic portfolio management strategies: A framework for
historical analysis .” In:SSRN e\-Print .
The performance of dynamic trading and investment strategies can be difficult to predict. Although not without
its problems, analysis of the historical performance of a strategy can provide valuable insight into its general risk
andreturnproperties.Furthermore,historicalanalysisallowsonetocomparevariationsofastrategyandexamine
the impact of various parameter choices and implementation rules. Dynamic strategy applications in three areas
are considered, namely derivatives, asset allocation and equity factor portfolios. Firstly, the analysis of a strategy
involving single\-stock derivatives is examined in which call options on certain constituents of an index portfolio
are sold as an alternative method of under\-weighting the underlying. Secondly, the historical performance of an
optimization\-based asset allocation strategy is considered. The assumed aim of the strategy is to outperform a
116benchmark of CPI 5 via dynamic trading in a portfolio of domestic equities, bonds, property and cash, as well as
international equities and bonds. Finally, the effects of portfolio construction on factor performance are studied
via an historical analysis in which portfolios corresponding to a selection of fundamental factors are managed
according to a range of weighting schemes, rebalance frequencies and portfolio sizes.
Seymour, A. J., Chikurunhe, F., and Flint, E. J. (2014\). “Full\-Scale Optimization: A Flexible Framework for Hedge
Design.” In:SSRN e\-Print .
In this work we consider the application of expected utility optimization to the construction of an optimal hedge.
Utility theory provides a rich framework for decision\-making under uncertainty and features preferences specified
via a range of simple to possibly complex functions of future portfolio returns. Optimal hedge construction
examples are discussed in the context of downside protection for domestic equity, and the reduction of currency
exposure risk inherent in a foreign equity position. We also quantify the impact of currency derivatives on
the risk and return properties of a foreign equity holding. This is done by considering two types of preference
specification featuring loss aversion, namely kinked utility and S\-shaped utility. Both of these functions have
particular relevance for fund managers concerned with the value of a portfolio falling below that of a benchmark,
or a pension fund becoming underfunded at a certain point.
Shah, T. and Parikh, A. (2019\). “Does the number of holdings in a risk parity portfolio matter? ” In:Journal of
Asset Management 20, pp. 123–133\.
This empirical study is an endeavor to assess the impact of the number of securities in a risk parity portfolio
on its performance. The study focuses on performance analysis of fifty, seventy\-five and hundred stocks risk
parity portfolio for emerging markets and China the developed market USA. Alpha of the risk parity portfolio
has shown sensitivity to the change in the size as a number of holdings of the portfolio. The findings of this
empirical study reveal that seventy\-five stocks risk parity portfolio is in a sweet\-spot for the full sample time
period from Dec 2002 to Dec 2014\. It not only generates statistically significant superior alpha, but also achieves
a similar level of risk diversification as to fifty and hundred stocks portfolio. Testing of sub\-periods of the full
sample time period, which is coinciding with interest rate cycle, suggests that during the crucial period of
financial crisis of 2008, seventy\-five stocks portfolio shows the superior performance of alpha, Sharpe ratio and
Treynor ratio over fifty stocks and hundred stocks portfolio with a similar level of risk diversification. However,
the possibility of superior risk parity portfolio with a marginally higher or lower number than seventy\-five stock
portfolio cannot be denied.
Shaik, M. and Maheswaran, S. (2020\). “A new unbiased additive robust volatility estimation using extreme values
of asset prices .” In:Financial Markets and Portfolio Management 34(3\), pp. 313–347\.
We propose a new unbiased robust volatility estimator based on extreme values of asset prices. We show that
the proposed Add Extreme Value Robust Volatility Estimator (AEVRVE) is unbiased and is 2\-3 times more
efficient relative to the Classical Robust Volatility Estimator (CRVE). We put forth a novel procedure to remove
the downward bias present in the data even without increasing the number of steps in the stock price path. We
perform Monte Carlo simulation experimentsto showthe properties of unbiasedness and efficiency. The proposed
estimator remains exactly unbiased relative to the standard robust volatility estimator in the empirical data
based on global stock indices namely CAC 40, DOW, IBOVESPA, NIKKEI, S\&P 500 and SET 50\.
Shalett, L., Hunt, D., Ye, Z., and Wang, S. (2017\). Tax Efficiency: Getting to What You Need by Keeping More of
What You Earn . Tech. rep. Morgan Stanley Wealth Management.
Taxes are a substantial drag on investment returns that compound over time. Because of this, even small
reductions in tax costs can have enormous consequences for wealth accumulation. In an example drawn from
this report, an improvement of 0\.6% per year in aftertax returns resulted in a remaining wealth difference of 75%
after 30 years of distributions. At a time when interest rates are low, and conservative and balanced portfolios
don’t deliver the returns they once did, investors can often improve their progress toward their financial goals
by enhancing their tax efficiency. We outline strategies for doing so, ranging from the simple and commonly
used to the underutilized, less well\-known and more complex; evaluate each to ascertain its appropriateness for
different investors; and assess their potential impact on investors’ bottom lines.
Sheikh, A. Z. and Sun, J. (2012\). “Regime Change: Implications of Macroeconomic Shifts on Asset Class and
Portfolio Performance .” In:The Journal of Investing 21(3\), pp. 36–54\.
It is a well\-recognized empirical observation that different asset classes respond differently to different economic
drivers. It is also well recognized that asset class behavior can vary significantly over shifting economic scenarios.
This article builds on this empirical evidence to develop a quantitative framework for regime\-based asset alloca\-
tion. It investigates whether regime\-based investing can effectively respond to changes in economic regimes at the
117portfolio level in an effort to provide better long\-term results when compared to a more static approach. Results
indicate that it is both possible and practical to develop a regime\-based investing approach that can potentially
add value over time. Success depends on identifying key factors that influence asset class performance, and then
developing a way to model those non\-linear relationships. Regime\-based investing also requires a healthy degree
of economic forecasting skill, which need not be perfect to add value. Based on the authors’ analysis, regime
based investing can offer investors a compelling alternative to a more static approach.
Shin, D. W. (2018\). “Forecasting realized volatility: A review .” In:Journal of the Korean Statistical Society 47(4\),
pp. 395–404\.
Forecast methods for realized volatilities are reviewed. Basic theoretical and empirical features of realized volatil\-
itiesaswellasversionsofestimatorsofrealizedvolatilityarebrieflyinvestigated.Majorforecastmodelsfeaturing
the empirical aspects of persistency and asymmetry are discussed in terms of forecasting models for which the
heterogeneous autoregressive (HAR) model is one of the most basic one in the recent literature. Forecast meth\-
ods addressing the issues of jump, break, implied volatility, and market microstructure noise are reviewed.
Forecasting realized covariance matrix is also considered.
Shirota, Y. and Murakami, A. (2021\). “Long\-term Time Series Data Clustering of Stock Prices for Portfolio Selec\-
tion.” In:IEEE International Conference on Service Operations and Logistics, and Informatics (SOLI) . IEEE.
In this paper, clustering for stock data is conducted with two clustering methods, k\-Shape and k\-means with
DTW distance measure and the results are compared. The data is the top 129 global electronics manufactures’
stock prices from 2018 to 2020 which included the worst Christmas in 2018 and the beginning of COVID\-19
outbreak.TheinvolvedcountriesareUS,China,Taiwan,Korea,Japanandsomeothers.Theclusteringresultsby
k\-Shape indicate distinctively different effects on those countries’ stock markets due to the COVID\-19 turmoil.
The patterns of the clusters can be visualized to identify the differences among the clusters. We found that
each of eight clusters comprises of the same country companies. From that, we could guess that investors or
their algorithms tend to invest in companies according to its country rather than the individual company’s
performance.
Sialm, C. and Sosner, N. (2017\). “Taxes, Shorting, and Active Management .” In:Financial Analysts Journal 74(1\),
pp. 88–107\.
We examine the consequences of short selling in the context of quantitative investment strategies held by
individual investors in taxable accounts. Short positions not only allow investors to benefit from the anticipated
underperformance of securities but also create tax benefits because they enhance opportunities to time capital
gains realizations. Relaxing short\-selling constraints results in tax benefits because a portfolio’s long positions
tend to realize net long\-term capital gains taxed at relatively low rates, whereas short positions tend to realize
net short\-term capital losses, which can offset short\-term capital gains from other strategies in the investor’s
portfolio. Our results show that investment strategies that take advantage of short selling can generate superior
after\-tax performance by significantly reducing the tax burden.
Sialm, C. and Zhang, H. (2020\). “Tax\-Efficient Asset Management: Evidence from Equity Mutual Funds .” In:The
Journal of Finance 75(2\), pp. 735–777\.
We investigate the relation between tax burdens and mutual fund performance from both a theoretical and an
empirical perspective. The theoretical model introduces heterogeneous tax clienteles in an environment with
decreasing returns to scale and shows that the equilibrium performance of mutual funds depends on the size
of the tax clienteles. Our empirical results show that the performance of U.S. equity mutual funds is related
to their tax burdens. We find that tax\-efficient funds exhibit not only superior after\-tax performance, but also
superior before\-tax performance due to lower trading costs, favorable style exposures, and better selectivity.
Simaan, M., Simaan, Y., and Tang, Y. (2018\). “Estimation error in mean returns and the mean\-variance efficient
frontier.” In:International Review of Economics \& Finance 56, pp. 109–124\.
In this paper, we build estimation error in mean returns into the mean\-variance (MV) portfolio theory under
the assumption that returns on individual assets follow a joint normal distribution. We derive the conditional
sampling distribution of the MV portfolio along with its mean and risk return when the sample covariance
matrix is equal to the population covariance matrix. We use the mean squared error (MSE) to characterize
the effects of estimation error in mean returns on the joint sampling distributions and examine how such error
affects the risk\-return tradeoff of the MV portfolios. We show that the negative effects of error in mean returns
on the joint sampling distributions increase with the decision maker’s risk tolerance and the number of assets
in a portfolio, but decrease with the sample size.
Simoes, G. (2017\). “Robust portfolio optimisation with filtering uncertainty .” PhD thesis. University of Oxford.
118This thesis focuses on how portfolio optimisation can be carried out under different types of uncertainty, which
we often measure through the use of filters. Chapter 1 motivates the problem, gives an overview of the thesis
and covers some necessary background material. Chapter 2 deals with uncertainty in the covariance matrix and
how by identifying different regimes we can solve optimisation problems of interest to practitioners. Chapter 3
focuses on the uncertainty over tail events and how we can not only extract relevant information by filtering the
data but also how we can use that information to construct a portfolio optimisation problem that acts on it.
In Chapter 4 we address the lack of tractability for general relative robust portfolio optimisation problems and
how one can overcome this so as to make it a viable tool. Chapter 5 considers the problem of uncertainty in the
filter itself and how this uncertainty can be fully incorporated in the portfolio optimisation problem. Finally in
Chapter 6 we conclude and propose topics for future research.
Simoes, G., McDonald, M., Williams, S., Fenn, D., and Hauser, R. (2018\). “Relative Robust Portfolio Optimization
with benchmark regret .” In:Quantitative Finance 18(12\), pp. 1991–2003\.
WeextendRelativeRobustPortfolioOptimizationmodelstoallowportfoliostooptimizetheirperformancewhen
considered relative to a set of benchmarks. We do this in a minimum volatility setting, where we model regret
directly as the maximum difference between our volatility and that of a given benchmark. Portfolio managers are
also given the option of computing regret as a proportion of the benchmark performance, which is more in line
with market practice than other approaches suggested in the literature. Furthermore, we propose using regret
as an extra constraint rather than as a brand new objective function, so practitioners can maintain their current
framework. We also look into how such a triple optimization problem can be solved or at least approximated for
a general class of objective functions and uncertainty and benchmark sets. Finally, we illustrate the benefits of
this approach by examining its performance against other common methods in the literature in several equity
markets.
Simon, P. M. and Turkay, C. (2018\). “Hunting high and low: visualising shifting correlations in financial markets .”
In:Computer Graphics Forum 37(3\), pp. 479–490\.
The analysis of financial assets’ correlations is fundamental to many aspects of finance theory and practice,
especially modern portfolio theory and the study of risk. In order to manage investment risk, in\-depth analysis
of changing correlations is needed, with both high and low correlations between financial assets (and groups
thereof) important to identify. In this paper, we propose a visual analytics framework for the interactive analysis
of relations and structures in dynamic, high\-dimensional correlation data. We conduct a series of interviews and
review the financial correlation analysis literature to guide our design. Our solution combines concepts from
multi\-dimensional scaling, weighted complete graphs and threshold networks to present interactive, animated
displays which use proximity as a visual metaphor for correlation and animation stability to encode correlation
stability. We devise interaction techniques coupled with context\-sensitive auxiliary views to support the analysis
of subsets of correlation networks. As part of our contribution, we also present behaviour profiles to help guide
future users of our approach. We evaluate our approach by checking the validity of the layouts produced, present\-
ing a number of analysis stories, and through a user study. We observe that our solutions help unravel complex
behaviours and resonate well with study participants in addressing their needs in the context of correlation
analysis in finance.
Simonian, J. (2021\). “Causal Uncertainty in Capital Markets: A Robust Noisy\-Or Framework for Portfolio Man\-
agement.” In:The Journal of Financial Data Science 3(1\), pp. 43–55\.
Understanding the causal relations that drive markets is integral to both explaining past events and predicting
future developments. Although there are various theories of economic causality, there has not yet been a wide
adoption of machine learning\-inspired causal frameworks within economics and finance. Causal networks are
among the latter and provide one of the most transparent and practical models for representing the relationships
between economic causes and effects that are relevant for making investment decisions. Among the various
approaches to causal networks, the noisy\-or model stands out because it provides the formal means to simplify
the calculation of the cumulative impact of more than one cause on an effect. One of the implicit assumptions of
the noisy\-or model is that the causal probability values posited by model builders are completely reliable. This
assumption is unrealistic, however, especially in financial applications in which beliefs about market events are
generally supported by significantly less data relative to beliefs about natural phenomena. Moreover, aside from
the need to evaluate the reliability of individual beliefs, portfolio managers presumably also need to assess the
investment processes that produce those beliefs. To address the foregoing challenges, in this article, a formal,
logic\-based framework to produce robust, uncertainty\-adjusted causal probability assignments within the noisy\-
or model is proposed. The robust noisy\-or framework described provides both a technical enhancement of the
119basicnoisy\-ormodelandapracticalsolutionforaddressingthechallengeposedbythevaryingqualityofevidence
that supports most investment decisions.
Simonian, J. and Wu, C. (2019\). “Minsky vs. Machine: New Foundations for Quant\-Macro Investing .” In:The
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
Singh, A. (2018\). “Bayesian Dynamic Interactions and Predictions: U.S., BRIC, and Frontier Equity Markets .” In:
The Journal of Wealth Management 20(4\), pp. 96–109\.
This study attempts to highlight short\-run dynamic interactions (return spillover effects) and predictions among
the U.S. and other developing economies, that is, BRIC and frontier equity markets, by employing a Bayesian
VAR framework along with its branches. The findings report the existence of spillover effects among the equity
markets, whereby the contribution of the U.S. equity market in explaining forecasted error variances increases
over a period of time in the BRIC and frontier equity markets. Considerable cross\-market variance effects
are recorded among the U.S., BRIC, and frontier equity markets. The out\-of\-sample forecasted values point
toward optimism in the markets in the coming one year. All these findings have strong implications for market
participants regarding portfolio management and asset allocation decisions.
Sironi, P. (2015\). Modern Portfolio Management: from Markowitz to Probabilistic Scenario Optimisation . Risk
Books. 204 pp.
Modern Portfolio Management provides a methodology for portfolio choice based upon modern risk management
techniques and a clearer definition of the investment risk/return profile to feature goal\-based investing and
probabilistic scenario optimisation. The financial markets have undergone a period of distress that has strained
the trusted relationship between investors and financial advisors; new regulation has been forged to push for
higher levels of transparency and risk\-based communication as part of investment decision\-making. This has
ignited the quest for better portfolio optimisation techniques that can combine the added\-value asymmetry of
real products (as they strongly contributed to pre\-crisis budgets) with the life\-cycle requirements of investors,
supported by intuitive graphical representation of seemingly complex mathematical relationships between real
portfolios and products as required by regulation. Upon reading Modern Portfolio Management, readers will
understand the importance of simulating real securities (especially fixed income and structured products) during
themakingofoptimalportfolios,aswellastheimportanceofsimulatingfinancialinvestmentsovertimetomatch
in a transparent way actual goals and constraints instead of relying solely upon past performance or personal
judgement.
Sjostrand, D. and Behnejad, N. (2020\). “Exploration of Hierarchical Clustering in Long\-only Risk\-based Portfolio
Optimization .” MA thesis. Copenhagen Business School.
Modern portfolio optimization methods have introduced new ways of allocating capital and have drawn the
attention of scholars, practitioners, and the general public alike. The thesis aims to add to the empirical ev\-
idence on the impact and risk\-based performance of hierarchical clustering portfolios in long\-only risk\-based
portfolio optimization. This is achieved by analyzing and investigating the Hierarchical Risk Parity, Hierarchical
Equal Risk Contribution, and Nested Clustered Optimization methods, and compare these from a risk\-based
perspective to several traditional optimization methods. The relative risk\-based performance is assessed through
Monte Carlo simulations using synthetic data as well as through a walk\-forward backtest applied on historical
S\&P 500 data. Together, the methodology provides a broad view of the general performance, but also more
focused insights into potential estimation error reduction and the impact of different clustering parameters. The
combined empirical results do not provide conclusive support for any general performance gains from hierarchi\-
cal clustering in portfolio optimization. The initial positive effects found in earlier studies for Nested Clustered
120Optimization are hypothesized to stem from the highly stylized and simplified assumptions applied. The re\-
sults given in this thesis suggest that these initial positive effects diminish when applied to more realistic data.
Furthermore, the results for Hierarchical Risk Parity and Hierarchical Equal Risk Contribution show results
in line with previous studies by Raffinot (2018\). It is concluded that they are performing reasonably well but
underperform in comparison to several of the traditional portfolios on most risk\-based performance dimensions
included. The findings do not indicate any general increase in risk\-based performance, but do, however, show
promise in providing more control over the weight concentration. In conclusion, the authors find that clustering
indicates some promising aspects, but that these are limited given the applied hierarchical methodology, and
further research is warranted to reach more conclusive answers.
Skallsjo, S. R. (2019\). “Simple formulas for portfolio rebalancing rules .” In:SSRN e\-Print .
Portfolio rebalancing rules are used by large scale asset managers to manage a trade\-off between frequent
rebalancing on one hand, and a cost of deviating from the portfolio benchmark on the other. This note con\-
tributes to the design of such policies in two ways. First, it clarifies the analytical framework, by showing how
the rebalancing problem can be formulated in a standard model for asset management. Although this step is
straightforward, it is important as it makes a clear distinction between a risk factor and a risk factor exposure.
Keeping this distinction facilitates the design of the optimal policy.Second, for a given policy the note provides
closed form expressions for certain statistical quantities relevant for the policy design. These include average
rebalancing frequency, average annual transaction amount, mean square deviation from benchmark, and mean
absolute deviation from benchmark. The resulting formulas are simple arithmetic expressions, easy to interpret
and straightforward to implement.
Snow, D. (2020\). “Machine Learning in Asset Management \- Part 2: Portfolio Construction \- Weight Optimization .”
In:The Journal of Financial Data Science 2 (2\), pp. 17–24\.
This is the second in a series of articles dealing with machine learning in asset management. This article focuses
on portfolio weighting using machine learning. Following from the previous article (Snow 2020\), which looked at
trading strategies, this article identifies different weight optimization methods for supervised, unsupervised, and
reinforcement learning frameworks. In total, seven submethods are summarized, with the code made available
for further exploration.
Sokolov, V. and Polson, M. (2019\). “Strategic Bayesian Asset Allocation .” In:arXiv e\-Print .
Strategic asset allocation requires an investor to select stocks from a given basket of assets. Bayesian regulariza\-
tion is shown to not only provide stock selection but also optimal sequential portfolio weights. The perspective
of the investor is to maximize alpha risk\-adjusted returns relative to a benchmark index. Incorporating investor
preferences with regularization is related to the approach of Black (1992\) and Puelz (2015\). Tailored MCMC
algorithms are developed to calculate portfolio weights and perform selection. We illustrate our methodology
with an application to stock selection from the SP100, and the top fifty holdings of Renaissance Technologies
and Viking Global hedge fund portfolios. Finally, we conclude with directions for future research.
Sosner, N. and Krasner, S. (2020\). “Tax\-Efficient Portfolio Transition: A Tax\-Aware Relaxed\-Constraint Approach
to Switching Equity Managers .” In:SSRN e\-Print .
For a taxable investor with a highly appreciated equity portfolio, replacing the portfolio manager is likely
to trigger substantial tax liabilities. We focus on transitioning an appreciated equity portfolio to an actively
managed strategy. We compare transition from an appreciated portfolio to a traditional long\-only tax\-agnostic
equitystrategywithtransitiontoequitystrategiesutilizingmoreadvancedportfoliomanagementtechniquessuch
as tax\-aware rebalancing and relaxed\-constraint portfolio construction. We find that transition to a tax\-aware
relaxed\-constraint strategy results in both high implementation efficiency and tax efficiency both during and
after the transition. As a result, a tax\-aware relaxed\-constraint post\-transition strategy significantly outperforms
a traditional tax\-agnostic long\-only strategy in its ability to preserve and grow the investors after\-tax wealth
over the long term. We also discuss risks and limitations of the tax\-aware relaxed\-constraint approach.
Sosner, N., Krasner, S., and Pyne, T. (2019\). “The Tax Benefits of Relaxing the Long\-Only Constraint: Do They
Come from Character or Deferral? ” In:The Journal of Wealth Management 21(4\), pp. 10–31\.
In this study, we propose a decomposition of the total tax benefit (or liability) of a strategy into what we define
as character and deferral components. Our decomposition is mathematically straightforward and intuitive, and
it allows for a quick and informative assessment of tax benefits of different tax\-aware strategies without modeling
various investor\-specific situations. We use this character\-deferral decomposition to identify the source of tax
benefits resulting from relaxation of the long\-only constraint. Our empirical evidence shows that, for tax\-aware
strategies, relaxing the long\-only constraint results in a drastic increase in their tax benefits, in particular
121owing to an increase in the character benefit. We conclude that tax\-aware relaxed\-constraint strategies are more
attractive to taxable investors than their long\-only counterparts.
Sosner, N., Sullivan, R., and Urrutia, L. (2018\). “Multi\-Period After\-Tax Reporting: A Practical Solution .” In:The
Journal of Wealth Management 21(3\), pp. 11–25\.
After\-tax performance reporting is critical for taxable investors but is unfortunately often overlooked due, in
part, to its complexity and lack of offerings in the space. Instead, most performance reporting models available
today provide only pre\-tax reporting, ignoring the after\-tax aspects so relevant for taxable investors. In this
article, the authors seek to resolve this issue by proposing an effective and workable after\-tax performance
report aimed at enhancing wealth preservation and accumulation for taxable investors. They also outline and
offer justification for the various choices that are made in their report in the hope that others will not only adopt
their proposed solution, but also review, comment, and improve on it.
Stagnol, L. (2017\). “The Risk Parity Principle Applied to a Corporate Bond Index .” In:The Journal of Fixed Income
27(1\), pp. 27–48\.
In this paper, we apply the principle of risk parity to a corporate bond index, an asset class so far left behind in
this literature. Specifically, we rely on the Duration Times Spread (DTS), a coherent metric for bond credit risk.
Weconstruct indexesbased onsector, issuer, and bondlevel,usingstructured blockcorrelationmatrixes, weights
being inversely proportional to DTS. Our results provide evidence that applying an Equal Risk Contribution
(ERC)principleusingDTSintheindexdesignsignificantlyimprovescorporatebondindexrisk\-adjustedreturns.
It appears that the higher the granularity, the higher the risk\-adjusted performance enhancements will be. More
generally, the ERC application we present seems to be a valuable tradeoff between heuristic and more complex
risk\-modeling based weighting schemes.
Stein, D. M. and Garland, J. P. (2008\). “Investment Management for Taxable Investors .” In:Handbook of Finance:
Volume II. Investment Management and Finance Management . Wiley.
Much of the practice of investment management has evolved to suit the needs of tax\-exempt institutional pension
funds. There is an increasing realization, however, that many practices suitable for tax\-exempt investing need to
bemodifiedfortaxableinvesting.Taxesmatteragreatdeal.Taxesrepresentaverylargeperformancedrag,often
larger than transaction costs, management fees, or inflation. The popular sentiment is that investors should not
allow their investment decisions to be dominated by tax considerations. While it is true that tax considerations
should not dominate investment decisions, tax considerations do significantly influence investment returns, and
investors would be well advised to consider taxes in their investment decisions. Failing to do so can be expensive,
particularly if investors allow taxes to erode their returns over the long term.
Stivers, C. and Sun, L. (2016\). “Mitigating Estimation Risk in Asset Allocation: Diagonal Models Versus 1/N
Diversification .” In:Financial Review 51(3\), pp. 403–433\.
Recentliterature suggests that optimal asset\-allocationmodels struggle to consistentlyoutperformthe 1/N naive
diversification strategy, which highlights estimation\-risk concerns. We propose a dichotomous classification of
asset\-allocation models based on which elements of the inverse covariance matrix that a model uses: diagonal
only versus full matrix. We argue that parsimonious diagonal\-only strategies, which use limited information
such as volatility or idiosyncratic volatility, are likely to offer a good tradeoff between incorporating limited
information while mitigating estimation risk. Evaluating five sets of portfolios over 1926\-2012, we find that 1/N
is generally not optimal when compared with these diagonal strategies.
Su, J.\-B. (2020\). “The Implementation of Asset Allocation Approaches: Theory and Evidence .” In:Sustainability
12(17\), p. 7162\.
This study develops three capital allocation approaches and a directional weight increment algorithm to identify
the efficient frontier of all possible multi\-asset portfolios precisely and rapidly. Subsequently, this study proposes
an asset selection criterion, based on the coefficient of variance and volatility risk measures, to perform the
asset allocation for two types of investors who are willing or not willing to bear the risk. Finally, this study
uses a multivariate generalized autoregressive conditional heteroskedasticity (GARCH) model to estimate the
conditional variance and covariance of several multi\-asset portfolios constituted of seven assets dispersed in the
oil, stock, and currency markets of the US. The empirical results show that, via applying the proposed asset
selection criterion, the most suitable multi\-asset portfolios are the SP500\-Nasdaq and the GasNyh\-DJ, which
belong to the relatively most efficient portfolios. Moreover, two capital allocation approaches using the entire
sample weight forecasts have the best forecast performance. Additionally, for all multi\-asset portfolios the weight
combination set of portfolios on the efficient frontier that resulted from the proposed algorithm is consistent
with that obtained from the traditional approach.
122Su, W. (2021\). “Volatility of S\&P500: Estimation and Evaluation .” In:arXiv e\-Print .
In an era when derivatives is getting popular, risk management has gradually become the core content of modern
finance. In order to study how to accurately estimate the volatility of the S\&P 500 index, after introducing the
theoretical background of several methods, this paper uses the historical volatility method, GARCH model
method and implied volatility method to estimate the real volatility respectively. At the same time, two ways
of adjusting the estimation window, rolling and increasing, are also considered. The unbiased test and goodness
of fit test are used to evaluate these methods. The empirical result shows that the implied volatility is the
best estimator of the real volatility. The rolling estimation window is recommended when using the historical
volatility. On the contrary, the estimation window is supposed to be increased when using the GARCH model.
Subekti,R.,Sari,E.R.,andKusumawati,R.(2019\). “CombiningBlack\-Littermanmodelwithclusteringonportfolio
construction .” In:Journal of Physics: Conference Series 1321, p. 022051\.
This research aims to propose a new strategy for an investor when using Black Litterman Model (BLM) in order
to gain higher performance on their portfolio. The proposed strategy is starting to cluster stocks then combine
it with allocation weight following the Black\-Litterman rules. We describe two scenarios combination cluster
and BLM in the processing of portfolio construction then we investigate both performances measured with the
Sharpe index. In this research, we limited for expressing views which only use absolute views. We find that
a result from combining the cluster technique will help investors to determine which assets that will be given
certain views on their portfolio.
Suhonen, A., Lennkh, M., and Perez, F. (2017\). “Quantifying Backtest Overfitting in Alternative Beta Strategies .”
In:The Journal of Portfolio Management 43 (2\), pp. 90–104\.
The authors investigate the biases in the backtested performance of ”alternative beta”strategies using a unique
sample of 215 trading strategies developed and promoted by global investment banks. Their results lend support
to the cautions in the recent literature regarding backtest overfitting and lack of robustness in trading strategy
performance during the ”live”period (out of sample). The authors report a median 73 percent deterioration
in Sharpe ratios between backtested and live performance periods for the strategies, and they establish a link
between performance deterioration and strategy complexity, with the realized reduction in live versus back\-
tested Sharpe ratios of the most complex strategies exceeding those of the simplest ones by over 30 percentage
points. The robustness of strategy exposure to risk factors varies between asset classes and strategies; it appears
reasonable in equity volatility and FX carry strategies but quite weak in the equity value strategy in particular.
Sun, R., Ma, T., Liu, S., and Sathye, M. (2019\). “Improved covariance matrix estimation for portfolio risk measure\-
ment: A review .” In:Journal of Risk and Financial Management 12(1\), p. 48\.
The literature on portfolio selection and risk measurement has considerably advanced in recent years. The aim
of the present paper is to trace the development of the literature and identify areas that require further research.
This paper provides a literature review of the characteristics of financial data, commonly used models of portfolio
selection, and portfolio risk measurement. In the summary of the characteristics of financial data, we summarize
the literature on fat tail and dependence characteristic of financial data. In the portfolio selection model part,
we cover three models: mean\-variance model, global minimum variance (GMV) model and factor model. In the
portfolio risk measurement part, we first classify risk measurement methods into two categories: moment\-based
risk measurement and moment\-based and quantile\-based risk measurement. Moment\-based risk measurement
includes time\-varying covariance matrix and shrinkage estimation, while moment\-based and quantile\-based risk
measurement includes semi\-variance, VaR and CVaR.
Supandi, E. D., Rosadi, D., and Abdurakhman (2017\). “An empirical comparison between robust estimation and ro\-
bust optimization to mean\-variance portfolio .” In:Journal of Modern Applied Statistical Methods 16(1\), pp. 589–
611\.
Mean\-variance portfolios constructed using the sample mean and covariance matrix of asset returns perform
poorly out\-of\-sample due to estimation error. Recently, there are two approaches designed to reduce the effect
of estimation error: robust statistics and robust optimization. Two different robust portfolios were examined by
assessing the out\-of\-sample performance and the stability of optimal portfolio compositions. The performance of
the proposed robust portfolios was compared to classical portfolios via expected return, risk, and Sharpe Ratio.
The aim is to shed light on the debate concerning the importance of the estimation error and weights stability
in the portfolio allocation problem, and the potential benefits coming from robust strategies in comparison to
classical portfolios.
Taljaard, B. H. and Maré, E. (2021\). “Why has the equal weight portfolio underperformed and what can we do
about it? ” In:Quantitative Finance 21(11\), pp. 1855–1868\.
123It is widely noted that market capitalisation weighted portfolios are inefficient and underperform an equal
weighted portfolio over the long\-term. However, at least since 2016, an equal weighted portfolio of stocks in
the S\&P500 has significantly underperformed the market capitalisation weighted portfolio. In this paper, we
analyse this underperformance using stochastic portfolio theory. We show that the equal weighted portfolio
does appear to outperform the market capitalisation weighted portfolio over the long\-term but with periods of
significant short\-term underperformance. In addition, we find that concentration in the market capitalisation
weighted portfolio has increased in recent years and has contributed to the recent underperformance together
with a significantly lower level of diversification benefits. Furthermore, we highlight an approach to improve the
performance of a portfolio by dynamically selecting a market cap or an equal weighting using a rudimentary
linear regression model.
Taljaard, B. and Mare, E. (2019\). “Too Much Rebalancing Is Not a Good Thing .” In:SSRN e\-Print .
Thereisnowanabundanceofliteratureshowingthattheequalweightedportfoliooutperformsthevalueweighted
portfolio. However, this has led to claims that the act of rebalancing itself within an equal weight strategy is
what leads to outperformance, whether or not individual security returns are mean\-reverting. In this paper we
show that you can achieve the same, if not better, returns than that of the equal weighted portfolio rebalanced
monthlybyrebalancinglessthanhalfofthetime.Thisisachievedbyconsideringonlywhetherthediversification
benefit is increasing or decreasing over some period of time.
Tayali, S. T. (2020\). “A novel backtesting methodology for clustering in mean–variance portfolio optimization .” In:
Knowledge\-Based Systems 209, p. 106454\.
The decisions of asset selection and allocation lie at the heart of financial portfolio management. For these
challenging tasks, the mathematical programming model of the mean\-variance optimization problem proposes
to use the concept of diversification. The novel methodology in this article is a representation of the accumulated
knowledge of this model from the modern portfolio theory. It is a practical application for portfolio managers
to help synthesize the available historical data and to infer rational decisions. The state\-of\-the\-art backtesting
methodology integrates the unsupervised machine learning method of clustering analysis into the mean\-variance
portfolio optimization model. The test results from the proposed novel methodology show that clustering with
Euclidean distance measures outperform the results of the benchmark and other specified clustering methods
for different datasets, backtesting periods, and temporal scales of major stock indices.
Tchernister, A. and Rubisov, D. (2009\). “Robust estimation of historical volatility and correlations in risk manage\-
ment.” In:Quantitative Finance 9(1\), pp. 43–54\.
Financial time series have two features which, in many cases, prevent the use of conventional estimators of
volatilitiesandcorrelations:leptokurtoticdistributionsandcontaminationofdatawithoutliers.Othertechniques
are required to achieve stable and accurate results. In this paper, we review robust estimators for volatilities
and correlations and identify those best suited for use in risk management. The selection criteria were that
the estimator should be stable to both fractionally small departures for all data points (fat tails), and to
fractionally large departures for a small number of data points (outliers). Since risk management typically deals
with thousands of time series at once, another major requirement was the independence of the approach of any
manual correction or data pre\-processing. We recommend using volatility t\-estimators, for which we derived the
estimation error formula for the case when the exact shape of the data distribution is unknown. A convenient
robust estimator for correlations is Kendall’s tau, whose drawback is that it does not guarantee the positivity
of the correlation matrix. We chose to use geometric optimization that overcomes this problem by finding the
closest correlation matrix to a given matrix in terms of the Hadamard norm. We propose the weights for the
norm and demonstrate the efficiency of the algorithm on large\-scale problems.
Tola, V., Lillo, F., Gallegati, M., and Mantegna, R. N. (2008\). “Cluster analysis for portfolio optimization .” In:
Journal of Economic Dynamics and Control 32(1\), pp. 235–258\.
We consider the problem of the statistical uncertainty of the correlation matrix in the optimization of a financial
portfolio. By assuming idealized conditions of perfect forecast ability for the future return and volatility of stocks
and short selling, we show that the use of clustering algorithms can improve the reliability of the portfolio in
terms of the ratio between predicted and realized risk. Bootstrap analysis indicates that this improvement is
obtained in a wide range of the parameters N (number of assets) and T (investment horizon). The predicted
and realized risk level and the relative portfolio composition of the selected portfolio for a given value of the
portfolio return are also investigated for each considered filtering method. We also show that several of the
results obtained by assuming idealized conditions are still observed under the more realistic assumptions of no
short selling and mean return and volatility forecasting based on historical data.
124Toma, A. and Leoni\-Aubin, S. (2015\). “Robust Portfolio Optimization Using Pseudodistances .” In:PLoS ONE
10(10\), e0140546\+.
The presence of outliers in financial asset returns is a frequently occurring phenomenon which may lead to
unreliable mean\-variance optimized portfolios. This fact is due to the unbounded influence that outliers can
have on the mean returns and covariance estimators that are inputs in the optimization procedure. In this paper
we present robust estimators of mean and covariance matrix obtained by minimizing an empirical version of
a pseudodistance between the assumed model and the true model underlying the data. We prove and discuss
theoretical properties of these estimators, such as affine equivariance, B\-robustness, asymptotic normality and
asymptotic relative efficiency. These estimators can be easily used in place of the classical estimators, thereby
providing robust optimized portfolios. A Monte Carlo simulation study and applications to real data show the
advantages of the proposed approach. We study both in\-sample and out\-of\-sample performance of the proposed
robust portfolios comparing them with some other portfolios known in literature.
Tong, J., Yang, J., Xi, J., Yu, Y., and Ogunbona, P. O. (2019\). “Tuning the Parameters for Precision Matrix
Estimation Using Regression Analysis .” In:IEEE Access 7, pp. 90585–90596\.
Precision matrix, i.e., inverse covariance matrix, is widely used in signal processing, and often estimated from
trainingsamples.Regularizationtechniques,suchasbandingandrankreduction,canbeappliedtothecovariance
matrix or precision matrix estimation for improving the estimation accuracy when the training samples are
limited. In this paper, exploiting regression interpretations of the precision matrix, we introduce two data\-driven,
distribution\-free methods to tune the parameter for regularized precision matrix estimation. The numerical
examples are provided to demonstrate the effectiveness of the proposed methods and example applications in
the design of minimum mean squared error (MMSE) channel estimators for large\-scale multiple\-input multiple\-
output (MIMO) communication systems are demonstrated.
Traccucci, P., Dumontier, L., Garchery, G., and Jacot, B. (2019\). “A Triptych Approach for Reverse Stress Testing
of Complex Portfolios .” In:Risk (Cutting Edge) .
Pascal Traccucci, Luc Dumontier, Guillaume Garchery and Benjamin Jacot present an extended reverse stress
test (ERST) triptych approach with three variables: level of plausibility, level of loss and scenario. Any two of
these variables can be derived, provided the third is given as input. A new version of the Levenberg\-Marquardt
optimisation algorithm is introduced to derive the ERST in certain complex cases.
Tran, T., Nguyen, N., Nguyen, T., and Mai, A. (2020\). “Voting shrinkage algorithm for Covariance Matrix Estima\-
tion and its application to portfolio selection .” In:RIVF International Conference on Computing and Commu\-
nication Technologies (RIVF) . IEEE.
Reducing errors of covariance matrix estimation plays a very important role in many optimization problems,
e.g., portfolio optimization. In this paper we propose a data\-driven approach which basically combines the
original framework of a popular approach named shrinkage estimation and cross\-validation technique to adapt
the shrinkage intensity with different levels of uncertainty of real data. Particularly, this approach can be applied
well to asset management to enhance the quality of portfolio selection which is known as a huge area of research
in modern portfolio theory. Experimental results carried out using the prices and volumes data of the Vietnamese
stock market show that our proposed method can practically improve the quality and robustness of portfolio
selection. Last but not least, we introduce an automatic backtesting system that can help us evaluate the
portfolio based on various financial indicators in a real\-time manner.
Trucios, C., Hotta, L. K., and Valls Pereira, P. L. (2019\). “On the robustness of the principal volatility components .”
In:Journal of Empirical Finance 52, pp. 201–219\.
Abstract In this paper, we analyse the recent principal volatility components analysis procedure. The procedure
overcomes several difficulties in modelling and forecasting the conditional covariance matrix in large dimensions
arising from the curse of dimensionality. We show that outliers have a devastating effect on the construction of
the principal volatility components and on the forecast of the conditional covariance matrix and consequently
in economic and financial applications based on this forecast. We propose a robust procedure and analyse its
finite sample properties by means of Monte Carlo experiments and also illustrate it using empirical data. The
robust procedure outperforms the classical method in simulated and empirical data.
Tuck, J., Barratt, S., and Boyd, S. (2021\). “Portfolio Construction Using Stratified Models .” In:arXiv e\-Print .
In this paper we develop models of asset return mean and covariance that depend on some observable market
conditions,andusethesetoconstructatradingpolicythatdependsontheseconditions,andthecurrentportfolio
holdings. After discretizing the market conditions, we fit Laplacian regularized stratified models for the return
mean and covariance. These models have a different mean and covariance for each market condition, but are
125regularized so that nearby market conditions have similar models. This technique allows us to fit models for
market conditions that have not occurred in the training data, by borrowing strength from nearby market
conditions for which we do have data. These models are combined with a Markowitz\-inspired optimization
method to yield a trading policy that is based on market conditions. We illustrate our method on a small
universe of 18 ETFs, using four well known and publicly available market variables to construct 10000 market
conditions, and show that it performs well out of sample. The method, however, is general, and scales to much
larger problems, that presumably would use proprietary data sources and forecasts along with publicly available
data.
Turvey, P. A., Basu, A. K., and Verhoeven, P. (2013\). “Embedded Tax Liabilities and Portfolio Choice .” In:The
Journal of Portfolio Management 39(3\), pp. 93–101\.
Taxes play an important role in determining after\-tax investment risk and returns, but many practitioners still
make investment decisions based on pre\-tax values. The apparent complexity of dealing with deferred capital
gains and the question of how these implied future tax liabilities should be valued are central to this problem.
The authors use a simple arbitrage argument to show that a risk\-free discount rate is appropriate for calculating
the present value of future tax liabilities. This lets analysts adjust risk and returns for effective tax rates and
present a more accurate picture to the investor. The results show a taxation\-induced preference for holding
equities over bonds and a location preference for holding equities in a taxable account and bonds in retirement
accounts. These important findings contrast with traditional investment advice that suggests a greater capacity
for risk in retirement accounts.
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
Furthermore, we introduce a novel asset selection property with stochastic gates that protects the risk budgeting
portfolio against the unprofitable assets.
Valentine, K. D., Buchanan, E. M., Scofield, J. E., and Beauchamp, M. T. (2019\). “Beyond p values: utilizing
multiple methods to evaluate evidence .” In:Behaviormetrika 46(1\), pp. 121–144\.
126Null hypothesis significance testing is cited as a threat to validity and reproducibility. While many individuals
suggest that we focus on altering the p value at which we deem an effect significant, we believe this suggestion
is short\-sighted. Alternative procedures (i.e., Bayesian analyses and observation\-oriented modeling: OOM) can
be more powerful and meaningful to our discipline. However, these methodologies are less frequently utilized
and are rarely discussed in combination with NHST. Herein, we discuss three methodologies (NHST, Bayesian
Model comparison, and OOM), then compare the possible interpretations of three analyses (ANOVA, Bayes
Factor, and an Ordinal Pattern Analysis) in various data environments using a frequentist simulation study.
We found that changing significance thresholds had little effect on conclusions. Furthermore, we suggest that
evaluating multiple estimates as evidence of an effect allows for more robust and nuanced interpretations of
results and implies the need to redefine evidentiary value and reporting practices. Recent events in psychological
sciencehavepromptedconcernswithinthedisciplineregardingresearchpracticesandultimately,thevalidityand
reproducibility of published reports (Etz and Vandekerckhove 2016; Lindsay 2015, Open Science Collaboration
2015; van Elk et al. 2015\). One often discussed matter is over\-reliance, abuse, and potential hacking of p values
produced by frequentist null hypothesis significance testing (NHST), as well as misinterpretations of NHST
results (Gigerenzer 2004; Ioannidis 2005; Simmons et al. 2011\). We agree with these concerns and believe that
many before us have voiced sound, generally accepted opinions on potential remedies, such as an increased focus
on effect sizes (Cumming 2008; Lakens 2013; Maxwell et al. 2015; Nosek et al. 2012\). However, other suggestions
have been met with less enthusiasm, including an article by Benjamin et al. (2018\) advocating that researchers
should begin thinking only of p values less than .005 as ”statistically significant”, thus changing alpha levels
to control Type I error rates. Alternatively, Pericchi and Pereira (2016\) promote the use of fluctuating alpha
levels as a function of sample size to assist with these errors. Trafimow et al. (2018\) critiques this suggestion to
broadly lower the alpha level to .005 and suggested that findings should be weighted on the basis of evidence
accumulation from multiple studies. We argue that alpha should not be the sole focus of our attention, but
rather, we should wonder if a p value should be utilized at all, and, if so, what that p value can tell us
in relation with other indicators. While NHST and p values may have merit, researchers have a wealth of
other statistical tools available to them. We believe that improvements may be made to the sciences as a
whole when individuals become aware of these tools and how these methods may be used, either alone or in
combination, to strengthen understanding of data and conclusions. These sentiments have been shared by the
American Statistical Association who recently held a conference focusing on going beyond NHST, expanding
their previous stance on p values (Wasserstein and Lazar 2016\). Therefore, the main goal of this project was
to show researchers how two alternative paradigms compare to NHST in terms of their methodological design,
statistical interpretations, and comparative robustness. Herein, we will discuss the following methodologies:
NHST, Bayes factor comparisons, and observation\-oriented modeling. To compare their methodological designs,
we first provide historical backgrounds, procedural steps, and limitations for each paradigm. We then simulated
data using a three timepoint repeated measures design with a Likert\-type scale as the outcome variable to be
able to compare the statistical interpretations and comparative robustness. By simulating possible data sets
and analyzing them with each of the three paradigms, we will be able to discuss the conclusions these three
methods reach given the same data and to compare how often these methodologies agree within different data
environments (i.e., given varying sample sizes and effect sizes). Beyond simply comparing methodologies, we also
sought to identify how changing the alpha criteria within the NHST framework may alter conclusions. Although
previous work has already compared Frequentist NHST to Bayesian approaches (Goodman 1999; Rouder et
al. 2012; Wetzels et al. 2011\), this manuscript adds a novel contribution: observation\-oriented modeling. By
introducing social scientists to observation\-oriented modeling (OOM), a relatively new paradigm that is readily
interpretable, we will show both how useful this paradigm can be in these contexts, and how it compares to two
well\-known methods. We hope that by discussing these methodologies in terms of a simple statistical analysis
researchers will be able to easily compare and contrast methodologies.
Vamvakas,O.G.(2015\). “Fixedincomeportfolioconstruction:aBayesianapproachfortheallocationofriskfactors .”
PhD thesis. City University London.
Active portfolio management is driven by the trade\-off between the expected return and the associated risks.
In light of the most recent extensions of Black\-Litterman model, we stick to a Bayesian approach for the
construction of active fixed income portfolios. Within the investment grade universe, the equilibrium returns are
approximated by the yield levels implied by the market prices and these are blended together with investment
views. In parallel, risk factors are preferred over asset class risk modelling. Affinity towards risk factors rather
than asset classes is primarily linked with two elements; the reduction of the dimensionality of the risk estimation
127problem and the intuitive way in which portfolio exposures per risk factor can be expressed as performance
drivers. The first empirical part of the thesis deals with the optimisation of a relative to an index portfolio
where the centre of gravity is the chosen benchmark. The first ingredient of the optimisation is the blend of
the yield advantage over the index and the expectations for excess returns over the index emanating from the
investment views. The second ingredient is the risk estimated by a multifactor risk model. Then, a set of relative
to the index investment grade portfolios is constructed. The second empirical part investigates whether there
is scope to blend the multifactor risk framework with more sophisticated risk estimation techniques such as
resampling. Tail risk estimated by block bootstrapping on the risk exposures of real actively managed portfolio
exposures vs. the Barclays Capital US Aggregate index is compared with the parametric and exponentially
weighted moving average risk model findings. The multifactor risk estimate using block bootstrapping exhibits
better performance than the alternatives tested but struggles to capture the out of sample extremes. Finally,
the third empirical part aims to enhance the allocation model by taking advantage of the findings of the second
empirical part. The blending mechanism of equilibrium returns and investment views, which are expressed as
optimisation constraints, is performed with the aid of a numerically approximated returns’ distribution. The
resampled distribution deviates from the normality assumption imposed initially in the Black\-Litterman model
and forms a more realistic basis for the evaluation of investment views and for the portfolio construction against
tail risk measures such as value at risk and conditional value at risk.
van der Schans, M. and Steehouwer, H. (2016\). “Time\-Dependent Black\-Litterman .” In:SSRN e\-Print .
The Black\-Litterman method is widely used in the investment management industry to incorporate views in
investment portfolios. The method applies when views are expressed as expected returns over the horizon on
which allocation decisions are made, i.e., the investment horizon. In practice, however, the investor’s views are
typically formulated for the near future while the investor’s investment horizon is much longer. To incorporate
such views, we introduce the time\-dependent Black\-Litterman method and show that, in this time\-dependent
setting,adistinctionshouldbemadebetweenunconditionalandconditionalviews.Furthermore,wedemonstrate
its use for buy and hold investors. In an example, we show that the investor’s views have a plausible impact on
resulting allocation decisions.
van Pelt, T. G. (2020\). “Constructing Robust Portfolios, the Role of Parameter Uncertainty in Dynamic Optimal
Portfolio Allocations .” MA thesis. Erasmus University.
This paper investigates the ability to improve traditional portfolio optimisation rules in practice. SpeciFIcally, I
examine the effect of parameter uncertainty on Markowitz portfolio performance and quantify the corresponding
losses. Frequentist methods, in the form of di\-rect parameter shrinkage and assigned portfolio weight shrinkage
are employed to suppress effects of estimation errors. A Bayesian approach of the traditional Markowitz portfolio
is used to account for estimation risks implicitly and novel Bayesian portfolio combinations are defined in search
of an optimal investment rule. Moreover, the assumption of normal re\-turns is relaxed by considering Markov
Switching Gaussian Mixture models. I demonstrate the mean\-variance modifications to be effective in improving
out\-of\-sample performance and show ability to beat the equally weighted benchmark for empirical samples of
the 48 Industry portfolios and Fama\-French 100 portfolios. Lastly, I validate the competence of producing robust
portfolios over periods of changing economic times when parameter uncertainty is considered in the Markowitz
model.
van Staden, P. M., Dang, D.\-M., and Forsyth, P. A. (2021a). “On the Distribution of Terminal Wealth under
Dynamic Mean\-Variance Optimal Investment Strategies .” In:SIAM Journal on Financial Mathematics 12(2\),
pp. 566–603\.
We compare the distributions of terminal wealth obtained from implementing the optimal investment strategies
associatedwiththedifferentapproachestodynamicmean\-variance(MV)optimizationavailableintheliterature.
This includes the precommitment MV (PCMV) approach, the dynamically optimal MV (DOMV) approach,
as well as the time\-consistent MV approach with a constant risk aversion parameter (cTCMV) and wealth\-
dependent risk\-aversion parameter (dTCMV), respectively. For benchmarking purposes, a constant proportion
(CP) investment strategy is also considered. To ensure that terminal wealth distributions are compared on a fair
and practical basis, we assume that an investor, otherwise agnostic about the philosophical differences of the
underlying approaches to dynamic MV optimization, requires that the same expected value of terminal wealth
should be obtained regardless of the approach. We present first\-order stochastic dominance results proving that
forwealthoutcomesbelowthechosenexpectedvaluetarget,thecTCMVstrategyalwaysoutperformstheDOMV
strategy, and an appropriately chosen CP strategy always outperforms the dTCMV strategy. We also show that
the PCMV strategy results in a terminal wealth distribution with fundamentally different characteristics than
128any of the other strategies. Finally, our analytical results are very effective in explaining the numerical results
currently available in the literature regarding the relative performance of the various investment strategies.
van Staden, P. M., Dang, D.\-M., and Forsyth, P. A. (2021b). “The surprising robustness of dynamic Mean\-Variance
portfolio optimization to model misspecification errors .” In:European Journal of Operational Research 289(1\),
pp. 774–792\.
In single\-period portfolio optimization settings, Mean\-Variance (MV) optimization can result in notoriously
unstable asset allocations due to small changes in the underlying asset parameters. This has resulted in the
widespread questioning of whether and how MV optimization should be implemented in practice, and has also
resultedinanumberofalternativesbeingproposedtotheMVobjectiveforassetallocationpurposes.Incontrast,
in dynamic or multi\-period MV portfolio optimization settings, preliminary numerical results show that MV
investment outcomes can be remarkably robust to model misspecification errors, which arise when the investor
derives an optimal investment strategy based on some chosen model for the underlying asset dynamics (the
investor model), but implements this strategy in a market driven by potentially completely different dynamics
(the true model). In this paper, we systematically investigate the causes of this surprising robustness of dynamic
MV portfolio optimization to model misspecification errors under both the pre\-commitment MV (PCMV) and
time\-consistent MV (TCMV) approaches. We identify particular combinations of parameters that play a key
role in explaining the observed model misspecification errors. We investigate the impact of the chosen dynamic
MV approach, underlying model formulation, portfolio rebalancing frequency and the application of multiple
realistic investment constraints on the robustness of investment outcomes, as well as the implications for model
calibration.
Van Staden, P. M. (2020\). “Numerical methods for mean\-risk portfolio optimization .” PhD thesis. The University
of Queensland.
We consider various aspects of the dynamic mean\-risk portfolio optimization problem, with specific focus on
the numerical methods to solve this problem in the case where the risk measure is either the variance of wealth
outcomes or the quadratic variation of the wealth process. In the case where the risk measure is the variance of
wealth outcomes, the mean\-risk problem is known as the dynamic mean\-variance (MV) portfolio optimization
problem. Since variance is not separable in the sense of dynamic programming, the MV objective violates
Bellman’s principle of optimality. As a result, the possibility of the time\-inconsistency of the associated MV\-
optimalinvestmentstrategiesleadstoanumberofcompetingapproachestoformulatingandsolvingthedynamic
MV problem. We primarily focus on the two main approaches, namely the time\-consistent MV (TCMV) and the
pre\-commitment MV (PCMV) optimization problems. In addition, this investigation also leads us to consider
related approaches which are not necessarily MV optimal in some sense, such as the Mean\-Quadratic Variation
(MQV) portfolio optimization problem. First, we investigate the TCMV portfolio optimization problem under
a realistic context that involves the simultaneous application of different types of investment constraints and
modelling assumptions, for which a closed\-form solution is not known to exist. We develop an efficient numerical
partial differential equation method for determining the optimal control for this problem. Central to our method
is a combination of (i) an impulse control formulation of the MV investment problem, and (ii) a discretized
version of the dynamic programming principle enforcing a time\-consistency constraint. Our method requires
solution of linear partial integro\-differential equations between intervention times, which is numerically simple
and computationally effective. Solving the TCMV problem numerically enables us to conduct a comprehensive
comparison study of the PCMV and the TCMV optimal investment strategies. Second, we investigate the
MQV problem and its relationship to the TCMV problem. In the case of the MQV problem, the risk measure
is the quadratic variation (QV) of the controlled portfolio wealth process. In the case of jumps in the risky
asset process and no investment constraints, we derive analytical solutions for the TCMV and MQV problems.
We study conditions under which the two problems are (i) identical with respect to MV trade\-offs, and (ii)
equivalent, i.e. same value function and optimal control. In order to compare the MQV and TCMV problems in
a more realistic setting which involves investment constraints and modelling assumptions for which analytical
solutions are not known to exist, using a impulse control approach, we develop an efficient partial integro\-
differential equation (PIDE) method for determining the optimal control for the MQV problem. We also prove
convergence of the proposed numerical method to the viscosity solution of the corresponding PIDE. We find
that MQV investor achieves essentially the same results concerning terminal wealth as TCMV investor, but
the MQV\-optimal investment process has more desirable risk characteristics from the perspective of long\-term
investors with fixed investment time horizons. As a result, we conclude that MQV portfolio optimization is a
potentially desirable alternative to the TCMV counterpart. Third, we investigate the surprising robustness to
129model misspecification of the dynamic MV portfolio optimization results obtained using either the PCMV or the
TCMV approach. Model misspecification errors occur when the investor derives an optimal investment strategy
basedonsomechosenmodelfortheunderlyingassetdynamics(theinvestormodel),butimplementsthisstrategy
in a market driven by potentially completely different dynamics (the true model). We find that, since the error in
MV outcomes is driven by certain ratios of combinations of model parameters, individual parameters only play
a secondary role, and hence MV outcomes are, in general, very robust to model mispecification. Furthermore,
under certain conditions, we show that the PCMV results are less robust than the TCMV results to model
misspecification errors when no realistic investment constraints are applied. However, our numerical tests show
that the opposite can hold true when constraints are included. Finally, we compare the distributions of terminal
wealth obtained from implementing the optimal investment strategies associated with the different approaches to
dynamic MV optimization available in the literature. This includes not only the PCMV and TCMV approaches,
but also the dynamically optimal MV (DOMV) approach which has been proposed recently. For benchmarking
purposes, a constant proportion (CP) investment strategy is also considered, under which a constant proportion
ofwealthisalwaysinvestedintheriskyasset.Toensurethatterminalwealthdistributionsarecomparedonafair
and reasonable basis, we assume that an investor, otherwise agnostic about the philosophical differences of the
underlying approaches to dynamic MV optimization, requires that the same expected value of terminal wealth
should be obtained regardless of the approach. We present first\-order stochastic dominance results proving
that for wealth outcomes below the chosen expected value target, the TCMV strategy with a constant risk
aversion parameter always outperforms the DOMV strategy, and an appropriately chosen CP strategy always
outperformstheTCMVstrategywithawealth\-dependentriskaversionparameter.WealsoshowthatthePCMV
strategy results in a terminal wealth distribution with fundamentally different characteristics than any of the
other strategies. Our analytical results are very effective in explaining the numerical results currently available in
the literature regarding the relative performance of the various investment strategies. In conclusion, the results
presented in this thesis make a number of important contributions regarding various aspects of the dynamic
mean\-risk portfolio optimization problems considered.
Vaquez,I.,Villar,J.R.,Sedano,J.,andSimic,S.(2019\). “Apreliminarystudyonmultivariatetimeseriesclustering .”
In:14th international conference on soft computing models in industrial and environmental applications (SOCO
2019\). Ed. by F. Martinez Alvarez, A. Troncoso Lora, J. A. Saez Munoz, H. Quintian, and E. Corchado. Vol. 950\.
Springer International Publishing, pp. 473–480\.
Time Series (TS) clustering is one of the most effervescent research fields due to the Big Data and the IoT
explosion. The problem gets more challenging if we consider the multivariate TS. In the field of Business and
Management, multivariate TS are becoming more and more interesting as they allow to match events the co\-
occur in time but that is hardly noticeable. In this study, Recurrent Neural Networks and transfer learning
have been used to analyze each example, measuring similarities between variables. All the results are finally
aggregated to create an adjacency matrix that allows extracting the groups. Proof\-of\-concept experimentation
has been included, showing that the solution might be valid after several improvements.
Vilkkumaa, E., Liesio, J., Salo, A., and Ilmola\-Sheppard, L. (2018\). “Scenario\-based portfolio model for building
robust and proactive strategies .” In:European Journal of Operational Research (2661\), pp. 205–220\.
In order to address major changes in the operational environment, companies can (i) define scenarios that
characterize different alternatives for this environment, (ii) assign probabilities to these scenarios, (iii) evaluate
the performance of strategic actions across the scenarios, and (iv) choose those actions that are expected to
perform best. In this paper, we develop a portfolio model to support the selection of such strategic actions when
the information about scenario probabilities is possibly incomplete and may depend on the selected actions. This
model helps build a strategy that is robust in that it performs relatively well in view of all available probability
information, and proactive in that it can help steer the future as reflected by the scenarios toward the desired
direction. We also report a case study in which the model helped a group of Nordic, globally operating steel and
engineering companies build a platform ecosystem strategy that accounts for uncertainties related to markets,
politics, and technological development.
Vincent, K., Hsu, Y.\-C., and Lin, H.\-W. (2018\). “Analyzing the Performance of Multifactor Investment Strategies
under a Multiple Testing Framework .” In:The Journal of Portfolio Management 44(4\), pp. 113–126\.
Evaluating portfolios based on numerous combinations of factors using the individual backtesting method could
suffer from serious data mining bias and lead to spurious significant findings. Accordingly, the authors employ
a multiple hypothesis testing method to examine the multifactor portfolio performance. Their empirical results
showthatevenaftertheyadjustforthemultiplecomparisonsbias,stock\-pickingstrategieswithcertaincombined
130firm characteristics could generate significantly better liquidity risk\-adjusted returns. In addition, the outper\-
forming multifactor strategies that the authors report are robust to alternative definitions of factors. However,
they observe that the number of significantly profitable multifactor portfolios has decreased substantially in the
era of increased liquidity and trading activity in the U.S. stock market.
Vovk, V. and Wang, R. (2020\). “True and false discoveries with e\-values .” In:arXiv e\-Print .
The topic of this paper is multiple hypothesis testing based on e\-values, which are Bayes factors stripped of
their Bayesian content. Using e\-values instead of p\-values, which are standard in this area, leads to simple and
efficient procedures that control the number of false discoveries under arbitrary dependence of the base e\-values.
We prove an optimality result for our main procedure and demonstrate advantages of our methods over standard
methods using simulated and real\-world datasets.
Vovk, V. and Wang, R. (2021\). “E\-values: Calibration, combination, and applications .” In:Annals of Statistics
49(3\), pp. 1736–1753\.
Multiple testing of a single hypothesis and testing multiple hypotheses are usually done in terms of p\-values.
In this paper we replace p\-values with their natural competitor, e\-values, which are closely related to betting,
Bayes factors, and likelihood ratios. We demonstrate that e\-values are often mathematically more tractable; in
particular, in multiple testing of a single hypothesis, e\-values can be merged simply by averaging them. This
allows us to develop efficient procedures using e\-values for testing multiple hypotheses.
Vyrost, T., Lyocsa, S., and Baumohl, E. (2019\). “Network\-based asset allocation strategies .” In:The North American
Journal of Economics and Finance 47, pp. 516–536\.
In this study, we construct financial networks in which nodes are represented by assets and where edges are
based on long\-run correlations. We construct four networks (complete graph, a minimum spanning tree, a pla\-
narmaximallyfilteredgraph,andathresholdsignificancegraph)andusethreecentralitymeasures(betweenness,
eigenvalue centrality, and the expected force). To improve risk return characteristics of well\-known return max\-
imization and risk minimization benchmark portfolios, we propose simple adjustments to portfolio selection
strategies that utilize centralization measures from financial networks. From a sample of 45 assets (stock market
indices, bond and money market instruments, commodities, and foreign exchange rates) and from data for 1999
to 2015, we show that irrespective of the network and centrality employed, the proposed network\-based asset
allocation strategies improve key portfolio return characteristics in an out of sample framework, most notably,
risk and left tail risk adjusted returns. Resolving portfolio model selection uncertainties further improves risk
return characteristics. Improvements made to portfolio strategies based on risk minimization are also robust to
transaction costs.
Walters, J. (2014\). “The Black\-Litterman Model in Detail .” In:SSRN e\-Print .
InthispaperwesurveytheliteratureontheBlack\-Littermanmodel.Thissurveyisprovidedbothasachronology
andataxonomyastherearemanyclaimsonthemodelintheliterature.Weprovideacompletedescriptionofthe
canonical model including full derivations from the underlying principles using both Theil’s Mixed Estimation
model and Bayes Theory. The various parameters of the model are considered, along with information on their
computation or calibration. Further consideration is given to several of the key papers, with worked examples
illustrating the concepts.
Wang, H., Pappada, R., Durante, F., and Foscolo, E. (2017\). “A Portfolio Diversification Strategy via Tail De\-
pendence Clustering .” In:Soft Methods for Data Science . Ed. by M. B. Ferraro, P. Giordani, B. Vantaggi, M.
Gagolewski, M. Angeles Gil, P. Grzegorzewski, and O. Hryniewicz. Vol. 456\. Advances in Intelligent Systems
and Computing. Springer International Publishing, pp. 511–518\.
We provide a two\-stage portfolio selection procedure in order to increase the diversification benefits in a bear
market. By exploiting tail dependence\-based risky measures, a cluster analysis is carried out for discerning
between assets with the same performance in risky scenarios. Then, the portfolio composition is determined by
fixing a number of assets and by selecting only one item from each cluster. Empirical calculations on the EURO
STOXX 50 prove that investing on selected assets in trouble periods may improve the performance of risk\-averse
investors.
Wang, H. and Zhou, X. Y. (2020\). “Continuous\-time mean\-variance portfolio selection: A reinforcement learning
framework .” In:Mathematical Finance 30(4\), pp. 1273–1308\.
We approach the continuous\-time mean\-variance portfolio selection with reinforcement learning (RL). The prob\-
lem is to achieve the best trade\-off between exploration and exploitation, and is formulated as an entropy\-
regularized, relaxed stochastic control problem. We prove that the optimal feedback policy for this problem
must be Gaussian, with time\-decaying variance. We then prove a policy improvement theorem, based on which
131we devise an implementable RL algorithm. We find that our algorithm and its variant outperform both tradi\-
tional and deep neural network based algorithms in our simulation and empirical studies.
Wang, H., Suri, A., Laster, D., and Almadi, H. (2011\). “Portfolio Selection in Goals\-Based Wealth Management .”
In:The Journal of Wealth Management 14(1\), pp. 55–65\.
The authors propose an incremental step toward combining the insights of modern portfolio theory with some
of the propensities documented in the literature on behavioral finance. They develop a goals\-based wealth
management approach that finds a specific subportfolio to address each of an investor’s goals and then de\-
rive the least\-cost solution. T hey relate the closed\-form solution for the one\-period, two\-asset problem to the
mean\-variance efficient frontier. Consistent with the \- lockbox separation\- concept proposed by Sharpe, they
demonstrate that a multiperiod goal, such as a retirement plan, can be viewed as a collection of single\-period
problems. Next, they extend their result to a market with many assets, where portfolios are exogenously given.
Finally, they illustrate the approach with a case study with multiple asset classes and multiperiod goals.
Wang, J., Ma, F., Liang, C., and Chen, Z. (2022\). “Volatility forecasting revisited using Markov\-switching with
time\-varying probability transition .” In:International Journal of Finance \& Economics .
This study proposes a novel model, Markov\-switching Heterogeneous Autoregressive (MS\-HAR) model with
jump\-driven time\-varying transition probabilities (TVTP), to forecast the future volatility in Chinese stock
market. The in\-sample results show that MS\-HAR models are more powerful than HAR\-RV\-type models; fur\-
thermore,thehigh\-volatilityregimeisshort\-lived.Moreover,theout\-of\-sampleresultsindicatethattheMS\-HAR
with TVTP model can achieve a superior forecasting performance and increase the economic value than the
competing models including the simple HAR model and the MS\-HAR with fixed transition probabilities (FTP)
model. The results are robust to several robustness checks including alternative forecast window, alternative
evaluation method, alternative predictive model, sub\-sample analysis and alternative representative index.
Wang, P. and Spinney, J. (2017\). “Strategic Asset Allocation: Combining Science and Judgment to Balance Short\-
Term and Long\-Term Goals .” In:The Journal of Portfolio Management 44(1\), pp. 69–82\.
The authors build on traditional mean\-variance optimization with a quantitative framework for combining the
best of science and judgment in selecting an asset allocation for long\-horizon investors such as endowments. The
novelty of their approach lies in its ability to balance the desire for long\-term returns with the need to manage
short\-term risk and funding constraints\-important goals that are often in conflict. To reap the benefits of long\-
term risk premia, investors must be able to withstand occasional short\-term painful drawdowns. The authors
show how their unified approach can be used to examine how different combinations of asset classes, spending
rates, and even alpha impact the policy portfolio over various planning horizons. The framework merges the
science of portfolio optimization with a structure that informs sound judgment in determining an organization’s
strategic asset allocation and spending policies.
Wang, Y. and Aste, T. (2022\). “Dynamic Portfolio Optimization with Inverse Covariance Clustering .” In:arXiv
e\-Print.
Market conditions change continuously. However, in portfolio’s investment strategies, it is hard to account for
this intrinsic non\-stationarity. In this paper, we propose to address this issue by using the Inverse Covariance
Clustering (ICC) method to identify inherent market states and then integrate such states into a dynamic
portfolio optimization process. Extensive experiments across three different markets, NASDAQ, FTSE and
HS300, over a period of ten years, demonstrate the advantages of our proposed algorithm, termed Inverse
Covariance Clustering\-Portfolio Optimization (ICC\-PO). The core of the ICC\-PO methodology concerns the
identification and clustering of market states from the analytics of past data and the forecasting of the future
market state. It is therefore agnostic to the specific portfolio optimization method of choice. By applying the
same portfolio optimization technique on a ICC temporal cluster, instead of the whole train period, we show
that one can generate portfolios with substantially higher Sharpe Ratios, which are statistically more robust
and resilient with great reductions in maximum loss in extreme situations. This is shown to be consistent across
markets, periods, optimization methods and selection of portfolio assets.
Watagoda, L. C. R. P. and Olive, D. J. (2021\). “Comparing six shrinkage estimators with large sample theory and
asymptotically optimal prediction intervals .” In:Statistical Papers 62(5\), pp. 2407–2431\.
Consider the multiple linear regression model with sample size n. This paper compares the six shrinkage estima\-
tors: forward selection, lasso, partial least squares, principal components regression, lasso variable selection, and
ridge regression, with large sample theory and two new prediction intervals that are asymptotically optimal if
the estimator is a consistent estimator of . Few prediction intervals have been developed for pn, and they are
not asymptotically optimal. For p fixed, the large sample theory for variable selection estimators like forward
132selection is new, and the theory shows that lasso variable selection is consistent under much milder conditions
than lasso. This paper also simplifies the proofs of the large sample theory for lasso, ridge regression, and elastic
net.
Wiecki, T., Campbell, A., Lent, J., and Stauth, J. (2016\). “All That Glitters Is Not Gold: Comparing Backtest
and Out\-of\-Sample Performance on a Large Cohort of Trading Algorithms .” In:The Journal of Investing 25(3\),
pp. 69–80\.
When automated trading strategies are developed and evaluated using backtests on historical pricing data, there
exists a tendency to overfit to the past. Using a unique dataset of 888 algorithmic trading strategies developed
and backtested on the Quantopian platform, with at least six months of out\-of\-sample performance, this ar\-
ticle studies the prevalence and impact of backtest overfitting. Specifically, the authors find that commonly
reported backtest evaluation metrics, such as the Sharpe ratio, offer little value in predicting out\-of\-sample
performance (R2 \< 0\.025\). In contrast, higher\-order moments, such as volatility and maximum drawdown, as
well as portfolio construction features (e.g., hedging), show significant predictive value of relevance to quanti\-
tative finance practitioners. Moreover, in line with prior theoretical considerations, the authors find empirical
evidence of overfitting\-the more backtesting a quant has done for a strategy, the larger the discrepancy be\-
tween backtest and out\-of\-sample performance. Finally, they show that by training nonlinear, machine\-learning
classifiers on a variety of features that describe backtest behavior, out\-of\-sample performance can be predicted
with much greater accuracy (R2 \= 0\.17\) on hold\-out data than when using linear, univariate features. A port\-
folio constructed by using predictions on hold\-out data performed significantly better out\-of\-sample than one
constructed from algorithms with the highest backtest Sharpe ratios.
Wu, L., Feng, Y., and Palomar, D. P. (2020\). “General sparse risk parity portfolio design via successive convex
optimization .” In:Signal Processing 170, p. 107433\.
Since the 2008 financial crisis, risk management has become more important and portfolio approaches, such as
the minimum\-variance and equally weighted portfolios, have gained popularity. However, such portfolios still
do not diversify the risk in the true sense. Recently, risk parity portfolios has been receiving significant interest
from both the theoretical and practical perspectives due to its advantages in the diversification of (ex\-ante) risk
contributions among assets. However, this portfolio type usually results in nonzero weights in all the assets,
which implies high transaction cost in practice. In addition, focusing only on the risk aspect can make this
type of portfolio unsatisfactory if other performance factors, e.g., annual yield, are considered. In this paper,
we jointly consider asset selection and risk diversification via imposing sparsity and risk parity regularization in
the portfolio problem formulation, which turns out to be a general and flexible portfolio framework. Then we
propose an efficient sequential algorithm based on the successive convex optimization framework. The numerical
results on historical data show that our portfolio approach, compared with benchmark portfolios, can achieve
a good balance among asset selection, risk diversification and other evaluation criteria, and achieves the best
performance on profit and loss (P\&L) and/or drawdown.
Xiao, Y. and Valdez, E. A. (2015\). “A Black\-Litterman asset allocation model under Elliptical distributions .” In:
Quantitative Finance 15(3\), pp. 509–519\.
In optimal portfolio allocation, Black and Litterman \[Financ. Anal. J., 1992, 48, 28?43] provide for a pioneering
framework of allowing to incorporate investors? views based on a prior distribution to derive a posterior dis\-
tribution of portfolio returns and optimal asset allocations. Meucci \[Risk and Asset Allocation, 2005] rephrases
the model in terms of investors? views on the market, rather than just the market parameters as in the original
Black and Litterman \[Financ. Anal. J., 1992, 48, 28?43]. This market\-based version is believed to be much more
parsimonious and allows for a more natural extension to directly input views in a non\-Normal market. This
paper extends Meucci?s market\-based version of the Black?Litterman model to the case when returns in the
market fall within the class of Elliptical distributions, while also importantly preserving the equilibrium\-based
assumption in the model. Here, within this class for which the Normal distribution is a special case, we develop
the explicit form of the posterior distribution after considering proper conditional conjugate\-type prior distribu\-
tions. This resulting posterior allows us to obtain solutions to optimization problems of asset allocation based on
a variety of risk measures (e.g. Mean\-Variance, Mean\-VaR, Mean\-Conditional VaR). Elliptical models of port\-
folio returns have recently crept into the financial literature because of their greater flexibility to accommodate
larger tails. As numerical demonstrations, we examine how these principles work in a portfolio with international
stock indices and show why models with more flexible tails can affect the asset allocation. In optimal portfolio
allocation, Black and Litterman \[Financ. Anal. J., 1992, 48, 28?43] provide for a pioneering framework of allow\-
ing to incorporate investors? views based on a prior distribution to derive a posterior distribution of portfolio
133returns and optimal asset allocations. Meucci \[Risk and Asset Allocation, 2005] rephrases the model in terms
of investors? views on the market, rather than just the market parameters as in the original Black and Litter\-
man \[Financ. Anal. J., 1992, 48, 28?43]. This market\-based version is believed to be much more parsimonious
and allows for a more natural extension to directly input views in a non\-Normal market. This paper extends
Meucci?s market\-based version of the Black?Litterman model to the case when returns in the market fall within
the class of Elliptical distributions, while also importantly preserving the equilibrium\-based assumption in the
model. Here, within this class for which the Normal distribution is a special case, we develop the explicit form of
the posterior distribution after considering proper conditional conjugate\-type prior distributions. This resulting
posterior allows us to obtain solutions to optimization problems of asset allocation based on a variety of risk
measures (e.g. Mean\-Variance, Mean\-VaR, Mean\-Conditional VaR). Elliptical models of portfolio returns have
recently crept into the financial literature because of their greater flexibility to accommodate larger tails. As
numerical demonstrations, we examine how these principles work in a portfolio with international stock indices
and show why models with more flexible tails can affect the asset allocation.
Xidonas,P.,Steuer,R.,andHassapis,C.(2020\). “Robustportfoliooptimization:acategorizedbibliographicreview .”
In:Annals of Operations Research 292(1\), pp. 533–552\.
Robust portfolio optimization refers to finding an asset allocation strategy whose behavior under the worst
possible realizations of the uncertain inputs, e.g., returns and covariances, is optimized. The robust approach is
in contrast to the classical approach, where one estimates the inputs to a portfolio allocation problem and then
treats them as certain and accurate. In this paper we provide a categorized bibliography on the application of
robust mathematical programming to the portfolio selection problem. With no similar surveys available, one of
the aims of this review is to provide quick access for those interested, but maybe not yet in the area, so they
know what the area is about, what has been accomplished and where everything can be found. Toward this end,
a total of 148 references have been compiled and classified in various ways. Additionally, the number of Scopus
citations by contribution and journal is recorded. Finally, a brief discussion of the review’s major findings is
provided and some solid leads on future directions are given.
Xing, F. Z., Cambria, E., Malandri, L., and Vercellis, C. (2018\). “Discovering Bayesian Market Views for Intelligent
Asset Allocation .” In:arXiv e\-Print .
Along with the advance of opinion mining techniques, public mood has been found to be a key element for stock
market prediction. However, in what manner the market participants are affected by public mood has been rarely
discussed. As a result, there has been little progress in leveraging public mood for the asset allocation problem,
as the application is preferred in a trusted and interpretable way. In order to address the issue of incorporating
public mood analyzed from social media, we propose to formalize it into market views that can be integrated
into the modern portfolio theory. In this framework, the optimal market views will maximize returns in each
period with a Bayesian asset allocation model. We train two neural models to generate the market views, and
benchmark the performance of our model using market views on other popular asset allocation strategies. Our
experimental results suggest that the formalization of market views significantly increases the profitability (5%
to 10%) of the simulated portfolio at a given risk level.
Yam, S. C. P., Yang, H., and Yuen, F. L. (2016\). “Optimal asset allocation: Risk and information uncertainty .” In:
European Journal of Operational Research 251(2\), pp. 554–561\.
In asset allocation problem, the distribution of the assets is usually assumed to be known in order to identify the
optimalportfolio.Inpractice,weneedtoestimatetheirdistribution.Theestimationsarenotnecessarilyaccurate
and it is known as the uncertainty problem. Many researches show that most people are uncertainty aversion
and this affects their investment strategy. In this article, we consider risk and information uncertainty under a
commonasset allocation framework.The effects of risk premium and covarianceuncertaintyare demonstrated by
the worst scenario in a set of measures generated by a relative entropy constraint. The nature of the uncertainty
and its impacts on the asset allocation are discussed.
Yang, H., Wang, M.\-h., and Huang, N.\-j. (2021a). “The alpha Tail Distance with an Application to Portfolio
Optimization Under Different Market Conditions .” In:Computational Economics .
It is very important to find some new distance measurement methods to estimate the correlation of the return of
stocks because that the traditional distance measurement methods do not consider the influence of the market
conditions. In this paper, a new distance measurement which called the alpha\-tail distance is introduced to
measure the correlations of stock’s returns under the different market conditions. We give some properties of the
alpha\-tail distance and provide some details on how to determine the parametric alpha in the alpha\-tail distance
via the market condition evaluation indices. A mean variance model with variable cardinality constraints based
134on the hierarchical clustering is given as an application of the alpha\-tail distance. Moreover, the numerical
example verifies that the alpha\-tail distance is more suitable for measuring the correlation between stock’s
returns than other traditional distance measurements under the different market conditions.
Yang, Q., Hong, Z., Tian, R., Ye, T., and Zhang, L. (2021b). “Asset Allocation via Machine Learning and Applica\-
tions to Equity Portfolio Management .” In:SSRN e\-Print .
In this paper, we document a novel machine learning based bottom\-up approach for static and dynamic portfolio
optimization on, potentially, a large number of assets. The methodology overcomes many major difficulties
arising in current optimization schemes. For example, we no longer need to compute the covariance matrix and
its inverse for mean\-variance optimization, therefore the method is immune from the estimation error on this
quantity. Moreover, no explicit calls of optimization routine are needed. Applications to a bottom\-up mean\-
variance\-skewness\-kurtosis or CRRA (Constant Relative Risk Aversion) optimization with short\-sale portfolio
constraints in both simulation and real market (China A\-shares and U.S. equity markets) environments are
studied and shown to perform very well.
Yin, C., Perchet, R., and Soupe, F. (2021\). “A practical guide to robust portfolio optimization .” In:Quantitative
Finance 21(6\), pp. 911–928\.
Robust optimization takes into account the uncertainty in expected returns to address the shortcomings of
portfolio mean\-variance optimization, namely the sensitivity of the optimal portfolio to inputs. We investigate
the mechanisms by which robust optimization achieves its goal and give practical guidance when it comes to
the choice of uncertainty in form and level. We explain why the quadratic uncertainty set should be preferred to
box uncertainty based on the literature review, we show that a diagonal uncertainty matrix with only variances
should be used, and that the level of uncertainty can be chosen as a function of the asset Sharpe ratios. Finally,
we use practical examples to show that, with the proposed parametrization, robust optimization does overcome
the weaknesses of mean\-variance optimization and can be applied in real investment problems such as the
management of multi\-asset portfolios or in robo\-advising.
Yu, L. (2021\). “Comparing Classical Portfolio Optimization and Robust Portfolio Optimization on Black Swan
Events.” MA thesis. University of Waterloo.
Blackswanevents,suchasnaturalcatastrophesandmanmademarketcrashes,historicallyhaveadrasticnegative
influence on investments; and there is a discrepancy on losses caused by these two types of disasters. In general,
thereisarecoveryanditisofinteresttounderstandwhattypeofinvestmentstrategiesleadtobetterperformance
for investors. In this thesis we study classical portfolio optimization, robust portfolio optimization and some
historical black swan events. We compare two main strategies: mean variance optimization vs robust portfolio
optimization on two types of black swan events: natural vs anthropogenic. The comparison illustrates that
robust portfolio optimization is much more conservative, and has a shorter recovery time than classical portfolio
optimization. Moreover, the losses in the stock investment resulted from a natural disaster are very minor
compared to the losses resulted from an anthropogenic market crash.
Yuan,J.andYuan,X.(2021\). “AMonteCarlosyntheticsamplebasedperformanceevaluationmethodforcovariance
matrix estimators .” In:Applied Economics Letters .
The evaluation of covariance matrix estimators is very important for portfolio analysis and risk management.
The Monte Carlo synthetic sample based performance evaluation method proposed by this article can avoid
the main shortcomings of statistical and economic methods which are widely used in the existing literature.
The proposed method does not need the true covariance and does not need to introduce the performance of
the out\-of\-sample portfolios. It is an intuitive, effective and robust measure for both simulation and empirical
analysis.
Yuan, M. and Zhou, G. (2022\). “Why Naive 1/N Diversification Is Not So Naive, and How to Beat It? ” In:SSRN
e\-Print.
In this paper, we study portfolio choice problem under estimation risk and show why the 1/N rule is very difficult
to beat in applications and studies. First, as long as the dimensionality is high relative to sample size, we show
that the usual estimated investment strategies are biased even asymptotically. Second, we show that the 1/N
rule is optimal in a one\-factor model with diversifiable risks as dimensionality increases, irrespectively of the
sample size, making investment theory\-based rules inadequate as they suffer from estimation errors. Third, we
provide strategies that can outperform the 1/N under suitable conditions.
Zaimovic, A., Omanovic, A., and Arnaut\-Berilo, A. (2021\). “How Many Stocks Are Sufficient for Equity Portfolio
Diversification? A Review of the Literature .” In:Journal of Risk and Financial Management 14(11\), p. 551\.
135Using extensive and comprehensive databases to select a subset of research papers, we aim to critically analyze
previous empirical studies to identify certain patterns in determining the optimal number of stocks in well\-
diversified portfolios in different markets, and to compare how the optimal number of stocks has changed over
different periods and how it has been affected by market turmoil such as the Global Financial Crisis (GFC) and
the current COVID\-19 pandemic. The main methods used are bibliometric analysis and systematic literature
review. Evaluating the number of assets which lead to optimal diversification is not an easy task as it is impacted
by a huge number of different factors: the way systematic risk is measured, the investment universe (size, asset
classes and features of the asset classes), the investor’s characteristics, the change over time of the asset features,
the model adopted to measure diversification (i.e., equally weighted versus optimal allocation), the frequency
of the data that is being used, together with the time horizon, conditions in the market that the study refers
to, etc. Our paper provides additional support for the fact that (1\) a generalized optimal number of stocks that
constitute a well\-diversified portfolio does not exist for whichever market, period or investor. Recent studies
further suggest that (2\) the size of a well\-diversified portfolio is larger today than in the past, (3\) this number
is lower in emerging markets compared to developed financial markets, (4\) the higher the stock correlations
with the market, the lower the number of stocks required for a well\-diversified portfolio for individual investors,
and (5\) machine learning methods could potentially improve the investment decision process. Our results could
be helpful to private and institutional investors in constructing and managing their portfolios and provide a
framework for future research.
Zakamulin,V.(2015\). “ATestofCovariance\-MatrixForecastingMethods .”In:TheJournalofPortfolioManagement
41(3\), pp. 97–108\.
Providing a more accurate covariance matrix forecast can substantially improve the performance of optimized
portfolios. Using out\-of\-sample tests we evaluate alternative covariance matrix forecasting methods by looking
at (1\) their forecast accuracy (2\) their ability to track the volatility of the minimum\-variance portfolio (3\) their
abilitytokeepthevolatilityoftheminimum\-varianceportfolioatatargetlevel.Wefindlargedifferencesbetween
the methods. Our results suggest that shrinkage of the sample covariance matrix improves neither the forecast
accuracy nor the performance of minimum\-variance portfolios. In contrast, switching from the sample covariance
matrix forecast to a multivariate GARCH forecast reduces forecasting error and portfolio tracking error by at
least half. Our findings also reveal that the exponentially weighted covariance matrix forecast performs only
slightly worse than the multivariate GARCH forecast.
Zanella, N. (2015\). “Risk Capacity over the Life Cycle: The Role of Human Capital, High Priority Goals, and
Discretionary Wealth .” In:The Journal of Wealth Management 18(3\), pp. 27–36\.
From the perspective of wealth management, life cycle theoretical models suggest that the total portfolio,
including human capital, should play an influential role in determining the composition of financial assets. In
fact, by incorporating human capital into portfolio choice optimization, investors become wealthier, holding
a respectable amount of safe assets. Young investors should be invested in stocks, and the risky asset share
is expected to decline as individuals convert their human wealth into financial capital. Unfortunately, these
academic recommendations and popular wisdom are inconsistent with the empirical observations on portfolio
choice at an international level. In this article, stylized facts on income and saving patterns over the life cycle are
presented, providing evidence that human wealth should be hump\-shaped; younger workers, who do not have
substantial wealth, have to implement a hierarchy of saving goals. Discretionary wealth to invest aggressively in
the stock markets is present only during the years of middle\-aged prosperity. The glide path used by the actual
target\-date funds in retirement plans needs to be reconsidered.
Zareei, A. (2019\). “Network origins of portfolio risk .” In:Journal of Banking \& Finance 109, p. 105663\.
This paper shows that shocks, in the presence of asymmetric propagation structures, diminish investors diversifi\-
cation benefits. First, we construct an interdependency network with assets as nodes, and links corresponding to
cross\-dependency in returns. Second, we show that higher heterogeneity in the structure of the network increases
portfolio risk. In particular, diversification among assets with star\-like network structures, where a central asset
cross\-affects other assets in the portfolio, results in the lowest level of diversification benefits. Finally, we empiri\-
cally demonstrate that two distinct datasets of U.S. industries and international stock markets greatly resemble
star\-like network structures.
Zhang, C., Li, Y., Chen, X., Jin, Y., Tang, P., and Li, J. (2020a). “DoubleEnsemble: A New Ensemble Method Based
on Sample Reweighting and Feature Selection for Financial Data Analysis .” In:IEEE International Conference
on Data Mining (ICDM) . IEEE.
136Modern machine learning models (such as deep neural networks and boosting decision tree models) have become
increasingly popular in financial market prediction, due to their superior capacity to extract complex non\-linear
patterns. However, since financial datasets have very low signal\-to\-noise ratio and are non\-stationary, complex
models are often very prone to overfitting and suffer from instability issues. Moreover, as various machine
learning and data mining tools become more widely used in quantitative trading, many trading firms have been
producinganincreasingnumberoffeatures(akafactors).Therefore,howtoautomaticallyselecteffectivefeatures
becomes an imminent problem. To address these issues, we propose DoubleEnsemble, an ensemble framework
leveraging learning trajectory based sample reweighting and shuffling based feature selection. Specifically, we
identify the key samples based on the training dynamics on each sample and elicit key features based on
the ablation impact of each feature via shuffling. Our model is applicable to a wide range of base models,
capable of extracting complex patterns, while mitigating the overfitting and instability issues for financial market
prediction. We conduct extensive experiments, including price prediction for cryptocurrencies and stock trading,
using both DNN and gradient boosting decision tree as base models. Our experiment results demonstrate that
DoubleEnsemble achieves a superior performance compared with several baseline methods.
Zhang, F., Guo, R., and Cao, H. (2020b). “Information Coefficient as a Performance Measure of Stock Selection
Models.” In:arXiv e\-Print .
Information coefficient (IC) is a widely used metric for measuring investment managers’ skills in selecting stocks.
However, its adequacy and effectiveness for evaluating stock selection models has not been clearly understood,
as IC from a realistic stock selection model can hardly be materially different from zero and is often accompanies
with high volatility. In this paper, we investigate the behavior of IC as a performance measure of stick selection
models. Through simulation and simple statistical modeling, we examine the IC behavior both statically and
dynamically. The examination helps us propose two practical procedures that one may use for IC\-based ongoing
performance monitoring of stock selection models.
Zhang, J. and Maringer, D. (2010\). Asset Allocation under Hierarchical Clustering . Tech. rep. COMISEF Compu\-
tational Optimization Methods in Statistics, Econometrics and Finance.
This paper proposes a clustering asset allocation scheme which provides better risk\-adjusted portfolio perfor\-
mance than those obtained from tradi\- tional asset allocation approaches such as the equal weight strategy
and the Markowitz minimum variance allocation. The clustering criterion used, which involves maximization
of the in\-sample Sharpe ratio (SR), is different from traditional clustering criteria reported in the literature.
Two evolu\- tionary methods, namely Differential Evolution and Genetic Algorithm, are employed to search for
such an optimal clustering structure given a clus\- ter number. To explore the clustering impact on the SR, the
in\-sample and the out\-of\-sample SR distributions of the portfolios are studied using bootstrapped data as well
as simulated paths from the single index market model. It was found that the SR distributions of the portfolios
under the clustering asset allocation structure have higher mean values and skewness but approximately the
same standard deviation and kurtosis than those in the non\-clustered case. Genetic Algorithm is suggested as a
more efficient approach than Differential Evolution for the purpose of solving the cluster\-ing problem.
Zhang, J. and Maringer, D. (2011\). “Distributing weights under hierarchical clustering: A way in reducing perfor\-
mance breakdown .” In:Expert Systems with Applications 38(12\), pp. 14952–14959\.
This paper proposes a clustering asset allocation scheme which provides better risk\-adjusted portfolio perfor\-
mance than those obtained from traditional asset allocation approaches such as the equal weight strategy and
the Markowitz minimum variance allocation. The clustering criterion used, which involves maximization of the
in\-sample Sharpe ratio (SR), is different from traditional clustering criteria reported in the literature. Two evo\-
lutionary methods, namely Differential Evolution and Genetic Algorithm, are employed to search for such an
optimal clustering structure given a cluster number. To explore the clustering impact on the SR, the in\-sample
and the out\-of\-sample SR distributions of the portfolios are studied using bootstrapped data as well as simu\-
lated paths from the single index market model. It was found that the SR distributions of the portfolios under
the clustering asset allocation structure have higher mean values and skewness but approximately the same
standard deviation and kurtosis than those in the non\-clustered case. Genetic Algorithm is suggested as a more
efficient approach than Differential Evolution for the purpose of solving the clustering problem. We introduce
a clustering scheme to improve portfolio Sharpe ratio. Mean and Skewness of Sharpe ratio can be improved
by using the clustering scheme. Genetic Algorithm is apt at finding an optimal clustering structure. Clustering
asset helps to improve portfolio risk\-adjusted performance. Sharpe ratio maximization can be considered as a
suitable clustering criterion.
137Zhang, Y., Li, X., and Guo, S. (2018\). “Portfolio selection problems with Markowitz mean\-variance framework: a
review of literature .” In:Fuzzy Optimization and Decision Making 17(2\), pp. 125–158\.
Since the pioneering work of Harry Markowitz, mean\-variance portfolio selection model has been widely used
in both theoretical and empirical studies, which maximizes the investment return under certain risk level or
minimizes the investment risk under certain return level. In this paper, we review several variations or gener\-
alizations that substantially improve the performance of Markowitz mean\-variance model, including dynamic
portfolio optimization, portfolio optimization with practical factors, robust portfolio optimization and fuzzy
portfolio optimization. The review provides a useful reference to handle portfolio selection problems for both
researchers and practitioners. Some summaries about the current studies and future research directions are
presented at the end of this paper.
Zhang, Z., Zohren, S., and Roberts, S. (2020c). “Deep Learning for Portfolio Optimization .” In:The Journal of
Financial Data Science 22(4\), pp. 8–20\.
In this article, the authors adopt deep learning models to directly optimize the portfolio Sharpe ratio. The
framework they present circumvents the requirements for forecasting expected returns and allows them to
directly optimize portfolio weights by updating model parameters. Instead of selecting individual assets, they
trade exchange\-traded funds of market indexes to form a portfolio. Indexes of different asset classes show robust
correlations, and trading them substantially reduces the spectrum of available assets from which to choose. The
authors compare their method with a wide range of algorithms, with results showing that the model obtains the
best performance over the testing period of 2011 to the end of April 2020, including the financial instabilities
of the first quarter of 2020\. A sensitivity analysis is included to clarify the relevance of input features, and the
authors further study the performance of their approach under different cost rates and different risk levels via
volatility scaling.
Zhang, Z., Zohren, S., and Roberts, S. (2021\). “Deep Learning for Portfolio Optimisation .” In:arXiv e\-Print .
We adopt deep learning models to directly optimise the portfolio Sharpe ratio. The framework we present
circumventstherequirementsforforecastingexpectedreturnsandallowsustodirectlyoptimiseportfolioweights
by updating model parameters. Instead of selecting individual assets, we trade Exchange\-Traded Funds (ETFs)
of market indices to form a portfolio. Indices of different asset classes show robust correlations and trading them
substantially reduces the spectrum of available assets to choose from. We compare our method with a wide
range of algorithms with results showing that our model obtains the best performance over the testing period,
from 2011 to the end of April 2020, including the financial instabilities of the first quarter of 2020\. A sensitivity
analysis is included to understand the relevance of input features and we further study the performance of our
approach under different cost rates and different risk levels via volatility scaling.
Zhao, L. (2019\). “Essays on data\-driven optimization .” PhD thesis. University of Texas at Austin.
The estimation of a data matrix contains two parts: the well estimated and the poorly estimated. The latter is
usually throwing away because the estimations are off. As argued in this paper, ignoring is the wrong thing to
do as the poorly estimated part is orthogonal to the well estimated. I will show how to use such orthogonality in\-
formation via robust optimization and provide application in portfolio optimization, least\-square regression, and
dimension reduction. Across a large number of experiments, utilizing the orthogonality information consistently
improves the performance.
Zhao, L., Chakrabarti, D., and Muthuraman, K. (2019\). “Portfolio Construction by Mitigating Error Amplification:
The Bounded\-Noise Portfolio .” In:Operations Research 67(4\), pp. 965–983\.
We address the problem of poor portfolio performance when a minimum\-variance portfolio is constructed using
thesampleestimates.Estimationerrorsaremostlyblamedforthepoorportfolioperformance.However,weargue
that even small unbiased estimation errors can lead to significantly bad performance because the optimization
step amplifies errors, in a nonsymmetric way. Instead of trying to independently improve the estimation step or
fix the optimization step for robustness, we disentangle the well\-estimated aspects from the poorly estimated
aspects of the covariance matrix. By using a single parameter held constant over all data sets and time periods,
our method achieves excellent performance both empirically and in the simulation. We also show how to use
information from the sample mean to construct mean\-variance portfolios that have higher out\-of\-sample Sharpe
ratios.
Zhao, Z., Xu, F., Du, D., and Meihua, W. (2021\). “Robust portfolio rebalancing with cardinality and diversification
constraints .” In:Quantitative Finance 21(10\), pp. 1707–1721\.
In this paper, we develop a robust conditional value at risk (CVaR) optimal portfolio rebalancing model un\-
der various financial constraints to construct sparse and diversified rebalancing portfolios. Our model includes
138transaction costs and double cardinality constraints in order to capture the trade\-off between the limit of in\-
vestment scale and the diversified industry coverage requirement. We first derive a closed\-form solution for the
robust CVaR portfolio rebalancing model with only transaction costs. This allows us to conduct an industry
risk analysis for sparse portfolio rebalancing in the absence of diversification constraints. Then, we attempt to
remedy the hidden industry risk by establishing a new robust portfolio rebalancing model with both sparse and
diversified constraints. This is followed by the development of a distributed\-version of the Alternating Direc\-
tion Method of Multipliers (ADMM) algorithm, where each subproblem admits a closed\-form solution. Finally,
we conduct empirical tests to compare our proposed strategy with the standard sparse rebalancing and no\-
rebalancing strategies. The computational results demonstrate that our rebalancing approach produces sparse
and diversified portfolios with better industry coverage. Additionally, to measure out\-of\-sample performance,
two superiority indices are created based on worst\-case CVaR and annualized return, respectively. Our ADMM
strategy outperforms the sparse rebalancing and no\-rebalancing strategies in terms of these indices.
Zhou, C., Wu, C., and Xu, W. (2020\). “Incorporating time\-varying jump intensities in the mean\-variance portfolio
decisions .” In:Journal of Futures Markets 40(3\), pp. 460–478\.
This paper examines the role of time\-varying jump intensities in forming mean\-variance portfolios. We find
that compared with the no\-jump or constant\-jump models, the model which incorporates time\-varying jump
intensities better fits the dynamics of the assets returns, and yields mean\-variance portfolios with higher Sharpe
ratios. Our research suggests that using a better econometric model that captures non\-normal features in the
data has benefits for portfolio allocation even for a mean\-variance investor.
Zilbering, Y., Jaconetti, C. M., and Kinniry Jr., F. M. (2015\). Best practices for portfolio rebalancing . Tech. rep.
Vanguard.
The primary goal of a rebalancing strategy is to minimize risk relative to a target asset allocation, rather than
to maximize returns. Over time, asset classes produce different returns that can change the portfolio’s asset
allocation. To recapture the portfolio’s original risk\-and\-return characteristics, the portfolio should therefore be
rebalanced. In theory, investors select a rebalancing strategy that weighs their willingness to assume risk against
expected returns net of the cost of rebalancing. Vanguard research has found that there is no optimal frequency
or threshold for rebalancing, since risk\-adjusted returns do not differ meaningfully from one rebalancing strategy
to another. As a result, we conclude that for most broadly diversified stock and bond fund portfolios (assuming
reasonable expectations regarding return patterns, average returns, and risk), annual or semiannual monitoring,
with rebalancing at 5 percent thresholds, is likely to produce a reasonable balance between risk control and
cost minimization for most investors. Annual rebalancing is likely to be preferred when taxes or substantial
time/costs are involved.
Zitelli, G. L. (2020\). “Random matrix models for datasets with fixed time horizons .” In:Quantitative Finance 20(5\),
pp. 769–781\.
This paper examines the use of random matrix theory as it has been applied to model large financial datasets,
especially for the purpose of estimating the bias inherent in Mean\-Variance portfolio allocation when a sample
covariance matrix is substituted for the true underlying covariance. Such problems were observed and modeled in
theseminalworkofLalouxetal.\[Noisedressingoffinancialcorrelationmatrices.Phys.Rev.Lett.,1999,83,1467]
and rigorously proved by Bai et al. \[Enhancement of the applicability of Markowitz’s portfolio optimization by
utilizing random matrix theory. Math. Finance, 2009, 19, 639\-667] under minimal assumptions. If the returns on
assets to be held in the portfolio are assumed independent and stationary, then these results are universal in that
they do not depend on the precise distribution of returns. This universality has been somewhat misrepresented
in the literature, however, as asymptotic results require that an arbitrarily long time horizon be available before
such predictions necessarily become accurate. In order to reconcile these models with the highly non\-Gaussian
returns observed in real financial data, a new ensemble of random rectangular matrices is introduced, modeled
on the observations of independent Levy processes over a fixed time horizon.
Zolotareva, E. (2021\). “Aiding Long\-Term Investment Decisions with XGBoost Machine Learning Model .” In:arXiv
e\-Print.
The ability to identify stock market trends has obvious advantages for investors. Buying stock on an upward
trend (as well as selling it in case of downward movement) results in profit. Accordingly, the start and end\-
points of the trend are the optimal points for entering and leaving the market. The research concentrates on
recognizing stock market long\-term upward and downward trends. The key results are obtained with the use of
gradient boosting algorithms, XGBoost in particular. The raw data is represented by time series with basic stock
market quotes with periods labelled by experts as Trend or Flat. The features are then obtained via various
139data transformations, aiming to catch implicit factors resulting in a change of stock direction. Modelling is done
in two stages: stage one aims to detect endpoints of tendencies (i.e. sliding windows), stage two recognizes the
tendency itself inside the window. The research addresses such issues as imbalanced datasets and contradicting
labels, as well as the need for specific quality metrics to keep up with practical applicability. The model can
be used to design an investment strategy though further research in feature engineering and fine calibration is
required.This paper is the full text of the research, presented at the 20th International Conference on Artificial
Intelligence and Soft Computing Web System (ICAISC 2021\).
Zumbach, G. (2019\). “Stochastic regularization for the mean\-variance allocation scheme .” In:Quantitative Finance
19(7\), pp. 1097–1120\.
Despite being based on sound principles, the original Markovitz portfolio allocation theory cannot produce
sound allocations, and restrictions or modifications need to be imposed from outside the theory in order to
obtain meaningful portfolios. This is unsatisfactory, and the reasons for this failure are discussed, in particular,
the unavoidable small eigenvalues of the covariance. Within the original principles of risk minimization and
return maximization, several modifications of the original theory are introduced. First, the strategic and tactical
time horizons are separated. A base long\-term allocation is chosen at the strategic time horizon, while the
portfolio is optimized at the tactical time horizon using information from the price histories. Second, the tactical
portfolio is financed by the strategic one, and a funding operator is introduced. The corresponding optimal
allocation (without constraints) has one free parameter fixing the leverage. Third, the transaction costs are
taken into account. This includes the current re\-allocation cost, but crucially the expected costs of the next
reallocation. This last term depends on the sensitivity of the allocation with respect to the covariance, and the
expectation introduces another dependency on the (inverse) covariance. The new term regularizes the original
minimization problem by modifying the lower part of the spectrum of the covariance, leading to meaningful
portfolios. Without constraints, the final Lagrangian can be minimized analytically, with a solution that has a
structure similar to the original Markovitz solution, but with the inverse covariance regularized by the expected
transaction costs.
140