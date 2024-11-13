# References with abstracts forQWIMproject: Portfolio diversification

# in quantitative wealth and investment management

## Cristian Homescu

## December 2022

```
Abstract
This document includes the list of references (including abstracts) for this QWIM project
```
## Contents

**1 Motivation for the project 2**
1.1 Beware of correlations which are not consistent with intuition...................... 2
1.2 Portfolio optimization............................................ 2
1.3 Portfolio diversification............................................ 2

**2 Relevant references 3**
2.1 Main references................................................ 3
2.2 Comprehensive list of references....................................... 4
2.2.1 Investment portfolios from a diversification perspective...................... 4
2.2.2 Metrics and quantification of portfolio diversification....................... 6
2.2.3 Portfolio diversification through ESG investing.......................... 7
2.2.4 Testing and comparison procedures for investment portfolios.................. 7

**References 9**


## 1 Motivation for the project

### 1.1 Beware of correlations which are not consistent with intuition

In many cases, advanced quantitative approaches (including machine learning) may not necessarily deliver better
results inQWIM, especially when decision making relies on data-based spurious correlations rather than on real
causality.
Vigen ( _Spurious Correlations_ , 2019): many examples of such data-based spurious correlations

- Divorce rate in Maine has 99 % correlation with per capita consumption of margarin
- Per capita consumption of mozzarella cheese has 96 % correlation with civil engineering doctorates awarded
    in US
- Per capita consumption of chicken has 90 % correlation with total US crude oil imports

Example inQWIMLaurinaityte et al. (“Elephants and the Cross-Section of Expected Returns,” 2019): population
growth of captive Asian elephants explains cross-section of expected returns of usually sorted portfolios withR^2 =
0. 91 andtStat= 2. 93 for market price of risk.
_Question: Does it mean that number of captive elephants is the new outstanding factor in empirical asset pricing?_
Answer: Likely it is an artifact due to data mining rather than a proper factor for factor-based investing.

### 1.2 Portfolio optimization

While there are many challenges in a portfolio optimization process relying on the corelation (or covariance) matrix,
some of the most important issues (including potential lack of robustness and diversification) are due to the fact
that correlation matrix lacks the notion of hierarchy.
It was shown that many complex systems can be arranged in a natural hierarchy comprising nested substructures,
and financial markets are no exception. While a correlation matrix makes no differentiation between assets, some
assets seem closer substitutes of one another, while others seem complementary to one another. This can be better
handled through network analysis and clustering.
Networks enable practical usage of high / low centrality concepts

- significant interconnectedness risk (tail events propagate more quickly) due to assets with high centrality
    scores
- "peripheral assets" carry relatively less interconnectedness risk

Network-based and clustering-based portfolio optimization is likely to deliver more robust and diversified portfolios,
and achieve better risk-adjusted performances compared to portfolios obtained using commonly used portfolio
optimization techniques. Since no single clustering algorithm can be said to perform best on all datasets, different
strategies must be tested and compared.

### 1.3 Portfolio diversification

Diversification is one of the most important concepts in the financial world. It is often said that diversification
is the only free lunch in finance. From a qualitative point of view, the concept of diversification is quite clear: a
portfolio is well-diversified if shocks in the individual components do not heavily impact on the overall portfolio.
Relatively simple to understand then but profoundly difficult to define. Indeed, there is no broadly accepted precise
and quantitative definition of diversification.
One of the most vexing problems in investment management is that diversification seems to disappear when
investors need it the most. A key challenge in the construction of diversified multi-asset portfolio strategies is that
even a seemingly well-balanced allocation to many asset classes can eventually translate into a portfolio with a very
concentrated set of underlying risk exposures.
Network analysis applied to structure of investment portfolios is very beneficial to analyze diversification prop-
erties. We can also consider a portfolio selection approach that combines diversification and optimization.


## 2 Relevant references

### 2.1 Main references

List of references:
Anson (“Diversification – A Free Starbucks Cup of Coffee?” 2022)
Bratis et al. (“Dynamics among global asset portfolios,” 2020)
Choi et al. (“Diversified reward-risk parity in portfolio construction,” 2022)
Chua et al. (“The Myth of Diversification,” 2009)
Dees et al. (“Portfolio Cuts: A Graph-Theoretic Framework to Diversification,” 2020)
Eom et al. (“Limitations of portfolio diversification through fat tails of the return Distributions: Some empirical
evidence,” 2021)
Flint et al. (“The Cost of a Free Lunch: Dabbling in Diversification,” 2016)
Flint et al. (“Defining and measuring portfolio diversification,” 2021)
Fusai et al. (“Equally Diversified or Equally Weighted?” 2020)
Jacobsen and Scheiber (“Harvesting Multi-Asset Carry, Value, and Momentum: Work Smarter, Not Harder,”
2022)
Jaeger et al. (“Understanding machine learning for diversified portfolio construction by explainable AI,” 2020)
Jaeger et al. (“Interpretable Machine Learning for Diversified Portfolio Construction,” 2021)
Jaeger et al. (“Adaptive Seriational Risk Parity and other Extensions for Heuristic Portfolio Construction using
Machine Learning and Graph Theory,” 2021)
Kelliher et al. (“A Novel Approach to Risk Parity: Diversification across Risk Factors and Market Regimes,”
2022)
Kinlaw et al. (“The Myth of Diversification Reconsidered,” 2021)
Koumou (“Diversification and portfolio theory: a review,” 2020)
Kurtti (“How many stocks make a diversified portfolio in a continuous-time world?” 2020)
Laur (“Portfolio Optimization - Can Optimizing Portfolio Outperform Naive Diversification?” 2020)
Lim and Ong (“Portfolio Diversification Using Shape-Based Clustering,” 2021)
Lohre et al. (“Hierarchical Risk Parity: Accounting for Tail Dependencies in Multi-asset Multi-factor Alloca-
tions,” 2020)
Lopez de Prado (“Building Diversified Portfolios that Outperform Out of Sample,” 2016)
Lopez de Prado ( _Machine learning for asset managers_ , 2020)
Madan and Wang (“Measuring the Benefits of Diversification Across Portfolios,” 2021)
Martellini and Milhau (“Proverbial Baskets Are Uncorrelated Risk Factors! A Factor-Based Framework for
Measuring and Managing Diversification in Multi-Asset Investment Solutions,” 2018)
Meucci et al. (“Risk budgeting and diversification based on optimised uncorrelated factors,” 2015)
Molyboga (“A Modified Hierarchical Risk Parity Framework for Portfolio Management,” 2020)
Olmo (“Optimal portfolio allocation and asset centrality revisited,” 2021)
Page ( _Beyond Diversification: What Every Investor Needs to Know About Asset Allocation_ , 2020)
Page and Panariello (“When Diversification Fails,” 2018)
Papenbrock et al. (“Matrix Evolutions: Synthetic Correlations and Explainable Machine Learning for Con-
structing Robust Investment Portfolios,” 2021)
Parmentier (“Measures of Portfolio Diversification,” 2018)
Raffinot (“Hierarchical Clustering-Based Asset Allocation,” 2017)
Raffinot (“The Hierarchical Equal Risk Contribution Portfolio,” 2018)
Roncalli (“Advanced Course in Asset Management,” 2021)
Sakurai et al. (“Correlation diversified passive portfolio strategy based on permutation of assets,” 2021)
Scherer (“Adding alternative assets: return enhancement, diversification or hedging?” 2021)
Schwendner et al. (“Adaptive Seriational Risk Parity and Other Extensions for Heuristic Portfolio Construction
Using Machine Learning and Graph Theory,” 2021)
Serur and Avellaneda (“Hierarchical PCA and Modeling Asset Correlations,” 2021)
Swedroe (“The Importance of Diversification in Achieving Long-Term Goals,” 2020)
Taljaard and Maré (“Why has the equal weight portfolio underperformed and what can we do about it?” 2021)
Thiagarajan et al. (“Financial Globalization and Its Implications for Diversification of Portfolio Risk,” 2021)
Yuan and Zhou (“Why Naive 1/N Diversification Is Not So Naive, and How to Beat It?” 2022)


Zaimovic et al. (“How Many Stocks Are Sufficient for Equity Portfolio Diversification? A Review of the Litera-
ture,” 2021)
Zhao et al. (“Robust portfolio rebalancing with cardinality and diversification constraints,” 2021)

### 2.2 Comprehensive list of references

**2.2.1 Investment portfolios from a diversification perspective**

List of references:
Amenc et al. (“Accounting for Cross-Factor Interactions in Multifactor Portfolios without Sacrificing Diversifi-
cation and Risk Control,” 2017)
Ang et al. (“How Many Active Funds Should You Hold?” 2021)
Anson (“Diversification – A Free Starbucks Cup of Coffee?” 2022)
Arroyo et al. (“Dynamic Portfolio Cuts: A Spectral Approach to Graph-Theoretic Diversification,” 2021)
Attig and Sy (“Diversification during Hard Times,” 2021)
Ayres and Nalebuff (“Diversification Across Time,” 2013)
Bakry et al. (“Bitcoin and Portfolio Diversification: A Portfolio Optimization Approach,” 2021)
Banner et al. (“Diversification, Volatility, and Surprising Alpha,” 2019)
Bardoscia et al. (“Lost in Diversification,” 2019)
Barkhagen et al. (“Optimising portfolio diversification and dimensionality,” 2019)
Bennyhoff (“Time Diversification and Horizon-Based Asset Allocations,” 2009)
Bock (“An updated review of (sub-)optimal diversification models,” 2018)
Borsboom et al. (“Domain-dependent diversification: The influence of gain-loss domain and information aggre-
gation on correlation choice,” 2021)
Bratis et al. (“Dynamics among global asset portfolios,” 2020)
Cadenas et al. (“How dark is the dark side of diversification?” 2020)
Candelon et al. (“Diversification Potential in Real Estate Portfolios,” 2021)
Carmichael et al. (“Rao’s quadratic entropy and maximum diversification indexation,” 2018)
Cesarone et al. (“Does Greater Diversification Really Improve Performance in Portfolio Selection?” 2014)
Cesarone et al. (“A risk-gain dominance maximization approach to enhanced index tracking,” 2019)
Choi et al. (“Diversified reward-risk parity in portfolio construction,” 2022)
Choueifaty et al. (“Properties of the most diversified portfolio,” 2013)
Chua et al. (“The Myth of Diversification,” 2009)
Colombo et al. (“The Diversification Benefits of Cryptocurrencies in Multi-Asset Portfolios: Cross-Country
Evidence,” 2021)
Curran and Zalla (“Can Volatility Solve the Naive Diversification Puzzle?” 2021)
Darnell (“Did Diversification Fail?” 2009)
Davis et al. (“The Efficient Frontier and International Portfolio Diversification in Taxable and Tax-Privileged
Accounts,” 2020)
de Carvalho et al. (“Diversify and Purify Factor Premiums in Equity Markets,” 2017)
Dees et al. (“Portfolio Cuts: A Graph-Theoretic Framework to Diversification,” 2020)
Defau and De Moor (“The investment behaviour of pension funds in alternative assets: Interest rates and
portfolio diversification,” 2021)
DeMiguel et al. (“Optimal versus Naive Diversification: how Inefficient is the 1/N Portfolio Strategy,” 2009)
Domian et al. (“Diversification in Portfolios of Individual Stocks: 100 Stocks Are Not Enough,” 2007)
Elkamhi et al. (“The Jury is Still Out On the Performance of Naive Diversification (1/N rule),” 2021)
Elton and Gruber (“A Review of the Performance Measurement of Long-Term Mutual Funds,” 2020)
Flint et al. (“The Cost of a Free Lunch: Dabbling in Diversification,” 2016)
Flores et al. (“The Diversification Delta: A Different Perspective,” 2017)
Fouquau et al. (“International and temporal diversifications: the best of both worlds?” 2018)
Fusai et al. (“Equally Diversified or Equally Weighted?” 2020)
Hallerbach (“If You Have Said A, You Must Also Say B: Calculating Diversified Asset Returns,” 2017)
Heckel et al. (“Factor Investing in Corporate Bond Markets: Enhancing Efficacy Through Diversification and
Purification!” 2020)
Heinrich et al. (“Factor investing: alpha concentration versus diversification,” 2021)


Hoesli and Johner (“Portfolio Diversification across U.S. Gateway and Non-Gateway Real Estate Markets,”
2021)
Hubrich (“Allocating to Liquid Alternative Strategies for Mean–Variance Diversification,” 2021)
Humphrey et al. (“Is diversification always optimal?” 2015)
Ilmanen and Kizer (“The Death of Diversification Has Been Greatly Exaggerated,” 2012)
Jacobs et al. (“How should individual investors diversify? An empirical evaluation of alternative asset allocation
policies,” 2014)
Jacobsen and Ma (“Alpha alchemy: diversifying without diluting alpha,” 2020)
Jacobsen and Scheiber (“Harvesting Multi-Asset Carry, Value, and Momentum: Work Smarter, Not Harder,”
2022)
Jaeger et al. (“Understanding machine learning for diversified portfolio construction by explainable AI,” 2020)
Jaeger et al. (“Interpretable Machine Learning for Diversified Portfolio Construction,” 2021)
Jennings and Payne (“Fees Eat Diversification’s Lunch,” 2016)
Jennings et al. (“Normal return gaps: dispersion illuminates diversification,” 2020)
Kelliher et al. (“A Novel Approach to Risk Parity: Diversification across Risk Factors and Market Regimes,”
2022)
Kinlaw et al. (“The Myth of Diversification Reconsidered,” 2021)
Kritzman (“What Practitioners Need to Know ... About Time Diversification (corrected),” 2015)
Koumou (“Diversification and portfolio theory: a review,” 2020)
Lassance et al. (“Optimal portfolio diversification via independent component analysis,” 2020)
Lassance (“Reconciling Mean-Variance Portfolio Theory with Non-gaussian Returns,” 2021)
Laur (“Portfolio Optimization - Can Optimizing Portfolio Outperform Naive Diversification?” 2020)
Le Courtois (“On the Diversification of Fixed Income Assets,” 2020)
Levy and Levy (“The cost of diversification over time, and a simple way to improve target-date funds,” 2021)
Lim and Ong (“Portfolio Diversification Using Shape-Based Clustering,” 2021)
Lundstrum (“Emerging Market Diversification Benefits: Stock Funds Versus Currency Funds,” 2021)
Louton and Saraoglu (“How Many Mutual Funds Are Needed to Form a Well- Diversified Asset Allocated
Portfolio?” 2008)
Martellini and Milhau (“Proverbial Baskets Are Uncorrelated Risk Factors! A Factor-Based Framework for
Measuring and Managing Diversification in Multi-Asset Investment Solutions,” 2018)
Massahi et al. (“Development of an efficient cluster-based portfolio optimization model under realistic market
conditions,” 2020)
McKay et al. (“What Free Lunch? The Costs of Overdiversification,” 2018)
Meucci et al. (“Risk budgeting and diversification based on optimised uncorrelated factors,” 2015)
Page ( _Beyond Diversification: What Every Investor Needs to Know About Asset Allocation_ , 2020)
Page and Panariello (“When Diversification Fails,” 2018)
Page and Taborsky (“The myth of diversification: risk factors versus asset classes,” 2011)
Papathanakos (“Diversification Potential,” 2020)
Parmentier (“Measures of Portfolio Diversification,” 2018)
Pedersen (“Simple Portfolio Optimization that Works!” 2021)
Pedersen (“Fast Portfolio Diversification,” 2022)
Petukhina et al. (“Investing with cryptocurrencies – evaluating their potential for portfolio allocation strategies,”
2021)
Pham et al. (“Portfolio diversification and model uncertainty: a robust dynamic mean-variance approach,” 2018)
Pham et al. (“Portfolio diversification and model uncertainty: a robust dynamic mean-variance approach,” 2018)
Pittman et al. (“Diversification benefits, where art thou?” 2019)
Platanakis et al. (“Harmful Diversification: Evidence from Alternative Investments,” 2017)
Pola (“On entropy and portfolio diversification,” 2016)
Pourbabaee et al. (“Risk minimization and portfolio diversification,” 2016)
Reinholtz et al. (“Do People Understand the Benefit of Diversification?” 2021)
Sakurai et al. (“Correlation diversified passive portfolio strategy based on permutation of assets,” 2021)
Scalzo et al. (“Nonstationary Portfolios: Diversification in the Spectral Domain,” 2021)
Scherer (“Adding alternative assets: return enhancement, diversification or hedging?” 2021)
Serur and Avellaneda (“Hierarchical PCA and Modeling Asset Correlations,” 2021)


```
Shen et al. (“Asset Allocation and Private Market Investing,” 2021)
Sokolov et al. (“Neural Embeddings of Financial Time-Series Data,” 2020)
Staines et al. (“Dimensions of Diversification,” 2016)
Swedroe (“The Importance of Diversification in Achieving Long-Term Goals,” 2020)
Taljaard and Maré (“Why has the equal weight portfolio underperformed and what can we do about it?” 2021)
Thos (“Naive Diversification with Fewer Assets - A Risk Reduction Approach Using Clustering Methods,” 2020)
Vandenbroucke (“Adaptive Portfolios and the Power of Diversification,” 2019)
Wang et al. (“A Portfolio Diversification Strategy via Tail Dependence Clustering,” 2017)
Yang and Kazemi (“Holdings concentration and hedge fund investment strategies,” 2020)
Yuan and Zhou (“Why Naive 1/N Diversification Is Not So Naive, and How to Beat It?” 2022)
Zaker (“The invisible free lunch,” 2022)
Zhao et al. (“Robust portfolio rebalancing with cardinality and diversification constraints,” 2021)
```
**2.2.2 Metrics and quantification of portfolio diversification**

List of references:
Aked and Ko (“Time Diversification Redux,” 2017)
Allen et al. (“Down-Side Risk Metrics as Portfolio Diversification Strategies across the Global Financial Crisis,”
2016)
Baitinger et al. (“A Wholistic Approach to Diversification Management: The Diversification Delta Strategy
Applied to Non-Normal Return Distributions,” 2015)
Bardoscia et al. (“Lost in Diversification,” 2019)
Bianchi et al. (“The Time Diversification Puzzle: A Survey,” 2016)
Carli et al. ( _Improved Risk Reporting with Factor-Based Diversification Measures_ , 2014)
Carmichael et al. (“Unifying Portfolio Diversification Measures Using Rao’s Quadratic Entropy,” 2015)
Carmichael et al. (“A New Formulation of Maximum Diversification Indexation Using Rao’s Quadratic Entropy,”
2015)
Carmichael et al. (“Rao’s quadratic entropy and maximum diversification indexation,” 2018)
Cesarone and Colucci (“Minimum risk versus capital and risk diversification strategies for portfolio construction,”
2018)
Chollete et al. (“International Diversification: A Copula Approach,” 2011)
Chollete et al. (“International diversification: An extreme value approach,” 2012)
du Plessis and van Rensburg (“Diversification and the realised volatility of equity portfolios,” 2017)
Durante et al. ( _A portfolio diversification strategy via tail dependence measures_ , 2015)
Eom et al. (“Limitations of portfolio diversification through fat tails of the return Distributions: Some empirical
evidence,” 2021)
Fleming (“Diversification and the Distribution of Portfolio Variance, Part 3: Polynomial optimisation for asset
allocation,” 2021)
Fleming and Kroeske (“Diversification and the Distribution of Portfolio Variance, Part 1: Sums of IID Variables
and Higher-Order Moments,” 2020)
Fleming and Kroeske (“Diversification and the Distribution of Portfolio Variance, Part 2: Volatility Stability as
a Measure of Diversification,” 2020)
Fouquau et al. (“International and temporal diversifications: the best of both worlds?” 2018)
Flint et al. (“Defining and measuring portfolio diversification,” 2021)
Heinze (“Markowitz 3.0: Including Diversification Targets in Portfolio Optimization via Diversification Func-
tions,” 2016)
Hjalmarsson (“Portfolio Diversification Across Characteristics,” 2011)
Kashyap (“Combining Dimension Reduction, Distance Measures and Covariance,” 2017)
Kinlaw et al. (“The Myth of Diversification Reconsidered,” 2021)
Koekebakker and Zakamulin (“Warren Buffett versus Zvi Bodie: Should You Buy Or Sell Put Options?” 2021)
Kurtti (“How many stocks make a diversified portfolio in a continuous-time world?” 2020)
Lee (“Risk-Based Asset Allocation: A New Answer to an Old Question?” 2011)
Lee (“Risk Based Asset Allocation,” 2013)
Madan and Wang (“Measuring the Benefits of Diversification Across Portfolios,” 2021)


Nguyen et al. (“Asset Classes and Portfolio Diversification: Evidence from a Stochastic Spanning Approach,”
2020)
Oyenubi (“Diversification Measures and the Optimal Number of Stocks in a Portfolio: An Information Theoretic
Explanation,” 2019)
Parmentier (“Measures of Portfolio Diversification,” 2018)
Pastor et al. (“Portfolio Liquidity and Diversification: Theory and Evidence,” 2017)
Raju and Agarwalla (“Equity Portfolio Diversification: How Many Stocks Are Enough? Evidence From India,”
2021)
Reinholtz et al. (“Do People Understand the Benefit of Diversification?” 2021)
Scalzo et al. (“Nonstationary Portfolios: Diversification in the Spectral Domain,” 2021)
Vermorken et al. (“The Diversification Delta: A Higher-MomentMeasure for Portfolio Diversification,” 2012)
Wang et al. (“A Portfolio Diversification Strategy via Tail Dependence Clustering,” 2017)
Zaimovic et al. (“How Many Stocks Are Sufficient for Equity Portfolio Diversification? A Review of the Litera-
ture,” 2021)

**2.2.3 Portfolio diversification through ESG investing**

List of references:
Balcilar et al. (“Do Sustainable Stocks Offer Diversification Benefits for Conventional Portfolios? An Empirical
Analysis of Risk Spillovers and Dynamic Correlations,” 2017)
De and Clayman (“The Benefits of Socially Responsible Investing: An Active Manager’s Perspective,” 2015)
Giese et al. (“Foundations of ESG investing: how ESG affects equity valuation, risk, and performance,” 2019)
Gougler and Utz (“Factor exposures and diversification: Are sustainably screened portfolios any different?”
2020)
Hambel et al. (“Asset Pricing and Decarbonization: Diversification versus Climate Action,” 2021)
Kilmurray et al. (“Integrating Impact Funds into Mainstream Portfolios,” 2021)
Ouchen (“Is the ESG portfolio less turbulent than a market benchmark portfolio?” 2021)
Rubbaniy et al. (“Are ESG Stocks Safe-Haven during COVID-19?” 2021)
van der Miesen (“The Effect of ESG Screening on Investment Return, Risk and Diversification,” 2021)

**2.2.4 Testing and comparison procedures for investment portfolios**

References:
Adcock et al. (“Portfolio Performance Measurement: Monotonicity with Respect to the Sharpe Ratio and
Multivariate Tests of Correlation,” 2017)
Arnott et al. (“A backtesting protocol in the era of machine learning,” 2019)
Bailey et al. (“Stock Portfolio Design and Backtest Overfitting,” 2017)
Bessler and Wolff (“Portfolio Optimization with Industry Return Prediction Models,” 2017)
Bessler et al. (“Multi-asset portfolio optimization and out-of-sample performance: an evaluation of Black Lit-
terman, mean-variance, and naive diversification approaches,” 2017)
Bjerring et al. (“Feature selection for portfolio optimization,” 2017)
Bruni et al. (“On exact and approximate stochastic dominance strategies for portfolio selection,” 2017)
Bruni et al. (“Real-world datasets for portfolio selection and solutions of some stochastic dominance portfolio
models,” 2016)
Bryzgalova et al. (“Bayesian solutions for the factor zoo: we just ran two quadrillion models,” 2021)
Cesarone et al. (“On the stability of portfolio selection models,” 2019)
Cesarone et al. (“Why Small Portfolios Are Preferable and How to Choose Them,” 2018)
Chaudhuri and Lo (“Dynamic Alpha: A Spectral Decomposition of Investment Performance Across Time Hori-
zons,” 2019)
Diris et al. (“Long-Term Strategic Asset Allocation: An Out-of-Sample Evaluation,” 2015)
Fabozzi and Lopez de Prado (“Being Honest in Backtest Reporting: A Template for Disclosing Multiple Tests,”
2018)
Greiner and Stoyanov (“Portfolio scoring by expected risk premium,” 2019)
Guidolin et al. (“Portfolio performance of linear SDF models: an out-of-sample assessment,” 2018)
Guo (“A Statistical Response to Challenges in Vast Portfolio Selection,” 2019)


Guo et al. (“When Does The 1/N Rule Work?” 2019)
Haley (“K-fold cross validation performance comparisons of six naive portfolio selection rules: how naive can
you be and still have successful out-of-sample portfolio performance?” 2017)
Harvey et al. (“An Evaluation of Alternative Multiple Testing Methods for Finance Applications,” 2020)
Hens et al. (“Escaping the backtesting illusion,” 2020)
Hsu et al. ( _Do Cross-Sectional Stock Return Predictors Pass the Test without Data-Snooping Bias?_ 2017)
Hsu et al. (“Asset allocation strategies, data snooping, and the 1 / N rule,” 2018)
Huang and Yu (“A new procedure for resampled portfolio with shrinkaged covariance matrix,” 2020)
Hwang et al. (“Naive versus optimal diversification: Tail risk and performance,” 2018)
Ielpo et al. ( _Engineering Investment Process: Making Value Creation Repeatable_ , 2017)
Jaeger et al. (“Understanding machine learning for diversified portfolio construction by explainable AI,” 2020)
Kazak and Pohlmeier (“Testing out-of-sample portfolio performance,” 2019)
Kazak and Pohlmeier ( _Portfolio Pretesting with Machine Learning_ , 2020)
Kuntz (“Portfolio Strategies with Classical and Alternative Benchmarks,” 2018)
Lohre et al. (“Hierarchical Risk Parity: Accounting for Tail Dependencies in Multi-asset Multi-factor Alloca-
tions,” 2020)
Lopez de Prado (“A Data Science Solution to the Multiple-Testing Crisis in Financial Research,” 2019)
Lopez de Prado and Lewis (“Detection of false investment strategies using unsupervised learning methods,”
2019)
Malavasi et al. (“Second order of stochastic dominance efficiency vs mean variance efficiency,” 2021)
Mooney et al. (“Dynamic Regime Strategy for Stress Testing and Optimizing Institutional Investor Portfolios,”
2020)
Platanakis et al. (“Horses for Courses: Mean-Variance for Asset Allocation and 1/N for Stock Selection,” 2021)
Radovanov and Marcikic (“Testing The Performance Of The Investment Portfolio Using Block Bootstrap
Method,” 2014)
Rebonato (“A financially justifiable and practically implementable approach to coherent stress testing,” 2019)
Schumann (“Backtesting,” 2019)
Seymour et al. (“Dynamic portfolio management strategies: A framework for historical analysis,” 2018)
Suhonen et al. (“Quantifying Backtest Overfitting in Alternative Beta Strategies,” 2017)
Taljaard and Maré (“Why has the equal weight portfolio underperformed and what can we do about it?” 2021)
Tayali (“A novel backtesting methodology for clustering in mean–variance portfolio optimization,” 2020)
Traccucci et al. (“A Triptych Approach for Reverse Stress Testing of Complex Portfolios,” 2019)
Valentine et al. (“Beyond p values: utilizing multiple methods to evaluate evidence,” 2019)
Vincent et al. (“Analyzing the Performance of Multifactor Investment Strategies under a Multiple Testing
Framework,” 2018)
Vovk and Wang (“True and false discoveries with e-values,” 2020)
Vovk and Wang (“E-values: Calibration, combination, and applications,” 2021)
Wiecki et al. (“All That Glitters Is Not Gold: Comparing Backtest and Out-of-Sample Performance on a Large
Cohort of Trading Algorithms,” 2016)
Yu (“Comparing Classical Portfolio Optimization and Robust Portfolio Optimization on Black Swan Events,”
2021)
Zhang et al. (“DoubleEnsemble: A New Ensemble Method Based on Sample Reweighting and Feature Selection
for Financial Data Analysis,” 2020)
Zhang et al. (“Information Coefficient as a Performance Measure of Stock Selection Models,” 2020)
Zhang et al. (“Deep Learning for Portfolio Optimization,” 2020)


## References

Adcock, C., Areal, N., Armada, M. R., Cortez, M. C., Oliveira, B., and Silva, F. (2017).“Portfolio Performance
Measurement: Monotonicity with Respect to the Sharpe Ratio and Multivariate Tests of Correlation.” In: _SSRN
e-Print_.
This paper reports an investigation into methods of portfolio performance measurement. The work is motivated
first by equivocal empirical evidence reported by several authors about the correlation of performance measures
with the Sharpe ratio. Secondly it is motivated by recent work which specifies that performance measures will
be monotone functions of the Sharpe ratio if portfolio returns follow the same location-scale distribution. The
paper demonstrates that the class of location-scale distributions is broader than previously reported. It presents
conditions under which monotonicity with respect to the Sharpe ratio will fail. The paper shows that for large
sample sizes the correlation between pairs of performance measures that are functions of the Sharpe ratio is
unity. The correct null hypothesis for tests of correlation is therefore rho=1. Two multivariate tests of this
null hypothesis are presented. The new tests are used to carry out of a comprehensive study of performance
measurement for a set over ninety UK investment trusts.
Aked, M. and Ko, A. (2017).“Time Diversification Redux.” In: _SSRN e-Print_.
Conventional risk measures may not accurately describe the volatility investors actually experience, especially
for portfolios servicing their retirement spending needs. Return volatility rises as its calculated holding period
nears 1 year and falls as it lengthens to 10 years. Lower volatility at longer holding periods implies that longer-
term mean reversion exists. A portfolio achieves the greatest extra-return benefit by rebalancing over the holding
period of highest volatility. Time diversification is helpful, up until long-term uncertainty about the value of
reinvested cash flows from dividends leads to rising volatility.
Allen, D., McAleer, M., Powell, R., and Singh, A. (2016).“Down-Side Risk Metrics as Portfolio Diversification
Strategies across the Global Financial Crisis.” In: _Journal of Risk and Financial Management_ 9(2), pp. 6+.
This paper features an analysis of the effectiveness of a range of portfolio diversification strategies, with a focus
on down-side risk metrics, as a portfolio diversification strategy in a European market context. We apply these
measures to a set of daily arithmetically-compounded returns, in U.S. dollar terms, on a set of ten market
indices representing the major European markets for a nine-year period from the beginning of 2005 to the end
of 2013. The sample period, which incorporates the periods of both the Global Financial Crisis (GFC) and
the subsequent European Debt Crisis (EDC), is a challenging one for the application of portfolio investment
strategies. The analysis is undertaken via the examination of multiple investment strategies and a variety of
hold-out periods and backtests. We commence by using four two-year estimation periods and a subsequent one-
year investment hold out period, to analyse a naive 1/N diversification strategy and to contrast its effectiveness
with Markowitz mean variance analysis with positive weights. Markowitz optimisation is then compared to
various down-side investment optimisation strategies. We begin by comparing Markowitz with CVaR, and then
proceed to evaluate the relative effectiveness of Markowitz with various draw-down strategies, utilising a series
of backtests. Our results suggest that none of the more sophisticated optimisation strategies appear to dominate
naive diversification.
Amenc, N., Ducoulombier, F., Esakia, M., Goltz, F., and Sivasubramanian, S. (2017).“Accounting for Cross-Factor
Interactions in Multifactor Portfolios without Sacrificing Diversification and Risk Control.” In: _The Journal of
Portfolio Management_ 43(5), pp. 99–114.
In this article, the authors compare different approaches for constructing multifactor equity portfolios: bottom-
up score-weighting approaches that target high-factor intensity and top-down approaches that also consider
diversification objectives. They find that focusing solely on increasing factor intensity leads to inefficiency in
capturing factor premia, because exposure to unrewarded risks more than offsets the benefits of increased factor
scores. High factor scores in bottom-up approaches also come with high instability and turnover. The authors
introduce an approach that considers cross-factor interactions in top-down portfolios through an adjustment at
the stock-selection level. While producing lower factor intensity than bottom-up methods, this approach leads
to higher levels of diversification and produces higher returns per unit of factor intensity. The authors report
that it dominates bottom-up approaches in terms of relative performance, while considerably reducing extreme
relative losses and turnover.
Ang, A., Madhavan, A., and Ribando, J. (2021).“How Many Active Funds Should You Hold?” In: _SSRN e-Print_.
Traditional quantitative approaches to portfolio construction have drawbacks for investors or advisors who
combine multiple active managers in typically producing large numbers of disperse positions. We develop a new


methodology for sequentially allocating to active funds that results in parsimonious numbers of funds and test
our results on US active equity mutual funds. To initiate the algorithm, we choose the fund with the highest
information ratio (IR). Then, we select the next fund that produces the highest increase in the portfolio’s IR,
noting that the IRs of the remaining funds depend on the current active portfolio. This procedure is repeated
as long as the active risk of the portfolio is above a minimum threshold. Under certain conditions, the problem
nests the well-known Knapsack Problem. The algorithm generates approximately the same IRs with significantly
smaller numbers of funds than traditional mean-variance optimizations.
Anson, M. (2022).“Diversification – A Free Starbucks Cup of Coffee?” In: _The Journal of Portfolio Management_
48(4), pp. 220–227.
Diversification of sophisticated portfolios has become more difficult. In the past, asset class and geographic
dispersion were sufficient to ensure a properly diversified portfolio. Not so anymore, as major economies integrate
and coordinate their monetary and fiscal policies. In addition, the growth of the exchange-traded fund market
has impinged on what was previously the alpha hunting ground of active managers, blurring the distinction
between what is beta and what is alpha. This article shows how multi-asset solutions can be used to expand the
free lunch of diversification back to its full potential.
Arnott, R. D., Harvey, C. R., and Markowitz, H. (2019).“A backtesting protocol in the era of machine learning.”
In: _The Journal of Financial Data Science_ 1(1), pp. 64–74.
Machine learning offers a set of powerful tools that holds considerable promise for investment management. As
with most quantitative applications in finance, the danger of misapplying these techniques can lead to disap-
pointment. One crucial limitation involves data availability. Many of machine learning early successes originated
in the physical and biological sciences, in which truly vast amounts of data are available. Machine learning
applications often require far more data than are available in finance, which is of particular concern in longer-
horizon investing. Hence, choosing the right applications before applying the tools is important. In addition,
capital markets reflect the actions of people, which may be influenced by others actions and by the findings
of past research. In many ways, the challenges that affect machine learning are merely a continuation of the
long-standing issues researchers have always faced in quantitative finance. While investors need to be cautious,
more cautious than in past applications of quantitative methods new tools offer many potential applications in
finance. In this article, the authors develop a research protocol that pertains both to the application of machine
learning techniques and to quantitative finance in general.
Arroyo, A., Scalzo, B., Stankovic, L., and Mandic, D. P. (2021).“Dynamic Portfolio Cuts: A Spectral Approach to
Graph-Theoretic Diversification.” In: _arXiv e-Print_.
Stock market returns are typically analyzed using standard regression, yet they reside on irregular domains which
is a natural scenario for graph signal processing. To this end, we consider a market graph as an intuitive way to
represent the relationships between financial assets. Traditional methods for estimating asset-return covariance
operate under the assumption of statistical time-invariance, and are thus unable to appropriately infer the
underlying true structure of the market graph. This work introduces a class of graph spectral estimators which
cater for the nonstationarity inherent to asset price movements, and serve as a basis to represent the time-varying
interactions between assets through a dynamic spectral market graph. Such an account of the time-varying nature
of the asset-return covariance allows us to introduce the notion of dynamic spectral portfolio cuts, whereby the
graph is partitioned into time-evolving clusters, allowing for online and robust asset allocation. The advantages
of the proposed framework over traditional methods are demonstrated through numerical case studies using
real-world price data.
Attig, N. and Sy, O. (2021).“Diversification during Hard Times.” In: _SSRN e-Print_.
Using a large sample of stocks from 48 developed and emerging markets, we show that the benefits of diversifi-
cation persist during the global financial crisis, the coronavirus pandemic, and other hard times, demonstrating
their countercyclicality. This result suggests that the benefits of holding an international portfolio are not re-
duced when investors need them the most. While international diversification is the best risk-reduction tool
when developed and emerging markets are jointly considered, we find that after the turn of the millennium,
industrial diversification is the best alternative for funds limited to developed markets.
Ayres, I. and Nalebuff, B. (2013).“Diversification Across Time.” In: _The Journal of Portfolio Management_ 39(2),
pp. 73–86.
Young people who buy stock on margin and reduce their equity exposure as they age can reduce lifetime portfolio
risk. For example, an initially leveraged portfolio produces the same mean accumulation as a constant 74 percent
stock allocation with a 21 percent smaller standard deviation. Since the means are equal, the reduced volatility


doesn’t depend on the equity premium. A leveraged life-cycle strategy also lets investors come closer to their
utility-maximizing equity allocation. Monte Carlo simulations show that the gains continue even with equity
premiums well below historical levels.
Bailey, D. H., Borwein, J. M., and Lopez de Prado, M. (2017).“Stock Portfolio Design and Backtest Overfitting.”
In: _Journal of Investment Management_ 15(1), pp. 75–87.
In mathematical finance, backtest overfitting connotes the usage of historical market data to develop an invest-
ment strategy, where too many variations of the strategy are tried, relative to the amount of data available.
Backtest overfitting is now thought to be a primary reason why investment models and strategies that look
good on paper often disappoint in practice. Models and strategies suffering from overfitting typically target the
specific idiosyncrasies of a limited dataset, rather than any general behavior, and, as a result, often perform
erratically when presented with new data. In this study, we address overfitting in the context of designing a
mutual fund or investment portfolio as a weighted collection of stocks. Very often a newly minted equity-based
fund of this type has been designed by an exhaustive computer-based search of some sort to obtain an optimal
weighting that exhibits excellent performance based, say, on the past 10 or 20 years’ historical market data, and
the fund often highlights this backtest performance.
Baitinger, E., Kutsarov, I., Maier, T., Storr, M., and Wan, T. (2015).“A Wholistic Approach to Diversification
Management: The Diversification Delta Strategy Applied to Non-Normal Return Distributions.” In: _Credit and
Capital Markets - Kredit und Kapital_ 48(1), pp. 89–119.
In this paper we study a higher moment diversification measure, the so-called diversification delta (Vermorken
et al. (2012)), in a dynamic portfolio optimization context. Particularly, we set up an investment strategy that
dynamically maximizes the diversification delta for a given set of assets. Thus, we label the resulting optimized
portfolio structure as Maximum Diversification Delta Portfolio (MDDP). Our out-of-sample empirical study
reveals that considering crisis-periods, the MDDP is superior to popular investment strategies, such as Minimum-
Variance-Portfolio, Risk-Parity-Portfolio and Equally-Weighted-Portfolio, in terms of risk adjusted returns, risk
moments and certainty equivalents. However, in line with other diversification measures the MDDP is no longer
superior in upward trending markets.
Bakry, W., Rashid, A., Al-Mohamad, S., and El-Kanj, N. (2021).“Bitcoin and Portfolio Diversification: A Portfolio
Optimization Approach.” In: _Journal of Risk and Financial Management_ 14(7), p. 282.
This study investigates the performance of Bitcoin as a diversifier under different constraining portfolio opti-
mization frameworks. The study employs different constraining optimization frameworks that seek to maximize
risk-adjusted returns (Sharpe ratio) of the portfolio by optimizing allocations to each asset class (asset allo-
cation). The performance attributes are evaluated by comparing the portfolios both with and without Bitcoin
under frameworks ranging from equal-weighted, risk-parity, and semi-constrained to unconstrained. This study
suggests that Bitcoin, due to its exotic nature, unwavering appeal, and unknown set of drivers, could act as a
diversifier in normal market conditions, and it might also have some borderline hedge to safe haven properties.
The results further suggest that while Bitcoin may be a potential diversifier for a risk-seeking investor, the risk-
averse investor must exercise caution by limiting their exposure to Bitcoin in their portfolios, as unnecessary
exposure may increase the probability of losses in extreme market conditions.
Balcilar, M., Demirer, R., and Gupta, R. (2017).“Do Sustainable Stocks Offer Diversification Benefits for Conven-
tional Portfolios? An Empirical Analysis of Risk Spillovers and Dynamic Correlations.” In: _Sustainability_ 9(10),
p. 1799.
This paper explores the potential diversification benefits of socially responsible investments for conventional stock
portfolios by examining the risk spillovers and dynamic correlations between conventional and sustainability
stock indexes from a number of regions. We observe significant unidirectional volatility transmissions from
conventional to sustainable equities, suggesting that the criteria applied for socially responsible investments
do not necessarily shield these securities from common market shocks. While significant dynamic correlations
are observed between sustainable and conventional stocks, particularly in Europe, the analysis of both in- and
out-of-sample dynamic portfolios suggests that supplementing conventional stock portfolios with sustainable
counterparts improves the risk/return profile of stock portfolios in all regions. The findings overall suggest that
sustainable investments can indeed provide diversification gains for conventional stock portfolios globally.
Banner, A., Fernholz, E. R. R., Papathanakos, V., Ruf, J., and Schofield, D. (2019).“Diversification, Volatility, and
Surprising Alpha.” In: _Journal of Investment Consulting_ 19(1), pp. 23–30.
It has been widely observed that capitalization-weighted indexes can be beaten by surprisingly simple, systematic
investment strategies. Indeed, in the U.S. stock market, equal-weighted portfolios, random-weighted portfolios,


and other naive, non-optimized portfolios tend to outperform a capitalization-weighted index over the long
term. This outperformance is generally attributed to beneficial factor exposures. Here, we provide a deeper,
more general explanation of this phenomenon by decomposing portfolio log-returns into an average growth and
an excess growth component. Using a rank-based empirical study we argue that the excess growth component
plays the major role in explaining the outperformance of naive portfolios. In particular, individual stock growth
rates are not as critical as is traditionally assumed.
Bardoscia, M., d’Arienzo, D., Marsili, M., and Volpati, V. (2019).“Lost in Diversification.” In: _SSRN e-Print_.
As financial instruments grow in complexity more and more information is neglected by risk optimization
practices. This brings down a curtain of opacity on the origination of risk, that has been one of the main culprits
in the 2007-2008 global financial crisis. We discuss how the loss of transparency may be quantified in bits,
using information theoretic concepts. We find that i) financial transformations imply large information losses,
ii) portfolios are more information sensitive than individual stocks only if fundamental analysis is sufficiently
informative on the co-movement of assets, that iii) securitisation, in the relevant range of parameters, yields assets
that are less information sensitive than the original stocks and that iv) when diversification (or securitisation)
is at its best (i.e. when assets are uncorrelated) information losses are maximal. We also address the issue of
whether pricing schemes can be introduced to deal with information losses. This is relevant for the transmission
of incentives to gather information on the risk origination side. Within a simple mean variance scheme, we find
that market incentives are not generally sufficient to make information harvesting sustainable.
Barkhagen, M., Fleming, B., Quiles, S. G., Gondzio, J., Kalcsics, J., Kroeske, J., Sabanis, S., and Staal, A. (2019).
“Optimising portfolio diversification and dimensionality.” In: _arXiv e-Print_.
A new framework for portfolio diversification is introduced which goes beyond the classical mean-variance
approach and portfolio allocation strategies such as risk parity. It is based on a novel concept called portfolio
dimensionality that connects diversification to the non-Gaussianity of portfolio returns and can typically be
defined in terms of the ratio of risk measures which are homogenous functions of equal degree. The latter
arises naturally due to our requirement that diversification measures should be leverage invariant. We introduce
this new framework and argue the benefits relative to existing measures of diversification in the literature,
before addressing the question of optimizing diversification or, equivalently, dimensionality. Maximising portfolio
dimensionality leads to highly non-trivial optimization problems with objective functions which are typically
non-convex and potentially have multiple local optima. Two complementary global optimization algorithms are
thus presented. For problems of moderate size and more akin to asset allocation problems, a deterministic
Branch and Bound algorithm is developed, whereas for problems of larger size a stochastic global optimization
algorithm based on Gradient Langevin Dynamics is given. We demonstrate analytically and through numerical
experiments that the framework reflects the desired properties often discussed in the literature.
Bennyhoff, D. G. (2009).“Time Diversification and Horizon-Based Asset Allocations.” In: _The Journal of Investing_
18(1), pp. 45–52.
Time diversification, the concept that investments in stocks are less risky over longer periods than shorter ones,
has been the subject of spirited debate for decades. Over the last few years the growing acceptance of life cycle
investment products, such as target retirement mutual funds, has renewed interest in this topic. The objective
of this article is not to prove or disprove time diversification, but to evaluate whether the concept must be valid
for a horizon-based asset allocation framework to be viable and appropriate. Our findings suggest that there
is little evidence to support the notion that time moderates the perceived volatility inherent in risky assets.
However, we would expect the risk/reward relationships of the past to prevail in the future, and if that is the
case, a longer investment horizon may support a willingness and ability to assume the greater uncertainty of
equity-centric asset allocations. This may be true particularly for younger investors for whom the allocation to
human capital and the risk posed by the erosion of purchasing power by inflation can reasonably be assumed to
be greatest.
Bessler, W., Opfer, H., and Wolff, D. (2017).“Multi-asset portfolio optimization and out-of-sample performance: an
evaluation of Black Litterman, mean-variance, and naive diversification approaches.” In: _The European Journal
of Finance_ 23(1), pp. 1–30.
The Black Litterman model aims to enhance asset allocation decisions by overcoming the problems of mean-
variance portfolio optimization. We propose a sample-based version of the Black Litterman model and implement
it on a multi-asset portfolio consisting of global stocks, bonds, and commodity indices, covering the period from
January 1993 to December 2011. We test its out-of-sample performance relative to other asset allocation models
and find that Black Litterman optimized portfolios significantly outperform na ive-diversified portfolios (1/N


rule and strategic weights), and consistently perform better than mean-variance, Bayes Stein, and minimum-
variance strategies in terms of out-of-sample Sharpe ratios, even after controlling for different levels of risk
aversion, investment constraints, and transaction costs. The BL model generates portfolios with lower risk, less
extreme asset allocations, and higher diversification across asset classes. Sensitivity analyses indicate that these
advantages are due to more stable mixed return estimates that incorporate the reliability of return predictions,
smaller estimation errors, and lower turnover.
Bessler, W. and Wolff, D. (2017).“Portfolio Optimization with Industry Return Prediction Models.” In: _SSRN
e-Print_.
We postulate that utilizing return prediction models with fundamental, macroeconomic, and technical indica-
tors instead of using historical averages should result in superior asset allocation decisions. We investigate the
predictive power of individual variables for forecasting industry returns in-sample and out-of-sample and then
analyze multivariate predictive regression models including OLS, a regularization technique, principal compo-
nents, a target-relevant latent factor approach, and forecast combinations. The gains from using industry return
predictions are evaluated in an out-of-sample Black-Litterman portfolio optimization framework. We provide em-
pirical evidence that portfolio optimization utilizing industry return prediction models significantly outperform
portfolios using historical averages and those being passively managed.
Bianchi, R., Drew, M., and Walk, A. (2016).“The Time Diversification Puzzle: A Survey.” In: _Financial Planning
Research Journal_.
Since Samuelson’s (1969) theoretical proof that risk and time are unrelated, a half century of debate and
controversy has ensued, leaving time diversification as one of the most enduring puzzles of modern finance. The
most conspicuous aspect of the debate is the questionable assumptions that underlie much of the analysis. Thus
we are left with an unsatisfying debate conducted in a paradigm where terminal wealth is usually a function
only of returns, and where time-weighted measures are assumed to adequately evaluate performance. This paper
reviews the major streams in the time diversification literature and argues that more realistic analysis using
defensible assumptions is likely to lead to better prescriptions for improved retirement investing.
Bjerring, T., Ross, O., and Weissensteiner, A. (2017).“Feature selection for portfolio optimization.” In: _Annals of
Operations Research_ 256, pp. 21–40.
Most portfolio selection rules based on the sample mean and covariance matrix perform poorly out-of-sample.
Moreover, there is a growing body of evidence that such optimization rules are not able to beat simple rules
of thumb, such as 1/N. Parameter uncertainty has been identified as one major reason for these findings. A
strand of literature addresses this problem by improving the parameter estimation and/or by relying on more
robust portfolio selection methods. Independent of the chosen portfolio selection rule, we propose using feature
selection first in order to reduce the asset menu. While most of the diversification benefits are preserved, the
parameter estimation problem is alleviated. We conduct out-of-sample back-tests to show that in most cases
different well-established portfolio selection rules applied on the reduced asset universe are able to improve alpha
relative to different prominent factor models.
Bock, J. (2018).“An updated review of (sub-)optimal diversification models.” In: _arXiv e-Print_.
In the past decade many researchers have proposed new optimal portfolio selection strategies to show that
sophisticated diversification can outperform the naive 1/N strategy in out-of-sample benchmarks. Providing
an updated review of these models since DeMiguel et al. (2009b), I test sixteen strategies across six empirical
datasets to see if indeed progress has been made. However, I find that none of the recently suggested strategies
consistently outperforms the 1/N or minimum-variance approach in terms of Sharpe ratio, certainty-equivalent
return or turnover. This suggests that simple diversification rules are not in fact inefficient, and gains promised by
optimal portfolio choice remain unattainable out-of-sample due to large estimation errors in expected returns.
Therefore, further research effort should be devoted to both improving estimation of expected returns, and
possibly exploring diversification rules that do not require the estimation of expected returns directly, but also
use other available information about the stock characteristics.
Borsboom, C., Duxbury, D., and Zeisberger, S. (2021).“Domain-dependent diversification: The influence of gain-loss
domain and information aggregation on correlation choice.” In: _SSRN e-Print_.
Despite the compelling evidence on gain-loss-domain-dependent behavior, research on domain-dependent port-
folio diversification is scarce. In an online experimental study, we recruited 251 experienced US retail investors
to select portfolios that differ in asset correlation and risk measures in both the gain and the loss domain.
Our findings unveil that diversification behavior is domain-dependent and interacts with the level of informa-
tion aggregation. Presenting aggregated portfolio outcomes prompts portfolio choices consistent with prospect


theory risk preferences and generally higher levels of portfolio diversification. In contrast, displaying individual
stock outcomes results in more diversified portfolios in the loss compared to the gain domain on average, in
line with previous evidence suggesting that individuals do not accurately understand the concept of portfolio
diversification.
Bratis, T., Laopodis, N. T., and Kouretas, G. P. (2020).“Dynamics among global asset portfolios.” In: _The European
Journal of Finance_ 26(18), pp. 1876–1899.
We examine the dynamic correlations among several global financial assets with an eye to potential portfolio di-
versification benefits during the 2008 US financial crisis and EMU sovereign debt crisis of the 2010s. Our findings
are summarized as follows: First, evidence for rigorous, dynamic cross-correlations among global equities around
the 2008 crisis suggested a weak global diversification potential. Second, financial spillovers strengthened in the
post-crisis period thus, exhibiting cycles of inter-linkages among various assets classes. Third, heterogeneous
global portfolios (that is, portfolios formed by various asset classes) offered greater returns than homogeneous
portfolios for the whole period and especially in the period preceding the 2008 crisis. Overall, we conclude
that the US and EMU crisis periods did not affect assets in the same way and hence, risk managers should
follow portfolio-construction strategies with risk-offsetting assets (such as commodities) with regard to their
cyclical/countercyclical movements.
Bruni, R., Cesarone, F., Scozzari, A., and Tardella, F. (2016).“Real-world datasets for portfolio selection and
solutions of some stochastic dominance portfolio models.” In: _Data in Brief_ 8, pp. 858–862.
A large number of portfolio selection models have appeared in the literature since the pioneering work of
Markowitz. However, even when computational and empirical results are described, they are often hard to
replicate and compare due to the unavailability of the datasets used in the experiments. We provide here several
datasets for portfolio selection generated using real-world price values from several major stock markets. The
datasets contain weekly return values, adjusted for dividends and for stock splits, which are cleaned from errors
as much as possible. The datasets are available in different formats, and can be used as benchmarks for testing the
performances of portfolio selection models and for comparing the efficiency of the algorithms used to solve them.
We also provide, for these datasets, the portfolios obtained by several selection strategies based on Stochastic
Dominance models (see ”On Exact and Approximate Stochastic Dominance Strategies for Portfolio Selection”
(Bruni et al. [2])). We believe that testing portfolio models on publicly available datasets greatly simplifies the
comparison of the different portfolio selection strategies.
Bruni, R., Cesarone, F., Scozzari, A., and Tardella, F. (2017).“On exact and approximate stochastic dominance
strategies for portfolio selection.” In: _European Journal of Operational Research_ 259(1), pp. 322–329.
New type of approximate stochastic dominance designed for portfolio selection. Equivalent to minimizing the
expected shortfall of the portfolio below the benchmark. An easily solvable LP model for the practical implemen-
tation of our approach. Extensive empirical comparison of stochastic dominance models for portfolio selection.
One recent and promising strategy for Enhanced Indexation is the selection of portfolios that stochastically
dominate the benchmark. We propose here a new type of approximate stochastic dominance rule which implies
other existing approximate stochastic dominance rules. We then use it to find the portfolio that approximately
stochastically dominates a given benchmark with the best possible approximation. Our model is initially for-
mulated as a Linear Program with exponentially many constraints, and then reformulated in a more compact
manner so that it can be very efficiently solved in practice. This reformulation also reveals an interesting finan-
cial interpretation. We compare our approach with several exact and approximate stochastic dominance models
for portfolio selection. An extensive empirical analysis on real and publicly available datasets shows very good
out-of-sample performances of our model.
Bryzgalova, S., Huang, J., and Julliard, C. (2021).“Bayesian solutions for the factor zoo: we just ran two quadrillion
models.” In: _SSRN e-Print_.
We propose a novel, and simple, Bayesian estimation and model selection procedure for cross-sectional asset
pricing. Our approach, that allows for both tradable and non-tradable factors, and is applicable to high dimen-
sional cases, has several desirable properties. First, weak and spurious factors lead to diffuse, and centered at
zero, posteriors for their market price of risk, making such factors easily detectable. Second, posterior inference is
robust to the presence of such factors. Third, we show that flat priors for risk premia lead to improper marginal
likelihoods, rendering model selection invalid. Therefore, we provide a novel prior, that is diffuse for strong
factors but shrinks away useless ones, under which posterior probabilities are well behaved, and can be used
for factor and (non necessarily nested) model selection, as well as model averaging, in large scale problems. We


apply our method to a very large set of factors proposed in the literature, and analyse 2.25 quadrillion possible
models, gaining novel insights on the empirical drivers of asset returns.
Cadenas, P., Gzyl, H., and Park, H. W. (2020).“How dark is the dark side of diversification?” In: _arXiv e-Print_.
Against the widely held belief that diversification at banking institutions contributes to the stability of the
financial system, Wagner (2010) found that diversification actually makes systemic crisis more likely. While it
is true, as Wagner asserts, that the probability of joint default of the diversified portfolios is larger; we contend
that, as common practice, the effect of diversification is examined with respect to a risk measure like VaR. We
find that when banks use VaR, diversification does reduce individual and systemic risk. This, in turn, generates
a different set of incentives for banks and regulators.
Candelon, B., Fuerst, F., and Hasse, J.-B. (2021).“Diversification Potential in Real Estate Portfolios.” In: _SSRN
e-Print_.
In this paper, we study the international and sectoral diversification potential in real estate portfolios. Building
on a unique dataset of direct real estate markets covering 16 OECD countries over the 1999-2018 period, we intro-
duce a statistical test to compare country-level and sector-level diversification potential. This new diversification
test provides investors and analysts with a valuable tool as it delivers both estimates and robust significance lev-
els. The empirical findings for real estate investments broadly reveal that international diversification dominates
sectoral diversification.
Carli, T., Deguest, R., and Martellini, L. (2014). _Improved Risk Reporting with Factor-Based Diversification Mea-
sures_. Tech. rep. EDHEC-Risk Institute.
This paper analyses various measures of portfolio diversification, and explores the implication in terms of ad-
vanced risk reporting techniques. We use the minimal linear torsion approach (Meucci et al. (2013)) to turn
correlated constituents into uncorrelated factors, and focus on the effective number of (uncorrelated) bets (ENB),
the entropy of the distribution of risk factor contribution to portfolio risk, as a meaningful measure of the de-
gree of diversification in a portfolio. In an attempt to assess whether a relationship exists between the degree
of diversification of a portfolio and its performance in various market conditions, we empirically analyse the
diversification of various equity indices and pension fund policy portfolios. We find strong evidence of a signif-
icantly positive time-series and cross-sectional relationship between the ENB risk diversification measure and
performance in bear markets. This relationship, however, is highly linear, and the top performing portfolios in
severe bear markets are typically portfolios concentrated in safe assets, as opposed to well-diversified portfolios.
We also find statistical and economic evidence that this diversification measure has predictive power for equity
market returns, a predictive power which becomes substantial over long holding period. Overall our results
suggest that the ENB measure could be a useful addition to the list of risk indicators reported for equity and
policy portfolios.
Carmichael, B., Koumou, G., and Moran, K. (2015a).“A New Formulation of Maximum Diversification Indexation
Using Rao’s Quadratic Entropy.” In: _SSRN e-Print_.
This paper proposes a new formulation of the Maximum Diversification indexation strategy based on Rao
Quadratic Entropy (RQE). It clarifies the investment problem underlying the Most Diversified Portfolio (MDP)
formed with this strategy, identifies the source of the MDP out-of-sample performance, and suggests dimensions
along which this performance can be improved. We show that these potential improvements are quantitatively
important and are robust to portfolio turnover, portfolio risk, estimation window, and covariance matrix esti-
mation.
Carmichael, B., Koumou, G., and Moran, K. (2015b).“Unifying Portfolio Diversification Measures Using Rao’s
Quadratic Entropy.” In: _SSRN e-Print_.
This paper extends the use of Rao (1982b)’s Quadratic Entropy (RQE) to modern portfolio theory. It argues
that the RQE of a portfolio is a valid, flexible and unifying approach to measuring portfolio diversification. The
paper demonstrates that portfolio’s RQE can encompass most existing measures, such as the portfolio variance,
the diversification ratio, the normalized portfolio variance, the diversification return or excess growth rates, the
Gini-Simpson indices, the return gaps, Markowitz’s utility function and Bouchaud’s general free utility. The
paper also shows that assets selected under RQE can protect portfolios from mass destruction (systemic risk)
and an empirical illustration suggests that this protection is substantial.
Carmichael, B., Koumou, G. B., and Moran, K. (2018).“Rao’s quadratic entropy and maximum diversification
indexation.” In: _Quantitative Finance_ 18(6), pp. 1017–1031.
This paper proposes a new formulation of the maximum diversification indexation strategy based on Rao’s
Quadratic Entropy. It clarifies the investment problem underlying this diversification strategy, identifies the


source of its out-of-sample performance, and suggests new dimensions along which this performance can be
improved. We show that these potential improvements are quantitatively important and are robust to portfolio
turnover, portfolio risk, estimation window, and covariance matrix estimation.
Cesarone, F. and Colucci, S. (2018).“Minimum risk versus capital and risk diversification strategies for portfolio
construction.” In: _Journal of the Operational Research Society_ 69(2), pp. 183–200.
In this paper, we propose an extensive empirical analysis on three categories of portfolio selection models with
very different objectives: minimization of risk, maximization of capital diversification, and uniform distribution
of risk allocation. The latter approach, also called Risk Parity or Equal Risk Contribution (ERC), is a recent
strategy for asset allocation that aims at equally sharing the risk among all the assets of the selected portfolio.
The risk measure commonly used to select ERC portfolios is volatility. We propose here new developments of
the ERC approach using Conditional Value-at-Risk (CVaR) as a risk measure. Furthermore, under appropriate
conditions, we also provide an approach to find a CVaR ERC portfolio as a solution of a convex optimization
problem. We investigate how these classes of portfolio models (Minimum-Risk, Capital-Diversification, and Risk-
Diversification) work on seven investment universes, each with different sources of risk, including equities, bonds,
and mixed assets. Then, we highlight some strengths and weaknesses of all portfolio strategies in terms of various
performance measures.
Cesarone, F., Lampariello, L., and Sagratella, S. (2019a).“A risk-gain dominance maximization approach to en-
hanced index tracking.” In: _Finance Research Letters_ 29, pp. 231–238.
Following the research strands of enhanced index tracking and of portfolio performance measures optimization,
we propose to choose, among the feasible asset portfolios of a given market, the one that maximizes the geometric
mean of the differences between its risk and gain and those of a suitable reference benchmark, such as the market
index. This approach, which has a peculiar geometric interpretation and enjoys remarkable features, provides
the efficient portfolio that dominates the largest amount of portfolios dominating the reference benchmark index.
Preliminary empirical results highlight good out-of-sample performances of our approach compared with those
of the market index.
Cesarone, F., Moretti, J., and Tardella, F. (2014).“Does Greater Diversification Really Improve Performance in
Portfolio Selection?” In: _SSRN e-Print_.
One of the fundamental principles in portfolio selection models is minimization of risk through diversification
of the investment. This seems to require that in a given working universe, or market, the investment should be
spread among all (or almost all) the available assets. Indeed, this is what some classical investment strategies,
like Equally-Weighted portfolios, or more recent and refined ones, like Risk Parity, actually recommend. The
purpose of this work consists in giving some empirical evidence of the fact that diversifying through the use of
larger portfolios is not the best way to achieve an improvement in out-of-sample performance. More precisely,
we investigate the role of the restriction on the number of assets in a portfolio (a cardinality constraint) on
the in-sample and out-of-sample outcomes of the Equally-Weighted approach and of some well-known portfolio
selection models that minimize risk through the use of Variance, Semi-Mean Absolute Deviation, and Conditional
Value-at-Risk. Our empirical analysis is based on some new and on some publicly available benchmark data sets
often used in the literature.
Cesarone, F., Moretti, J., and Tardella, F. (2018).“Why Small Portfolios Are Preferable and How to Choose Them.”
In: _SSRN e-Print_.
One of the fundamental principles in portfolio selection models is minimization of risk through diversification of
the investment. However, this principle does not necessarily translate into a request for investing in all the assets
of the investment universe. Indeed, following a line of research started by Evans and Archer almost 50 years
ago, we provide here further evidence that small portfolios are sufficient to achieve almost optimal in-sample
risk reduction with respect to variance and to some other popular risk measures, and very good out-of-sample
performances. While leading to similar results, our approach is significantly different from the classical one
pioneered by Evans and Archer. Indeed, we describe models for choosing the portfolio of a prescribed size with
the smallest possible risk, as opposed to the random portfolio choice investigated in most of the previous works.
We find that the smallest risk portfolios generally require no more than 15 assets. Furthermore, it is almost
always possible to find portfolios that are just 1% more risky than the smallest risk portfolios and contain no
more than 10 assets. The preference for small optimal portfolios is also justified by recent theoretical results on
the estimation errors for the parameters required by portfolio selection models. Our empirical analysis is based
on some new and on some publicly available benchmark data sets often used in the literature.


Cesarone, F., Mottura, C., Ricci, J. M., and Tardella, F. (2019b).“On the stability of portfolio selection models.”
In: _SSRN e-Print_.
One of the main issues in portfolio selection models consists in assessing the effect of the estimation errors of the
parameters required by the models on the quality of the selected portfolios. Several studies have been devoted to
this topic for the minimum variance and for several other minimum risk models. However, no sensitivity analysis
seems to have been reported for the recent popular Risk Parity diversification approach, nor for other portfolio
selection models requiring maximum gain-risk ratios.Based on artificial and real-world data, we provide here
empirical evidence showing that the Risk Parity model is always the most stable one in all the cases analyzed.
Furthermore, the minimum risk models are typically more stable than the maximum gain-risk models, with the
minimum variance model often being the preferable one.
Chaudhuri, S. E. and Lo, A. W. (2019).“Dynamic Alpha: A Spectral Decomposition of Investment Performance
Across Time Horizons.” In: _Management Science_ 65(9), pp. 4440–4450.
The value added by an active investor is traditionally measured using alpha, tracking error, and the information
ratio. However, these measures do not characterize the dynamic component of investor activity, nor do they
consider the time horizons over which weights are changed. In this paper, we propose a technique to measure the
value of active investment that captures both the static and dynamic contributions of an investment process. This
dynamic alpha is based on the decomposition of a portfolio’s expected return into its frequency components using
spectral analysis. The result is a static component that measures the portion of a portfolio’s expected return
resulting from passive investments and security selection and a dynamic component that captures the manager’s
timing ability across a range of time horizons. Our framework can be universally applied to any portfolio and
is a useful method for comparing the forecast power of different investment processes. Several analytical and
empirical examples are provided to illustrate the practical relevance of this decomposition.
Choi, J., Kim, H., and Kim, Y. S. (2022).“Diversified reward-risk parity in portfolio construction.” In: _arXiv e-Print_.
We introduce diversified risk parity embedded with various reward-risk measures and more general allocation
rules for portfolio construction. We empirically test advanced reward-risk parity strategies and compare their
performance with an equally-weighted risk portfolio in various asset universes. All reward-risk parity strategies
we tested exhibit consistent outperformance evidenced by higher average returns, Sharpe ratios, and Calmar
ratios. The alternative allocations also reflect less downside risks in Value-at-Risk, conditional Value-at-Risk,
and maximum drawdown. In addition to the enhanced performance and reward-risk profile, transaction costs
can be reduced by lowering turnover rates. The Carhart four-factor analysis also indicates that the diversified
reward-risk parity allocations gain superior performance.
Chollete, L., Pena, V. de la, and Lu, C. (2011).“International Diversification: A Copula Approach.” In: _Journal of
Banking and Finance_ 35(2), pp. 403–417.
The viability of international diversification involves balancing benefits and costs. This balance hinges on the
degree of asset dependence. In light of theoretical research linking diversification and dependence, we examine
international diversification using two measures of dependence: correlations and copulas. We document several
findings. First, dependence has increased over time. Second, we find evidence of asymmetric dependence or
downside risk in Latin America, but less in the G5. The results indicate very little downside risk in East Asia.
Third, East Asian and Latin American returns exhibit some correlation complexity. Interestingly, the regions with
maximal dependence or worst diversification do not command large returns. Our results suggest international
limits to diversification. They are also consistent with a possible tradeoff between international diversification
and systemic risk.
Chollete, L., Pena, V. de la, and Lu, C. (2012).“International diversification: An extreme value approach.” In:
_Journal of Banking and Finance_ 36(3), pp. 871–885.
International diversification has costs and benefits, depending on the degree of asset dependence. We study
international diversification with two dependence measures: correlations and extreme dependence. We discover
that dependence has typically increased over time, and document mixed evidence on heavy tails in individual
countries. Moreover, we uncover three additional findings related to dependence. First, the timing of downside
risk differs depending on the region. Surprisingly, recent Latin American returns exhibit little downside risk.
Second, Latin America exhibits a great deal of correlation complexity. Third, according to the empirical results,
correlation does not vary with returns, but extreme dependence does vary monotonically with regional returns.
Our results are consistent with a tradeoff between international diversification and systemic risk. They also
suggest international limits to diversification, and that international investors demand some compensation for
joint downside risk during extreme events.


Choueifaty, Y., Froidure, T., and Reynier, J. (2013).“Properties of the most diversified portfolio.” In: _The Journal
of Investment Strategies_ 1(2), pp. 119–131.
This article expands upon Toward Maximum Diversification by Choueifaty and Coignard [2008]. We present new
mathematical properties of the Diversification Ratio and Most Diversified Portfolio (MDP), and investigate the
optimality of the MDP in a mean-variance framework. We also introduce a set of Portfolio Invariance Properties,
providing the basic rules an unbiased portfolio construction process should respect. The MDP is then compared
in light of these rules to popular methodologies (equal weights, equal risk contribution, minimum variance), and
their performance is investigated over the past decade, using the MSCI World as reference universe. We believe
that the results obtained in this article show that the MDP is a strong candidate for being the un-diversifiable
portfolio, and as such delivers investors with the full benefit of the equity premium.
Chua, D. B., Kritzman, M., and Page, S. (2009).“The Myth of Diversification.” In: _The Journal of Portfolio
Management_ 36(1), pp. 26–35.
Perhaps the most universally accepted precept of prudent investing is to diversify, yet this precept grossly
oversimplifies the challenge of portfolio construction. Correlations, as typically measured over the full sample
of returns, often belie an asset’s diversification properties in market environments when diversification is most
needed. Moreover, upside diversification is undesirable. The authors first describe the mathematics of conditional
correlations assuming returns are normally distributed. Then they present empirical results across a wide variety
of assets, which reveal that, unlike the theoretical conditional correlations, empirical correlations are significantly
asymmetric. Finally, the authors show that a portfolio construction technique called full-scale optimization
produces portfolios in which the component assets exhibit relatively lower correlations on the downside and
higher correlations on the upside than mean-variance optimization portfolios.
Colombo, J., Cruz, F., Paese, L., and Cortes, R. (2021).“The Diversification Benefits of Cryptocurrencies in Multi-
Asset Portfolios: Cross-Country Evidence.” In: _SSRN e-Print_.
Using a sample of 21 developing and developed countries, we analyze whether a well-diversified investor of tra-
ditional assets (stocks, bonds, real estate, and commodities) may benefit from investing in cryptocurrencies.
Country-specific analyses indicate that cryptocurrencies usually fit in the tangent portfolio (maximum Sharpe
ratio) but no – or very little – in the minimum variance portfolio (MVP). Out-of-sample analysis indicates that
even global portfolios that already benefits from international diversification may enjoy investing marginally in
cryptocurrencies: mean-variance optimal and naive with cryptocurrencies outperformed otherwise identical port-
folios in terms of risk-adjusted returns. Besides, exchange rate movements do not drive this better performance

- it occurs for both local (all returns denominated in the local currency) and global perspectives (all returns
in U.S. Dollars). We also find that cryptocurrencies’ diversification benefits occur both before and after the
COVID-19 pandemics, with the 1/N portfolio with cryptocurrencies presenting the higher risk-adjusted returns.
Our paper adds to the literature by analyzing the marginal effects of adding cryptocurrencies on a sample of
developing and developed economies and considering up-to-date data following the COVID-19 crisis.
Curran, M. and Zalla, R. (2021).“Can Volatility Solve the Naive Diversification Puzzle?” In: _arXiv e-Print_.
We investigate whether sophisticated volatility estimation improves the out-of-sample performance of mean-
variance portfolio strategies relative to the naive 1/N strategy. The portfolio strategies rely solely upon second
moments. Using a diverse group of econometric and portfolio models across multiple datasets, most models
achieve higher Sharpe ratios and lower portfolio volatility that are statistically and economically significant
relative to the naive rule, even after controlling for turnover costs. Our results suggest benefits to employing
more sophisticated econometric models than the sample covariance matrix, and that mean-variance strategies
often outperform the naive portfolio across multiple datasets and assessment criteria.
Darnell, M. (2009).“Did Diversification Fail?” In: _SSRN e-Print_.
Many investors had felt that by spreading their investments across many asset classes - by investing in a wide
array of betas - that they would avoid the risk of an across-theboard decline in their investments. They thought
that they had avoided the problem associated with putting all their eggs in one basket as the adage advises.
When most assets did fall together in largely simultaneous fashion in the midst of the recent credit crisis,
investors rated diversification a failure, and cried out in frustration that correlations had all converged on one.
Diversification failed this year, 1 was the title of a New York Times article in the business section in November
last year. In another, more recent article,2 one of the large university endowments explained that diversification
had failed to protect its asset values. This sentiment was, and is, entirely common. If their eggs were all in
different baskets, then it would appear that they were somehow all tied together sharing a common fate when
their fates were assumed to have been independent of one another instead. There are several aspects of this that


are wrong. Diversification didn’t fail; the metaphor of eggs in different baskets doesn’t accurately capture the
purpose of diversification; and those weren’t betas that they diversified across.
Davis, J., Hagelstein, P., Lackner, I., and Piziak, R. (2020).“The Efficient Frontier and International Portfolio
Diversification in Taxable and Tax-Privileged Accounts.” In: _Journal of Finance and Investment Analysis_ 9(2),
pp. 59–78.
In this paper, we consider efficient frontiers associated to two and three fund portfolios consisting of total
domestic bond funds, total domestic equity funds, and total international equity funds. These frontiers are
intended to help inform investment decisions regarding international exposure in taxable and tax-privileged
accounts.
De, I. and Clayman, M. R. (2015).“The Benefits of Socially Responsible Investing: An Active Manager’s Perspec-
tive .” In: _The Journal of Investing_ 24(4), pp. 49–72.
There has been a lot of research on the predictive power of environmental, social, and governance (ESG) ratings,
the relationship between ESG ratings and subsequent stock performance, and whether using ESG data in stock
analysis and portfolio management was value-additive or valuedetracting. In this article, the authors examine
the relationship between the ESG ratings of a company and its stock returns, volatility, and risk-adjusted
returns in the post-2008 financial crisis era. They explore the negative relationship between ESG and volatility
in greater depth, given the well-documented low-volatility anomaly (outperformance of low-volatility stocks).
Both (high) ESG rating and (low) volatility positively impact stock returns, but the ESG effect is independent
of the low-volatility effect, and ESG is a positive contributor in its own right. Given the controversy surrounding
the effect of ESG-based investment restrictions, the authors test the effect of restricting the investible universe
by deleting the lower tail of ESG companies on portfolio performance. Asset managers can thus actively use
the association between corporate ESG ratings and stock return, volatility, and risk-adjusted return to enhance
their stock-picking and portfolio-construction abilities.
de Carvalho, R. L., Lu, X., Soupe, F., and Dugnolle, P. (2017).“Diversify and Purify Factor Premiums in Equity
Markets.” In: _Factor Investing_. Elsevier, pp. 73–97.
In this chapter, we consider the question of how to improve the efficacy of strategies designed to capture factor
premiums in equity markets and, in particular, from the value, quality, low-risk and momentum factors. We
consider a number of portfolio construction approaches designed to capture factor premiums with the appropriate
levels of risk controls aiming at increasing information ratios. We show that information ratios can be increased
by targeting constant volatility (CV) over time, hedging market beta (HB) and hedging exposures to the size
factor, i.e. neutralizing biases in the market capitalization of stocks used in factor strategies. With regard to the
neutralization of sector exposures, we find this to be of particular importance for the value and low-risk factors.
Finally, we look at the added value of shorting stocks in factor strategies. We find that with few exceptions the
contributions to performance from the short leg are inferior to those from the long leg. Thus, long-only strategies
can be efficient alternatives to capture these factor premiums. Finally, we find that factor premiums tend to
have fatter tails than what could be expected from a Gaussian distribution of returns, but that skewness is not
significantly negative in most cases.
Dees, B. S., Stankovic, L., Constantinides, A. G., and Mandic, D. P. (2020).“Portfolio Cuts: A Graph-Theoretic
Framework to Diversification.” In: _IEEE International Conference on Acoustics, Speech and Signal Processing
(ICASSP)_.
Investment returns naturally reside on irregular domains, however, standard multivariate portfolio optimization
methods are agnostic to data structure. To this end, we investigate ways for domain knowledge to be conveniently
incorporated into the analysis, by means of graphs. Next, to relax the assumption of the completeness of graph
topology and to equip the graph model with practically relevant physical intuition, we introduce the portfolio
cut paradigm. Such a graph-theoretic portfolio partitioning technique is shown to allow the investor to devise
robust and tractable asset allocation schemes, by virtue of a rigorous graph framework for considering smaller,
computationally feasible, and economically meaningful clusters of assets, based on graph cuts. In turn, this
makes it possible to fully utilize the asset returns covariance matrix for constructing the portfolio, even without
the requirement for its inversion. The advantages of the proposed framework over traditional methods are
demonstrated through numerical simulations based on real-world price data.
Defau, L. and De Moor, L. (2021).“The investment behaviour of pension funds in alternative assets: Interest rates
and portfolio diversification.” In: _International Journal of Finance & Economics_.
In the last decades, pension funds and other institutional investors have significantly increased their allocations to
alternative assets: however, until today, there is no empirical research that evaluates this growth. In the pension


fund industry, experts point at two important reasons for the growing interest in alternative assets: historically
low interest rates and trends in portfolio diversification. The aim of this article is to assess whether these factors
actually have an impact on the investment behaviour of pension funds in alternative assets. For this article,
we analysed the CEM Benchmarking Inc. database with pension funds from North America, Europe, Australia,
and New Zealand. The empirical analysis includes 890 pension funds for the period 2000-2015. The results
confirm that portfolio diversification trends play an essential role in the growing popularity of alternative assets,
most probably because these assets allow the pension funds to optimize their portfolio structure. Furthermore,
our results reject the popular belief that pension funds have increased their allocations to alternative assets
because of the low interest rate environment; in contrast, our findings suggest that pension funds invest more
in alternative assets when interest rates are higher.
DeMiguel, V., Garlappi, L., and Uppal, R. (2009).“Optimal versus Naive Diversification: how Inefficient is the 1/N
Portfolio Strategy.” In: _The Review of Financial Studies_ 22(5), pp. 1915–1953.
We evaluate the out-of-sample performance of the sample-based mean-variance model, and its extensions de-
signed to reduce estimation error, relative to the naive 1/N portfolio. Of the 14 models we evaluate across seven
empirical datasets, none is consistently better than the 1/N rule in terms of Sharpe ratio, certainty-equivalent
return, or turnover, which indicates that, out of sample, the gain from optimal diversification is more than offset
by estimation error. Based on parameters calibrated to the US equity market, our analytical results and simula-
tions show that the estimation window needed for the sample-based mean-variance strategy and its extensions
to outperform the 1/N benchmark is around 3000 months for a portfolio with 25 assets and about 6000 months
for a portfolio with 50 assets. This suggests that there are still many miles to go before the gains promised by
optimal portfolio choice can actually be realized out of sample.
Diris, B., Palm, F., and Schotman, P. (2015).“Long-Term Strategic Asset Allocation: An Out-of-Sample Evaluation.”
In: _Management Science_ 61(9), pp. 2185–2202.
We evaluate the out-of-sample performance of a long-term investor who follows an optimized dynamic trading
strategy. Although the dynamic strategy is able to benefit from predictability out-of-sample, a short-term investor
using a single-period market timing strategy would have realized an almost identical performance. The value
of intertemporal hedge demands in strategic asset allocation appears negligible. The result is caused by the
estimation error in predicting the predictors. A myopic investor only needs to predict one-period-ahead expected
returns, but hedge demands also require accurate predictions of the predictor variables. To reduce the problem
of errors in optimized portfolio weights, we consider Bayesian procedures. Myopic and dynamic portfolios are
similarly affected by such modifications, and differences in performance become even smaller.
Domian, D. L., Louton, D. A., and Racine, M. D. (2007).“Diversification in Portfolios of Individual Stocks: 100
Stocks Are Not Enough.” In: _Financial Review_ 42(4), pp. 557–570.
We examine returns and ending wealth in portfolios selected from 1,000 large U.S. stocks over a 20-year holding
period. Shortfall risk, the possibility of ending wealth being below a target, is a useful metric for long horizon
investors and is consistent with the Safety First criterion. Density functions obtained from simulations illustrate
that shortfall risk reduction continues as portfolio size is increased, even above 100 stocks. A slightly lower
risk can be achieved in small portfolios by diversifying across industries, but a greater reduction is obtained by
simply increasing the number of stocks.
du Plessis, H. and van Rensburg, P. (2017).“Diversification and the realised volatility of equity portfolios.” In:
_Investment Analysts Journal_ 46(3), pp. 213–234.
In Markowitz’s (1952) portfolio theory, a reduction in volatility for a given level of expected return is implied
as being equivalent to an increase in diversification. The recent development of risk-based portfolio construction
methods, which emphasise diversification separately from volatility reduction, challenges this equivalence. Using
a point-in-time database of liquid equities listed on the Johannesburg Stock Exchange between 1998 and 2016,
a numerical simulation technique is employed to study the behaviour of a range of diversification measures as a
portfolio-level attribute and assess and compare their usefulness in estimating out-of-sample portfolio volatility.
The empirical performance of maximum diversification portfolios based on each measure is then investigated.
It is found that a portfolio?s diversification level is a significant predictor of future portfolio risk beyond that
of historic volatility, and that the empirical performance of maximum diversification portfolios, attractive in all
cases, depends critically on the definition of diversification applied.
Durante, F., Foscolo, E., Pappada, R., and Wang, H. (2015). _A portfolio diversification strategy via tail dependence
measures_. Tech. rep. DEAMS Research Paper Series.


We provide a two-stage portfolio selection procedure in order to increase the diversification benefits in a bear
market. By exploiting tail dependence-based risky measures a first-step cluster analysis is carried out for discern-
ing between assets with the same performance during risky scenarios. Then a mean-variance efficient frontier is
computed by fixing a number of assets per portfolio and by selecting only one item from each cluster. Empirical
calculations on the EURO STOXX 50 prove that investing on selected index components in trouble periods may
improve the risk-averse investor portfolio performance.
Elkamhi, R., Jo, C., Lee, J., and Salerno, M. (2021).“The Jury is Still Out On the Performance of Naive Diversi-
fication (1/N rule).” In: _SSRN e-Print_.
DeMiguel et. al. (2009b) made a compelling case that estimation error dwarfs diversification benefits resulting
in naive diversification (1/N) dominating mean-variance portfolios. We illustrate the necessary and sufficient
conditions for risk-based allocation rules to be optimal in a mean-variance framework. We show empirically that
many common datasets satisfy such conditions, making these rules preferred to mean-variance in the presence
of estimation error. Our out-of-sample tests show that these rules outperform both mean-variance and 1/N.
Further, we show that clustering the data using machine learning enhances the diversification benefits of these
rules by making the data closer to the required conditions for optimality.
Elton, E. J. and Gruber, M. J. (2020).“A Review of the Performance Measurement of Long-Term Mutual Funds.”
In: _Financial Analysts Journal_ 76(3), pp. 22–37.
We review the major models of mutual fund performance: (1) using return data to evaluate equity funds-from
single to multi-index models, (2) measuring passive portfolio performance, (3) using holdings-based performance
measures, (4) measuring timing ability, and (5) measuring bond fund performance. We conclude with a discussion
of issues affecting performance measurement: data sources and bias, missing factors, and improvements to
benchmarks.
Eom, C., Kaizoji, T., Livan, G., and Scalas, E. (2021).“Limitations of portfolio diversification through fat tails of
the return Distributions: Some empirical evidence.” In: _The North American Journal of Economics and Finance_
56, p. 101358.
This study investigates the level of risk due to fat tails of the return distribution and the changes of tail fatness
(TF) through portfolio diversification. TF is not eliminated through portfolio diversification, and, interestingly,
the positive tail has declining fatness until a certain level is reached, while the negative tail has rising fatness.
This indicates that fat tails are highly relevant to common factors on systematic risk and that the relevance
of common factors is higher for the negative tail compared to the positive tail. In the portfolio diversification
effect, the declining fatness of the positive tail further reduces risk, but the rising fatness of the negative tail
does not contribute to this effect. The asymmetry between the fatness of the positive and negative tails in the
return distribution corresponds to the asymmetry of the trade-off relationship between loss avoidance and profit
sacrifice that is expected as a consequence of portfolio diversification. Investors use portfolio diversification to
reduce their risk of suffering high losses, but following this strategy means sacrificing high-profit potential. Our
study provides empirical confirmation for the practical limitation of portfolio diversification and explains why
investors with diversified portfolios suffer high losses from market crashes. An examination of the Northeast
Asian stock markets of China, Japan, Korea, and Taiwan show identical results.
Fabozzi, F. J. and Lopez de Prado, M. (2018).“Being Honest in Backtest Reporting: A Template for Disclosing
Multiple Tests.” In: _The Journal of Portfolio Management_ 45(1), pp. 141–147.
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
Fleming, B. (2021).“Diversification and the Distribution of Portfolio Variance, Part 3: Polynomial optimisation for
asset allocation.” In: _SSRN e-Print_.


Diversification is a fundamental topic for all investors but there remains little agreement on how to measure
it. Often it is defined ambiguously through risk-based portfolio construction techniques. Recently it has been
suggested to connect maximising diversification with minimising risk instability, via kurtosis, which presents
practical optimisation challenges. In particular, minimising kurtosis is a non-convex problem that is typically
solved using deterministic Branch-and-Bound methods, that do not scale well, or stochastic methods that pro-
vide limited guarantees on finding minima. We thus apply a deterministic hierarchical polynomial optimization
framework that allows realistic asset allocation problems to be readily solved and also provides a numerical
certificate of optimality.
Fleming, B. and Kroeske, J. (2020a).“Diversification and the Distribution of Portfolio Variance, Part 1: Sums of
IID Variables and Higher-Order Moments.” In: _SSRN e-Print_.
For a weighted sum of asset returns that are independent and identically distributed (IID) up to variance,
we derive expressions linking the distribution of variance across assets with higher-order portfolio moments,
assuming these quantities are finite. In particular, we show concise relationships for portfolio skewness and
kurtosis and, within a general framework, review related metrics in the literature for measuring diversification.
Fleming, B. and Kroeske, J. (2020b).“Diversification and the Distribution of Portfolio Variance, Part 2: Volatility
Stability as a Measure of Diversification.” In: _SSRN e-Print_.
We introduce a new framework for understanding portfolio diversification that provides a coherent basis for
comparing methodologies and offers a new approach to portfolio construction. The primary argument is that
measures of diversification based only on a covariance matrix are ambiguous because in such a risk setting only
the overall portfolio variance is of any import. To resolve this we propose that the purpose of diversification
is most helpfully viewed as reducing the variance of portfolio variance itself, which in turn is only meaningful
when one accounts for excess kurtosis. Connecting diversification and the variance of variance provides a natural
extension to the ubiquitous mean-variance approach. Examples are provided to demonstrate the intuitive nature
of portfolios that maximize diversification through minimizing kurtosis. Furthermore, we introduce portfolio
dimensionality as a transformation of kurtosis that allows us to interpret diversification in terms of an equi.
Flint, E., Seymour, A., and Chikurunhe, F. (2021).“Defining and measuring portfolio diversification.” In: _South
African Actuarial Journal_ 20(1), pp. 17–48.
It is often said that diversification is the only ’free lunch’ available to investors; meaning that a properly
diversified portfolio reduces total risk without necessarily sacrificing expected return. However, achieving true
diversification is easier said than done, especially when we do not fully know what we mean when we are talking
about diversification. While the qualitative purpose of diversification is well known, a satisfactory quantitative
definition of portfolio diversification remains elusive. In this research, we summarise a wide range of diversification
measures, focusing our efforts on those most commonly used in practice. We categorise each measure based on
which portfolio aspect it focuses on: cardinality, weights, returns, risk or higher moments. We then apply these
measures to a range of South African equity indices, thus giving a diagnostic review of historical local equity
diversification and, perhaps more importantly, providing a description of the investable opportunity set available
tofund managers in this space. Finally, we introduce the idea of diversification profiles. These regime dependent
profiles give a much richer description of portfolio diversification than their single-value counterparts and also
allow one to manage diversification proactively based on one’s view of future market conditions.
Flint, E. J., Chikurunhe, F., and Seymour, A. J. (2016).“The Cost of a Free Lunch: Dabbling in Diversification.”
In: _SSRN e-Print_.
It’s often said that diversification is the only ’free lunch’ available to investors; meaning that a properly di-
versified portfolio reduces total risk without necessarily sacrificing expected return. However, achieving true
diversification is easier said than done, especially when we don’t fully know what we mean when we’re talking
about diversification. While the qualitative purpose of diversification is well-known, a satisfactory quantitative
definition of portfolio diversification is not. In this report, we summarise a wide range of diversification mea-
sures, focussing our efforts on those most commonly used in practice. We categorise each measure based on
which portfolio aspect it focusses on: cardinality, weights, returns, risk or higher moments. We then apply these
measures to a range of South African equity indices, thus giving a diagnostic review of historical local equity
diversification and, perhaps more importantly, providing a description of the investable opportunity set available
to fund managers in this space. Finally, we introduce the idea of diversification profiles. These regime-dependent
profiles give a much richer description of portfolio diversification than their single-value counterparts and also
allow one to manage diversification proactively based on one’s view of future market conditions.


Flores, Y. S., Bianchi, R. J., Drew, M. E., and Truck, S. (2017).“The Diversification Delta: A Different Perspective.”
In: _The Journal of Portfolio Management_ 43(4), pp. 112–124.
In a 2012 article published in The Journal of Portfolio Management, Vermorken, Medda, and Schroder introduce
a new measure of diversification, the Diversification Delta (DD), based on the entropy of the portfolio return
distribution. Entropy as a measure of uncertainty has been used successfully in several frameworks and takes
into account the entire statistical distribution, rather than just the first two moments. In this article, the authors
highlight some drawbacks of the DD measure and go on to propose an alternative measure based on exponential
entropy that overcomes the identified shortcomings. The authors present the properties of this new measure and
propose it as an alternative for portfolio optimization that incorporates higher moments of asset returns, such
as skewness and excess kurtosis.
Fouquau, J., Kharoubi, C., and Spieser, P. (2018).“International and temporal diversifications: the best of both
worlds?” In: _Journal of Risk_ 20(4), pp. 27–54.
Modern portfolio theory advises investors to diversify their assets to reduce risk. Diversification encompasses
two major concepts: international and temporal diversifications. While international diversification tells investors
how many and what type of assets they should put in their portfolios to diversify them, temporal diversification
tells them how long they should hold the assets in their portfolios. To investigate these questions simultaneously,
we propose an alternative approach based on two recent methodologies: wavelets and copulas. We focus on seven
stock market indexes in different geographical areas. Our main findings are the following. First, we confirm the
usual benefits of international diversification. Second, the results of nonparametric copulas show that the shape
of the copula varies across the long or short term of the relationship. Third, this methodology shows some
structural differences in dependencies across different timescales. We then highlight the existence of potential
holding periods that allow investors to improve their diversification processes and identify risks.
Fusai, G., Mignacca, D., Nardon, A., and Human, B. (2020).“Equally Diversified or Equally Weighted?” In: _Risk
(Cutting Edge)_.
Gianluca Fusai, Domenico Mignacca, Andrea Nardon and Ben Human show how to decompose portfolio volatility
into undiversified volatility and a diversification component. The authors’ decomposition has a clear statistical
interpretation because it relates the diversification component to partial covariances. On this basis, they advocate
the construction of an equally diversified portfolio. An empirical analysis illustrates the superior out-of-sample
performance of the equally diversified portfolio with respect to an equally weighted portfolio.
Giese, G., Lee, L.-E., Melas, D., Nagy, Z., and Nishikawa, L. (2019).“Foundations of ESG investing: how ESG
affects equity valuation, risk, and performance.” In: _The Journal of Portfolio Management_ 45(5), pp. 69–83.
Many studies have focused on the relationship between companies with strong environmental, social, and gover-
nance (ESG) characteristics and corporate financial performance. However, these have often struggled to show
that positive correlations produced in fact explain the behavior. The authors of this article provide a link
between ESG information and the valuation and performance of companies, by examining three transmission
channels within a standard discounted cash flow model they call the cash-flow channel, the idiosyncratic risk
channel, and the valuation channel. They tested each of these transmission channels using MSCI ESG Ratings
data and financial variables. This showed that companies ESG information was transmitted to their valuation
and performance, both through their systematic risk profile (lower costs of capital and higher valuations) and
their idiosyncratic risk profile (higher profitability and lower exposures to tail risk). The research suggests that
changes in a company ESG characteristics may be a useful financial indicator. ESG ratings may also be suitable
for integration into policy benchmarks and financial analyses.
Gougler, A. and Utz, S. (2020).“Factor exposures and diversification: Are sustainably screened portfolios any
different?” In: _Financial Markets and Portfolio Management_ 34, pp. 221–249.
We analyze the performance, risk, and diversification characteristics of global screened and best-in-class equity
portfolios constructed according to Inrate’s sustainability ratings. The financial performance of sustainably high-
rated portfolios is similar to the risk-adjusted market performance in terms of abnormal returns of a five-factor
market model. In contrast, low-rated portfolios exhibit negative abnormal returns. Firms with high sustainability
ratings show lower idiosyncratic risk and higher exposure toward the high-minus-low and the conservative-minus-
aggressive factor.
Greiner, S. P. and Stoyanov, S. V. (2019).“Portfolio scoring by expected risk premium.” In: _The Journal of Portfolio
Management_ 45(4), pp. 83–90.
In this article, the authors discuss a general method for ranking portfolios that places few limitations on the
portfolio constituents other than using publicly traded assets. The ranking scores reflect the expected reward


investors would require for accepting the risks of the portfolio in the context of an asset pricing framework.
The scores are computed through a factor model that acknowledges the factor return correlations. The authors
illustrate the approach with a large universe of exchange-traded funds assuming a linear model with Fama-
French-Carhart factors wherein factor premiums (i.e., expected returns) are proportional to factor volatilities.
The empirical analysis implies that the most significant factors from the Fama-French-Carhart factor set driving
the premiums are the market and the momentum factors.
Guidolin, M., Hansen, E., and Lozano-Banda, M. (2018).“Portfolio performance of linear SDF models: an out-of-
sample assessment.” In: _Quantitative Finance_ 18(8), pp. 1425–1436.
We evaluate linear stochastic discount factor models using an ex-post portfolio metric: the realized out-of-
sample Sharpe ratio of mean-variance portfolios backed by alternative linear factor models. Using a sample of
monthly US portfolio returns spanning the period 1968-2016, we find evidence that multifactor linear models have
better empirical properties than the CAPM, not only when the cross-section of expected returns is evaluated in-
sample, but also when they are used to inform one-month ahead portfolio selection. When we compare portfolios
associated to multifactor models with mean-variance decisions implied by the single-factor CAPM, we document
statistically significant differences in Sharpe ratios of up to 10 percent. Linear multifactor models that provide
the best in-sample fit also yield the highest realized Sharpe ratios.
Guo, D. (2019).“A Statistical Response to Challenges in Vast Portfolio Selection.” PhD thesis. University of
Waterloo.
The thesis is written in response to emerging issues brought about by an increasing number of assets allocated
in a portfolio and seeks answers to puzzling empirical findings in the portfolio management area. Over the years,
researchers and practitioners working in the portfolio optimization area have been concerned with estimation
errors in the first two moments of asset returns. The thesis comprises several related chapters on our statistical
inquiry into this subject. Chapter 1 of the thesis contains an introduction to what will be reported in the
remaining chapters. A few well-known covariance matrix estimation methods in the literature involve adjustment
of sample eigenvalues. Chapter 2 of the thesis examines the effects of sample eigenvalue adjustment on the out-
of-sample performance of a portfolio constructed from the sample covariance matrix.
Guo, D., Boyle, P. P., Weng, C., and Wirjanto, T. S. (2019).“When Does The 1/N Rule Work?” In: _SSRN e-Print_.
We propose a ”1/N favorability index” to measure how favorable a market is to holding a 1/N portfolio. This
index reflects the extent of difficulty for an optimized portfolio to outperform the 1/N portfolio in a specific
market. A single-factor model predicts that bull markets are accompanied by a high 1/N favorability index and
vice versa. We validate the model implication that the 1/N portfolio is more difficult to beat in bull markets
using stock return datasets from a number of countries as well as the classic datasets used by DeMiguel et al.
(2009). Our results imply that the reported good performance of the 1/N portfolio in the US equity market can
be partially attributed to the long-run bullish trend in the market which gives rise to the high favorability of
the market to the 1/N portfolio.
Haley, M. R. (2017).“K-fold cross validation performance comparisons of six naive portfolio selection rules: how
naive can you be and still have successful out-of-sample portfolio performance?” In: _Annals of Finance_ 13,
pp. 341–353.
Recent research reports that optimal portfolio selection models often perform worse than equal-weight naive
diversification in out-of-sample testing. This paper extends this line of inquiry by comparing the out-of-sample
performance of the equal-weight naive strategy to the out-of-sample performance of five alternative naive strate-
gies, each of which derives from a simple heuristic that does not require any optimization. Out-of-sample portfolio
performance is assessed by mean, standard deviation, skewness, and Sharpe ratio; k-fold cross validation is used
as the out-of-sample testing mechanism. The results indicate that the proposed naive heuristic rules exhibit
strong out-of-sample performance, in most cases superior to the equal-weight naive strategy. These findings are
consequential for at least two reasons: first, if these simple heuristic-based rules outperform the equal-weight
naive strategy, then by transitivity they can outperform the mean-variance- and shortfall-optimal portfolio rules
that have been shown in the literature to be inferior to the equal-weight naive rule, which further emphasizes the
out-of-sample fragility of ”optimal”methods; and second, among naive diversification strategies, some appear
more robust in out-of-sample testing than others, hence the proposed methods may be useful when forming
mixed portfolio selection models wherein a naive strategy is combined with an optimal strategy to improve
performance.
Hallerbach, W. G. (2017).“If You Have Said A, You Must Also Say B: Calculating Diversified Asset Returns.” In:
_The Journal of Wealth Management_ 20(2), pp. 76–81.


The bottom-up route to portfolio diversification is clear: Combining individual assets into a portfolio will lower
portfolio risk (especially when correlations are low). The top-down route of evaluating individual assets from the
perspective of the diversified portfolio is widely applied in risk budgeting but is neglected in return attributions.
Consequently, many investors evaluate individual assets on the basis of their undiversified returns instead of
including the diversification benefits they offer. This perspective biases the evaluation of high-volatility/low-
correlation assets in the portfolio. In this note, we highlight the importance of evaluating diversified returns and
show how we can calculate these returns. We illustrate the method for a U.S. asset portfolio.
Hambel, C., Kraft, H., and Ploeg, R. van der (2021).“Asset Pricing and Decarbonization: Diversification versus
Climate Action.” In: _SSRN e-Print_.
Asset pricing and climate policy are analyzed in a global economy where consumption goods are produced by
both a green and a carbon-intensive sector. We allow for two types of damages from global warming. Given that
the economy is initially heavily dependent on carbon-intensive capital, the desire to diversify assets complements
the attempt to mitigate economic damages from climate change. In the longer run, however, a trade-off between
diversification and climate action emerges. We derive the optimal carbon price, the equilibrium risk-free rate,
and risk premia. Climate disasters, which are more likely to occur sooner as temperature rises, significantly
increase risk premia on financial assets.
Harvey, C. R., Liu, Y., and Saretto, A. (2020).“An Evaluation of Alternative Multiple Testing Methods for Finance
Applications.” In: _The Review of Asset Pricing Studies_ 10(2), pp. 199–248.
In almost every area of empirical finance, researchers confront multiple tests. One high-profile example is the
identification of outperforming investment managers, many of whom beat their benchmarks purely by luck.
Multiple testing methods are designed to control for luck. Factor selection is another glaring case in which
multiple tests are performed, but numerous other applications do not receive as much attention. One important
example is a simple regression model testing five variables. In this case, because five variables are tried, a t-
statistic of 2.0 is not enough to establish significance. Our paper provides a guide to various multiple testing
methods and details a number of applications. We provide simulation evidence on the relative performance of
different methods across a variety of testing environments. The goal of our paper is to provide a menu that
researchers can choose from to improve inference in financial economics.
Heckel, T., Amghar, Z., Haik, I., Laplenie, O., and Carvalho, R. L. de (2020).“Factor Investing in Corporate Bond
Markets: Enhancing Efficacy Through Diversification and Purification!” In: _The Journal of Fixed Income_ 29(3),
pp. 6–21.
We show that factors from value, quality, low risk, and momentum styles play an important role in explaining
the cross-section of corporate bond expected returns for the US and Euro Investment Grade and US BB-B
Nonfinancial High Yield universes. We demonstrate the importance of purifying factor data by neutralizing a
number of risk biases that are present in the factors: controlling for sectors, option-adjusted spread (OAS),
duration, and size biases significantly increase the predictive power of style factors. We propose a new simple
approach for efficiently neutralizing the biases from multiple risk variables and demonstrate its superiority
relative to stratified sampling and optimization as alternative control methods. We also measure the added value
from diversifying the number of factors in each style. Finally, we show that the results are robust in relation to
transaction costs and can be used to design strategies that aim at outperforming traditional benchmark indexes.
Heinrich, L., Shivarova, A., and Zurek, M. (2021).“Factor investing: alpha concentration versus diversification.” In:
_Journal of Asset Management_.
Despite extensive research support, the role of diversification in current factor investing strategies remains ne-
glected. This paper investigates whether well-designed multifactor portfolios should not only be based on firm
characteristics, but should also include portfolio diversification effects. While the alpha concentration approach
mainly considers factor-specific firm characteristics, the diversified approach utilizes covariance estimators in
addition to firm characteristics to account for portfolio diversification. The corresponding out-of-sample results
show that including an efficient covariance estimator improves the performance of long-only multifactor portfo-
lios compared to the pure alpha concentration approach. A particular advantage of diversified factor investing
strategies can be identified in the significant increase in exposure to the low-volatility factor represented by firm
characteristics with high informational content. No significant performance differences are observed for long-
short portfolios where the factor exposures of the alpha concentration and diversification approaches are similar
with respect to the low-volatility factor.
Heinze, T. (2016).“Markowitz 3.0: Including Diversification Targets in Portfolio Optimization via Diversification
Functions.” In: _SSRN e-Print_.


Given Markowitz’s mean-risk model, maximization of diversification is established as an additional investment
target next to return maximization and risk minimization. This widens the opportunity to transfer market views
into the model by additional diversification parameters and should therefore lead to an improved mapping of
economic reality. The main focus is on the introduction of diversification functions which make diversification
quantifiable and which are used as third objective in the optimization. Thus, the resulting efficient frontier
extends to a three dimensional surface which includes the original efficient frontier according to Markowitz.
Starting with the original Markowitz model through improvements in stochastic modelling in terms of risk
measures, copulas, fat tails, etc., leaving the pure return/risk context can be interpreted as a third model
generation.
Hens, T., Schenk-Hoppe, K. R., and Woesthoff, M.-H. (2020).“Escaping the backtesting illusion.” In: _The Journal
of Portfolio Management_ 46(4), pp. 81–93.
Two tests can help asset managers to develop more robust investment strategies: an impact test and a survival
test. Both tests complement the backtest, in which one checks how a proposed investment strategy would have
performed in the past. The impact test considers the performance of the strategy when assets under management
grow (crowdedness), and it checks the impact that growth in assets under management in competing strategies
has on the proposed strategy (cross impact). The survival test considers the effect of the long-term evolution
of assets under management in competition for market capital. Using Shiller S&P 500 index and bond market
data, we show that time-series momentum (relative strength) performs best in the backtest and the impact test
but that an expected relative cash-flow rule (relative dividend yield) has the best long-term survival properties.
Hjalmarsson, E. (2011).“Portfolio Diversification Across Characteristics.” In: _The Journal of Investing_ 20(4), pp. 84–
88.
This article studies long short portfolio strategies formed on seven different stock characteristics representing
various measures of past returns, value, and size. Each individual characteristic results in a profitable portfolio
strategy, but these single-characteristic strategies are dominated by a diversified strategy that places equal
weight on each of the single-characteristic strategies. The benefits of diversifying across characteristic-based
long short strategies are substantial and can be attributed to the mostly low, and sometimes substantially
negative, correlation between the returns on the single-characteristic strategies.
Hoesli, M. E. R. and Johner, L. (2021).“Portfolio Diversification across U.S. Gateway and Non-Gateway Real
Estate Markets.” In: _SSRN e-Print_.
Using simulation analysis and property-level data for the U.S., we compare performance metrics for portfolios
containing varying proportions of gateway and non-gateway markets. Risk-adjusted performance is found to be
similar across types of markets. Gateway markets have higher appreciation and total returns, while non-gateway
markets exhibit higher income returns even after accounting for capital expenditures. Downside risk appears
to be slightly greater for gateway markets than for non-gateway markets; however, full drawdown and recovery
lengths tend to be shorter for gateway markets. Systematic risk is found to be constant across types of markets.
We show that discriminating between gateway and non-gateway markets is useful for mixed-asset diversification
purposes, with the former type of markets appearing in risky portfolios and the latter in low-risk portfolios. By
considering a large spectrum of performance metrics in a realistic investment setting, the results should provide
investors with valuable information when allocating funds across gateway and non-gateway markets. The paper
also provides insights regarding how best to define gateway markets.
Hsu, Y.-C., Lin, H.-W., and Vincent, K. (2017). _Do Cross-Sectional Stock Return Predictors Pass the Test without
Data-Snooping Bias?_ Tech. rep. Institute of Economics Academia Sinica.
This study examines the possible data-snooping bias as a competing explanation for the anomalies in the cross-
section of stock returns. We posit that the exhaustive standalone searches for profitable strategies could lead
to recommending spuriously predictive variables. In order to explore the severity of this problem, we use a
multiple testing method to evaluate the profitability of portfolios constructed by these predictors. Our empirical
analyses suggest that over half of the findings based on individual testing method are no longer statistically
significant after we adjust for data-snooping bias. Excluding the micro-cap stocks before portfolios construction
and applying the notion of economic significance in this study further weaken the evidence for predictability.
Hsu, P.-H., Han, Q., Wu, W., and Cao, Z. (2018).“Asset allocation strategies, data snooping, and the 1 / N rule.”
In: _Journal of Banking & Finance_ 97, pp. 257–269.
Using a series of advanced tests from White’s (2000) Check to correct for data-snooping bias, we assess the out-
of-sample performance of various portfolio strategies relative to the naive 1/N rule. When we analyze 16 basic
portfolio strategies, 126 learning strategies, and nearly 2,000 extended strategies, we find that some strategies


outperform the 1/N rule in conventional tests that do not account for data-snooping bias. However, after we use
the new tests that control for such bias, we find that none or very few of these strategies outperform the 1/N
rule. Thus, our finding underscores the necessity to control for data-snooping bias when making asset allocation
decisions.
Huang, M. and Yu, S. (2020).“A new procedure for resampled portfolio with shrinkaged covariance matrix.” In:
_Journal of Applied Statistics_ 47(44), pp. 642–652.
Dealing with estimation error is an important issue when we implement the mean-variance paradigm for portfolio
construction. To tackle the problem, two approaches are proposed in literature, the portfolio resampling technique
introduced by Michuad and the well-known shrinkaged covariance matrix method. There are certain evidences on
the advantages of shrinkaged covariance over portfolio resampling, however, it is unclear whether a combination of
the two approaches could produce a better performance compared with using shrinkaged covariance alone. In this
paper, we propose a new algorithm to integrated linear or nonlinear shrinkage estimation with resampled portfolio
to achieve a further improvement. Our method are demonstrated via extensive simulation and application in
active portfolio management process.
Hubrich, S. (2021).“Allocating to Liquid Alternative Strategies for Mean–Variance Diversification.” In: _The Journal
of Alternative Investments_ 24(1), pp. 61–74.
Buyers of alternative investments need to make an allocation decision in a broader portfolio context that includes
traditional assets-how much to allocate and from where to fund? Permissible allocations are often capped, and
formulating explicit return assumptions is particularly challenging. Focusing on ”liquid alternative” mutual
funds, the author introduces a framework to assess such an investment purely in terms of its risk by using mean-
variance considerations to extract the return threshold that would justify a moderate, realistic allocation. The
framework reveals nuanced relationships between the risk properties and attractiveness to the broader portfolio:
Both greater volatility and a lack of equity market correlation can be advantageous in the sense of lowering this
return threshold. Comparing the empirical performance of liquid alternative investments (which includes the
sell-off in 2020) with the return thresholds implied by this framework suggests that only a minority of funds
have historically cleared the threshold that merits investment, with some differentiation across subcategories
observed.
Humphrey, J. E., Benson, K. L., Low, R. K. Y., and Lee, W.-L. (2015).“Is diversification always optimal?” In:
_Pacific-Basin Finance Journal_ 35, pp. 521–532.
Should retirement savers diversify across many funds or consolidate into one fund? We examine Australian
retirement savings. Theoretically, diversification across funds is the optimal strategy. With real-world short-
selling constraints, investment in a single fund is optimal. Finance theory and recent literature suggest that
investors should diversify their retirement savings across a number of funds. However, the Australian government
encourages investors to consolidate retirement savings into just one fund. Using a number of optimization
techniques, we investigate which of these two actions would result in the best outcome for investors in terms
of risk and return. We find that in the majority of cases investors would be better off not diversifying their
holdings; mainly because superannuation funds cannot be short sold. Consolidation therefore does appear to be
the optimal strategy for the average superannuation investor.
Hwang, I., Xu, S., and In, F. (2018).“Naive versus optimal diversification: Tail risk and performance.” In: _European
Journal of Operational Research_ 265(1), pp. 372–388.
It is well documented in portfolio optimization that naive diversification outperforms optimal mean-variance
diversification because the latter is subject to severe estimation error. Our study provides an alternative expla-
nation for the outperformance of naive diversification by examining the tail risk of naive diversification relative
to optimal mean-variance diversification. We utilize a rolling-sample approach and compare the out-of-sample
performance and tail risk of various optimal strategies to that of the naive diversification strategy. Using port-
folios consisting of individual stocks, we show that for portfolios containing relatively small number of stocks,
naive diversification outperforms optimal mean-variance diversification and is less exposed to tail risk. However,
for relatively large number of stocks in the portfolio, naive diversification maintains its superior performance but
increases tail risk and results in more concave portfolio returns. These results imply that the outperformance of
naive diversification acts as compensation for the increase in tail risk and concavity.
Ielpo, F., Merhy, C., and Simon, G. (2017). _Engineering Investment Process: Making Value Creation Repeatable_.
Elsevier. 430 pp.
The book explores the quantitative steps of a financial investment process. The authors study how these steps are
articulated in order to make any value creation, whatever the asset class, consistent and robust. The discussion


includes factors, portfolio allocation, statistical and economic backtesting, but also the influence of negative rates,
dynamical trading, state-space models, stylized facts, liquidity issues, or data biases. Besides the quantitative
concepts detailed here, the reader will find useful references to other works to develop an in-depth understanding
of an investment process.
Ilmanen, A. and Kizer, J. (2012).“The Death of Diversification Has Been Greatly Exaggerated.” In: _The Journal
of Portfolio Management_ 38, pp. 15–27.
Asset-class correlations generally tend to rise during crises. That certainly was true in the 2007-2009 financial
crisis, and since then correlations have generally remained elevated as markets switch between binary risk-
on/risk-off environments. However, we believe it would be wrong to interpret these developments as conclusive
evidence of the death of diversification. First, academics (Asness, Israelov and Liew [2011]) have stressed that
while diversification often fails in short-term panics - especially one as systemic as the 2007-2009 crisis - it
does effectively reduce downside risks over longer horizons. Second, high-quality bonds have fairly consistently
provided positive returns during stressful market environments. Third, in this article, we argue and show that
factor diversification has been more effective than asset-class diversification in general and, in particular, during
crises. The last two arguments challenge the concentration in equity risk found in most institutional portfolios,
which is also a central argument in favor of more risk-balanced, so-called risk parity, portfolios. Traditional
asset-class diversification involves allocating nominal dollars to various asset classes and their subsets. Several
large institutions have begun to explore an alternative perspective of factor allocation, asking: What are the
most important factors driving our portfolio returns? This perspective involves at least two changes. First, focus
is shifted from dollar allocations to risk allocations. This change often reveals the dominant role of the most
volatile asset classes and the portfolio’s dependence on equity market direction. Second, portfolio analysis is
extended beyond asset classes to dynamic strategy styles or to underlying risk factors. Fundamental factors
such as growth, inflation and liquidity are naturally interesting, but they are inherently hard to measure. Most
investors prefer investable factors and therefore use market-based proxies - equities for growth, Treasuries for
deflation and commodities for inflation.
Jacobs, H., Muller, S., and Weber, M. (2014).“How should individual investors diversify? An empirical evaluation
of alternative asset allocation policies.” In: _Journal of Financial Markets_ 19, pp. 62–85.
For global equity diversification, prominent Markowitz extensions do not outperform several heuristic weighting
schemes (1/N heuristic, market value-weighting and GDP-weighting). Comparing the different heuristic stock
weighting schemes, the value-weighted heuristic performs worse than the GDP-weighted global stock portfolio.
Diversification gains in the asset allocation context are mainly driven by a well-balanced allocation over different
asset classes. Consistent with global equity diversification, Markowitz-based optimization methods do not add
significant value when allocating across different asset classes. This paper evaluates numerous diversification
strategies as a possible remedy against widespread costly investment mistakes of individual investors. Our
results reveal that a very broad range of simple heuristic allocation schemes offers similar diversification gains as
well-established or recently developed portfolio optimization approaches. This holds true for both international
diversification in the stock market and diversification over different asset classes. We thus suggest easy-to-
implement allocation guidelines for individual investors.
Jacobsen, B. and Ma, C. (2020).“Alpha alchemy: diversifying without diluting alpha.” In: _The Journal of Wealth
Management_ 23(2), pp. 75–87.
Managers are often evaluated and selected on the basis of their portfolio stand-alone risk and return properties.
This is too narrowly focused. The basics of mean-variance optimization tells us that covariance and the relation-
ship of a security returns within the context of the overall portfolio is important. We illustrate how the basics of
portfolio construction with individual securities also applies to building a portfolio of managers. First, we show
the statistical properties of different asset classes, as more and more managers are used to get exposure to the
asset class. Depending on the asset class, tracking error, relative skewness, and relative excess kurtosis improve
at different rates. This is important for considering how many managers may be necessary to get exposure to an
asset class. We then illustrate an optimization method of combining the managers. Although the managers, on
their own, may not have statistically positive alphas, they can be combined in a way to improve the likelihood
that the portfolio of managers has a statistically positive alpha. The optimization method is not a substitute for
traditional due diligence. It is just one additional tool useful for manager selection and portfolio construction.
Jacobsen, B. and Scheiber, M. (2022).“Harvesting Multi-Asset Carry, Value, and Momentum: Work Smarter, Not
Harder.” In: _The Journal of Financial Data Science_ 4(2), pp. 50–61.


Carry, value, and momentum are the trinity of systematic investing. As signals, it is important to know what
they signify and how to interpret the signals. What is the cost of delay? How does their effectiveness change as a
function of the holding period? The authors illustrate how these signals can differ in terms of their informational
content and persistence. They also show how classification trees can be used to combine these signals to get the
most meaning out of them.
Jaeger, M., Krugel, S., Marinelli, D., Papenbrock, J., and Schwendner, P. (2020).“Understanding machine learning
for diversified portfolio construction by explainable AI.” In: _SSRN e-Print_.
In this paper, we construct a pipeline to investigate heuristic diversification strategies in asset allocation. We
use machine learning concepts (”explainable AI”) to compare the robustness of different strategies and back
out implicit rules for decision making.In a first step, we augment the asset universe (the empirical dataset)
with a range of scenarios generated with a block bootstrap from the empirical dataset.Second, we backtest the
candidate strategies over a long period of time, checking their performance variability. Third, we use XGBoost
as a regression model to connect the difference between the measured performances between two strategies to
a pool of statistical features of the portfolio universe tailored to the investigated strategy. Finally, we employ
the concept of Shapley values to extract the relationships that the model could identify between the portfolio
characteristics and the statistical properties of the asset universe. We test this pipeline for studying risk-parity
strategies with a volatility target, and in particular, comparing the machine learning-driven Hierarchical Risk
Parity (HRP) to the classical Equal Risk Contribution (ERC) strategy.In the augmented dataset built from
a multi-asset investment universe of commodities, equities and fixed income futures, we find that HRP better
matches the volatility target, and shows better risk-adjusted performances. Finally, we train XGBoost to learn
the difference between the realized Calmar ratios of HRP and ERC and extract explanations.The explanations
provide fruitful ex-post indications of the connection between the statistical properties of the universe and
the strategy performance in the training set. For example, the model confirms that features addressing the
hierarchical properties of the universe are connected to the relative performance of HRP respect to ERC.
Jaeger, M., Krugel, S., Marinelli, D., Papenbrock, J., and Schwendner, P. (2021a).“Interpretable Machine Learning
for Diversified Portfolio Construction.” In: _The Journal of Financial Data Science_ 3(3), pp. 31–51.
In this paper, the authors construct a pipeline to benchmark Hierarchical Risk Parity (HRP) relative to Equal
Risk Contribution (ERC) as examples of diversification strategies allocating to liquid multi-asset futures markets
with dynamic leverage (”volatility target”). The authors use interpretable machine learning concepts (”explain-
able AI”) to compare the robustness of the strategies and to back out implicit rules for decision making. The
empirical dataset consists of 17 equity index, government bond and commodity futures markets across 20 years.
The two strategies are backtested for the empirical dataset and for about 100 000 bootstrapped datasets. XG-
Boost is used to regress the Calmar ratio spread between the two strategies against features of the bootstrapped
datasets. Compared to ERC, HRP shows higher Calmar ratios and better matches the volatility target. Using
Shapley values, the Calmar ratio spread can be attributed especially to univariate drawdown measures of the
asset classes.
Jaeger, M., Krugel, S., Papenbrock, J., and Schwendner, P. (2021b).“Adaptive Seriational Risk Parity and other
Extensions for Heuristic Portfolio Construction using Machine Learning and Graph Theory.” In: _SSRN e-Print_.
In this article, the authors present a conceptual framework named Adaptive Seriational Risk Parity (ASRP)
to extend Hierarchical Risk Parity (HRP) as an asset allocation heuristic. The first step of HRP (quasi-
diagonalization) determining the hierarchy of assets is required for the actual allocation in the second step
of HRP (recursive bisectioning). In the original HRP scheme, this hierarchy is found using the single-linkage
hierarchical clustering of the correlation matrix, which is a static tree-based method. The authors of this paper
compare the performance of the standard HRP with other static and also adaptive tree-based methods, but
also seriation-based methods that do not rely on trees. Seriation is a broader concept allowing to reorder the
rows or columns of a matrix to best express similarities between the elements. Each discussed variation leads
to a different time series reflecting portfolio performance using a 20-year backtest of a multi-asset futures uni-
verse. An unsupervised representation learning based on this time series data creates a taxonomy that groups
the strategies in high correspondence to the structure of the various types of ASRP. The performance analysis
of the variations shows that most of the static tree-based alternatives of HRP outperform the single linkage
clustering used in HRP on a risk-adjusted basis. Adaptive tree methods show mixed results and most generic
seriation-based approaches underperform.
Jennings, W. W., O’Malley, T. C., and Payne, B. C. (2020).“Normal return gaps: dispersion illuminates diversifi-
cation.” In: _The Journal of Wealth Management_ 23(2), pp. 18–35.


Despite ever more sophisticated risk management and measurement, investment professionals have generally
overlooked a simple but powerful measure of relative performance and portfolio diversification the normal return
gap. The authors develop a generalized specification of the expected difference in returns between two investments
based on the folded normal distribution. Even highly correlated investments can have quite large expected return
gaps. They then demonstrate the applicability of this dispersion to capital market forecasts, manager selection,
performance evaluation, style tilts, sector bets, socially responsible investing, manager combinations, wash sale
taxation, and rebalancing.
Jennings, W. W. and Payne, B. C. (2016).“Fees Eat Diversification’s Lunch.” In: _Financial Analysts Journal_ 72(2),
pp. 31–40.
Although diversification is often spoken of as the only free lunch in investing, the authors show that it is not
free and that it must be considered in light of its costs. They also show that fees on diversifying asset classes are
high relative to their risk-adjusted diversification benefit, with the more exotic asset classes carrying higher price
tags. Because there is meaningful cross-sectional variation, fees need to be considered when making strategic
asset allocation decisions.
Kashyap, R. (2017).“Combining Dimension Reduction, Distance Measures and Covariance.” In: _arXiv e-Print_.
We develop a novel methodology based on the marriage between the Bhattacharyya distance, a measure of
similarity across distributions of random variables, and the Johnson Lindenstrauss Lemma, a technique for
dimension reduction. The resulting technique is a simple yet powerful tool that allows comparisons between data-
sets representing any two distributions. The degree to which different entities, (markets, groups of securities, etc.),
have different measures of their corresponding distributions tells us the extent to which they are different, aiding
participants looking for diversification or looking for more of the same thing. We demonstrate a relationship
between covariance and distance measures based on a generic extension of Stein’s Lemma. We consider an asset
pricing application and then briefly discuss how this methodology lends itself to numerous marketstructure
studies and even applications outside the realm of finance / social sciences by illustrating a biological application.
Kazak, E. and Pohlmeier, W. (2019).“Testing out-of-sample portfolio performance.” In: _International Journal of
Forecasting_ 35(2), pp. 540–554.
This paper studies the quality of portfolio performance tests based on out-of-sample returns. By disentangling
the components of the out-of-sample performance, we show that the observed differences are driven largely by
the differences in estimation risk. Our Monte Carlo study reveals that the puzzling empirical findings of inferior
performances of theoretically superior strategies result mainly from the low power of these tests. Thus, our results
provide an explanation as to why the null hypothesis of equal performance of the simple equally-weighted
portfolio compared to many theoretically-superior alternative strategies cannot be rejected in many out-of-
sample horse races. Our findings turn out to be robust with respect to different designs and the implementation
strategies of the tests. For the applied researcher, we provide some guidance as to how to cope with the problem
of low power. In particular, we make use of a novel pretest-based portfolio strategy to show how the information
regarding performance tests can be used optimally.
Kazak, E. and Pohlmeier, W. (2020). _Portfolio Pretesting with Machine Learning_. Tech. rep. University of Lancaster.
This paper exploits the idea of pretesting to choose between competing portfolio strategies. We propose an
estimator for a portfolio weight vector, which optimally trades off between Type I and Type II errors when
choosing the best investment strategy. Furthermore we accommodate the idea of bagging in the portfolio testing
problems, which helps to avoid sharp thresholding and reduces the amount of portfolio turnover. Our approach
borrows from both shrinkage and forecast combination literature. The portfolio weights of our strategy are
weighted averages of the portfolio weights from a set of stand-alone strategies. More specifically, the weights are
generated from a pseudo out-of-sample portfolio pretesting, such that they reflect the probability that a given
strategy will be overall best performing. Contrary to previous approaches, the shrinkage intensity is continuously
updated to incorporate the most recent information in the rolling window forecasting set-up. We show that the
bagged pretest estimator performs exceptionally well, especially when combined with adaptive smoothing. The
resulting strategy allows for a flexible and smooth switch between the underlying strategies and is shown to
outperform the corresponding stand-alone strategies.
Kelliher, C., Hazrachoudhury, A., and Irving, B. (2022).“A Novel Approach to Risk Parity: Diversification across
Risk Factors and Market Regimes.” In: _The Journal of Portfolio Management_ 48(3).
In this article, the authors describe a robust approach to portfolio diversification that balances risk contributions
across risk factors and market regimes. After identifying four compensated macro risk factors-growth, inflation,
real rates, and liquidity-the authors construct a factor portfolio for each based on a broad set of asset classes,


including proxies for private equity and private real estate. Next, the authors identify five distinct market
regimes characterized by unique asset class behaviors. The factor portfolios are then combined such that the
risk contributions to the resulting total portfolio are as balanced as possible, regardless of which market regime
materializes. By combining regime-aware correlations with dynamic volatility estimates for each factor and
applying standard 1.5x to 2x leverage, the authors demonstrate a risk-parity portfolio with 10% ex ante volatility
and attractive absolute and risk-adjusted returns. Compared with a traditional 60/40 portfolio, the proposed risk-
parity portfolio displays greater diversification, more consistent factor-risk contributions, and greater resilience
to economic shocks.
Kilmurray, D., Melin, L., and Mercereau, B. (2021).“Integrating Impact Funds into Mainstream Portfolios.” In:
_The Journal of Impact and ESG Investing_ 1(4), pp. 103–119.
Interest in impact investing is growing, but investors typically allocate to impact funds and traditional assets
independently from one another. We develop an optimizer that brings both types of assets together. Doing so
allows investors to maximize impact for a certain level of risk-adjusted returns. For example, we find that investors
can allocate 18% more to impact funds on average while keeping risk-adjusted returns constant. Intuitively,
analyzing how impact funds and traditional assets interact should allow for better portfolio diversification. As
interest in impact investing broadens, tools integrating impact funds into mainstream finance should become
more widespread.
Kinlaw, W. B., Kritzman, M., Page, S., and Turkington, D. (2021).“The Myth of Diversification Reconsidered.”
In: _The Journal Of Portfolio Management_ 47(8).
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
Koekebakker, S. and Zakamulin, V. (2021).“Warren Buffett versus Zvi Bodie: Should You Buy Or Sell Put Options?”
In: _The Journal of Wealth Management_ 24(2), pp. 65–81.
Academics and investment professionals often disagree when it comes to investment advice. Legendary investor
Warren Buffett is a proponent of time diversification and firmly believes that stocks are less risky in the long
run. Therefore, he often sells long-term put options instead of buying them for portfolio protection. By contrast,
famous professor Zvi Bodie argues that time diversification is a fallacy and, therefore, his advice to fund managers
is to buy long-term portfolio insurance. In this paper, we consider the optimal portfolio choice problem for a
loss-averse investor. First, we demonstrate that our loss-averse investor subscribes to the principle of time
diversification. In particular, our investor allocates more to stocks as the investment horizon lengthens. Second,
we allow our investor to trade in stocks and put options. We find that when the investment horizon is short,
our investor is better off with portfolio insurance. Conversely, when the investment horizon is long, our investor
sells put options. That is, our loss-averse investor prefers Buffett’s investment advice over Bodie’s.
Koumou, G. B. (2020).“Diversification and portfolio theory: a review.” In: _Financial Markets and Portfolio Man-
agement_ 34, pp. 267–312.
Diversification is one of the major components of investment decision-making under risk or uncertainty. However,
paradoxically, as the 2007-2009 financial crisis revealed, the concept remains misunderstood. Our goal in writing
this paper is to correct this issue by reviewing the concept in portfolio theory. The core of our review focuses
on the following diversification principles: law of large numbers, correlation, capital asset pricing model and
risk contribution or risk parity diversification principles. These four diversification principles are the DNA of
the existing portfolio selection rules and asset pricing theories and are instrumental to the understanding of


diversification in portfolio theory. We review their definition. We also review their optimality, with respect to
expected utility theory, and their usefulness. Finally, we explore their measurement.
Kritzman, M. (2015).“What Practitioners Need to Know ... About Time Diversification (corrected).” In: _Financial
Analysts Journal_ 71(1), pp. 29–34.
Although an investor may be less likely to lose money over a long horizon than over a short horizon, the
magnitude of a potential loss increases with the length of the investment horizon.
Kuntz, L.-C. (2018).“Portfolio Strategies with Classical and Alternative Benchmarks.” PhD thesis. Georg August
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
Kurtti, M. (2020).“How many stocks make a diversified portfolio in a continuous-time world?” MA thesis. University
of Oulu.
This thesis aims to answer how many stocks make a diversified portfolio in a continuous-time world. The study
investigates what are the factors determining diversification effects in a real, continuous-time, world as opposed
to thoroughly studied theoretical single period world. Continuous-time world investors care about geometric,
instead of arithmetic, rate of return.
We show how methodology based on information theory can be utilized in investing context. Geometric risk
premium is explained by the Shannon limit and its derivative, fractional Kelly criterion. Investing world coun-
terpart for the Shannon limit, compounding process capacity, is derived. Geometric risk premium is decomposed
to single stock risk premium and diversification premium. Method for estimating diversification premium is
provided. Concept of realizable risk premium is derived and used in risk averse investor diversification metrics.
Diversification effect is measured as a (realizable) risk premium ratio and as a (realizable) gross compound
excess wealth ratio. Both ratios are between a randomly selected portfolio of selected size and fully diversified
benchmark.
We show, both analytically and empirically, that diversification in a continuous-time world is a negative price
lunch as opposed to free lunch in a single period world. Investor is paid a diversification premium, implying
higher geometric risk premium, for consuming a lunch. The magnitude of diversification premium difference
to benchmark, the opportunity cost of foregone diversification, is shown to be equal to one half of portfolio’s
idiosyncratic variance scaled by squared investment fraction. To maintain a constant wealth ratio, required level
of diversification for a long-term risk neutral investor is approximately directly proportional to investment time
horizon length.
The factors determining required level of diversification in a continuous-time world are number of stocks in the
benchmark, Sharpe ratio and variance of the benchmark, idiosyncratic variance of an average stock, investment
fraction and time. At investment fraction 1.0, risk averse investor requires more than 100, 200 or 1000 stocks
to achieve 90%, 95% or 99% of the maximum diversification benefit, respectively. For short-term risk neutral
investor, the corresponding numbers are about 20, 40 or 200 stocks and yet significantly more for long-term risk
neutral investor. The numbers increase and decrease as investment fraction increase and decrease, respectively.
We find that small firms require substantially more diversification compared to large firms and that there are
substantial and consistent differences in diversification premiums between investing styles.
Lassance, N. (2021).“Reconciling Mean-Variance Portfolio Theory with Non-gaussian Returns.” In: _SSRN e-Print_.


Mean-variance portfolio theory remains frequently used as investment rationale because of its simplicity, its
closed-form solution, and the availability of many well-performing robust estimators. At the same time, it is also
frequently rejected on the grounds that it ignores the higher moments of non-Gaussian returns. However, higher-
moment portfolios are associated with many different objective functions, are numerically more complex, and
exacerbate estimation risk. In this paper, we reconcile mean-variance portfolio theory with non-Gaussian returns
by identifying, among all portfolios on the mean-variance efficient frontier, the one that optimizes a chosen higher-
moment criterion. Via numerical simulations and an empirical analysis, we find that, for three higher-moment
objective functions and adjusting for transaction costs, the resulting portfolios outperform the minimum-variance
and fully optimized portfolios out of sample both in terms of Sharpe ratio and higher moments, thus striking a
favorable tradeoff between specification and estimation error.
Lassance, N., DeMiguel, V., and Vrins, F. D. (2020).“Optimal portfolio diversification via independent component
analysis.” In: _SSRN e-Print_.
A popular approach for enhancing diversification in portfolio selection is to rely on the factor-risk-parity portfolio,
which is often defined as the portfolio whose return variance is spread equally among the principal components
(PCs) of asset returns. Although PCs are useful for dimensionality reduction, they are arbitrary because any
rotation of the PC basis yields an equally uncorrelated basis. This is problematic because we theoretically
demonstrate that any portfolio is the factor-risk-parity portfolio corresponding to a specific uncorrelated basis.
To overcome this problem, we rely on the factor-risk-parity portfolio based on the independent components
(ICs), which are the rotation of the PCs that are maximally independent, and thus, account for higher-order
moments. We propose a shrinkage portfolio that is obtained by combining the minimum-variance portfolio and
the IC-risk-parity portfolio. We also show how to exploit the near independence of the ICs to parsimoniously
estimate the factor-risk-parity portfolio with respect to Value-at-Risk. Finally, we empirically demonstrate that
shrinkage portfolios based on the IC basis outperform those based on the PC basis, as well as the minimum-
variance portfolio.
Laur, B. (2020).“Portfolio Optimization - Can Optimizing Portfolio Outperform Naive Diversification?” In: _SSRN
e-Print_.
In this study we examined the performances of mean-variance and tangency portfolio investment strategies in
order to determine if optimal diversification has benefits over 1/N strategy.
Laurinaityte, N., Meinerding, C., Schlag, C., and Thimme, J. (2019).“Elephants and the Cross-Section of Expected
Returns.” In: _SSRN e-Print_.
The population growth of captive Asian elephants explains the cross-section of expected returns of size-value
sorted portfolios with a cross-sectional R2 of 93% and a t-statistic of 4.0 for the market price of risk. One may be
tempted to conclude that elephants are the new outstanding factor in empirical asset pricing. We argue that one
has to be careful with such conclusions. Standard GMM cross-sectional asset pricing tests can generate spurious
explanatory power for factor models when the weight on certain moment conditions is set inappropriately. In
fact, by shifting the weights in the GMM, any desired level of cross-sectional fit can be attained at the price
of not matching the factor means. We run placebo tests with factors that by construction do not explain the
cross-section of expected returns and obtain spuriously high cross-sectional R2’s. Finally, we document some
examples of factor models proposed in the literature that suffer from this bias.
Le Courtois, O. A. (2020).“On the Diversification of Fixed Income Assets.” In: _SSRN e-Print_.
This article introduces a new approach for dealing with the diversification/concentration risk of fixed income
assets. Because Government bonds, corporate bonds, and mortgage securities constitute most of the assets of
insurance companies in most countries, it is important to be able to determine the number of lines/issuers of
such assets, not only for portfolio management, but also for risk management purposes. The approach that we
introduce allows us to show the dependence of the critical number of lines of fixed income assets on the main
interest rate risk and credit risk drivers. Specifically, we examine the importance of volatility risk, force of mean
reversion, default risk, recovery risk, and default dependence risk on the critical number of fixed income assets
in which an insurance business should invest.
Lee, W. (2011).“Risk-Based Asset Allocation: A New Answer to an Old Question?” In: _The Journal of Portfolio
Management_ 37(4), pp. 11–28.
In recent years, we have witnessed an alarmingly large and growing amount of literature on portfolio construction
approaches focused on risks and diversification rather than on estimating expected returns. Numerous simulations
applied to different universes have been documented in support of these approaches based on their apparent
outperformance versus passive market capitalization-weighted or static fixed-weight portfolios. Many studies


attribute the better performance of these risk-based asset allocation approaches to superior diversification.
Given the absence of clearly defined investment objective functions behind these approaches as well as the
metrics used by these studies to evaluate ex post performance, Lee puts these approaches into the same context
of mean-variance efficiency in an attempt to understand their theoretical underpinnings. In doing so, he hopes
to shed some light on what these approaches attempt to achieve and on the characteristics of the investment
universe, if indeed these approaches are meant to approximate mean-variance efficiency. Rather than adding
to the already large collection of simulation results, Lee uses some simple examples to compare and contrast
the portfolio and risk characteristics of these approaches. He also reiterates that any portfolio which deviates
from the market capitalization-weighted portfolio is an active portfolio. He concludes that there is no theory to
predict, ex ante, that any of these risk-based approaches should outperform.
Lee, W. (2013).“Risk Based Asset Allocation.” In: _Second Annual Inside Indexing Conference_.
In recent years, we have witnessed an alarmingly large and growing amount of literature on portfolio construction
approaches focused on risks and diversification rather than estimating expected returns. Numerous simulations,
applied to different universes, have been documented in support of these approaches based on their apparent
outperformance versus passive market-capitalization weighting or static, fixed weight portfolios. Many studies
attribute the better performance of these risk-based asset allocation approaches to superior diversification.
Given the absence of clearly defined investment objective functions behind these approaches as well as the
metrics used by these studies to evaluate ex-post performance, we put these approaches into the same context
of mean-variance efficiency in an attempt to understand their theoretical underpinnings. In doing so, we hope
to shed some light on what these approaches attempt to achieve and on the characteristics of the investment
universe, if indeed these approaches are meant to approximate meanvariance efficiency. Rather than adding to
the already large collection of simulation results, we use some simple examples to compare and contrast the
portfolio and risk characteristics of these approaches. We also reiterate that any portfolio that deviates from the
market capitalization-weighted portfolio is an active portfolio. Finally, we conclude there is no theory to predict,
ex-ante, that any of these riskbased approaches should outperform.
Levy, H. and Levy, M. (2021).“The cost of diversification over time, and a simple way to improve target-date
funds.” In: _Journal of Banking & Finance_ 122, p. 105995.
Diversification across time means changing the asset allocation over time. We show that under mild conditions
diversification across time is inferior for all risk-averters and for all investment horizons, relative to a portfolio
with the same average asset allocation, held constant over time. Target-date funds help reduce the variation in
the asset allocation throughout the lifecycle, by implicitly considering the reduction in human capital with age.
However, their structure implies two systematic deviations from constant asset allocation. We suggest a simple
correction leading to a typical increase of 5%-22% in welfare.
Lim, T. and Ong, C. S. (2021).“Portfolio Diversification Using Shape-Based Clustering.” In: _The Journal of Fi-
nancial Data Science_ 3(1), pp. 111–126.
Portfolio diversification involves lowering the correlation between portfolio assets to achieve improved risk-return
exposure. It is reasonable to infer from the classic Anscombe quartet that relying on descriptive statistics,
and specifically, correlation, to achieve portfolio diversification may not derive the most optimal multiperiod
portfolio risk-adjusted return because stocks in a portfolio can exhibit different price trends over time, even with
the same computed pairwise correlation. This research applied a shape-based time-series clustering technique
of agglomerative hierarchical clustering using dynamic time-series warping as a distance measure to aggregate
stocks into like-trending clusters across time as a portfolio diversification tool. Results support the use of the
shape-based clustering technique for (1) portfolio allocation and rebalancing, (2) dynamic predictive portfolio
construction, and (3) individual stock selection through outlier identification. The findings will be a useful
addition to the existing literature in portfolio management by providing shape-based clustering as an alternative
tool for portfolio construction and security selection.
Lohre, H., Rother, C., and Schafer, K. A. (2020).“Hierarchical Risk Parity: Accounting for Tail Dependencies
in Multi-asset Multi-factor Allocations.” In: _Machine Learning for Asset Management: New Developments and
Financial Applications_. Ed. by E. Jurczenko. Wiley, pp. 329–368.
This chapter examines the use and merits of hierarchical clustering techniques in the context of multi-asset
multi-factor investing. In particular, it contrasts these techniques with several competing risk-based allocation
paradigms, such as 1/N, minimum-variance, standard risk parity and diversified risk parity. The chapter intro-
duces hierarchical risk parity (HRP) strategies based on the Pearson correlation coefficient and also introduces
hierarchical clustering based on the lower tail dependence coefficient. The chapter provides an overview of tradi-


tional risk-based allocation strategies and outlines a framework to measure and manage portfolio diversification.
It examines the performance of the introduced HRP strategies relative to the traditional alternatives. The chap-
ter discusses Meucci’s approach to managing diversification, which serves to construct a diversified risk parity
strategy based on economic factors.
Lopez de Prado, M. (2016).“Building Diversified Portfolios that Outperform Out of Sample.” In: _The Journal of
Portfolio Management_ 42(4), pp. 59–69.
In this article, the author introduces the Hierarchical Risk Parity (HRP) approach to address three major con-
cerns of quadratic optimizers, in general, and Markowitz’s critical line algorithm (CLA), in particular: instability,
concentration, and underperformance. HRP applies modern mathematics (graph theory and machine-learning
techniques) to build a diversified portfolio based on the information contained in the covariance matrix. How-
ever, unlike quadratic optimizers, HRP does not require the invertibility of the covariance matrix. In fact,
HRP can compute a portfolio on an ill-degenerated or even a singular covariance matrix an impossible feat for
quadratic optimizers. Monte Carlo experiments show that HRP delivers lower out-ofsample variance than CLA,
even though minimum variance is CLA’s optimization objective. HRP also produces less risky portfolios out of
sample compared to traditional risk parity methods.
Lopez de Prado, M. (2019).“A Data Science Solution to the Multiple-Testing Crisis in Financial Research.” In: _The
Journal of Financial Data Science_ 1(1), pp. 99–110.
Most discoveries in empirical finance are false, as a consequence of selection bias under multiple testing. Although
many researchers are aware of this problem, the solutions proposed in the literature tend to be complex and hard
to implement. In this article, the author reduces the problem of selection bias in the context of investment strategy
development to two sub-problems: determining the number of essentially independent trials and determining
the variance across those trials. The author explains what data researchers need to report to allow others to
evaluate the effect that multiple testing has had on reported performance. He applies his method to a real case
of strategy development and estimates the probability that a discovered strategy is false.
Lopez de Prado, M. (2020). _Machine learning for asset managers_. Cambridge University Press. 190 pp.
Successful investment strategies are specific implementations of general theories. An investment strategy that
lacks a theoretical justification is likely to be false. Hence, an asset manager should concentrate her efforts
on developing a theory rather than on backtesting potential trading rules. The purpose of this Element is to
introduce machine learning (ML) tools that can help asset managers discover economic and financial theories.
ML is not a black box, and it does not necessarily overfit. ML tools complement rather than replace the classical
statistical methods. Some of ML’s strengths include (1) a focus on out-of-sample predictability over variance
adjudication; (2) the use of computational methods to avoid relying on (potentially unrealistic) assumptions;
(3) the ability to learn complex specifications, including nonlinear, hierarchical, and noncontinuous interaction
effects in a high-dimensional space; and (4) the ability to disentangle the variable search from the specification
search, robust to multicollinearity and other substitution effects.
Lopez de Prado, M. and Lewis, M. J. (2019).“Detection of false investment strategies using unsupervised learning
methods.” In: _Quantitative Finance_ 19(9), pp. 1555–1565.
In this paper we address the problem of selection bias under multiple testing in the context of investment strate-
gies. We introduce an unsupervised learning algorithm that determines the number of effectively uncorrelated
trials carried out in the context of a discovery. This estimate is critical for computing the familywise false positive
probability, and for filtering out false investment strategies.
Louton, D. and Saraoglu, H. (2008).“How Many Mutual Funds Are Needed to Form a Well- Diversified Asset
Allocated Portfolio?” In: _The Journal of Investing_ 17(3), pp. 47–63.
Funds of funds, which have become a popular investment vehicle in recent years, diversify across asset classes
as well as managers with different styles and expertise. Lifecycle funds are a good example of funds of funds
where investors can invest in a group of asset classes in different proportions depending on their investment
horizon, risk tolerance, and objectives. Given that the number of mutual funds in the portfolios of lifecycle funds
offered by different investment companies varies significantly even for those with similar targets, it is important
to investigate the relationship between the number of mutual funds in an asset allocated portfolio and the
resulting diversification benefits. As investors in lifecycle funds are concerned with the level of wealth they will
have accumulated as of a target date, the variability of terminal wealth at the end of a given holding period is
a relevant measure of risk for their portfolios. In this article the authors use a survivorship-bias-free sample to
assess the impact of the number of mutual funds in an asset allocated portfolio on the variability and shortfall
risk of its terminal wealth. Specifically, they run simulations to generate a large number of terminal wealth level


outcomes for a portfolio with a given number of funds. Then, they obtain the frequency distribution of the
terminal wealth outcomes, and use its dispersion as the risk measure in the analysis. The findings for three asset
allocation scenarios, which are reported for 5-year and 10-year investment horizons, indicate that holding 10 to
12 funds in the portfolio instead of the minimum possible 2 funds as dictated by the asset allocation to equity
and bonds reduces the standard deviation of terminal wealth by about 60%. This reduction can be obtained
without sacrificing expected terminal wealth levels, and hence without a reduction in total returns. Similarly,
the mean shortfall of terminal wealth and the semivariance of terminal wealth are reduced by 60% and 85%,
respectively.
Lundstrum, L. L. (2021).“Emerging Market Diversification Benefits: Stock Funds Versus Currency Funds.” In: _The
Journal of Wealth Management_ 24(2), pp. 82–91.
We examine the empirical evidence on the diversification benefits of adding investable emerging market currency
fund exposure to a portfolio that is otherwise internationally-diversified across developed markets, and do likewise
with an emerging market equity fund. We find that emerging market equity exposure does not offer diversification
benefits, while, in contrast, emerging market currency funds do offer diversification benefits. These results are
explained in part by the fact that a large proportion of the currency fund return variance is driven by idiosyncratic
risk, and that proportion has not diminished over time. Furthermore, unlike emerging market equity returns,
emerging market currency returns have not become more integrated over time with an internationally-diversified
developed market portfolio. The results of a spanning test support these findings and suggest that currency funds
favorably shift the efficient frontier. We conclude that emerging market currency funds are an effective investable
vehicle to realize the diversification benefits of emerging market investing.
Madan, D. B. and Wang, K. (2021).“Measuring the Benefits of Diversification Across Portfolios.” In: _SSRN e-Print_.
A portfolio diversification index is defined as the ratio of an equivalent number of independent assets to the
number of assets. The equivalence is based on either attaining the same diversification benefit or spread reduction.
The diversification benefit is the difference in value of a value maximizing portfolio and the maximum value of
the components. The spread reduction is the percentage reduction attained by a spread minimizing portfolio
relative to the smallest spread for the components. Asset values, bid and ask, are given by conservative valuation
operators from the theory of two price economies. The diversification indices fall with the number of assets in
the portfolio and they are explained by a measure of concentration applied to normalized eigenvalues of the
correlation matrix along with the average level of correlation. A time series of the indices constructed on the
basis of the S&P 500 index and the nine sector ETF’s reveals a collapse during the final crisis with no recovery
until 2016, peaking in February 2020 and a COVID crash in March of 2020. Furthermore factor diversification
possibilities are richer than those found in equity indices. Diversification benefits across global indices are not
as strong as diversification across an equal number of domestic assets, but they rise substantially for longer
horizons of up to three years.
Malavasi, M., Lozza, S. O., and Truck, S. (2021).“Second order of stochastic dominance efficiency vs mean variance
efficiency.” In: _European Journal of Operational Research_ 290(3), pp. 1192–1206.
In this paper, we compare two of the main paradigms of portfolio theory: mean variance analysis and expected
utility. In particular, we show empirically that mean variance efficient portfolios are typically sub-optimal for
non satiable and risk averse investors. We illustrate that the second order stochastic dominance (SSD) efficient
set is the solution of a multi-objective optimization problem. We further show that the market portfolio is not
necessarily a solution to this optimization problem. We also conduct an empirical analysis, examining the ex
ante and ex post performance of SSD and mean variance efficient portfolios, using a bootstrap approach. In an
ex ante analysis, we compare empirical moments, the level of diversification and set distances of mean variance
and SSD efficient sets. We also show that the global minimum variance (GMV) portfolio and the part of the
mean variance efficient frontier (MVEF) composed of highly diversified portfolios is second order stochastically
dominated. This result also provides a possible alternative explanation for the diversification puzzle. Conducting
an ex post analysis, we construct second order stochastic dominating strategies that outperform the GMV
portfolio in terms of wealth and various other performance measures, producing a positive ex post opportunity
cost.
Martellini, L. and Milhau, V. (2018).“Proverbial Baskets Are Uncorrelated Risk Factors! A Factor-Based Framework
for Measuring and Managing Diversification in Multi-Asset Investment Solutions.” In: _The Journal of Portfolio
Management_ 44(2), pp. 8–22.
Multi-asset investment solutions have become increasingly popular among sophisticated institutional investors
focusing on efficient harvesting of risk premia across and within asset classes. One key challenge in the con-


struction of diversified multi-asset portfolio strategies is that even a seemingly well-balanced allocation to many
asset classes can eventually translate into a portfolio with a very concentrated set of underlying risk exposures.
The authors suggest using a factor-based framework to more effectively measure and manage diversification in
multi-asset portfolios.
Massahi, M., Mahootchi, M., and Khamseh, A. A. (2020).“Development of an efficient cluster-based portfolio
optimization model under realistic market conditions.” In: _Empirical Economics_.
Modern portfolio theory introduced by Markowitz in 1952 is the most popular portfolio optimization framework
established based on the trade-off between risk and return as an operation research model. The main shortcoming
of applying Markowitz portfolio optimization in practice is that the obtained optimal weights are really sensitive
to the embedded uncertainty in return series of stocks. In this paper, it is demonstrated how using a new
methodology of time series clustering as a remedy can lead to a more robust and accurate portfolio in terms of
the gap between mean variance efficient frontier obtained from the optimization model and the one observed
in reality. In this regard, two similarity measures, the autocorrelation coefficients and the weighted dynamic
time warping, are used in an innovative way to construct the desired portfolio optimization model. Moreover,
the effectiveness of proposed approach is investigated in two different market conditions: semi-realistic and full-
realistic. In the first one, it is assumed that the forecasted and realized stocks mean returns are the same;
however, these returns are not necessarily equal in the second market conditions. Finally, a database of stock
prices from the literature is utilized to show the robustness and accuracy of the proposed approach in empirical
results in comparison with applied similarity measures in previous researches.
McKay, S., Shapiro, R., and Thomas, R. (2018).“What Free Lunch? The Costs of Overdiversification.” In: _Financial
Analysts Journal_ 74(1), pp. 44–58.
Institutional investors, charged with outperforming a policy benchmark, often allocate to external active man-
agers in order to hit their return objective. The challenge is to do so without overdiversifying the plan. Hiring
too many managers can significantly reduce active risk, leaving the plan with high fees and limited ability to
outperform a policy benchmark. We review the number of external investment strategies held by the largest
US public and corporate pension funds. Our analysis shows that most large pension funds are overdiversified,
allowing us to suggest a simpler framework for moving forward.
Meucci, A., Santangelo, A., and Deguest, R. (2015).“Risk budgeting and diversification based on optimised uncor-
related factors.” In: _Risk_.
We measure the contributions to risk of a set of factors, strategies, or investments, based on ”Minimum-Torsion
Bets”, namely a set of uncorrelated factors, optimized to closely track the factors used to allocate the portfolio.
We then introduce a novel definition of contributions to risk, which generalizes the ”marginal contributions to
risk”, traditionally used in banks for risk budgeting and in asset management to build risk parity strategies.
The Minimum-Torsion Bets allow us to also introduce a natural diversification score, the Effective Number
of Minimum-Torsion Bets, which we use to measure and manage diversification. We discuss the advantages of
the Minimum-Torsion Bets over the traditional approach to diversification based on marginal contributions to
risk. We present two case studies, a security-based investment in the stocks of the S&P 500, and a factor-based
investment in the five Fama-French factors.
Molyboga, M. (2020).“A Modified Hierarchical Risk Parity Framework for Portfolio Management.” In: _The Journal
of Financial Data Science_ 2(3), pp. 128–139.
This article introduces a modified hierarchical risk parity (MHRP) approach that extends the HRP approach
by incorporating three intuitive elements commonly used by practitioners. The new approach (1) replaces the
sample covariance matrix with an exponentially weighted covariance matrix with Ledoit-Wolf shrinkage; (2)
improves diversification across portfolio constituents both within and across clusters by relying on an equal
volatility, rather than an inverse variance, allocation approach; and (3) improves diversification across time by
applying volatility targeting to portfolios. The author examines the impact of the enhancements on portfolios
of commodity trading advisors within a large-scale Monte Carlo simulation framework that accounts for the
realistic constraints of institutional investors. The author finds a striking improvement in the out-of-sample
Sharpe ratio of 50%, on average, along with a reduction in downside risk.
Mooney, T., Rapaka, R., and Vera, T. (2020).“Dynamic Regime Strategy for Stress Testing and Optimizing
Institutional Investor Portfolios.” In: _SSRN e-Print_.
Our work aims to develop a stand-alone trading system to construct portfolios that show the benefits of value
and momentum style integration and presents the effectiveness of alternative integration methods for long-only
absolute return funds, which seeks absolute returns that are not highly correlated to traditional assets such


as stocks and bonds. Our approach uses the CRoss Industry Standard Process for Data Mining (CRISP-DM)
model to guide the necessary steps, processes, and workflows for executing our project.
Nguyen, D. K., Topaloglou, N., and Walther, T. (2020).“Asset Classes and Portfolio Diversification: Evidence from
a Stochastic Spanning Approach.” In: _SSRN e-Print_.
We propose a stochastic spanning approach to assess whether a traditional portfolio of stocks and bonds spans
augmented portfolios including commodities, foreign exchange, and real estate. We empirically show that in
all seven portfolio combinations, the augmented portfolio is not spanned by the traditional one. Our results
are further confirmed by both parametric and non-parametric tests in an out-of-sample setting. Therefore,
traditional investors can generally benefit in terms of higher Sharpe ratios from augmenting their portfolio with
alternative asset classes. Additional analysis demonstrates that diversification benefits can be explained by the
current state of the U.S. economy and stock markets.
Olmo, J. (2021).“Optimal portfolio allocation and asset centrality revisited.” In: _Quantitative Finance_ 21(9),
pp. 1475–1490.
This paper revisits the relationship between eigenvector asset centrality and optimal asset allocation in a mini-
mum variance portfolio. We show that the standard definition of eigenvector centrality is misleading when the
adjacency matrix in a network can take negative values. This is, for example, the case when the network topology
is induced by the correlation matrix between assets in a portfolio. To correct for this, we introduce the concept
of positive and negative eigenvector centrality. Our results show that the loss function associated to the mini-
mum variance portfolio is positively/negatively related to the positive and negative eigenvector centrality under
short-selling constraints but cannot be generalized beyond that. Furthermore, in contrast to what is claimed
in the related literature, this relationship does not imply any monotonic relationship between the centrality of
an asset and its optimal portfolio allocation. These theoretical insights are illustrated empirically in a portfolio
allocation exercise with assets from U.S. and U.K. financial markets.
Ouchen, A. (2021).“Is the ESG portfolio less turbulent than a market benchmark portfolio?” In: _Risk Management_
24, pp. 1–33.
Given that there is no consensus on the fact that ESG portfolios are characterized by very high returns and very
low risks compared to conventional portfolios, this study aims to empirically verify whether the series of returns
of an ESG portfolio is less volatile than the returns of a benchmark market portfolio. To verify this hypothesis,
we used the Markov-switching GARCH models in order to model the process of the series of daily returns of
the ESG portfolio ”MSCI USA ESG Select,” as well as those of the market benchmark portfolio daily returns
series ”S&P 500,” during the period June 01, 2005 to December 31, 2020 as well as that excluding the COVID19
crisis and from June 1, 2005 to October 29, 2019. It can be concluded that the ESG portfolio ”MSCI USA ESG
Select” is relatively less turbulent compared to the market benchmark portfolio ”S&P 500.”.
Oyenubi, A. (2019).“Diversification Measures and the Optimal Number of Stocks in a Portfolio: An Information
Theoretic Explanation.” In: _Computational Economics_ (54), pp. 11443-1471–29.
This paper provides a plausible explanation for why the optimum number of stocks in a portfolio is elusive,
and suggests a way to determine this optimal number. Diversification has a lot to do with the number of stocks
in a portfolio. Adding stocks to a portfolio increases the level of diversification, and consequently leads to risk
reduction up to a certain number of stocks, beyond which additional stocks are of no benefit, in terms of risk
reduction. To explain this phenomenon, this paper investigates the relationship between portfolio diversification
and concentration using a genetic algorithm. To quantify diversification, we use the portfolio Diversification Index
(PDI). In the case of concentration, we introduce a new quantification method. Concentration is quantified as
complexity of the correlation matrix. The proposed method quantifies the level of dependency (or redundancy)
between stocks in a portfolio. By contrasting the two methods it is shown that the optimal number of stocks
that optimizes diversification depends on both number of stocks and average correlation. Our result shows that,
for a given universe, there is a set of Pareto optimal portfolios containing a different number of stocks that
simultaneously maximizes diversification and minimizes concentration. The choice portfolio among the Pareto
set will depend on the preference of the investor. Our result also suggests that an ideal condition for the optimal
number of stocks is when variance reduction benefit of diversification is off-set by the variance contribution of
complexity.
Page, S. (2020). _Beyond Diversification: What Every Investor Needs to Know About Asset Allocation_. McGraw Hill.
220 pp.
Written by a leading allocation expert from T. Rowe Price, Beyond Diversification provides the knowledge,
insights, and approaches you need to make the best allocation decisions for your goals. This deep dive into the


how’s and why’s of asset allocation is organized by the three decisive components of a successfully allocated
portfolio:
1) Return Forecasting discusses the desired return investors seek.
2) Risk Forecasting covers the level of risk investors are prepared to assume to achieve that return.
3) Portfolio Construction calibrates the stock-bond mix that balances the risks and returns.
.
Page, S. and Panariello, R. A. (2018).“When Diversification Fails.” In: _Financial Analysts Journal_ 74(3), pp. 19–32.
One of the most vexing problems in investment management is that diversification seems to disappear when
investors need it the most. We surmise that many investors still do not fully appreciate the impact of extreme
correlations on portfolio efficiency particular, on exposure to loss. We take an in-depth look at what drives the
stock-to-credit, stock-to-hedge fund, stock-to-private asset, stock-to-risk factors, and stock-to-bond correlations
during tail events. We introduce a data-augmentation technique to improve the robustness of tail correlation
estimates. Finally, we discuss implications for multi-asset investing.
Page, S. and Taborsky, M. A. (2011).“The myth of diversification: risk factors versus asset classes.” In: _The Journal
of Portfolio Management_ 37(4), pp. 1–2.
In our New Normal world, regime shifts in economic conditions will continue to cause significant challenges
for risk management and portfolio construction. On average, correlations across risk factors are lower than
correlations across asset classes, and risk factor correlations tend to be more robust to regime shifts. Risk factors
provide a flexible language with which investors may express their forward-looking economic views, adapt to
regime shifts and diversify their portfolios accordingly.
Papathanakos, V. (2020).“Diversification Potential.” In: _SSRN e-Print_.
In these working notes, we introduce the concept of the diversification potential, which expresses the maximum
diversification premium available by rebalancing to fixed target weights for a collection of assets. We distinguish
between two forms of diversification potential: the unconstrained (which allows portfolios with short positions)
and the constrained (which only permits long-only portfolios).
Papenbrock, J., Schwendner, P., Jaeger, M., and Krugel, S. (2021).“Matrix Evolutions: Synthetic Correlations and
Explainable Machine Learning for Constructing Robust Investment Portfolios.” In: _The Journal of Financial
Data Science_ 3(2), pp. 51–69.
In this article, the authors present a novel and highly flexible concept to simulate correlation matrixes of financial
markets. It produces realistic outcomes regarding stylized facts of empirical correlation matrixes and requires
no asset return input data. The matrix generation is based on a multiobjective evolutionary algorithm, so the
authors call the approach matrix evolutions. It is suitable for parallel implementation and can be accelerated by
graphics processing units and quantum-inspired algorithms. The approach is useful for backtesting, pricing, and
hedging correlation-dependent investment strategies and financial products. Its potential is demonstrated in a
machine learning case study for robust portfolio construction in a multi-asset universe: An explainable machine
learning program links the synthetic matrixes to the portfolio volatility spread of hierarchical risk parity versus
equal risk contribution.
Parmentier, L. (2018).“Measures of Portfolio Diversification.” MA thesis. Louvain School of Management.
Diversification is one the main and most important concept in the financial world. It is often said that diver-
sification is the only free lunch in finance. From a qualitative point of view, the concept of diversification is
quite clear: a portfolio is well-diversified if shocks in the individual components do not heavily impact on the
overall portfolio. Relatively simple to understand then but profoundly difficult to define. Indeed, there is no
broadly accepted precise and quantitative definition of diversification. Over the years, many different measures
of diversification have been developed in the literature, each with its pros and cons. In the framework of this
thesis, we have chosen to analyze six of them. Because we wanted to confront the weights concentration criterion
with the risk minimization criterion, we decided to select measures that are based on the entropy of the weights
and others that are based on the sources of risk. Those six different measures are the Shannon’s Entropy, the
Diversification Delta, the Diversification Ratio, the MarginalRisk Contributions, the Portfolio Diversification
Index and the Effective Number of Bets.
Pastor, L., Stambaugh, R. F., and Taylor, L. A. (2017).“Portfolio Liquidity and Diversification: Theory and
Evidence.” In: _SSRN e-Print_.


A portfolio’s liquidity depends not only on the liquidity of its holdings but also on its diversification. We propose
simple, theoretically motivated measures of portfolio liquidity and diversification. We also develop an equilibrium
model relating portfolio liquidity to fund size, expense ratio, and turnover. As the model predicts, mutual funds
with less liquid portfolios have smaller size, higher expense ratios, and lower turnover. The model also yields
additional predictions that we verify empirically: larger funds are cheaper, funds that trade less are larger and
cheaper, and funds that are too big perform worse. We also find that mutual fund portfolios have become more
liquid because both components of diversification, coverage and balance, have trended upward.
Pedersen, M. (2021).“Simple Portfolio Optimization that Works!” In: _SSRN e-Print_.
We first show that the common ”mean-variance” portfolio method fails because variance is a horrible risk-
measure for investing, and also because estimation errors may cause that method to concentrate the portfolio in
losing assets that are highly correlated. We then present a new so-called ”filter-diversify” method for portfolio
optimization. The filtering process is trivial as it only allows assets into the portfolio if they have sufficiently high
estimated returns. The diversification process is based on a new algorithm with several benefits: The algorithm
is fairly simple. It allows both positive and negative portfolio weights. It is extremely fast and only takes a few
milli-seconds to compute for a portfolio of 1000 assets. It is guaranteed to converge to the optimal solution. It
is very robust to estimation errors, because it will only decrease the portfolio weights, so the worst that can
happen is that it moves too much of the portfolio into cash (or another low-risk asset of your choice). We perform
numerous tests of the new portfolio method on real-world stock-data from USA, and find that the new method
performs extremely well on all performance metrics, and is very robust to estimation errors.
Pedersen, M. (2022).“Fast Portfolio Diversification.” In: _SSRN e-Print_.
This is a concise description of a new algorithm for diversifying an investment portfolio, that was previously
described and tested in great detail in another paper, which also showed that the algorithm is very fast and
guaranteed to converge to the optimal solution in just a few iterations, and the algorithm improves the portfolio
on several performance metrics, while being extremely robust to estimation errors in the correlation matrix.
This paper further shows how to implement the algorithm for a sparse correlation matrix, and it compares the
time-usage of the sparse and dense versions of the algorithm, as well as parallel and serial versions.
Petukhina, A., Trimborn, S., Hardle, W. K., and Elendner, H. (2021).“Investing with cryptocurrencies – evaluating
their potential for portfolio allocation strategies.” In: _Quantitative Finance_.
Cryptocurrencies (CCs) have risen rapidly in market capitalization over the past years. Despite striking volatility,
their high average returns and low correlations have established CCs as alternative investment assets for portfolio
and risk management. We investigate the benefits of adding CCs to well-diversified portfolios of conventional
financial assets for different types of investors, including risk-averse, return-maximizing and diversification-
seeking investors who may trade at different frequencies, namely, daily, weekly or monthly. We calculate out-
of-sample performance and diversification benefits for the most popular portfolio-construction rules, including
mean-variance optimization, risk-parity, and maximum-diversification strategies, as well as combined strategies.
Our results demonstrate that CCs can improve the risk-return profile of portfolios, but their benefit depends
on investor objectives. In particular, diversification strategies (maximizing the portfolio diversification index
or equating risk contributions) draw appreciably on CCs and show, in line with spanning tests, CCs to be
non-redundant extensions of the investment universe. However, when we introduce liquidity constraints via the
LIBRO method to account for illiquidity of many CCs, out-of-sample performance drops considerably, while
the diversification benefits persist. We conclude that the utility of CC investments strongly depends on investor
characteristics.
Pham, H., Wei, X., and Zhou, C. (2018).“Portfolio diversification and model uncertainty: a robust dynamic mean-
variance approach.” In: _arXiv e-Print_.
This paper focuses on a dynamic multi-asset mean-variance portfolio selection problem under model uncertainty.
We develop a continuous time framework for taking into account ambiguity aversion about both expected return
rates and correlation matrix of the assets, and for studying the join effects on portfolio diversification. The
dynamic setting allows us to consider time varying ambiguity sets, which include the cases where the drift
and correlation are estimated on a rolling window of historical data or when the investor takes into account
learning on the ambiguity. In this context, we prove a general separation principle for the associated robust
control problem, which allows us to reduce the determination of the optimal dynamic strategy to the parametric
computation of the minimal risk premium function. Our results provide a justification for under-diversification,
as documented in empirical studies and in the static models [16], [34]. Furthermore, we explicitly quantify the
degree of under-diversification in termsof correlation bounds and Sharpe ratios proximities, and emphasize the


different features induced by drift and correlation ambiguity. In particular, we show that an investor with a poor
confidence in the expected return estimation does not hold any risky asset, and on the other hand, trades only
one risky asset when the level of ambiguity on correlation matrix is large. We also provide a complete picture
of the diversification for the optimal robust portfolio in the three-asset case.
Pittman, S., Singh, A., and Srinivasan, S. (2019).“Diversification benefits, where art thou?” In: _The Journal of
Wealth Management_ (22), 3, pp. 70–84.
Following the global financial crisis, a portfolio concentrated in US large cap equity and aggregate fixed income
has provided higher returns than diversified portfolios through 2019. Such a prolonged experience causes in-
vestors to question the benefits of diversification. This leads us to use a longer history of data across 15 asset
classes to understand the historical benefits of diversifying a portfolio with international equity, real assets,
and below investment grade fixed income. Our results portray the frequency and magnitude of risk-adjusted
return improvement coming from different diversifying asset classes over five-year holding periods. We find that
certain asset classes, such as below investment grade fixed income, regularly improve risk-adjusted return of the
portfolio, while other asset classes like commodities improve risk-adjusted returns less frequently. Further, we
observe that some asset classes do not deliver meaningful risk-adjusted return improvements in the presence of
other asset classes. Our conclusion is that investors should continue to build diversified portfolios, but in doing
so they should consider that some asset classes more consistently improved risk-adjusted returns than others.
Platanakis, E., Sakkas, A., and Sutcliffe, C. (2017).“Harmful Diversification: Evidence from Alternative Invest-
ments .” In: _SSRN e-Print_.
Alternative assets have become as important as equities and fixed income in the portfolios of major investors,
and so their diversification properties are also important. However, adding five alternative assets (real estate,
commodities, hedge funds, emerging markets and private equity) to equity and bond portfolios is shown to
be harmful for US investors. We use 19 portfolio models, in conjunction with dummy variable regression, to
demonstrate this harm over the 1997-2015 period. This finding is robust to different estimation periods, risk
aversion levels, and the use of two regimes. Harmful diversification into alternatives is not primarily due to
transactions costs or non-normality, but to estimation risk. This is larger for alternative assets, particularly
during the credit crisis which accounts for the harmful diversification of real estate, private equity and emerging
markets. Diversification into commodities, and to a lesser extent hedge funds, remains harmful even when the
credit crisis is excluded.
Platanakis, E., Sutcliffe, C. M., and Ye, X. (2021).“Horses for Courses: Mean-Variance for Asset Allocation and
1/N for Stock Selection.” In: _European Journal of Operational Research_ 288(1), pp. 302–317.
For various organizational reasons, large investors typically split their portfolio decision into two stages - asset
allocation and stock selection. We hypothesise that mean-variance models are superior to equal weighting for
asset allocation, while the reverse applies for stock selection, as estimation errors are less of a problem for
mean-variance models when used for asset allocation than for stock selection. We confirm this hypothesis in
separate analyses of US and international equities using four different types of mean-variance model (Bayes-
Stein, Black-Litterman, Bayesian diffuse prior and Markowitz), a range of parameter settings, and a simulation
analysis calibrated to US data.
Pola, G. (2016).“On entropy and portfolio diversification.” In: _Journal of Asset Management_ 17, pp. 218–228.
Entropy, a term used in Physics to quantify the degree of randomness in a complex system, is shown to be relevant
for portfolio diversification. The link between entropy and diversification lies in the notion of uncertainty. We
introduce the concept of available diversification in an investment universe and of diversification curves. We build
a framework for assembling a fully diversified risk parity-like portfolio with a fundamental-based high-conviction
strategy, through a constrained entropy-maximisation process by which a portion of potential portfolio return
is swapped for extra diversification. The main results of this study are: mean-variance optimised portfolios are
highly concentrated and scarcely related to the asset return assumptions; few basis points of expected returns
can be converted into a huge amount of extra diversification that making the portfolio allocation more robust to
parameter uncertainty; on a more conceptual ground, we investigate the relationship between portfolio risk and
diversification concluding that they should be managed distinctly. The empirical analysis presented in this work
shows that entropy is a useful means to alleviate the lack of diversification of portfolios on the efficient frontier.
Pourbabaee, F., Kwak, M., and Pirvu, T. A. (2016).“Risk minimization and portfolio diversification.” In: _Quanti-
tative Finance_ 16(9), pp. 1325–1332.
In an incomplete market Black-Scholes setting with constant parameters, the optimal portfolioswhich minimize
theCaRand achieve a negative prescribed correlationwith a given financial index, are characterized analytically.


It is shown that, under a certain choice of the financial market, the correlation constraint leads to a more
diversified portfolio, that is, the variance of constrained optimal portfolios is lower than the variance of optimal
unconstrained portfolios. Moreover, it turns out that the correlation constraint reduces the variance and increases
the risk-free investment during market declines. Numerical experiments explore the effect on the optimal portfolio
composition induced by the correlation constraint.
Radovanov, B. and Marcikic, A. (2014).“Testing The Performance Of The Investment Portfolio Using Block Boot-
strap Method.” In: _Economic Themes_ 52(2).
The aim of this paper is to create a stable model of investment portfolio optimization through a high degree
of diversification and reduction of sudden changes in the allocation with monitoring of the dynamics of the
impact factor. In this sense, there is bootstrap application procedure, which, without an excessive number of
constraints involved in the optimization process provides solutions based on uncertain information. Thus defined,
the optimization method has been patented by Michaud (1999) entitled re-sampled efficiency. Accordingly, this
paper offers a comparison of the performance block bootstrap optimization models and traditional Markowitz’s
model inside and outside of the sample by applying the most frequently traded stocks on the BSE. The results
show a better performance out of the sample and the presence of a larger number of shares forming the portfolio
through bootstrap methodology. However, only through the traditional optimization process could be attained
optimum according to the required limits. Such effects can be observed by comparing the limits of efficiency
obtained through these optimization models. However, optimization-based methods bootstrap finds its place in
reducing errors of assessment resulting from the limited sample size.
Raffinot, T. (2017).“Hierarchical Clustering-Based Asset Allocation.” In: _The Journal of Portfolio Management_
44(2), pp. 89–99.
This article proposes a hierarchical clustering-based asset allocation method, which uses graph theory and
machine learning techniques. Hierarchical clustering refers to the formation of a recursive clustering, suggested
by the data, not defined a priori. Several hierarchical clustering methods are presented and tested. Once the
assets are hierarchically clustered, the authors compute a simple and efficient capital allocation within and
across clusters of assets, so that many correlated assets receive the same total allocation as a single uncorrelated
one. The out-of-sample performances of hierarchical clustering-based portfolios and more traditional risk-based
portfolios are evaluated across three disparate datasets, which differ in term of the number of assets and the
assets’ composition. To avoid data snooping, the authors assess the comparison of profit measures using the
bootstrap-based model confidence set procedure. Their empirical results indicate that hierarchical clustering-
based portfolios are robust and truly diversified and achieve statistically better risk-adjusted performances than
commonly used portfolio optimization techniques.
Raffinot, T. (2018).“The Hierarchical Equal Risk Contribution Portfolio.” In: _SSRN e-Print_.
Building upon the fundamental notion of hierarchy, the ”Hierarchical Risk Parity” (HRP) and the ”Hierarchical
Clustering based Asset Allocation” (HCAA), the Hierarchical Equal Risk Contribution Portfolio (HERC) aims
at diversifying capital allocation and risk allocation. HERC merges and enhances the machine learning approach
of HCAA and the Top-Down recursive bisection of HRP. In more detail, the modified Top-Down recursive
division is based on the shape of dendrogram, follows an Equal Risk Contribution allocation and is extended to
downside risk measures such as conditional value at risk (CVaR) and Conditional Drawdown at Risk (CDaR).
The out-of-sample performances of hierarchical clustering based portfolios are evaluated across two empirical
datasets, which differ in terms of number of assets and composition of the universe (multi-assets and individual
stocks). Empirical results highlight that HERC Portfolios based on downside risk measures achieve statistically
better risk-adjusted performances, especially those based on the CDaR.
Raju, R. and Agarwalla, S. K. (2021).“Equity Portfolio Diversification: How Many Stocks Are Enough? Evidence
From India.” In: _SSRN e-Print_.
How many stocks are required to reduce unsystematic risk significantly is an important question for investors.
While there is a large body of research on the subject in the United States, there is little formal work on this
question in India. We show that a 15-20 stock portfolio, the traditional market rule-of-thumb for a diversified
portfolio, is likely inadequate to minimize unsystematic risk. We show that an investor could target to reduce
diversifiable risk by 90% with a 90% confidence with a portfolio of 40-50 stocks. We build a practical framework
that serves as a baseline for investors to target a specific reduction in diversifiable unsystematic risk at a chosen
confidence level.
Rebonato, R. (2019).“A financially justifiable and practically implementable approach to coherent stress testing.”
In: _Quantitative Finance_ 19(5), pp. 827–842.


We present an approach to stress testing that is both practically implementable and solidly rooted in well-
established financial theory. We present our results in a Bayesian-net context, but the approach can be extended
to different settings. We show (i) how the consistency and continuity conditions are satisfied; (ii) how the result
of a scenario can be consistently cascaded from a small number of macrofinancial variables to the constituents
of a granular portfolio; and (iii) how an approximate but robust estimate of the likelihood of a given scenario
can be estimated. This is particularly important for regulatory and capital-adequacy applications.
Reinholtz, N., Fernbach, P. M., and Langhe, B. de (2021).“Do People Understand the Benefit of Diversification?”
In: _Management Science_.
Diversification-investing in imperfectly correlated assets-reduces volatility without sacrificing expected returns.
Although the expected return of a diversified portfolio is the weighted average return of its constituent parts, the
variance of the portfolio is less than the weighted average variance of its constituent parts. Our results suggest
that very few people have correct statistical intuitions about the effects of diversification. The average person in
our data sees no benefit of diversification in terms of reducing portfolio volatility. Many people, especially those
low in financial literacy, believe diversification actually increases the volatility of a portfolio. These people seem
to believe that the unpredictability of individual assets compounds when aggregated together. Additionally,
most people believe diversification increases the expected return of a portfolio. Many of these people correctly
link diversification with the concept of risk reduction but seem to understand risk reduction to mean greater
returns on average. We show that these beliefs can lead people to construct investment portfolios that mismatch
investors’ risk preferences. Furthermore, these beliefs may help explain why many investors are underdiversified.
Roncalli, T. (2021).“Advanced Course in Asset Management.” In: _SSRN e-Print_.
These presentation slides have been written for the Advanced Course in Asset Management (theory and appli-
cations) given at the University of Paris-Saclay. They contain 15 tutorial exercises and 5 main lectures:
1) Portfolio Optimization
2) Risk Budgeting
3) Smart Beta, Factor Investing and Alternative Risk Premia
4) Green and Sustainable Finance, ESG Investing and Climate Risk
5) Machine Learning in Asset Management
The Table of contents is the following:
Part 1. Portfolio Optimization 1. Theory of portfolio optimization 1.a. The Markowitz framework 1.b. Capital
asset pricing model (CAPM) 1.c. Portfolio optimization in the presence of a benchmark 1.d. Black-Litterman
model 2. Practice of portfolio optimization 2.a. Covariance matrix 2.b. Expected returns 2.c. Regularization of
optimized portfolios 2.d. Adding constraints 3. Tutorial exercises 3.a. Variations on the efficient frontier 3.b.
Beta coefficient 3.c. Black-Litterman model
Part 2. Risk Budgeting 1. The ERC portfolio 1.a. Definition 1.b. Special cases 1.c. Properties 1.d. Numerical
solution 2. Extensions to risk budgeting portfolios 2.a. Definition of RB portfolios 2.b. Properties of RB portfolios
2.c. Diversification measures 2.d. Using risk factors instead of assets 3. Risk budgeting, risk premia and the risk
parity strategy 3.a. Diversified funds 3.b. Risk premium 3.c. Risk parity strategies 3.d. Performance budgeting
portfolios 4. Tutorial exercises 4.a. Variation on the ERC portfolio 4.b. Weight concentration of a portfolio 4.c.
The optimization problem of the ERC portfolio 4.d. Risk parity funds
Part 3. Smart Beta, Factor Investing and Alternative Risk Premia 1. Risk-based indexation 1.a. Capitalization-
weighted indexation 1.b. Risk-based portfolios 1.c. Comparison of the four risk-based portfolios 1.d. The case
of bonds 2. Factor investing 2.a. Factor investing in equities 2.b. How many risk factors? 2.c. Construction of
risk factors 2.d. Risk factors in other asset classes 3. Alternative risk premia 3.a. Definition 3.b. Carry, value,
momentum and liquidity 3.c. Portfolio allocation with ARP 4. Tutorial exercises 4.a. Equally-weighted portfolio
4.b. Most diversified portfolio 4.c. Computation of risk-based portfolios 4.d. Building a carry trade exposure
Part 4. Green and Sustainable Finance, ESG Investing and Climate Risk 1. ESG investing 1.a. Introduction to
sustainable finance 1.b. ESG scoring 1.c. Performance in the stock market 1.d. Performance in the corporate
bond market 2. Climate risk 2.a. Introduction to climate risk 2.b. Climate risk modeling 2.c. Regulation of
climate risk 2.d. Portfolio management with climate risk 3. Sustainable financing products 3.a. SRI Investment
funds 3.b. Green bonds 3.c. Social bonds 3.d. Other sustainability-linked strategies 4. Impact investing 4.a.
Definition 4.b. Sustainable development goals (SDG) 4.c. Voting policy, shareholder activism and engagement
4.d. The challenge of reporting 5. Tutorial exercises 5.a. Probability distribution of an ESG score 5.b. Enhanced
ESG score and tracking error control


Part 5. Machine Learning in Asset Management 1. Portfolio optimization 1.a. Standard optimization algorithms
1.b. Machine learning optimization algorithms 1.c. Application to portfolio allocation 2. Pattern learning and
self-automated strategies 3. Market generators 4. Tutorial exercises 4.a. Portfolio optimization with CCD and
ADMM algorithms 4.b. Regularized portfolio optimization.
Rubbaniy, G., Khalid, A. A., Ali, S., and Naveed, M. (2021).“Are ESG Stocks Safe-Haven during COVID-19?” In:
_SSRN e-Print_.
This study contributes to the debate on safe-haven characteristics of environmental, social, and governance
(ESG) stocks during COVID-19 pandemic. Using wavelet coherence framework on four major ESG stock indices
from global and emerging stock markets, and two proxies of COVID-19 fear over the period from February 5th,
2020, to March 18th, 2021, we find a strong and positive co-movement between health fear index of COVID-19
and returns on ESG stocks suggesting the existence of safe-haven properties in ESG stocks. However, we also
observe a negative co-movement between stock market base proxy of COVID-19 and returns on ESG indices,
suggesting that safe-haven properties of ESG stocks are contingent upon the proxy of COVID-19 pandemic. Our
findings are of particular interest for the investors and asset managers who may use ESG stocks to diversify
their portfolios during health crisis due to COVID-19 pandemic.
Sakurai, Y., Yuki, Y., Katsuki, R., Yazane, T., and Ishizaki, F. (2021).“Correlation diversified passive portfolio
strategy based on permutation of assets.” In: _The Journal of Investment Strategies_.
In this paper we develop a passive strategy to improve index investing, which we call the correlation diversified
portfolio strategy. The proposed method adjusts the weight vector of the original index based on the permutation
of the assets belonging to the original index. We seek the permutation of these assets such that those assets
with a strong correlation to many other assets are placed in the center of the permutation. By reducing the
weights of such central assets, we can construct portfolios that are more diversified and have better risk-return
characteristics than the original index. We solve this asset-permutation problem by adopting a quantum-inspired
approach. Concretely, we convert this permutation problem into a quadratic unconstrained binary optimization
problem and use simulated annealing on a personal computer or annealing machine to find a near-optimal
solution in a reasonable time. To examine the usefulness and computational feasibility of the proposed method,
we apply it to three major indexes of the United States and Japan, and we provide numerical experiments that
show portfolios constructed by the proposed method can achieve a higher return with lower volatility compared
with the original indexes, while their behaviors are still similar to those of the original indexes.
Scalzo, B., Arroyo, A., Stankovic, L., and Mandic, D. P. (2021a).“Nonstationary Portfolios: Diversification in the
Spectral Domain.” In: _ICASSP 2021 - 2021 IEEE International Conference on Acoustics, Speech and Signal
Processing (ICASSP)_. IEEE.
Classical portfolio optimization methods typically determine an optimal capital allocation through the implicit,
yet critical, assumption of statistical time-invariance. Such models are inadequate for real-world markets as
they employ standard time-averaging based estimators which suffer significant information loss if the market
observables are non-stationary. To this end, we reformulate the portfolio optimization problem in the spectral
domain to cater for the nonstationarity inherent to asset price movements and, in this way, allow for optimal
capital allocations to be time-varying. Unlike existing spectral portfolio techniques, the proposed framework
employs augmented complex statistics in order to exploit the interactions between the real and imaginary parts
of the complex spectral variables, which in turn allows for the modelling of both harmonics and cyclostationarity
in the time domain. The advantages of the proposed framework over traditional methods are demonstrated
through numerical simulations using real-world price data.
Scalzo, B., Arroyo, A., Stankovic, L., and Mandic, D. P. (2021b).“Nonstationary Portfolios: Diversification in the
Spectral Domain.” In: _arXiv e-Print_.
Classical portfolio optimization methods typically determine an optimal capital allocation through the implicit,
yet critical, assumption of statistical time-invariance. Such models are inadequate for real-world markets as
they employ standard time-averaging based estimators which suffer significant information loss if the market
observables are non-stationary. To this end, we reformulate the portfolio optimization problem in the spectral
domain to cater for the nonstationarity inherent to asset price movements and, in this way, allow for optimal
capital allocations to be time-varying. Unlike existing spectral portfolio techniques, the proposed framework
employs augmented complex statistics in order to exploit the interactions between the real and imaginary parts
of the complex spectral variables, which in turn allows for the modelling of both harmonics and cyclostationarity
in the time domain. The advantages of the proposed framework over traditional methods are demonstrated
through numerical simulations using real-world price data.


Scherer, B. (2021).“Adding alternative assets: return enhancement, diversification or hedging?” In: _Journal of Asset
Management_ 22, pp. 437–442.
Adding assets (so-called extensions) to an already existing portfolio is a reoccurring question in times of rapidly
expanding investment opportunity sets. Examples for this ”how much” question are the incorporation of liquid
alternative assets in the form of hedge funds or alternative risk premia in a global balanced portfolio, the
addition of global equities to a domestic equity portfolios or simply the optimal allocation of corporate credit
within a government debt portfolio. While this is hardly a new question and a variety of tools have already been
established, we suggest a new framework to decompose the demand for risky assets in economically meaningful
components. This allows us to identify whether a particular allocation is driven by demand created from noisy
return estimates or by more predictable hedging and diversification demand.
Schumann, E. (2019).“Backtesting.” In: _SSRN e-Print_.
We discuss the backtesting of investment and trading strategies. We start with the challenges and pitfalls:
overfitting, data preparation, and the effects of randomness. Then, we introduce and describe R software for
backtesting. We demonstrate how to use the software for univariate and multivariate strategies (i.e. portfolio
strategies) for two equity data sets. Specifically, we discuss the implementation and testing of momentum and
portfolio optimization models. Throughout, we stress the analysis of sensitivity and robustness checks. Since
such analyses require to run many backtests, we also discuss how backtests can be run in parallel.
Schwendner, P., Papenbrock, J., Jaeger, M., and Krugel, S. (2021).“Adaptive Seriational Risk Parity and Other
Extensions for Heuristic Portfolio Construction Using Machine Learning and Graph Theory.” In: _The Journal
of Financial Data Science_ 3(4), pp. 65–83.
In this article, the authors present a conceptual framework named adaptive seriational risk parity (ASRP) to ex-
tend hierarchical risk parity (HRP) as an asset allocation heuristic. The first step of HRP (quasi-diagonalization),
determining the hierarchy of assets, is required for the actual allocation done in the second step (recursive bisec-
tioning). In the original HRP scheme, this hierarchy is found using single-linkage hierarchical clustering of the
correlation matrix, which is a static tree-based method. The authors compare the performance of the standard
HRP with other static and adaptive tree-based methods, as well as seriation-based methods that do not rely
on trees. Seriation is a broader concept allowing reordering of the rows or columns of a matrix to best express
similarities between the elements. Each discussed variation leads to a different time series reflecting portfolio
performance using a 20-year backtest of a multi-asset futures universe. Unsupervised learningbased on these
time-series creates a taxonomy that groups the strategies in high correspondence to the construction hierarchy
of the various types of ASRP. Performance analysis of the variations shows that most of the static tree-based
alternatives to HRP outperform the single-linkage clustering used in HRP on a risk-adjusted basis. Adaptive
tree methods show mixed results, and most generic seriation-based approaches underperform.
Serur, J. A. and Avellaneda, M. (2021).“Hierarchical PCA and Modeling Asset Correlations.” In: _SSRN e-Print_.
Modeling cross-sectional correlations between thousands of stocks, acrosscountries and industries, can be chal-
lenging. In this paper, we demonstratethe advantages of using Hierarchical Principal Component Analysis
(HPCA)over the classic PCA. We also introduce a statistical clustering algorithmto identify homogeneous clus-
ters of stocks or ”synthetic sectors”. We apply these methods to study cross-sectional correlations in the US,
Europe, China,and Emerging Markets.
Seymour, A., Flint, E. J., and Chikurunhe, F. (2018).“Dynamic portfolio management strategies: A framework for
historical analysis.” In: _SSRN e-Print_.
The performance of dynamic trading and investment strategies can be difficult to predict. Although not without
its problems, analysis of the historical performance of a strategy can provide valuable insight into its general risk
and return properties. Furthermore, historical analysis allows one to compare variations of a strategy and examine
the impact of various parameter choices and implementation rules. Dynamic strategy applications in three areas
are considered, namely derivatives, asset allocation and equity factor portfolios. Firstly, the analysis of a strategy
involving single-stock derivatives is examined in which call options on certain constituents of an index portfolio
are sold as an alternative method of under-weighting the underlying. Secondly, the historical performance of an
optimization-based asset allocation strategy is considered. The assumed aim of the strategy is to outperform a
benchmark of CPI 5 via dynamic trading in a portfolio of domestic equities, bonds, property and cash, as well as
international equities and bonds. Finally, the effects of portfolio construction on factor performance are studied
via an historical analysis in which portfolios corresponding to a selection of fundamental factors are managed
according to a range of weighting schemes, rebalance frequencies and portfolio sizes.


Shen, J., Li, D., Qiu, G., Jeet, V., Teng, M. (, and Wong, K. C. (2021).“Asset Allocation and Private Market
Investing.” In: _The Journal of Portfolio Management_ 47(4), pp. 71–82.
Investors have been increasing their allocations to private assets, seeking higher returns and better portfolio
diversification. However, as this allocation increases, the liquidity characteristics of their portfolios change. The
authors create a framework that links bottom-up private asset investing with top-down asset allocation. Private
asset cash flows are consistently modeled together with public asset returns and risk that, in turn, drive portfolio
construction. This helps investors analyze how allocations to illiquid private assets, in combination with their
commitment strategy, may affect their portfolio’s ability to respond to various liquidity demands. By measuring
the potential trade-off among asset allocations, total portfolio performance, and the frequency of certain liquidity
events with different severities, this framework can help investors quantify the interaction between their portfolio
structure and performance and formalize their decision making around portfolio liquidity choices.
Sokolov, A., Mostovoy, J., Parker, B., and Seco, L. (2020).“Neural Embeddings of Financial Time-Series Data.” In:
_The Journal of Financial Data Science_ 2(4), pp. 33–43.
The dominant approaches for financial portfolio construction rely on estimating sample covariance and corre-
lations matrixes, which serve as an input into a number of classical portfolio construction techniques. These
classical approaches are not forward looking, are constrained by the ability to estimate covariance and correla-
tion matrixes, and are inflexible to incorporating additional information. The authors propose a new approach of
using learned representations from deep learning networks to augment such classical techniques. This approach
can incorporate learned estimates of future performance and can be customized to create tailored representations
best suited to meeting varying financial objectives. This article showcases one example of such an embedding,
compares and contrasts it with classical approaches to portfolio construction, and discusses additional possibil-
ities for applying representation learning in quantitative finance.
Staines, J., Li, W. V., and Romahi, Y. (2016).“Dimensions of Diversification.” In: _The Journal of Index Investing_
7(2), pp. 119–127.
Within the investment industry, diversification now refers to not only the division of capital among a large number
of securities but also the avoidance of risk concentration in any of a number of dimensions. Market-capitalization-
weighted indexes often fail this requirement. The authors thus argue that although capitalization weighting
makes a suitable benchmark, smart beta can provide a way to build indexes more suitable for investment. The
authors present a methodology to measure and hence maximize diversification simultaneously across multiple
dimensions. They show the practical value of this measure by using it to backtest equity portfolios. This provides
an example of how the properties of assets, rather than historical returns, can be used to systematically construct
well-diversified portfolios.
Suhonen, A., Lennkh, M., and Perez, F. (2017).“Quantifying Backtest Overfitting in Alternative Beta Strategies.”
In: _The Journal of Portfolio Management_ 43 (2), pp. 90–104.
The authors investigate the biases in the backtested performance of ”alternative beta”strategies using a unique
sample of 215 trading strategies developed and promoted by global investment banks. Their results lend support
to the cautions in the recent literature regarding backtest overfitting and lack of robustness in trading strategy
performance during the ”live”period (out of sample). The authors report a median 73 percent deterioration
in Sharpe ratios between backtested and live performance periods for the strategies, and they establish a link
between performance deterioration and strategy complexity, with the realized reduction in live versus back-
tested Sharpe ratios of the most complex strategies exceeding those of the simplest ones by over 30 percentage
points. The robustness of strategy exposure to risk factors varies between asset classes and strategies; it appears
reasonable in equity volatility and FX carry strategies but quite weak in the equity value strategy in particular.
Swedroe, L. (2020).“The Importance of Diversification in Achieving Long-Term Goals.” In: _Advisor Perspectives_.
My 2007 book, Wise Investing Made Simple: Larry Swedroe’s Tales to Enrich Your Future, contained 27 tales
to educate investors about important investment concepts and strategies. This article is in the spirit of those
tales. The examples are hypothetical.
Taljaard, B. H. and Maré, E. (2021).“Why has the equal weight portfolio underperformed and what can we do
about it?” In: _Quantitative Finance_ 21(11), pp. 1855–1868.
It is widely noted that market capitalisation weighted portfolios are inefficient and underperform an equal
weighted portfolio over the long-term. However, at least since 2016, an equal weighted portfolio of stocks in
the S&P500 has significantly underperformed the market capitalisation weighted portfolio. In this paper, we
analyse this underperformance using stochastic portfolio theory. We show that the equal weighted portfolio
does appear to outperform the market capitalisation weighted portfolio over the long-term but with periods of


significant short-term underperformance. In addition, we find that concentration in the market capitalisation
weighted portfolio has increased in recent years and has contributed to the recent underperformance together
with a significantly lower level of diversification benefits. Furthermore, we highlight an approach to improve the
performance of a portfolio by dynamically selecting a market cap or an equal weighting using a rudimentary
linear regression model.
Tayali, S. T. (2020).“A novel backtesting methodology for clustering in mean–variance portfolio optimization.” In:
_Knowledge-Based Systems_ 209, p. 106454.
The decisions of asset selection and allocation lie at the heart of financial portfolio management. For these
challenging tasks, the mathematical programming model of the mean-variance optimization problem proposes
to use the concept of diversification. The novel methodology in this article is a representation of the accumulated
knowledge of this model from the modern portfolio theory. It is a practical application for portfolio managers
to help synthesize the available historical data and to infer rational decisions. The state-of-the-art backtesting
methodology integrates the unsupervised machine learning method of clustering analysis into the mean-variance
portfolio optimization model. The test results from the proposed novel methodology show that clustering with
Euclidean distance measures outperform the results of the benchmark and other specified clustering methods
for different datasets, backtesting periods, and temporal scales of major stock indices.
Thiagarajan, R., Han, J., Hurd, A., Im, H., and Mallik, G. (2021).“Financial Globalization and Its Implications
for Diversification of Portfolio Risk.” In: _The Journal of Investing_ 30(6), pp. 22–33.
Trade disputes and the impact of the COVID-19 pandemic on global supply chains have drawn much attention
to the notion of ”deglobalization.” The common concern is that the steady trend of globalization and its many
benefits may reverse. But the globalization trend is not a monolith. In this article, we show that although
trade globalization has stalled since the Global Financial Crisis (GFC), financial globalization has continued to
increase. We further show that financial globalization has a much more significant impact on portfolios than
trade globalization. The primary mechanism of this impact, US dollar hegemony, impacts portfolios primarily
through increased spillover of US monetary policy shocks. The two implications for investors are: (1) global
equity markets have become increasingly correlated and are likely to stay that way, and (2) this increased
correlation reduces the benefits of portfolio diversification and leads to a more concentrated exposure to US
monetary policy shocks.
Thos, A.-K. (2020).“Naive Diversification with Fewer Assets - A Risk Reduction Approach Using Clustering
Methods.” PhD thesis. Technical University of Kaiserslautern.
Diversification is one of the main pillars of investment strategies. The prominent 1/N portfolio, which puts equal
weight on each asset is, apart from its simplicity, a method which is hard to outperform in realistic settings, as
many studies have shown. However, depending on the number of considered assets, this method can lead to very
large portfolios. On the other hand, optimization methods like the mean-variance portfolio suffer from estimation
errors, which often destroy the theoretical benefits. We investigate the performance of the equal weight portfolio
when using fewer assets. For this we explore different naive portfolios, from selecting the best Sharpe ratio
assets to exploiting knowledge about correlation structures using clustering methods. The clustering techniques
separate the possible assets into non-overlapping clusters and the assets within a cluster are ordered by their
Sharpe ratio. Then the best asset of each portfolio is chosen to be a member of the new portfolio with equal
weights, the cluster portfolio. We show that this portfolio inherits the advantages of the 1/N portfolio and can
even outperform it empirically. For this we use real data and several simulation models. We prove these findings
from a statistical point of view using the framework by DeMiguel, Garlappi and Uppal (2009). Moreover, we
show the superiority regarding the Sharpe ratio in a setting, where in each cluster the assets are comonotonic. In
addition, we recommend the consideration of a diversification-risk ratio to evaluate the performance of different
portfolios.
Traccucci, P., Dumontier, L., Garchery, G., and Jacot, B. (2019).“A Triptych Approach for Reverse Stress Testing
of Complex Portfolios.” In: _Risk (Cutting Edge)_.
Pascal Traccucci, Luc Dumontier, Guillaume Garchery and Benjamin Jacot present an extended reverse stress
test (ERST) triptych approach with three variables: level of plausibility, level of loss and scenario. Any two of
these variables can be derived, provided the third is given as input. A new version of the Levenberg-Marquardt
optimisation algorithm is introduced to derive the ERST in certain complex cases.
Valentine, K. D., Buchanan, E. M., Scofield, J. E., and Beauchamp, M. T. (2019).“Beyond p values: utilizing
multiple methods to evaluate evidence.” In: _Behaviormetrika_ 46(1), pp. 121–144.


Null hypothesis significance testing is cited as a threat to validity and reproducibility. While many individuals
suggest that we focus on altering the p value at which we deem an effect significant, we believe this suggestion
is short-sighted. Alternative procedures (i.e., Bayesian analyses and observation-oriented modeling: OOM) can
be more powerful and meaningful to our discipline. However, these methodologies are less frequently utilized
and are rarely discussed in combination with NHST. Herein, we discuss three methodologies (NHST, Bayesian
Model comparison, and OOM), then compare the possible interpretations of three analyses (ANOVA, Bayes
Factor, and an Ordinal Pattern Analysis) in various data environments using a frequentist simulation study.
We found that changing significance thresholds had little effect on conclusions. Furthermore, we suggest that
evaluating multiple estimates as evidence of an effect allows for more robust and nuanced interpretations of
results and implies the need to redefine evidentiary value and reporting practices. Recent events in psychological
science have prompted concerns within the discipline regarding research practices and ultimately, the validity and
reproducibility of published reports (Etz and Vandekerckhove 2016; Lindsay 2015, Open Science Collaboration
2015; van Elk et al. 2015). One often discussed matter is over-reliance, abuse, and potential hacking of p values
produced by frequentist null hypothesis significance testing (NHST), as well as misinterpretations of NHST
results (Gigerenzer 2004; Ioannidis 2005; Simmons et al. 2011). We agree with these concerns and believe that
many before us have voiced sound, generally accepted opinions on potential remedies, such as an increased focus
on effect sizes (Cumming 2008; Lakens 2013; Maxwell et al. 2015; Nosek et al. 2012). However, other suggestions
have been met with less enthusiasm, including an article by Benjamin et al. (2018) advocating that researchers
should begin thinking only of p values less than .005 as ”statistically significant”, thus changing alpha levels
to control Type I error rates. Alternatively, Pericchi and Pereira (2016) promote the use of fluctuating alpha
levels as a function of sample size to assist with these errors. Trafimow et al. (2018) critiques this suggestion to
broadly lower the alpha level to .005 and suggested that findings should be weighted on the basis of evidence
accumulation from multiple studies. We argue that alpha should not be the sole focus of our attention, but
rather, we should wonder if a p value should be utilized at all, and, if so, what that p value can tell us
in relation with other indicators. While NHST and p values may have merit, researchers have a wealth of
other statistical tools available to them. We believe that improvements may be made to the sciences as a
whole when individuals become aware of these tools and how these methods may be used, either alone or in
combination, to strengthen understanding of data and conclusions. These sentiments have been shared by the
American Statistical Association who recently held a conference focusing on going beyond NHST, expanding
their previous stance on p values (Wasserstein and Lazar 2016). Therefore, the main goal of this project was
to show researchers how two alternative paradigms compare to NHST in terms of their methodological design,
statistical interpretations, and comparative robustness. Herein, we will discuss the following methodologies:
NHST, Bayes factor comparisons, and observation-oriented modeling. To compare their methodological designs,
we first provide historical backgrounds, procedural steps, and limitations for each paradigm. We then simulated
data using a three timepoint repeated measures design with a Likert-type scale as the outcome variable to be
able to compare the statistical interpretations and comparative robustness. By simulating possible data sets
and analyzing them with each of the three paradigms, we will be able to discuss the conclusions these three
methods reach given the same data and to compare how often these methodologies agree within different data
environments (i.e., given varying sample sizes and effect sizes). Beyond simply comparing methodologies, we also
sought to identify how changing the alpha criteria within the NHST framework may alter conclusions. Although
previous work has already compared Frequentist NHST to Bayesian approaches (Goodman 1999; Rouder et
al. 2012; Wetzels et al. 2011), this manuscript adds a novel contribution: observation-oriented modeling. By
introducing social scientists to observation-oriented modeling (OOM), a relatively new paradigm that is readily
interpretable, we will show both how useful this paradigm can be in these contexts, and how it compares to two
well-known methods. We hope that by discussing these methodologies in terms of a simple statistical analysis
researchers will be able to easily compare and contrast methodologies.
van der Miesen, S. (2021).“The Effect of ESG Screening on Investment Return, Risk and Diversification.” MA
thesis. Radboud University.
In the past decades, the interest in environmental, social, and corporate governance has grown immensely. An
increasing part of investors is interested in the ESG performance of a company before investing in it through
financial markets. Also, a great body of research has focused on the effects of ESG performance on financial
performance of the firm, and on the financial performance of investing in those highly rated ESG companies.
However, there still is a lack of consensus regarding the effects of investing in ESG companies on the return of
investment. This thesis forms portfolios based on positive- and negative ESG screening and tries to capture the


effects of those screening methods on risk, return and diversification. The findings indicate that both screening
methods have no effect on the risk-adjusted return of a European portfolio for a retail investor. In line with prior
research this thesis finds lower volatility of ESG screened portfolios, compared to the market portfolio. However,
the idiosyncratic risk of the individual stocks in the portfolio is higher for the ESG screened portfolios, which is
not as expected. Finally, ESG screening has a significant, but small, effect on the diversification of the portfolio.
Overall, portfolios of retail investors in Europe, when well diversified, do not suffer from ESG screening.
Vandenbroucke, J. (2019).“Adaptive Portfolios and the Power of Diversification.” In: _The Journal of Investing_
28(5), pp. 29–37.
The article gives a qualitative description of an advisory or discretionary investment process that manages
the emotional aspect of investing. Portfolios are adaptive, meaning they automatically adjust their allocation in
response to changing market conditions. The adjustments are model-based and transparent, and align in terms of
frequency and magnitude with the investor’s emotionality. The process looks beyond the risk-focused paradigm in
relation to investor profiling, product positioning, and portfolio construction. First, investor profiles distinguish
between the attitude toward risk and the attitude toward loss. Second, products differentiate in terms of variance
and in terms of skewness. Finally, adaptive portfolios represent a client centric combination of products that
lifts the power of diversification to a higher level and ultimately contributes to long term buy-and-hold investor
behavior.
Vermorken, M. A., Medda, F. R., and Schroder, T. (2012).“The Diversification Delta: A Higher-MomentMeasure
for Portfolio Diversification.” In: _The Journal of Portfolio Management_ 39(1), pp. 67–74.
The concept of diversification is central in finance and has become even more so since the 2008 financial crisis. In
this article, the authors introduce a new measure for diversification. The measure, referred to as diversification
delta, is nonparametric, based on higher moments, easily interpretable due to its mathematical formulation,
and incorporates the advantages of the present measures of diversification while extending them. The mea-
sure is applied to infrastructure returns data in order to understand the benefits of diversifying across various
infrastructure classes, gaining useful insights for infrastructure fund managers and investors.
Vigen, T. (2019). _Spurious Correlations_ .url:https://www.tylervigen.com/spurious-correlations.
Military intelligence analyst and Harvard Law student Tyler Vigen illustrates the golden rule that ”correlation
does not equal causation” through hilarious graphs. Is there a correlation between Nic Cage films and swimming
pool accidents? What about beef consumption and people getting struck by lightning? Absolutely not. But that
hasn’t stopped millions of people from going to tylervigen.com and asking, ”Wait, what?” Vigen has designed
software that scours enormous data sets to find unlikely statistical correlations. He began pulling the funniest
ones for his website and has since gained millions of views, hundreds of thousands of likes, and tons of media
coverage. Subversive and clever, Spurious Correlations is geek humor at its finest, nailing our obsession with
data and conspiracy theory.
Vincent, K., Hsu, Y.-C., and Lin, H.-W. (2018).“Analyzing the Performance of Multifactor Investment Strategies
under a Multiple Testing Framework.” In: _The Journal of Portfolio Management_ 44(4), pp. 113–126.
Evaluating portfolios based on numerous combinations of factors using the individual backtesting method could
suffer from serious data mining bias and lead to spurious significant findings. Accordingly, the authors employ
a multiple hypothesis testing method to examine the multifactor portfolio performance. Their empirical results
show that even after they adjust for the multiple comparisons bias, stock-picking strategies with certain combined
firm characteristics could generate significantly better liquidity risk-adjusted returns. In addition, the outper-
forming multifactor strategies that the authors report are robust to alternative definitions of factors. However,
they observe that the number of significantly profitable multifactor portfolios has decreased substantially in the
era of increased liquidity and trading activity in the U.S. stock market.
Vovk, V. and Wang, R. (2020).“True and false discoveries with e-values.” In: _arXiv e-Print_.
The topic of this paper is multiple hypothesis testing based on e-values, which are Bayes factors stripped of
their Bayesian content. Using e-values instead of p-values, which are standard in this area, leads to simple and
efficient procedures that control the number of false discoveries under arbitrary dependence of the base e-values.
We prove an optimality result for our main procedure and demonstrate advantages of our methods over standard
methods using simulated and real-world datasets.
Vovk, V. and Wang, R. (2021).“E-values: Calibration, combination, and applications.” In: _Annals of Statistics_
49(3), pp. 1736–1753.
Multiple testing of a single hypothesis and testing multiple hypotheses are usually done in terms of p-values.
In this paper we replace p-values with their natural competitor, e-values, which are closely related to betting,


Bayes factors, and likelihood ratios. We demonstrate that e-values are often mathematically more tractable; in
particular, in multiple testing of a single hypothesis, e-values can be merged simply by averaging them. This
allows us to develop efficient procedures using e-values for testing multiple hypotheses.
Wang, H., Pappada, R., Durante, F., and Foscolo, E. (2017).“A Portfolio Diversification Strategy via Tail De-
pendence Clustering.” In: _Soft Methods for Data Science_. Ed. by M. B. Ferraro, P. Giordani, B. Vantaggi, M.
Gagolewski, M. Angeles Gil, P. Grzegorzewski, and O. Hryniewicz. Vol. 456. Advances in Intelligent Systems
and Computing. Springer International Publishing, pp. 511–518.
We provide a two-stage portfolio selection procedure in order to increase the diversification benefits in a bear
market. By exploiting tail dependence-based risky measures, a cluster analysis is carried out for discerning
between assets with the same performance in risky scenarios. Then, the portfolio composition is determined by
fixing a number of assets and by selecting only one item from each cluster. Empirical calculations on the EURO
STOXX 50 prove that investing on selected assets in trouble periods may improve the performance of risk-averse
investors.
Wiecki, T., Campbell, A., Lent, J., and Stauth, J. (2016).“All That Glitters Is Not Gold: Comparing Backtest
and Out-of-Sample Performance on a Large Cohort of Trading Algorithms.” In: _The Journal of Investing_ 25(3),
pp. 69–80.
When automated trading strategies are developed and evaluated using backtests on historical pricing data, there
exists a tendency to overfit to the past. Using a unique dataset of 888 algorithmic trading strategies developed
and backtested on the Quantopian platform, with at least six months of out-of-sample performance, this ar-
ticle studies the prevalence and impact of backtest overfitting. Specifically, the authors find that commonly
reported backtest evaluation metrics, such as the Sharpe ratio, offer little value in predicting out-of-sample
performance (R2 < 0.025). In contrast, higher-order moments, such as volatility and maximum drawdown, as
well as portfolio construction features (e.g., hedging), show significant predictive value of relevance to quanti-
tative finance practitioners. Moreover, in line with prior theoretical considerations, the authors find empirical
evidence of overfitting-the more backtesting a quant has done for a strategy, the larger the discrepancy be-
tween backtest and out-of-sample performance. Finally, they show that by training nonlinear, machine-learning
classifiers on a variety of features that describe backtest behavior, out-of-sample performance can be predicted
with much greater accuracy (R2 = 0.17) on hold-out data than when using linear, univariate features. A port-
folio constructed by using predictions on hold-out data performed significantly better out-of-sample than one
constructed from algorithms with the highest backtest Sharpe ratios.
Yang, X. and Kazemi, H. B. (2020).“Holdings concentration and hedge fund investment strategies.” In: _The Journal
of Alternative Investments_ 22(4), pp. 92–106.
This article examines the risk-return performance of concentrated positions of hedge funds in large-cap and
small-cap stocks. The research shows that small-cap stocks in which hedge funds have concentrated positions
earn higher future returns than those that are not part of hedge funds concentrated holdings. Also, stocks that
are part of the concentrated positions of hedge funds display higher downside risks and relatively large downside
returns during periods of market turmoil. The results presented indicate that hedge fund managers are skilled in
making equity investments under different degrees of market efficiency. The authors findings have two practical
implications: (1) hedge funds that hold concentrated positions in small-cap stocks may outperform their peers
and (2) investors may be able to improve the performance of their equity portfolios by monitoring hedge funds
positions in small-cap stocks.
Yu, L. (2021).“Comparing Classical Portfolio Optimization and Robust Portfolio Optimization on Black Swan
Events.” MA thesis. University of Waterloo.
Black swan events, such as natural catastrophes and manmade market crashes, historically have a drastic negative
influence on investments; and there is a discrepancy on losses caused by these two types of disasters. In general,
there is a recovery and it is of interest to understand what type of investment strategies lead to better performance
for investors. In this thesis we study classical portfolio optimization, robust portfolio optimization and some
historical black swan events. We compare two main strategies: mean variance optimization vs robust portfolio
optimization on two types of black swan events: natural vs anthropogenic. The comparison illustrates that
robust portfolio optimization is much more conservative, and has a shorter recovery time than classical portfolio
optimization. Moreover, the losses in the stock investment resulted from a natural disaster are very minor
compared to the losses resulted from an anthropogenic market crash.
Yuan, M. and Zhou, G. (2022).“Why Naive 1/N Diversification Is Not So Naive, and How to Beat It?” In: _SSRN
e-Print_.


In this paper, we study portfolio choice problem under estimation risk and show why the 1/N rule is very difficult
to beat in applications and studies. First, as long as the dimensionality is high relative to sample size, we show
that the usual estimated investment strategies are biased even asymptotically. Second, we show that the 1/N
rule is optimal in a one-factor model with diversifiable risks as dimensionality increases, irrespectively of the
sample size, making investment theory-based rules inadequate as they suffer from estimation errors. Third, we
provide strategies that can outperform the 1/N under suitable conditions.
Zaimovic, A., Omanovic, A., and Arnaut-Berilo, A. (2021).“How Many Stocks Are Sufficient for Equity Portfolio
Diversification? A Review of the Literature.” In: _Journal of Risk and Financial Management_ 14(11), p. 551.
Using extensive and comprehensive databases to select a subset of research papers, we aim to critically analyze
previous empirical studies to identify certain patterns in determining the optimal number of stocks in well-
diversified portfolios in different markets, and to compare how the optimal number of stocks has changed over
different periods and how it has been affected by market turmoil such as the Global Financial Crisis (GFC) and
the current COVID-19 pandemic. The main methods used are bibliometric analysis and systematic literature
review. Evaluating the number of assets which lead to optimal diversification is not an easy task as it is impacted
by a huge number of different factors: the way systematic risk is measured, the investment universe (size, asset
classes and features of the asset classes), the investor’s characteristics, the change over time of the asset features,
the model adopted to measure diversification (i.e., equally weighted versus optimal allocation), the frequency
of the data that is being used, together with the time horizon, conditions in the market that the study refers
to, etc. Our paper provides additional support for the fact that (1) a generalized optimal number of stocks that
constitute a well-diversified portfolio does not exist for whichever market, period or investor. Recent studies
further suggest that (2) the size of a well-diversified portfolio is larger today than in the past, (3) this number
is lower in emerging markets compared to developed financial markets, (4) the higher the stock correlations
with the market, the lower the number of stocks required for a well-diversified portfolio for individual investors,
and (5) machine learning methods could potentially improve the investment decision process. Our results could
be helpful to private and institutional investors in constructing and managing their portfolios and provide a
framework for future research.
Zaker, S. (2022).“The invisible free lunch.” In: _SSRN e-Print_.
In the world of investing, diversification is usually regarded as the only true free lunch. Market efficiency, an
even more crucial free lunch, is taken for granted. Market efficiency is foundational in wealth management. It is
not just the axiom and corner stone of Modern Portfolio Theory.
Zhang, C., Li, Y., Chen, X., Jin, Y., Tang, P., and Li, J. (2020a).“DoubleEnsemble: A New Ensemble Method Based
on Sample Reweighting and Feature Selection for Financial Data Analysis.” In: _IEEE International Conference
on Data Mining (ICDM)_. IEEE.
Modern machine learning models (such as deep neural networks and boosting decision tree models) have become
increasingly popular in financial market prediction, due to their superior capacity to extract complex non-linear
patterns. However, since financial datasets have very low signal-to-noise ratio and are non-stationary, complex
models are often very prone to overfitting and suffer from instability issues. Moreover, as various machine
learning and data mining tools become more widely used in quantitative trading, many trading firms have been
producing an increasing number of features (aka factors). Therefore, how to automatically select effective features
becomes an imminent problem. To address these issues, we propose DoubleEnsemble, an ensemble framework
leveraging learning trajectory based sample reweighting and shuffling based feature selection. Specifically, we
identify the key samples based on the training dynamics on each sample and elicit key features based on
the ablation impact of each feature via shuffling. Our model is applicable to a wide range of base models,
capable of extracting complex patterns, while mitigating the overfitting and instability issues for financial market
prediction. We conduct extensive experiments, including price prediction for cryptocurrencies and stock trading,
using both DNN and gradient boosting decision tree as base models. Our experiment results demonstrate that
DoubleEnsemble achieves a superior performance compared with several baseline methods.
Zhang, F., Guo, R., and Cao, H. (2020b).“Information Coefficient as a Performance Measure of Stock Selection
Models.” In: _arXiv e-Print_.
Information coefficient (IC) is a widely used metric for measuring investment managers’ skills in selecting stocks.
However, its adequacy and effectiveness for evaluating stock selection models has not been clearly understood,
as IC from a realistic stock selection model can hardly be materially different from zero and is often accompanies
with high volatility. In this paper, we investigate the behavior of IC as a performance measure of stick selection
models. Through simulation and simple statistical modeling, we examine the IC behavior both statically and


dynamically. The examination helps us propose two practical procedures that one may use for IC-based ongoing
performance monitoring of stock selection models.
Zhang, Z., Zohren, S., and Roberts, S. (2020c).“Deep Learning for Portfolio Optimization.” In: _The Journal of
Financial Data Science_ 22(4), pp. 8–20.
In this article, the authors adopt deep learning models to directly optimize the portfolio Sharpe ratio. The
framework they present circumvents the requirements for forecasting expected returns and allows them to
directly optimize portfolio weights by updating model parameters. Instead of selecting individual assets, they
trade exchange-traded funds of market indexes to form a portfolio. Indexes of different asset classes show robust
correlations, and trading them substantially reduces the spectrum of available assets from which to choose. The
authors compare their method with a wide range of algorithms, with results showing that the model obtains the
best performance over the testing period of 2011 to the end of April 2020, including the financial instabilities
of the first quarter of 2020. A sensitivity analysis is included to clarify the relevance of input features, and the
authors further study the performance of their approach under different cost rates and different risk levels via
volatility scaling.
Zhao, Z., Xu, F., Du, D., and Meihua, W. (2021).“Robust portfolio rebalancing with cardinality and diversification
constraints.” In: _Quantitative Finance_ 21(10), pp. 1707–1721.
In this paper, we develop a robust conditional value at risk (CVaR) optimal portfolio rebalancing model un-
der various financial constraints to construct sparse and diversified rebalancing portfolios. Our model includes
transaction costs and double cardinality constraints in order to capture the trade-off between the limit of in-
vestment scale and the diversified industry coverage requirement. We first derive a closed-form solution for the
robust CVaR portfolio rebalancing model with only transaction costs. This allows us to conduct an industry
risk analysis for sparse portfolio rebalancing in the absence of diversification constraints. Then, we attempt to
remedy the hidden industry risk by establishing a new robust portfolio rebalancing model with both sparse and
diversified constraints. This is followed by the development of a distributed-version of the Alternating Direc-
tion Method of Multipliers (ADMM) algorithm, where each subproblem admits a closed-form solution. Finally,
we conduct empirical tests to compare our proposed strategy with the standard sparse rebalancing and no-
rebalancing strategies. The computational results demonstrate that our rebalancing approach produces sparse
and diversified portfolios with better industry coverage. Additionally, to measure out-of-sample performance,
two superiority indices are created based on worst-case CVaR and annualized return, respectively. Our ADMM
strategy outperforms the sparse rebalancing and no-rebalancing strategies in terms of these indices.


