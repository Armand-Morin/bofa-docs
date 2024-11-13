ESG, impact and climate\-based investing in quantitative wealth and
investment management QWIM
Cristian Homescu
December 2022
Abstract
This document provides details for this QWIM project, and it incorporates the following sections
•Motivation
•Relevant references
•Suggested project tasks and timelines
•Practical info
Recommended software tools
Recommended datasets
•Design and implementation for the project codes
•Potentially useful Python and R packages, codes and frameworks
•Appendices
Appendices include
•Overviews of investment processes and models in QWIM
•Comparison of investment portfolios using portfolios metrics and benchmark portfolios
Contents
1 Motivation for the project 4
1\.1 ESG\-based portfolio construction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
1\.2 ESG ratings and scores . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
1\.3 Climate\-based investing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
1\.4 Portfolio diversification and tail risk protection through ESG investing . . . . . . . . . . . . . . . . . 4
1\.5 Practical challenges with ESG investing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
2 Relevant references 6
2\.1 Main references . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
2\.2 Comprehensive set of references . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
2\.2\.1 ESG investing and risk . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
2\.2\.2 ESG\-based portfolio construction and investment strategies . . . . . . . . . . . . . . . . . . . 11
2\.2\.3 Portfolio diversification and tail risk protection through ESG investing . . . . . . . . . . . . . 12
2\.2\.4 ESG ratings and scores . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13
2\.2\.5 Impact Investing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
2\.2\.6 Climate based investing and risk . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
2\.2\.7 Metrics, performance and benchmarks for ESG\-based investing . . . . . . . . . . . . . . . . . 16
2\.2\.8 NLP, text, topic and sentiment analysis within context of ESG investing . . . . . . . . . . . . 17
2\.2\.9 Testing and comparison procedures for investment portfolios . . . . . . . . . . . . . . . . . . 17
13 Practical details for the project 20
3\.1 Interaction with students . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
3\.2 Data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
3\.3 Private GitHub repository for the QWIM project . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
3\.4 Deliverables . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
3\.5 (Optional) Article submission to leading journals . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
4 Project tasks and timelines 22
4\.1 Suggested timelines for project tasks . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22
4\.2 Literature review . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22
4\.3 Write\-up summary of literature review . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
4\.4 Identification of appropriate Python and/or R packages . . . . . . . . . . . . . . . . . . . . . . . . . 23
4\.5 Code design . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
4\.6 Implementation of coding framework and components . . . . . . . . . . . . . . . . . . . . . . . . . . 24
4\.7 Interactive visualizer . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24
4\.8 Project report and presentation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24
5 Design and implementation for the project codes 25
5\.1 Visualize project workflow and coding framework . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25
5\.2 Representative examples of Python libraries with well designed folder structure . . . . . . . . . . . . 29
6 Practical Info 30
6\.1 Recommended software tools . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30
6\.1\.1 Python . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30
6\.1\.2 R . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30
6\.1\.3 R IDE . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30
6\.1\.4 Python IDE . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30
6\.1\.5 Bibliography Manager . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30
6\.1\.6 Document processor . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31
6\.1\.7 Source control manager . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31
6\.1\.8 File editor . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31
6\.1\.9 Runtime libraries . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31
6\.2 Recommended datasets . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31
7 Potentially useful Python and R software implementations: packages, codes and frameworks 34
7\.1 Collections and repositories of resources . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34
7\.2 Connection between Python and R codes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34
7\.3 Anomaly detection and data outliers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35
7\.4 Bayesian analysis and modeling . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 36
7\.5 Causality, inference and dependencies . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 38
7\.6 Classification, Motifs, Neighbors, Wavelets, Transforms . . . . . . . . . . . . . . . . . . . . . . . . . . 39
7\.7 Clustering . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 41
7\.8 Coding utilities and frameworks . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 44
7\.9 Computational performance . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 48
7\.10 Containers, projects, pipelines and deployment . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 49
7\.11 Covariances, correlations and volatilities . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 50
7\.12 Data analysis and exploration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 51
7\.13 Data augmentation, scenario generation and synthetic time series . . . . . . . . . . . . . . . . . . . . 53
7\.14 Data cleaning, preparation and validation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 55
7\.15 Data Imputation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 56
7\.16 Data regimes, states and changepoints: analysis and modeling . . . . . . . . . . . . . . . . . . . . . . 58
7\.17 Data structures, storage and serialization . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 60
7\.18 Dates and times . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 62
7\.19 Dimensionality reduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 63
7\.20 Distances and Similarity . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 64
27\.21 ESG and Impact Investing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 65
7\.22 Explainability, Interpretability, Fairness, Data Privacy . . . . . . . . . . . . . . . . . . . . . . . . . . 66
7\.23 Features for time series . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 67
7\.24 Filtering and spectral analysis for time series . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 68
7\.25 Forecasting time series . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 69
7\.26 Graphs and graphical modeling . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 74
7\.27 Linear algebra . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 74
7\.28 Machine Learning . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 75
7\.29 Machine Learning frameworks (includes Automated ML and hyperparameters tuning) . . . . . . . . 79
7\.30 Network and graph analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 80
7\.31 Numerical methods (includes numerical optimization) . . . . . . . . . . . . . . . . . . . . . . . . . . 82
7\.32 Probabilistic modeling (includes mixture models and Gaussian Processes) . . . . . . . . . . . . . . . 84
7\.33 Reinforcement learning . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 87
7\.34 Robust numerical methods . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 89
7\.35 Selection of features, variables, models, data splits . . . . . . . . . . . . . . . . . . . . . . . . . . . . 90
7\.36 Sensitivity analysis and numerical derivatives . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 93
7\.37 Statistics and Probability . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 93
7\.38 Stress testing, rare events, extreme values and scenarios, survival analysis . . . . . . . . . . . . . . . 95
7\.39 Symbolic regression \& data\-driven model discovery and machine learning . . . . . . . . . . . . . . . 96
7\.40 Testing (numerical, statistical, etc.), comparison and ranking . . . . . . . . . . . . . . . . . . . . . . 97
7\.41 Testing software codes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 101
7\.42 Time series analysis and modeling . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 102
7\.43 Text, sentiment and topic analytics (including NLP) . . . . . . . . . . . . . . . . . . . . . . . . . . . 105
7\.44 Uncertainty: analysis and modeling . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 107
7\.45 Visualization and reporting . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 108
8 Codes for QWIM (Quantitative Wealth and Investment Management) 112
8\.1 Collections of resources . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 112
8\.2 Research studies with code . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 113
8\.3 Python software implementations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 114
8\.4 R software implementations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 116
References 118
Appendix A: Overviews of investment processes and models in QWIM 132
Appendix C: Comparison of investment using portfolios metrics and benchmark portfolios 133
31 Motivation for the project
Investors throughout the world are increasingly interested in environmental, social, and governance (ESG) investing.
The 2021 Global Sustainable Investment Report indicated a significant increase for sustainable and responsible
investments, bringing the total to USD 35\.3 trillion.
Many investors have social or ethical reasons for ESG investing, and academic and practitioner surveys indicate
that majority of surveyed investment professionals believe that incorporating ESG information into an investment
evaluation process is relevant to investment performance.
1\.1 ESG\-based portfolio construction
ESG identifies factors that reflect environmental considerations (E), societal preferences (S), and governance of the
firm (G) and may complement, or compete with, classical portfolio construction methods. It is complementary if
the ESG factors enhance alpha. It is competitive if the factors detract from alpha.
1\.2 ESG ratings and scores
Billio et al. (“Inside the ESG Ratings: (Dis)agreement and Performance,” 2021\) : Analysis the ESG rating criteria
used by prominent agencies indicate a lack of a commonality in the definition of ESG (i) characteristics, (ii)
attributes and (iii) standards in defining E, S and G components. Such heterogeneity in rating criteria can lead
agencies to have opposite opinions on the same evaluated companies and that agreement across those providers was
found to be substantially low in many cases.
1\.3 Climate\-based investing
Climate risk is denitively back on the agenda of investors and goes beyond ESG ratings. However, climate risk
assessment methodologies have not reached maturity. Nevertheless, the development of climate risk measures and
their sophistication have an increasing impact on portfolio construction and management. While first developed on
the side of passive management and low\-carbon equity indices, these approaches are now gaining a lot of traction
in active management.
1\.4 Portfolio diversification and tail risk protection through ESG investing
Diversification is one of the most important concepts in the financial world. It is often said that diversification
is the only free lunch in finance. From a qualitative point of view, the concept of diversification is quite clear: a
portfolio is well\-diversified if shocks in the individual components do not heavily impact on the overall portfolio.
Relatively simple to understand then but profoundly difficult to define. Indeed, there is no broadly accepted precise
and quantitative definition of diversification.
One of the most vexing problems in investment management is that diversification seems to disappear when
investors need it the most. A key challenge in the construction of diversified multi\-asset portfolio strategies is that
even a seemingly well\-balanced allocation to many asset classes can eventually translate into a portfolio with a very
concentrated set of underlying risk exposures.
Incorporating ESG into portfolios may also improve their diversification behavior.
1\.5 Practical challenges with ESG investing
Practical challenges include
•inconsistent ESG metrics and ratings
•particularly noisy data
•entanglement of ESG factors with standard risk factors
4The lack of standardized ESG metrics creates opportunities for greenwashing by companies less interested in pur\-
suing legitimate ESG objectives, than in building brand by meeting minimum criteria for metrics that may be
somewhat easy to game.
ESG data typically are deficient in the following areas:
•Quantity: Not enough data are available.
•Consistency: Companies often report different ESG data items.
•Quality: Methodologies used to derive or compute the reported ESG data mayvary across companies.
52 Relevant references
2\.1 Main references
List of references:
Alessandrini and Jondeau (“Optimal Strategies for ESG Portfolios,” 2021\)
Alessandrini et al. (“ESG Screening in the Fixed\-Income Universe,” 2021\)
Alford (“Some considerations for investors exploring ESG strategies,” 2019\)
Amon et al. (“Passive ESG Portfolio Management – The Benchmark Strategy for Socially Responsible Investors,”
2021\)
Antoncic et al. (“Sustainable Investment \- Exploring the Linkage between Alpha, ESG, and SDG’s,” 2020\)
Apostolou and Papaioannou (“Integration of Environmental Factors into Portfolio Risk Assessment,” 2021\)
Ascioglu et al. (“Integration of ESG Metrics into a Student\-Managed Fund:Creating Sustainable Student\-
Managed Funds,” 2017\)
Avramov et al. (“Investment and Asset Pricing with ESG Disagreement,” 2021\)
Bauer et al. (“Get Real! Individuals Prefer More Sustainable Investments,” 2021\)
Baz et al. (“Climate Regulatory Exposure: Evidence from Stock Returns,” 2021\)
Becker et al. (“Fostering the Power of ESG Transparency: The Effect of Sustainability Labels on Mutual Funds
and Individual Investors,” 2021\)
Benedetti et al. (“Climate change investment risk: optimal portfolio construction ahead of the transition to a
lower\-carbon economy,” 2021\)
Berg et al. (“ESG Confusion and Stock Returns: Tackling the Problem of Noise,” 2021\)
Billio et al. (“Inside the ESG Ratings: (Dis)agreement and Performance,” 2021\)
Bingler et al. (“Cheap Talk and Cherry\-Picking: What ClimateBert has to say on Corporate Climate Risk
Disclosures,” 2021\)
Bohn et al. (“Sustainable Investing From a Practitioner’s Viewpoint: What’s in Your ESG Portfolio?” 2022\)
Branch et al. (“A guide to ESG portfolio construction,” 2019\)
Breedt et al. (“Is ESG an Equity Factor or Just an Investment Guide?” 2019\)
Bruder et al. (“Integration of ESG in asset allocation,” 2019\)
Bruno et al. (“”Honey, I Shrunk the ESG Alpha”: Risk\-Adjusting ESG Portfolio Returns,” 2022\)
Cai et al. (“Socially Responsible Investing and Factor Investing, Is There an Opportunity Cost?” 2022\)
Cesarone et al. (“Does ESG impact really enhances portfolio profitability?” 2022\)
Chava et al. (“Doing Well by Doing Good? Risk, Return, and Environmental and Social Ratings,” 2021\)
Chen and Mussalli (“An integrated approach to quantitative ESG investing,” 2020\)
Coqueret (“Perspectives in ESG equity investing,” 2021\)
Coqueret et al. (“ESG Equity Investing: A Short Survey,” 2021\)
Coqueret et al. (“Boosting ESG\-Based Optimization With Asset Pricing Characteristics,” 2021\)
Coqueret ( Perspectives in sustainable equity investing (website version) , 2022\)
Cornell (“ESG Investing: Conceptual Issues,” 2020\)
Cosemans et al. (“Climate Change and Long\-Horizon Portfolio Choice: Combining Theory and Empirics,” 2021\)
De Franco et al. (“Sustainable Investing: ESG versus SDG,” 2021\)
De Spiegeleer et al. (“ESG: A New Dimension in Portfolio Allocation,” 2020\)
Dimson et al. (“Divergent ESG Ratings,” 2020\)
Dumitrescu et al. (“Defining Greenwashing,” 2022\)
Geczy and Guerard (“ESG and Expected Returns on Equities: The Case of Environmental Ratings,” 2021\)
Geczy et al. (“Investing in Socially Responsible Mutual Funds,” 2021\)
Gibson Brandon et al. (“ESG Rating Disagreement and Stock Returns,” 2021\)
Giese et al. (“Performance and Risk Analysis of Index\-Based ESG Portfolios,” 2019\)
Giese et al. (“Consistent ESG through ESG Benchmarks,” 2019\)
Giese et al. (“Deconstructing ESG Ratings Performance: Risk and Return for E, S, and G by Time Horizon,
Sector, and Weighting,” 2021\)
Giese et al. (“Foundations of Climate Investing: How Equity Markets Have Priced Climate\-Transition Risks,”
2021\)
Grim and Berkowitz (“ESG, SRI, and Impact Investing: A Primer for Decision\-Making,” 2020\)
6Hays and McCabe (“Sustainable and Impact Investing: A Taxonomy of Approaches and Considerations for
Fiduciaries,” 2021\)
Henriksson et al. (“Integrating ESG in portfolio construction,” 2019\)
Hubel and Scholz (“Integrating sustainability risks in asset management: the role of ESG exposures and ESG
ratings,” 2020\)
Jacobsen et al. (“The alpha, beta, and sigma of ESG: better beta, additional alpha?” 2019\)
Jacobsen et al. (“Climate Change and Asset Allocation: A Distinction That Makes a Difference,” 2021\)
Kaiser (“ESG integration: value, growth and momentum,” 2020\)
Kazdin et al. (“Climate Alpha with Predictors Also Improving Company Efficiency,” 2021\)
Kilmurray et al. (“Integrating Impact Funds into Mainstream Portfolios,” 2021\)
Krappel et al. (“Heterogeneous Ensemble for ESG Ratings Prediction,” 2021\)
Lanza et al. (“Mind the gap! Machine Learning, ESG Metrics and Sustainable Investment,” 2020\)
Lee et al. (“Combining E, S, and G Scores: An Exploration of Alternative Weighting Schemes,” 2020\)
Le Guenedal and Roncalli ( Portfolio Construction with Climate Risk Measures , 2022\)
Lepetit et al. ( The Recent Performance of ESG Investing, the COVID\-19 Catalyst and the Biden Effect , 2021\)
Lindeman (“ESG Score Design And Portfolio Construction,” 2022\)
Lioui and Tarelli (“Chasing The ESG Factor,” 2021\)
Lo and Zhang (“Quantifying the Impact of Impact Investing,” 2022\)
Macpherson et al. (“Artificial Intelligence and FinTech Technologies for ESG Data and Analysis,” 2021\)
Madhavan et al. (“Toward ESG Alpha: Analyzing ESG Exposures through a Factor Lens,” 2021\)
Margot et al. (“ESG Investments: Filtering versus Machine Learning Approaches,” 2021\)
Martin (“Impact Investing. A Practitioner Perspective,” 2021\)
Mercereau and Melin (“Optimizing Portfolios across Risk, Return, and Climate,” 2020\)
Naffa and Fain (“A factor approach to the performance of ESG leaders and laggards,” 2022\)
Ouchen (“Is the ESG portfolio less turbulent than a market benchmark portfolio?” 2021\)
Parker (“Achieving Goals While Making an Impact: Balancing Financial Goals with Impact Investing,” 2021\)
Pedersen et al. (“Responsible investing: The ESG\-efficient frontier,” 2021\)
Roncalli et al. (“Measuring and Managing Carbon Risk in Investment Portfolios,” 2020\)
Roncalli (“Advanced Course in Asset Management,” 2021\)
Roncalli (“Green and Sustainable Finance, ESG Investing and Climate Risk,” 2021\)
Rubbaniy et al. (“Are ESG Stocks Safe\-Haven during COVID\-19?” 2021\)
Sahin\-et\-al\-2021
Schmidt and Zhang (“Optimal ESG Portfolios: Which ESG Ratings to Use?” 2021\)
Simpson et al. (“The ESG Mirage,” 2021\)
Sokolov et al. (“Weak Supervision and Black\-Litterman for Automated ESG Portfolio Construction,” 2021\)
Sokolov et al. (“Building Machine Learning Systems for Automated ESG Scoring,” 2021\)
Sorensen et al. (“The Quantitative Approach for Sustainable Investing,” 2021\)
Stotz (“Expected and realized returns on stocks with high\- and low\-ESG exposure,” 2021\)
Tokat\-Acikel et al. (“Top\-Down Portfolio Implications of Climate Change,” 2021\)
Varmaz et al. (“Portfolio optimization for sustainable investments,” 2021\)
Venturini (“Climate change, risk factors and stock returns: A review of the literature,” 2022\)
Yeh et al. (“SustainBench: Benchmarks for Monitoring the Sustainable Development Goals with Machine Learn\-
ing,” 2021\)
Yoshino and Yuyama (“Studies of Applied Economics,” 2021\)
2\.2 Comprehensive set of references
2\.2\.1 ESG investing and risk
List of references:
Alessandrini and Jondeau (“ESG investing: from sin stocks to smart beta,” 2020\)
Alessandrini and Jondeau (“Optimal Strategies for ESG Portfolios,” 2021\)
Alessandrini et al. (“ESG Screening in the Fixed\-Income Universe,” 2021\)
Amon et al. (“Passive ESG Portfolio Management – The Benchmark Strategy for Socially Responsible Investors,”
2021\)
7Andersson et al. (“Portfolio Construction and New Energy Infrastructure Investing,” 2021\)
Antoncic et al. (“Sustainable Investment \- Exploring the Linkage between Alpha, ESG, and SDG’s,” 2020\)
Apostolou and Papaioannou (“Integration of Environmental Factors into Portfolio Risk Assessment,” 2021\)
Areal et al. (“The conditional performance of US mutual funds over different market regimes: do different types
of ethical screens matter?” 2013\)
Austmo and Eikeland (“Exploiting ESG Information by Extending Conventional Smart Beta Strategies: An
Empirical Analysis of Portfolio Performances through the Booms and Busts in the European Equity Market,”
2021\)
Avramov et al. (“Investment and Asset Pricing with ESG Disagreement,” 2021\)
Avramov et al. (“Dynamic ESG Equilibrium,” 2021\)
Aw et al. (“A Morality Tale of ESG: Assessing Socially Responsible Investing,” 2017\)
Azevedo et al. (“Investor sentiment and the time\-varying sustainability premium,” 2021\)
Baeza\-Sampere et al. (“A fuzzy data envelopment analysis model for evaluating the efficiency of socially respon\-
sible and conventional mutual funds,” 2016\)
Bag and Mohanty (“Impact of ESG Factors on Emerging Market Stock Returns,” 2021\)
Bahra and Thukral (“ESG in Global Corporate Bonds: The Analysis Behind the Hype,” 2020\)
Balcilar et al. (“Do Sustainable Stocks Offer Diversification Benefits for Conventional Portfolios? An Empirical
Analysis of Risk Spillovers and Dynamic Correlations,” 2017\)
Bauer et al. (“Get Real! Individuals Prefer More Sustainable Investments,” 2021\)
Bax et al. (“ESG, Risk, and (tail) dependence,” 2021\)
Becker et al. (“Fostering the Power of ESG Transparency: The Effect of Sustainability Labels on Mutual Funds
and Individual Investors,” 2021\)
Benedetti et al. (“Climate change investment risk: optimal portfolio construction ahead of the transition to a
lower\-carbon economy,” 2021\)
Bender et al. (“Thematic Indexing, Meet Smart Beta! Merging ESG into Factor Portfolios,” 2017\)
Bennani et al. (“How ESG investing has impacted the asset pricing in the equity market,” 2019\)
Ben Slimane et al. (“ESG Investing in Fixed Income: It’s Time to Cross the Rubicon,” 2020\)
Berg et al. (“ESG Confusion and Stock Returns: Tackling the Problem of Noise,” 2021\)
Blank et al. (“Best Practices in ESG Investing,” 2016\)
Bohn et al. (“Sustainable Investing From a Practitioner’s Viewpoint: What’s in Your ESG Portfolio?” 2022\)
Branch et al. (“A guide to ESG portfolio construction,” 2019\)
Breedt et al. (“Is ESG an Equity Factor or Just an Investment Guide?” 2019\)
Briere et al. (“Do Social Responsibility Screens Really Matter When Assessing Mutual Fund Performance?”
2017\)
Bruder et al. (“Integration of ESG in asset allocation,” 2019\)
Bruno et al. (“”Honey, I Shrunk the ESG Alpha”: Risk\-Adjusting ESG Portfolio Returns,” 2022\)
Bush et al. (“E, S, or G \- Analyzing Global ESG Performance,” 2020\)
Cai et al. (“Socially Responsible Investing and Factor Investing, Is There an Opportunity Cost?” 2022\)
Cao et al. (“Unlocking ESG Premium from Options,” 2021\)
Chan et al. (“ESG in Factors,” 2020\)
Chang et al. (“How Interpretable and Trustworthy are GAMs?” 2021\)
Chava et al. (“Doing Well by Doing Good? Risk, Return, and Environmental and Social Ratings,” 2021\)
Chen and Mussalli (“An integrated approach to quantitative ESG investing,” 2020\)
Chen et al. (“The Unreasonable Attractiveness of More ESG Data,” 2021\)
Chen et al. (“NLP for SDGs: Measuring Corporate Alignment with the Sustainable Development Goals,” 2022\)
Choi et al. (“Measuring the carbon exposure of institutional investors,” 2020\)
Chong and Phillips (“ESG Investing: A Simple Approach,” 2016\)
Climent et al. (“ESG Disclosure and Portfolio Performance,” 2021\)
Coqueret (“Perspectives in ESG equity investing,” 2021\)
Coqueret et al. (“Boosting ESG\-Based Optimization With Asset Pricing Characteristics,” 2021\)
Coqueret et al. (“ESG Equity Investing: A Short Survey,” 2021\)
Coqueret ( Perspectives in sustainable equity investing , 2022\)
Cornell (“ESG Investing: Conceptual Issues,” 2020\)
Cornell (“ESG preferences, risk and return,” 2021\)
8Cornell and Damodaran (“Valuing ESG: Doing Good or Sounding Good?” 2020\)
Dash and Kajiji (“Behavioral Portfolio Management with Layered ESG Goals and AI Estimation of Asset
Returns,” 2021\)
De and Clayman (“The Benefits of Socially Responsible Investing: An Active Manager’s Perspective,” 2015\)
De Franco et al. (“ESG investments: Filtering versus machine learning approaches,” 2020\)
De Franco et al. (“Sustainable Investing: ESG versus SDG,” 2021\)
De Spiegeleer et al. (“ESG: A New Dimension in Portfolio Allocation,” 2020\)
Dı́az et al. (“Reconsidering systematic factors during the Covid\-19 pandemic – The rising importance of ESG,”
2021\)
Drei et al. (“ESG Investing in Recent Years: New Insights from Old Challenges,” 2019\)
Dumitrescu et al. (“Defining Greenwashing,” 2022\)
Fish et al. (“The ESG Sacrifice,” 2019\)
Fridson et al. (“ESG Impact on High\-Yield Returns,” 2021\)
Gao et al. (“Styles through a convergent/divergent lens: the curious case of ESG,” 2020\)
Garefalakis and Dimitras (“Looking back and forging ahead: the weighting of ESG factors,” 2020\)
Geczy et al. (“Efficient SRI / ESG portfolios,” 2019\)
Gaussel and Le Saint (“ESG Risk Rating of Alternative Portfolios,” 2021\)
Geczy and Guerard (“ESG and Expected Returns on Equities: The Case of Environmental Ratings,” 2021\)
Geczy et al. (“Contracts with (Social) benefits: The implementation of impact investing,” 2021\)
Geczy et al. (“Investing in Socially Responsible Mutual Funds,” 2021\)
Gerard (“ESG and socially responsible investment: A critical review,” 2018\)
Gidwani (“Some Issues with Using ESG Ratings in an Investment Process,” 2020\)
Giese et al. (“ESG as a performance factor for smart beta indexes,” 2016\)
Giese et al. (“Performance and Risk Analysis of Index\-Based ESG Portfolios,” 2019\)
Giese et al. (“Consistent ESG through ESG Benchmarks,” 2019\)
Giese et al. (“Foundations of ESG investing: how ESG affects equity valuation, risk, and performance,” 2019\)
Gougler and Utz (“Factor exposures and diversification: Are sustainably screened portfolios any different?”
2020\)
Gregory (“Market Efficiency in ESG Indexes: Trading Opportunities,” 2021\)
Grim and Berkowitz (“ESG, SRI, and Impact Investing: A Primer for Decision\-Making,” 2020\)
Hanna (“The Impact of ESG\-Related Industry Exclusions in Minimum\-Volatility Portfolios,” 2020\)
Harper (“One Institutional Investor Approach to Integrating ESG in the Investment Process,” 2020\)
Hays and McCabe (“Sustainable and Impact Investing: A Taxonomy of Approaches and Considerations for
Fiduciaries,” 2021\)
Henriksson et al. (“Integrating ESG in portfolio construction,” 2019\)
Hsu et al. (“Outperformance through Investing in ESG in Need,” 2018\)
Hubel and Scholz (“Integrating sustainability risks in asset management: the role of ESG exposures and ESG
ratings,” 2020\)
Husse and Pippo (“Responsible Minus Irresponsible \- a determinant of equity risk premia?” 2022\)
Jacob and Wilkens (“What drives sustainable indices? A framework for analyzing the sustainable index land\-
scape,” 2021\)
Jacobsen et al. (“The alpha, beta, and sigma of ESG: better beta, additional alpha?” 2019\)
Jin (“Is ESG a systematic risk factor for US equity mutual funds?” 2018\)
Jin (“Systematic ESG Risk and Decision Criteria for Optimal Portfolio Selection,” 2021\)
Kaiser and Schaller (“Environmentally (Un\-)Friendly Portfolio Construction,” 2019\)
Kaiser (“ESG integration: value, growth and momentum,” 2020\)
Kanuri (“Risk and Return Characteristics of Environmental, Social, and Governance (ESG) Equity ETFs,”
2020\)
Khan (“Corporate Governance, ESG, and Stock Returns around the World,” 2019\)
Klement (“Does ESG matter for asset allocation?” 2018\)
Kumar (“ESG: Alpha or Duty?” 2019\)
Kumar and Khasnis (“Fallen Angels with ESG Wings,” 2020\)
Lanza et al. (“Mind the gap! Machine Learning, ESG Metrics and Sustainable Investment,” 2020\)
9Lee (“What Does ESG Investing Really Mean? Implications for Investors of Separating Financial Materiality
and Social Objectives,” 2021\)
Lepetit et al. ( The Recent Performance of ESG Investing, the COVID\-19 Catalyst and the Biden Effect , 2021\)
Li et al. (“Robust enhanced indexation with ESG: An empirical study in the Chinese Stock Market,” 2022\)
Lindeman (“ESG Score Design And Portfolio Construction,” 2022\)
Lindsey et al. (“The Cost of ESG Investing,” 2021\)
Lioui (“ESG Factor Investing: Myth or Reality ?” 2018\)
Lioui and Tarelli (“Chasing The ESG Factor,” 2021\)
Macpherson et al. (“Artificial Intelligence and FinTech Technologies for ESG Data and Analysis,” 2021\)
Madhavan et al. (“Toward ESG Alpha: Analyzing ESG Exposures through a Factor Lens,” 2021\)
Maiti (“Is ESG the succeeding risk factor?” 2021\)
Margot et al. (“ESG Investments: Filtering versus Machine Learning Approaches,” 2021\)
Matos (“ESG and Responsible Institutional Investing Around the World: A Critical Review,” 2020\)
Mendiratta et al. (“How ESG Affected Corporate Credit Risk and Performance,” 2021\)
Mercereau and Melin (“Optimizing Portfolios across Risk, Return, and Climate,” 2020\)
Miralles\-Quiros et al. (“Sustainable Development Goals and Investment Strategies: The Profitability of Using
Five\-Factor Fama\-French Alphas,” 2020\)
Mohanty et al. (“Alpha enhancement in global equity markets with ESG overlay on factor\-based investment
strategies,” 2021\)
Morgenstern et al. (“Tuning Trend\-Following Strategies with Macro ESG Data,” 2021\)
Naffa and Fain (“A factor approach to the performance of ESG leaders and laggards,” 2022\)
Nagy et al. (“Can ESG Add Alpha? An Analysis of ESG Tilt and Momentum Strategies,” 2016\)
Ocal and Kamil (“The impact of risk indicators on sustainability (ESG) and broad\-based indices: an empirical
analysis from Germany, France, Indonesia and Turkey,” 2021\)
Oikonomou et al. (“Socially Responsible Investment Portfolios: Does the Optimization Process Matter?” 2017\)
Ouchen (“Is the ESG portfolio less turbulent than a market benchmark portfolio?” 2021\)
Pan (“Demystifying ESG investing considerations for institutional cash investors,” 2020\)
Pastor et al. (“Dissecting Green Returns,” 2021\)
Pedersen et al. (“Responsible investing: The ESG\-efficient frontier,” 2021\)
Pham and Nguyen (“Asymmetric tail dependence between green bonds and other asset classes,” 2021\)
Porage (“Sustainability in Portfolio Optimization,” 2021\)
Roncalli (“Advanced Course in Asset Management,” 2021\)
Rubbaniy et al. (“Are ESG Stocks Safe\-Haven during COVID\-19?” 2021\)
Sautner and Starks (“ESG and Downside Risks: Implications for Pension Funds,” 2021\)
Schanzenbach and Sitkoff (“ESG Investing: Theory, Evidence, and Fiduciary Principles,” 2021\)
Schmidt (“Optimal ESG portfolios: an example for the Dow Jones index,” 2020\)
Schmidt (“The ESG Conundrum: An Outsider’s View,” 2021\)
Serafeim (“ESG: Hyperboles and Reality,” 2021\)
Shafer and Szado (“Environmental, social, and governance practices and perceived tail risk,” 2020\)
Sherwood and Pollard (“The risk\-adjusted return potential of integrating ESG strategies into emerging market
equities,” 2018\)
Silva et al. (“ESG Integration Strategy for Stocks Portfolios Based on a Resampling Methodology with a Mul\-
tivariate Normal Distribution,” 2021\)
Simpson et al. (“The ESG Mirage,” 2021\)
Sokolov et al. (“Weak Supervision and Black\-Litterman for Automated ESG Portfolio Construction,” 2021\)
Sorensen et al. (“The Quantitative Approach for Sustainable Investing,” 2021\)
Stotz (“Expected and realized returns on stocks with high\- and low\-ESG exposure,” 2021\)
Swedroe (“ESG Investing Means Lower Bond Yields,” 2021\)
Swedroe (“Socially Responsible Funds Do Not Deliver Excess Returns,” 2021\)
van der Meulen (“Assessment of SRI portfolio performance with particular attention to crisis periods,” 2021\)
Varmaz et al. (“Portfolio optimization for sustainable investments,” 2021\)
Vojtko and Padysak (“Quant look on ESG investing strategies,” 2020\)
von Ditfurth et al. (“Low volatility and ESG investing combined: Invesco’s holistic approach,” 2021\)
10Wilhelmsen and Woods (“ESG ratings and stock performance : an empirical investigation of the link between
ESG ratings and stock performance of European large cap firms,” 2021\)
Xiong (“The Impact of ESG Risk on Stocks,” 2021\)
Yoshino and Yuyama (“Studies of Applied Economics,” 2021\)
2\.2\.2 ESG\-based portfolio construction and investment strategies
List of references:
Alessandrini and Jondeau (“ESG investing: from sin stocks to smart beta,” 2020\)
Alessandrini and Jondeau (“Optimal Strategies for ESG Portfolios,” 2021\)
Alford (“Some considerations for investors exploring ESG strategies,” 2019\)
Amon et al. (“Passive ESG Portfolio Management – The Benchmark Strategy for Socially Responsible Investors,”
2021\)
Andersson et al. (“Portfolio Construction and New Energy Infrastructure Investing,” 2021\)
Antoncic et al. (“Sustainable Investment \- Exploring the Linkage between Alpha, ESG, and SDG’s,” 2020\)
Ascioglu et al. (“Integration of ESG Metrics into a Student\-Managed Fund:Creating Sustainable Student\-
Managed Funds,” 2017\)
Austmo and Eikeland (“Exploiting ESG Information by Extending Conventional Smart Beta Strategies: An
Empirical Analysis of Portfolio Performances through the Booms and Busts in the European Equity Market,”
2021\)
Bahra and Thukral (“ESG in Global Corporate Bonds: The Analysis Behind the Hype,” 2020\)
Benedetti et al. (“Climate change investment risk: optimal portfolio construction ahead of the transition to a
lower\-carbon economy,” 2021\)
Bennani et al. (“How ESG investing has impacted the asset pricing in the equity market,” 2019\)
Bengo et al. (“Preserving the Integrity of Social Impact Investing: Towards a Distinctive Implementation Strat\-
egy,” 2021\)
Ben Slimane et al. (“ESG Investing in Fixed Income: It’s Time to Cross the Rubicon,” 2020\)
Blitz and Hoogteijling (“Carbon\-Tax\-Adjusted Value,” 2021\)
Bohn et al. (“Sustainable Investing From a Practitioner’s Viewpoint: What’s in Your ESG Portfolio?” 2022\)
Branch et al. (“A guide to ESG portfolio construction,” 2019\)
Bruno et al. (“”Honey, I Shrunk the ESG Alpha”: Risk\-Adjusting ESG Portfolio Returns,” 2022\)
Bruder et al. (“Integration of ESG in asset allocation,” 2019\)
Caldeira (“Impact of ESG on financial performance on the most capitalized stock markets : evidence from the
USA Europe and Asia,” 2021\)
Cesarone et al. (“Does ESG impact really enhances portfolio profitability?” 2022\)
Chan et al. (“ESG in Factors,” 2020\)
Cheema\-Fox et al. (“Decarbonization Factors,” 2021\)
Chen and Mussalli (“An integrated approach to quantitative ESG investing,” 2020\)
Chong and Phillips (“ESG Investing: A Simple Approach,” 2016\)
Coqueret et al. (“Boosting ESG\-Based Optimization With Asset Pricing Characteristics,” 2021\)
Coqueret et al. (“ESG Equity Investing: A Short Survey,” 2021\)
Coqueret ( Perspectives in sustainable equity investing (website version) , 2022\)
Cornell (“ESG Investing: Conceptual Issues,” 2020\)
Cornell (“Is the Stock Market Worried About Climate Change? Lessons from the 2010s,” 2021\)
Cornell (“ESG preferences, risk and return,” 2021\)
Cosemans et al. (“Climate Change and Long\-Horizon Portfolio Choice: Combining Theory and Empirics,” 2021\)
De Spiegeleer et al. (“ESG: A New Dimension in Portfolio Allocation,” 2020\)
Dumitrescu et al. (“Defining Greenwashing,” 2022\)
Fiordelisi et al. (“An ESG Ratings Free Assessment of Socially Responsible Investment Strategies,” 2021\)
Giese et al. (“Consistent ESG through ESG Benchmarks,” 2019\)
Giese et al. (“Foundations of ESG investing: how ESG affects equity valuation, risk, and performance,” 2019\)
Gueant et al. (“Environmental transition alignment and portfolio performance,” 2021\)
Hanicova and Vojtko (“Backtesting ESG Factor Investing Strategies,” 2020\)
Harper (“One Institutional Investor Approach to Integrating ESG in the Investment Process,” 2020\)
11Henriksson et al. (“Integrating ESG in portfolio construction,” 2019\)
Hsu et al. (“Outperformance through Investing in ESG in Need,” 2018\)
Ielasi et al. (“Integrating ESG Analysis into Smart Beta Strategies,” 2020\)
Jacobsen et al. (“The alpha, beta, and sigma of ESG: better beta, additional alpha?” 2019\)
Juddoo et al. (“An Investment Strategy Based on Impact,” 2021\)
Kaiser (“ESG integration: value, growth and momentum,” 2020\)
Kaiser and Schaller (“Environmentally (Un\-)Friendly Portfolio Construction,” 2019\)
Kanuri (“Risk and Return Characteristics of Environmental, Social, and Governance (ESG) Equity ETFs,”
2020\)
Klement (“Does ESG matter for asset allocation?” 2018\)
Kumar (“ESG: Alpha or Duty?” 2019\)
Lanza et al. (“Mind the gap! Machine Learning, ESG Metrics and Sustainable Investment,” 2020\)
Lee et al. (“Combining E, S, and G Scores: An Exploration of Alternative Weighting Schemes,” 2020\)
Le Guenedal and Roncalli ( Portfolio Construction with Climate Risk Measures , 2022\)
Lindeman (“ESG Score Design And Portfolio Construction,” 2022\)
Madhavan and Sobczyk (“On the Factor Implications of Sustainable Investing in Fixed\-Income Active Funds,”
2020\)
Margot et al. (“ESG Investments: Filtering versus Machine Learning Approaches,” 2021\)
Mercereau and Melin (“Optimizing Portfolios across Risk, Return, and Climate,” 2020\)
Miralles\-Quiros et al. (“Sustainable Development Goals and Investment Strategies: The Profitability of Using
Five\-Factor Fama\-French Alphas,” 2020\)
Mohanty et al. (“Alpha enhancement in global equity markets with ESG overlay on factor\-based investment
strategies,” 2021\)
Morgenstern et al. (“Tuning Trend\-Following Strategies with Macro ESG Data,” 2021\)
Nagy et al. (“Can ESG Add Alpha? An Analysis of ESG Tilt and Momentum Strategies,” 2016\)
Owadally et al. (“Long\-Term Sustainable Investment for Retirement,” 2021\)
Pedersen et al. (“Responsible investing: The ESG\-efficient frontier,” 2021\)
Pisani and Russo (“Sustainable Finance and COVID\-19: The Reaction of ESG Funds to the 2020 Crisis,” 2021\)
Raynaud et al. (“Portfolio Alignment to a 2C Trajectory: Science or Art?” 2020\)
Roncalli (“Green and Sustainable Finance, ESG Investing and Climate Risk,” 2021\)
Ruf et al. (“Investments in ESG\-Rated Mutual Funds: Is Good Better than Great?” 2019\)
Sahin et al. (“The pitfalls of (non\-definitive) Environmental, Social, and Governance scoring methodology,”
2022\)
Sahin et al. (“ESGM: ESG scores and the Missing pillar,” 2022\)
Schmidt (“Optimal ESG portfolios: an example for the Dow Jones index,” 2020\)
Schmidt and Zhang (“Optimal ESG Portfolios: Which ESG Ratings to Use?” 2021\)
Sherwood and Pollard (“The risk\-adjusted return potential of integrating ESG strategies into emerging market
equities,” 2018\)
Silva et al. (“ESG Integration Strategy for Stocks Portfolios Based on a Resampling Methodology with a Mul\-
tivariate Normal Distribution,” 2021\)
Sokolov et al. (“Weak Supervision and Black\-Litterman for Automated ESG Portfolio Construction,” 2021\)
Sorensen et al. (“The Quantitative Approach for Sustainable Investing,” 2021\)
Varmaz et al. (“Portfolio optimization for sustainable investments,” 2021\)
Vojtko and Padysak (“Quant look on ESG investing strategies,” 2020\)
2\.2\.3 Portfolio diversification and tail risk protection through ESG investing
List of references:
Balcilar et al. (“Do Sustainable Stocks Offer Diversification Benefits for Conventional Portfolios? An Empirical
Analysis of Risk Spillovers and Dynamic Correlations,” 2017\)
Bax et al. (“ESG, Risk, and (tail) dependence,” 2021\)
Broadstock et al. (“The Role of ESG Performance During Times of Financial Crisis: Evidence from COVID\-19
in China,” 2020\)
Chan et al. (“ESG in Factors,” 2020\)
12De and Clayman (“The Benefits of Socially Responsible Investing: An Active Manager’s Perspective,” 2015\)
Giese et al. (“Foundations of ESG investing: how ESG affects equity valuation, risk, and performance,” 2019\)
Gougler and Utz (“Factor exposures and diversification: Are sustainably screened portfolios any different?”
2020\)
Gueant et al. (“Environmental transition alignment and portfolio performance,” 2021\)
Hambel et al. (“Asset Pricing and Decarbonization: Diversification versus Climate Action,” 2021\)
Kilmurray et al. (“Integrating Impact Funds into Mainstream Portfolios,” 2021\)
Lepetit et al. ( The Recent Performance of ESG Investing, the COVID\-19 Catalyst and the Biden Effect , 2021\)
Lioui (“ESG Factor Investing: Myth or Reality ?” 2018\)
Lioui and Tarelli (“Chasing The ESG Factor,” 2021\)
Mohanty et al. (“Alpha enhancement in global equity markets with ESG overlay on factor\-based investment
strategies,” 2021\)
Ouchen (“Is the ESG portfolio less turbulent than a market benchmark portfolio?” 2021\)
Pham and Nguyen (“Asymmetric tail dependence between green bonds and other asset classes,” 2021\)
Rubbaniy et al. (“Are ESG Stocks Safe\-Haven during COVID\-19?” 2021\)
Shafer and Szado (“Environmental, social, and governance practices and perceived tail risk,” 2020\)
Xiong (“The Impact of ESG Risk on Stocks,” 2021\)
2\.2\.4 ESG ratings and scores
List of references:
Akgun et al. (“How Company Size Bias in ESG Scores Impacts the Small Cap Investor,” 2021\)
Angelova et al. (“Sovereign rating methodologies, ESG and climate change risk: an overview,” 2021\)
Avramov et al. (“Sustainable investing with ESG rating uncertainty,” 2022\)
Berg et al. (“ESG Confusion and Stock Returns: Tackling the Problem of Noise,” 2022\)
Berg et al. (“Aggregate Confusion: The Divergence of ESG Ratings,” 2022\)
Berg et al. (“Rewriting History II: The (Un)Predictable Past of ESG Ratings,” 2021\)
Bettin (“Sustainable finance and ESG scores: A portfolio analysis a la Fama and French,” 2021\)
Billio et al. (“Inside the ESG Ratings: (Dis)agreement and Performance,” 2021\)
Boucher et al. ( Backtesting ESG Ratings , 2021\)
Cakici and Zaremba (“Responsible Investing: ESG Ratings and the Cross\-Section of International Stock Re\-
turns,” 2021\)
Caldeira (“Impact of ESG on financial performance on the most capitalized stock markets : evidence from the
USA Europe and Asia,” 2021\)
Cornell (“ESG preferences, risk and return,” 2021\)
D’Amato et al. (“Fundamental ratios as predictors of ESG scores: a machine learning approach,” 2021\)
Dimson et al. (“Divergent ESG Ratings,” 2020\)
Fiordelisi et al. (“An ESG Ratings Free Assessment of Socially Responsible Investment Strategies,” 2021\)
Geczy and Guerard (“ESG and Expected Returns on Equities: The Case of Environmental Ratings,” 2021\)
Gibson Brandon et al. (“ESG Rating Disagreement and Stock Returns,” 2021\)
Gidwani (“Some Issues with Using ESG Ratings in an Investment Process,” 2020\)
Giese et al. (“Deconstructing ESG Ratings Performance: Risk and Return for E, S, and G by Time Horizon,
Sector, and Weighting,” 2021\)
Gregory (“The Response of the S\&P 1500 during the COVID\-19 Pandemic and ESG Scores,” 2021\)
Gyonyorova et al. (“ESG ratings: relevant information or misleading clue? Evidence from the S\&P Global
1200,” 2022\)
Ielasi et al. (“Integrating ESG Analysis into Smart Beta Strategies,” 2020\)
Kaurissaari (“Markowitz Revisited: Is there trade\-off between return and responsibility?” 2021\)
Kapri (“Implications of mutual funds’ ESG score on performance,” 2021\)
Krappel et al. (“Heterogeneous Ensemble for ESG Ratings Prediction,” 2021\)
Lee et al. (“Combining E, S, and G Scores: An Exploration of Alternative Weighting Schemes,” 2020\)
Lindeman (“ESG Score Design And Portfolio Construction,” 2022\)
Lopez et al. (“ESG Ratings: The Road Ahead,” 2020\)
Mannix (“Investors turn to raw data over ratings in ESG alpha hunt,” 2020\)
13Martin (“Impact Investing. A Practitioner Perspective,” 2021\)
Oude Veldhuis (“Corporate Social Responsibility and the effect of ESG scores on stock returns,” 2021\)
Polbennikov et al. (“ESG Ratings and Performance of Corporate Bonds,” 2016\)
Pyles (“Examining Portfolios Created by Bloomberg ESG Scores: Is Disclosure an Alpha Factor?” 2020\)
Rzenik et al. (“The Salience of ESG Ratings for Stock Pricing: Evidence From (Potentially) Confused Investors,”
2021\)
Sahin et al. (“The pitfalls of (non\-definitive) Environmental, Social, and Governance scoring methodology,”
2022\)
Sahin et al. (“ESGM: ESG scores and the Missing pillar,” 2022\)
Schmidt and Zhang (“Optimal ESG Portfolios: Which ESG Ratings to Use?” 2021\)
Semet et al. (“ESG and Sovereign Risk: What is Priced in by the Bond Market and Credit Rating Agencies?”
2021\)
Shanaev and Ghimire (“When ESG meets AAA: The effect of ESG rating changes on stock returns,” 2021\)
Sokolov et al. (“Building Machine Learning Systems for Automated ESG Scoring,” 2021\)
Swedroe (“Do Wide Divergences in ESG Ratings Doom Investors?” 2021\)
Swedroe (“Revisionist History in ESG Ratings,” 2021\)
Tang et al. (“The Determinants of ESG Ratings: Rater Ownership Matters,” 2021\)
Tharavanij (“ESG Rating and Financial Performance: A Review Article,” 2021\)
Wang et al. (“Does ESG Screening Enhance or Destroy Stock Portfolio Value? Evidence from China,” 2022\)
Zhang (“ESG Rating Divergence: Beauty Is in the Eye of the Beholder,” 2021\)
2\.2\.5 Impact Investing
List of references:
Barber et al. (“Impact investing,” 2021\)
Bengo et al. (“Preserving the Integrity of Social Impact Investing: Towards a Distinctive Implementation Strat\-
egy,” 2021\)
Berk and van Binsbergen (“The Impact of Impact Investing,” 2021\)
Geczy et al. (“Contracts with (Social) benefits: The implementation of impact investing,” 2021\)
Grim and Berkowitz (“ESG, SRI, and Impact Investing: A Primer for Decision\-Making,” 2020\)
Gutterman (“Impact Investment Tools, Structures and Instruments,” 2020\)
Hays and McCabe (“Sustainable and Impact Investing: A Taxonomy of Approaches and Considerations for
Fiduciaries,” 2021\)
Juddoo et al. (“An Investment Strategy Based on Impact,” 2021\)
Kilmurray et al. (“Integrating Impact Funds into Mainstream Portfolios,” 2021\)
Lo and Zhang (“Quantifying the Impact of Impact Investing,” 2022\)
Parker (“Achieving Goals While Making an Impact: Balancing Financial Goals with Impact Investing,” 2021\)
Jeffers et al. (“The Risk and Return of Impact Investing Funds,” 2021\)
2\.2\.6 Climate based investing and risk
List of references:
Amel\-Zadeh (“The Materiality of Climate Risk,” 2021\)
Andersson et al. (“Portfolio Construction and New Energy Infrastructure Investing,” 2021\)
Barnett et al. (“Pricing uncertainty induced by climate change,” 2020\)
Bajic et al. (“Handle with Care: Challenges and Opportunities of using Company\-Level Emissions Data for
Assessing Financial Risks from Climate Change,” 2021\)
Baz et al. (“Climate Regulatory Exposure: Evidence from Stock Returns,” 2021\)
Bender et al. (“Reducing the carbon intensity of low volatility portfolios,” 2020\)
Benedetti et al. (“Climate change investment risk: optimal portfolio construction ahead of the transition to a
lower\-carbon economy,” 2021\)
Bingler et al. (“Cheap Talk and Cherry\-Picking: What ClimateBert has to say on Corporate Climate Risk
Disclosures,” 2021\)
Bingler et al. (“Cheap Talk in Corporate Climate Commitments: The Role of Active Institutional Ownership,
Signaling, Materiality, and Sentiment,” 2022\)
14Blitz and Hoogteijling (“Carbon\-Tax\-Adjusted Value,” 2021\)
Bolliger and Cornilly (“Sustainability Attribution: The Case of Carbon Intensity,” 2021\)
Bolton and Kacperczyk (“Do investors care about carbon risk?” 2021\)
Chan et al. (“ESG in Factors,” 2020\)
Cheema\-Fox et al. (“Decarbonization Factors,” 2021\)
Chen and Bowler (“Constructing and Validating Climate Risk Factors from ESG Data: an Empirical Compari\-
son,” 2021\)
Choi et al. (“Measuring the carbon exposure of institutional investors,” 2020\)
Cosemans et al. (“Climate Change and Long\-Horizon Portfolio Choice: Combining Theory and Empirics,” 2021\)
Duan et al. (“Is Carbon Risk Priced in the Cross Section of Corporate Bond Returns?” 2021\)
Engle et al. (“Hedging climate change news,” 2020\)
Faccini et al. (“Dissecting Climate Risks: Are they Reflected in Stock Prices?” 2021\)
Focardi and Fabozzi (“Climate change and asset management,” 2020\)
Friederich et al. (“Automated Identification of Climate Risk Disclosures in Annual Corporate Reports,” 2021\)
Garnier (“The Climate Extended Risk Model (CERM),” 2022\)
Giese et al. (“Foundations of Climate Investing: How Equity Markets Have Priced Climate\-Transition Risks,”
2021\)
Gorgen et al. (“Get Green or Die Trying? Carbon Risk Integration into Portfolio Management,” 2021\)
Heeb et al. (“Do Investors Care About Impact?” 2022\)
Hain et al. (“Let’s get physical: Comparing metrics of physical climate risk,” 2021\)
Hambel et al. (“Asset Pricing and Decarbonization: Diversification versus Climate Action,” 2021\)
Hodges et al. (“Net Zero Investing for Multi\-Asset Portfolios seeking to satisfy Paris Aligned Benchmark Re\-
quirements with Climate Alpha Signals,” 2022\)
Immel et al. (“Green bonds: shades of green and brown,” 2021\)
Jacobsen et al. (“Climate Change and Asset Allocation: A Distinction That Makes a Difference,” 2021\)
Jondeau et al. (“Building Benchmarks Portfolios with Decreasing Carbon Footprints,” 2021\)
Kaustia and Yu (“Greenwashing in Mutual Funds,” 2021\)
Kazdin et al. (“Climate Alpha with Predictors Also Improving Company Efficiency,” 2021\)
Krueger et al. (“The importance of climate risks for institutional investors,” 2020\)
Le Guenedal and Roncalli ( Portfolio Construction with Climate Risk Measures , 2022\)
Lo and Zhang (“Quantifying the Impact of Impact Investing,” 2022\)
Mercereau and Melin (“Optimizing Portfolios across Risk, Return, and Climate,” 2020\)
Nofsinger and Varma (“Keeping Promises? Carbon Risk Disclosure and Mutual Fund Portfolios,” 2021\)
Raynaud et al. (“Portfolio Alignment to a 2C Trajectory: Science or Art?” 2020\)
Reboredo and Otero (“Are investors aware of climate\-related transition risks? Evidence from mutual fund flows,”
2021\)
Roncalli et al. (“Measuring and Managing Carbon Risk in Investment Portfolios,” 2020\)
Roncalli (“Green and Sustainable Finance, ESG Investing and Climate Risk,” 2021\)
Semet et al. (“ESG and Sovereign Risk: What is Priced in by the Bond Market and Credit Rating Agencies?”
2021\)
Shen et al. (“Strategic asset allocation with climate change,” 2019\)
Swinkels (“Allocating to green bonds,” 2021\)
Terpstra (“ESG ratings and stock performance: Do high ESG portfolios perform differently within and between
industries?” 2021\)
Tokat\-Acikel et al. (“Top\-Down Portfolio Implications of Climate Change,” 2021\)
Venturini (“Climate change, risk factors and stock returns: A review of the literature,” 2022\)
van Tilborg (“(Ir)responsible Investing: Revisiting the Effects of ESG Performance on Portfolio Returns,” 2021\)
Webersinke et al. (“ClimateBert: A Pretrained Language Model for Climate\-Related Text,” 2021\)
Westcott et al. (“Be Prepared: Exploring Future Climate\-Related Risk for Residential and Commercial Real
Estate Portfolios,” 2020\)
152\.2\.7 Metrics, performance and benchmarks for ESG\-based investing
List of references:
Alessandrini and Jondeau (“Optimal Strategies for ESG Portfolios,” 2021\)
Amon et al. (“Passive ESG Portfolio Management – The Benchmark Strategy for Socially Responsible Investors,”
2021\)
Antoncic et al. (“Sustainable Investment \- Exploring the Linkage between Alpha, ESG, and SDG’s,” 2020\)
Ascioglu et al. (“Integration of ESG Metrics into a Student\-Managed Fund:Creating Sustainable Student\-
Managed Funds,” 2017\)
Austmo and Eikeland (“Exploiting ESG Information by Extending Conventional Smart Beta Strategies: An
Empirical Analysis of Portfolio Performances through the Booms and Busts in the European Equity Market,”
2021\)
Aw et al. (“A Morality Tale of ESG: Assessing Socially Responsible Investing,” 2017\)
Baeza\-Sampere et al. (“A fuzzy data envelopment analysis model for evaluating the efficiency of socially respon\-
sible and conventional mutual funds,” 2016\)
Bahra and Thukral (“ESG in Global Corporate Bonds: The Analysis Behind the Hype,” 2020\)
Billio et al. (“Inside the ESG Ratings: (Dis)agreement and Performance,” 2021\)
Bolliger and Cornilly (“Sustainability Attribution: The Case of Carbon Intensity,” 2021\)
Boucher et al. ( Backtesting ESG Ratings , 2021\)
Broadstock et al. (“The Role of ESG Performance During Times of Financial Crisis: Evidence from COVID\-19
in China,” 2020\)
Bush et al. (“E, S, or G \- Analyzing Global ESG Performance,” 2020\)
Cai et al. (“Socially Responsible Investing and Factor Investing, Is There an Opportunity Cost?” 2022\)
Calvo et al. (“Finding socially responsible portfolios close to conventional ones,” 2015\)
Chang et al. (“How Interpretable and Trustworthy are GAMs?” 2021\)
Chen and Bowler (“Constructing and Validating Climate Risk Factors from ESG Data: an Empirical Compari\-
son,” 2021\)
Chen and Deleon (“Financial Quality Metrics and ESG Factor Interactions in Equity Markets,” 2020\)
Coqueret et al. (“Boosting ESG\-Based Optimization With Asset Pricing Characteristics,” 2021\)
Coqueret et al. (“ESG Equity Investing: A Short Survey,” 2021\)
Cornell (“ESG preferences, risk and return,” 2021\)
Cosemans et al. (“Climate Change and Long\-Horizon Portfolio Choice: Combining Theory and Empirics,” 2021\)
De Franco (“ESG Controversies and Their Impact on Performance,” 2019\)
Dumitrescu et al. (“Defining Greenwashing,” 2022\)
Filbeck et al. (“Performance assessment of firms following sustainalytics ESG principles,” 2019\)
Fridson et al. (“ESG Impact on High\-Yield Returns,” 2021\)
Giese et al. (“Consistent ESG through ESG Benchmarks,” 2019\)
Giese et al. (“Consistent ESG through ESG Benchmarks,” 2019\)
Giese et al. (“Foundations of ESG investing: how ESG affects equity valuation, risk, and performance,” 2019\)
Gueant et al. (“Environmental transition alignment and portfolio performance,” 2021\)
Hain et al. (“Let’s get physical: Comparing metrics of physical climate risk,” 2021\)
Hanicova and Vojtko (“Backtesting ESG Factor Investing Strategies,” 2020\)
Hodges et al. (“Net Zero Investing for Multi\-Asset Portfolios seeking to satisfy Paris Aligned Benchmark Re\-
quirements with Climate Alpha Signals,” 2022\)
Hsu et al. (“Outperformance through Investing in ESG in Need,” 2018\)
Jondeau et al. (“Building Benchmarks Portfolios with Decreasing Carbon Footprints,” 2021\)
Khan (“Corporate Governance, ESG, and Stock Returns around the World,” 2019\)
Lanza et al. (“Mind the gap! Machine Learning, ESG Metrics and Sustainable Investment,” 2020\)
Le Guenedal and Roncalli ( Portfolio Construction with Climate Risk Measures , 2022\)
Li et al. (“Robust enhanced indexation with ESG: An empirical study in the Chinese Stock Market,” 2022\)
Lindeman (“ESG Score Design And Portfolio Construction,” 2022\)
Lo and Zhang (“Quantifying the Impact of Impact Investing,” 2022\)
Ouchen (“Is the ESG portfolio less turbulent than a market benchmark portfolio?” 2021\)
Plagge and Grim (“Have investors paid a performance price? examining the behavior of ESG equity funds,”
2020\)
16Polbennikov et al. (“ESG Ratings and Performance of Corporate Bonds,” 2016\)
Roncalli (“Advanced Course in Asset Management,” 2021\)
Ruf et al. (“Investments in ESG\-Rated Mutual Funds: Is Good Better than Great?” 2019\)
Sorensen et al. (“The Quantitative Approach for Sustainable Investing,” 2021\)
Statman and Glushkov (“Classifying and Measuring the Performance of Socially Responsible Mutual Funds,”
2016\)
Tharavanij (“ESG Rating and Financial Performance: A Review Article,” 2021\)
Walkshausl (“Dissecting the performance of socially responsible firms,” 2018\)
Yeh et al. (“SustainBench: Benchmarks for Monitoring the Sustainable Development Goals with Machine Learn\-
ing,” 2021\)
2\.2\.8 NLP, text, topic and sentiment analysis within context of ESG investing
List of references:
Ascioglu et al. (“Analysis of Sustainability Reports for Top 20 Companies in the S\&P 500 Index,” 2022\)
Azevedo et al. (“Investor sentiment and the time\-varying sustainability premium,” 2021\)
Ballinari and Mahmoud (“From Chatter to Action: An Index of Sustainability Sentiment,” 2021\)
Ben Dor et al. (“ESG and Alternative Data: Capturing Corporates’ Sustainability\-Related Activities with Job
Postings,” 2021\)
Bingler et al. (“Cheap Talk and Cherry\-Picking: What ClimateBert has to say on Corporate Climate Risk
Disclosures,” 2021\)
Bingler et al. (“Cheap Talk in Corporate Climate Commitments: The Role of Active Institutional Ownership,
Signaling, Materiality, and Sentiment,” 2022\)
Bonaparte (“The ESG Investor Sentiment Index: A Cross Sectional and Time Series Analyses,” 2021\)
Borms et al. (“Semi\-supervised Text Mining for Monitoring the News About the ESG Performance of Compa\-
nies,” 2021\)
Chava et al. (“Doing Well by Doing Good? Risk, Return, and Environmental and Social Ratings,” 2021\)
Chen et al. (“NLP for SDGs: Measuring Corporate Alignment with the Sustainable Development Goals,” 2022\)
Coqueret and Tran (“ESG news spillovers to (and from) the supply chain,” 2022\)
D’Amato et al. (“Fundamental ratios as predictors of ESG scores: a machine learning approach,” 2021\)
Engle et al. (“Hedging climate change news,” 2020\)
Faccini et al. (“Dissecting Climate Risks: Are they Reflected in Stock Prices?” 2021\)
Friederich et al. (“Automated Identification of Climate Risk Disclosures in Annual Corporate Reports,” 2021\)
Guo et al. (“ESG2Risk: A Deep Learning Framework from ESG News to Stock Volatility Prediction,” 2020\)
Hakala (“Can ESG controversies predict medium\- to long\-term stock performance? Evidence from global mar\-
kets,” 2021\)
Luccioni et al. (“Analyzing Sustainability Reports Using Natural Language Processing,” 2020\)
Nugent et al. (“Detecting ESG topics using domain\-specific language models and data augmentation approaches,”
2020\)
Serafeim (“Public sentiment and the price of corporate sustainability,” 2020\)
Sokolov et al. (“Building Machine Learning Systems for Automated ESG Scoring,” 2021\)
Taleb et al. (“Corporate ESG News and The Stock Market,” 2020\)
Webersinke et al. (“ClimateBert: A Pretrained Language Model for Climate\-Related Text,” 2021\)
2\.2\.9 Testing and comparison procedures for investment portfolios
References:
Adcock et al. (“Portfolio Performance Measurement: Monotonicity with Respect to the Sharpe Ratio and
Multivariate Tests of Correlation,” 2017\)
Arnott et al. (“A backtesting protocol in the era of machine learning,” 2019\)
Bailey et al. (“Stock Portfolio Design and Backtest Overfitting,” 2017\)
Bessler and Wolff (“Portfolio Optimization with Industry Return Prediction Models,” 2017\)
Bessler et al. (“Multi\-asset portfolio optimization and out\-of\-sample performance: an evaluation of Black Lit\-
terman, mean\-variance, and naive diversification approaches,” 2017\)
Bjerring et al. (“Feature selection for portfolio optimization,” 2017\)
17Bruni et al. (“On exact and approximate stochastic dominance strategies for portfolio selection,” 2017\)
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
Guo et al. (“When Does The 1/N Rule Work?” 2019\)
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
18Yu (“Comparing Classical Portfolio Optimization and Robust Portfolio Optimization on Black Swan Events,”
2021\)
Zhang et al. (“DoubleEnsemble: A New Ensemble Method Based on Sample Reweighting and Feature Selection
for Financial Data Analysis,” 2020\)
Zhang et al. (“Information Coefficient as a Performance Measure of Stock Selection Models,” 2020\)
Zhang et al. (“Deep Learning for Portfolio Optimization,” 2020\)
193 Practical details for the project
The main purpose of the project described in this document is to provide exposure to students on important (and
interesting) practical topics in quantitative wealth and investment management QWIM.
The level of complexity depends on the number of hours designated for the project. For example, 50\-60 hours for
a regular project, and 100\-120 hours for a thesis/capstone project. Upon request, the scope (and the corresponding
number if hours) of any given project can be extended.
The students would work on the project as part of a team (usually with 2\-3 students).
All QWIM projects were selected such that the students’ efforts have a good chance of producing results relevant
to the industry, and at least as good as the results presented in the QWIM literature. Thus for each project we
may consider (on an optional basis, based primarily on students’ preference) to submit a corresponding article to
journals widely followed by practitioners and academics in investment and wealth management, with participating
students included as the leading coauthors of the submitted article.
The main challenge for each project is to identify the criteria for what would be considered “good enough ”.
Similar to projects in the industry, the meaning of “good enough” is based on a combination of comprehensive
literature review, discussions within team and with me (and/or my colleagues) and analysis of results. Emphasis is
placed on creating a narrative (with the aid of an interactive visualizer) for convincing the intended audience that
what was done in the project delivers “good enough ”outcome.
3\.1 Interaction with students
For each project I would make myself available for meetings on a weekly basis (for discussions and guidance).
Some of my colleagues have also expressed interest to participate in such meetings. Due to our work schedule and
deliverables, most of the discussions will have to be scheduled outisde working hours (in weekends or evenings).
The meetings will take place through video conferencing such as WebEx, Zoom, Google Meet, Microsoft Teams,
etc., based on the team’s preference. If the meetings are through WebEx, I would provide a link, while the student
team will provide a link for any other video conferencing tool.
The students working on a given project can also send questions by email (my recommendation is to aggregate
the questions from team members into an email sent once a day). We aim to provide answers within 1\-2 days, either
by email or through a phone discussion.
3\.2 Data
Due to compliance reasons all projects would be based on publicly available, non\-proprietary and non\-confidential
data (indices, ETFs, mutual funds, etc.). Since neither I nor my team are allowed to provide these datasets, I can
only provide a list of suggested datasets. This list is included in a later section named Practical Info.
The datasets were selected to have the following features:
•be good proxies for most representative asset and subasset classes
•to be widely available
•to be as liquid as possible
•to have daily granularity
•to encompass periods with as many market regimes as possibles (most proposed daily datasets are from 1990
or 1991\)
•time series have “nicer” statistical properties compared to time series of, say, individual stocks or bonds
3\.3 Private GitHub repository for the QWIM project
The team will create a private GitHub repository, which will store relevant project materials, including codes. The
team will use Git Desktop application as source control repository linked to the GitHub repository.
203\.4 Deliverables
The project deliverables include literature survey, numerical results, analysis and visualization. For each project
references will be provided for a comprehensive literature survey, and students are encouraged to identify additional
relevant literature. Regarding the implementation, the project will primarily use existing codes:
•Python and R packages from official repositories (PyPi for Python and CRAN for R)
•machine learning platforms such as TensorFlow, PyTorch, CNTK, Chainer, mlr3, H20, PlaidML, mlpack, etc.
•implementations of articles through codes available in repositories such as GitHub, BitBucket, GitLab, etc.
Visualization of data and results visualization will be interactive and it will be based on Shiny R framework; to
reduce programming effort, a template for such a Shiny visualizer will be provided in the team private GitHub
repository.
The deliverables are:
•written report including literature survey and numerical results
•interactive visualizer (most likely Shiny\-based visualizer using R and Python packages)
•(optional) presentation slides, and/or RMarkdown presentation, and/or Jupyter Notebook(s)
3\.5 (Optional) Article submission to leading journals
On an optional basis (based primarily on students’ preference), a version of the report can be prepared for submision
to leading journals such as Journal of Financial Data Science, Journal of Portfolio Management, Journal of Asset
Management, Journal of Investment Strategies, Quantitative Finance, Journal of Wealth Management, Journal of
Investing, Journal of Machine Learning in Finance, etc.
214 Project tasks and timelines
For each project the main tasks are:
1\)literature review
2\)decide on the appropriate metrics and quantitative methods within context of "good enough" for the project
3\)write\-up summary of literature review: methods, metrics, testing procedures
4\)identification of Python and/or R packages which are most appropriate for the selected methods and metrics
5\)code design to decide on main code components
6\)implementation of code components
7\)interactive visualization of numerical results
8\)project report containing description of methods, metrics, and tests, and analysis of results.
4\.1 Suggested timelines for project tasks
The table below suggests a timeline for the project tasks and the corresponding percentages of project time:
Table 1: Suggested timeline for project tasks
Task ID Task Name Percentage of project time
1 Literature review 15%
2 Identification of "good enough" metrics and quantitative methods 5%
3 Write\-up of summary of literature review 5%
4 Identification of appropriate packages in Python and/or R 10%
5 Code design for main components of project coding framework 5%
6 Implementation of coding framework and components 40%
7 Interactive visualizer using the provided Shiny template 10%
8 Project report and presentation 10%
4\.2 Literature review
The first task is based on a comprehensive literature survey, included in the preliminary document of the project.
Students are encouraged to identify additional relevant literature.
This task may be the most important of the project, since it provides an overview of what was done, what works
well and less well, and what appear to be the most promising avenues to complete the project.
Emphasis is placed on information contained in the Main References; the other References would be considered
only if time permits and the team is interested in exploring other avenues.
When reading the literature, there are 4 main directions to consider:
1\)methods
2\)metrics to assess the performance/robustness of the methods
3\)testing procedures
4\)numerical results
The primary focus would be on the the references included in "Main References" subsection of the document for your
QWIM project. Then, to the extent there is time, to consider the other references included in the project document.
In the same time, you are encouraged to identify other references that might be considered "Main references", and
to share those references with me for discussion.
For the articles in Main References category, the suggested approach would be the following:
22•For each article focus primarily on Abstract, Conclusion, and Numerical Results
•Do this for all articles considered to be Main References, such that you gain a high\-level understanding of
what is currently done in the literature
•Select the metrics that you may want to use in order to quantify the meaning of "good enough" for the project.
•Select the quantitative methods which appear to be most likely to be "good enough" for the project.
•Perform a "deeper dive" into the articles containing the approaches you consider the most promising,
For the articles which are not in "Main References" category, read Abstract, Conclusion, and Numerical Results, to
see whether any of those articles might need to be considered for inclusion in your summary.
4\.3 Write\-up summary of literature review
The write\-up summary summarizes the methods, metrics, testing procedures, and numerical results identified during
the literature review. The write\-up could also be incorporated within reports and/or presentations for the QWIM
project.
4\.4 Identification of appropriate Python and/or R packages
Based on the literature review and on diiscussions, we identify the most potentially useful methods, metrics and
testing procedures. Then wee identify the most appropriate implementations of the selected methods and metrics.
The primary sources of implementatins are existing codes from:
•Python and R packages from official repositories (PyPi for Python and CRAN for R)
•machine learning platforms such as TensorFlow, PyTorch, CNTK, Chainer, mlr3, H20, PlaidML, mlpack, etc.
•Codes available in repositories such as GitHub, BitBucket, GitLab, etc.
4\.5 Code design
An important task is to have a code design session to decide in advance on the main code components, which are
meant to be modular and encapsulated, such that the entire team can work on the codes.
Examples of such main components include extracting data, calculate metrics for the considered procedures,
portfolio metrics, performing tests, construct interactive visualizer, etc.
The code design procedure consists of:
1\)visual display of major components of the coding framework
2\)UML diagrams for each of the components.
The Appendix contains an illustrative example within context of a QWIM project on forecasting of financial
time series. The first figure shows the major components, while the second figure shows UML diagrams of those
components (the names of data members and methods are currently generic, and one would need to change them
to appropriate names)
While these figures were obtained through Microsoft Visio using a code design file (.vsd file), there are other
software tools (either online or installed locally) which can be used to create such code design diagrams. NOTE: if
you have access to Microsoft Visio and you want to use it for code design diagrams, you can ask me for the .vsd
file which was exported into the PDF from which I have extracted the snapshots.
List of software tools for code design diagrams, which are either free (open source) or have a free type of account
•Modelio (either desktop version or online version)
•LucidChart ( online )
•draw.io (either desktop version or online version, now called app.diagrams.net)
23•Visual Paradigm ( online )
•UMLet (either desktop oronline version)
•Curated list of UML tools – 2019 edition
•Top online UML modeling tools in 2019
4\.6 Implementation of coding framework and components
The implementation is done using identified packages or codes, in Python and/or R. The project will primarily use
existing codes:
•Python and R packages from official repositories (PyPi for Python and CRAN for R)
•machine learning platforms such as TensorFlow, PyTorch, CNTK, Chainer, mlr3, H20, PlaidML, mlpack, etc.
•implementations of articles through codes available in repositories such as GitHub, BitBucket, GitLab, etc.
4\.7 Interactive visualizer
While visualization of data and numerical results can be done through various tools (including Jupyter notebooks
or Dash in Python), my recommendation is to consider an interactive visualizer based on Shiny framework in R.
A template for the Shiny visualizer will be provided in the private GitHub repository set up by the team for the
project.
Some information about Shiny:
•Shiny from RStudio :tutorials andgallery
•Why R Shiny Trumps UI and JavaScript Based Visualization Tools
•Shiny’s Holy Grail: Interactivity with reproducibility
4\.8 Project report and presentation
The report containing description of methods, metrics, and tests, and analysis of results.
While the report can be written using various tools (including Microsoft Word), my recommendation is to use
LyX to write both the project report and the project presentation. Two LyX templates for creating reports and,
respectively, presentations will be provided in the private GitHub repository set up by the team for the project.
Some information about Shiny:
•LyX features
•LyX tutorial with PDF here
•LyX Tutorial video Part One andPart Two
•LyX tutorial video Part One andPart Two andPart Three andPart Four
•Introduction to LyX
•Insert figures in LyX
•Essentials of LyX
245 Design and implementation for the project codes
This section describes a possible approach for the design process and for the implementation (folder structure) of
the project. This approach is presented only to exemplify how it could be done. Each student team has freedom to
consider their own design process.
Design and implementation would be based on following principles:
•coding framework is Python based, with calls to functions available in existing Python and R packages
•leverage common components (such as data input/output, numerical methods, time series, testing, interactive
visualization and reporting, etc.)
•reusability
•incorporate best practices in coding and numerical implementations
•use, augment and enhance (to largest extent possible) existing Python and R packages and codes
5\.1 Visualize project workflow and coding framework
The starting point is to visualize the project workflow in terms of major components, and then to design the code
framework.
The code design procedure consists of:
1\)visual display of major components of the coding framework
2\)UML diagrams for each of the components.
We present examples below for projects including time series forecasting and analysis, machine learning for portfolio
construction, etc.
Figure 1: Examples of architecture of coding framework: AlphaPy
Source: AlphaPy
25Figure 2: Examples of architecture of coding framework: Greykite
Source: Geykite
Figure 3: QLib Framework
Trading Agent
Meta ControllerAnalyser
Decision
Forecast ModelInterface Multi\-level Workflow InfrastractureForecasting... Portfolio A...Execution...
Information ExtractorOnline Serving
Graph EventFactor Text
Risk Alpha
Data Server
local remoteTrainer
Algorithms Auto\-MLModel Manager
ModelModelModelsModelModelDecision GeneratorsModel Interpreter
Decision Generator
Order executi...
Execution ResultsExecution Env
Sub\-workfl... VWAP/Close/......
Highly Customiz...
Module in devel...ExplanationSub\-workflow(1\) (E.g. High\-frequ...
Execution E...
...
(1\) The sub\-workflow will make more fine\-grained decisions according to the decision from the upper\-level trading agentStock selecti... Asset allocat...Trading...
Viewer does not support full SVG 1\.1
26Figure 4: Examples of major components of coding framework (top) and UML diagrams (bottom)
27Figure 5: Financial Machine Learning in Portfolio Construction
Source: Machine Learning in Asset Management285\.2 Representative examples of Python libraries with well designed folder structure
List of Python libraries
•QLib is a AI\-oriented quantitative investment platform in Python developed by Microsoft researchers
•GluonTS is a Python library deveoped by Amazon researchers for probabilistic time series modeling
•sktime is a unified framework for machine learning with time series, developed by researchers at Alan Turing
Institute for data science and artificial intelligence.
•darts is a Python library for easy manipulation and forecasting of time series, developed by researchers at
Unit8 AI and data analytics company.
•Katsis a Python library developed by Facebook researchers to analyze time series data.
•Katsis a Python library developed by Tinkoff AI researchers to analyze time series data.
•MLFinLab (Machine Learning Financial Laboratory) is a Python library developed by researchers at Hudson
\& Thames.
296 Practical Info
6\.1 Recommended software tools
The sections below describe the recommended software tools, including corresponding versions/subversions, tutorials
and details
6\.1\.1 Python
The recommended versions are:
•Python version 3\.8 (subversion Python 3\.8\.10 or 3\.8\.15\)
•Python version 3\.9 (subversion Python 3\.9\.10 or 3\.9\.15\)
•Python version 3\.10 (latest subversion, currently Python 3\.10\.8\)
There are also relevant Python packages, identified while you are working the project. As a starting point you can
consider the packages included in section on Potentially useful Python and R packages.
6\.1\.2 R
The recommended versions are:
•R version 4\.2 (recommended is latest subversion, currently R 4\.2\.2\)
•R version 3\.6 (subversion R 3\.6\.3\)
On Windows computers you also need to install Rtools to build R packages from source through compilation, since
not all packages have associated Windows binaries.
There are also relevant R packages, identified while you are working the project. As a starting point you can
consider the packages included in section on Potentially useful Python and R packages.
6\.1\.3 R IDE
The recommended R IDE is RStudio Desktop Open Source
•latest version, currently 2022\.07\.2\+576
6\.1\.4 Python IDE
The recommended Python IDE is Visual Studio Code VSC
•latest version, currently VSC 1\.73
Then add Python extension and other Visual Studio Code extensions from Visual Studio MarketPlace.
Note: Upon request I can provide a list of potentially useful VSC extensions, which can be installed on your
computer (see for example link)
6\.1\.5 Bibliography Manager
The recomemnded bibliography manager is JabRef
•latest version: version 5\.7, or
•latest development version from link
30I can provide you with a bibliography file which contains all refeernces mentioned in the project description, This
file (of extension bib) can be viewed and edited with JabRef, and used together with LyX to write your project
related documents (report, presentation, etc.).
You can easily add/delete/edit this bib file using JabRef.
There are video tutorials on using JabRef: link 1,link 2,link 3\.
In addition to these video tutorials, I can also have a video online session, to provide an overview and answer
your questions on using LyX and JabRef. This online session (through Google Meet Google Meet) can be recorded
and shared with you afterwards.
6\.1\.6 Document processor
The recommended document processor is LyX, which is a document processor that encourages an approach to
writing based on the structure of your documents (WYSIWYM) and not simply their appearance (WYSIWYG).
LyX combines the power and flexibility of TeX/LaTeX with the ease of use of a graphical interface. It shoudl
be emohasized that you do not need to know/learn LaTeX in order to tuse LyX.
To install LyX, you need to download and install first TeXLive (see link), which is a packaged distribution of
LaTeX and associated packages
Then install LyX using installers , making sure that you are pointing to location of installed TeXLive when asked
for a LaTeX distribution during the run of LyX installer.
Recommended versions:
•TexLive (recommended is latest version, currently TeXLive 2022\)
•LyX (recommended is latest subversion, currently LyX 2\.3\.6\.1\)
There are video tutorials ( link 1 andlink 2\).
In addition to these video tutorials, I can also have a video online session, to provide an overview and answer
your questions on using LyX and JabRef. This online session (through Google Meet Google Meet) can be recorded
and shared with you afterwards.
6\.1\.7 Source control manager
The recommended source control manager is GitHub desktop , which can be used in conjunction with thr private
GitHub repository that each student team will create for their project
•latest subversion, currently GitHub Desktop 3\.1\.2
6\.1\.8 File editor
The recommended file editor is Notepad\+\+
•latest subversion (currently Notepad\+\+ 8\.4\.7\) with various plugins (see list of available plugins at link 1 and
link 2\)
6\.1\.9 Runtime libraries
Many Python and R packages require runtime libraries such as Microsoft Visual C\+\+ Redistributable
•latest version, currently Microsoft Visual C\+\+ Redistributable 64\-bit for Visual Studio 2015, 2017, 2019, and
2022
6\.2 Recommended datasets
The datasets below were selected to have the following features:
•to be representative proxies for most relevant asset and subasset classes
•to be widely available
31•to be as liquid as possible
•to have daily granularity
•to encompass time periods containing as many market regimes as possibles (under this consideration, the
recommended daily datasets start from early 1990s)
•to have “nicer” statistical properties, which will make modeling easier (under this consideration, time series of
recommended financial indices have “nicer” statistical properties compared to time series of individual stocks
or bonds)
The following datasets are suggested
Table 2: Daily data sets
Name Description Name Description
BCOMTR Bloomberg Commodity Index Total
ReturnRU20VATR iShares Russell 2000 Value ETF
HFRIFWI HFRI Fund Weighted Composite Index RUMCINTR iShares Russell Mid\-Cap ETF
LBUSTRUU Bloomberg Barclays US Aggregate Bond
IndexRUMRINTR iShares Micro\-Cap ETF
LG30TRUU Bloomberg Barclays Global High Yield
Total Return Index Value UnhedgeRUTPINTR iShares Russell Top 200 ETF
LMBITR Bloomberg Barclays Municipal Bond
Index Total Return Index Value
Unhedged USDS5COND S\&P 500 Consumer Discretionary Index
NDDUE15X Amundi MSCI Europe Ex UK Ucits ETF
DrS5CONS S\&P 500 Consumer Staples Index
NDDUJN MSCI Japan Index S5ENRS S\&P 500 Energy Index
NDDUNA iShares MSCI North America UCITS
ETFS5FINL S\&P 500 Financials Sector GICS Level 1
Index
NDDUPXJ MSCI Pacific ex Japan UCITS ETF S5HLTH S\&P 500 Health Care Index
NDDUUK iShares MSCI UK ETF S5INDU S\&P 500 Industrials Index
NDDUWXUS MSCI World ex USA total net return S5INFT S\&P 500 Information Technology Index
NDUEEGF SPDR MSCI Emerging Markets UCITS
ETFS5MATR S\&P 500 Materials Index
RU10GRTR iShares Russell 1000 Growth ETF S5RLST S\&P 500 Real Estate Index
RU10VATR  iShares Russell 1000 Value ETF S5TELS S\&P 500 Communication Services Index
RU20GRTR  iShares Russell 2000 Growth ETF S5UTIL S\&P 500 Utilities Index
RU20INTR Russell 2000 Total Return SPXT Proshares S\&P 500 EX Technology ETF
32Table 3: Monthly data sets
Name Description Name Description
IBXXSHY1 iShares 0\-5 Year High Yield Corporate
Bond ETFM2USEV MSCI USA Enhanced Value Index
IDCT20RT ICE U.S. Treasury 20\+ Year Bond Total
Return IndexM2USRWGT MSCI USA Risk Weighted Index
LBUSTRUU Bloomberg Barclays US Agg Total Return
Value Unhedged USDM2USSNQ MSCI USA Sector Neutral Quality Index
LC07TRUU Bloomberg Barclays U.S. Universal Total
Return Index Value UnhedgedMID S\&P 400 Mid Cap Index index
LD01TRUU Bloomberg Barclays 1\-3 Yr Credit Total
Return Index Value Unhedged USMXEA MSCI EAFE Index
LT01TRUU Bloomberg Barclays US Treasury 1\-3
Year IndexMXEF MSCI Emerging Markets Index
LUICTRUU Bloomberg Barclays U.S. Intermediate
Credit Total Return IndexMXUSMVOL MSCI USA Minimum Volatility Index
LULCTRUU Bloomberg Barclays U.S. Long Credit
IndexMXWD MSCI All Countries World Index
M1CXBRU iShares Core MSCI International
Developed Markets ETFMXWOUIM MSCI All Countries World Index
M1USMVOL MSCI USA Minimum Volatility (USD)
IndexNDDUUS MSCI Daily Total Return Net USA USD
Index
M2US000$ iShares Edge MSCI USA Momentum
Factor ETFSPX S\&P 500 Index
337 Potentially useful Python and R software implementations: pack\-
ages, codes and frameworks
7\.1 Collections and repositories of resources
For Data Science, Numerical Methods/ Algorithms, Programming
List of links:
•Data Science CheatSheet
•professional\-programming: collection of full\-stack resources for programmers.
For Python
List of links:
•Awesome Python
•Awesome Python frameworks, libraries, software and resources
•Best of Python
•Curated list of Python frameworks, libraries, software and resources
•Pythonidae: Curated decibans of scientific programming resources in Python
•Ranked list of Python open\-source Machine Learning libraries and tools
•Ranked list of Python open\-source libraries and tools
•Ranked list of Python developer tools and libraries
•Time series: analytics, statistics, machine learning, frameworks and databases
•Time series Python packages
For R
List of links:
•Available CRAN Packages By Date of Publication
•CRAN Task Views
7\.2 Connection between Python and R codes
List of links:
•arrow: R interface to ’Apache’ ’Arrow’, a cross\-language for accelerated data interchange in\-memory data
•pyarrow: Python library for Apache Arrow
•reticulate: R Interface to ’Python’ modules, classes, and functions
•rpy2: Python interface to the R language
•rpy2\-arrow: Share Apache Arrow datasets between Python and R
•R Extension for Visual Studio Code
347\.3 Anomaly detection and data outliers
Collections of resources
List of links:
•Anomaly detection related books, papers, videos, and toolboxes
Python software implementations
List of packages and/or codes and/or frameworks and/or links:
•adtk: Python toolkit for rule\-based/unsupervised anomaly detection in time series
•Anomaly Detection Learning Resources
•Awesome anomaly detection resources
•Curve: time series data anomaly detection by Baidu
•kats: kit to analyze time series data by Facebook
•luminaire: ML driven package by Zillow for monitoring time series data
•Merlion: A Machine Learning Framework for Time Series Intelligence by SalesForce
•PyGOD: Graph Outlier Detection (Anomaly Detection)
•PyOD: Python Toolbox for Scalable Outlier Detection (Anomaly Detection)
•PyODDS: An End\-to\-end Outlier Detection System
•ruptures: change point detection in Python
•seriesdistancematrix: implements the Series Distance Matrix framework, a flexible component\-based frame\-
work that bundles various Matrix Profile related techniques
•Software tools and datasets for anomaly detection on time series data
•Tools and datasets for anomaly detection on time\-series data.
•tsad: Time Series Forecasting and Anomaly Detection
•TODS: An Automated Time\-series Outlier Detection System
•tsmoothie: time\-series smoothing and outlier detection
R software implementations
List of packages and/or codes and/or frameworks and/or links:
•amelie: Anomaly Detection with Normal Probability Functions
•ANN2: Artificial Neural Networks for Anomaly Detection
•anomaly: Detecting Anomalies in Data
•AnomalyDetection: package by Twitter to detect anomalies
•anomalize: Tidy Anomaly Detection
•composits: Compositional, Multivariate and Univariate Time Series Outlier Ensemble
•dobin: Dimension Reduction for Outlier Detection
35•dsos: Dataset Shift with Outlier Scores
•HDoutliers: Leland Wilkinson’s Algorithm for Detecting Multidimensional Outliers
•isotree: Isolation\-Based Outlier Detection
•kssa: automatically identify and validate the best method for missing data imputation in a time series
•lookout: Leave One Out Kernel Density Estimates for Outlier Detection
•mvoutlier: Multivariate Outlier Detection Based on Robust Methods
•odetector: Outlier Detection Using Partitioning Clustering Algorithms
•otsad: Online Time Series Anomaly Detectors
•outForest: Multivariate Outlier Detection and Replacement
•outliers: Tests for Outliers
•outliertree: Explainable Outlier Detection Through Decision Tree Conditioning
•stray: Anomaly Detection in High Dimensional and Temporal Data
•TagAnomaly: Anomaly detection analysis and labeling tool by Microsoft
•trendsegmentR: Linear Trend Segmentation and Point Anomaly Detection
•tsoutliers: Detection of Outliers in Time Series
•univOutl: Detection of Univariate Outliers
7\.4 Bayesian analysis and modeling
Python software implementations
List of packages and/or codes and/or frameworks and/or links:
•ArviZ: Exploratory analysis of Bayesian models with Python
•baal: enable Bayesian active learning in your research or labeling work
•bambi: BAyesian Model\-Building Interface (Bambi)
•bilby: Bayesian inference library
•BayesianOptimization: implementation of global optimization with gaussian processes
•BayesTSA: ayesian methods for solving estimation and forecasting problems in time series analysis
•BoTorch: Bayesian optimization in PyTorch
•Bumps: data fitting and uncertainty estimation
•nutpie: A fast sampler for bayesian posteriors
•Orbit: Bayesian forecasting package by Uber
•PyApprox: high\-dimensional approximation and uncertainty quantification
•pyMC: Bayesian Modeling and Probabilistic Machine Learning with Aesara
•PyStan: Python interface to Stan, a platform for statistical modeling
•zeus: Lightning Fast MCMC
36R software implementations
List of packages and/or codes and/or frameworks and/or links:
•ashr: Methods for Adaptive Shrinkage, using Empirical Bayes
•bain: Bayes Factors for Informative Hypotheses (equality, inequality, and about equality constrained hypothe\-
ses)
•bamp: Bayesian Age\-Period\-Cohort Modeling and Prediction
•bsamGP: Bayesian Spectral Analysis Models using Gaussian Process Priors
•bayesdfa: Bayesian Dynamic Factor Analysis (DFA) with ’Stan’
•bayefdr: Bayesian Estimation and Optimisation of Expected False Discovery Rate
•BayesFM: Bayesian Inference for Factor Modeling
•bayesforecast: Bayesian Time Series Modeling with Stan
•BayesHMM: Full Bayesian Inference for Hidden Markov Models
•bayesian: Bindings for Bayesian TidyModels
•bayesmodels: The ’Tidymodels’ Extension for Bayesian Models
•bayesplot: Plotting for Bayesian Models
•BayesPostEst: Generate Postestimation Quantities for Bayesian MCMC Estimation
•bayestestR: Understand and Describe Bayesian Models and Posterior Distributions
•BayesTools: Tools for Bayesian Analyses
•BayesVarSel: Bayes Factors, Model Choice and Variable Selection in Linear Models
•BEST: Bayesian Estimation Supersedes the t\-Test
•beyondWhittle: Bayesian Spectral Inference for Stationary Time Series
•BFpack: Flexible Bayes Factor Testing of Scientific Expectations
•BMAmevt: Multivariate Extremes: Bayesian Estimation of the Spectral Measure
•bmixture: Bayesian Estimation for Finite Mixture of Distributions
•bnmonitor: An Implementation of Sensitivity Analysis in Bayesian Networks
•BNPmix: Bayesian Nonparametric Mixture Models
•bpcs: Bayesian Paired Comparison Analysis with Stan
•bpgmm: Bayesian Model Selection Approach for Parsimonious Gaussian Mixture Models
•brms: Bayesian Regression Models using ’Stan’
•BSL: Bayesian Synthetic Likelihood
•bspec: Bayesian Spectral Inference
•bsvars: Bayesian Estimation of Structural Vector Autoregressive Models
•dalmatian: Automating the Fitting of Double Linear Mixed Models in ’JAGS’ and ’nimble’
•dbnR: Dynamic Bayesian Network Learning and Inference
37•DEBBI: Differential Evolution\-Based Bayesian Inference
•ensembleBMA: Probabilistic Forecasting using Ensembles and Bayesian Model Averaging
•fbst: The Full Bayesian Evidence Test, Full Bayesian Significance Test and the e\-Value
•greta: scalable statistical modelling in R
•LaplacesDemon: Complete Environment for Bayesian Inference
•mBvs: Bayesian Variable Selection Methods for Multivariate Data
•mlr3mbo: Flexible Bayesian Optimization
•mombf: Bayesian Model Selection and Averaging for Non\-Local and Local Priors
•networkABC: Network Reverse Engineering with Approximate Bayesian Computation
•nimble: MCMC, Particle Filtering, and Programmable Hierarchical Modeling
•Nmix: Bayesian Inference on Univariate Normal Mixtures
•posterior: Tools for Working with Posterior Distributions
•rBayesianOptimization: Bayesian Optimization of Hyperparameters
•Rbeast: Bayesian Change\-Point Detection and Time Series Decomposition
•REBayes: Empirical Bayes Estimation and Inference
•Revticulate: Interaction with ”RevBayes” in R
•rstan: R Interface to Stan
•rstanarm: Bayesian Applied Regression Modeling via Stan
•SequenceSpikeSlab: Exact Bayesian Model Selection Methods for the Sparse Normal Sequence Model
•shrinkTVP: Efficient Bayesian Inference for Time\-Varying Parameter Models with Shrinkage
•tidybayes: Tidy Data and ’Geoms’ for Bayesian Models
7\.5 Causality, inference and dependencies
Python software implementations
List of packages and/or codes and/or frameworks and/or links:
•bilby: Bayesian inference library
•CausalDiscoveryToolbox: causal inference in graphs and in the pairwise settings
•causality: Tools for causal analysis
•causalml: package by Uber for Uplift modeling and causal inference with machine learning algorithms
•copulae: Multivariate data modelling with Copulas
•DoWhy: library by Microsoft for causal inference that supports explicit modeling and testing of causal as\-
sumptions
•HiDimStat: High\-dimensional statistical inference tool
•tigramite: time series analysis python module for causal discovery
38R software implementations
List of packages and/or codes and/or frameworks and/or links:
•causal.decomp: Causal Decomposition Analysis
•CausalImpact: toolkit by Google to infer Causal Effects using Bayesian Structural Time\-Series Models
•causaloptim: An Interface to Specify Causal Graphs and Compute Bounds on Causal Effects
•copula: Multivariate Dependence with Copulas
•dCovTS: Distance Covariance and Correlation for Time Series Analysis
•estimatr: Fast Estimators for Design\-Based Inference
•flipr: Flexible Inference via Permutations in R
•generalCorr: Generalized Correlations, Causal Paths and Portfolio Selection
•HellCor: The Hellinger Correlation
•infer: Tidy Statistical Inference
•jackstraw: Statistical Inference for Unsupervised Learning
•konfound: Quantify the Robustness of Causal Inferences
•mashr: Multivariate Adaptive Shrinkage
•multivariance: Measuring Multivariate Dependence Using Distance Multivariance
•NlinTS: Models for Non Linear Causality Detection in Time Series
•NNS: Nonlinear nonparametric statistics using partial moments
•pcalg: Methods for Graphical Models and Causal Inference
•qmd: Quantification of Multivariate Dependence
•rmcfs: The MCFS\-ID Algorithm for Feature Selection and Interdependency Discovery
•sherlock: package by Netflix for causal machine learning for segment discovery and analysis
•SIHR: Statistical Inference in High Dimensional Regression
•tlverse: One Stop to Targeted Learning in R
•tscopula: Time Series Copula Models
•VLTimeCausality: Variable\-Lag Time Series Causality Inference Framework
7\.6 Classification, Motifs, Neighbors, Wavelets, Transforms
Python software implementations
List of packages and/or codes and/or frameworks and/or links:
•abess: Fast Best\-Subset Selection Library
•catboost: Gradient Boosting on Decision Trees by Yandex
•HiClass: hierarchical classification compatible with scikit\-learn
39•LightGBM: fast, distributed, high performance gradient boosting (GBT, GBDT, GBRT, GBM or MART)
framework by Microsoft
•Local Cascade Ensemble (LCE) is a high\-performing, scalable and user\-friendly machine learning method for
the general tasks of Classification and Regression
•matrixprofile: time series data mining tasks, utilizing matrix profile algorithms
•pyts: time series classification
•scikit\-learn: machine learning in Python
•seriesdistancematrix: implements the Series Distance Matrix framework, a flexible component\-based frame\-
work that bundles various Matrix Profile related techniques
•sktime: unified framework for machine learning with time series
•stumpy: modern time series analysis
•tslearn: machine learning toolkit dedicated to time\-series data
R software implementations
List of packages and/or codes and/or frameworks and/or links:
•abess: Fast Best\-Subset Selection Library
•AUC: Threshold Independent Performance Measures for Probabilistic Classifiers
•bcTSNE: Projected t\-SNE for Batch Correction
•biwavelet: Conduct Univariate and Bivariate Wavelet Analyses
•caret: Classification and Regression Training
•classmap: Visualizing Classification Results
•classifly: Explore Classification Models in High Dimensions
•ContaminatedMixt: Clustering and Classification with the Contaminated Normal
•CORElearn: Classification, Regression and Feature Evaluation
•cvms: Cross\-Validation for Model Selection
•ddalpha: Depth\-Based Classification and Calculation of Data Depth
•dtw: Dynamic Time Warping Algorithms
•greed: Clustering and Model Selection with the Integrated Classification Likelihood
•ipred: Improved Predictors
•klaR: Classification and Visualization
•matrixProfile: Matrix Profile
•matrixprofiler: Matrix Profile for R
•mclust: Gaussian Mixture Modelling for Model\-Based Clustering, Classification, and Density Estimation
•MixGHD: Model Based Clustering, Classification and Discriminant Analysis Using the Mixture of Generalized
Hyperbolic Distributions
•MixMatrix: Classification with Matrix Variate Normal and t Distributions
40•mixSPE: Mixtures of Power Exponential and Skew Power Exponential Distributions for Use in Model\-Based
Clustering and Classification
•mixture: Mixture Models for Clustering and Classification
•randomUniformForest: Random Uniform Forests for Classification, Regression and Unsupervised Learning
•rbooster: AdaBoost Framework for Any Classifier
•rebmix: Finite Mixture Modeling, Clustering \& Classification
•regtools: Regression and Classification Tools
•Rmixmod: Classification with Mixture Modelling
•RSSL: Implementations of Semi\-Supervised Learning Approaches for Classification
•Rtsne: T\-Distributed Stochastic Neighbor Embedding using a Barnes\-Hut Implementation
•sbfc: Selective Bayesian Forest Classifier
•SKNN: A Super K\-Nearest Neighbor (SKNN) Classification Algorithm
•stacks: Tidy Model Stacking
•TSMining: Mining Univariate and Multivariate Motifs in Time\-Series Data
•tsmp: Time Series with Matrix Profile
•yardstick: Tidy Characterizations of Model Performance
7\.7 Clustering
Python software implementations
List of packages and/or codes and/or frameworks and/or links:
•cclust: Convex Clustering Methods and Clustering Indexes
•ChronoClust: perform clustering on each of a time\-series of discrete datasets, and explicitly track the evolution
of clusters over time
•classix: Fast and explainable clustering based on sorting
•ClusterEnsembles: package for cluster ensembles
•clustergram: Visualization and diagnostics for cluster analysis in Python
•Clusteval: methods for unsupervised cluster validation
•deeptime: analysis of time series data including dimensionality reduction, clustering, and Markov model
estimation
•dtaidistance: Time series distances: Dynamic Time Warping
•DTCR: Learning Representations for Time Series Clustering
•DTW\_kmedoids: Multivariate time series clustering using Dynamic Time Warping (DTW) and k\-mediods
•ETNA Time Series Library by Tinkoff AI
•faiss: efficient similarity search and clustering of dense vectors
•fastcluster: Fast hierarchical clustering routines
41•genieclust: Fast and Robust Hierarchical Clustering with Noise Point Detection
•hcluster: Hierarchical Clustering Algorithms
•hdbscan: high performance implementation of HDBSCAN clustering
•scikit\-learn: machine learning in Python
•TimeSeriesDeepClustering: End\-to\-end deep representation learning for time series clustering
•tslearn: machine learning toolkit dedicated to time\-series data
•validclust: Validate clustering results
R software implementations
List of packages and/or codes and/or frameworks and/or links:
•apcluster: Affinity Propagation Clustering
•bahc: bahc: Filter Covariance and Correlation Matrices with Bootstrapped\-Averaged Hierarchical Ansatz
•bootcluster: Bootstrapping Estimates of Clustering Stability
•cclust: Convex Clustering Methods and Clustering Indexes
•clue: Cluster Ensembles
•clusrank: Wilcoxon Rank Tests for Clustered Data
•clustAnalytics: Cluster Evaluation on Graphs
•ClustAssess: Tools for Assessing Clustering
•ClustBlock: Hierarchical and partitioning algorithms of blocks of variables
•cluster: ”Finding Groups in Data”: Cluster Analysis Extended Rousseeuw et al.
•clusterability: Performs Tests for Cluster Tendency of a Data Set
•ClusterBootstrap: Analyze Clustered Data with Generalized Linear Models using the Cluster Bootstrap
•Clustering: Techniques for Evaluating Clustering
•clusterSEs: Calculate Cluster\-Robust p\-Values and Confidence Intervals
•ClusterR: Gaussian Mixture Models, K\-Means, Mini\-Batch\-Kmeans, K\-Medoids and Affinity Propagation
Clustering
•clusterSim: Searching for Optimal Clustering Procedure for a Data Set
•clustrd: Methods for Joint Dimension Reduction and Clustering
•clustree: Visualise Clusterings at Different Resolutions
•clValid: Validation of Clustering Results
•cmbClust: Conditional Mixture Modeling and Model\-Based Clustering
•Ckmeans.1d.dp: Optimal, Fast, and Reproducible Univariate Clustering
•diceR: Diverse Cluster Ensemble in R
•dtwclust: Time Series Clustering Along with Optimizations for the Dynamic Time Warping Distance
42•evclust: Evidential Clustering
•fastcluster: Fast Hierarchical Clustering Routines for R and ’Python’
•fastkmedoids: Faster K\-Medoids Clustering Algorithms: FastPAM, FastCLARA, FastCLARANS
•FCPS: Fundamental Clustering Problems Suite
•flexclust: Flexible Cluster Algorithms
•fpc: Flexible Procedures for Clustering
•genie: Fast, Robust, and Outlier Resistant Hierarchical Clustering
•genieclust: The Genie\+\+ Hierarchical Clustering Algorithm with Noise Points Detection
•heatmaply: Interactive Cluster Heat Maps Using ’plotly’ and ’ggplot2’
•HierPortfolios: Hierarchical Clustering\-Based Portfolio Allocation Strategies
•htestClust: Reweighted Marginal Hypothesis Tests for Clustered Data
•kselection: Selection of K in K\-Means Clustering
•l1spectral: An L1\-Version of the Spectral Clustering
•leaderCluster: Leader Clustering Algorithm
•LearnClust: Learning Hierarchical Clustering Algorithms
•MatTransMix: Clustering with Matrix Gaussian and Matrix Transformation Mixture Models
•mclust: Gaussian Mixture Modelling for Model\-Based Clustering, Classification, and Density Estimation
•mclustcomp: Measures for Comparing Clusters
•mdendro: Extended Agglomerative Hierarchical Clustering
•Mercator: Clustering and Visualizing Distance Matrices
•MixGHD: Model Based Clustering, Classification and Discriminant Analysis Using the Mixture of Generalized
Hyperbolic Distributions
•MixSim: Simulating Data to Study Performance of Clustering Algorithms
•mixSPE: Mixtures of Power Exponential and Skew Power Exponential Distributions for Use in Model\-Based
Clustering and Classification
•mixture: Mixture Models for Clustering and Classification
•MKMeans: A Modern K\-Means (MKMeans) Clustering Algorithm
•mlr3cluster: Cluster Extension for ’mlr3’
•motifcluster: Motif\-Based Spectral Clustering of Weighted Directed Networks
•MSclust: Multiple\-Scaled Clustering
•mstknnclust: MST\-kNN Clustering Algorithm
•NNS: Nonlinear nonparametric statistics using partial moments
•ProjectionBasedClustering: Projection Based Clustering
•protoclust: Hierarchical Clustering with Prototypes
43•pytorch\_cluster: PyTorch Extension Library of Optimized Graph Cluster Algorithms
•QuClu: Quantile\-Based Clustering Algorithms
•rebmix: Finite Mixture Modeling, Clustering \& Classification
•RCTS: Clustering Time Series While Resisting Outliers
•RMBC: Robust Model Based Clustering
•sClust: R Toolbox for Unsupervised Spectral Clustering
•sigclust: Statistical Significance of Clustering
•SLBDD: Statistical Learning for Big Dependent Data
•Spectrum: Fast Adaptive Spectral Clustering for Single and Multi\-View Data
•T4cluster: Tools for Cluster Analysis
•tclust: Robust Trimmed Clustering
•tglkmeans: Efficient Implementation of K\-Means\+\+ Algorithm
•TSclust: Time Series Clustering Utilities
•vimpclust: Variable Importance in Clustering
7\.8 Coding utilities and frameworks
Python software implementations
List of packages and/or codes and/or frameworks and/or links:
•Algviz is an algorithm visualization tool for your Python code
•asteval: minimalistic evaluator of python expression using ast module
•autoflake: Removes unused imports and unused variables as reported by pyflakes
•autopep8: automatically formats Python code to conform to the PEP 8 style guide
•autoray: Write numeric code that automatically works with any numpy\-ish libraries
•bandit: find common security issues in Python code
•birdseye: Graphical debugger to view the values of all evaluated expressions
•black: uncompromising Python code formatter
•BLUE: The slightly less uncompromising Python code formatter
•Bowler: Safe code refactoring by Facebook for modern Python
•Comprehensive Python Cheatsheet
•conda\-deps: Generate conda environment files from Python and R source code
•Crashtest is a Python library that makes exceptions handling and inspection easier.
•darker: Apply black reformatting to Python files only in regions changed since a given commit
•enum\_tools: Tools to expand Python’s enum module.
•erdantic: tool for drawing entity relationship diagrams (ERDs) for Python data model classes.
44•flake8: glues together pycodestyle, pyflakes, mccabe, and third\-party plugins to check the style and quality of
code
•flake8\-black: flake8 plugin to run black for checking Python coding style
•friendly: replaces standard tracebacks by something easier to understand
•Hatch is a modern, extensible Python project manager.
•icecream: Never use print() to debug again
•ipdb: exports functions to access the IPython debugger
•isort: utility / library to sort imports
•jedi: autocompletion, static analysis and refactoring library
•jsonschema: implementation of the JSON Schema specification for Python
•kedro: framework for creating reproducible, maintainable and modular data science code
•kedro\-viz: Visualise your Kedro data and machine\-learning pipelines and track your experiments.
•libfyaml: Fully feature complete YAML parser and emitter
•luddite: Checks for out\-of\-date package versions
•makepackage: easy packaging of Python code
•mamba: Fast Cross\-Platform Package Manager (reimplementation of the conda package manager in C\+\+)
•memray: memory profiler for Python
•metaflow: build and manage real\-life data science projects
•mkdocs: Project documentation with Markdown
•mkdocs\-material: Technical documentation that just works
•MonkeyType: toolkit by Instagram to generate static type annotations by collecting runtime types
•Monty: supplementary useful functions for Python that are not part of the standard library
•mypy: Optional static typing for Python
•nptyping: Type hints for Numpy
•numpydoc: Numpy’s Sphinx extensions
•pdbpp: a drop\-in replacement for pdb (the Python debugger)
•PlantUML: Generate UML diagram from textual description
•poetry: dependency management and packaging made easy
•Pretty\_Errors: Prettify Python exception output to make it legible
•prospector: Inspects source files and provides information about type and location of classes, methods
•ptvsd: debugger package by Microsoft for use with Visual Studio and Visual Studio Code
•pudb: Full\-screen console debugger for Python
•pyan: Static call graph generator
•pycodestyle: Simple Python style checker
45•pydantic: Data parsing and validation using Python type hints
•pyDeprecate: tooling for marking deprecated functions or classes and re\-routing to the new successors’ in\-
stance.
•pyflakes: checks Python source files for errors
•pylint: static code analysis tool
•pyquickhelper: automation of many things
•pyre: framework for building scientific applications in Python
•pyre\-check: Performant type\-checking toolkit by Facebook
•pyright: Static type checker by Microsoft
•PyScaffold: Python project template generator with batteries included
•PySnooper: Never use print for debugging again
•py\-spy: Sampling profiler for Python programs
•pytools: a big bag of things that are ”missing” from the Python standard library
•pytype: static type analyzer by Google
•radon: tool that computes various metrics from the source code
•rope: refactoring library
•scalene: high\-performance, high\-precision CPU, GPU, and memory profiler for Python
•sphinx: Sphinx documentation builder
•StrictYAML is a type\-safe YAML parser that parses and validates a restricted subset of the YAML specification
•tryceratops: linter to prevent exception handling antipatterns in Python
•typeguard: Run\-time type checker for Python
•TypePigeon: type converter focused on converting values between various Python data types.
•varname:Dark magics about variable names in python
•vulture: Find dead Python code
•xlwings: ibrary that makes it easy to call Python from Excel and vice versa
•yapf: formatter by Google for Python files
•yappi: Yet Another Python Profiler, but this time multithreading, asyncio and gevent aware.
46R software implementations
List of packages and/or codes and/or frameworks and/or links:
•adaptalint: Check Code Style Painlessly
•baguette: Efficient Model Functions for Bagging
•box: Write Reusable, Composable and Modular R Code
•butcher: Model Butcher: axe components of fitted model objects and help reduce the size of model objects
saved to disk
•cartbonate: Create beautiful images of source code using ’carbon.js
•checkmate: Fast and Versatile Argument Checks
•checkpoint: Install Packages from Snapshots on the Checkpoint Server for Reproducibility
•cleanr: Helps You to Code Cleaner
•delayed: A Framework for Parallelizing Dependent Tasks
•goodpractice: Advice on R Package Building
•hardhat: Construct Modeling Packages
•IRdisplay: ’Jupyter’ Display Machinery
•IRkernel: Native R Kernel for the ’Jupyter Notebook’
•jetpack: A Friendly Package Manager
•leprechaun: Create Simple ’Shiny’ Applications as Packages
•lintr: A ’Linter’ for R Code
•lvec: Out of Memory Vectors
•memuse: Memory Estimation Utilities
•metaflow: build and manage real\-life data science projects
•miniCRAN: Create a Mini Version of CRAN Containing Only Selected Packages
•mongolite: Fast and Simple ’MongoDB’ Client for R
•packager: Create, Build and Maintain Packages
•parsnip: A Common API to Modeling and Analysis Functions
•prettifyAddins: ’RStudio’ Addins to Prettify ’JavaScript’, ’C\+\+’, ’Python’, and More
•R6: Encapsulated Classes with Reference Semantics
•R6P: Design Patterns in R
•recipes: Preprocessing and Feature Engineering Steps for Modeling
•renv: Project Environments
•rhino: A Framework for Enterprise Shiny Applications
•roxut: Document Unit Tests Roxygen\-Style
•roxygen2: In\-Line Documentation for R
47•rstudio.prefs: Set ’RStudio’ Preferences
•tidymodules: obust framework for developing ‘Shiny’ modules based on R6 classes which should facilitates
inter\-modules communication.
•waldo: Find Differences Between R Objects
•vetiver: Version, Share, Deploy, and Monitor Models
•workflows: Modeling Workflows
•workflowsets: Create a Collection of ’tidymodels’ Workflows
7\.9 Computational performance
Python software implementations
List of packages and/or codes and/or frameworks and/or links:
•Aesara: definie, optimize, and efficiently evaluate mathematical expressions involving multi\-dimensional ar\-
rays.
•arctic: High performance datastore by Man Group for time series and tick data
•bottleneck: Fast NumPy array functions written in C
•Dask: Parallel computing with task scheduling
•Dask\-ML provides scalable machine learning in Python using Dask alongside popular machine learning libraries
•datatable: library for fast multi\-threaded data manipulation and munging
•fairscale: PyTorch extensions for high performance and large scale training.
•fastcore: Python supercharged for the fastai library
•hypre: high performance preconditioners
•jax: automatically differentiate native Python and NumPy functions
•modin: ake your pandas code run faster by changing one line of code
•multiprocess: better multiprocessing and multithreading in python
•numexpr: Fast numerical expression evaluator for NumPy
•PandaPy: speed of NumPy and the usability of Pandas but much faster
•pandarallel: parallelize Pandas operations on all available CPUs
•pandasvault:Advanced Pandas Vault \- Utilities, Functions and Snippets
•polars: Fast multi\-threaded DataFrame library
•ppft: distributed and parallel python
•PyArma: Linear algebra library for Python
•PyArmadillo: an alternative approach to linear algebra in Python
•pyperf: Toolkit to run Python benchmarks
•pyperformance: Python Performance Benchmark Suite
•py\-spy: Sampling profiler for Python programs
48•scalene: high\-performance, high\-precision CPU, GPU, and memory profiler for Python
•swifter: efficiently applies any function to a pandas dataframe or series in the fastest available manner
•tempeh is a framework to TEst Machine learning PErformance exHaustively which includes tracking memory
usage and run time.
R software implementations
List of packages and/or codes and/or frameworks and/or links:
•collapse: Advanced and Fast Data Transformation
•dataPreparation: Automated Data Preparation
•delayed: A Framework for Parallelizing Dependent Tasks
•dplyr: A Grammar of Data Manipulation
•MatrixStats: Methods that Apply to Rows and Columns of Matrices (and to Vectors)
•mirai: Minimalist Async Evaluation Framework for R
•purrr: Functional Programming Tools
•tidyverse: set of packages that work in harmony because they share common data representations and ’API’
design
•timetk: A Tool Kit for Working with Time Series in R
•tibble: Simple Data Frames
•tidytidbits: A Collection of Tools and Helpers Extending the Tidyverse
•tsibble: Tidy Temporal Data Frames and Tools
7\.10 Containers, projects, pipelines and deployment
Python software implementations
List of packages and/or codes and/or frameworks and/or links:
•Driblet \- Google Cloud based ML pipeline by Google
•MLflow: A Machine Learning Lifecycle Platform
•metaflow: Python/R library by Netflix to build and manage real\-life data science projects
•mlflow: Interface to ’MLflow’
•mlxtend: extension and helper modules for data analysis and machine learning libraries
•NNI: toolkit by Microsoft to help users automate Feature Engineering, Neural Architecture Search, Hyperpa\-
rameter Tuning and Model Compression
•petastorm: toolkit by Uber for single machine or distributed training and evaluation of deep learning models
(Tensorflow, Pytorch, and PySpark) from datasets in Apache Parquet format
•pipelines: Machine Learning Pipelines for Kubeflow
•Prefect: second\-generation dataflow coordination and orchestration platform
•PyTorch Lightning: The lightweight PyTorch wrapper for high performance AI research
•Tango: toolkit by Allen Institute of Articial Intelligence for choreographing machine learning research
49R software implementations
List of packages and/or codes and/or frameworks and/or links:
•DriveML: Self\-Drive Machine Learning Projects
•metaflow: Python/R library by Netflix to build and manage real\-life data science projects
•mlflow: Interface to ’MLflow’
7\.11 Covariances, correlations and volatilities
Python software implementations
List of packages and/or codes and/or frameworks and/or links:
•numpy: scientific computing
•precise: online covariance and precision forecasting, portfolios, and model ensembles
•PyPortfolioOpt: Financial portfolio optimization
•sklearn.covariance: covariance estimation in scikit\-learn
•statsmodels: statistical modeling and econometrics
R software implementations
List of packages and/or codes and/or frameworks and/or links:
•bahc: Filter Covariance and Correlation Matrices with Bootstrapped\-Averaged Hierarchical Ansatz
•BBcor: Bayesian Bootstrapping Correlations
•BEKKs: Multivariate Conditional Volatility Modelling and Forecasting
•BSCOV: Detection of Multiple Structural Breaks in Large Covariance Matrices
•clubSandwich: Cluster\-Robust (Sandwich) Variance Estimators with Small\-Sample Corrections
•cocor: Comparing Correlations
•corpcor: Efficient Estimation of Covariance and (Partial) Correlation
•correlation: Methods for Correlation Analysis
•corx: Create and Format Correlation Matrices
•CovTools: Statistical Tools for Covariance Analysis
•cvCovEst: Cross\-Validated Covariance Matrix Estimation
•dcortools: Providing Fast and Flexible Functions for Distance Correlation Analysis
•dCovTS: Distance Covariance and Correlation for Time Series Analysis
•fitHeavyTail: Mean and Covariance Matrix Estimation under Heavy Tails
•FRCC: Fast Regularized Canonical Correlation Analysis
•gencor: Generate Customized Correlation Matrices
•generalCorr: Generalized Correlations, Causal Paths and Portfolio Selection
•mashr: Multivariate Adaptive Shrinkage
50•MatrixCorrelation: Matrix Correlation Coefficients
•MTS: All\-Purpose Toolkit for Analyzing Multivariate Time Series (MTS) and Estimating Multivariate Volatil\-
ity Models
•NonParRolCor: a Non\-Parametric Statistical Significance Test for Rolling Window Correlation
•NNS: Nonlinear nonparametric statistics using partial moments
•rags2ridges: Ridge Estimation of Precision Matrices from High\-Dimensional Data
•rmcorr: Repeated Measures Correlation
•robcor: Robust Correlations
•robustcov: Collection of Robust Covariance and (Sparse) Precision Matrix Estimators
•RSC: Robust and Sparse Correlation Matrix
•sandwich: Robust Covariance Matrix Estimators
•WGCNA: Weighted Correlation Network Analysis
7\.12 Data analysis and exploration
Python software implementations
List of packages and/or codes and/or frameworks and/or links:
•AutoViz: Automatically Visualize any dataset, any size with a single line of code.
•daal4py: simplified API to Intel oneAPI Data Analytics Library
•DeepGraph: scalable, general\-purpose data analysis with Pandas\-based Networks
•D\-tale:Visualizer by Man Group for pandas data structures
•dython: Data analysis tools
•empiricaldist: empirical distribution functions
•hyperspy: Multidimensional data analysis
•Lux: automate the visualization and data analysis process
•mlxtend: extension and helper modules for Python’s data analysis and machine learning libraries.
•numericalunits: Units and dimensional analysis compatible with everything
•Orange: Interactive data analysis
•pandas\-profiling: Create HTML profiling reports from pandas DataFrame objects
•PyApprox: high\-dimensional approximation and uncertainty quantification
•sweetviz: Visualize and compare datasets, target values and associations
51R software implementations
List of packages and/or codes and/or frameworks and/or links:
•checkmate: Fast and Versatile Argument Checks
•collapse: Advanced and Fast Data Transformation
•datacleanr: Interactive and Reproducible Data Cleaning
•DataEditR: An Interactive Editor for Viewing, Entering, Filtering \& Editing Data
•DataExplorer: Automate Data Exploration and Treatment
•datamods: Modules to Import and Manipulate Data in ’Shiny’
•dataprep: Efficient and Flexible Data Preprocessing Tools
•DataVisualizations: Visualizations of High\-Dimensional Data
•datawizard: Easy Data Wrangling
•DescTools: Tools for Descriptive Statistics
•dimensio: Multivariate Data Analysis
•discoveR: Exploratory Data Analysis System
•dlookr: Tools for Data Diagnosis, Exploration, Transformation
•EasyDescribe: A Convenient Way of Descriptive Statistics
•esquisse: Explore and Visualize Your Data Interactively
•explor: Interactive Interfaces for Results Exploration
•exploratory: A Tool for Large\-Scale Exploratory Analyses
•explore: Simplifies Exploratory Data Analysis
•factoextra: extract and visualize the output of multivariate data analyses, including ’PCA’ (Principal Compo\-
nent Analysis), ’CA’ (Correspondence Analysis), ’MCA’ (Multiple Correspondence Analysis), ’FAMD’ (Factor
Analysis of Mixed Data), ’MFA’ (Multiple Factor Analysis) and ’HMFA’ (Hierarchical Multiple Factor Anal\-
ysis)
•FactoInvestigate: Automatic Description of Factorial Analysis
•FactoMineR: Multivariate Exploratory Data Analysis and Data Mining
•ggESDA: Exploratory Symbolic Data Analysis with ’ggplot2’
•HDTSA: High Dimensional Time Series Analysis Tools
•infotheo: Information\-Theoretic Measures
•kfa: K\-Fold Cross Validation for Factor Analysis
•MazamaRollUtils: Efficient Rolling Functions
•mmpca: Integrative Analysis of Several Related Data Matrices
•praznik: Tools for Information\-Based Feature Selection and Scoring
•predictoR: Predictive Data Analysis System
52•rigr: Regression, Inference, and General Data Analysis Tools in R
•robCompositions: Compositional Data Analysis
•rrcov: Scalable Robust Estimators with High Breakdown Point
•SmartEDA: Summarize and Explore the Data
•statsExpressions: Tidy Dataframes and Expressions with Statistical Details
•Statsomat: Shiny Apps for Automated Data Analysis and Automated Interpretation
•thinkr: Tools for Cleaning Up Messy Files
•tswge: Time Series for Data Science.Accompanies the texts Time Series for Data Science and Applied Time
Series Analysis with R,
•validata: Validate Data Frames
•validate: Data Validation Infrastructure
•validatetools: Checking and Simplifying Validation Rule Sets
•wrangle: A Systematic Data Wrangling Idiom
7\.13 Data augmentation, scenario generation and synthetic time series
Collections of resources
List of links:
•Synthetic data generation by Van Der Schaar Lab
•Useful data augmentation resources
Python software implementations
List of packages and/or codes and/or frameworks and/or links:
•agots: Anomaly Generator on Time Series
•benchmark\_VAE: Unifying Generative Autoencoder implementations in Python
•Copulas: model multivariate data using copulas
•CTGAN: Conditional GAN for Tabular Data
•COMET Flows: Towards Generative Modeling of Multivariate Extremes and Tail Dependence
•DataGeneration: Synthetic financial correlation matrix and time series generation
•DECAF: Generating Fair Synthetic Data Using Causally\-Aware Generative Networks
•DeepEcho: Synthetic Data Generation for mixed\-type, multivariate time series
•deltapy: Tabular Data Augmentation
•extremeIndex: Forecast Verification for Extreme Events
•ixmp: platform for integrated and cross\-cutting scenario analysis
•MLlforHealthLab: Machine Learning and Artificial Intelligence for Medicine
•pydantic\-factories: Pydantic based mock data generation
53•pythae: Unifying Generative Autoencoder implementations in Python
•RDT: Reversible Data Transforms to reproduce realistic data
•scattering\_covariance: analysis and generation of time series
•SDMetrics: Metrics for Synthetic Data Generation Projects
•SDGym: Benchmarking synthetic data generation methods
•SDV: Synthetic Data Generation for tabular, relational and time series data
•SignalFilters: Signal Filtering and Generation of Synthetic Time\-Series
•snorkel: system for quickly generating training data with weak supervision
•synthia: Multidimensional synthetic data generation in Python
•TGAN: Generative adversarial training for generating synthetic tabular data
•TimeGAN: Time\-series Generative Adversarial Networks
•time\-series\-generator: Time Series Generator
•TimeSynth: Synthetic Time Series Generation
•tsaug: time series augmentation
•tsBNgen: Generate Time Series Data Based on an Arbitrary Bayesian Network Structure
•tsGAN: Time\-series Generative Adversarial Networks
•ydata\-synthetic: Synthetic structured data generators
R software implementations
List of packages and/or codes and/or frameworks and/or links:
•anySim: Simulation of Non\-Gaussian Correlated Random Variables, Stochastic Processes and Random Fields
•bootComb: Combine Parameter Estimates via Parametric Bootstrap
•conjurer: A Parametric Method for Generating Synthetic Data
•covsim: VITA, IG and PLSIM Simulation for Given Covariance and Marginals
•fabricatr: Imagine Your Data Before You Collect It
•fwb: Fractional Weighted Bootstrap
•gencor: Generate Customized Correlation Matrices
•gratis: Generating Time Series with Diverse and Controllable Characteristics
•meboot: Maximum Entropy Bootstrap for Time Series
•metamer: Create Data with Identical Statistics
•missMethods: Methods for Missing Data
•MixSim: Simulating Data to Study Performance of Clustering Algorithms
•modeltime.resample: Resampling Tools for Time Series Forecasting
•MonteCarlo: Automatic Parallelized Monte Carlo Simulations
54•MSCMT: Multivariate Synthetic Control Method Using Time Series
•mvlognCorrEst: Sampling from Multivariate Lognormal Distributions and Estimating Correlations from Un\-
complete Correlation Matrix
•naive: Empirical Extrapolation of Time Feature Patterns
•RMT4DS: Computation of Random Matrix Models
•rsample: General Resampling Infrastructure
•segen: Sequence Generalization Through Similarity Network
•SimJoint: Simulate Joint Distribution
•simmer: Discrete\-Event Simulation for R
•simts: Time Series Analysis Tools
•spooky: Time Feature Extrapolation Using Spectral Analysis and Jack\-Knife Resampling
•Synth: Synthetic Control Group Method for Comparative Case Studies
•synthesis: Generate Synthetic Data from Statistical Models
•tetragon: Automatic Sequence Prediction by Expansion of the Distance Matrix
•TidyDensity: Functions for Tidy Analysis and Generation of Random Data
•tscopula: Time Series Copula Models
7\.14 Data cleaning, preparation and validation
Python software implementations
List of packages and/or codes and/or frameworks and/or links:
•cerberus: Lightweight, extensible data validation library
•datatest: Tools for test driven data\-wrangling and data validation
•doubtlab: Doubt your data, find bad labels
•framework: Data management framework for Python that provides functionality to describe, extract, validate,
and transform tabular data
•formencode: validation and form generation
•pandera: perform data validation on dataframes
•pydantic: Data parsing and validation using Python type hints
•pyjanitor: Clean APIs for data cleaning. Python implementation of R package Janitor
•PyOptimus: framework for cleaning and pre\-processing data in a distributed fashion
•scikit\-learn: machine learning in Python
•schema: library for validating Python data structures
•serde: framework for defining, serializing, deserializing, and validating data structures
•typical: Fast, simple, \& correct data\-validation using Python 3 typing.
•validators: Python data validation for Humans
55•Voluptuous: data validation library.
•validr: simple, fast, extensible python library for data validation
•wtforms: flexible forms validation and rendering library
R software implementations
List of packages and/or codes and/or frameworks and/or links:
•cleanTS: Testbench for Univariate Time Series Cleaning
•dataPreparation: Automated Data Preparation
•data.validator: Automatic Data Validation and Reporting
•datawizard: Easy Data Wrangling
•errorlocate: Locate Errors with Validation Rules
•pointblank: Data Validation and Organization of Metadata for Local and Remote Tables
•testdat: Data Unit Testing for R
•tsrobprep: Robust Preprocessing of Time Series Data
•validate: Data Validation Infrastructure
•validatetools: Checking and Simplifying Validation Rule Sets
•wrangle: A Systematic Data Wrangling Idiom
7\.15 Data Imputation
Python software implementations
List of packages and/or codes and/or frameworks and/or links:
•AutoImpute: Imputation Methods
•Clairvoyance: a Unified, End\-to\-End AutoML Pipeline for Medical Time Series
•fancyimpute: Multivariate imputation and matrix completion algorithms
•HyperImpute: framework for prototyping and benchmarking imputation methods
•imputena: automated and customized treatment of missing values in datasets
•miceforest: Fast, Memory Efficient Imputation with LightGBM
•MissForestExtra: nonparametric imputation on missing values
•scikit\-learn: machine learning in Python
•statsmodels: statistical modeling and econometrics
•tsai: time series tasks like classification, regression, forecasting, imputation
56R software implementations
List of packages and/or codes and/or frameworks and/or links:
•Amelia: A Program for Missing Data
•CoImp: Copula Based Imputation Method
•deductive: Data Correction and Imputation Using Deductive Methods
•ggmice: Visualizations for ’mice’ with ’ggplot2’
•howManyImputations: Calculate How many Imputations are Needed for Multiple Imputation
•imputeFin: Imputation of Financial Time Series with Missing Values and/or Outliers
•imputeGeneric: Ease the Implementation of Imputation Methods
•imputeTestbench: Test Bench for the Comparison of Imputation Methods
•imputeTS: Time Series Missing Value Imputation
•Iscores: Proper Scoring Rules for Missing Value Imputation
•mdgc: Missing Data Imputation Using Gaussian Copulas
•mice: Multivariate Imputation by Chained Equations
•miceadds: Some Additional Multiple Imputation Functions, Especially for ’mice’
•miceafter: Data and Statistical Analyses after Multiple Imputation
•miceFast: Fast Imputations Using ’Rcpp’ and ’Armadillo’
•micemd: Multiple Imputation by Chained Equations with Multilevel Data
•misPRIME: Partial Replacement Imputation Estimation for Missing Covariates
•missMDA: Handling Missing Values with Multivariate Data Analysis
•missMethods: Methods for Missing Data
•missRanger: Fast Imputation of Missing Values
•mlim: Multiple Imputation with Automated Machine Learning
•NADIA: NA Data Imputation Algorithms
•naniar: Data Structures, Summaries, and Visualisations for Missing Data
•rego: Automatic Time Series Forecasting and Missing Value Imputation
•Rforestry: Random Forests, Linear Trees, and Gradient Boosting for Inference and Interpretability
•simputation: Simple Imputation
•SLBDD: Statistical Learning for Big Dependent Data
•smcfcs: Multiple Imputation of Covariates by Substantive Model Compatible Fully Conditional Specification
•univOutl: Detection of Univariate Outliers
•VIM: Visualization and Imputation of Missing Values
•yaImpute: Nearest Neighbor Observation Imputation and Evaluation Tools
577\.16 Data regimes, states and changepoints: analysis and modeling
Collections of resources
List of links:
•Classifying market regimes
•TCPD: toolkit by UK national institute for data science and artificial intelligence for Turing Change Point
Dataset \- A collection of time series for the evaluation and development of change point detection algorithms
•TCPDBench: toolkit by UK national institute for data science and artificial intelligence for Turing Change
Point Detection Benchmark: An Extensive Benchmark Evaluation of Change Point Detection Algorithms on
real\-world data
Python software implementations
List of packages and/or codes and/or frameworks and/or links:
•changeforest: Random Forests for Change Point Detection
•deeptime: analysis of time series data including dimensionality reduction, clustering, and Markov model
estimation
•greykite: flexible, intuitive and fast forecasting library
•HMMLearn: Hidden Markov Models in Python with scikit\-learn like API
•kalmanfilter: Kalman Filter
•kats: tookit by Facebook for time series analysis and forecasting
•kimfilter: Rcpp’ implementation of the multivariate Kim filter, which combines the Kalman and Hamilton
filters for state probability inference
•Merlion: A Machine Learning Framework for Time Series Intelligence by SalesForce
•msmtools: estimation and analysis of discrete state space Markov chains via Markov state models (MSM)
•PyEMMA: Emma’s Markov Model Algorithms
•pyGPCCA: Generalized Perron Cluster Cluster Analysis to coarse\-grain reversible and non\-reversible Markov
state models.
•pyhsmm: Bayesian inference in HSMMs and HMMs
•pymc3\-hmm: Hidden Markov models in PyMC3
•ruptures: change point detection
•SST: fast implementation of Singular Spectrum Transformation
•Stone\-Soup: framework for the development and testing of tracking algorithms
•statsmodels: Markov switching models in statsmodels
•transitionMatrix: Statistical analysis and visualization of state transition phenomena
•tsmoothie: time\-series smoothing and outlier detection
58R software implementations
List of packages and/or codes and/or frameworks and/or links:
•BayesHMM: Full Bayesian Inference for Hidden Markov Models
•breakfast: Methods for Fast Multiple Change\-Point Detection and Estimation
•BSCOV: Detection of Multiple Structural Breaks in Large Covariance Matrices
•ChangepointInference: Tools to test for a change in mean after changepoint detection
•changepoints: A Collection of Change\-Point Detection Methods
•ChangePointTaylor: Identify Changes in Mean
•chngpt: Estimation and Hypothesis Testing for Threshold Regression
•cpss: Change\-Point Detection by Sample\-Splitting Methods
•crossvalidationCP: Cross\-Validation for Change\-Point Regression
•depmixS4: Dependent Mixture Models \- Hidden Markov Models of GLMs and Other Distributions in S4
•dynr: Dynamic Models with Regime\-Switching
•earlywarnings: Early Warning Signals Toolbox for Detecting Critical Transitions in Timeseries
•fabisearch: Change Point Detection in High\-Dimensional Time Series Networks
•fHMM: Fitting Hidden Markov Models to Financial Data
•inflection: Finds the Inflection Point of a Curve
•InspectChangepoint: High\-Dimensional Changepoint Estimation via Sparse Projection
•jcp: Joint Change Point Detection
•HMM: Hidden Markov Models
•hmm.discnp: Hidden Markov Models with Discrete Non\-Parametric Observation Distributions
•hmmr: ”Mixture and Hidden Markov Models with R” Datasets and Example Code
•KFAS: Kalman Filter and Smoother for Exponential Family State Space Models
•ldhmm: Hidden Markov Model for Financial Time\-Series Based on Lambda Distribution
•mHMMbayes: Multilevel Hidden Markov Models Using Bayesian Estimation
•MSGARCH: Markov\-Switching GARCH Models
•MSTest: Hypothesis Testing for Markov Switching Models
•NHMSAR: Non\-Homogeneous Markov Switching Autoregressive Models
•onlineBcp: Online Bayesian Methods for Change Point Analysis
•plotHMM: Plot Hidden Markov Models
•pomp: Statistical Inference for Partially Observed Markov Processes
•Rbeast: Bayesian Change\-Point Detection and Time Series Decomposition
•RChest: Locating Distributional Changes in Highly Dependent Time Series
59•robcp: Robust Change\-Point Tests
•segmented: Regression Models with Break\-Points / Change\-Points Estimation
•seqHMM: Mixture Hidden Markov Models for Social Sequence Data and Other Multivariate, Multichannel
Categorical Time Series
•trendchange: Innovative Trend Analysis and Time\-Series Change Point Analysis
•tsDyn: Nonlinear Time Series Models with Regime Switching
•wbsts: Multiple Change\-Point Detection for Nonstationary Time Series
7\.17 Data structures, storage and serialization
Python software implementations
List of packages and/or codes and/or frameworks and/or links:
•addict: Python Dict
•anndata: package for handling annotated data matrices in memory and on disk
•arctic: High performance datastore by Man Group for time series and tick data
•cloudpickle: serialize Python constructs not supported by the default pickle module
•dataclassy is a reimplementation of data classes in Python
•datatable: fast multi\-threaded data manipulation and munging
•dill: extends Python’s pickle module for serializing and deserializing python objects to the majority of the
built\-in python types.
•extendedjson: Easily extend JSON to encode and decode arbitrary Python objects
•framework: Data management framework for Python that provides functionality to describe, extract, validate,
and transform tabular data
•MarketStore: DataFrame Server for Financial Timeseries Data
•marshmallow: lightweight library for converting complex objects to and from simple Python datatypes
•modin.pandas DataFrame is a parallel and distributed drop\-in replacement for panda
•Mongita is to MongoDB as SQLite is to SQL
•mongo\-arrow: Tools for using Apache Arrow with MongoDB
•multidict: multidict implementation
•Odo provides a uniform API for moving data between different formats
•pandas: data structures for data analysis, time series, and statistics
•pandasvault: Advanced Pandas Vault \- Utilities, Functions and Snippets
•pickle: Python object serialization
•polars: Fast multi\-threaded DataFrame library
•pyarrow: Python API for Apache Arrow, a language independent columnar memory format for flat and
hierarchical data
60•PyMongo \- the Python driver for MongoDB
•PyStore: Fast data store for Pandas time\-series data
•PyTables: package for managing hierarchical datasets
•rpy2\-arrow: Share Apache Arrow datasets between Python and R
•serde: framework for defining, serializing, deserializing, and validating data structures
•sklearn\-pandas: bridge between Scikit\-Learn’s machine learning methods and pandas\-style Data Frames
•sortedcontainers: Sorted Containers – Sorted List, Sorted Dict, Sorted Set
•sqlite: Persistent dict, backed by sqlite3 and pickle, multithread\-safe.
•sparse: Sparse Multidimensional Arrays
•srsly: Modern high performance serialization utilities
•tablib: Module for Tabular Datasets in XLS, CSV, JSON, YAML,
•tabmat: Efficient matrix representations for working with tabular data
•TileDB: powerful engine for storing and accessing dense and sparse multi\-dimensional arrays
•tidypandas: grammar of data manipulation for pandas inspired by tidyverse
•tinyarray: Tinyarrays are similar to NumPy arrays, but optimized to be much faster for small sizes
•TinyDB is a lightweight document oriented database optimized for your happiness
•tinyflux: iny time series database optimized for your happiness
•torcharrow: torch.Tensor\-like DataFrame library by Facebook using Arrow as a common memory format
•ubermagtable: package for manipulating tabular data
•ultrajson: Ultra fast JSON decoder and encoder written in C with Python bindings
•Vector: arrays of 2D, 3D, and Lorentz vectors
•Woodwork is a Python library that provides robust methods for managing and communicating data typing
information
•xarray: multidimensional labeled arrays and datasets
•xpandas: Universal 1d/2d data containers with Transformers functionality for data analysis
R software implementations
List of packages and/or codes and/or frameworks and/or links:
•arrow: Integration to Apache Arrow
•dibble: Dimensional Data Frames
•fst: Lightning Fast Serialization of Data Frames
•gluedown: Wrap Vectors in Markdown Formatting
•listdown: Create R Markdown from Lists
•motifcluster: Motif\-Based Spectral Clustering of Weighted Directed Networks
61•qs: Quick Serialization of R Objects
•RcppSimdJson: ’Rcpp’ Bindings for the ’simdjson’ Header\-Only Library for ’JSON’ Parsing
•tibble: stricter checking and better formatting than the traditional data frame
•tibblify: Rectangle Nested Lists
•tidytable: Tidy Interface to ’data.table’
•tiledb: Universal Storage Engine for Sparse and Dense Multidimensional Arrays
•tsibble: Tidy Temporal Data Frames and Tools
•tsbox: Class\-Agnostic Time Series
•vtreat: A Statistically Sound data.frame Processor/Conditioner
7\.18 Dates and times
Python software implementations
List of packages and/or codes and/or frameworks and/or links:
•arrow: Better dates and times for Python
•dateparser: parser for human readable dates
•dateutil: Useful extensions to the standard Python datetime features
•orjson: Fast, correct Python JSON library supporting dataclasses, datetimes, and numpy
•parsedatetime: human\-readable date/time strings
•pendulum: datatimes made easy
•Pyrsistent: Persistent/Functional/Immutable data structures
•python\-dateutil: Useful extensions to the standard Python datetime features
•PyTime: operate datetime by string
R software implementations
List of packages and/or codes and/or frameworks and/or links:
•clock: Date\-Time Types and Tools
•lubridate: Make Dealing with Dates a Little Easier
•qlcal: R Bindings to the Calendaring Functionality of ’QuantLib’
•tidyquant: Tidy Quantitative Financial Analysis
•timechange: Efficient Manipulation of Date\-Times
•timetk: A Tool Kit for Working with Time Series in R
•tsbox: Class\-Agnostic Time Series
•TSrepr: Time Series Representations
•xts: eXtensible Time Series
•zoo: S3 Infrastructure for Regular and Irregular Time Series
627\.19 Dimensionality reduction
Python
List of packages/codes/frameworks/links:
•abess: Fast Best\-Subset Selection Library
•deeptime: analysis of time series data including dimensionality reduction, clustering, and Markov model
estimation
•direpack: State\-of\-the\-Art Statistical Dimension Reduction Methods
•EZyRB: Easy Reduced Basis method ; performs a data\-driven model order reduction for parametrized prob\-
lems exploiting the recent approaches.
•humap: Hierarchical Manifold Approximation and Projection (HUMAP) is a technique based on UMAP for
hierarchical non\-linear dimensionality reduction.
•pyFIt\-SNE: FFT\-accelerated Interpolation\-based t\-SNE (FIt\-SNE)
•scikit\-dimension: intrinsic dimension estimation
•scikit\-learn: machine learning in Python
•(t\-SNE: t\-Distributed Stochastic Neighbor Embedding (t\-SNE) for dimensionality reduction
•UMAP: Uniform Manifold Approximation and Projection
R software implementations
List of packages and/or codes and/or frameworks and/or links:
•abess: Fast Best\-Subset Selection Library
•abundant: High\-Dimensional Principal Fitted Components and Abundant Regression
•bayesdfa: Bayesian Dynamic Factor Analysis (DFA) with ’Stan’
•clustrd: Methods for Joint Dimension Reduction and Clustering
•dimRed: A Framework for Dimensionality Reduction
•DLPCA: The Distributed Local PCA Algorithm
•dobin: Dimension Reduction for Outlier Detection
•dyndimred: Dimensionality Reduction Methods in a Common Format
•EMD: Empirical Mode Decomposition and Hilbert Spectral Analysis
•ForeCA: Forecastable Component Analysis
•freqdom: Frequency Domain Based Analysis: Dynamic PCA
•ica: Independent Component Analysis
•ICtest: Estimating and Testing the Number of Interesting Components in Linear Dimension Reduction
•prinvars: Principal Variables (methods for reducing the number of features within a data set)
•quantdr: Dimension Reduction Techniques for Conditional Quantiles
•rrpack: Reduced\-Rank Regression
63•Rdimtools: Dimension Reduction and Estimation Methods
•RSpectra: Solvers for Large\-Scale Eigenvalue and SVD Problems
•shrinkTVP: Efficient Bayesian Inference for Time\-Varying Parameter Models with Shrinkage
•spcr: Sparse Principal Component Regression
•SuperPCA: Supervised Principal Component Analysis
•svd: Interfaces to Various State\-of\-Art SVD and Eigensolvers
•tapkee: tapkee: Wrapper for ’tapkee’ Dimension Reduction Library
•tidydr: Unify Dimensionality Reduction Results
•TSrepr: Time Series Representations (dimensionality reduction, preprocessing, feature extraction)
•umap: Uniform Manifold Approximation and Projection
7\.20 Distances and Similarity
Python software implementations
List of packages and/or codes and/or frameworks and/or links:
•DataGene: Identify How Similar TS Datasets Are to One Another
•dcor: Distance correlation and related E\-statistics
•dtaidistance: Distance measures for time series
•dtw\-python: comprehensive implementation of dynamic time warping (DTW) algorithms
•faiss: efficient similarity search and clustering of dense vectors
•FLANN: Fast Library for Approximate Nearest Neighbors
•GraKeL: scikit\-learn compatible library for graph kernels
•khiva\-python: Python binding for Khiva library for time series analytics
•mass\-ts: MASS (Mueen’s Algorithm for Similarity Search)
•MatrixProfile: ime series data mining tasks utilizing matrix profile
•matrixprofile\-ts: detect patterns and anomalies in massive datasets using Matrix Profile
•netrd: library for network {reconstruction, distances, dynamics}
•POT : Python Optimal Transport
•PyMD: imple but general framework for embedding, called Minimum\-Distortion Embedding (MDE), for finite
sets of items, such as images, biological cells, nodes in a network, or any other abstract object
•PySCAMP: SCAlable Matrix Profile
•seriesdistancematrix: implements the Series Distance Matrix framework, a flexible component\-based frame\-
work that bundles various Matrix Profile related techniques
•sktime: unified framework for machine learning with time series by UK national institute for data science and
artificial intelligence
•Stone\-Soup: framework for the development and testing of tracking algorithms
64•stumpy: variety of time series data mining tasks
•tidydr: Unify Dimensionality Reduction Results
•timesmash: Quantifier of universal similarity amongst arbitrary data streams without a priori knowledge,
features, or training
•wildboar: Time series learning
R software implementations
List of packages and/or codes and/or frameworks and/or links:
•dispRity: Measuring Disparity (multidimensional space occupancy)
•Distance: Distance Sampling Detection Function and Abundance Estimation
•distantia: Assessing Dissimilarity Between Multivariate Time Series
•dtw: Dynamic Time Warping Algorithms
•dtwclust: Time Series Clustering Along with Optimizations for the Dynamic Time Warping Distance
•fICA: Classical, Reloaded and Adaptive FastICA Algorithms
•gdm: Generalized Dissimilarity Modeling
•IncDTW: Incremental Calculation of Dynamic Time Warping
•KernelKnn: Extends the simple k\-nearest neighbors algorithm by incorporating numerous kernel functions
and a variety of distance metrics
•MatrixCorrelation: Matrix Correlation Coefficients
•mclustcomp: Measures for Comparing Clusters
•Mercator: Clustering and Visualizing Distance Matrices
•philentropy: Similarity and Distance Quantification Between Probability Functions
•proxy: Distance and Similarity Measures
•segen: Sequence Generalization Through Similarity Network
•tetragon: Automatic Sequence Prediction by Expansion of the Distance Matrix
•TSclust: set of measures of dissimilarity between time series to perform time series clustering
•TSdist: Distance Measures for Time Series Data
•tsmp: UCR Matrix Profile Algorithm
•VPdtw: Variable Penalty Dynamic Time Warping
7\.21 ESG and Impact Investing
Python software implementations
List of packages and/or codes and/or frameworks and/or links:
•ESG AI: ESG scoring as an automatic, data\-driven process
•ESG\-BERT: Domain Specific BERT Model for Text Mining in Sustainable Investing
65R software implementations
List of packages and/or codes and/or frameworks and/or links:
•EnvStats: Package for Environmental Statistics, Including US EPA Guidance
•ESGBoost: ESG and ECHO\-based model for smart investing
•gfer: Green Finance and Environmental Risk
•text2sdg: Detecting UN Sustainable Development Goals in Text
7\.22 Explainability, Interpretability, Fairness, Data Privacy
Python software implementations
List of packages and/or codes and/or frameworks and/or links:
•AIF360: comprehensive set of fairness metrics for datasets and machine learning models, explanations for
these metrics, and algorithms to mitigate bias in datasets and models
•captum: Model interpretability and understanding for PyTorch
•CrypTen: framework for Privacy Preserving Machine Learning
•Dice\-ML: Generate Diverse Counterfactual Explanations for any machine learning model
•DoWhy: toolkit by Microsoft for causal inference that supports explicit modeling and testing of causal as\-
sumptions
•Interpret: Fit interpretable models by Microsoft. Explain blackbox machine learning
•Interpretability dashboard, for understanding model predictions
•Lime: Local Interpretable Model\-Agnostic Explanations for machine learning classifiers
•Lucid: neural network interpretability
•PyExplainer: A Local Rule\-Based Model\-Agnostic Technique
•Skater: Model Interpretation/Explanations
•transformers\-interpret: Model explainability that works seamlessly with transformers
•XAI: eXplainability toolbox for machine learning
•Xplique: toolkit dedicated to explainability, currently based on Tensorflow
R software implementations
List of packages and/or codes and/or frameworks and/or links:
•DALEX: moDel Agnostic Language for Exploration and eXplanation
•distillML: Model Distillation and Interpretability Methods for Machine Learning Models
•fairml: Fair Models in Machine Learning
•iml: Interpretable Machine Learning
•interpret: Fit Interpretable Machine Learning Models
•modelDown: Make Static HTML Website for Predictive Models
•modelStudio: Interactive Studio for Explanatory Model Analysis
66•pdp: Partial Dependence Plots
•pre: Prediction Rule Ensembles
•Rforestry: Random Forests, Linear Trees, and Gradient Boosting for Inference and Interpretability
•rSAFE: Surrogate\-Assisted Feature Extraction
•sensitivity: Global Sensitivity Analysis of Model Outputs
•triplot: Explaining Correlated Features in Machine Learning Models
•yhat: Interpreting Regression Effects
7\.23 Features for time series
Python software implementations
List of packages and/or codes and/or frameworks and/or links:
•cesium: Platform for Time Series Inference
•Clairvoyance: a Unified, End\-to\-End AutoML Pipeline for Medical Time Series
•FeatureTools: automated feature engineering
•Featurewiz: advanced feature engineering strategies
•khiva\-python: Python binding for Khiva library for time series analytics
•mne\-features: MNE\-Features software for extracting features from multivariate time series
•scikit\-learn: machine learning in Python
•seglearn: integrated pipeline for segmentation, feature extraction, feature processing, and final estimator
•tsfeatures: Calculates various features from time series data
•tsfel: extract features from time series
•tsflex: Flexible time series feature extraction \& processing
•tsfresh: extract features from time series
R software implementations
List of packages and/or codes and/or frameworks and/or links:
•autostsm: Automatic Structural Time Series Models
•bfast: Breaks for Additive Season and Trend
•entropy: Estimation of Entropy, Mutual Information and Related Quantities
•feasts: Feature Extraction and Statistics for Time Series
•fsMTS: Feature Selection for Multivariate Time Series
•naive: Empirical Extrapolation of Time Feature Patterns
•plsVarSel: Variable Selection in Partial Least Squares
•MDFS: MultiDimensional Feature Selection
•Rcatch22: Calculation of 22 CAnonical Time\-Series CHaracteristics
67•theft: Tools for Handling Extraction of Features from Time Series
•tsfeatures: Time Series Feature Extraction
•TSrepr: Time Series Representations (dimensionality reduction, preprocessing, feature extraction)
7\.24 Filtering and spectral analysis for time series
Python software implementations
List of packages and/or codes and/or frameworks and/or links:
•FilterPy: Kalman filtering and optimal estimation library
•mkl\_fft: NumPy\-based Python interface to Intel (R) MKL FFT functionality
•pyfilter: Particle filtering and sequential parameter inference
•PyWavelets: Wavelet Transforms in Python
•simdkalman: Kalman filters vectorized as Single Instruction, Multiple Data
•Stone\-Soup: framework for the development and testing of tracking algorithms
R software implementations
List of packages and/or codes and/or frameworks and/or links:
•ASSA: Applied Singular Spectrum Analysis (ASSA)
•beyondWhittle: Bayesian Spectral Inference for Stationary Time Series
•BMAmevt: Multivariate Extremes: Bayesian Estimation of the Spectral Measure
•bsamGP: Bayesian Spectral Analysis Models using Gaussian Process Priors
•bspec: Bayesian Spectral Inference
•cohortBuilder: Data Source Agnostic Filtering Tools
•EMD: Empirical Mode Decomposition and Hilbert Spectral Analysis
•FKF: Fast Kalman Filter
•FKF.SP: Fast Kalman Filtering Through Sequential Processing
•frequencyConnectedness: Spectral Decomposition of Connectedness Measures
•kalmanfilter: Kalman Filter
•KFAS: Kalman Filter and Smoother for Exponential Family State Space Models
•kimfilter: Rcpp’ implementation of the multivariate Kim filter, which combines the Kalman and Hamilton
filters for state probability inference
•LMfilteR: Filter Methods for Parameter Estimation in Linear and Non Linear Regression Models
•mlr3filters: Filter Based Feature Selection for ’mlr3’
•multitaper: Spectral Analysis Tools using the Multitaper Method
•neverhpfilter: An Alternative to the Hodrick\-Prescott Filter
•praznik: Tools for Information\-Based Feature Selection and Scoring
68•psd: Adaptive, Sine\-Multitaper Power Spectral Density and Cross Spectrum Estimation
•psdr: Use Time Series to Generate and Compare Power Spectral Density
•quantspec: Quantile\-Based Spectral Analysis of Time Series
•Rfssa: Functional Singular Spectrum Analysis
•rhosa: Higher\-Order Spectral Analysis
•robfilter: Robust Time Series Filters
•RobKF: Innovative and/or Additive Outlier Robust Kalman Filtering
•RSpectra: Solvers for Large\-Scale Eigenvalue and SVD Problems
•Rssa: A Collection of Methods for Singular Spectrum Analysis
•Rwave: Time\-Frequency Analysis of 1\-D Signals
•SLBDD: Statistical Learning for Big Dependent Data
•spectral: Common Methods of Spectral Data Analysis
•Spectrum: Fast Adaptive Spectral Clustering for Single and Multi\-View Data
•spooky: Time Feature Extrapolation Using Spectral Analysis and Jack\-Knife Resampling
•wavethresh: Wavelets Statistics and Transforms
7\.25 Forecasting time series
Collections of resources
List of links:
•Popular Python Time Series Packages
•State of the art research (with codes) on time series forecasting
Python software implementations
List of packages and/or codes and/or frameworks and/or links:
•anticipy: time series forecasting
•atspy: Automated Time Series Models in Python
•Autoformer: Decomposition Transformers with Auto\-Correlation for Long\-Term Series Forecasting
•AutoTS: Automated Time Series Forecasting
•Auto\_TS: Automatically build multiple Time Series models using a Single Line of Code
•Clairvoyance: Unified, End\-to\-End AutoML Pipeline for Medical Time Series
•darts: toolkit by Unit8 for easy manipulation and forecasting of time series
•ETNA Time Series Library by Tinkoff AI
•fbprophet: forecasting toolkit by Facebook
•fireTS: multi\-variate time series prediction library working with sklearn
•Flow Forecast: Deep learning PyTorch library for time series forecasting, classification, and anomaly detection
69•glum: Generalized linear models
•GluonTS: toolkit by Amazon for Probabilistic time series modeling in Python
•greykite: flexible, intuitive and fast forecasting library by LinkedIn
•hcrystallball: unifies the API for most commonly used libraries and modeling techniques for time\-series
forecasting in the Python ecosystem
•HierarchicalForecast: Hierarchical forecasting with statistical and econometric methods
•kats: tookit by Facebook for time series analysis and forecasting
•lazypredict: build models without much code
•Local Cascade Ensemble (LCE) is a high\-performing, scalable and user\-friendly machine learning method for
the general tasks of Classification and Regression
•MAPIE: scikit\-learn\-compatible module for estimating prediction intervals.
•Merlion: A Machine Learning Framework for Time Series Intelligence by SalesForce
•MLForecast: Scalable machine learning based time series forecasting
•NGBoost: Natural Gradient Boosting for Probabilistic Prediction
•N\-HiTS: Neural Hierarchical Interpolation for Time Series Forecasting
•NeuralForecast: time series forecasting with deep learning models
•nixtla: Automated time series processing and forecasting
•Orbit: Bayesian forecasting package by Uber
•piecewise\-regression: For fitting straight line models to data with one or more breakpoints where the gradient
changes
•pmdarima: tatistical library designed to fill the void in Python’s time series analysis capabilities
•predictionrevisited: implements the core statistical concepts from the book ”Prediction Revisited: The Im\-
portance of Observation”
•Prophet: Automatic Forecasting Procedure by Facebook
•PyAF: Automatic Time Series Forecasting
•PyFlux: modern time series models, nference options (frequentist and Bayesian) that can be applied to these
models
•pyFTS: Fuzzy Time Series for Python
•pysf: Supervised forecasting of sequential data by UK national institute for data science and artificial intelli\-
gence
•PyTorch Forecasting: Forecasting timeseries with PyTorch \- dataloaders, normalizers, metrics and models
•pyts: time series classification
•pytsal: Time Series analysis, visualization, forecasting along with AutoTS
•scikit\-hts: Hierarchical Time Series Forecasting
•scikit\-learn: machine learning in Python
70•sktime: unified framework for machine learning with time series by UK national institute for data science and
artificial intelligence
•slearn: package linking symbolic representation with scikit\-learn machine learning
•statsforecast: Lightning � fast forecasting with statistical and econometric models
•Statsmodels: statistical modeling and econometrics in Python
•tbats: BATS and TBATS time series forecasting methods
•timemachines: Autonomous, univariate, k\-step ahead time\-series forecasting functions assigned Elo ratings
•TIMEX: time series forecasting as a service
•TSCV: Time Series CrossValidation
•ts\-eval: Time Series analysis and evaluation tools
•tslearn: machine learning toolkit dedicated to time series data
R software implementations
List of packages and/or codes and/or frameworks and/or links:
•ACV: Optimal Out\-of\-Sample Forecast Evaluation and Testing under Stationarity
•AIafter: Forecast Combination Using the AI\-AFTER Algorithm
•arfima: Fractional ARIMA (and Other Long Memory) Time Series Modeling
•ATAforecasting: Automatic Time Series Analysis and Forecasting Using the Ata Method
•autoTS: Automatic Model Selection and Prediction for Univariate Time Series
•baguette: Efficient Model Functions for Bagging
•bigtime: Sparse Estimation of Large Time Series Models
•BINtools: Bayesian BIN (Bias, Information, Noise) Model of Forecasting
•boot.pval: Bootstrap p\-Values
•caretForecast: Time Series Forecasting Using Caret Infrastructure
•cvms: Cross\-Validation for Model Selection
•dsos: Dataset Shift with Outlier Scores
•ensembleBMA: Probabilistic Forecasting using Ensembles and Bayesian Model Averaging
•fable: Forecasting Models for Tidy Time Series
•fable.ata: ATAforecasting Modelling Interface for fable Framework
•fable.prophet: Prophet Modelling Interface for ’fable’
•fabletools: Core Tools for Packages in the ’fable’ Framework
•FinnTS: Microsoft Finance Time Series Forecasting Framework
•flexmix: Flexible Mixture Modeling
•ForeCA: Forecastable Component Analysis
71•ForecastComb: Forecast Combination Methods
•forecastHybrid: Convenient Functions for Ensemble Time Series Forecasts
•forecastML: Time Series Forecasting with Machine Learning Methods
•forecastSNSTS: Forecasting for Stationary and Non\-Stationary Time Series
•ForecastTB: Test Bench for the Comparison of Forecast Methods
•FoReco: Point Forecast Reconciliation
•forecTheta: Forecasting Time Series by Theta Models
•fpp3: Data for ”Forecasting: Principles and Practice” (3rd Edition)
•fracdiff: Fractionally Differenced ARIMA aka ARFIMA(P,d,q) Models
•fwildclusterboot: Fast Wild Cluster Bootstrap Inference for Linear Models
•greybox: Toolbox for Model Building and Forecasting
•Greymodels: Shiny App for Grey Forecasting Model
•hts: Hierarchical and Grouped Time Series
•ipred: Improved Predictors
•legion: Forecasting Using Multivariate Models
•MAPA: Multiple Aggregation Prediction Algorithm
•mFLICA: Leadership\-Inference Framework for Multivariate Time Series
•modeltime: The Tidymodels Extension for Time Series Modeling
•modeltime.ensemble: Ensemble Algorithms for Time Series Forecasting with Modeltime
•modeltime.gluonts: ’GluonTS’ Deep Learning
•modeltime.resample: Resampling Tools for Time Series Forecasting
•ngboostForecast: Probabilistic Time Series Forecasting
•OOS: Out\-of\-Sample Time Series Forecasting
•origami: Generalized Framework for Cross\-Validation
•pre: Prediction Rule Ensembles
•predtoolsTS: Time Series Prediction Tools
•profoc: Probabilistic Forecast Combination Using CRPS Learning
•prophet: Automatic Forecasting Procedure
•PSF: Forecasting of Univariate Time Series Using the Pattern Sequence\-Based Forecasting (PSF) Algorithm
•PTSR: Positive Time Series Regression
•RFpredInterval: Prediction Intervals with Random Forests and Boosted Forests
•rigr: Regression, Inference, and General Data Analysis Tools in R
•Rlgt: Bayesian Exponential Smoothing Models with Trend Modifications
72•robets: Forecasting Time Series with Robust Exponential Smoothing
•robustarima: Robust ARIMA Modeling
•scoringfunctions: A Collection of Scoring Functions for Assessing Point Forecasts
•scoringRules: Scoring Rules for Parametric and Simulated Distribution Forecasts
•scoringutils: Utilities for Scoring and Assessing Predictions
•s2dverification: Set of Common Tools for Forecast Verification
•see: Visualisation Toolbox for ’easystats’ and Extra Geoms, Themes and Color Palettes for ’ggplot2’
•seer: Feature\-Based Forecast Model Selection
•segmented: Regression Models with Break\-Points / Change\-Points Estimation
•sense: Automatic Stacked Ensemble for Regression Tasks
•shrink: Global, Parameterwise and Joint Shrinkage Factor Estimation
•SLBDD: Statistical Learning for Big Dependent Data
•smooth: Forecasting Using State Space Models
•spcr: Sparse Principal Component Regression
•SPlit: Split a Dataset for Training and Testing
•StabilizedRegression: Stabilizing Regression and Variable Selection
•stacks: Tidy Model Stacking
•subsemble: An Ensemble Method for Combining Subset\-Specific Algorithm Fits
•tensorTS: Factor and Autoregressive Models for Tensor Time Series
•tfarima: Transfer Function and ARIMA Models
•thief: Temporal Hierarchical Forecasting
•tidymv: Tidy Model Visualisation for Generalised Additive Models
•traineR: Predictive Models Homologator
•TSdeeplearning: Deep Learning Model for Time Series Forecasting
•tsDyn: Nonlinear Time Series Models with Regime Switching
•tsensembler: Dynamic Ensembles for Time Series Forecasting
•TSPred: Functions for Benchmarking Time Series Prediction
•TSstudio: Functions for Time Series Analysis and Forecasting
•tsutils: Time Series Exploration, Modelling and Forecasting
•tswge: Time Series for Data Science.Accompanies the texts Time Series for Data Science and Applied Time
Series Analysis with R,
•vars: VAR Modelling
•yardstick: Tidy Characterizations of Model Performance
•yhat: Interpreting Regression Effects
737\.26 Graphs and graphical modeling
Python software implementations
List of packages and/or codes and/or frameworks and/or links:
•ogb: Benchmark datasets, data loaders, and evaluators for graph machine learning
•pathpy: analysis of time series data on networks using higher\-order and multi\-order graphical models
•PGM: Probabilistic Graphical Models
•pgmpy: Probabilistic Graphical Models
•PGM\_PyLib: Inference and Learning of Probabilistic Graphical Models
•pyaGrUM: Bayesian networks and other Probabilistic Graphical Models
•scikit\-network: nalysis of large graphs
•skggm: Scikit\-learn compatible estimation of general graphical models
•vishwakarma: visualization library for Probabilistic Graphical Models, Discrete \& Continuous Distributions,
and a lot more
R software implementations
List of packages and/or codes and/or frameworks and/or links:
•backbone: Extracts the Backbone from Graphs
•deepgp: Deep Gaussian Processes using MCMC
•gmgm: Gaussian Mixture Graphical Model Learning and Inference
•pcalg: Methods for Graphical Models and Causal Inference
•Revticulate: Interaction with ”RevBayes” in R
•tgp: Bayesian Treed Gaussian Process Models
•tidygraph: A Tidy API for Graph Manipulation
7\.27 Linear algebra
Python software implementations
List of packages and/or codes and/or frameworks and/or links:
•arctic: High performance datastore by Man Group for time series and tick data
•PyArma: Linear algebra library for Python
•PyArmadillo: an alternative approach to linear algebra in Python
•PyPardiso: Python interface to the Intel MKL Pardiso library to solve large sparse linear systems of equations
•Scipy: mathematics, science, and engineering
74R software implementations
List of packages and/or codes and/or frameworks and/or links:
•EigenR: Complex Matrix Algebra with ’Eigen’
•fastmatrix: Fast Computation of some Matrices Useful in Statistics
•freqdom: Frequency Domain Based Analysis: Dynamic PCA
•ica: Independent Component Analysis
•Matrix: Sparse and Dense Matrix Classes and Methods
•MatrixExtra: Extra Methods for Sparse Matrices
•matsbyname: An Implementation of Matrix Mathematics
•proxyC: Computes Proximity in Large Sparse Matrices
•rARPACK: Solvers for Large Scale Eigenvalue and SVD Problems
•RcppArmadillo: ’Rcpp’ Integration for the ’Armadillo’ Templated Linear Algebra Library
•RcppEigen: ’Rcpp’ Integration for the ’Eigen’ Templated Linear Algebra Library
•Rlinsolve: Iterative Solvers for (Sparse) Linear System of Equations
•RSpectra: Solvers for Large\-Scale Eigenvalue and SVD Problems
•sanic: Solving Ax \= b Nimbly in C\+\+
•SparseChol: Sparse Cholesky LDL Decomposition of Symmetric Matrices
•SparseM: Sparse Linear Algebra
•svd: Interfaces to Various State\-of\-Art SVD and Eigensolvers
7\.28 Machine Learning
Collections of resources
List of links:
•Curated list of open source libraries to deploy, monitor, version and scale machine learning
•Dive into Machine Learning
•Artificial Intelligence and Machine Learning For Quantum Technologies
Python software implementations
List of packages and/or codes and/or frameworks and/or links:
•abess: Fast Best Subset Selection
•AIF360: comprehensive set of fairness metrics for datasets and machine learning models, explanations for
these metrics, and algorithms to mitigate bias in datasets and models
•benchmark\_VAE: Unifying Generative Autoencoder implementations in Python
•bindsnet: Simulation of spiking neural networks (SNNs) using PyTorch
•biosphere: Simple, fast random forests
75•Catalyst: PyTorch framework for Deep Learning Research and Development
•catboost: Gradient Boosting on Decision Trees by Yandex
•Chainer: flexible framework of neural networks for deep learning
•combo: A Python Toolbox for Machine Learning Model Combination
•compose: machine learning tool for automated prediction engineering
•coremltools: convert machine learning models from third\-party libraries to the Core ML format (by Apple)
•CrypTen: framework for Privacy Preserving Machine Learning
•DeepChecks: Testing and Validating ML Models and Data
•DoubleML: Double Machine Learning in Python
•Driblet \- Google Cloud based ML pipeline by Google
•geotorch: Constrained optimization toolkit for PyTorch
•GPyTorch: Gaussian processes for modern machine learning systems.
•Hub for Tensorflow: library for transfer learning by reusing parts of TensorFlow models
•Hummingbird: library by Microsoft for compiling trained traditional ML models into tensor computations
•InvarianceUnitTests: Linear unit\-tests for invariance discovery
•JAX: toolkit by Google for composable transformations of Python\+NumPy programs: differentiate, vectorize,
JIT to GPU/TPU, and more
•jraph: Graph Neural Network Library in Jax
•karateclub: Framework for Unsupervised Learning on Graphs
•keras: deep learning API written in Python, running on top of the machine learning platform TensorFlow
•Local Cascade Ensemble (LCE) is a high\-performing, scalable and user\-friendly machine learning method for
the general tasks of Classification and Regression
•LightGBM: fast, distributed, high performance gradient boosting (GBT, GBDT, GBRT, GBM or MART)
framework by Microsoft
•Merlion: A Machine Learning Framework for Time Series Intelligence by SalesForce
•mlflow: Interface to ’MLflow’
•MLForecast: Scalable machine learning based time series forecasting
•mlinsights: Extends scikit\-learn with new models, transformers, metrics, plotting.
•MLJAR Automated Machine Learning for Humans
•mlxtend: extension and helper modules for Python’s data analysis and machine learning libraries.
•MMdnn: toolkit by Microsoft to convert models between Caffe, Keras, MXNet, Tensorflow, CNTK, PyTorch
Onnx and CoreML.
•Model Garden for TensorFlow
•mvlearn is an open\-source Python software package for multiview learning tools.
76•NannyM: estimate post\-deployment model performance (without access to targets), detect data drift, and
intelligently link data drift alerts back to changes in model performance
•NeuralForecast: time series forecasting with deep learning models
•NGBoost: Natural Gradient Boosting for Probabilistic Prediction
•nimbusml: toolkit by Microsoft that provides Python bindings for ML.NET
•nolearn: Combines the ease of use of scikit\-learn with the power of Theano/Lasagne
•norse: Deep learning with spiking neural networks (SNNs) in PyTorch.
•OPACUS: Training PyTorch models with differential privacy
•ptgnn: PyTorch Graph Neural Network Library
•PyCaret : machine learning library
•PyTorch: Tensors and Dynamic neural networks in Python with strong GPU acceleration
•PyTorch Lightning: lightweight PyTorch wrapper for ML researchers
•Ray: packaged with RLlib, a scalable reinforcement learning library, and Tune, a scalable hyperparameter
tuning librar
•scikit\-learn: machine learning in Python
•scikit\-learn\-intelex: Intel Extension for Scikit\-learn
•sklearn\-onnx converts scikit\-learn models to ONNX
•skorch: scikit\-learn compatible neural network library that wraps PyTorch
•SNNTORCH: Deep and online learning with spiking neural networks
•tensorflow: end\-to\-end open source platform for machine learning
•tf2onnx: Convert TensorFlow, Keras, Tensorflow.js and Tflite models to ONNX
•Transfer Learning Library for Domain Adaptation, Task Adaptation, and Domain Generalization
•transformers: State\-of\-the\-art Machine Learning for Pytorch, TensorFlow, and JAX
•Trax: Deep Learning by Google with Clear Code and Speed
•tslearn: machine learning toolkit dedicated to time\-series data
•xformers: Hackable and optimized Transformers building blocks, supporting a composable construction
•yellowbrick: Visual analysis and diagnostic tools to facilitate machine learning model selection
R software implementations
List of packages and/or codes and/or frameworks and/or links:
•abess: Fast Best Subset Selection
•agua: ’tidymodels’ Integration with ’h2o’
•APML: An Approach for Machine\-Learning Modelling
•arenar: Arena for the Exploration and Comparison of any ML Models
•brulee: High\-Level Modeling Functions with ’torch’
77•distillML: Model Distillation and Interpretability Methods for Machine Learning Models
•elmNNRcpp: The Extreme Learning Machine Algorithm
•fairmodels: Flexible Tool for Bias Detection, Visualization, and Mitigation
•familiar: End\-to\-End Automated Machine Learning and Model Evaluation
•KernelKnn: Extends the simple k\-nearest neighbors algorithm by incorporating numerous kernel functions
and a variety of distance metrics
•lightgbm: Light Gradient Boosting Machine by Microsoft
•MachineShop: Machine Learning Models and Tools
•mcboost: Multi\-Calibration Boosting
•MetricsWeighted: Weighted Metrics, Scoring Functions and Performance Measures for Machine Learning
•mikropml: User\-Friendly R Package for Supervised Machine Learning Pipelines
•mlflow: Interface to ’MLflow’
•mlquantify: Algorithms for Class Distribution Estimation
•mlr3: Machine Learning in R \- Next Generation
•mlr3cluster: Cluster Extension for ’mlr3’
•mlr3learners: Recommended Learners for ’mlr3’
•mlr3tuning: hyperparameter tuning with ’mlr3’
•mlr3verse: package family is a set of packages for machine\-learning purposes built in a modular fashion
•mlr3viz: Visualizations for’mlr3
•mlrintermbo: Model\-Based Optimization for ’mlr3’ Through ’mlrMBO’
•mlrMBO: Bayesian Optimization and Model\-Based Optimization of Expensive Black\-Box Functions
•multiview: Cooperative Learning for Multi\-View Analysis
•rTorch: R Bindings to ’PyTorch’
•SPlit: Split a Dataset for Training and Testing
•tensorflow: R Interface to ’TensorFlow’
•tfdatasets: Interface to ’TensorFlow’ Datasets
•tfprobability: Interface to ’TensorFlow Probability’
•TSdeeplearning: Deep Learning Model for Time Series Forecasting
•xgboost: Extreme Gradient Boosting
787\.29 Machine Learning frameworks (includes Automated ML and hyperparameters
tuning)
Python software implementations
List of packages and/or codes and/or frameworks and/or links:
•AI2 Tango: library for choreographing machine learning research
•AutoGluon: toolkit by Amazon on AutoML for Text, Image, and Tabular Data
•AutoKeras: An AutoML system based on Keras
•AutoPyTorch: Automatic architecture search and hyperparameter optimization for PyTorch
•auto\-sklearn: Automated Machine Learning with scikit\-learn
•BayesianOptimization: global optimization with gaussian processes.
•cesium: Machine Learning Time\-Series Platform
•Clairvoyance: Unified, End\-to\-End AutoML Pipeline for Medical Time Series
•Colossal\-AI: A Unified Deep Learning System for Big Model Era
•EvalML is an AutoML library which builds, optimizes, and evaluates machine learning pipelines using domain\-
specific objective functions.
•FLAML: accurate machine learning models automatically, efficiently and economically (by Microsoft)
•flax: neural network library for JAX that is designed for flexibility
•H2O is an Open Source, Distributed, Fast \& Scalable Machine Learning Platform
•Hypernets: General Automated Machine Learning framework
•HyperOpt: Distributed Asynchronous Hyperparameter Optimization
•hyperopt\-sklearn: Hyper\-parameter optimization for sklearn
•kedro: framework for creating reproducible, maintainable and modular data science code
•kedro\-viz: Visualise your Kedro data and machine\-learning pipelines and track your experiments.
•keras\-tuner: hyperparameter optimization framework
•MLBox: Automated Machine Learning library
•mlpack: ’Rcpp’ Integration for the ’mlpack’ Library
•mlr3tuning: Tuning for ’mlr3’
•model\_search: framework (by Google) that implements AutoML algorithms for model architecture search at
scale
•NannyM: estimate post\-deployment model performance (without access to targets), detect data drift, and
intelligently link data drift alerts back to changes in model performance
•NNI: toolkit by Microsoft to help users automate Feature Engineering, Neural Architecture Search, Hyperpa\-
rameter Tuning and Model Compression
•oneflow: OneFlow is a deep learning framework designed to be user\-friendly, scalable and efficient.
•ONNX: Open Neural Network Exchange is an Open standard for machine learning interoperability
79•Optuna: hyperparameter optimization framework
•PyCaret : machine learning library
•squirrel\-core: library that enables ML teams to share, load, and transform data in a collaborative, flexible,
and efficient way.
•Relevance AI \- The ML Platform for Unstructured Data Analysis
•Talos: Hyperparameter Optimization for TensorFlow, Keras and PyTorch
•trax: end\-to\-end library (by Google Brain) for deep learning that focuses on clear code and speed.
•tune\-sklearn: drop\-in replacement for Scikit\-Learn’s GridSearchCV / RandomizedSearchCV – but with cutting
edge hyperparameter tuning techniques
•vowpal\_wabbit: machine learning system which pushes the frontier of machine learning with techniques such
as online, hashing, allreduce, reductions, learning2search, active, and interactive learning
R software implementations
List of packages and/or codes and/or frameworks and/or links:
•autokeras: R Interface to ’AutoKeras’
•automl: Deep Learning with Metaheuristic
•DriveML: Self\-Drive Machine Learning Projects
•familiar: End\-to\-End Automated Machine Learning and Model Evaluation
•mlpack: ’Rcpp’ Integration for the ’mlpack’ Library
•mlr3tuningspaces: Search Spaces for Hyperparameter Tuning
•ParBayesianOptimization: Parallel Bayesian Optimization of Hyperparameters
•rBayesianOptimization: Bayesian Optimization of Hyperparameters
•RemixAutoML: automation of machine learning, forecasting, feature engineering, model evaluation, model
interpretation, recommenders, and EDA.
7\.30 Network and graph analysis
Python software implementations
List of packages and/or codes and/or frameworks and/or links:
•dantro: handle, transform, and visualize hierarchically structured data
•deeptime: nalysis of time series data including dimensionality reduction, clustering, and Markov model esti\-
mation
•ETNA Time Series Library by Tinkoff AI
•fastpath: find the path through a network of nodes
•GraKeL: scikit\-learn compatible library for graph kernels
•grapharray: handle network link/node attributes as Numpy arrays
•GraphVite: A General and High\-performance Graph Embedding System
•karateclub: Framework for Unsupervised Learning on Graphs
80•netrd: etwork {reconstruction, distances, dynamics}
•networkit: toolkit for large\-scale network analysis
•NetworkX: Network Analysis in Python
•pandana: Pandas Network Analysis: fast accessibility metrics and shortest paths, using contraction hierarchies
•pyvis: visualizing interactive network graphs
•rustworkx: high performance Python graph library implemented in Rust
•scikit\-learn: machine learning in Python
•tslearn: machine learning toolkit dedicated to time\-series data
R software implementations
List of packages and/or codes and/or frameworks and/or links:
•backbone: identify the most ‘important’ or ‘significant’ edges in a network
•bnmonitor: An Implementation of Sensitivity Analysis in Bayesian Networks
•bootnet: Bootstrap Methods for Various Network Estimation Routines
•CINNA: Deciphering Central Informative Nodes in Network Analysis
•dbnR: Dynamic Bayesian Network Learning and Inference
•diceR: Diverse Cluster Ensemble in R
•dtwclust: Time Series Clustering Along with Optimizations for the Dynamic Time Warping Distance
•fabisearch: Change Point Detection in High\-Dimensional Time Series Networks
•fastkmedoids: Faster K\-Medoids Clustering Algorithms: FastPAM, FastCLARA, FastCLARANS
•gRain: Graphical Independence Networks
•heatmaply: Interactive Cluster Heat Maps Using ’plotly’ and ’ggplot2’
•influential: Identification and Classification of the Most Influential Nodes
•MatTransMix: Clustering with Matrix Gaussian and Matrix Transformation Mixture Models
•Mercator: Clustering and Visualizing Distance Matrices
•MixSim: Simulating Data to Study Performance of Clustering Algorithms
•mixture: Mixture Models for Clustering and Classification
•MKMeans: A Modern K\-Means (MKMeans) Clustering Algorithm
•ndtv: Network Dynamic Temporal Visualizations
•network: Classes for Relational Data
•networkABC: Network Reverse Engineering with Approximate Bayesian Computation
•networkDynamic: Dynamic Extensions for Network Objects
•NetworKit: tool suite for high\-performance network analysis
•networktools: Tools for Identifying Important Nodes in Networks
81•statnet: Software Tools for the Statistical Analysis of Network Data
•visNetwork: Network Visualization using ’vis.js’ Library
•wdnet: Weighted and Directed Networks
•WGCNA: Weighted Correlation Network Analysis
7\.31 Numerical methods (includes numerical optimization)
Python software implementations
List of packages and/or codes and/or frameworks and/or links:
•ADE: Asynchronous Differential Evolution, with efficient multiprocessing
•autoray: Write numeric code that automatically works with any numpy\-ish libraries
•BayesianOptimization: global optimization with gaussian processes
•CasADi is a symbolic framework for numeric optimization implementing automatic differentiation in forward
and reverse modes on sparse matrix\-valued computational graphs
•cmaes: Covariance Matrix Adaptation Evolution Strategy (CMA\-ES)
•coco: Numerical Black\-Box Optimization Benchmarking Framework
•cp\_solver: CP\-SAT Solver by Google
•cvxopt: convex optimization
•cvxpy: convex optimization
•DEAP: Distributed Evolutionary Algorithms in Python
•derivative: Numerical differentiation of noisy time series data
•Differential Evolution expensiveopt
•eigenpy: Efficient Python bindings between Numpy/Eigen
•ELA drframework: Dimensionality Reduction Framework for Exploratory Landscape Analysis
•evol: grammar for evolutionary algorithms and heuristics
•fcmaes complements scipy optimize by providing additional optimization methods, faster C\+\+/Eigen based
implementations and a coordinated parallel retry mechanism.
•gemseo: Generic Engine for Multi\-disciplinary Scenarios, Exploration and Optimization
•General Purpose Optimization Library GPOL
•HiGHS: Linear optimization
•hyperactive: optimization and data collection toolbox for convenient and fast prototyping of computationally
expensive models
•ipopt: Cython interface for the interior point optimzer IPOPT
•ipyopt: interface for the interior point optimizer COIN\-OR IPOpt
•mystic: highly\-constrained non\-convex optimization and uncertainty quantification
•nevergrad: Python toolbox for performing gradient\-free optimization by Facebook
82•nlopt: nonlinear optimization
•Open MDAO: optimization framework
•optima: library for numerical optimization calculations
•OR\-Tools: optimization toolkit by Google
•osqp: Operator Splitting QP Solver
•pybobyqa: Derivative\-Free Optimization with Bound Constraints
•pycma: Covariance Matrix Adaptation Evolution Strategy (CMA\-ES)
•pymoo: Multi\-objective Optimization
•pyomo: supports a diverse set of optimization capabilities for formulating and analyzing optimization models.
•PyOptSparse: object\-oriented framework for formulating and solving nonlinear constrained optimization prob\-
lems
•PyPDE: solve partial differential equations using finite differences.
•qpsolvers: Quadratic programming solvers in Python with a unified API
•root\_numpy: interface between ROOT and NumPy
•scikit\-opt: Swarm Optimization methods
•scikit\-optimize: Sequential model\-based optimization with a ‘scipy.optimize‘ interface
•Scipy: Fundamental algorithms for scientific computing
•SHADE: Success\-History Based Parameter Adaptation for Differential Evolution
•stgaircase: data analysis package based on mathematical step functions
•theseus: differentiable nonlinear optimization
•torchquad: High\-performance numerical integration on the GPU with PyTorch, JAX and Tensorflow
•torchsde: Differentiable SDE solvers with GPU support and efficient sensitivity analysis
•trust\-region:trust\-region subproblem solvers for nonlinear optimization
R software implementations
List of packages and/or codes and/or frameworks and/or links:
•ao: Alternating Optimization
•bbotk: Black\-Box Optimization Toolkit
•CGNM: Cluster Gauss\-Newton Method: Find multiple solutions of a nonlinear least squares problem
•CVXR: Disciplined Convex Optimization
•DEoptim: Global Optimization by Differential Evolution
•DEoptimR: Differential Evolution Optimization in Pure R
•ECOSolveR: Embedded Conic Solver in R
•ggblanket: Simplify ’ggplot2’ Visualisation
83•graDiEnt: derivative\-free, optim\-style Stochastic Quasi\-Gradient Differential Evolution optimization
•itp: The Interpolate, Truncate, Project (ITP) Root\-Finding Algorithm
•LowRankQP: Low Rank Quadratic Programming
•miesmuschel: Mixed Integer Evolution Strategies
•minqa: Derivative\-Free Optimization Algorithms by Quadratic Approximation
•mlr3mbo: Flexible Bayesian Optimization
•NMOF: Numerical Methods and Optimization in Finance
•osqp: Quadratic Programming Solver using the ’OSQP’ Library
•RcppEnsmallen: Header\-Only C\+\+ Mathematical Optimization Library for ’Armadillo’
•rvinecopulib: High Performance Algorithms for Vine Copula Modeling
•rgenoud: R Version of GENetic Optimization Using Derivatives
•rmoo: Multi\-Objective Optimization in R
•scs: Splitting Conic Solver for linear programs (’LPs’), second\-order cone programs (’SOCPs’), semidefinite
programs (’SDPs’), exponential cone programs (’ECPs’), and power cone programs (’PCPs’), or problems
with any combination of those cone
•SimEngine: A Modular Framework for Statistical Simulations in R
•trustOptim: Trust Region Optimization for Nonlinear Functions with Sparse Hessians
7\.32 Probabilistic modeling (includes mixture models and Gaussian Processes)
Links to resources
•Professionally curated list of awesome Conformal Prediction videos, tutorials, books, papers, PhD and MSc
theses, articles and open\-source libraries
Python software implementations
List of packages and/or codes and/or frameworks and/or links:
•beanmachine: inference on probabilistic models
•celerite2: fast and scalable Gaussian Process (GP) Regression
•conformal\-rnn: code for ”Conformal time\-series forecasting”, NeurIPS 2021
•crepes: Conformal Regressors and Conformal Predictive Systems
•EnbPI: Ensemble batch prediction intervals
•EnCQR: ensemble conformalized quantile regression (EnCQR)
•GluonTS: toolkit by Amazon for Probabilistic time series modeling in Python
•gptools: Gaussian processes with arbitrary derivative constraints and predictions.
•GPy: Gaussian processes framework
•GPyTorch: Gaussian processes for modern machine learning systems.
•MAPIE: scikit\-learn\-compatible module for estimating prediction intervals
84•NGBoost: Natural Gradient Boosting for Probabilistic Prediction
•orbit\-ml: Bayesian forecasting package by Uber
•pgmpy: Probabilistic Graphical Models – learning (Structure and Parameter), inference (Probabilistic and
Causal), and simulations in Bayesian Networks
•pplbench: Evaluation Framework for Probabilistic Programming Languages
•PyMC: Bayesian Modeling and Probabilistic Machine Learning with Aesara
•pyro: Deep universal probabilistic programming with Python and PyTorch
•PySloth: Probabilistic Prediction
•skpro: toolkit by UK national institute for data science and artificial intelligence for Supervised domain\-
agnostic prediction framework for probabilistic modelling
•tinyGP: The tiniest of Gaussian Process libraries
•zhusuan: probabilistic programming library for Bayesian deep learning, generative models, based on Tensor\-
flow
R software implementations
List of packages and/or codes and/or frameworks and/or links:
•AdequacyModel: Adequacy of Probabilistic Models and General Purpose Optimization
•AdMit: Adaptive Mixture of Student\-t Distributions
•aldvmm: Adjusted Limited Dependent Variable Mixture Models
•bgmm: Gaussian Mixture Modeling Algorithms and the Belief\-Based Mixture Modeling
•bmixture: Bayesian Estimation for Finite Mixture of Distributions
•BNPmix: Bayesian Nonparametric Mixture Models
•bpgmm: Bayesian Model Selection Approach for Parsimonious Gaussian Mixture Models
•ClusterR: Gaussian Mixture Models, K\-Means, Mini\-Batch\-Kmeans, K\-Medoids and Affinity Propagation
Clustering
•conformalInference.multi: Conformal Inference Tools for Regression with Multivariate Response
•DistributionOptimization: Distribution Optimization
•distributionsrd: Distribution Fitting and Evaluation
•EMCluster: EM Algorithm for Model\-Based Clustering of Finite Mixture Gaussian Distribution
•evmix: Extreme Value Mixture Modelling, Threshold Estimation and Boundary Corrected Kernel Density
Estimation
•flexmix: Flexible Mixture Modeling
•flexmixNL: Finite Mixture Modeling of Generalized Nonlinear Models
•GauPro: Gaussian Process Fitting
•gmgm: Gaussian Mixture Graphical Model Learning and Inference
•greta.gp: Gaussian Process Modelling in ’greta’
85•hmmr: ”Mixture and Hidden Markov Models with R” Datasets and Example Code
•ltmix: Left\-Truncated Mixtures of Gamma, Weibull, and Lognormal Distributions
•MatrixMixtures: Model\-Based Clustering via Matrix\-Variate Mixture Models
•MGMM: Missingness Aware Gaussian Mixture Models
•mistr: Mixture and Composite Distributions
•mixComp: Estimation of Order of Mixture Distributions
•MixMatrix: Classification with Matrix Variate Normal and t Distributions
•MixSim: Simulating Data to Study Performance of Clustering Algorithms
•mixsmsn: Fitting Finite Mixture of Scale Mixture of Skew\-Normal Distributions
•mixreg: Functions to Fit Mixtures of Regressions
•mixSPE: Mixtures of Power Exponential and Skew Power Exponential Distributions for Use in Model\-Based
Clustering and Classification
•mixsqp: Sequential Quadratic Programming for Fast Maximum\-Likelihood Estimation of Mixture Proportions
•mixtools: Tools for Analyzing Finite Mixture Models
•mixture: Mixture Models for Clustering and Classification
•mclust: Gaussian Mixture Modelling for Model\-Based Clustering, Classification, and Density Estimation
•mlr3proba: Probabilistic Supervised Learning for ’mlr3’
•MoMPCA: Inference and Clustering for Mixture of Multinomial Principal Component Analysis
•mvgb: Multivariate Probabilities of Scale Mixtures of Multivariate Normal Distributions via the Genz and
Bretz (2002\) QRSVN Method
•ngboostForecast: Probabilistic Time Series Forecasting
•nlsmsn: Fitting Nonlinear Models with Scale Mixture of Skew\-Normal Distributions
•Nmix: Bayesian Inference on Univariate Normal Mixtures
•nvmix: Multivariate Normal Variance Mixtures
•opGMMassessment: Optimized Automated Gaussian Mixture Assessment
•pgmm: Parsimonious Gaussian Mixture Models
•pGPx: Pseudo\-Realizations for Gaussian Process Excursions
•pks: Probabilistic Knowledge Structures
•plgp: Particle Learning of Gaussian Processes
•plotmm: Tidy Tools for Visualizing Mixture Models
•QuantileGH: Quantile Least Mahalanobis Distance Estimator for Tukey g\-\&\-h Mixture
•rebmix: Finite Mixture Modeling, Clustering \& Classification
•Revticulate: Interaction with ”RevBayes” in R
•RGMM: Robust Mixture Model
86•RMixtComp: Mixture Models with Heterogeneous and (Partially) Missing Data
•robmixglm: Robust Generalized Linear Models (GLM) using Mixtures
•Rmixmod: Classification with Mixture Modelling
•RobMixReg: Robust Mixture Regression
•rrMixture: Reduced\-Rank Mixture Models
•seqHMM: Mixture Hidden Markov Models for Social Sequence Data and Other Multivariate, Multichannel
Categorical Time Series
•skewlmm: Scale Mixture of Skew\-Normal Linear Mixed Models
•skewMLRM: Estimation for Scale\-Shape Mixtures of Skew\-Normal Distributions
•uGMAR: Estimate Univariate Gaussian and Student’s t Mixture Autoregressive Models
7\.33 Reinforcement learning
Collections of resources
List of links:
•Awesome Reinforcement Learning: Reinforcement learning resources curated
•Awesome Deep RL: curated list of awesome Deep Reinforcement Learning resources
Python software implementations
List of packages and/or codes and/or frameworks and/or links:
•Acme: a research framework by DeepMind for reinforcement learning
•Baconian: Model\-based Reinforcement Learning Framework
•Open AI Baselines: high\-quality implementations by OpenAI of reinforcement learning algorithms
•Catalyst.RL: Distributed Framework for Reproducible RL Research
•ChainerRL: deep reinforcement learning library built on top of Chainer
•Coach: Reinforcement Learning by Intel AI Lab
•d3rlpy: offline deep reinforcement learning library
•Decision Transformer: Reinforcement Learning via Sequence Modeling
•DRL with PyTorch: PyTorch implementations of deep reinforcement learning algorithms and environments
•Deep Reinforcement Learning Hands\-On
•deer: DEEp Reinforcement learning framework
•Dopamine: research framework by Google for fast prototyping of reinforcement learning algorithms
•ElegantRL: Lightweight and scalable deep reinforcement learning using PyTorch
•FinRL: Deep Reinforcement Learning for Quantitative Finance
•FinRL\-Meta: Universe of Near\-Real Market Environments for Data\-Driven Financial Reinforcement Learning
•garage: toolkit for reproducible reinforcement learning research
87•Gym: ttolkit by openAI for toolkit for developing and comparing reinforcement learning algorithms
•HRAC: Generating Adjacency\-Constrained Subgoals in Hierarchical Reinforcement Learning
•keras\-rl: Deep Reinforcement Learning for Keras
•Mava: library of multi\-agent reinforcement learning components and systems
•Multi\-Agent Resource Optimization (MARO) platform is an instance of Reinforcement Learning as a Service
(RaaS) for real\-world resource optimization problems.
•MBRL\-Lib: toolbox by Facebook for facilitating development of Model\-Based Reinforcement Learning algo\-
rithms
•Mushroom RL: modular toolkit able to use modularity allows to use libraries for tensor computation (e.g.
PyTorch, Tensorflow) and RL benchmarks (e.g. OpenAI Gym, PyBullet, Deepmind Control Suite)
•PettingZoo: Gym for multi\-agent reinforcement learning
•PFRL: PyTorch\-based deep reinforcement learning library
•PGPortfolio: Policy Gradient Portfolio
•PyTorchRL: reinforcement learning library focused on modularity and simplicity
•Rainbow: Combining Improvements in Deep Reinforcement Learning
•ReAgent: platform by Facebook for Reasoning systems (Reinforcement Learning, Contextual Bandits, etc.)
•rl: modular, primitive\-first, python\-first PyTorch library for Reinforcement Learning.
•RLkit: Collection of reinforcement learning algorithms
•RLlib: Ray is packaged with RLlib, a scalable reinforcement learning library, and Tune, a scalable hyperpa\-
rameter tuning librar
•RLMeta is a light\-weight flexible framework for Distributed Reinforcement Learning Research
•rlpyt: Reinforcement Learning in PyTorch
•rlstructures: Facebook library to facilitate the implementation of new reinforcement learning algorithms
•skrl: Modular reinforcement learning
•Stable Baselines3: PyTorch version of Stable Baselines, reliable implementations of reinforcement learning
algorithms
•Tensorforce: TensorFlow library for applied reinforcement learning
•TensorLayer: Deep Learning and Reinforcement Learning Library for Scientists and Engineers
•TF\-Agents: TensorFlow library for Contextual Bandits and Reinforcement Learning
•Tianshou: PyTorch deep reinforcement learning library
•Tonic RL: Tonic RL library
•TorchBeast: A PyTorch Platform by Facebook for Distributed RL
•TRFL: TensorFlow Reinforcement Learning by DeepMind
•vowpal\_wabbit: machine learning system which pushes the frontier of machine learning with techniques such
as online, hashing, allreduce, reductions, learning2search, active, and interactive learning
88R software implementations
List of packages and/or codes and/or frameworks and/or links:
•Hands\-On Reinforcement Learning
•QLearning: Reinforcement Learning using the Q Learning Algorithm
•reinforcelearn: reinforcement learning, including Q\-Learning algorithm
•ReinforcementLearning: Model\-Free Reinforcement Learning
•RLT: Reinforcement Learning Trees
7\.34 Robust numerical methods
Python software implementations
List of packages and/or codes and/or frameworks and/or links:
•derivative: Numerical differentiation of noisy time series data
•hypothesize: hypothesis testing using robust statistics
•robusta: interface to many common statistical analyses, performed using through R and RPY2\.
•Robustats is a Python library for high\-performance computation of robust statistical estimators
•robustbase: Statistical Estimators (Sn, Qn, MAD, IQR)
R software implementations
List of packages and/or codes and/or frameworks and/or links:
•clubSandwich: Cluster\-Robust (Sandwich) Variance Estimators with Small\-Sample Corrections
•l1spectral: An L1\-Version of the Spectral Clustering
•L2E: Robust Structured Regression via the L2 Criterion
•pcaPP: Robust PCA by Projection Pursuit
•RCTS: Clustering Time Series While Resisting Outliers
•RDnp: Robust Test for Complete Independence in High\-Dimensions
•revss: Robust Estimation in Very Small Samples
•RGMM: Robust Mixture Model
•rigr: Regression, Inference, and General Data Analysis Tools in R
•robcp: Robust Change\-Point Tests
•robcor: Robust Correlations
•robfilter: Robust Time Series Filters
•robmixglm: Robust Generalized Linear Models (GLM) using Mixtures
•RobMixReg: Robust Mixture Regression
•RobStatTM: Robust Statistics: Theory and Methods
•robust: Port of the S\+ ”Robust Library”
89•RobustANOVA: Robust One\-Way ANOVA Tests under Heteroscedasticity and Nonnormality
•robustbase: Basic Robust Statistics
•RobustCalibration: Robust Calibration of Imperfect Mathematical Models
•robustcov: Collection of Robust Covariance and (Sparse) Precision Matrix Estimators
•robustHD: Robust Methods for High\-Dimensional Data
•rrcov: Scalable Robust Estimators with High Breakdown Point
•RSC: Robust and Sparse Correlation Matrix
•sandwich: Robust Covariance Matrix Estimators
•StabilizedRegression: Stabilizing Regression and Variable Selection
•tsrobprep: Robust Preprocessing of Time Series Data
•walrus: Robust Statistical Methods
7\.35 Selection of features, variables, models, data splits
Collections of resources
List of links:
•Data Science Feature Engineering and Selection Tutorials
•Feature Engineering and Selection: A Practical Approach for Predictive Models
•Guide for Feature Engineering and Feature Selection
Python software implementations
List of packages and/or codes and/or frameworks and/or links:
•abess: Fast Best\-Subset Selection Library
•boruta\_py: Boruta all\-relevant feature selection method
•dython: Data analysis tools
•featureclass: Feature engineering library to keep track of feature dependencies, documentation and schema
•feature\_engine: library with multiple transformers to engineer and select features for use in machine learning
models
•FeatureTools: automated feature engineering
•Featurewiz: advanced feature engineering strategies
•ITMO\_FS: Feature selection library
•KnockPy: Knockoffs for controlled variable selection
•kydavra: feature selection
•Py\_FS: Feature Selection
•pyHSICLasso: Versatile Nonlinear Feature Selection Algorithm for High\-dimensional Data
•python\_stepwiseSelection: Automated Backward and Forward Selection
90•scikit\-learn: machine learning in Python
•scikit\-rebate: scikit\-learn\-compatible Python implementation of ReBATE, a suite of Relief\-based feature
selection algorithms
•Sklearn\-genetic\-opt: Hyperparameters tuning and feature selection, using evolutionary algorithms
•sktime: unified framework for machine learning with time series by UK national institute for data science and
artificial intelligence
•tsfeatures: Calculates various features from time series data. Python implementation of the R package
tsfeatures
•UltraNest: Fit and compare complex models reliably and rapidly. Advanced nested sampling
•zoofs: feature selection using a variety of nature\-inspired wrapper algorithms
R software implementations
List of packages and/or codes and/or frameworks and/or links:
•abess: Fast Best\-Subset Selection Library
•BAS: Bayesian Variable Selection and Model Averaging using Bayesian Adaptive Sampling
•basad: Bayesian Variable Selection with Shrinking and Diffusing Priors
•BayesVarSel: Bayes Factors, Model Choice and Variable Selection in Linear Models
•bpgmm: Bayesian Model Selection Approach for Parsimonious Gaussian Mixture Models
•bravo: Bayesian Screening and Variable Selection
•care: High\-Dimensional Regression and CAR Score Variable Selection
•dials: Tools for Creating Tuning Parameter Values
•EMVS: The Expectation\-Maximization Approach to Bayesian Variable Selection
•FeatureTerminatoR: Feature Selection Engine to Remove Features with Minimal Predictive Power
•FSinR: Feature Selection
•fsMTS: Feature Selection for Multivariate Time Series
•gausscov: The Gaussian Covariate Method for Variable Selection
•greybox: Toolbox for Model Building and Forecasting
•hrqglas: Group Variable Selection for Quantile and Robust Mean Regression
•knockoff: The Knockoff Filter for Controlled Variable Selection
•mBvs: Bayesian Variable Selection Methods for Multivariate Data
•MDFS: MultiDimensional Feature Selection
•mlr3fselect: Feature Selection for ’mlr3’
•mplot: Graphical Model Stability and Variable Selection Procedures
•MXM: Feature Selection (Including Multiple Solutions) and Bayesian Networks
•nestfs: Cross\-Validated (Nested) Forward Selection
91•NonpModelCheck: Model Checking and Variable Selection in Nonparametric Regression
•pcaPP: Robust PCA by Projection Pursuit
•picR: Predictive Information Criteria for Model Selection
•plsVarSel: Variable Selection in Partial Least Squares
•praznik: Tools for Information\-Based Feature Selection and Scoring
•prinvars: Principal Variables (methods for reducing the number of features within a data set)
•projpred: Projection Predictive Feature Selection
•Rforestry: Random Forests, Linear Trees, and Gradient Boosting for Inference and Interpretability
•rmcfs: The MCFS\-ID Algorithm for Feature Selection and Interdependency Discovery
•rSAFE: Surrogate\-Assisted Feature Extraction
•rstanarm: Bayesian Applied Regression Modeling via Stan
•SelectBoost: A General Algorithm to Enhance the Performance of Variable Selection Methods in Correlated
Datasets
•SignifReg: Consistent Significance Controlled Variable Selection in Generalized Linear Regression
•sivs: Stable Iterative Variable Selection
•smoothic: Variable Selection Using a Smooth Information Criterion
•SPlit: Split a Dataset for Training and Testing
•splitTools: Tools for Data Splitting
•stabiliser: Stabilising Variable Selection
•stabm: Stability Measures for Feature Selection
•stacks: Tidy Model Stacking
•stepgbm: Stepwise Variable Selection for Generalized Boosted Regression Modeling
•SWIM: Scenario Weights for Importance Measurement
•theft: Tools for Handling Extraction of Features from Time Series
•tornado: Plots for Model Sensitivity and Variable Importance
•valse: Variable Selection with Mixture of Models
•WLasso: Variable Selection for Highly Correlated Predictors
927\.36 Sensitivity analysis and numerical derivatives
Python software implementations
List of packages and/or codes and/or frameworks and/or links:
•derivative: Numerical differentiation of noisy time series data
•higher: obtain higher order gradients
•jacobi: Numerical derivatives for Python
•JAX: toolkit by Google for composable transformations of Python\+NumPy programs: differentiate, vectorize,
JIT to GPU/TPU, and more
•OMSens: OpenModelica sensitivity analysis and optimization module
•PyApprox: high\-dimensional approximation and uncertainty quantification by Sandia Labs
•SALib: Sensitivity Analysis Library (Contains Sobol, Morris, FAST, and other methods)
•sensitivity: Sensitivity Analysis
•tangent: library (by Google) for automatic differentiation providing Source\-to\-Source Debuggable Derivatives
in Pure Python
•torchsde: Differentiable SDE solvers with GPU support and efficient sensitivity analysis
R software implementations
List of packages and/or codes and/or frameworks and/or links:
•bnmonitor: An Implementation of Sensitivity Analysis in Bayesian Networks
•GSA.UN: Global Sensitivity Analysis Tool
•reval: Argument Table Generation for Sensitivity Analysis
•samon: Sensitivity Analysis for Missing Data
•sensemakr: Sensitivity Analysis Tools for Regression Models
•sensitivity: Global Sensitivity Analysis of Model Outputs
•sensobol: Computation of Variance\-Based Sensitivity Indices
•SWIM: Scenario Weights for Importance Measurement
•tornado: Plots for Model Sensitivity and Variable Importance
7\.37 Statistics and Probability
Python software implementations
List of packages and/or codes and/or frameworks and/or links:
•distfit: probability density function fitting and hypothesis testing
•empiricaldist: empirical distribution functions
•momentum: Running mean, variance, skew, and kurtosis
•pingouin: Statistical package in Python based on Pandas
•probs: Probability library
93•PyProbables: Probabilistic data structures in python
•PyStats: statistical analysis and distributions
•RunStats: Computing Statistics and Regression in One Pass
•statsmodels: statistical modeling and econometrics
•tensorflow\-probability: Probabilistic reasoning and statistical analysis in TensorFlow
•wquantiles: Weighted quantiles
R software implementations
List of packages and/or codes and/or frameworks and/or links:
•arsenal: An Arsenal of ’R’ Functions for Large\-Scale Statistical Summaries
•ashr: Methods for Adaptive Shrinkage, using Empirical Bayes
•confintr: Confidence Intervals
•DEM: The Distributed EM Algorithms in Multivariate Gaussian Mixture Models
•DescTools: Tools for Descriptive Statistics
•distr6: The Complete R6 Probability Distributions Interface
•distr: Object Oriented Implementation of Distributions
•distrEx: Extensions of Package ’distr’
•distributionsrd: Distribution Fitting and Evaluation
•DPQ: Density, Probability, Quantile (’DPQ’) Computations
•EasyDescribe: A Convenient Way of Descriptive Statistics
•entropy: Estimation of Entropy, Mutual Information and Related Quantities
•estimatr: Fast Estimators for Design\-Based Inference
•evd: Functions for Extreme Value Distributions
•expectreg: Expectile and Quantile Regression
•fitur: Fit Univariate Distributions
•fromo: Fast Robust Moments
•Gmedian: Geometric Median, k\-Medians Clustering and Robust Median PCA
•HSAUR3: A Handbook of Statistical Analyses Using R (3rd Edition)
•lmom: L\-Moments
•lmomco: L\-Moments, Censored L\-Moments, Trimmed L\-Moments, L\-Comoments, and Many Distributions
•matrixdist: Statistics for Matrix Distributions
•MatrixModels: Modelling with Sparse and Dense Matrices
•matrixStats: Functions that Apply to Rows and Columns of Matrices (and to Vectors)
•minsample2: The Minimum Sample Size
94•mlquantify: Algorithms for Class Distribution Estimation
•mvtnorm: Multivariate Normal and t Distributions
•NNS: Nonlinear nonparametric statistics using partial moments
•overlapping: Estimation of Overlapping in Empirical Distributions
•PCDimension: Finding the Number of Significant Principal Components
•philentropy: Similarity and Distance Quantification Between Probability Functions
•pls: Partial Least Squares and Principal Component Regression
•psre: Presenting Statistical Results Effectively
•Qest: Quantile\-Based Estimator
•qp: Quantile parametrization for probability distribution functions
•RcppRoll: Efficient Rolling / Windowed Operations
•revss: Robust Estimation in Very Small Samples
•RobStatTM: Robust Statistics: Theory and Methods
•robustbase: Basic Robust Statistics
•roll: Rolling and Expanding Statistics
•statsExpressions: Tidy Dataframes and Expressions with Statistical Details
•walrus: Robust Statistical Methods
•weights: Weighting and Weighted Statistics
7\.38 Stress testing, rare events, extreme values and scenarios, survival analysis
Python software implementations
List of packages and/or codes and/or frameworks and/or links:
•pyextremes: Extreme Value Analysis
•pycox is a python package for survival analysis and time\-to\-event prediction with PyTorch
•scikit\-extremes: univariate extreme value calculations
R software implementations
List of packages and/or codes and/or frameworks and/or links:
•BMAmevt: Multivariate Extremes: Bayesian Estimation of the Spectral Measure
•climextRemes: Tools for Analyzing Climate Extremes
•extRemes: Extreme Value Analysis
•extremeStat: Extreme Value Statistics and Quantile Estimation
•evd: Functions for Extreme Value Distributions
•evmix: Extreme Value Mixture Modelling, Threshold Estimation and Boundary Corrected Kernel Density
Estimation
95•ExtremalDep: Extremal Dependence Models
•ExtremeRisks: Extreme Risk Measures
•lax: Loglikelihood Adjustment for Extreme Value Models
•lite: Likelihood\-Based Inference for Time Series Extremes
•mev: Modelling of Extreme Values
•survivalmodels: Models for Survival Analysis
7\.39 Symbolic regression \&data\-driven model discovery and machine learning
Python software implementations
List of packages and/or codes and/or frameworks and/or links:
•2SEGP: Simple Simultaneous Ensemble Learning in Genetic Programming
•AIFeynman: Physics\-Inspired Method for Symbolic Regression
•BindingGP: Symbolic Regression with Dimension Calculation
•Data Driven Symbolic Regression
•DEAP: Distributed Evolutionary Algorithms
•DeepSymReg: Neural Network\-Based Symbolic Regression in Deep Learning for Scientific Discovery
•DeepSymRegTorch: PyTorch implementation of the EQL network, a neural network for symbolic regression
•Deep symbolic optimization
•diffeqpy: Solving differential equations in Python using DifferentialEquations.jl and the SciML Scientific
Machine Learning organization
•ellyn: python\-wrapped version of ellen, a linear genetic programming system for symbolic regression and
classification
•EQLearner: A Seq2Seq approach to Symbolic Regression
•ffx: Fast Function Extraction for symbolic regressio
•geppy: framework for gene expression programming
•gplearn: Genetic Programming in Python, with a scikit\-learn inspired API
•hal\-cgp: Cartesian genetic programming
•Neural Symbolic Regression That Scales
•pyglyph: library based on deap providing abstraction layers for symbolic regression problems
•pymbolic: Easy Expression Trees and Term Rewriting
•PySR: High\-Performance Symbolic Regression in Python
•PySINDy: sparse identification of nonlinear dynamical systems from data
•pySRURGS: Symbolic regression by uniform random global search
•salmon\-lm: symbolic algebra of linear regression and modeling
•slearn: package linking symbolic representation with scikit\-learn machine learning
96•SR Bench: benchmark framework for symbolic regression
•SymEngine is a fast symbolic manipulation library
•symfit: Symbolic Fitting; fitting as it should be.
•symbolic experiments: Repository for symbolic regression/classification experiments
•Symbolic Regression Boosting
•Simpy: symbolic mathematics
•symreg: A Symbolic Regression engine
R software implementations
List of packages and/or codes and/or frameworks and/or links:
•DiffEqR: Solving differential equations in R using DifferentialEquations.jl and the SciML Scientific Machine
Learning ecosystem
•gramEvol: Grammatical Evolution for R
•symbolicDA: Analysis of Symbolic Data
•symengine: Interface to the ’SymEngine’ Library
7\.40 Testing (numerical, statistical, etc.), comparison and ranking
Python software implementations
List of packages and/or codes and/or frameworks and/or links:
•AutoTS: Automated Time Series Forecasting
•darts: toolkit by Unit8 for easy manipulation and forecasting of time series
•goftests: Generic goodness of fit tests for random plain old data
•hypothesize: hypothesis testing using robust statistics
•hypothetical: Hypothesis and statistical testing
•hyppo: multivariate hypothesis testing
•InvarianceUnitTests: Linear unit\-tests for invariance discovery
•MAPIE: scikit\-learn\-compatible module for estimating prediction intervals.
•Merlion: A Machine Learning Framework for Time Series Intelligence by SalesForce
•permute: permutation tests and confidence sets
•PhiK: practical correlation constant that works consistently between categorical, ordinal and interval variables
•pingouin: Statistical package in Python based on Pandas
•responsible\-ai\-toolbox: Error Analysis dashboard, for identifying model errors and discovering cohorts of data
for which the model underperforms.
•RunStats: Computing Statistics and Regression in One Pass
•scikit\-learn: machine learning in Python
•statsmodels: statistical modeling and econometrics
•UltraNest: Fit and compare complex models reliably and rapidly. Advanced nested sampling.
•xskillscore: Metrics for verifying forecasts
97R software implementations
List of packages and/or codes and/or frameworks and/or links:
•ACV: Optimal Out\-of\-Sample Forecast Evaluation and Testing under Stationarity
•amp: Statistical Test for the Multivariate Point Null Hypotheses
•ashr: Methods for Adaptive Shrinkage, using Empirical Bayes
•bayefdr: Bayesian Estimation and Optimisation of Expected False Discovery Rate
•BEST: Bayesian Estimation Supersedes the t\-Test
•BFpack: Flexible Bayes Factor Testing of Scientific Expectations
•blocklength: Select an Optimal Block\-Length to Bootstrap Dependent Data (Block Bootstrap)
•boot: Bootstrap Functions
•boot.pval: Bootstrap p\-Values
•bootUR: Bootstrap Unit Root Tests
•CADFtest: A Package to Perform Covariate Augmented Dickey\-Fuller Unit Root Tests
•ChangepointTesting: Change Point Estimation for Clustered Signals
•clusrank: Wilcoxon Rank Tests for Clustered Data
•cocor: Comparing Correlations
•corTESTsrd: Significance Testing of Rank Cross\-Correlations under SRD
•CovTools: Statistical Tools for Covariance Analysis
•crossvalidationCP: Cross\-Validation for Change\-Point Regression
•crseEventStudy: A Robust and Powerful Test of Abnormal Stock Returns in Long\-Horizon Event Studies
•cvCovEst: Cross\-Validated Covariance Matrix Estimation
•cvms: Cross\-Validation for Model Selection
•CVST: Fast Cross\-Validation via Sequential Testing
•dgof: Discrete Goodness\-of\-Fit Tests
•digitTests: Tests for Detecting Irregular Digit Patterns
•DiscreteFDR: Multiple Testing Procedures with Adaptation for Discrete Tests
•dsos: Dataset Shift with Outlier Scores
•elo: Ranking Teams by Elo Rating and Comparable Methods
•energy: E\-Statistics: Multivariate Inference via the Energy of Data
•exactRankTests: Exact Distributions for Rank and Permutation Tests
•FactorAssumptions: Set of Assumptions for Factor and Principal Component Analysis
•FAMT: Factor Analysis for Multiple Testing (FAMT) : Simultaneous Tests under Dependence in High\-
Dimensional Data
•fbst: The Full Bayesian Evidence Test, Full Bayesian Significance Test and the e\-Value
98•fdrci: Permutation\-Based FDR Point and Confidence Interval Estimation
•FDRestimation: Estimate, Plot, and Summarize False Discovery Rates
•funtimes: Nonparametric estimators and tests for time series analysis
•fwb: Fractional Weighted Bootstrap
•fwildclusterboot: Fast Wild Cluster Bootstrap Inference for Linear Models
•gvlma: Global Validation of Linear Models Assumptions
•gt: Easily Create Presentation\-Ready Display Tables
•gtExtras: Extending ’gt’ for Beautiful HTML Tables
•heplots: Visualizing Hypothesis Tests in Multivariate Linear Models
•HSAUR3: A Handbook of Statistical Analyses Using R (3rd Edition)
•htestClust: Reweighted Marginal Hypothesis Tests for Clustered Data
•ICtest: Estimating and Testing the Number of Interesting Components in Linear Dimension Reduction
•inferr: Inferential Statistics (parametric and non\-parametric statistical tests)
•L2DensityGoFtest: Density Goodness\-of\-Fit Test
•locits: Test of Stationarity and Localized Autocovariance
•mashr: Multivariate Adaptive Shrinkage
•mcStats: Visualize Results of Statistical Hypothesis Tests
•melt: Multiple Empirical Likelihood Tests
•metrica: evaluate prediction performance of point\-forecast models
•MixedIndTests: Tests of Randomness and Tests of Independence
•modeltime.resample: Resampling Tools for Time Series Forecasting
•MSTest: Hypothesis Testing for Markov Switching Models
•multDM: Multivariate Version of the Diebold\-Mariano Test
•MultiFit: Multiscale Fisher’s Independence Test for Multivariate Dependence
•MultiHorizonSPA: Multi Horizon Superior Predictive Ability
•multiverse: ’Explorable Multiverse’ Data Analysis and Reports to show the robustness of statistical inference
•MVTests: Multivariate Hypothesis Tests and the confidence intervals
•nestedcv: Nested Cross\-Validation with ’glmnet’ and ’caret’
•NonParRolCor: a Non\-Parametric Statistical Significance Test for Rolling Window Correlation
•OOS: Out\-of\-Sample Time Series Forecasting
•origami: Generalized Framework for Cross\-Validation
•OptSig: Optimal Level of Significance for Regression and Other Statistical Tests
•OPTtesting: Optimal Testing
99•OutliersO3: Draws Overview of Outliers (O3\) Plots
•pbo: Probability of Backtest Overfitting
•performance: Assessment of Regression Models Performance
•permutes: Permutation Tests for Time Series Data
•poolr: Methods for Pooling P\-Values from (Dependent) Tests
•portes: Portmanteau Tests for Univariate and Multivariate Time Series Models
•randtoolbox: Toolbox for Pseudo and Quasi Random Number Generation and Random Generator Tests
•RDieHarder: R Interface to the ’DieHarder’ RNG Test Suite
•RDnp: Robust Test for Complete Independence in High\-Dimensions
•rigr: Regression, Inference, and General Data Analysis Tools in R
•Rita: Automated Transformations, Normality Testing, and Reporting
•rmcorr: Repeated Measures Correlation
•RobustANOVA: Robust One\-Way ANOVA Tests under Heteroscedasticity and Nonnormality
•robusTest: Calibrated Correlation, Two\-Sample Tests
•rsample: General Resampling Infrastructure
•rstatix: Pipe\-Friendly Framework for Basic Statistical Tests
•s2dverification: Set of Common Tools for Forecast Verification
•scoringfunctions: A Collection of Scoring Functions for Assessing Point Forecasts
•scoringRules: Scoring Rules for Parametric and Simulated Distribution Forecasts
•scoringutils: Utilities for Scoring and Assessing Predictions
•sdafilter: distribution free multiple testing rules for false discovery rate (FDR) control under general depen\-
dence
•sgof: Multiple Hypothesis Testing
•SHT: Statistical Hypothesis Testing Toolbox
•slider: Sliding Window Functions
•SlidingWindows: Methods for Time Series Analysis
•SPlit: Split a Dataset for Training and Testing
•splitTools: Tools for Data Splitting
•statsExpressions: Tidy Dataframes and tests (parametric, nonparametric, robust, etc)
•tidyposterior: Bayesian Analysis to Compare Models using Resampling Statistics
•tidystats: Save Output of Statistical Tests
•UnitStat: Performs Unit Root Test Statistics
•urca: Unit Root and Cointegration Tests for Time Series Data
•USP: U\-Statistic Permutation Tests of Independence for all Data Types
•walrus: Robust Statistical Methods
•yardstick: Tidy Characterizations of Model Performance
1007\.41 Testing software codes
Python software implementations
List of packages and/or codes and/or frameworks and/or links:
•benchmark: microbenchmark support library
•bugsnag error monitoring and error reporting
•case: Python unittest Utilities
•cxxtest: CxxTest Unit Testing Framework
•dirty\-equals: make python code (generally unit tests) more declarative and therefore easier to read and write.
•expectest: implements expect tests (also known as ”golden” tests)
•formencode: validation and form generation
•freezegun: allows your Python tests to travel through time by mocking the datetime module
•green: clean, colorful, fast python test runner
•Hypothesis: family of testing libraries which let you write tests parametrized by a source of examples
•Mamba Test Runner: definitive testing tool for Python
•mutattest: Safely run mutation trials without source code modifications and see what will get past your test
suite.
•nose2: unittest with plugins.
•nox: Flexible test automation for Python
•partialtesting: toolkit by Man Group to run only the tests relevant for code changes
•playwright\-python: Python version of the Playwright testing and automation library
•Pynguin: PYthoN General UnIt Test geNerator
•pyperformance: intended to be an authoritative source of benchmarks for all Python implementations
•pytest: easy to write small tests, yet scales to support complex functional testing
•pytest\-benchmark: py.test fixture for benchmarking code
•pytest\-check: pytest plugin that allows multiple failures per test.
•pytest\-html: Plugin for generating HTML reports for pytest results
•pytest\-parallel: pytest plugin for parallel and concurrent testing
•pytest\-regressions: Pytest plugin for regression testing
•stestr: parallel Python test runner built around subunit
•TestSlide: test framework by Facebook
•testtools: extensions to the Python standard library’s unit testing framework.
•tox: Command line driven CI frontend and development task automation tool
•ward: modern test framework for Python with a focus on productivity and readability.
101R software implementations
List of packages and/or codes and/or frameworks and/or links:
•exampletestr: Help for Writing Unit Tests Based on Function Examples
•melt: Multiple Empirical Likelihood Tests
•mockthat: Function Mocking for Unit Testing
•patrick: Parameterized Unit Testing by Google
•realtest: When Expectations Meet Reality: Realistic Unit Testing
•shinytest2: Testing for Shiny Applications
•testdat: Data Unit Testing for R
•testthat: Unit Testing for R
•testthis: Utils and ’RStudio’ Addins to Make Testing Even More Fun
•ttdo: Extend ’tinytest’ with ’diffobj’
•unitizer: Interactive R Unit Tests
•unittest: TAP\-Compliant Unit Testing
•xpectr: Generates Expectations for ’testthat’ Unit Testing
7\.42 Time series analysis and modeling
Collections of resources
List of links:
•Curated list with python packages for time series analysis
•Popular Python Time Series Packages
•Resources for working with time series and sequence data
Python software implementations
List of packages and/or codes and/or frameworks and/or links:
•Clairvoyance: Unified, End\-to\-End AutoML Pipeline for Medical Time Series
•darts: toolkit by Unit8 for easy manipulation and forecasting of time series
•DataGene: Identify How Similar TS Datasets Are to One Another
•deeptime: analysis of time series data including dimensionality reduction, clustering, and Markov model
estimation
•EntropyHub: open\-source toolkit for entropic time\-series analysis.
•ETNA Time Series Library by Tinkoff AI
•fastreg: Fast sparse regressions with advanced formula syntax. OLS, GLM, Poisson, Maxlike, and more.
High\-dimensional fixed effects
•Featuretools: automated feature engineering
•glum: Generalized linear models
102•hcrystalball: unifies the API for most commonly used libraries and modeling techniques for time\-series fore\-
casting in the Python ecosystem
•HyperTools: toolbox for gaining geometric insights into high\-dimensional data
•HyperTS: Full\-Pipeline Automated Time Series (AutoTS) Analysis Toolkit
•kats: tookit by Facebook for time series analysis and forecasting
•KFAS: Kalman Filter and Smoother for Exponential Family State Space Models
•khiva\-python: Python binding for Khiva library for time series analytics
•Loud ML: inference engine for metrics and events
•luminaire: ML driven solutions for monitoring time series data
•matrixprofile\-ts: detect patterns and anomalies in massive datasets using Matrix Profile
•MatrixStats: Methods that Apply to Rows and Columns of Matrices (and to Vectors)
•mkl\_fft: NumPy\-based Python interface to Intel (R) MKL FFT functionality
•nixtla: Automated time series processing and forecasting
•pandas: data structures for data analysis, time series, and statistics
•pyFFTW is a pythonic wrapper around FFTW 3, the speedy FFT library
•pyFIt\-SNE: FFT\-accelerated Interpolation\-based t\-SNE (FIt\-SNE)
•pyts: time series classification
•pytsal: Time Series analysis, visualization, forecasting along with AutoTS
•seglearn: machine learning for time series
•sktime: unified framework for machine learning with time series by UK national institute for data science and
artificial intelligence
•slearn: package linking symbolic representation with scikit\-learn machine learning
•statsmodels: statistical modeling and econometrics
•stumpy: variety of time series data mining tasks
•theft: Tools for Handling Extraction of Features from Time Series
•timemachines: Evaluation and standardization of popular time series packages
•timetk: A Tool Kit for Working with Time Series in R
•Traces: library for unevenly\-spaced time series analysis
•tsai: time series tasks like classification, regression, forecasting, imputation
•tsam: time series aggregation module (tsam)
•ts\-eval: Time Series analysis and evaluation tools
•tsfresh: extracts relevant characteristics from time series
•tslearn: machine learning toolkit dedicated to time\-series data
•tspreprocess: package to preprocess time series
•tsmoothie: time\-series smoothing and outlier detection in a vectorized way
•vectorbt: library for backtesting and analyzing trading strategies at scale
103R software implementations
List of packages and/or codes and/or frameworks and/or links:
•ASSA: Applied Singular Spectrum Analysis
•astsa: Applied Statistical Time Series Analysis
•autostsm: Automatic Structural Time Series Models
•bdots: Bootstrapped Differences of Time Series
•bfast: Breaks for Additive Season and Trend
•bimets: Time Series and Econometric Modeling
•bootUR: Bootstrap Unit Root Tests
•ctbi: A Procedure to Clean, Decompose and Aggregate Timeseries
•energy: E\-Statistics: Multivariate Inference via the Energy of Data
•entropy: Estimation of Entropy, Mutual Information and Related Quantities
•freqdom: Frequency Domain Based Analysis: Dynamic PCA
•funtimes: Functions for Time Series Analysis
•garchx: Flexible and Robust GARCH\-X Modelling
•LMD: A Self\-Adaptive Approach for Demodulating Multi\-Component Signal
•LSTS: Locally Stationary Time Series
•lubridate: Make Dealing with Dates a Little Easier
•mcvis: Multi\-Collinearity Visualization
•MixedIndTests: Tests of Randomness and Tests of Independence
•MTS: All\-Purpose Toolkit for Analyzing Multivariate Time Series (MTS) and Estimating Multivariate Volatil\-
ity Models
•NonlinearTSA: Nonlinear Time Series Analysis
•nonlinearTseries: Nonlinear Time Series Analysis
•nortsTest: Assessing Normality of Stationary Process
•NTS: Nonlinear Time Series Analysis
•Rfssa: Functional Singular Spectrum Analysis
•rhosa: Higher\-Order Spectral Analysis
•rrcov: Scalable Robust Estimators with High Breakdown Point
•rrMixture: Reduced\-Rank Mixture Models
•Rssa: A Collection of Methods for Singular Spectrum Analysis
•rtrend: Trend Estimating Tools
•Rwave: Time\-Frequency Analysis of 1\-D Signals
•seastests: Seasonality Tests
104•shrink: Global, Parameterwise and Joint Shrinkage Factor Estimation
•simts: Time Series Analysis Tools
•SLBDD: Statistical Learning for Big Dependent Data
•svars: Data\-Driven Identification of SVAR Models
•tempdisagg: Temporal Disaggregation and Interpolation of Time Series
•theft: Tools for Handling Extraction of Features from Time Series
•TidyDensity: Functions for Tidy Analysis and Generation of Random Data
•timetk: A Tool Kit for Working with Time Series in R
•TSA: Time Series Analysis
•tsbox: Class\-Agnostic Time Series
•tscopula: Time Series Copula Models
•tseries: Time Series Analysis and Computational Finance
•TSrepr: Time Series Representations
•tsrobprep: Robust Preprocessing of Time Series Data
•TSstudio: Functions for Time Series Analysis and Forecasting
•tsutils: Time Series Exploration, Modelling and Forecasting
•tsviz: Easy and Interactive Time Series Visualization
•vars: VAR Modelling
•xts: eXtensible Time Series
7\.43 Text, sentiment and topic analytics (including NLP)
Python software implementations
•AllenNLP: toolkit by Allen Institute of Articial Intelligence for NLP research
•EmTract: Extracting Emotions from Social Media Text Tailored for Financial Contexts
•EvoMSA: Sentiment Analysis System based on B4MSA and EvoDAG
•fairseq: Facebook AI Research Sequence\-to\-Sequence Toolkit
•FastFormers: toolkit by Microsoft to achieve inference of Transformer models for Natural Language Under\-
standing
•gensim: topic modelling, document indexing and similarity retrieval with large corpora
•GPT\-3: Language Models are Few\-Shot Learners
•LIT: Language Interpretability Tool: Interactively analyze NLP models for model understanding
•LangTech Text Library (LTTL) is an open\-source python package for text processing and analysis.
•Natural Language Processing Best Practices and Examples by Microsoft
•netts: toolkit by UK national institute for data science and artificial intelligence for creating networks cap\-
turing semantic content of speech transcripts
105•nlpaug: Data augmentation for NLP
•nltk: Natural Language Toolkit
•pytext: A natural language modeling framework based on PyTorch
•PyTorch\-NLP: Basic Utilities for PyTorch Natural Language Processing (NLP)
•Senta: Baidu’s open\-source Sentiment Analysis System.
•spaCy: Industrial\-strength Natural Language Processing (NLP) in Python
•stocksight: Stock market analyzer and predictor using Elasticsearch, Twitter, News headlines, NLP and
sentiment analysis
•sumy: automatic summarization of text documents and HTML pages
•textacy: NLP, before and after spaCy
•vaderSentiment: VADER (Valence Aware Dictionary and sEntiment Reasoner) is a lexicon and rule\-based
sentiment analysis tool
•wordfreq: Access a database of word frequencies, in various natural languages.
R software implementations
•cleanNLP: Tidy Data Model for Natural Language Processing
•doc2concrete: Measuring Concreteness in Natural Language
•fastTextR: An Interface to the ’fastText’ Library
•globaltrends: Google Trends portal.
•lsa: Latent Semantic Analysis
•LSX: Model for Semisupervised Text Analysis Based on Word Embeddings
•meanr: Sentiment Analysis Scorer
•NLP: Natural Language Processing Infrastructure
•opitools: Analyzing the Opinions in a Big Text Document
•quanteda: Quantitative Analysis of Textual Data
•saotd: Sentiment Analysis of Twitter Data
•sentiment.ai: Simple Sentiment Analysis Using Deep Learning
•SentimentAnalysis: Dictionary\-Based Sentiment Analysis
•sentimentr: Calculate Text Polarity Sentiment
•sentometrics: Integrated Framework for Textual Sentiment Time Series Aggregation and Prediction
•spacyr: Wrapper to the ’spaCy’ ’NLP’ Library
•sweater: Speedy Word Embedding Association Test and Extras Using R
•syuzhet: Extracts Sentiment and Sentiment\-Derived Plot Arcs from Text
•tau: Text Analysis Utilities
•text2map: R Tools for Text Matrices, Embeddings, and Networks
106•text2sdg: Detecting UN Sustainable Development Goals in Text
•text2vec: Modern Text Mining Framework for R
•texter: An Easy Text and Sentiment Analysis Library
•TextForecast: Regression Analysis and Forecasting Using Textual Data from a Time\-Varying Dictionary
•textTinyR: Text Processing for Small or Big Data Files
•tidytext: Text Mining using ’dplyr’, ’ggplot2’, and Other Tidy Tools
•transforEmotion: Sentiment Analysis for Text and Qualitative Data
•tsentiment: Fetching Tweet Data for Sentiment Analysis
•Xplortext: Statistical Analysis of Textual Data
7\.44 Uncertainty: analysis and modeling
Links to resources
•Professionally curated list of awesome Conformal Prediction videos, tutorials, books, papers, PhD and MSc
theses, articles and open\-source libraries
Python software implementations
List of packages and/or codes and/or frameworks and/or links:
•Bumps: data fitting and uncertainty estimation
•conformal\-rnn: code for ”Conformal time\-series forecasting”, NeurIPS 2021
•crepes: Conformal Regressors and Conformal Predictive Systems
•EasyVVUQ: verification, validation and uncertainty quantification in high performance computing
•EnbPI: Ensemble batch prediction intervals
•EnCQR: ensemble conformalized quantile regression (EnCQR)
•MAPIE: scikit\-learn\-compatible module for estimating prediction intervals
•mystic: highly\-constrained non\-convex optimization and uncertainty quantification
•OpenTURNS (Open source initiative to Treat Uncertainties, Risks’N Statistics)
•PySloth: Probabilistic Prediction
•UncertaintyToolbox: predictive uncertainty quantification, calibration, metrics, and visualization
•UQpy: UQpy (Uncertainty Quantification with python) is a general purpose Python toolbox for modeling
uncertainty in physical and mathematical systems
R software implementations
List of packages and/or codes and/or frameworks and/or links:
•bootComb: Combine Parameter Estimates via Parametric Bootstrap
1077\.45 Visualization and reporting
Python software implementations
List of packages and/or codes and/or frameworks and/or links:
•Algviz is an algorithm visualization tool for your Python code
•appmode: Jupyter extension that turns notebooks into web applications
•Best of Streamlit
•clustergram: Visualization and diagnostics for cluster analysis in Python
•dash: framework for building ML and data science web apps
•dash\-extensions:extensions to the Plotly Dash framework
•D\-tale:Visualizer by Man Group for pandas data structures
•FlameScope: visualization ny Netflix for exploring different time ranges as Flame Graphs.
•HyperTools: toolbox for gaining geometric insights into high\-dimensional data
•ipyslides: Create Interactive Slides in Jupyter Notebook with all kind of rich content
•itables: Pandas DataFrames as Interactive DataTables
•Lux: automate the visualization and data analysis process
•Markdown: Python implementation of markdown
•matplotlib: omprehensive library for creating static, animated, and interactive visualizations
•mpl\-animators: interative animation framework for matplotlib
•Orange: Interactive data analysis
•plotly: graphing library makes interactive, publication\-quality graphs
•Plotly Resampler: Visualize large time\-series data in plotly
•plotnine: A grammar of graphics for Python
•plottable: Beautifully customized tables with matplotlib
•psyplot: interactive data visualization
•PyGraphistry: quickly load, shape, embed, and explore big graphs with the GPU\-accelerated Graphistry
visual graph analyzer
•PyMetis: Python wrapper around Metis, a graph partitioning package
•PyShiny: Shiny for Python
•pyvis: visualizing interactive network graphs
•seaborn: statistical data visualization
•seaborn analyzer: data analysis and visualization tool using Seaborn library
•streamlit: fastest way to build and share data apps
•tensorboard: TensorFlow’s Visualization Toolkit
•torchsde: Differentiable SDE solvers with GPU support and efficient sensitivity analysis
108•tourr: Tour Methods for Multivariate Data Visualisation
•Vega\-Altair is a declarative statistical visualization library for Pytho
•VisPy: interactive scientific visualization in Python
•visdom: lexible tool for creating, organizing, and sharing visualizations of live, rich data
R software implementations
List of packages and/or codes and/or frameworks and/or links:
•apexcharter: Create Interactive Chart with the JavaScript ’ApexCharts’ Library
•autoplotly: Automatic Generation of Interactive Visualizations for Statistical Results
•classmap: Visualizing Classification Results
•cleanrmd: Clean Class\-Less ’R Markdown’ HTML Documents
•clustree: Visualise Clusterings at Different Resolutions
•ComplexUpset: Create Complex UpSet Plots Using ’ggplot2’ Components
•condformat: Conditional Formatting in Data Frames
•conductor: Create Tours in ’Shiny’ Apps Using ’Shepherd.js’
•d3po: Fast and Beautiful Interactive Visualization for ’Markdown’ and ’Shiny’
•DataVisualizations: Visualizations of High\-Dimensional Data
•descriptr: Generate Descriptive Statistics
•DT: A Wrapper of the JavaScript Library ’DataTables’
•echarty: Minimal R/Shiny Interface to JavaScript Library ’ECharts’
•esquisse: Explore and Visualize Your Data Interactively
•fmtr: Easily Apply Formats to Data
•ggalluvial: Alluvial Plots in ’ggplot2’
•GGally: Extension to ’ggplot2’
•gganimate: A Grammar of Animated Graphics
•ggbreak: Set Axis Break for ’ggplot2’
•ggcharts: Shorten the Distance from Data Visualization Idea to Actual Plot
•ggcorrplot: Visualization of a Correlation Matrix using ’ggplot2’
•ggcorset: The Corset Plot
•ggdag: Analyze and Create Elegant Directed Acyclic Graphs
•ggdist: Visualizations of Distributions and Uncertainty
•ggDoubleHeat: A Heatmap\-Like Visualization Tool
•ggeffects: Create Tidy Data Frames of Marginal Effects for ’ggplot’ from Model Outputs
•ggESDA: Exploratory Symbolic Data Analysis with ’ggplot2’
109•ggfocus: Scales that Focus Specific Levels in your ggplot
•ggforce: Accelerating ’ggplot2’
•ggformula: Formula Interface to the Grammar of Graphics
•ggfortify: Data Visualization Tools for Statistical Analysis Results
•gghdr: Visualisation of Highest Density Regions in ’ggplot2’
•ggheatmap: Plot Heatmap
•gghighlight: Highlight Lines and Points in ’ggplot2’
•ggh4x: Hacks for ’ggplot2’
•ggiraph: Make ’ggplot2’ Graphics Interactive
•ggmatplot: Plot Columns of Two Matrices Against Each Other Using ’ggplot2’
•ggmice: Visualizations for ’mice’ with ’ggplot2’
•ggmosaic: Mosaic Plots in the ’ggplot2’ Framework
•ggmulti: High Dimensional Data Visualization
•ggnetwork: Geometries to Plot Networks with ’ggplot2’
•ggpattern: ’ggplot2’ Pattern Geoms
•ggpie: pie, donut and rose pie plots with ggplot2
•ggplot2: Create Elegant Data Visualisations Using the Grammar of Graphics
•ggplotify: Convert Plot to ’grob’ or ’ggplot’ Object
•ggpmisc: Miscellaneous Extensions to ’ggplot2’
•ggpubr: ’ggplot2’ Based Publication Ready Plots
•ggpval: Annotate Statistical Tests for ’ggplot2’
•ggquickeda: Quickly Explore Your Data Using ’ggplot2’ and ’table1’ Summary Tables
•ggside extends ’ggplot2’ by allowing users to add graphical information about one of the main panel’s axis
using a familiar ’ggplot2’ style API with tidy data
•ggsignif: Significance Brackets for ’ggplot2’
•ggstance: Horizontal ’ggplot2’ Components
•ggstar: Multiple Geometric Shape Point Layer for ’ggplot2’
•ggstatsplot: ’ggplot2’ Based Plots with Statistical Details
•ggthemes: Extra Themes, Scales and Geoms for ’ggplot2’
•ggtrace: Provides ggplot2 geoms that allow groups of data points to be outlined or highlighted for emphasis
•gluedown: Wrap Vectors in Markdown Formatting
•gridstackeR: easy way to create responsive layouts with just a few lines of code using gridstack.js
•gt: Easily Create Presentation\-Ready Display Tables
•gtExtras: additional functions for creating tables with gt
110•gtsummary: Presentation\-Ready Data Summary and Analytic Result Tables
•heatmaply: Interactive Cluster Heat Maps Using ’plotly’ and ’ggplot2’
•heplots: Visualizing Hypothesis Tests in Multivariate Linear Models
•htmlTable: Advanced Tables for Markdown/HTML
•huxtable: Easily Create and Style Tables for LaTeX, HTML and Other Formats
•jjAnno: An Annotation Package for ’ggplot2’ Output
•kableExtra: Construct Complex Table with ’kable’ and Pipe Syntax
•listdown: Create R Markdown from Lists
•loon: Interactive Statistical Data Visualization
•loon.ggplot: A Grammar of Interactive Graphics
•magick: Advanced Graphics and Image\-Processing in R
•memoiR: R Markdown and Bookdown Templates to Publish Documents
•ndtv: Network Dynamic Temporal Visualizations
•numform: Tools to Format Numbers for Publication
•performance: Assessment of Regression Models Performance
•plot.matrix: Visualizes a Matrix as Heatmap
•presenter: Present Data with Style
•prompter: Add Tooltips in ’Shiny’ Apps with ’Hint.css’
•psre: Presenting Statistical Results Effectively
•quarto: R Interface to ’Quarto’ Markdown Publishing System
•r2resize: In\-Text Resizing for Containers, Images and Data Tables in ’Shiny’, ’Markdown’ and ’Quarto’
Documents
•r3js: allow WebGL\-based 3D plotting using the three.js library
•reactR: Make it easy to use ’React’ in R with ’htmlwidget’ scaffolds
•reporter: Creates Statistical Reports
•rheroicons: A Zero Dependency ’SVG’ Icon Library for ’Shiny’
•rhino: A Framework for Enterprise Shiny Applications
•rintrojs: Wrapper for the ’Intro.js’ Library
•rmarkdown: Dynamic Documents for R
•rsvg: Render SVG Images into PDF, PNG, (Encapsulated) PostScript, or Bitmap Arrays
•semantic.dashboard: Dashboard with Fomantic UI Support for Shiny
•shapviz: visualize SHapley Additive exPlanations (SHAP) \- waterfall, force, importance, dependence plots
•shiny: Web Application Framework for R
•shinyChakraUI: A Wrapper of the ’React’ Library ’Chakra UI’ for ’Shiny’
111•shinydlplot: Add a Download Button to a ’shiny’ Plot or ’plotly’
•shinyHugePlot: Efficient Plotting of Large\-Sized Data
•shinyMobile: Mobile Ready ’shiny’ Apps with Standalone Capabilities
•shinySelect: A Wrapper of the ’react\-select’ Library
•shiny.semantic: Semantic UI Support for Shiny
•shinytest: Test Shiny Apps
•shinyWidgets: Custom Inputs Widgets for Shiny
•starry: Explore Data with Plots and Tables
•statsExpressions: Tidy Dataframes and Expressions with Statistical Details
•sugrrants: Supporting Graphs for Analysing Time Series
•tidybayes: Tidy Data and ’Geoms’ for Bayesian Models
•tidycharts: Generate Tidy Charts Inspired by ’IBCS’
•tidyHeatmap: A Tidy Implementation of Heatmap
•tourr: Tour Methods for Multivariate Data Visualisation
•tornado: Plots for Model Sensitivity and Variable Importance
•trelliscopejs: Create Interactive Trelliscope Displays
•tsviz: Easy and Interactive Time Series Visualization
•UpSetR: A More Scalable Alternative to Venn and Euler Diagrams for Visualizing Intersecting Sets
•visNetwork: Network Visualization using ’vis.js’ Library
•visStatistics: Automated Visualization of Statistical Tests
•vtable: Variable Table for Variable Documentation
•xaringan: Presentation Ninja
•yardstick: Tidy Characterizations of Model Performance
8 Codes for QWIM (Quantitative Wealth and Investment Manage\-
ment)
8\.1 Collections of resources
List of links:
•Curated list of practical financial machine learning tools and applications
•EliteQuant: online resources for quantitative modeling, trading, portfolio management
1128\.2 Research studies with code
Ardia et al. (“RiskPortfolios: Computation of Risk\-Based Portfolios in R,” 2017\)
Boileau et al. (“cvCovEst: Cross\-validated covariance matrix estimator selection and evaluation in R,” 2021\)
Brugiere ( Quantitative Portfolio Management with Applications in Python , 2020\)
Bryzgalova et al. (“Forest Through the Trees: Building Cross\-Sections of Stock Returns,” 2021\)
Cajas (“Entropic Portfolio Optimization: a Disciplined Convex Programming Framework,” 2021\)
Cajas (“OWA Portfolio Optimization: a Disciplined Convex Programming Framework,” 2021\)
Chen and Zimmermann (“Open Source Cross\-Sectional Asset Pricing,” 2022\)
Chib (R package czfactor , 2020\)
Chib and Zhao ( R package czzg , 2020\)
Coqueret and Guida ( Machine Learning for Factor Investing: R Version , 2020\)
Coqueret ( Perspectives in sustainable equity investing (website version) , 2022\)
de Carvalho and Rua (“Real\-time nowcasting the US output gap: Singular spectrum analysis at work,” 2017\)
Ding et al. (“A Python package for multi\-stage stochastic programming,” 2020\)
Dixon et al. ( Machine Learning in Finance: from theory to practice , 2020\)
Dixon and Polson (“Deep Fundamental Factor Models,” 2020\)
Dong et al. (“Anomalies and the expected market return,” 2022\)
Guijarro\-Ordonez et al. (“Deep Learning Statistical Arbitrage,” 2021\)
Gurdogan and Kercheval (“Multi Anchor Point Shrinkage for the Sample Covariance Matrix (Extended Ver\-
sion),” 2021\)
Ho et al. (“Moving beyond P values: data analysis with estimation graphics,” 2019\)
Irlam (“Multi Scenario Financial Planning via Deep Reinforcement Learning AI,” 2020\)
Irlam (AI Planner , 2020\)
Irlam (“Machine learning for retirement planning,” 2020\)
Jansen (Machine Learning for Algorithmic Trading (Second Edition) , 2020\)
Kakushadze and Yu (“Statistical Risk Models,” 2016\)
Kakushadze and Yu (“Open Source Fundamental Industry Classification,” 2017\)
Kakushadze and Yu (“Betas, Benchmarks, and Beating the Market,” 2018\)
Kakushadze and Yu (“Decoding stock market with quant alphas,” 2018\)
Kakushadze and Yu (“Machine learning risk models,” 2019\)
Kakushadze and Yu (“Machine learning treasury yields,” 2020\)
Lai et al. (“TODS: An Automated Time Series Outlier Detection System,” 2021\)
Lettau and Pelger (“Factors That Fit the Time Series and Cross\-Section of Stock Returns,” 2020\)
Li et al. (“FinRL\-Podracer: High Performance and Scalable Deep Reinforcement Learning for Quantitative
Finance,” 2021\)
Liu et al. (“FinRL: Deep Reinforcement Learning Framework to Automate Trading in Quantitative Finance,”
2021\)
Liu et al. (“FinRL\-Meta: A Universe of Near\-Real Market Environments for Data\-Driven Deep Reinforcement
Learning in Quantitative Finance,” 2022\)
Marinescu (“Risk\-Based Optimal Portfolio Strategies: A Compendium,” 2022\)
Martin (“PyPortfolioOpt: portfolio optimization in Python,” 2021\)
Marwood and Minnen (“Safely Boosting Retirement Income by Harmonizing Drawdown Paths,” 2020\)
McIndoe (“A Data Driven Approach to Market Regime Classification,” 2020\)
Micheli and Neuman (“Evidence of Crowding on Russell 3000 Reconstitution Events,” 2022\)
Milevsky ( Retirement Income Recipes in R: From Ruin Probabilities to Intelligent Drawdowns , 2020\)
Qian et al. (“Combining forecasts for universally optimal performance,” 2022\)
Rao and Jelvis ( Foundations of Reinforcement Learning with Applications in Finance , 2022\)
Sarmas et al. ( Multicriteria Portfolio Construction with Python , 2020\)
Sharma et al. (“DoWhy: Addressing Challenges in Expressing and Validating Causal Assumptions,” 2021\)
Shi et al. (“Deep Learning Algorithms for Hedging with Frictions,” 2022\)
Siebert et al. (“A systematic review of Python packages for time series analysis,” 2021\)
Simos et al. (“Time\-varying Black–Litterman portfolio optimization using a bio\-inspired approach and neu\-
ronets,” 2021\)
Snow (“Machine learning in asset management,” 2019\)
113Snow (“Machine Learning in Asset Management Part 1: Portfolio Construction Trading Strategies,” 2020\)
Snow (“Machine Learning in Asset Management \- Part 2: Portfolio Construction \- Weight Optimization,” 2020\)
Tatsat et al. ( Machine Learning and Data Science Blueprints for Finance: From Building Trading Strategies to
Robo\-Advisors Using Python , 2020\)
Tuck et al. (“Portfolio Construction Using Stratified Models,” 2022\)
Ungolo et al. (“affine\_mortality: A Github repository for estimation, analysis, and projection of affine mortality
models,” 2021\)
Vamossy and Skog (“EmTract: Investor Emotions and Market Behavior,” 2021\)
Vinod (“R Package GeneralCorr Functions for Portfolio Choice,” 2021\)
Yang et al. (“FinBERT: A Pretrained Language Model for Financial Communications,” 2020\)
Yu et al. (“An AI approach to measuring financial risk,” 2020\)
8\.3 Python software implementations
List of packages and/or codes and/or frameworks and/or links:
•alive\-progress: new kind of Progress Bar, with real\-time throughput, ETA, and very cool animations
•alphalens: Performance analysis of predictive (alpha) stock factors
•AlphaPy: Automated Machine Learning \[AutoML] with Python, scikit\-learn, Keras, XGBoost, LightGBM,
and CatBoost
•auquantoolbox: Backtesting toolbox for trading strategies
•azapy: Financial Portfolio Optimization Algorithms
•bt: flexible backtesting framework
•btgym: Scalable, event\-driven, deep\-learning\-friendly backtesting library
•Clairvoyant: identify and monitor social/historical cues for short term stock movement
•CVXPortfolio: Portfolio optimization and simulation
•cyanure: Toolbox for Empirical Risk Minimization
•Elegant\-FinRL: algorithmic strategies using Reinforcement Learning
•Empyrial: AI and data\-driven quantitative portfolio management for risk and performance analytics
•empyrical: Common financial risk and performance metrics
•EmTract: Extracting Emotions from Social Media Text Tailored for Financial Contexts
•ffn: Financial functions for Python
•FinDataPy: download market data via Bloomberg, Eikon, Quandl, Yahoo etc.
•FinMarketPy: backtesting trading strategies and analyzing financial markets
•finnhub\-python: Finnhub Python API Client to provide financial data(real\-time stock price, global funda\-
mentals, global ETFs holdings and alternative data)
•FinRL: Deep Reinforcement Learning for Quantitative Finance
•FinRL\-Meta: Universe of Near\-Real Market Environments for Data\-Driven Financial Reinforcement Learning
•fredapi is a Python interface to the Federal Reserve Economic Data (FRED) and ALFRED databases
•lifelib: Actuarial models in Python
•lifelines: Survival analysis in Python, including Kaplan Meier, Nelson Aalen and regression
114•lrsm\_portfolio: Portfolio Construction using Stratified Models
•Machine Learning and Data Science Blueprints for Finance (codes for the book)
•Machine Learning fior asset management
•Machine Learning for Algorithmic Trading (codes for the book)
•MLFinLab: Machine Learning Financial Laboratory
•momentum: Running mean, variance, skew, and kurtosis
•Multicriteria Portfolio Construction with Python
•okama: investment portfolio analyzing and optimization tools
•OpenBBTerminal: modern Python\-based integrated environment for investment research
•OptimalPortfolio: portfolio optimization
•QuantAxis: Quantitative Financial FrameWork
•QuantEcon: quantitative economics
•Pandas TA: Technical Analysis Indicators
•portfolio\-backtest: backtest portfolio asset allocation
•precise: online covariance and precision forecasting, portfolios, and model ensembles
•predictionrevisited: implements the core statistical concepts from the book ”Prediction Revisited: The Im\-
portance of Observation”
•pyfinance: general financial and security returns analysis
•pyfolio: Portfolio and risk analytics in Python
•pyhrp: hierarchical risk parity algorithms
•PyPortfolioOpt: Financial portfolio optimisation
•Qlib: Microsoft AI\-oriented quantitative investment platform
•QuantEcon.py: quantitative economics
•QuantLib: Python bindings for the QuantLib library
•QuantResearch: Quantitative analysis, strategies and backtests
•Quantropy: Financial pipeline for the data\-driven investor to research, develop and deploy robust strategie
•QuantStats: Portfolio analytics for quants
•Riskfolio\-Lib: Portfolio Optimization and Quantitative Strategic Asset Allocation
•Robust Risk\-aware reinforcement learning
•stocksight: Stock market analyzer and predictor using Elasticsearch, Twitter, News headlines, NLP and
sentiment analysis
•ta: Technical Analysis Library using Pandas and Numpy
•TA\-lib: Python wrapper for TA\-Lib Technical Analysis Library
•Tax\-Calculator: USA Federal Individual Income and Payroll Tax Microsimulation Model
•tf\-quant\-finance: High\-performance TensorFlow library by Google for quantitative finance.
•vectorbt: Supercharged backtesting and technical analysis for quants
•zipline: Algorithmic Trading Library
1158\.4 R software implementations
List of packages and/or codes and/or frameworks and/or links:
•ASSA: Applied Singular Spectrum Analysis
•AssetAllocation: Backtesting Simple Asset Allocation Strategies
•BEKKs: Multivariate Conditional Volatility Modelling and Forecasting
•crseEventStudy: A Robust and Powerful Test of Abnormal Stock Returns in Long\-Horizon Event Studies
•DOSPortfolio: Dynamic Optimal Shrinkage Portfolio
•ExtremeRisks: Extreme Risk Measures
•FFdownload: Download Data from Kenneth French’s Website
•FinnTS: Microsoft Finance Time Series Forecasting Framework
•finreportr: Financial Data from U.S. Securities and Exchange Commission
•fHMM: Fitting Hidden Markov Models to Financial Data
•FinnTS: Microsoft Finance Time Series Forecasting Framework
•fitHeavyTail: Mean and Covariance Matrix Estimation under Heavy Tails
•fixedincome: Fixed Income Models, Calculations, Data Structures and Instruments
•generalCorr: Generalized Correlations, Causal Paths and Portfolio Selection
•greeks: Sensitivities of Prices of Financial Options
•HDShOP: High\-Dimensional Shrinkage Optimal Portfolios
•HierPortfolios: Hierarchical Clustering\-Based Portfolio Allocation Strategies
•highOrderPortfolios: Design of High\-Order Portfolios via Mean, Variance, Skewness, and Kurtosis
•imputeFin: Imputation of Financial Time Series with Missing Values and/or Outliers
•MarkowitzR: Statistical Significance of the Markowitz Portfolio
•MortCast: Estimation and Projection of Age\-Specific Mortality Rates
•parma: Portfolio Allocation and Risk Management Applications
•pbo: Probability of Backtest Overfitting
•pec: Prediction Error Curves for Risk Prediction Models in Survival Analysis
•pedquant: Public Economic Data and Quantitative Analysis
•PerformanceAnalytics: Econometric Tools for Performance and Risk Analysis
•PortfolioAnalytics: Portfolio Analysis, Including Numerical Methods for Optimization of Portfolios
•portfolioBacktest: Automated Backtesting of Portfolios over Multiple Datasets
•portvine: portfolio level risk estimates using ARMA\-GARCH and vine copulas
•priceR: Economics and Pricing Tools
•qlcal: R Bindings to the Calendaring Functionality of ’QuantLib’
116•qrmtools: Tools for Quantitative Risk Management
•quantmod: Quantitative Financial Modelling Framework
•RcppQuantuccia: R Bindings to the Calendaring Functionality of ’QuantLib’
•riskParityPortfolio: Design of Risk Parity Portfolios
•RiskPortfolios: Computation of Risk\-Based Portfolios
•riskRegression: Risk Regression Models and Prediction Scores for Survival Analysis with Competing Risks
•RPESE: Estimates of Standard Errors for Risk and Performance Measures
•RQuantLib: R Interface to the ’QuantLib’ Library
•SharpeR: Statistical Significance of the Sharpe Ratio
•sharpeRratio: Moment\-Free Estimation of Sharpe Ratios
•sparseIndexTracking: Design of Portfolio of Stocks to Track an Index
•SWIM: Scenario Weights for Importance Measurement
•TextForecast: Regression Analysis and Forecasting Using Textual Data from a Time\-Varying Dictionary
•tidyquant: Tidy Quantitative Financial Analysis
•Trading: CCR, Advanced Correlation \& Beta Estimates, Betting Strategies
•tseries: Time Series Analysis and Computational Finance
•ufRisk: Risk Measure Calculation in Financial TS
•usincometaxes: wrapper to the NBER’s TAXSIM 35 tax simulator for federal and state income taxes
•ycevo: Nonparametric Estimation of the Yield Curve Evolution
•yfR: Downloads and Organizes Financial Data from Yahoo Finance
117References
Adcock, C., Areal, N., Armada, M. R., Cortez, M. C., Oliveira, B., and Silva, F. (2017\). “Portfolio Performance
Measurement: Monotonicity with Respect to the Sharpe Ratio and Multivariate Tests of Correlation .” In:SSRN
e\-Print .
Akgun, O. T., Mudge, T. J., and Townsend, B. (2021\). “How Company Size Bias in ESG Scores Impacts the Small
Cap Investor .” In:The Journal of Impact and ESG Investing 1(4\), pp. 31–44\.
Alessandrini, F., Balula, D. B., and Jondeau, E. (2021\). “ESG Screening in the Fixed\-Income Universe .” In:SSRN
e\-Print .
Alessandrini, F. and Jondeau, E. (2020\). “ESG investing: from sin stocks to smart beta .” In:The Journal of Portfolio
Management 46(3\), pp. 75–94\.
Alessandrini, F. and Jondeau, E. (2021\). “Optimal Strategies for ESG Portfolios .” In:The Journal of Portfolio
Management 47(6\), pp. 114–138\.
Alford, A. W. (2019\). “Some considerations for investors exploring ESG strategies .” In:The Journal of Investing
28(2\), pp. 21–31\.
Amel\-Zadeh, A. (2021\). “The Materiality of Climate Risk .” In:SSRN e\-Print .
Amon, J., Rammerstorfer, M., and Weinmayer, K. (2021\). “Passive ESG Portfolio Management – The Benchmark
Strategy for Socially Responsible Investors .” In:Sustainability 13(16\), p. 9388\.
Andersson, C., Broberg, C., Kaskal, K., and Sonesson, M. (2021\). “Portfolio Construction and New Energy Infras\-
tructure Investing .” In:The Journal of Impact and ESG Investing 2(2\), pp. 57–76\.
Angelova, D., Bosello, F., Bigano, A., and Giove, S. (2021\). “Sovereign rating methodologies, ESG and climate
change risk: an overview .” In:SSRN e\-Print .
Antoncic, M., Bekaert, G., Rothenberg, R. V., and Noguer, M. (2020\). “Sustainable Investment \- Exploring the
Linkage between Alpha, ESG, and SDG’s .” In:SSRN e\-Print .
Apostolou, A. and Papaioannou, M. G. (2021\). “Integration of Environmental Factors into Portfolio Risk Assess\-
ment.” In:The Journal of Impact and ESG Investing 2(1\), pp. 74–91\.
Ardia, D., Boudt, K., and Gagnon\-Fleury, J.\-P. (2017\). “RiskPortfolios: Computation of Risk\-Based Portfolios in
R.” In:The Journal of Open Source Software 2(10\), pp. 171\+.
Areal, N., Cortez, M. C., and Silva, F. (2013\). “The conditional performance of US mutual funds over different
market regimes: do different types of ethical screens matter? ” In:Financial Markets and Portfolio Management
volume 27 (397\-429\).
Arnott, R. D., Harvey, C. R., and Markowitz, H. (2019\). “A backtesting protocol in the era of machine learning .”
In:The Journal of Financial Data Science 1(1\), pp. 64–74\.
Ascioglu, A., Gonzalez, J., and Zbib, L. (2022\). “Analysis of Sustainability Reports for Top 20 Companies in the
S\&P 500 Index .” In:The Journal of Impact and ESG Investing 2(2\).
Ascioglu, A., Saatcioglu, K., and Smith, A. (2017\). “Integration of ESG Metrics into a Student\-Managed Fund:Cre\-
ating Sustainable Student\-Managed Funds .” In:The Journal of Trading 13(1\), pp. 59–71\.
Austmo, J. H. and Eikeland, H. M. (2021\). “Exploiting ESG Information by Extending Conventional Smart Beta
Strategies: An Empirical Analysis of Portfolio Performances through the Booms and Busts in the European
Equity Market .” MA thesis. Copenhagen Business School.
Avramov, D., Cheng, S., Lioui, A., and Tarelli, A. (2021a). “Investment and Asset Pricing with ESG Disagreement .”
In:SSRN e\-Print .
Avramov, D., Cheng, S., Lioui, A., and Tarelli, A. (2022\). “Sustainable investing with ESG rating uncertainty .” In:
Journal of Financial Economics .
Avramov, D., Lioui, A., Liu, Y., and Tarelli, A. (2021b). “Dynamic ESG Equilibrium .” In:SSRN e\-Print .
Aw, E. N. W., LaPerla, S. J., and Sivin, G. Y. (2017\). “A Morality Tale of ESG: Assessing Socially Responsible
Investing .” In:The Journal of Wealth Management 19(4\), pp. 14–23\.
Azevedo, V., Kaserer, C., and Campos, L. M. S. (2021\). “Investor sentiment and the time\-varying sustainability
premium .” In:Journal of Asset Management 22, pp. 600–621\.
Bacon, C. R. (2019\). “Performance Attribution: History and Progress .” In:CFA Institute Research Foundation
Publications .
Baeza\-Sampere, I., Coll\-Serrano, V., M, B., and Mendez\-Rodriguez, P. (2016\). “A fuzzy data envelopment analysis
model for evaluating the efficiency of socially responsible and conventional mutual funds .” In:Journal of Risk
19(1\), pp. 77–90\.
118Bag, D. and Mohanty, S. (2021\). “Impact of ESG Factors on Emerging Market Stock Returns .” In:The Journal of
Impact and ESG Investing 2(2\), pp. 138–147\.
Bahra, B. and Thukral, L. (2020\). “ESG in Global Corporate Bonds: The Analysis Behind the Hype .” In:The
Journal of Portfolio Management 46(8\), pp. 133–147\.
Bailey, D. H., Borwein, J. M., and Lopez de Prado, M. (2017\). “Stock Portfolio Design and Backtest Overfitting .”
In:Journal of Investment Management 15(1\), pp. 75–87\.
Bajic, A., Kiesel, R., and Hellmich, M. (2021\). “Handle with Care: Challenges and Opportunities of using Company\-
Level Emissions Data for Assessing Financial Risks from Climate Change .” In:SSRN e\-Print .
Balcilar, M., Demirer, R., and Gupta, R. (2017\). “Do Sustainable Stocks Offer Diversification Benefits for Conven\-
tional Portfolios? An Empirical Analysis of Risk Spillovers and Dynamic Correlations .” In:Sustainability 9(10\),
p. 1799\.
Ballinari, D. and Mahmoud, O. (2021\). “From Chatter to Action: An Index of Sustainability Sentiment .” In:SSRN
e\-Print .
Barber, B. M., Morse, A., and Yasuda, A. (2021\). “Impact investing .” In:Journal of Financial Economics 139(1\),
pp. 162–185\.
Barnett, M., Brock, W., and Hansen, L. P. (2020\). “Pricing uncertainty induced by climate change .” In:The Review
of Financial Studies 33(3\), pp. 1024–1066\.
Bauer, R., Ruof, T., and Smeets, P. (2021\). “Get Real! Individuals Prefer More Sustainable Investments .” In:The
Review of Financial Studies 34(8\). Ed. by S. V. Nieuwerburgh, pp. 3976–4043\.
Bax, K., Sahin, O., Czado, C., and Paterlini, S. (2021\). “ESG, Risk, and (tail) dependence .” In:arXiv e\-Print .
Baz, S., Cathcart, L., Michaelides, A., and Zhang, Y. (2021\). “Climate Regulatory Exposure: Evidence from Stock
Returns .” In:SSRN e\-Print .
Becker, M. G., Martin, F., and Walter, A. (2021\). “Fostering the Power of ESG Transparency: The Effect of
Sustainability Labels on Mutual Funds and Individual Investors .” In:SSRN e\-Print .
Ben Dor, A., Guan, J., Kelleher, A., Lauretig, A., Preclaw, R., and Zeng, X. (2021\). “ESG and Alternative Data:
Capturing Corporates’ Sustainability\-Related Activities with Job Postings .” In:The Journal of Impact and ESG
Investing 1(2\), pp. 16–25\.
Ben Slimane, M., Brard, E., Le Guenedal, T., Roncalli, T., and Sekine, T. (2020\). “ESG Investing in Fixed Income:
It’s Time to Cross the Rubicon .” In:SSRN e\-Print .
Bender, J., He, C., Ooi, C., and Sun, X. (2020\). “Reducing the carbon intensity of low volatility portfolios .” In:The
Journal of Portfolio Management 46(3\), pp. 108–122\.
Bender, J., Sun, X., and Wang, T. (2017\). “Thematic Indexing, Meet Smart Beta! Merging ESG into Factor
Portfolios .” In:The Journal of Index Investing 8(3\), pp. 89–101\.
Benedetti, D., Biffis, E., Chatzimichalakis, F., Fedele, L. L., and Simm, I. (2021\). “Climate change investment risk:
optimal portfolio construction ahead of the transition to a lower\-carbon economy .” In:Annals of Operations
Research 299(1\-2\), pp. 847–871\.
Bengo, I., Borrello, A., and Chiodo, V. (2021\). “Preserving the Integrity of Social Impact Investing: Towards a
Distinctive Implementation Strategy .” In:Sustainability 13(5\), p. 2852\.
Bennani, L., Le Guenedal, T., Lepetit, F., Ly, L., Mortier, V., Roncalli, T., and Sekine, T. (2019\). “How ESG
investing has impacted the asset pricing in the equity market .” In:SSRN e\-Print .
Berg, F., Fabisik, K., and Sautner, Z. (2021a). “Rewriting History II: The (Un)Predictable Past of ESG Ratings .”
In:SSRN e\-Print .
Berg, F., Kolbel, J., Pavlova, A., and Rigobon, R. (2021b). “ESG Confusion and Stock Returns: Tackling the
Problem of Noise .” In:SSRN e\-Print .
Berg, F., Kolbel, J., Pavlova, A., and Rigobon, R. (2022a). “ESG Confusion and Stock Returns: Tackling the
Problem of Noise .” In:American Finance Association Annual Meeting .
Berg, F., Kolbel, J. F., and Rigobon, R. (2022b). “Aggregate Confusion: The Divergence of ESG Ratings .” In:
Review of Finance .
Berk, J. B. and van Binsbergen, J. H. (2021\). “The Impact of Impact Investing .” In:SSRN e\-Print .
Bessler, W., Opfer, H., and Wolff, D. (2017\). “Multi\-asset portfolio optimization and out\-of\-sample performance: an
evaluation of Black Litterman, mean\-variance, and naive diversification approaches .” In:The European Journal
of Finance 23(1\), pp. 1–30\.
Bessler, W. and Wolff, D. (2017\). “Portfolio Optimization with Industry Return Prediction Models .” In:SSRN
e\-Print .
119Bettin, G. (2021\). “Sustainable finance and ESG scores: A portfolio analysis a la Fama and French .” MA thesis.
Universita Ca Foscari Venezia.
Billio, M., Costola, M., Hristova, I., Latino, C., and Pelizzon, L. (2021\). “Inside the ESG Ratings: (Dis)agreement
and Performance .” In:SSRN e\-Print .
Bingler, J. A., Kraus, M., and Leippold, M. (2021\). “Cheap Talk and Cherry\-Picking: What ClimateBert has to
say on Corporate Climate Risk Disclosures .” In:SSRN e\-Print .
Bingler, J. A., Kraus, M., Leippold, M., and Webersinke, N. (2022\). “Cheap Talk in Corporate Climate Commit\-
ments: The Role of Active Institutional Ownership, Signaling, Materiality, and Sentiment .” In:SSRN e\-Print .
Bjerring, T., Ross, O., and Weissensteiner, A. (2017\). “Feature selection for portfolio optimization .” In:Annals of
Operations Research 256, pp. 21–40\.
Blank, H., Sgambati, G., and Truelson, Z. (2016\). “Best Practices in ESG Investing .” In:The Journal of Investing
25(2\), pp. 103–112\.
Blitz, D. and Hoogteijling, T. (2021\). “Carbon\-Tax\-Adjusted Value .” In:SSRN e\-Print .
Bohn, J., Goldberg, L. R., and Ulucam, S. (2022\). “Sustainable Investing From a Practitioner’s Viewpoint: What’s
in Your ESG Portfolio? ” In:Journal of Investment Management 20(2\).
Boileau, P., Hejazi, N., Collica, B., Laan, M. van der, and Dudoit, S. (2021\). “cvCovEst: Cross\-validated covariance
matrix estimator selection and evaluation in R .” In:Journal of Open Source Software 6(63\), p. 3273\.
Bolliger, G. and Cornilly, D. (2021\). “Sustainability Attribution: The Case of Carbon Intensity .” In:The Journal
of Impact and ESG Investing 2(1\), pp. 93–99\.
Bolton, P. and Kacperczyk, M. (2021\). “Do investors care about carbon risk? ” In:Journal of Financial Economics
142(2\), pp. 517–549\.
Bonaparte, Y. (2021\). “The ESG Investor Sentiment Index: A Cross Sectional and Time Series Analyses .” In:SSRN
e\-Print .
Borms, S., Boudt, K., Holle, F. V., and Willems, J. (2021\). “Semi\-supervised Text Mining for Monitoring the News
About the ESG Performance of Companies .” In:Data Science for Economics and Finance . Springer International
Publishing, pp. 217–239\.
Boucher, C., Le Lann, W., Matton, S., and Tokpavis, S. (2021\). Backtesting ESG Ratings . Tech. rep. University of
Orleans.
Branch, M., Goldberg, L. R., and Hand, P. (2019\). “A guide to ESG portfolio construction .” In:The Journal of
Portfolio Management 45(4\), pp. 61–66\.
Breedt, A., Ciliberti, S., Gualdi, S., and Seager, P. (2019\). “Is ESG an Equity Factor or Just an Investment Guide? ”
In:The Journal of Investing 28(2\), pp. 32–42\.
Briere, M., Peillex, J., and Ureche, L. (2017\). “Do Social Responsibility Screens Really Matter When Assessing
Mutual Fund Performance? ” In:SSRN e\-Print .
Broadstock, D., Chan, K., Cheng, L. T. W., and Wang, X. W. (2020\). “The Role of ESG Performance During Times
of Financial Crisis: Evidence from COVID\-19 in China .” In:SSRN e\-Print .
Bruder, B., Cheikh, Y., Deixonne, F., and Zheng, B. (2019\). “Integration of ESG in asset allocation .” In:SSRN
e\-Print .
Brugiere, P. (2020\). Quantitative Portfolio Management with Applications in Python . Springer International Pub\-
lishing. 189 pp.
Bruni, R., Cesarone, F., Scozzari, A., and Tardella, F. (2016\). “Real\-world datasets for portfolio selection and
solutions of some stochastic dominance portfolio models .” In:Data in Brief 8, pp. 858–862\.
Bruni, R., Cesarone, F., Scozzari, A., and Tardella, F. (2017\). “On exact and approximate stochastic dominance
strategies for portfolio selection .” In:European Journal of Operational Research 259(1\), pp. 322–329\.
Bruno, G., Esakia, M., and Goltz, F. (2022\). “”Honey, I Shrunk the ESG Alpha”: Risk\-Adjusting ESG Portfolio
Returns .” In:The Journal of Investing 31(3\), pp. 45–61\.
Bryzgalova, S., Huang, J., and Julliard, C. (2021a). “Bayesian solutions for the factor zoo: we just ran two quadrillion
models .” In:SSRN e\-Print .
Bryzgalova, S., Pelger, M., and Zhu, J. (2021b). “Forest Through the Trees: Building Cross\-Sections of Stock
Returns .” In:SSRN e\-Print .
Bush, R., Chen, J., and Legunn, E. (2020\). “E, S, or G \- Analyzing Global ESG Performance .” In:The Journal of
Impact and ESG Investing 1(2\), pp. 16–25\.
Cai, L., Cooper, R., and He, D. (2022\). “Socially Responsible Investing and Factor Investing, Is There an Oppor\-
tunity Cost? ” In:The Journal of Portfolio Management 48(2\), pp. 181–197\.
120Cajas, D. (2021a). “Entropic Portfolio Optimization: a Disciplined Convex Programming Framework .” In:SSRN
e\-Print .
Cajas, D. (2021b). “OWA Portfolio Optimization: a Disciplined Convex Programming Framework .” In:SSRN e\-
Print.
Cakici, N. and Zaremba, A. (2021\). “Responsible Investing: ESG Ratings and the Cross\-Section of International
Stock Returns .” In:SSRN e\-Print .
Caldeira, J. N. M. d. J. M. (2021\). “Impact of ESG on financial performance on the most capitalized stock markets
: evidence from the USA Europe and Asia .” MA thesis. Universidade Catolica Portuguesa.
Calvo, C., Ivorra, C., and Liern, V. (2015\). “Finding socially responsible portfolios close to conventional ones .” In:
International Review of Financial Analysis 40, pp. 52–63\.
Cao, J., Goyal, A., Zhan, X., and Zhang, W. E. (2021\). “Unlocking ESG Premium from Options .” In:SSRN e\-Print .
Cesarone, F., Martino, M. L., and Carleo, A. (2022\). “Does ESG impact really enhances portfolio profitability? ”
In:SSRN e\-Print .
Cesarone, F., Moretti, J., and Tardella, F. (2018\). “Why Small Portfolios Are Preferable and How to Choose Them .”
In:SSRN e\-Print .
Cesarone, F., Mottura, C., Ricci, J. M., and Tardella, F. (2019\). “On the stability of portfolio selection models .” In:
SSRN e\-Print .
Chan, Y., Hogan, K., Schwaiger, K., and Ang, A. (2020\). “ESG in Factors .” In:The Journal of Impact and ESG
Investing 1(1\), pp. 26–45\.
Chang, C.\-H., Tan, S., Lengerich, B., Goldenberg, A., and Caruana, R. (2021\). “How Interpretable and Trustworthy
are GAMs? ” In:Proceedings of the 27th ACM SIGKDD Conference on Knowledge Discovery \& Data Mining .
ACM.
Chaudhuri, S. E. and Lo, A. W. (2019\). “Dynamic Alpha: A Spectral Decomposition of Investment Performance
Across Time Horizons .” In:Management Science 65(9\), pp. 4440–4450\.
Chava, S., Kim, J. H. (, and Lee, J. (2021\). “Doing Well by Doing Good? Risk, Return, and Environmental and
Social Ratings .” In:SSRN e\-Print .
Cheema\-Fox, A., LaPerla, B. R., Serafeim, G., Turkington, D., and Wang, H. ( (2021\). “Decarbonization Factors .”
In:The Journal of Impact and ESG Investing 2(1\), pp. 47–73\.
Chen, A. Y. and Zimmermann, T. (2022\). “Open Source Cross\-Sectional Asset Pricing .” In:American Finance
Association Annual Meeting .
Chen, M. and Mussalli, G. (2020\). “An integrated approach to quantitative ESG investing .” In:The Journal of
Portfolio Management 46(3\), pp. 65–74\.
Chen, M., Mussalli, G., Amel\-Zadeh, A., and Weinberg, M. O. (2022\). “NLP for SDGs: Measuring Corporate
Alignment with the Sustainable Development Goals .” In:The Journal of Impact and ESG Investing 2(2\).
Chen, M., von Behren, R., and Mussalli, G. (2021\). “The Unreasonable Attractiveness of More ESG Data .” In:The
Journal of Portfolio Management 48(1\), pp. 147–162\.
Chen, S. and Bowler, M. (2021\). “Constructing and Validating Climate Risk Factors from ESG Data: an Empirical
Comparison .” In:SSRN e\-Print .
Chen, Y. and Deleon, A. (2020\). “Financial Quality Metrics and ESG Factor Interactions in Equity Markets .” In:
The Journal of Impact and ESG Investing 1(2\), pp. 7–15\.
Chib, S. (2020\). R package czfactor . Tech. rep. Washington University.
Chib, S. and Zhao, L. (2020\). R package czzg . Tech. rep. Washington University.
Choi, D., Gao, Z., and Jiang, W. (2020\). “Measuring the carbon exposure of institutional investors .” In:The Journal
of Alternative Investments 23(1\), pp. 12–23\.
Chong, J. and Phillips, G. M. (2016\). “ESG Investing: A Simple Approach .” In:The Journal of Wealth Management
19(2\), pp. 73–88\.
Climent, R. B., Garrigues, I. F.\-F., Paraskevopoulos, I., and Santos, A. (2021\). “ESG Disclosure and Portfolio
Performance .” In:Risks 9(10\), p. 172\.
Coqueret, G. (2021\). “Perspectives in ESG equity investing .” In:SSRN e\-Print .
Coqueret, G. (2022a). Perspectives in sustainable equity investing . Boca Raton: CRC Press. 140 pp.
Coqueret, G. (2022b). Perspectives in sustainable equity investing (website version) .
Coqueret, G. and Guida, T. (2020\). Machine Learning for Factor Investing: R Version . Chapman and Hall/CRC.
341 pp.
121Coqueret, G., Stiernegrip, S., Morgenstern, C., Kelly, J., Frey\-Skott, J., and Osterberg, B. (2021a). “Boosting
ESG\-Based Optimization With Asset Pricing Characteristics .” In:SSRN e\-Print .
Coqueret, G., Stiernegrip, S., Morgenstern, C., Kelly, J., Frey\-Skott, J., and Osterberg, B. (2021b). “ESG Equity
Investing: A Short Survey .” In:SSRN e\-Print .
Coqueret, G. and Tran, V. L. (2022\). “ESG news spillovers to (and from) the supply chain .” In:SSRN e\-Print .
Cornell, B. (2020\). “ESG Investing: Conceptual Issues .” In:The Journal of Wealth Management 23(3\), pp. 61–69\.
Cornell, B. (2021a). “ESG preferences, risk and return .” In:European Financial Management 27(1\), pp. 12–19\.
Cornell, B. (2021b). “Is the Stock Market Worried About Climate Change? Lessons from the 2010s .” In:The Journal
of Impact and ESG Investing 1(3\), pp. 51–58\.
Cornell, B. and Damodaran, A. (2020\). “Valuing ESG: Doing Good or Sounding Good? ” In:SSRN e\-Print .
Cosemans, M., Hut, X., and Dijk, M. A. V. (2021\). “Climate Change and Long\-Horizon Portfolio Choice: Combining
Theory and Empirics .” In:SSRN e\-Print .
D’Amato, V., D’Ecclesia, R., and Levantesi, S. (2021\). “Fundamental ratios as predictors of ESG scores: a machine
learning approach .” In:Decisions in Economics and Finance 44(2\), pp. 1087–1110\.
Dash, G. H. and Kajiji, N. (2021\). “Behavioral Portfolio Management with Layered ESG Goals and AI Estimation
of Asset Returns .” In:SSRN e\-Print .
De, I. and Clayman, M. R. (2015\). “The Benefits of Socially Responsible Investing: An Active Manager’s Perspec\-
tive.” In:The Journal of Investing 24(4\), pp. 49–72\.
de Carvalho, M. and Rua, A. (2017\). “Real\-time nowcasting the US output gap: Singular spectrum analysis at
work.” In:International Journal of Forecasting 33(1\), pp. 185–198\.
De Franco, C. (2019\). “ESG Controversies and Their Impact on Performance .” In:The Journal of Investing 29(2\),
pp. 33–45\.
De Franco, C., Geissler, C., Margot, V., and Monnier, B. (2020\). “ESG investments: Filtering versus machine
learning approaches .” In:arXiv e\-Print .
De Franco, C., Nicolle, J., and Tran, L.\-A. (2021\). “Sustainable Investing: ESG versus SDG .” In:The Journal of
Impact and ESG Investing 1(4\), pp. 45–62\.
De Spiegeleer, J., Hocht, S., Jakubowski, D., Reyners, S., and Schoutens, W. (2020\). “ESG: A New Dimension in
Portfolio Allocation .” In:SSRN e\-Print .
Dimson, E., Marsh, P., and Staunton, M. (2020\). “Divergent ESG Ratings .” In:TheJournalofPortfolioManagement
47(1\), pp. 75–87\.
Ding, L., Ahmed, S., and Shapiro, A. (2020\). “A Python package for multi\-stage stochastic programming .” In:
Optimization Online e\-Print .
Diris, B., Palm, F., and Schotman, P. (2015\). “Long\-Term Strategic Asset Allocation: An Out\-of\-Sample Evaluation .”
In:Management Science 61(9\), pp. 2185–2202\.
Dixon, M. and Polson, N. (2020\). “Deep Fundamental Factor Models .” In:SIAM Journal on Financial Mathematics
11(3\), SC–26–SC–37\.
Dixon, M. F., Halperin, I., and Bilokon, P. (2020\). Machine Learning in Finance: from theory to practice . Springer
International Publishing. 548 pp.
Dı́az, V., Ibrushi, D., and Zhao, J. (2021\). “Reconsidering systematic factors during the Covid\-19 pandemic – The
rising importance of ESG .” In:Finance Research Letters 38 (101870\).
Dong, X., Li, Y., Rapach, D., and Zhou, G. (2022\). “Anomalies and the expected market return .” In:Journal of
Finance 27(1\), pp. 639–681\.
Drei, A., Le Guenedal, T., Lepetit, F., Mortier, V., Roncalli, T., and Sekine, T. (2019\). “ESG Investing in Recent
Years: New Insights from Old Challenges .” In:SSRN e\-Print .
Duan, T., Li, F. W., and Wen, Q. (2021\). “Is Carbon Risk Priced in the Cross Section of Corporate Bond Returns? ”
In:SSRN e\-Print .
Dumitrescu, A., Gil\-Bazo, J., and Zhou, F. (2022\). “Defining Greenwashing .” In:SSRN e\-Print .
Engle, R. F., Giglio, S., Kelly, B., Lee, H., and Stroebel, J. (2020\). “Hedging climate change news .” In:The Review
of Financial Studies 33(3\), pp. 1184–1216\.
Fabozzi, F. J., Fabozzi, F. A., Lopez de Prado, M., and Stoyanov, S. (2021\). Asset Management: Tools and Issues .
World Scientific. 516 pp.
Fabozzi, F. J. and Lopez de Prado, M. (2018\). “Being Honest in Backtest Reporting: A Template for Disclosing
Multiple Tests .” In:The Journal of Portfolio Management 45(1\), pp. 141–147\.
122Faccini, R., Matin, R., and Skiadopoulos, G. (2021\). “Dissecting Climate Risks: Are they Reflected in Stock Prices? ”
In:SSRN e\-Print .
Filbeck, A., Filbeck, G., and Zhao, X. (2019\). “Performance assessment of firms following sustainalytics ESG
principles .” In:The Journal of Investing 28(2\), pp. 7–20\.
Fiordelisi, F., Galloppo, G., Lattanzio, G., and Paimanova, V. (2021\). “An ESG Ratings Free Assessment of Socially
Responsible Investment Strategies .” In:SSRN e\-Print .
Fish, A., Kim, D. H., and Venkatraman, S. (2019\). “The ESG Sacrifice .” In:SSRN e\-Print .
Focardi, S. M. and Fabozzi, F. J. (2020\). “Climate change and asset management .” In:The Journal of Portfolio
Management 46(3\), pp. 95–107\.
Fridson, M., Jiang, L., Mei, Z., and Navaei, D. (2021\). “ESG Impact on High\-Yield Returns .” In:The Journal of
Fixed Income 30(4\), pp. 53–63\.
Friederich, D., Kaack, L. H., Luccioni, A., and Steffen, B. (2021\). “Automated Identification of Climate Risk
Disclosures in Annual Corporate Reports.” In: arXiv e\-Print .
Gao, Y., Satchell, S., and Srivastava, N. (2020\). “Styles through a convergent/divergent lens: the curious case of
ESG.” In:Journal of Asset Management 21, pp. 4–12\.
Garefalakis, A. and Dimitras, A. (2020\). “Looking back and forging ahead: the weighting of ESG factors .” In:Annals
of Operations Research 294, pp. 151–189\.
Garnier, J. (2022\). “The Climate Extended Risk Model (CERM).” In: arXiv e\-Print .
Gaussel, N. and Le Saint, L. (2021\). “ESG Risk Rating of Alternative Portfolios .” In:SSRN e\-Print .
Geczy, C., Jeffers, J. S., Musto, D. K., and Tucker, A. M. (2021a). “Contracts with (Social) benefits: The imple\-
mentation of impact investing .” In:Journal of Financial Economics 142(2\), pp. 697–718\.
Geczy, C. C., Stambaugh, R. F., and Levin, D. (2021b). “Investing in Socially Responsible Mutual Funds .” In:The
Review of Asset Pricing Studies 11(2\), pp. 309–351\.
Geczy, C. C. and Guerard, J. (2021\). “ESG and Expected Returns on Equities: The Case of Environmental Ratings .”
In:SSRN e\-Print .
Geczy, C. C., Guerard, J., and Samonov, M. (2019\). “Efficient SRI / ESG portfolios .” In:SSRN e\-Print .
Gerard, B. (2018\). “ESG and socially responsible investment: A critical review .” In:SSRN e\-Print .
Gibson Brandon, R., Krueger, P., and Schmidt, P. S. (2021\). “ESG Rating Disagreement and Stock Returns .” In:
Financial Analysts Journal 77(4\), pp. 104–127\.
Gidwani, B. (2020\). “Some Issues with Using ESG Ratings in an Investment Process .” In:The Journal of Investing
29(6\), pp. 76–84\.
Giese, G., Lee, L.\-E., Melas, D., Nagy, Z., and Nishikawa, L. (2019a). “Consistent ESG through ESG Benchmarks .”
In:The Journal of Index Investing 10(2\), pp. 24–42\.
Giese, G., Lee, L.\-E., Melas, D., Nagy, Z., and Nishikawa, L. (2019b). “Foundations of ESG investing: how ESG
affects equity valuation, risk, and performance .” In:The Journal of Portfolio Management 45(5\), pp. 69–83\.
Giese, G., Lee, L.\-E., Melas, D., Nagy, Z., and Nishikawa, L. (2019c). “Performance and Risk Analysis of Index\-Based
ESG Portfolios .” In:The Journal of Index Investing 9(4\), pp. 46–57\.
Giese, G., Nagy, Z., and Lee, L.\-E. (2021a). “Deconstructing ESG Ratings Performance: Risk and Return for E, S,
and G by Time Horizon, Sector, and Weighting .” In:The Journal of Portfolio Management 47(3\), pp. 94–111\.
Giese, G., Nagy, Z., and Rauis, B. (2021b). “Foundations of Climate Investing: How Equity Markets Have Priced
Climate\-Transition Risks .” In:The Journal of Portfolio Management 47(9\), pp. 35–53\.
Giese, G., Ossen, A., and Bacon, S. (2016\). “ESG as a performance factor for smart beta indexes .” In:The Journal
of Index Investing 7(3\), pp. 7–20\.
Gorgen, M., Jacob, A., and Nerlinger, M. (2021\). “Get Green or Die Trying? Carbon Risk Integration into Portfolio
Management .” In:The Journal of Portfolio Management 47(3\), pp. 77–93\.
Gougler, A. and Utz, S. (2020\). “Factor exposures and diversification: Are sustainably screened portfolios any
different? ” In:Financial Markets and Portfolio Management 34, pp. 221–249\.
Grealish, A. and Kolm, P. N. (2021\). “Robo\-Advisory: From Investing Principles and Algorithms to Future Devel\-
opments .” In:SSRN e\-Print .
Gregory, R. P. (2021a). “Market Efficiency in ESG Indexes: Trading Opportunities .” In:The Journal of Impact and
ESG Investing 1(4\), pp. 72–82\.
Gregory, R. P. (2021b). “The Response of the S\&P 1500 during the COVID\-19 Pandemic and ESG Scores .” In:
SSRN e\-Print .
123Greiner, S. P. and Stoyanov, S. V. (2019\). “Portfolio scoring by expected risk premium .” In:The Journal of Portfolio
Management 45(4\), pp. 83–90\.
Grim, D. M. and Berkowitz, D. B. (2020\). “ESG, SRI, and Impact Investing: A Primer for Decision\-Making .” In:
The Journal of Impact and ESG Investing 1(1\), pp. 47–65\.
Gueant, O., Peladan, J.\-G., Robert\-Dautun, A., and Tankov, P. (2021\). “Environmental transition alignment and
portfolio performance .” In:SSRN e\-Print .
Guidolin, M., Hansen, E., and Lozano\-Banda, M. (2018\). “Portfolio performance of linear SDF models: an out\-of\-
sample assessment .” In:Quantitative Finance 18(8\), pp. 1425–1436\.
Guijarro\-Ordonez, J., Pelger, M., and Zanotti, G. (2021\). “Deep Learning Statistical Arbitrage .” In:SSRN e\-Print .
Guo, D. (2019\). “A Statistical Response to Challenges in Vast Portfolio Selection .” PhD thesis. University of
Waterloo.
Guo, D., Boyle, P. P., Weng, C., and Wirjanto, T. S. (2019\). “When Does The 1/N Rule Work? ” In:SSRN e\-Print .
Guo, T., Jamet, N., Betrix, V., Piquet, L.\-A., and Hauptmann, E. (2020\). “ESG2Risk: A Deep Learning Framework
from ESG News to Stock Volatility Prediction .” In:arXiv e\-Print .
Gurdogan, H. and Kercheval, A. (2021\). “Multi Anchor Point Shrinkage for the Sample Covariance Matrix (Extended
Version).” In: arXiv e\-Print .
Gutterman, A. (2020\). “Impact Investment Tools, Structures and Instruments .” In:SSRN e\-Print .
Gyonyorova, L., Stachoň, M., and Stašek, D. (2022\). “ESG ratings: relevant information or misleading clue? Evidence
from the S\&P Global 1200 .” In:Journal of Sustainable Finance \& Investment , pp. 1–35\.
Hain, L. I., Kolbel, J. F., and Leippold, M. (2021\). “Let’s get physical: Comparing metrics of physical climate risk .”
In:Finance Research Letters , p. 102406\.
Hakala, E.\-E. (2021\). “Can ESG controversies predict medium\- to long\-term stock performance? Evidence from
global markets .” MA thesis. Aalto University.
Haley, M. R. (2017\). “K\-fold cross validation performance comparisons of six naive portfolio selection rules: how
naive can you be and still have successful out\-of\-sample portfolio performance? ” In:Annals of Finance 13,
pp. 341–353\.
Hambel, C., Kraft, H., and Ploeg, R. van der (2021\). “Asset Pricing and Decarbonization: Diversification versus
Climate Action .” In:SSRN e\-Print .
Hanicova, D. and Vojtko, R. (2020\). “Backtesting ESG Factor Investing Strategies .” In:SSRN e\-Print .
Hanna, M. (2020\). “The Impact of ESG\-Related Industry Exclusions in Minimum\-Volatility Portfolios .” In:The
Journal of Impact and ESG Investing 1(2\), pp. 87–103\.
Harper, H. (2020\). “One Institutional Investor Approach to Integrating ESG in the Investment Process .” In:The
Journal of Portfolio Management 46(4\), pp. 110–123\.
Harvey, C. R., Liu, Y., and Saretto, A. (2020\). “An Evaluation of Alternative Multiple Testing Methods for Finance
Applications .” In:The Review of Asset Pricing Studies 10(2\), pp. 199–248\.
Hays, M. and McCabe, J. (2021\). “Sustainable and Impact Investing: A Taxonomy of Approaches and Considerations
for Fiduciaries .” In:The Journal of Wealth Management 24(2\), pp. 10–24\.
Heeb, F., Kolbel, J., Paetzold, F., and Zeisberger, S. (2022\). “Do Investors Care About Impact? ” In:SSRN e\-Print .
Henriksson, R., Livnat, J., Pfeifer, P., and Stumpp, M. (2019\). “Integrating ESG in portfolio construction .” In:The
Journal of Portfolio Management 45(4\), pp. 67–81\.
Hens, T., Schenk\-Hoppe, K. R., and Woesthoff, M.\-H. (2020\). “Escaping the backtesting illusion .” In:The Journal
of Portfolio Management 46(4\), pp. 81–93\.
Ho, J., Tumkaya, T., Aryal, S., Choi, H., and Claridge\-Chang, A. (2019\). “Moving beyond P values: data analysis
with estimation graphics .” In:Nature Methods 16(7\), pp. 565–566\.
Hodges, P., Ren, H., Schwaiger, K., and Ang, A. (2022\). “Net Zero Investing for Multi\-Asset Portfolios seeking to
satisfy Paris Aligned Benchmark Requirements with Climate Alpha Signals .” In:SSRN e\-Print .
Homescu, C. (2014\). “Many risks, one (optimal) portfolio .” In:SSRN e\-Print .
Homescu, C. (2015\). “Better Investing Through Factors, Regimes and Sensitivity Analysis .” In:SSRN e\-Print .
Hsu, Y.\-C., Lin, H.\-W., and Vincent, K. (2017\). Do Cross\-Sectional Stock Return Predictors Pass the Test without
Data\-Snooping Bias? Tech. rep. Institute of Economics Academia Sinica.
Hsu, P.\-H., Han, Q., Wu, W., and Cao, Z. (2018a). “Asset allocation strategies, data snooping, and the 1 / N rule .”
In:Journal of Banking \& Finance 97, pp. 257–269\.
Hsu, J., Liu, X., Shen, K., Viswanathan, V., and Zhao, Y. (2018b). “Outperformance through Investing in ESG in
Need.” In:The Journal of Index Investing 9(2\), pp. 18–26\.
124Huang, M. and Yu, S. (2020\). “A new procedure for resampled portfolio with shrinkaged covariance matrix .” In:
Journal of Applied Statistics 47(44\), pp. 642–652\.
Hubel, B. and Scholz, H. (2020\). “Integrating sustainability risks in asset management: the role of ESG exposures
and ESG ratings .” In:Journal of Asset Management 21, pp. 52–69\.
Husse, T. and Pippo, F. (2022\). “Responsible Minus Irresponsible \- a determinant of equity risk premia? ” In:Journal
of Sustainable Finance \& Investment , pp. 1–23\.
Hwang, I., Xu, S., and In, F. (2018\). “Naive versus optimal diversification: Tail risk and performance .” In:European
Journal of Operational Research 265(1\), pp. 372–388\.
Ielasi, F., Ceccherini, P., and Zito, P. (2020\). “Integrating ESG Analysis into Smart Beta Strategies .” In:Sustain\-
ability 12(22\), p. 9351\.
Ielpo, F., Merhy, C., and Simon, G. (2017\). Engineering Investment Process: Making Value Creation Repeatable .
Elsevier. 430 pp.
Immel, M., Hachenberg, B., Kiesel, F., and Schiereck, D. (2021\). “Green bonds: shades of green and brown .” In:
Journal of Asset Management 22, pp. 96–109\.
Irlam, G. (2020a). AI Planner .url:https://www.aiplanner.com/ .
Irlam, G. (2020b). “Machine learning for retirement planning .” In:The Journal of Retirement 8(1\), pp. 32–29\.
Irlam, G. (2020c). “Multi Scenario Financial Planning via Deep Reinforcement Learning AI .” In:SSRN e\-Print .
Jacob, A. and Wilkens, M. (2021\). “What drives sustainable indices? A framework for analyzing the sustainable
index landscape .” In:SSRN e\-Print .
Jacobsen, B., Cheng, E., and Lee, W. (2021\). “Climate Change and Asset Allocation: A Distinction That Makes a
Difference .” In:The Journal of Portfolio Management 47(4\), pp. 123–134\.
Jacobsen, B., Lee, W., and Ma, C. (2019\). “The alpha, beta, and sigma of ESG: better beta, additional alpha? ” In:
The Journal of Portfolio Management 45(6\), pp. 6–15\.
Jaeger, M., Krugel, S., Marinelli, D., Papenbrock, J., and Schwendner, P. (2020\). “Understanding machine learning
for diversified portfolio construction by explainable AI .” In:SSRN e\-Print .
Jansen, S. (2020\). Machine Learning for Algorithmic Trading (Second Edition) . Packt Publishing. 820 pp.
Jeffers, J., Lyu, T., and Posenau, K. (2021\). “The Risk and Return of Impact Investing Funds .” In:SSRN e\-Print .
Jin, I. (2018\). “Is ESG a systematic risk factor for US equity mutual funds? ” In:Journal of Sustainable Finance \&
Investment 8(1\), pp. 72–93\.
Jin, I. (2021\). “Systematic ESG Risk and Decision Criteria for Optimal Portfolio Selection .” In:SSRN e\-Print .
Jondeau, E., Mojon, B., and da Silva, L. A. P. (2021\). “Building Benchmarks Portfolios with Decreasing Carbon
Footprints .” In:SSRN e\-Print .
Juddoo, K., Malki, I., Mathew, S., and Sivaprasad, S. (2021\). “An Investment Strategy Based on Impact .” In:SSRN
e\-Print .
Jurczenko et al. (2020\). Machine Learning for Asset Management . Ed. by E. Jurczenko. Wiley. 445 pp.
Kaiser, L. (2020\). “ESG integration: value, growth and momentum .” In:Journal of Asset Management 21(1\), pp. 32–
51\.
Kaiser, L. and Schaller, F. (2019\). “Environmentally (Un\-)Friendly Portfolio Construction .” In:Journal of Invest\-
ment Consulting 19(1\), pp. 43–52\.
Kakushadze, Z. and Yu, W. (2016\). “Statistical Risk Models .” In:SSRN e\-Print .
Kakushadze, Z. and Yu, W. (2017\). “Open Source Fundamental Industry Classification .” In:MDPI Data 22 (2\).
Kakushadze, Z. and Yu, W. (2018a). “Betas, Benchmarks, and Beating the Market .” In:The Journal of Trading .
Kakushadze, Z. and Yu, W. (2018b). “Decoding stock market with quant alphas .” In:Journal of Asset Management ,
pp. 1–11\.
Kakushadze, Z. and Yu, W. (2019\). “Machine learning risk models .” In:SSRN e\-Print .
Kakushadze, Z. and Yu, W. (2020\). “Machine learning treasury yields .” In:SSRN e\-Print .
Kanuri, S. (2020\). “Risk and Return Characteristics of Environmental, Social, and Governance (ESG) Equity ETFs .”
In:The Journal of Index Investing 11(2\), pp. 66–75\.
Kapri, T. (2021\). “Implications of mutual funds’ ESG score on performance .” MA thesis. University of Vaasa.
Kaurissaari, M. (2021\). “Markowitz Revisited: Is there trade\-off between return and responsibility? ” MA thesis.
University of Helsinki.
Kaustia, M. and Yu, W. (2021\). “Greenwashing in Mutual Funds .” In:SSRN e\-Print .
Kazak, E. and Pohlmeier, W. (2019\). “Testing out\-of\-sample portfolio performance .” In:International Journal of
Forecasting 35(2\), pp. 540–554\.
125Kazak, E. and Pohlmeier, W. (2020\). Portfolio Pretesting with Machine Learning . Tech. rep. University of Lancaster.
Kazdin, J., Schwaiger, K., Wendt, V.\-S., and Ang, A. (2021\). “Climate Alpha with Predictors Also Improving
Company Efficiency .” In:The Journal of Impact and ESG Investing 2(2\), pp. 25–56\.
Khan, M. (2019\). “Corporate Governance, ESG, and Stock Returns around the World .” In:Financial Analysts
Journal 75(4\), pp. 103–123\.
Kilmurray, D., Melin, L., and Mercereau, B. (2021\). “Integrating Impact Funds into Mainstream Portfolios .” In:
The Journal of Impact and ESG Investing 1(4\), pp. 103–119\.
Klement, J. (2018\). “Does ESG matter for asset allocation? ” In:SSRN e\-Print .
Krappel, T., Bogun, A., and Borth, D. (2021\). “Heterogeneous Ensemble for ESG Ratings Prediction.” In: arXiv
e\-Print .
Kritzman, M., Kinlaw, W., and Turkington, D. (2017\). A Practitioner’s Guide to Asset Allocation . Wiley. 256 pp.
Krueger, P., Sautner, Z., and Starks, L. T. (2020\). “The importance of climate risks for institutional investors .” In:
The Review of Financial Studies 33(3\), pp. 1067–1111\.
Kumar, R. (2019\). “ESG: Alpha or Duty? ” In:The Journal of Index Investing 9(4\), pp. 58–66\.
Kumar, R. and Khasnis, A. (2020\). “Fallen Angels with ESG Wings .” In:The Journal of Impact and ESG Investing
1(2\), pp. 26–38\.
Kuntz, L.\-C. (2018\). “Portfolio Strategies with Classical and Alternative Benchmarks .” PhD thesis. Georg August
University of Gottingen.
Lai, K.\-H., Zha, D., Wang, G., Xu, J., Zhao, Y., Kumar, D., Chen, Y., Zumkhawaka, P., Wan, M., Martinez, D.,
and Hu, X. (2021\). “TODS: An Automated Time Series Outlier Detection System.” In: arXiv e\-Print .
Lanza, A., Bernardini, E., and Faiella, I. (2020\). “Mind the gap! Machine Learning, ESG Metrics and Sustainable
Investment .” In:SSRN e\-Print .
Le Guenedal, T. and Roncalli, T. (2022\). Portfolio Construction with Climate Risk Measures . Tech. rep. Amundi
Asset Management.
Lee, L.\-E. (2021\). “What Does ESG Investing Really Mean? Implications for Investors of Separating Financial
Materiality and Social Objectives .” In:SSRN e\-Print .
Lee, L.\-E., Giese, G., and Nagy, Z. (2020\). “Combining E, S, and G Scores: An Exploration of Alternative Weighting
Schemes .” In:The Journal of Impact and ESG Investing 1(1\), pp. 94–103\.
Lepetit, F., Le Guenedal, T., Ben Slimane, M., Cherief, A., Mortier, V., Sekine, T., and Stagnol, L. (2021\). The
Recent Performance of ESG Investing, the COVID\-19 Catalyst and the Biden Effect . Tech. rep. Amundi Asset
Management.
Lettau, M. and Pelger, M. (2020\). “Factors That Fit the Time Series and Cross\-Section of Stock Returns .” In:The
Review of Financial Studies 33(5\), pp. 2274–2325\.
Li, X., Xu, F., and Jing, K. (2022\). “Robust enhanced indexation with ESG: An empirical study in the Chinese
Stock Market .” In:Economic Modelling 107, p. 105711\.
Li, Z., Liu, X.\-Y., Zheng, J., Wang, Z., Walid, A., and Guo, J. (2021\). “FinRL\-Podracer: High Performance and
Scalable Deep Reinforcement Learning for Quantitative Finance .” In:ACM International Conference on AI in
Finance .
Lindeman, A. J. (2022\). “ESG Score Design And Portfolio Construction .” In:The Journal of Impact and ESG
Investing 2(3\), pp. 42–60\.
Lindsey, L. A., Pruitt, S., and Schiller, C. (2021\). “The Cost of ESG Investing .” In:SSRN e\-Print .
Lioui, A. (2018\). “ESG Factor Investing: Myth or Reality ? ” In:SSRN e\-Print .
Lioui, A. and Tarelli, A. (2021\). “Chasing The ESG Factor .” In:SSRN e\-Print .
Liu, X.\-Y., Rui, J., Gao, J., Yang, L., Yang, H., Wang, Z., Wang, C. D., and Guo, J. (2022\). “FinRL\-Meta: A
Universe of Near\-Real Market Environments for Data\-Driven Deep Reinforcement Learning in Quantitative
Finance.” In: arXiv e\-Print .
Liu, X.\-Y., Yang, H., Gao, J., and Wang, C. (2021\). “FinRL: Deep Reinforcement Learning Framework to Automate
Trading in Quantitative Finance .” In:SSRN e\-Print .
Lo, A. W. and Zhang, R. (2022\). “Quantifying the Impact of Impact Investing .” In:American Finance Association
Annual Meeting .
Lohre, H., Rother, C., and Schafer, K. A. (2020\). “Hierarchical Risk Parity: Accounting for Tail Dependencies
in Multi\-asset Multi\-factor Allocations .” In:Machine Learning for Asset Management: New Developments and
Financial Applications . Ed. by E. Jurczenko. Wiley, pp. 329–368\.
Lopez, C., Contreras, O., and Bendix, J. (2020\). “ESG Ratings: The Road Ahead .” In:SSRN e\-Print .
126Lopez de Prado, M. (2019\). “A Data Science Solution to the Multiple\-Testing Crisis in Financial Research .” In:The
Journal of Financial Data Science 1(1\), pp. 99–110\.
Lopez de Prado, M. (2020\). Machine learning for asset managers . Cambridge University Press. 190 pp.
Lopez de Prado, M. and Lewis, M. J. (2019\). “Detection of false investment strategies using unsupervised learning
methods .” In:Quantitative Finance 19(9\), pp. 1555–1565\.
Luccioni, A., Baylor, E., and Duchene, N. (2020\). “Analyzing Sustainability Reports Using Natural Language
Processing.” In: arXiv e\-Print .
Macpherson, M., Gasperini, A., and Bosco, M. (2021\). “Artificial Intelligence and FinTech Technologies for ESG
Data and Analysis .” In:SSRN e\-Print .
Madhavan, A. and Sobczyk, A. (2020\). “On the Factor Implications of Sustainable Investing in Fixed\-Income Active
Funds .” In:The Journal of Portfolio Management , jpm.46\.3\.141\.
Madhavan, A., Sobczyk, A., and Ang, A. (2021\). “Toward ESG Alpha: Analyzing ESG Exposures through a Factor
Lens.” In:Financial Analysts Journal 77(1\), pp. 69–88\.
Maiti, M. (2021\). “Is ESG the succeeding risk factor? ” In:Journal of Sustainable Finance \& Investment 11(3\),
pp. 199–213\.
Malavasi, M., Lozza, S. O., and Truck, S. (2021\). “Second order of stochastic dominance efficiency vs mean variance
efficiency .” In:European Journal of Operational Research 290(3\), pp. 1192–1206\.
Mannix, R. (2020\). “Investors turn to raw data over ratings in ESG alpha hunt .” In:Risk.
Margot, V., Geissler, C., Franco, C. D., and Monnier, B. (2021\). “ESG Investments: Filtering versus Machine
Learning Approaches .” In:Applied Economics and Finance 8(2\), p. 1\.
Marinescu, M. (2022\). “Risk\-Based Optimal Portfolio Strategies: A Compendium .” In:SSRN e\-Print .
Martin, R. (2021a). “PyPortfolioOpt: portfolio optimization in Python .” In:Journal of Open Source Software 6(61\),
p. 3066\.
Martin, S. M. (2021b). “Impact Investing. A Practitioner Perspective .” In:Studies of Applied Economics 39(3\).
Marwood, D. and Minnen, D. (2020\). “Safely Boosting Retirement Income by Harmonizing Drawdown Paths .” In:
Journal of Financial Planning 33(11\), pp. 46–60\.
Maschner, C., Moritz, B., and Schmitz, M. (2021\). “Modern Asset Management .” In:SSRN e\-Print .
Matos, P. (2020\). “ESG and Responsible Institutional Investing Around the World: A Critical Review .” In:SSRN
e\-Print .
McIndoe, C. (2020\). “A Data Driven Approach to Market Regime Classification .” MA thesis. Imperial College.
Mendiratta, R., Varsani, H. D., and Giese, G. (2021\). “How ESG Affected Corporate Credit Risk and Performance .”
In:The Journal of Impact and ESG Investing 2(2\), pp. 101–116\.
Mercereau, B. and Melin, L. (2020\). “Optimizing Portfolios across Risk, Return, and Climate .” In:The Journal of
Impact and ESG Investing 1(1\), pp. 115–131\.
Micheli, A. and Neuman, E. (2022\). “Evidence of Crowding on Russell 3000 Reconstitution Events.” In: arXiv
e\-Print .
Milevsky, M. A. (2020\). Retirement Income Recipes in R: From Ruin Probabilities to Intelligent Drawdowns . Springer
International Publishing. 302 pp.
Miralles\-Quiros, J. L., Miralles\-Quiros, M. M., and Nogueira, J. M. (2020\). “Sustainable Development Goals and
Investment Strategies: The Profitability of Using Five\-Factor Fama\-French Alphas .” In:Sustainability 12(5\),
p. 1842\.
Mohanty, S. S., Mohanty, O., and Ivanof, M. (2021\). “Alpha enhancement in global equity markets with ESG overlay
on factor\-based investment strategies .” In:Risk Management 23(3\), pp. 213–242\.
Mooney, T., Rapaka, R., and Vera, T. (2020\). “Dynamic Regime Strategy for Stress Testing and Optimizing
Institutional Investor Portfolios .” In:SSRN e\-Print .
Morgenstern, C., Coqueret, G., and Kelly, J. (2021\). “Tuning Trend\-Following Strategies with Macro ESG Data .”
In:The Journal of Impact and ESG Investing 2(2\), pp. 117–136\.
Naffa, H. and Fain, M. (2022\). “A factor approach to the performance of ESG leaders and laggards .” In:Finance
Research Letters 44 (102073\), p. 102073\.
Nagy, Z., Kassam, A., and Lee, L.\-E. (2016\). “Can ESG Add Alpha? An Analysis of ESG Tilt and Momentum
Strategies .” In:The Journal of Investing 25(2\), pp. 113–124\.
Nofsinger, J. R. and Varma, A. (2021\). “Keeping Promises? Carbon Risk Disclosure and Mutual Fund Portfolios .”
In:SSRN e\-Print .
127Nugent, T., Stelea, N., and Leidner, J. L. (2020\). “Detecting ESG topics using domain\-specific language models
and data augmentation approaches.” In: arXiv e\-Print .
Ocal, H. and Kamil, A. A. (2021\). “The impact of risk indicators on sustainability (ESG) and broad\-based indices:
an empirical analysis from Germany, France, Indonesia and Turkey .” In:International Journal of Sustainable
Economy 13(1\), p. 18\.
Oikonomou, I., Platanakis, E., and Sutcliffe, C. (2017\). “Socially Responsible Investment Portfolios: Does the
Optimization Process Matter? ” In:SSRN e\-Print .
Ouchen, A. (2021\). “Is the ESG portfolio less turbulent than a market benchmark portfolio? ” In:Risk Management
24, pp. 1–33\.
Oude Veldhuis, N. (2021\). “Corporate Social Responsibility and the effect of ESG scores on stock returns .” MA
thesis. University of Groningen.
Owadally, I., Mwizere, J.\-R., Kalidas, N., Murugesu, K., and Kashif, M. (2021\). “Long\-Term Sustainable Investment
for Retirement .” In:Sustainability 13(9\), p. 5000\.
Pan, L. (2020\). “Demystifying ESG investing considerations for institutional cash investors .” In:The Journal of
Portfolio Management 46(3\), pp. 153–156\.
Parker, F. J. (2021\). “Achieving Goals While Making an Impact: Balancing Financial Goals with Impact Investing .”
In:The Journal of Impact and ESG Investing 1(3\), pp. 27–38\.
Pastor, L., Stambaugh, R. F., and Taylor, L. A. (2021\). “Dissecting Green Returns .” In:SSRN e\-Print .
Pedersen, L. H., Fitzgibbons, S., and Pomorski, L. (2021\). “Responsible investing: The ESG\-efficient frontier .” In:
Journal of Financial Economics 142(2\), pp. 572–597\.
Perrin, S. and Roncalli, T. (2020\). “Machine Learning Optimization Algorithms \& Portfolio Allocation .” In:Machine
Learning for Asset Management: New Developments and Financial Applications . Ed. by E. Jurczenko. Wiley,
pp. 261–328\.
Pham, L. and Nguyen, C. P. (2021\). “Asymmetric tail dependence between green bonds and other asset classes .”
In:Global Finance Journal 50, p. 100669\.
Pisani, F. and Russo, G. (2021\). “Sustainable Finance and COVID\-19: The Reaction of ESG Funds to the 2020
Crisis.” In:Sustainability 13(23\), p. 13253\.
Plagge, J.\-C. and Grim, D. M. (2020\). “Have investors paid a performance price? examining the behavior of ESG
equity funds .” In:The Journal of Portfolio Management 46(3\), pp. 123–140\.
Platanakis, E., Sutcliffe, C. M., and Ye, X. (2021\). “Horses for Courses: Mean\-Variance for Asset Allocation and
1/N for Stock Selection .” In:European Journal of Operational Research 288(1\), pp. 302–317\.
Polbennikov, S., Desclee, A., Dynkin, L., and Maitra, A. (2016\). “ESG Ratings and Performance of Corporate
Bonds .” In:The Journal of Fixed Income 26(1\), pp. 21–41\.
Porage, C. (2021\). “Sustainability in Portfolio Optimization .” MA thesis. Orebro University.
Pyles, M. K. (2020\). “Examining Portfolios Created by Bloomberg ESG Scores: Is Disclosure an Alpha Factor? ”
In:The Journal of Impact and ESG Investing 1(2\), pp. 39–52\.
Qian, W., Rolling, C. A., Cheng, G., and Yang, Y. (2022\). “Combining forecasts for universally optimal perfor\-
mance .” In:International Journal of Forecasting .
Radovanov, B. and Marcikic, A. (2014\). “Testing The Performance Of The Investment Portfolio Using Block Boot\-
strap Method .” In:Economic Themes 52(2\).
Rao, A. and Jelvis, T. (2022\). Foundations of Reinforcement Learning with Applications in Finance .
Raynaud, J., Tankov, P., and Voisin, S. (2020\). “Portfolio Alignment to a 2C Trajectory: Science or Art? ” In:
SSRN e\-Print .
Rebonato, R. (2019\). “A financially justifiable and practically implementable approach to coherent stress testing .”
In:Quantitative Finance 19(5\), pp. 827–842\.
Reboredo, J. C. and Otero, L. A. (2021\). “Are investors aware of climate\-related transition risks? Evidence from
mutual fund flows .” In:Ecological Economics 189, p. 107148\.
Roncalli, T., Le Guenedal, T., Lepetit, F., Roncalli, T., and Sekine, T. (2020\). “Measuring and Managing Carbon
Risk in Investment Portfolios .” In:SSRN e\-Print .
Roncalli, T. (2021a). “Advanced Course in Asset Management .” In:SSRN e\-Print .
Roncalli, T. (2021b). “Green and Sustainable Finance, ESG Investing and Climate Risk .” In:SSRN e\-Print .
Rubbaniy, G., Khalid, A. A., Ali, S., and Naveed, M. (2021\). “Are ESG Stocks Safe\-Haven during COVID\-19? ” In:
SSRN e\-Print .
128Ruf, B. M., Das, N., Chatterjee, S., and Sunder, A. (2019\). “Investments in ESG\-Rated Mutual Funds: Is Good
Better than Great? ” In:The Journal of Wealth Management 22(1\), pp. 49–55\.
Rzenik, A., Hanley, K. W., and Pelizzon, L. (2021\). “The Salience of ESG Ratings for Stock Pricing: Evidence From
(Potentially) Confused Investors .” In:SSRN e\-Print .
Sahin, O., Bax, K., Czado, C., and Paterlini, S. (2022a). “ESGM: ESG scores and the Missing pillar.” In: arXiv
e\-Print .
Sahin, O., Bax, K., Paterlini, S., and Czado, C. (2022b). “The pitfalls of (non\-definitive) Environmental, Social,
and Governance scoring methodology .” In:SSRN e\-Print .
Sarmas, E., Xidonas, P., and Doukas, H. (2020\). Multicriteria Portfolio Construction with Python . Springer Inter\-
national Publishing.
Sautner, Z. and Starks, L. T. (2021\). “ESG and Downside Risks: Implications for Pension Funds .” In:SSRN e\-Print .
Schanzenbach, M. M. and Sitkoff, R. H. (2021\). “ESG Investing: Theory, Evidence, and Fiduciary Principles .” In:
SSRN e\-Print .
Schmidt, A. B. (2020\). “Optimal ESG portfolios: an example for the Dow Jones index .” In:SSRN e\-Print .
Schmidt, A. B. (2021\). “The ESG Conundrum: An Outsider’s View .” In:SSRN e\-Print .
Schmidt, A. B. and Zhang, X. (2021\). “Optimal ESG Portfolios: Which ESG Ratings to Use? ” In:SSRN e\-Print .
Schumann, E. (2019\). “Backtesting .” In:SSRN e\-Print .
Semet, R., Roncalli, T., and Stagnol, L. (2021\). “ESG and Sovereign Risk: What is Priced in by the Bond Market
and Credit Rating Agencies?” In: arXiv e\-Print .
Serafeim, G. (2020\). “Public sentiment and the price of corporate sustainability .” In:Financial Analysts Journal
76(2\), pp. 26–46\.
Serafeim, G. (2021\). “ESG: Hyperboles and Reality .” In:SSRN e\-Print .
Seymour, A., Flint, E. J., and Chikurunhe, F. (2018\). “Dynamic portfolio management strategies: A framework for
historical analysis .” In:SSRN e\-Print .
Shafer, M. and Szado, E. (2020\). “Environmental, social, and governance practices and perceived tail risk .” In:
Accounting \& Finance 60(4\), pp. 4195–4224\.
Shanaev, S. and Ghimire, B. (2021\). “When ESG meets AAA: The effect of ESG rating changes on stock returns .”
In:Finance Research Letters , p. 102302\.
Sharma, A., Syrgkanis, V., Zhang, C., and Kiciman, E. (2021\). “DoWhy: Addressing Challenges in Expressing and
Validating Causal Assumptions.” In: arXiv e\-Print .
Shen, S., LaPlante, A., and Rubtsov, A. (2019\). “Strategic asset allocation with climate change .” In:SSRN e\-Print .
Sherwood, M. W. and Pollard, J. L. (2018\). “The risk\-adjusted return potential of integrating ESG strategies into
emerging market equities .” In:Journal of Sustainable Finance \& Investment 8(1\), pp. 26–44\.
Shi, X., Xu, D., and Zhang, Z. (2022\). “Deep Learning Algorithms for Hedging with Frictions.” In: arXiv e\-Print .
Siebert, J., Gross, J., and Schroth, C. (2021\). “A systematic review of Python packages for time series analysis .”
In:Engineering Proceedings 5(1\) (22\).
Silva, A. F. A., Lôpo, R., and Lofiego, P. (2021\). “ESG Integration Strategy for Stocks Portfolios Based on a
Resampling Methodology with a Multivariate Normal Distribution .” In:SSRN e\-Print .
Simos, T. E., Mourtas, S. D., and Katsikis, V. N. (2021\). “Time\-varying Black–Litterman portfolio optimization
using a bio\-inspired approach and neuronets .” In:Applied Soft Computing 112, p. 107767\.
Simpson, C., Rathi, A., and Kishan, S. (2021\). “The ESG Mirage .” In:Bloomberg Businessweek .
Snow, D. (2019\). “Machine learning in asset management .” In:SSRN e\-Print .
Snow, D. (2020a). “Machine Learning in Asset Management \- Part 2: Portfolio Construction \- Weight Optimization .”
In:The Journal of Financial Data Science 2 (2\), pp. 17–24\.
Snow, D. (2020b). “Machine Learning in Asset Management Part 1: Portfolio Construction Trading Strategies .” In:
The Journal of Financial Data Science 2(1\) (1\), pp. 10–23\.
Sokolov, A., Caverly, K., Mostovoy, J., Fahoum, T., and Seco, L. (2021a). “Weak Supervision and Black\-Litterman
for Automated ESG Portfolio Construction .” In:The Journal of Financial Data Science 3(3\), pp. 129–138\.
Sokolov, A., Mostovoy, J., Ding, J., and Seco, L. (2021b). “Building Machine Learning Systems for Automated ESG
Scoring .” In:The Journal of Impact and ESG Investing 1(3\), pp. 39–50\.
Sorensen, E., Chen, M., and Mussalli, G. (2021\). “The Quantitative Approach for Sustainable Investing .” In:The
Journal of Portfolio Management 47(8\), pp. 38–49\.
Statman, M. and Glushkov, D. (2016\). “Classifying and Measuring the Performance of Socially Responsible Mutual
Funds .” In:The Journal of Portfolio Management 42(2\), pp. 140–151\.
129Stotz, O. (2021\). “Expected and realized returns on stocks with high\- and low\-ESG exposure .” In:Journal of Asset
Management 22, pp. 133–150\.
Suhonen, A., Lennkh, M., and Perez, F. (2017\). “Quantifying Backtest Overfitting in Alternative Beta Strategies .”
In:The Journal of Portfolio Management 43 (2\), pp. 90–104\.
Swedroe, L. (2021a). “Do Wide Divergences in ESG Ratings Doom Investors? ” In:Advisor Perspectives .
Swedroe, L. (2021b). “ESG Investing Means Lower Bond Yields .” In:Advisor Perspectives .
Swedroe, L. (2021c). “Revisionist History in ESG Ratings .” In:Advisor Perspectives .
Swedroe, L. (2021d). “Socially Responsible Funds Do Not Deliver Excess Returns .” In:Advisor Perspectives .
Swinkels, L. (2021\). “Allocating to green bonds .” In:SSRN e\-Print .
Taleb, W., Le Guenedal, T., Lepetit, F., Mortier, V., Sekine, T., and Stagnol, L. (2020\). “Corporate ESG News
and The Stock Market .” In:SSRN e\-Print .
Taljaard, B. H. and Maré, E. (2021\). “Why has the equal weight portfolio underperformed and what can we do
about it? ” In:Quantitative Finance 21(11\), pp. 1855–1868\.
Tang, D. Y., Yan, J., and Yao, Y. (2021\). “The Determinants of ESG Ratings: Rater Ownership Matters .” In:SSRN
e\-Print .
Tatsat, H., Puri, S., and Lookabaugh, B. (2020\). Machine Learning and Data Science Blueprints for Finance: From
Building Trading Strategies to Robo\-Advisors Using Python . O’Reilly. 400 pp.
Tayali, S. T. (2020\). “A novel backtesting methodology for clustering in mean–variance portfolio optimization .” In:
Knowledge\-Based Systems 209, p. 106454\.
Terpstra, M. (2021\). “ESG ratings and stock performance: Do high ESG portfolios perform differently within and
between industries? ” MA thesis. University of Groningen.
Tharavanij, P. (2021\). “ESG Rating and Financial Performance: A Review Article .” In:SSRN e\-Print .
Tokat\-Acikel, Y., Aiolfi, M., Johnson, L., Hall, J., and Jin, J. ( (2021\). “Top\-Down Portfolio Implications of Climate
Change .” In:The Journal of Portfolio Management 47(9\), pp. 69–91\.
Traccucci, P., Dumontier, L., Garchery, G., and Jacot, B. (2019\). “A Triptych Approach for Reverse Stress Testing
of Complex Portfolios .” In:Risk (Cutting Edge) .
Tuck, J., Barratt, S., and Boyd, S. (2022\). “Portfolio Construction Using Stratified Models .” In:Machine Learning
in Financial Markets: A guide to contemporary practices . Ed. by A. Capponi and C.\-A. Lehalle. Cambridge
University Press.
Ungolo, F., Sherris, M., and Zhou, Y. (2021\). “affine\_mortality: A Github repository for estimation, analysis, and
projection of affine mortality models .” In:SSRN e\-Print .
Valentine, K. D., Buchanan, E. M., Scofield, J. E., and Beauchamp, M. T. (2019\). “Beyond p values: utilizing
multiple methods to evaluate evidence .” In:Behaviormetrika 46(1\), pp. 121–144\.
Vamossy, D. and Skog, R. (2021\). “EmTract: Investor Emotions and Market Behavior.” In: arXiv e\-Print .
van der Meulen, W. (2021\). “Assessment of SRI portfolio performance with particular attention to crisis periods .”
MA thesis. University of Groningen.
van Tilborg, N. P. . (2021\). “(Ir)responsible Investing: Revisiting the Effects of ESG Performance on Portfolio
Returns .” MA thesis. University of Groningen.
Vanini, P. (2020\). “Asset Management .” In:SSRN e\-Print .
Varmaz, A., Fieberg, C., and Poddig, T. (2021\). “Portfolio optimization for sustainable investments .” In:SSRN
e\-Print .
Venturini, A. (2022\). “Climate change, risk factors and stock returns: A review of the literature .” In:International
Review of Financial Analysis 79, p. 101934\.
Vincent, K., Hsu, Y.\-C., and Lin, H.\-W. (2018\). “Analyzing the Performance of Multifactor Investment Strategies
under a Multiple Testing Framework .” In:The Journal of Portfolio Management 44(4\), pp. 113–126\.
Vinod, H. D. (2021\). “R Package GeneralCorr Functions for Portfolio Choice .” In:SSRN e\-Print .
Vojtko, R. and Padysak, M. (2020\). “Quant look on ESG investing strategies .” In:SSRN e\-Print .
von Ditfurth, M., Paarmann, T., and Radatz, E. (2021\). “Low volatility and ESG investing combined: Invesco’s
holistic approach .” In:SSRN e\-Print .
Vovk, V. and Wang, R. (2020\). “True and false discoveries with e\-values .” In:arXiv e\-Print .
Vovk, V. and Wang, R. (2021\). “E\-values: Calibration, combination, and applications .” In:Annals of Statistics
49(3\), pp. 1736–1753\.
Walkshausl, C. (2018\). “Dissecting the performance of socially responsible firms .” In:The Journal of Investing 27(2\),
pp. 29–40\.
130Wang, Z., Liao, K., and Zhang, Y. (2022\). “Does ESG Screening Enhance or Destroy Stock Portfolio Value? Evidence
from China .” In:Emerging Markets Finance and Trade , pp. 1–15\.
Webersinke, N., Kraus, M., Bingler, J. A., and Leippold, M. (2021\). “ClimateBert: A Pretrained Language Model
for Climate\-Related Text.” In: arXiv e\-Print .
Westcott, M., Ward, J., Surminski, S., Sayers, P., Bresch, D. N., and Claire, B. (2020\). “Be Prepared: Explor\-
ing Future Climate\-Related Risk for Residential and Commercial Real Estate Portfolios .” In:The Journal of
Alternative Investments 23(1\), pp. 24–34\.
Wiecki, T., Campbell, A., Lent, J., and Stauth, J. (2016\). “All That Glitters Is Not Gold: Comparing Backtest
and Out\-of\-Sample Performance on a Large Cohort of Trading Algorithms .” In:The Journal of Investing 25(3\),
pp. 69–80\.
Wilhelmsen, E. B. and Woods, E. (2021\). “ESG ratings and stock performance : an empirical investigation of the
link between ESG ratings and stock performance of European large cap firms .” MA thesis. Norwegian School of
Economics.
Xiong, J. X. (2021\). “The Impact of ESG Risk on Stocks .” In:The Journal of Impact and ESG Investing 2(1\),
pp. 7–18\.
Yang, Y., UY, M. C. S., and Huang, A. (2020\). “FinBERT: A Pretrained Language Model for Financial Commu\-
nications.” In: arXiv e\-Print .
Yeh, C., Meng, C., Wang, S., Driscoll, A., Rozi, E., Liu, P., Lee, J., Burke, M., Lobell, D. B., and Ermon, S. (2021\).
“SustainBench: Benchmarks for Monitoring the Sustainable Development Goals with Machine Learning.” In:
arXiv e\-Print .
Yoshino, N. and Yuyama, T. (2021\). “Studies of Applied Economics .” In:ESG/Green Investment and Allocation of
Portfolio Assets 39(3\).
Yu, L. (2021\). “Comparing Classical Portfolio Optimization and Robust Portfolio Optimization on Black Swan
Events .” MA thesis. University of Waterloo.
Yu, L., Hardle, W. K., Borke, L., and Benschop, T. (2020\). “An AI approach to measuring financial risk .” In:SSRN
e\-Print .
Zhang, C., Li, Y., Chen, X., Jin, Y., Tang, P., and Li, J. (2020a). “DoubleEnsemble: A New Ensemble Method Based
on Sample Reweighting and Feature Selection for Financial Data Analysis .” In:IEEE International Conference
on Data Mining (ICDM) . IEEE.
Zhang, F., Guo, R., and Cao, H. (2020b). “Information Coefficient as a Performance Measure of Stock Selection
Models .” In:arXiv e\-Print .
Zhang, L. (2021\). “ESG Rating Divergence: Beauty Is in the Eye of the Beholder .” In:The Journal of Index Investing
12(3\), pp. 53–63\.
Zhang, Z., Zohren, S., and Roberts, S. (2020c). “Deep Learning for Portfolio Optimization .” In:The Journal of
Financial Data Science 22(4\), pp. 8–20\.
131Appendix A: Overviews of investment processes and models in QWIM
References
List of references:
Coqueret and Guida ( Machine Learning for Factor Investing: R Version , 2020\)
Dixon et al. ( Machine Learning in Finance: from theory to practice , 2020\)
Fabozzi et al. ( Asset Management: Tools and Issues , 2021\)
Grealish and Kolm (“Robo\-Advisory: From Investing Principles and Algorithms to Future Developments,” 2021\)
Homescu (“Many risks, one (optimal) portfolio,” 2014\)
Homescu (“Better Investing Through Factors, Regimes and Sensitivity Analysis,” 2015\)
Jansen (Machine Learning for Algorithmic Trading (Second Edition) , 2020\)
Jurczenko et al. ( Machine Learning for Asset Management , 2020\)
Kritzman et al. ( A Practitioner’s Guide to Asset Allocation , 2017\)
Lopez de Prado ( Machine learning for asset managers , 2020\)
Maschner et al. (“Modern Asset Management,” 2021\)
Perrin and Roncalli (“Machine Learning Optimization Algorithms \& Portfolio Allocation,” 2020\)
Roncalli (“Advanced Course in Asset Management,” 2021\)
Vanini (“Asset Management,” 2020\)
Online courses
List of online courses:
•Investment Management with Python and Machine Learning Specialization
Introduction to Portfolio Construction and Analysis with Python
Advanced Portfolio Construction and Analysis with Python
Python and Machine Learning for Asset Management
Python and Machine Learning for Asset Management with Alternative Data Sets
•Machine Learning and Reinforcement Learning in Finance Specialization
Guided Tour of Machine Learning in Finance
Fundamentals of Machine Learning in Finance
Reinforcement Learning in Finance
Overview of Advanced Methods of Reinforcement Learning in Finance
•Investment Management Specialization
Understanding Financial Markets
Meeting Investors’ Goals
Portfolio and Risk Management
Securing Investment Returns in the Long Run
Planning your Client’s Wealth over a 5\-year Horizon
•Investment and Portfolio Management Specialization
Global Financial Markets and Instruments
Portfolio Selection and Risk Management
Biases and Portfolio Selection
Investment Strategies and Portfolio Analysis
Build a Winning Investment Portfolio
132Appendix C: Incorporating comparison of portfolio metrics using bench\-
mark portfolios
For your QWIM project it is likely that you would compare investment portfolios constructed using your method(s)
versus benchmark portfolios constructed using most common "optimal portfolio" types used in the industry and in
academia. See below for an example of how this can be done.
Figure 6: Example of portfolio optimization process
Source: PyPortfolioOpt
Portfolio optimization methods
List of portfolio optimization methods may include (see Roncalli (“Advanced Course in Asset Management,” 2021\)
andPerrin and Roncalli (“Machine Learning Optimization Algorithms \& Portfolio Allocation,” 2020\) for a com\-
prehensive overview of such methods):
•equal weighting
•mean variance optimization (Markowitz)
•minimum variance optimization
•maximum diversification
•risk budgeting/risk parity
•hierarchical risk parity
•Black\-Litterman
•robust versions of some the above portfolio optimization methods
Some relevant links:
•Portfolio Optimization: A General Framework for Portfolio Choice
•Performance of risk\-based asset allocation strategies
•Revisiting the Portfolio Optimization Machine Portfolio
•Construction Techniques Applied to Traditional Multi Asset Portfolios
133Python and R packages/codes for portfolio optimization
•Codes mentioned in Snow (“Machine Learning in Asset Management \- Part 2: Portfolio Construction \- Weight
Optimization,” 2020\)
•Empyrial
•MLFinLab
•Optimal Portfolio
•PortfolioAnalytics
•PortfolioLab
•PyPortfolioOpt
•Quantropy
•Riskfolio\-Lib
•RiskPortfolios
•riskparityportfolio
Portfolio metrics
List of portfolio metrics may include some of the following (see Bacon (“Performance Attribution: History and
Progress,” 2019\) for a comprehensive list):
•Sharpe ratio
•Sortino ratio
•Information ratio
•Maximum Drawdown
•expected shortfall
•maximum loss
•and more.
Some relevant links:
•Portfolio metrics
•Picking the Right Risk\-Adjusted Performance Metric
•Risk\-Adjusted Performance Measurement – State of the Art
•An Investor’s Guide to the Risk Versus Return Conundrum
•How sharp is the Sharpe ratio? Risk\-adjusted Performance Measures
134Python and R packages/codes for portfolio metrics and performance evaluation
•bt
•empyrical
•ffn
•JFE
•MLFinLab
•PerformanceAnalytics
•portfolioBacktest
•Portfolio Optimization and Performance Evaluation
•Pyfolio
•QuantStats
•Riskfolio\-Lib
•tidyquant
How to compare investment portfolios
Let us consider portfolio optimization methods (selected from the ones implemented in Python and/or R packages
mentioned above, such as PyPortfolioOpt) which rely on based on expected returns and expected covariance matrix.
One would construct two portfolios (let’s call them Traditional and Enhanced) using the same portfolio op\-
timization method(s), where the only difference would be in terms of the inputs (expected returns and expected
covariance matrix) to the optimization method:
As of the date of portfolio construction, expected returns and expected covariance matrix can be either calculated
using only historical data or, respectively, output from your model. Then one would compare side\-by\-side various
portfolio metrics for these two portfolios. Comparison would be done across the entire Out\-Of\-Sample period, and
also across each market regine period.
NOTE: If you have N forecasting methods used in your coding framework, then for each optimizaton method
you would end up with (1\+N) optimal portfolios
To exemplifty, let’s say that you want to construct portfolios at date of June 20, 2019, and you have data as
below
•Range of entire dataset: January 1st, 1990 \- August 1, 2020
•Range of Training dataset: January 1st, 1990\- February 20, 2017
•Range of Test dataset: February 20, 2017 \- August 1, 2020
For Traditional portfolio:
•vector of expected means is calculated based on historical data available at June 20, 2019 (namely from 1990
to June 19, 2019\)
•expected covariance matrix is calculated based on historical data available at June 20, 2019 (namely from
1990 to June 19, 2019\)
For Enhanced portfolio:
•vector of expected means is calculated based on forecasted values available at June 20, 2019 and obtained
using the forecasted model trained on given training dataset (which is from 1990 to 2017\)
135•expected covariance matrix is calculated based on forecasted values available at June 20, 2019 and obtained
using the forecasted model trained on given training dataset (which is from 1990 to 2017\)
Then one would compare various portfolio metrics among the two portfolios. These metrics can be calculated on
following time periods:
•from date of portfolio construction (June 20, 2019\) to last date for which you have data (August 1, 2020\)
•from starting date of dataset (January 1st, 1990\) to last date for which you have data (August 1, 2020\)
•from starting date of dataset (January 1st, 1990\) to date of portfolio construction (June 20, 2019\)
So you would have side\-by\-side comparisons of portfolio metrics for each of the above 3 time periods.
Portfolio metrics can be calculated using various Python and/or R packages mentioned above.
136