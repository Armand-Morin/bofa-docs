Retirement portfolios and strategies in quantitative wealth and
investment management QWIM
Cristian Homescu
December 2022
Abstract
This document provides details for this QWIM project and it incorporates the following sections
•Motivation
•Relevant references
•Suggested project tasks and timelines
•Practical info
Recommended software tools
Recommended datasets
•Design and implementation for the project codes
•Potentially useful Python and R packages codes and frameworks
•Appendices
Appendices include
•Overviews of investment processes and models in QWIM
•Comparison of investment portfolios using portfolios metrics and benchmark portfolios
Contents
1 Motivation for the project 4
2 Relevant references 5
2\.1 Main references . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
2\.2 Comprehensive list of references . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
2\.2\.1 Retirement portfolios and strategies . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
2\.2\.2 Goal\-based investing strategies for retirement . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
2\.2\.3 ESG\-based investing strategies for retirement . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
2\.2\.4 Accumulation and decumulation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
2\.2\.5 Taxation within context of retirement strategies . . . . . . . . . . . . . . . . . . . . . . . . . 12
2\.2\.6 Inflation within context of retirement . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13
2\.2\.7 Longevity and mortality within context of retirement strategies . . . . . . . . . . . . . . . . . 14
2\.2\.8 Incorporating costs of health care and long\-term care . . . . . . . . . . . . . . . . . . . . . . . 15
2\.2\.9 Financial advice and planning for retirement . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
2\.2\.10 Annuities . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
2\.2\.11 Sustainable withdrawals and spending in retirement . . . . . . . . . . . . . . . . . . . . . . . 18
2\.2\.12 Retirement income . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
2\.2\.13 Sequence of returns . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
12\.2\.14 Incorporating Social Security . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
2\.2\.15 Glidepath considerations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22
2\.2\.16 Target date strategies . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
2\.2\.17 Risk management for retirement portfolios and strategies . . . . . . . . . . . . . . . . . . . . 24
2\.2\.18 Presentation and visualization of retirement portfolios and strategies . . . . . . . . . . . . . . 25
2\.2\.19 Investor risk profile . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25
2\.2\.20 Testing, evaluating and comparison procedures for retirement portfolios and strategies . . . . 26
3 Practical details for the project 28
3\.1 Interaction with students . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28
3\.2 Data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28
3\.3 Private GitHub repository for the QWIM project . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28
3\.4 Deliverables . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29
3\.5 (Optional) Article submission to leading journals . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29
4 Project tasks and timelines 30
4\.1 Suggested timelines for project tasks . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30
4\.2 Literature review . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30
4\.3 Write\-up summary of literature review . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31
4\.4 Identification of appropriate Python and/or R packages . . . . . . . . . . . . . . . . . . . . . . . . . 31
4\.5 Code design . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31
4\.6 Implementation of coding framework and components . . . . . . . . . . . . . . . . . . . . . . . . . . 32
4\.7 Interactive visualizer . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32
4\.8 Project report and presentation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32
5 Design and implementation for the project codes 33
5\.1 Visualize project workflow and coding framework . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33
5\.2 Representative examples of Python libraries with well designed folder structure . . . . . . . . . . . . 37
6 Practical Info 38
6\.1 Recommended software tools . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 38
6\.1\.1 Python . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 38
6\.1\.2 R . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 38
6\.1\.3 R IDE . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 38
6\.1\.4 Python IDE . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 38
6\.1\.5 Bibliography Manager . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 38
6\.1\.6 Document processor . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 39
6\.1\.7 Source control manager . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 39
6\.1\.8 File editor . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 39
6\.1\.9 Runtime libraries . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 39
6\.2 Recommended datasets . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 39
7 Potentially useful Python and R software implementations: packages, codes and frameworks 42
7\.1 Collections and repositories of resources . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 42
7\.2 Connection between Python and R codes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 42
7\.3 Anomaly detection and data outliers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 43
7\.4 Bayesian analysis and modeling . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 44
7\.5 Causality, inference and dependencies . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 46
7\.6 Classification, Motifs, Neighbors, Wavelets, Transforms . . . . . . . . . . . . . . . . . . . . . . . . . . 47
7\.7 Clustering . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 49
7\.8 Coding utilities and frameworks . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 52
7\.9 Computational performance . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 56
7\.10 Containers, projects, pipelines and deployment . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 57
7\.11 Covariances, correlations and volatilities . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 58
7\.12 Data analysis and exploration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 59
27\.13 Data augmentation, scenario generation and synthetic time series . . . . . . . . . . . . . . . . . . . . 61
7\.14 Data cleaning, preparation and validation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 63
7\.15 Data Imputation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 64
7\.16 Data regimes, states and changepoints: analysis and modeling . . . . . . . . . . . . . . . . . . . . . . 66
7\.17 Data structures, storage and serialization . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 68
7\.18 Dates and times . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 70
7\.19 Dimensionality reduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 71
7\.20 Distances and Similarity . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 72
7\.21 ESG and Impact Investing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 73
7\.22 Explainability, Interpretability, Fairness, Data Privacy . . . . . . . . . . . . . . . . . . . . . . . . . . 74
7\.23 Features for time series . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 75
7\.24 Filtering and spectral analysis for time series . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 76
7\.25 Forecasting time series . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 77
7\.26 Graphs and graphical modeling . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 82
7\.27 Linear algebra . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 82
7\.28 Machine Learning . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 83
7\.29 Machine Learning frameworks (includes Automated ML and hyperparameters tuning) . . . . . . . . 87
7\.30 Network and graph analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 88
7\.31 Numerical methods (includes numerical optimization) . . . . . . . . . . . . . . . . . . . . . . . . . . 90
7\.32 Probabilistic modeling (includes mixture models and Gaussian Processes) . . . . . . . . . . . . . . . 92
7\.33 Reinforcement learning . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 95
7\.34 Robust numerical methods . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 97
7\.35 Selection of features, variables, models, data splits . . . . . . . . . . . . . . . . . . . . . . . . . . . . 98
7\.36 Sensitivity analysis and numerical derivatives . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 101
7\.37 Statistics and Probability . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 101
7\.38 Stress testing, rare events, extreme values and scenarios, survival analysis . . . . . . . . . . . . . . . 103
7\.39 Symbolic regression \& data\-driven model discovery and machine learning . . . . . . . . . . . . . . . 104
7\.40 Testing (numerical, statistical, etc.), comparison and ranking . . . . . . . . . . . . . . . . . . . . . . 105
7\.41 Testing software codes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 109
7\.42 Time series analysis and modeling . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 110
7\.43 Text, sentiment and topic analytics (including NLP) . . . . . . . . . . . . . . . . . . . . . . . . . . . 113
7\.44 Uncertainty: analysis and modeling . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 115
7\.45 Visualization and reporting . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 116
8 Codes for QWIM (Quantitative Wealth and Investment Management) 120
8\.1 Collections of resources . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 120
8\.2 Research studies with code . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 121
8\.3 Python software implementations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 122
8\.4 R software implementations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 124
References 126
Appendix A: Overviews of investment processes and models in QWIM 150
Appendix C: Comparison of investment using portfolios metrics and benchmark portfolios 151
31 Motivation for the project
A successful investment process for retirement incorporates many components, including:
•savings and earnings
•asset allocation and location
•goals\-based investing
•market returns
•taxation
•longevity
•health care costs
•long\-term costs
•inflation
•Social Security
•accumulation and decumulation
42 Relevant references
2\.1 Main references
List of references:
Ackerley et al. ( To spend or not to spend? 2022\)
Ali et al. (“Social Security Benefit Valuation, Risk, and Optimal Retirement,” 2019\)
Alsabah et al. (“Robo\-Advising: Learning Investors Risk Preferences via Portfolio Choices,” 2021\)
Arnold et al. (“Using ”Equivalent Tax Rates” to Determine Tax\-Efficient Retirement Investment and With\-
drawal,” 2018\)
Bailey et al. ( Planning for health care costs in retirement , 2021\)
Banerjee ( Asset Decumulation or Asset Preservation? What Guides Retirement Spending? 2019\)
Bengen (“The Planner’s Toolkit for Managing Retirement Withdrawal Plans,” 2021\)
Bernhardt and Donnelly ( Pension Decumulation Strategies: A State\-of\-the\-Art Report , 2018\)
Blanchett and Finke (“Should Annuities be Purchased from Tax\-Sheltered Assets?” 2019\)
Blanchett (“The value of allocating to annuities,” 2020\)
Blanchett (“Minding the Gap in Subjective Mortality Estimates,” 2021\)
Butt et al. (“Principles and Rules for Translating Retirement Objectives into Strategies,” 2021\)
Capponi et al. (“Personalized Robo\-Advising: Enhancing Investment through Client Interaction,” 2020\)
Cassidy et al. (“Be Kind to Your Retirement Plan \- Give It a Benchmark,” 2013\)
Chen and Munnell ( How Much Taxes Will Retirees Owe on Their Retirement Income? 2021\)
Chen et al. (“Personalised drawdown strategies and partial annuitisation to mitigate longevity risk,” 2021\)
Clare et al. (“Measuring sequence of returns risk,” 2020\)
Clare et al. (“Perfect Withdrawal in a Noisy World: Investing Lessons with and without Annuities while in
Drawdown between 2000 and 2019,” 2021\)
Collins (“Annuities and retirement income planning,” 2016\)
Collins et al. (“How Risky is Your Retirement Income Risk Model?” 2015\)
Costa et al. ( Fuel for the F.I.R.E.: Updating the 4% rule for early retirees , 2021\)
Crook and Sutedja (“Will Long\-Term Care Ruin Retirement Plans?” 2017\)
D’Acunto and Rossi (“New Frontiers of Robo\-Advising: Consumption, Saving, Debt Management, and Taxes,”
2021\)
Daher et al. ( From Accumulation to Decumulation – Why It Matters and What Plan Sponsors Should Know ,
2020\)
Dang et al. (“The 4 percent strategy revisited: a pre\-commitment mean\-variance optimal approach to wealth
management,” 2017\)
Das et al. (“Dynamic portfolio allocation in goals\-based wealth management,” 2020\)
Das et al. (“Optimal Goals\-Based Investment Strategies For Switching Between Bull and Bear Markets,” 2022\)
Das et al. (“Dynamic optimization for multi\-goals wealth management,” 2022\)
Das and Varma (“Dynamic Goals\-Based Wealth Management using Reinforcement Learning,” 2020\)
Das and Ross (“The Role of Options in Goals\-Based Wealth Management,” 2021\)
Dempster et al. (“Lifecycle Goal Achievement or Portfolio Volatility Reduction?” 2016\)
Dempster and Medova (“Asset Liability Management for Individual Households,” 2011\)
DeJong and Robinson (“A Case Study in Sequence Risk: A 20\-Year Retrospective on the Impact of the 2000\-2002
and 2007\-2009 Bear Markets on Retirement Nest Egg Sustainability,” 2022\)
Diamond et al. (“Optimal Claiming of Social Security Benefits,” 2021\)
DiJoseph ( Spending guidelines to help ease retirees’ market worries , 2020\)
DiLellio and Ostrov (“Constructing Tax Efficient Withdrawal Strategies for Retirees with Traditional 401(k)/IRAs,
Roth 401(k)/IRAs, and Taxable Accounts,” 2019\)
Ding et al. (“Statistical Learning for Individualized Asset Allocation,” 2022\)
Dixon and Halperin (“Goal\-based wealth management with generative reinforcement learning,” 2021\)
Dunham and Washer (“Using Life Tables for Retirement Planning,” 2020\)
Elkins (Stanford analyzed 292 retirement strategies to determine the best one – here’s how it works , 2019\)
Estrada (“Refining the Failure Rate,” 2017\)
Estrada (“Replacing the Failure Rate: A Downside Risk Perspective,” 2017\)
Estrada (“From Failure to Success: Replacing the Failure Rate,” 2018\)
5Estrada (“Maximum Withdrawal Rates: A Novel and Useful Tool,” 2017\)
Estrada (“Maximum withdrawal rates: an empirical and global perspective,” 2018\)
Estrada (“Retirement Planning: From Z to A,” 2020\)
Estrada (“Target\-Date Funds, Glidepaths, and Risk Aversion,” 2020\)
Estrada (“Sequence Risk: Is It Really a Big Deal?” 2021\)
Estrada (“The Sustainability of (Global) Withdrawal Strategies,” 2021\)
Estrada and Kritzman (“Toward Determining the Optimal Investment Strategy for Retirement,” 2019\)
Estrada and Kritzman (“Evaluating Retirement Strategies: A Utility\-Based Approach,” 2018\)
Fellowes et al. ( The Retirement Solution Hiding in Plain Sight: How Much Retirees Would Gain by Improving
Social Security Decisions , 2019\)
Finke and Blanchett (“An Overview of Retirement Income Strategies,” 2016\)
Fonseca et al. (“Accounting for the Rise of Health Spending and Longevity,” 2021\)
Forsyth et al. (“Optimal Asset Allocation for DC Pension Decumulation with a Variable Spending Rule,” 2020\)
Forsyth et al. (“Optimal control of the decumulation of a retirement portfolio with variable spending and dynamic
asset allocation,” 2021\)
Forsyth et al. (“Optimal control of the decumulation of a retirement portfolio with variable spending and dynamic
asset allocation,” 2021\)
Forsyth (“Two stage decumulation strategies for DC plan investors,” 2021\)
Forsyth (“A Stochastic Control Approach to Defined Contribution Plan Decumulation: ”The Nastiest, Hardest
Problem in Finance”,” 2022\)
Forsyth (“Short term decumulation strategies for underspending retirees,” 2022\)
Gabudean and Weiss (“How to Evaluate Target\-Date Funds: A Practical Guide,” 2019\)
Geisler et al. (“A Comparison of the Tax Efficiency of Decumulation Strategies,” 2021\)
Goodman and Richardson (“Achieving Retirement Income Security: A Comparison of Guaranteed Lifetime
Withdrawal Benefit, Systematic Withdrawal and Partial Variable Annuity Strategies,” 2019\)
Goldman Sachs Asset Management Research ( Retirement Realities: Time For Change: Retirement Survey \&
Insights Report 2021 , 2021\)
Halen et al. (“Understanding the True Cost of Health Care in Retirement,” 2020\)
Harbron et al. ( Withdrawal order: making the most of retirement assets , 2019\)
Harris (“Should a Retiree File for Social Security at 62 or 70?” 2019\)
Hosseini et al. (“The evolution of health over the life cycle,” 2022\)
Irlam (“Machine learning for retirement planning,” 2020\)
Irlam (“Multi Scenario Financial Planning via Deep Reinforcement Learning AI,” 2020\)
Jaconetti et al. ( From assets to income: A goals\-based approach to retirement spending , 2020\)
JP Morgan Asset Management Research ( Guide to Retirement , 2021\)
Jung (“Estimating Markov Transition Probabilities Between Health States Using U.S. Longitudinal Survey
Data,” 2021\)
Kahler et al. ( HSAs: An off\-label prescription for retirement saving , 2020\)
Khang and Clarke ( Safeguarding retirement in a bear market , 2020\)
Klement (“Risk Profiling and Tolerance: Insights for the Private Wealth Manager,” 2018\)
Kobor and Muralidhar (“Targeting Retirement Security with a Dynamic Asset Allocation Strategy,” 2020\)
Kuselias et al. (“The Financial and Tax Considerations of Social Security and Early Retirement,” 2021\)
Laster et al. (“Pitfalls in Retirement,” 2014\)
Laster et al. (“Strategies for Managing Retirement Risks,” 2016\)
Lobel et al. ( The replacement ratio: Making it personal , 2019\)
Lung et al. (“A Framework for Designing Investment Strategies for Default Retirement Plans,” 2021\)
Martellini and Milhau ( Advances in Retirement Investing , 2020\)
Martellini et al. (“’Flexicure’ Retirement Solutions: A Part of the Answer to the Pension Crisis?” 2019\)
Martellini et al. (“Securing Replacement Income with Goal\-Based Retirement Investing Strategies,” 2020\)
Medeiros et al. (“Forecasting Inflation in a Data\-Rich Environment: The Benefits of Machine Learning Methods,”
2021\)
Merton and Muralidhar (“Selfies: A new pension bond and currency for retirement,” 2020\)
Merton and Muralidhar (“A Six\-Component Integrated Approach to Addressing the Retirement Funding Chal\-
lenge,” 2020\)
6Milevsky (“Modeling Human Longevity and Life Tables,” 2020\)
Milevsky (“Calibrating Gompertz in reverse: What is your longevity\-risk\-adjusted global age?” 2020\)
Milevsky (“Intelligent Drawdown Rates,” 2020\)
Milevsky ( Retirement Income Recipes in R: From Ruin Probabilities to Intelligent Drawdowns , 2020\)
Mislinski (“How to Illustrate Planning Risks to Clients,” 2021\)
Mladina (“Optimal Lifetime Asset Allocation with Goals\-Based, Lifecycle Glide Paths,” 2016\)
Mladina (“Refining After\-Tax Return and Risk Parameters,” 2020\)
Mladina and Grant (“Glide Paths Based on a Retirement Goal and Depleting Human Capital,” 2019\)
Murguia and Pfau (“A Model Approach to Selecting a Personalized Retirement Income Strategy,” 2021\)
Mulvey and Hao (“Setting Realistic Goals for Personal Retirement Planning via Micro\-Macro Analyses,” 2020\)
Neville et al. (“The Best Strategies for Inflationary Times,” 2021\)
Owadally et al. (“Optimal investment for a retirement plan with deferred annuities,” 2021\)
Owadally et al. (“Long\-Term Sustainable Investment for Retirement,” 2021\)
Pakula (Guiding your clients through stormy weather: Sustainable withdrawal rates in times of crisis , 2020\)
Paradise and Kahler ( What to do with your next dollar: A quantitative framework , 2020\)
Parker (“Allocation of wealth both within and across goals: a practitioner guide,” 2020\)
Pellerin (“Investing for Retirement Income: A Comparison of Asset Allocations and Spending Strategies,” 2021\)
Pfau (“The four approaches to managing retirement income risk,” 2019\)
Pfau (Retirement Planning Guidebook: Navigating the Important Decisions for Retirement Success , 2021\)
Pruser (“Forecasting US inflation using Markov dimension switching,” 2021\)
Reichenstein (“Saving in Roth Accounts and Making Roth Conversions before Retirement in Today’s Low Tax
Rates,” 2020\)
Reichenstein and Meyer (“Valuing Roth Conversion and Recharacterization Options,” 2017\)
Reichenstein and Meyer (“Understanding the Tax Torpedo and Its Implications for Various Retirees,” 2018\)
Reichenstein and Meyer (“Social Security Claiming Strategies for Singles and Their Implications for Couples,”
2021\)
Reichenstein and Meyer (“Advice for Married Couples When One Spouse Will Die Year(s) Before the Other
Spouse,” 2021\)
Reichenstein and Meyer (“How Social Security Coordination Can Add Value to a Tax\-Efficient Withdrawal
Strategy,” 2021\)
Rietz et al. (“A Simulation for Minimizing both the Probability and the Length of Financial Ruin in Retirement,”
2020\)
Rogalla (“Optimal Portfolio Choice in Retirement With Participating Life Annuities,” 2021\)
Roux and de Villiers (“A simplified approach to estimate the sustainable lifestyle level for retirement planning,”
2020\)
Roy and Kim\-Steiner ( Three retirement spending surprises , 2019\)
Rundle (“A Social Security Purchase: Is Delaying Social Security More Effective than Purchasing a Deferred
Income Annuity?” 2018\)
Ryack (“Incorporating Financial Risk Tolerance Research into the Financial Planning Process,” 2016\)
Sestok (“Implementing Advice based on ”A Comparison of the Tax Efficiency of Decumulation Strategies”,”
2021\)
Scruggs (“Asset Allocation and Withdrawal Strategies: Three Levers for Managing Retirement Outcomes,”
2019\)
Sestok (“Implementing Advice based on ”A Comparison of the Tax Efficiency of Decumulation Strategies”,”
2021\)
Sherwood (“Risk Capacity Portfolio Construction,” 2021\)
Sornwanee (“Multi\-Regime, Goal\-Based Retirement Solutions: Sensitivity Analysis and Post\-Retirement Per\-
formance Comparison of Dynamic Strategies,” 2020\)
Suarez (“The perfect withdrawal amount over the historical record,” 2020\)
Sosner et al. (“Integration of Income and Estate Tax Planning,” 2021\)
Vanguard Research ( Dynamic spending: A better way to budget in retirement , 2020\)
Van Harlow et al. (“The Use and Value of Financial Advice for Retirement Planning,” 2020\)
Veres (“A Comparison of Risk Tolerance Products,” 2020\)
Vrdoljak et al. (“The Role of Variable Annuities in Addressing Retirement Risks,” 2014\)
7Warshawsky (“Reforming Retirement Income: Annuitization, Combination Strategies, and Required Minimum
Distributions,” 2018\)
Wolfe and Brazier ( Spending retirement assets ... or not? 2018\)
Wolfe and Ferraro ( Decumulation challenges and potential solutions – Helping build a pathway towards retirement
spending and income confidence , 2022\)
Xu (“Static and Dynamic Tax Diversification of Withdrawals from Multiple Individual Retirement Accounts,”
2018\)
Xu and Hoesch (“Predicting longevity: an analysis of potential alternatives to life expectancy reports,” 2018\)
Young (Tax\-Efficient Withdrawal Strategies , 2020\)
Zhang (“Optimal Retirement Planning: Scenario Generation, Preferences, and Objectives,” 2018\)
Zuss (Participants Will Need Support to Understand Lifetime Income Projections , 2022\)
2\.2 Comprehensive list of references
2\.2\.1 Retirement portfolios and strategies
References:
Basu and Wiafe (“Impact of persistent bad returns and volatility on retirement outcomes,” 2017\)
Browning et al. (“Spending in Retirement,” 2020\)
Blanchett et al. (“Required Retirement Savings Rates Today,” 2016\)
Blanchett et al. (“Low Returns and Optimal Retirement Savings,” 2018\)
Buetow et al. (“Active management in defined contribution plans,” 2020\)
Buetow and Hanke (“How Long is Long Enough?” 2020\)
Butt et al. (“Principles and Rules for Translating Retirement Objectives into Strategies,” 2021\)
Chen et al. (“Optimal retirement products under subjective mortality beliefs,” 2021\)
Clare et al. (“Measuring sequence of returns risk,” 2020\)
Clark et al. (“How Persistent Low Returns Will Shape Saving and Retirement,” 2018\)
Chen et al. (“Combining Flexible Asset Allocation, Sustainable Withdrawals, and Deferred Annuities to provide
an Adaptive Lifelong Investing Solution,” 2021\)
Chen and Langrene (“Deep neural network for optimal retirement consumption in defined contribution pension
system,” 2020\)
Chen et al. (“Optimal retirement products under subjective mortality beliefs,” 2021\)
Chien (Enhancing Retirement Success Rates in the United States , 2019\)
Dang et al. (“The 4 percent strategy revisited: a pre\-commitment mean\-variance optimal approach to wealth
management,” 2017\)
Das et al. (“Combining Investment and Tax Strategies for Optimizing Lifetime Solvency under Uncertain Returns
and Mortality,” 2020\)
Ding et al. (“Statistical Learning for Individualized Asset Allocation,” 2022\)
Donnelly et al. (“Investing for retirement: Terminal wealth constraints or a desired wealth target?” 2022\)
Drew et al. (“Improving retirement adequacy through asset class prioritization,” 2014\)
Dunham and Washer (“Using Life Tables for Retirement Planning,” 2020\)
Elkins (Stanford analyzed 292 retirement strategies to determine the best one – here’s how it works , 2019\)
Estrada (“Retirement Planning: From Z to A,” 2020\)
Estrada (“Target\-Date Funds, Glidepaths, and Risk Aversion,” 2020\)
Estrada and Kritzman (“Toward Determining the Optimal Investment Strategy for Retirement,” 2019\)
Forsyth and Vetzal (“Optimal asset allocation for retirement saving: deterministic vs. time consistent adaptive
strategies,” 2019\)
Forsyth et al. (“Optimal Asset Allocation for DC Pension Decumulation with a Variable Spending Rule,” 2020\)
Forsyth et al. (“Optimal control of the decumulation of a retirement portfolio with variable spending and dynamic
asset allocation,” 2021\)
Forsyth et al. (“Optimal control of the decumulation of a retirement portfolio with variable spending and dynamic
asset allocation,” 2021\)
Gemmo et al. (“Optimal portfolio choice with tontines under systematic longevity risk,” 2020\)
Fox (“Linking metrics to objectives: retirement saving, spending, and active management,” 2020\)
Grennon (“A Dynamic Asset Allocation Approach for Selecting a 401K QDIA,” 2015\)
8Grennon (“A Dynamic Approach to Retirement Income,” 2016\)
Horneff et al. (“How Persistent Low Expected Returns Alter Optimal Life Cycle Saving, Investment, and Re\-
tirement Behavior,” 2018\)
Hyams et al. (“Saving for retirement: rules of thumb,” 2020\)
Ilmanen and Rauseo (“Intelligent Risk Taking,” 2018\)
Irlam (“Machine learning for retirement planning,” 2020\)
Irlam (“Lifetime Portfolio Selection: Using Machine Learning,” 2020\)
Israelsen (“Retirement Portfolio Realities: The Mathematics of Survival,” 2017\)
JP Morgan Asset Management Research ( Guide to Retirement , 2021\)
Kahler et al. ( HSAs: An off\-label prescription for retirement saving , 2020\)
Kintzel (“Income Sustainability in Retirement: A Case Study of the Life\-Cycle Account,” 2020\)
Kobor and Muralidhar (“Targeting Retirement Security with a Dynamic Asset Allocation Strategy,” 2020\)
Kopa et al. (“Individual optimal pension allocation under stochastic dominance constraints,” 2018\)
Lung et al. (“A Framework for Designing Investment Strategies for Default Retirement Plans,” 2021\)
Lussier (“Secure retirement: connecting financial theory and human behavior,” 2019\)
Mantilla\-Garcia et al. (“From Defined\-Contribution Towards Target\-Income Retirement Systems,” 2020\)
Martellini and Milhau ( Advances in Retirement Investing , 2020\)
Martellini et al. (“Securing Replacement Income with Goal\-Based Retirement Investing Strategies,” 2020\)
Marwood and Minnen (“Safely Boosting Retirement Income by Harmonizing Drawdown Paths,” 2020\)
Merton (“The Crisis in Retirement Planning,” 2014\)
Merton and Muralidhar (“Selfies: A new pension bond and currency for retirement,” 2020\)
Merton and Muralidhar (“A Six\-Component Integrated Approach to Addressing the Retirement Funding Chal\-
lenge,” 2020\)
Milevsky (“Calibrating Gompertz in reverse: What is your longevity\-risk\-adjusted global age?” 2020\)
Milevsky ( Retirement Income Recipes in R: From Ruin Probabilities to Intelligent Drawdowns , 2020\)
Mitchell et al. (“How Persistent Low Returns Will Shape Saving and Retirement,” 2018\)
Munnell and Webb (“The Impact of Leakages from 401(k)s and IRAs,” 2021\)
Nicolas ( Investment Strategies for Retirement , 2019\)
Owadally et al. (“Optimal investment for a retirement plan with deferred annuities,” 2021\)
Paradise and Kahler ( What to do with your next dollar: A quantitative framework , 2020\)
Pellerin (“Investing for Retirement Income: A Comparison of Asset Allocations and Spending Strategies,” 2021\)
Pfau (“How to Link Retirement Strategies to Sustainable\-Spending Rates,” 2015\)
Pfau (“The four approaches to managing retirement income risk,” 2019\)
Pfau (Retirement Planning Guidebook: Navigating the Important Decisions for Retirement Success , 2021\)
Reichenstein and Meyer (“Investment implications of the rising and falling pattern of marginal tax rates for
retirees,” 2020\)
Reilly and Byrne (“Investing for Retirement in a Low Returns Environment,” 2018\)
Rook (“Multivariate Density Modeling for Retirement Finance,” 2017\)
Ruthbah (“The Retirement Puzzle,” 2020\)
Scruggs (“Asset Allocation and Withdrawal Strategies: Three Levers for Managing Retirement Outcomes,”
2019\)
Sharpe ( Retirement Income Analysis with scenario matrices , 2019\)
Sherwood (“Risk Capacity Portfolio Construction,” 2021\)
Tian and Zhu (“Optimal Investing after Retirement Under Time\-Varying Risk Capacity Constraint,” 2020\)
Tomlinson (“The Unimportance of Asset Allocation in Retirement Planning,” 2020\)
Vanguard Research ( Dynamic spending: A better way to budget in retirement , 2020\)
Van Harlow et al. (“The Use and Value of Financial Advice for Retirement Planning,” 2020\)
Winter and Planchet (“Modern tontines as a pension solution: a practical overview,” 2022\)
Xu and Anichini (“Mean\-Variance Analysis in Post\-Retirement Planning,” 2016\)
2\.2\.2 Goal\-based investing strategies for retirement
References:
9Aliaga\-Diaz et al. ( Vanguard’s Life\-Cycle Investing Model (VLCM): A general portfolio framework for goals\-based
investing , 2021\)
Branning and Grubbs (“Crafting Retirement Income that is Stable, Secure, and Sustainable,” 2019\)
Consigli and Di Tria (“Asset\-liability management and goal\-based investing for retail business,” 2018\)
Consiglio et al. (“Scenario optimization asset and liability modelling for individual investors,” 2006\)
Cvitanic et al. (“Pi portfolio management: reaching goals while avoiding drawdowns,” 2020\)
Das et al. (“Dynamic portfolio allocation in goals\-based wealth management,” 2020\)
Das et al. (“Optimal Goals\-Based Investment Strategies For Switching Between Bull and Bear Markets,” 2022\)
Das et al. (“Optimal Goals\-Based Investment Strategies For Switching Between Bull and Bear Markets,” 2022\)
Das and Varma (“Dynamic Goals\-Based Wealth Management using Reinforcement Learning,” 2020\)
Das and Ross (“The Role of Options in Goals\-Based Wealth Management,” 2021\)
Das et al. (“Dynamic optimization for multi\-goals wealth management,” 2022\)
Dempster et al. (“Lifecycle Goal Achievement or Portfolio Volatility Reduction?” 2016\)
Dempster and Medova (“Asset Liability Management for Individual Households,” 2011\)
Dixon and Halperin (“Goal\-based wealth management with generative reinforcement learning,” 2021\)
Hao (“A Regime\-Aware Agent\-Based Framework for Financial Planning,” 2019\)
Irlam (“Machine learning for retirement planning,” 2020\)
Irlam (“Multi Scenario Financial Planning via Deep Reinforcement Learning AI,” 2020\)
Jaconetti et al. ( From assets to income: A goals\-based approach to retirement spending , 2020\)
Kim et al. (“Personalized goal\-based investing via multi\-stage stochastic goal programming,” 2020\)
Martellini et al. (“’Flexicure’ Retirement Solutions: A Part of the Answer to the Pension Crisis?” 2019\)
Mitra and Medova (“Asset and liability management/liability\-driven investment for pension funds,” 2010\)
Mladina and Grant (“Glide Paths Based on a Retirement Goal and Depleting Human Capital,” 2019\)
Mulvey and Hao (“Setting Realistic Goals for Personal Retirement Planning via Micro\-Macro Analyses,” 2020\)
Parker (“Portfolio Selection in a Goal\-Based Setting,” 2016\)
Parker (“Goal\-Based Portfolio Optimization,” 2016\)
Parker (“Multi\-Period Goals\-Based Portfolio Optimization,” 2021\)
Parker (“Achieving Goals While Making an Impact: Balancing Financial Goals with Impact Investing,” 2021\)
Parker (“Allocation of wealth both within and across goals: a practitioner guide,” 2020\)
Sornwanee (“Multi\-Regime, Goal\-Based Retirement Solutions: Sensitivity Analysis and Post\-Retirement Per\-
formance Comparison of Dynamic Strategies,” 2020\)
Wang et al. (“The Determinants of Stock Returns in the October 9, 2007 March 9, 2009 Bear Market,” 2011\)
Wu et al. (“Multi\-period optimal investment choice post\-retirement with inter\-temporal restrictions in a defined
contribution pension plan,” 2020\)
2\.2\.3 ESG\-based investing strategies for retirement
References:
Le Guenedal and Roncalli ( Portfolio Construction with Climate Risk Measures , 2022\)
Mitchell (“Migrating with Black Swans: Climate Risk and Retirement Planning,” 2016\)
Owadally et al. (“Long\-Term Sustainable Investment for Retirement,” 2021\)
2\.2\.4 Accumulation and decumulation
References:
Ackerley et al. ( To spend or not to spend? 2022\)
Arnold et al. (“Excel Calculators for Determining Retirement Accumulation and Disbursement Information,”
2017\)
Arnold et al. (“Using ”Equivalent Tax Rates” to Determine Tax\-Efficient Retirement Investment and With\-
drawal,” 2018\)
Arshanapalli and Nelson (“Asset Allocation Options for Wealth Accumulation,” 2012\)
Banerjee ( Asset Decumulation or Asset Preservation? What Guides Retirement Spending? 2019\)
Basu and Wiafe (“Impact of persistent bad returns and volatility on retirement outcomes,” 2017\)
Bengen (“The Planner’s Toolkit for Managing Retirement Withdrawal Plans,” 2021\)
Bernhardt and Donnelly ( Pension Decumulation Strategies: A State\-of\-the\-Art Report , 2018\)
10Blanchett and Cormier (“Right\-Sizing Retirement: Exploring the Retirement Consumption Gap in Early Re\-
tirement,” 2021\)
Bravo (“Addressing the Pension Decumulation Phase of Employee Retirement Planning,” 2020\)
Fichtner and Seligman (“Retirement Saving and Decumulation in a Persistent Low\-Return Environment,” 2018\)
Cassidy et al. (“Be Kind to Your Retirement Plan \- Give It a Benchmark,” 2013\)
Chen et al. (“Optimal Decumulation Strategies During Retirement with Deferred Annuities,” 2017\)
Chen et al. (“Personalised drawdown strategies and partial annuitisation to mitigate longevity risk,” 2021\)
Consigli et al. (“Retirement planning in individual asset liability management,” 2012\)
Dadashi (“Optimal investment–consumption problem: Post\-retirement with minimum guarantee,” 2020\)
Daher et al. ( From Accumulation to Decumulation – Why It Matters and What Plan Sponsors Should Know ,
2020\)
Dang et al. (“The 4 percent strategy revisited: a pre\-commitment mean\-variance optimal approach to wealth
management,” 2017\)
de Villiers and Roux (“Reframing the Retirement Saving Challenge: Getting to a Sustainable Lifestyle Level,”
2019\)
DiJoseph ( Spending guidelines to help ease retirees’ market worries , 2020\)
Donnelly and Bernhardt ( Pension decumulation strategies: a state\-of\-the\-art report , 2018\)
Dunham and Washer (“Using Life Tables for Retirement Planning,” 2020\)
Estrada (“Managing to target: dynamic adjustments for accumulation strategies,” 2019\)
Estrada (“Retirement Planning: From Z to A,” 2020\)
Estrada (“Target\-Date Funds, Glidepaths, and Risk Aversion,” 2020\)
Estrada and Kritzman (“Evaluating Retirement Strategies: A Utility\-Based Approach,” 2018\)
Finke and Blanchett (“An Overview of Retirement Income Strategies,” 2016\)
Forsyth et al. (“Management of Withdrawal Risk Through Optimal Life Cycle Asset Allocation,” 2018\)
Forsyth et al. (“Management of Portfolio Depletion Risk through Optimal Life Cycle Asset Allocation,” 2019\)
Forsyth et al. (“Optimal Asset Allocation for DC Pension Decumulation with a Variable Spending Rule,” 2020\)
Forsyth et al. (“Optimal control of the decumulation of a retirement portfolio with variable spending and dynamic
asset allocation,” 2021\)
Forsyth (“Two stage decumulation strategies for DC plan investors,” 2021\)
Forsyth (“Short term decumulation strategies for underspending retirees,” 2022\)
Forsyth (“A Stochastic Control Approach to Defined Contribution Plan Decumulation: ”The Nastiest, Hardest
Problem in Finance”,” 2022\)
Fraser and Payne (“Bond Tents: Reshaping the Equity Glide Slope at the End of Wealth Accumulation,” 2018\)
Fullmer (“A Framework for Portfolio Decumulation,” 2009\)
Fullmer (“Modern Portfolio Decumulation A New Strategy for Managing Retirement Income,” 2012\)
Geisler et al. (“A Comparison of the Tax Efficiency of Decumulation Strategies,” 2021\)
Goldman Sachs Asset Management Research ( Retirement Realities: Time For Change: Retirement Survey \&
Insights Report 2021 , 2021\)
Gupta (“Optimal investment and consumption strategy for a retiree under stochastic force of mortality,” 2020\)
Harbron et al. ( Withdrawal order: making the most of retirement assets , 2019\)
Hagelstein et al. (“Markowitz Portfolios with Graham Bands in the Accumulation Phase,” 2019\)
Hagelstein et al. (“Fixed and Dynamic Asset Allocation in the Accumulation Phase,” 2019\)
Horan (Tax\-Advantaged Savings Accounts and Tax\-Efficient Wealth Accumulation , 2005\)
Kieren and Weber (“When saving is not enough – wealth decumulation in retirement,” 2022\)
Kintzel (“Income Sustainability in Retirement: A Case Study of the Life\-Cycle Account,” 2020\)
Johnston et al. (“An empirical evaluation of dynamic vs static withdrawal strategies,” 2019\)
Latham ( Bridging the Gap Between Accumulation and Decumulation for Participants , 2021\)
Lewis (“Is There a Role for Commodities in Long\-Term Wealth Accumulation?” 2009\)
Li and Forsyth (“A data\-driven neural network approach to optimal asset allocation for target based defined
contribution pension plans,” 2019\)
Lobel et al. ( The replacement ratio: Making it personal , 2019\)
Love and Phelan (“Hyperbolic discounting and life\-cycle portfolio choice,” 2015\)
MacDonald et al. (“Drawing Down Retirement Savings \- Do Pensions, Taxes and Government Transfers Matter
Much for Optimal Decisions?” 2018\)
11MacLean and Zhao (“Asset Price Dynamics: Shocks and Regimes,” 2017\)
Maclean et al. (“Time to wealth goals in capital accumulation,” 2005\)
Martel and Sharon ( Financial Advisors and Retirement: The Decumulation Dilemma , 2019\)
Pakula (Guiding your clients through stormy weather: Sustainable withdrawal rates in times of crisis , 2020\)
Raskie (“Navigating Uncertainties in Accumulation and Decumulation of Retirement Portfolios,” 2017\)
Rook (“Multivariate Density Modeling for Retirement Finance,” 2017\)
Roux and de Villiers (“A simplified approach to estimate the sustainable lifestyle level for retirement planning,”
2020\)
Roy and Kim\-Steiner ( Three retirement spending surprises , 2019\)
Sestok (“Implementing Advice based on ”A Comparison of the Tax Efficiency of Decumulation Strategies”,”
2021\)
Sexauer et al. (“Making Retirement Income Last a Lifetime,” 2015\)
Sneddon et al. (“Modelling defined contribution retirement outcomes: A stochastic approach using Australia as
a case study,” 2016\)
Sun et al. (“Optimal Retirement Asset Decumulation Strategies: The Impact of Housing Wealth,” 2008\)
Tretiakova and Yamada (“Autonomous portfolio:a decumulation investment strategy that will get you there,”
2017\)
van Bilsen and Bovenberg (“The decumulation period of a personal pension with risk sharing: investment
approach versus consumption approach,” 2020\)
Wiafe (“Investment strategies in retirees’ decumulation phase,” 2015\)
Wiafe et al. (“Portfolio Strategies in Decumulation Phase: Does Lifecycling Fail?” 2014\)
Wiafe et al. (“Portfolio choice after retirement: Should self\-annuitisation strategies hold more equities?” 2020\)
Wolfe and Brazier ( Spending retirement assets ... or not? 2018\)
Wolfe and Ferraro ( Decumulation challenges and potential solutions – Helping build a pathway towards retirement
spending and income confidence , 2022\)
Xu et al. (“Shortfall risk and shortfall duration for portfolio choice in decumulation,” 2019\)
2\.2\.5 Taxation within context of retirement strategies
References:
Arnold et al. (“Using ”Equivalent Tax Rates” to Determine Tax\-Efficient Retirement Investment and With\-
drawal,” 2018\)
Chen and Munnell ( How Much Taxes Will Retirees Owe on Their Retirement Income? 2021\)
Das et al. (“Combining Investment and Tax Strategies for Optimizing Lifetime Solvency under Uncertain Returns
and Mortality,” 2020\)
Dickson et al. ( A ”BETR” approach to Roth conversions , 2018\)
DiLellio and Ostrov (“Constructing Tax Efficient Withdrawal Strategies for Retirees with Traditional 401(k)/IRAs,
Roth 401(k)/IRAs, and Taxable Accounts,” 2019\)
Geisler and Hulse (“The Taxation of Social Security Benefits and Planning Implications,” 2016\)
Geisler et al. (“A Comparison of the Tax Efficiency of Decumulation Strategies,” 2021\)
Goldberg et al. (“Tax\-Rate Arbitrage: Realization of Long\-Term Gains to Enable Short\-Term Loss Harvesting,”
2021\)
Hofmann (“Quantifying the Tax Benefit of Retirement Accounts for Better Client Decisions (Part 1\),” 2021\)
Hofmann (“Quantifying the Tax Benefit of Retirement Accounts for Better Client Decisions (Part 2\),” 2021\)
Horneff et al. (“How Persistent Low Expected Returns Alter Optimal Life Cycle Saving, Investment, and Re\-
tirement Behavior,” 2017\)
Horneff et al. (“Following the rules: Integrating asset allocation and annuitization in retirement portfolios,”
2008\)
Huang and Milevsky (“Longevity risk and retirement income tax efficiency: A location spending rate puzzle,”
2016\)
Kuselias et al. (“The Financial and Tax Considerations of Social Security and Early Retirement,” 2021\)
Lewis and Caliendo (“Tax\-Deferred Retirement Saving,” 2006\)
MacDonald et al. (“Drawing Down Retirement Savings \- Do Pensions, Taxes and Government Transfers Matter
Much for Optimal Decisions?” 2018\)
12Marekwica et al. (“Life cycle asset allocation in the presence of housing and tax\-deferred investing,” 2013\)
McQuarrie (“When and for Whom are Roth Conversions Most Beneficial? A New Set of Guidelines, Cautions
and Caveats,” 2022\)
Meyer and Reichenstein (“Adding Longevity through Tax\-Efficient Withdrawal Strategies,” 2013\)
Moehle et al. (“Tax\-Aware Portfolio Construction via Convex Optimization,” 2021\)
Reichenstein (“Note on Applying After\-Tax Asset Allocation,” 2007\)
Reichenstein (“After\-Tax Asset Allocation,” 2006\)
Reichenstein (“Saving in Roth Accounts and Making Roth Conversions before Retirement in Today’s Low Tax
Rates,” 2020\)
Reichenstein and Meyer (“Valuing Roth Conversion and Recharacterization Options,” 2017\)
Reichenstein and Meyer (“Understanding the Tax Torpedo and Its Implications for Various Retirees,” 2018\)
Reichenstein and Meyer (“Medicare and Tax Planning for Higher\-Income Households,” 2019\)
Reichenstein and Meyer (“Investment implications of the rising and falling pattern of marginal tax rates for
retirees,” 2020\)
Reichenstein and Meyer (“How Social Security Coordination Can Add Value to a Tax\-Efficient Withdrawal
Strategy,” 2021\)
Rundle (“A Social Security Purchase: Is Delaying Social Security More Effective than Purchasing a Deferred
Income Annuity?” 2018\)
Sestok (“Implementing Advice based on ”A Comparison of the Tax Efficiency of Decumulation Strategies”,”
2021\)
Sneddon et al. (“Optimal Asset Liability Management for Post\-retirement stage with Income Protection Prod\-
uct,” 2015\)
Shoven and Sialm (“Asset location in tax\-deferred and conventional savings accounts,” 2004\)
Sosner et al. (“Integration of Income and Estate Tax Planning,” 2021\)
Turvey et al. (“Embedded Tax Liabilities and Portfolio Choice,” 2013\)
Xu (“Static and Dynamic Tax Diversification of Withdrawals from Multiple Individual Retirement Accounts,”
2018\)
Young (Tax\-Efficient Withdrawal Strategies , 2020\)
Young (“The Roth/Pretax Decision in Late Career Years: The Increasing Importance of Accumulated Assets in
Light of the SECURE Act,” 2020\)
2\.2\.6 Inflation within context of retirement
References:
Breach et al. (“The term structure and inflation uncertainty,” 2020\)
Canarella et al. (“Modeling US historical time\-series prices and inflation using alternative long\-memory ap\-
proaches,” 2020\)
Capolongo and Pacella (“Forecasting inflation in the euro area: countries matter!” 2021\)
Dai and Medhat (“US Inflation and Global Asset Returns,” 2021\)
de Mendonça et al. (“Rationality and anchoring of inflation expectations: An assessment from survey\-based and
market\-based measures,” 2021\)
Fulton and Hubrich (“Forecasting US Inflation in Real Time,” 2021\)
Goldstein (“The glide path less traveled: A critical examination of assumptions, outcomes, and glide path
specification,” 2018\)
Konicz et al. (“Optimal annuity portfolio under inflation risk,” 2015\)
Han and Hung (“Optimal asset allocation for DC pension plans under inflation,” 2012\)
Hanna and Kim (“Treatment of Inflation in Retirement Planning Calculations: An Improved Method,” 2017\)
Kohlscheen (“What does machine learning say about the drivers of inflation?” 2021\)
Laster et al. (“Pitfalls in Retirement,” 2014\)
Laster et al. (“Strategies for Managing Retirement Risks,” 2016\)
Medeiros et al. (“Forecasting Inflation in a Data\-Rich Environment: The Benefits of Machine Learning Methods,”
2021\)
Merton and Muralidhar (“Selfies: A new pension bond and currency for retirement,” 2020\)
13Muralidhar et al. (“The Most Basic Missing Instrument in Financial Markets: The Case for Forward Starting
Bonds,” 2016\)
Neville et al. (“The Best Strategies for Inflationary Times,” 2021\)
Pfau (“Making Sense Out of Variable Spending Strategies for Retirees,” 2015\)
Podkaminer et al. (“Protecting Portfolios Against Inflation,” 2022\)
Pruser (“Forecasting US inflation using Markov dimension switching,” 2021\)
Rosenthal (“Joint effect of random years of longevity and mean reversion in equity returns on the safe withdrawal
rate in retirement,” 2018\)
Rundle (“A Social Security Purchase: Is Delaying Social Security More Effective than Purchasing a Deferred
Income Annuity?” 2018\)
Sapra and Pedersen (“The Role of Long\-Maturity TIPS in Retirement Portfolios,” 2017\)
Šestanović and Arnerić (“Neural network structure identification in inflation forecasting,” 2021\)
Shang and Haberman (“Forecasting age distribution of death counts: an application to annuity pricing,” 2020\)
Sneddon et al. (“Optimal Asset Liability Management for Post\-retirement stage with Income Protection Prod\-
uct,” 2015\)
Tharp and Kitces (“Life\-Cycle Earnings Curves and Safe Savings Rates,” 2018\)
Williams (“Inflation Expectations in the U.S.: Linking Markets, Households, and Businesses,” 2021\)
2\.2\.7 Longevity and mortality within context of retirement strategies
References:
Assabil and Mcleish (“Assessing the Impact of Longevity Risk for Countries with Limited Data,” 2021\)
Azman and Pathmanathan (“The GLM framework of the Lee\-Carter model: a multi\-country study,” 2022\)
Bell et al. (“How do subjective life expectancies compare with mortality tables? Similarities and differences in
three national samples,” 2020\)
Blake and Cairns (“Longevity risk and capital markets: the 2018\-19 update,” 2020\)
Blanchett (“Minding the Gap in Subjective Mortality Estimates,” 2021\)
Boon et al. (“Systematic longevity risk: to bear or to insure?” 2020\)
Cairns et al. (“A Two\-Factor Model for Stochastic Mortality with Parameter Uncertainty: Theory and Calibra\-
tion,” 2020\)
Chen et al. (“Optimal retirement products under subjective mortality beliefs,” 2021\)
Chen et al. (“Personalised drawdown strategies and partial annuitisation to mitigate longevity risk,” 2021\)
Chen et al. (“Tail index\-linked annuity: A longevity risk sharing retirement plan,” 2022\)
Coppola et al. (“On the management of retirement age indexed to life expectancy: a scenario analysis of the
Italian longevity experience,” 2020\)
Das et al. (“Combining Investment and Tax Strategies for Optimizing Lifetime Solvency under Uncertain Returns
and Mortality,” 2020\)
Dehm (“Stochastic mortality : modelling and optimal investment,” 2020\)
Dunham and Washer (“Using Life Tables for Retirement Planning,” 2020\)
Finke and Blanchett (“An Overview of Retirement Income Strategies,” 2016\)
Frank et al. (“An Age\-Based, Three\-Dimensional Distribution Model Incorporating Sequence and Longevity
Risks,” 2012\)
Gemmo et al. (“Optimal portfolio choice with tontines under systematic longevity risk,” 2020\)
Horneff et al. (“Putting the Pension Back in 401(k) Retirement Plans: Optimal versus Default Longevity Income
Annuities,” 2018\)
Hosseini et al. (“The evolution of health over the life cycle,” 2022\)
Huang and Milevsky (“Longevity risk and retirement income tax efficiency: A location spending rate puzzle,”
2016\)
Huaxiong et al. (“Retirement Spending and Biological Age,” 2017\)
Laster et al. (“Pitfalls in Retirement,” 2014\)
Laster et al. (“Strategies for Managing Retirement Risks,” 2016\)
Li and Hyndman (“Assessing mortality inequality in the U.S.: What can be said about the future?” 2021\)
Li and Shi (“Mortality Forecasting with an Age\-Coherent Sparse VAR Model,” 2021\)
Meyer and Reichenstein (“Adding Longevity through Tax\-Efficient Withdrawal Strategies,” 2013\)
14Milevsky (“Swimming with Wealthy Sharks: Longevity, Volatility and the Value of Risk Pooling,” 2018\)
Milevsky (“Modeling Human Longevity and Life Tables,” 2020\)
Milevsky (“Biological (and Other) Ages,” 2020\)
Milevsky (“Calibrating Gompertz in reverse: What is your longevity\-risk\-adjusted global age?” 2020\)
Milevsky et al. (“The implied longevity curve: How long does the market think you are going to live?” 2018\)
Pfau et al. (“A Portfolio Approach to Retirement Income Security,” 2016\)
Quinn and Cahill (“Challenges and Opportunities of Living and Working Longer,” 2018\)
Rabitti and Borgonovo (“Is mortality or interest rate the most important risk in annuity models? A comparison
of sensitivity analysis methods,” 2020\)
Rosenthal (“Joint effect of random years of longevity and mean reversion in equity returns on the safe withdrawal
rate in retirement,” 2018\)
Shi (“Forecasting Mortality Rates with the Adaptive Spatial Temporal Autoregressive Model,” 2021\)
Simsek et al. (“Optimal Longevity Risk Management in the Retirement Stage of the Life Cycle,” 2018\)
Tsai and Cheng (“Incorporating statistical clustering methods into mortality models to improve forecasting
performances,” 2021\)
Wiafe (“Investment strategies in retirees’ decumulation phase,” 2015\)
Xu and Hoesch (“Predicting longevity: an analysis of potential alternatives to life expectancy reports,” 2018\)
Yang (“Longevity and statistical modelling,” 2017\)
2\.2\.8 Incorporating costs of health care and long\-term care
References:
Abeliansky and Strulik (“Health and Aging Before and after Retirement,” 2021\)
Anantharaman and Henderson (“Understanding Pension Liabilities: A Closer Examination of Discount Rates,”
2016\)
Bailey et al. ( Planning for health care costs in retirement , 2021\)
Blanchett (“Health shocks and subsequent retiree spending,” 2018\)
Cheng et al. (“Life Quality and Health Costs in Late Retirement,” 2017\)
Correia et al. (“Avoiding the Medicaid Trap: A Step\-by\-Step Guide to Estate Planning,” 2017\)
Crook and Baredes (“Total Wealth Allocation: Liquidity, Longevity, and Legacy,” 2015\)
Crook and Sutedja (“Will Long\-Term Care Ruin Retirement Plans?” 2017\)
De La Pena et al. (“Cost\-Free LTC Model Incorporated into Private Pension Schemes,” 2021\)
Drew et al. (“Withdrawal Capacity in the Face of Expected and Unexpected Health and Aged\-Care Expenses
During Retirement,” 2016\)
Du (“Essays on Portfolio Choice and Health over the Life Cycle,” 2021\)
Finefrock et al. (“Long\-Term Care Insurance: Comparisons for Determining the Best Options for Clients,” 2015\)
Fonseca et al. (“Accounting for the Rise of Health Spending and Longevity,” 2021\)
French and Jones (“Health, Health Insurance, and Retirement: A Survey,” 2017\)
Fuino and Wagner (“Long\-term care models and dependence probability tables by acuity level: New empirical
evidence from Switzerland,” 2018\)
Ghilarducci et al. (“New evidence on the effect of economic shocks on retirement plan withdrawals,” 2019\)
Gao and Sun (“Modeling retirees’ investment behaviors in the presence of health expenditure risk and financial
crisis risk,” 2021\)
Halen et al. (“Understanding the True Cost of Health Care in Retirement,” 2020\)
Hosseini et al. (“The evolution of health over the life cycle,” 2022\)
Hugonnier et al. (“Closing down the shop: optimal health and wealth dynamics near the end of life,” 2017\)
Jung (Estimating Markov Transition Probabilities Between Health States Using U.S. Longitudinal Survey Data ,
2020\)
Jung (“Estimating Markov Transition Probabilities Between Health States Using U.S. Longitudinal Survey
Data,” 2021\)
Kahler et al. ( HSAs: An off\-label prescription for retirement saving , 2020\)
Laster et al. (“Strategies for Managing Retirement Risks,” 2016\)
Milevsky (“Swimming with Wealthy Sharks: Longevity, Volatility and the Value of Risk Pooling,” 2018\)
Peijnenburg et al. (“Health Cost Risk: A Potential Solution To the Annuity Puzzle,” 2017\)
15Reichenstein and Meyer (“Medicare and Tax Planning for Higher\-Income Households,” 2019\)
Tomlinson (“New Estimates of the Need for Long\-Term Care,” 2020\)
Van Harlow and Brown (“Health State and the Savings Required for a Sustainable Retirement,” 2017\)
Wu (“Assessing the relationship between health and household portfolio allocation,” 2021\)
2\.2\.9 Financial advice and planning for retirement
References:
Bengen (“The Planner’s Toolkit for Managing Retirement Withdrawal Plans,” 2021\)
Bianchi and Briere (“Robo\-Advising for Small Investors,” 2021\)
Bianchi and Briere (“Robo\-Advising: Less AI and More XAI?,” 2021\)
Blanchett (“Do Advisors Improve 401(k) Plans?” 2021\)
Bogan et al. (“Financial planning: A research agenda for the next decade,” 2020\)
Brauer (“Nudged into Better Portfolios and Lower Risk: Robo\-Advice and Savings Decisions,” 2021\)
Bravo (“Addressing the Pension Decumulation Phase of Employee Retirement Planning,” 2020\)
Changwony et al. (“Savings goals and wealth allocation in household financial portfolios,” 2021\)
Chalmers and Reuter (“Is conflicted investment advice better than no advice?” 2020\)
Chang et al. (“A Framework for Assessing Individual Retirement Planning Investment Policy Performance,”
2010\)
Consigli et al. (“Retirement planning in individual asset liability management,” 2012\)
D’Acunto and Rossi (“New Frontiers of Robo\-Advising: Consumption, Saving, Debt Management, and Taxes,”
2021\)
Dunham and Washer (“Using Life Tables for Retirement Planning,” 2020\)
Elnekave (“The mathematics of savings and retirement planning,” 2007\)
Envestnet Research ( Capital Sigma: The Advisor Advantage , 2020\)
Estrada (“Retirement Planning: From Z to A,” 2020\)
Fidelity Research ( Why work with a financial advisor , 2019\)
Frank et al. (“An Age\-Based, Three\-Dimensional Distribution Model Incorporating Sequence and Longevity
Risks,” 2012\)
Friedenthal, “The Third Generation of Financial Planning,” 2020
Grealish and Kolm (“Robo\-Advisors Today and Tomorrow: Investment Advice Is Just an App Away,” 2021\)
Hao (“A Regime\-Aware Agent\-Based Framework for Financial Planning,” 2019\)
Harbron et al. ( Withdrawal order: making the most of retirement assets , 2019\)
Hicks (How Much Is An Adviser Worth? 2019\)
Irlam (“Machine learning for retirement planning,” 2020\)
Jung (Your advisor...worth more than 1%? 2017\)
Kinniry Jr. et al. ( Putting a value on your value: quantifying Vanguard Advisor’s Alpha , 2016\)
Kitces and Richards ( Kitces \& Carl Ep 01: How To Value The Value Of Financial Planning , 2019\)
Konicz et al. (“Optimal retirement planning with a focus on single and joint life annuities,” 2016\)
Levine (“No Investment Fee Is Small, Long Term,” 2021\)
Linnainmaa et al. (“The Misguided Beliefs of Financial Advisors,” 2021\)
Martel and Sharon ( Financial Advisors and Retirement: The Decumulation Dilemma , 2019\)
Mislinski (“How to Illustrate Planning Risks to Clients,” 2021\)
Mulvey and Hao (“Setting Realistic Goals for Personal Retirement Planning via Micro\-Macro Analyses,” 2020\)
Munnell et al. (“Are Early Claimers Making a Mistake?” 2016\)
Murguia and Pfau (“Retirement Income Beliefs and Financial Advice Seeking Behaviors,” 2021\)
Murphy et al. (“Identifying What Investors Value in a Financial Adviser: Uncovering Opportunities and Pitfalls,”
2020\)
Pfau (“An Overview of Retirement Income Planning,” 2018\)
Pittman (“Use Your Client’s Funded Ratio to Simplify and Improve Retirement Planning Decisions,” 2015\)
Reichenstein and Meyer (“Medicare and Tax Planning for Higher\-Income Households,” 2019\)
Rossi and Utkus (“The Needs and Wants in Financial Advice: Human versus Robo\-advising,” 2021\)
Roux and de Villiers (“A simplified approach to estimate the sustainable lifestyle level for retirement planning,”
2020\)
16Salampasis et al. (“Wealth Management in Times of Robo: Towards Hybrid Human\-Machine Interactions,”
2019\)
Scherer and Lehner (“What Drives Robo\-Advice?” 2021\)
Sun (“Dynamic Retirement Financial Planning Model,” 2019\)
Thompson et al. (“Measuring Financial Advice: Aligning Client Elicited and Revealed Risk,” 2021\)
Van Harlow et al. (“The Use and Value of Financial Advice for Retirement Planning,” 2020\)
Xu and Anichini (“Mean\-Variance Analysis in Post\-Retirement Planning,” 2016\)
Zhang (“Optimal Retirement Planning: Scenario Generation, Preferences, and Objectives,” 2018\)
2\.2\.10 Annuities
References:
Alexandrova and Gatzert (“What Do We Know About Annuitization Decisions?” 2019\)
Blanchett and Finke (“Should Annuities be Purchased from Tax\-Sheltered Assets?” 2019\)
Blanchett (“The value of allocating to annuities,” 2020\)
Blanchett (“The Benefit of Diversified Guaranteed Income for Retirees: Combining Immediate Fixed and Vari\-
able Annuities,” 2020\)
Bravo (“Funding for longer lives. Retirement wallet and risk\-sharing annuities,” 2019\)
Clark et al. (“Annuity options in public pension plans: the curious case of social security leveling,” 2018\)
Chen et al. (“Optimal Decumulation Strategies During Retirement with Deferred Annuities,” 2017\)
Chen et al. (“Combining Flexible Asset Allocation, Sustainable Withdrawals, and Deferred Annuities to provide
an Adaptive Lifelong Investing Solution,” 2021\)
Chen et al. (“Valuation of long\-term care options embedded in life annuities,” 2022\)
Chen et al. (“On the Optimal Combination of Annuities and Tontines,” 2019\)
Chen et al. (“The implication of the hyperbolic discount model for the annuitisation decisions,” 2020\)
Chen et al. (“Personalised drawdown strategies and partial annuitisation to mitigate longevity risk,” 2021\)
Chiu et al. (“Valuation and analysis on complex equity indexed annuities,” 2019\)
Deelstra et al. (“Optimal annuitisation in a deterministic financial environment,” 2021\)
Dillschneider et al. (“Dynamic Portfolio Choice with Annuities When the Interest Rate Is Stochastic,” 2020\)
Dong et al. (“Efficient willow tree method for variable annuities valuation and risk management,” 2020\)
Feng and Jing (“Analytical valuation and hedging of variable annuity guaranteed lifetime withdrawal benefits,”
2017\)
Finke and Pfau (“Reduce Retirement Costs with Deferred Income Annuities Purchased before Retirement,”
2015\)
Gan (“Application of data clustering and machine learning in variable annuity valuation,” 2013\)
Gudkov et al. (“Pricing of guaranteed minimum withdrawal benefits in variable annuities under stochastic
volatility, stochastic interest rates and stochastic mortality via the componentwise splitting method,” 2019\)
Habib et al. (“Optimal allocation to deferred income annuities,” 2018\)
Hejazi et al. (“A Spatial Interpolation Framework for Efficient Valuation of Large Portfolios of Variable Annu\-
ities,” 2017\)
Hu (“A Comprehensive Study of Guaranteed Minimum Maturity Benefit and Guaranteed Minimum Death
Benefit under Regime\-switching Models,” 2021\)
Iskhakov et al. (“Optimal Annuity Purchases for Australian Retirees,” 2015\)
Jang et al. (“Glide paths for a retirement plan with deferred annuities,” 2022\)
Kelly and Roy ( Annuities: An essential slice of the retirement pie , 2021\)
Kieren and Weber (“When saving is not enough – wealth decumulation in retirement,” 2022\)
Koijen et al. (“Optimal Annuity Risk Management,” 2011\)
Konicz et al. (“Optimal retirement planning with a focus on single and joint life annuities,” 2016\)
Mahayni and Schneider (“Variable annuities and the option to seek risk: Why should you diversify?” 2012\)
Markwat et al. (“Purchasing an Annuity: Now or Later? The Role of Interest Rates,” 2016\)
Mendu (“A critical review of ’optimal’ annuitization strategies,” 2021\)
Milevsky (“Life Annuities: From Immediate to Deferred,” 2020\)
Milevsky et al. (“A Glide Path for Target Date Fund Annuitization,” 2015\)
Millossovich et al. (“Variable Annuities: A Unifying Valuation Approach,” 2011\)
17Milevsky ( Calculus of Retirement Income: Financial Models for Pension Annuities and Life Insurance , 2006\)
Moenig (“It’s RILA Time: An Introduction to Registered Index\-Linked Annuities,” 2021\)
Munnell et al. (“How Best to Annuitize Defined Contribution Assets?” 2019\)
Ngai and Sherris (“Longevity risk management for life and variable annuities: The effectiveness of static hedging
using longevity bonds and derivatives,” 2011\)
Novotny and Mansson (“Finding the Optimal Withdrawal Rate on a Retirement Portfolio,” 2020\)
Owadally et al. (“Optimal investment for a retirement plan with deferred annuities,” 2021\)
Peijnenburg et al. (“Health Cost Risk: A Potential Solution To the Annuity Puzzle,” 2017\)
Prendergast (“Replicating Maximum\-Yield Annuities with US Treasury Funds,” 2021\)
Rabitti and Borgonovo (“Is mortality or interest rate the most important risk in annuity models? A comparison
of sensitivity analysis methods,” 2020\)
Rogalla (“Optimal Portfolio Choice in Retirement With Participating Life Annuities,” 2021\)
Rundle (“A Social Security Purchase: Is Delaying Social Security More Effective than Purchasing a Deferred
Income Annuity?” 2018\)
Shang and Haberman (“Forecasting age distribution of death counts: an application to annuity pricing,” 2020\)
Steinorth and Mitchell (“Valuing variable annuities with guaranteed minimum lifetime withdrawal benefits,”
2015\)
Sutcliffe (“Trading death: The implications of annuity replication for the annuity puzzle, arbitrage, speculation
and portfolios,” 2015\)
van Bilsen and Linders (“Affordable and adequate annuities with stable payouts: Fantasy or reality?” 2019\)
Vrdoljak et al. (“The Role of Variable Annuities in Addressing Retirement Risks,” 2014\)
2\.2\.11 Sustainable withdrawals and spending in retirement
References:
Bengen (“The Planner’s Toolkit for Managing Retirement Withdrawal Plans,” 2021\)
Beracha et al. (“The 4% rule: Does real estate make a difference?” 2017\)
Blanchett (“Addressing Key Retirement Risks,” 2014\)
Blanchett (“The Impact of Guaranteed Income and Dynamic Withdrawals on Safe Initial Withdrawal Rates,”
2017\)
Blanchett et al. (“Low Bond Yields and Safe Portfolio Withdrawal Rates,” 2013\)
Blanchett et al. (“Low Returns and Optimal Retirement Savings,” 2018\)
Campbell and Sigalov (“Portfolio choice with sustainable spending: A model of reaching for yield,” 2022\)
Chen et al. (“Combining Flexible Asset Allocation, Sustainable Withdrawals, and Deferred Annuities to provide
an Adaptive Lifelong Investing Solution,” 2021\)
Clare et al. (“Absolute Momentum, Sustainable Withdrawal Rates and Glidepath Investing in US Retirement
Portfolios from 1925,” 2019\)
Clare et al. (“Perfect Withdrawal in a Noisy World: Investing Lessons with and without Annuities while in
Drawdown between 2000 and 2019,” 2021\)
Clare et al. (“Can sustainable withdrawal rates be enhanced by trend following?” 2021\)
Costa et al. ( Fuel for the F.I.R.E.: Updating the 4% rule for early retirees , 2021\)
Dang et al. (“The 4 percent strategy revisited: a pre\-commitment mean\-variance optimal approach to wealth
management,” 2017\)
Delong and Chen (“Asset allocation, sustainable withdrawal, longevity risk and non\-exponential discounting,”
2016\)
de Villiers and Roux (“Reframing the Retirement Saving Challenge: Getting to a Sustainable Lifestyle Level,”
2019\)
DiJoseph ( Spending guidelines to help ease retirees’ market worries , 2020\)
Dreyer and Pogorelova (“The Effect of Income\-Dependent Mortality on Withdrawal Strategies,” 2018\)
Dziwisch et al. (“Empirical determination of sustainable withdrawal rates considering historical yields and
inflation rates in Germany,” 2021\)
Estrada (“Refining the Failure Rate,” 2017\)
Estrada (“Replacing the Failure Rate: A Downside Risk Perspective,” 2017\)
Estrada (“From Failure to Success: Replacing the Failure Rate,” 2018\)
18Estrada (“Maximum Withdrawal Rates: A Novel and Useful Tool,” 2017\)
Estrada (“Maximum withdrawal rates: an empirical and global perspective,” 2018\)
Estrada (“The Sustainability of (Global) Withdrawal Strategies,” 2021\)
Finke (Bill Sharpe Seeks a Better Retirement Income Solution , 2019\)
Forsyth (“Short term decumulation strategies for underspending retirees,” 2022\)
Fox (“Linking metrics to objectives: retirement saving, spending, and active management,” 2020\)
Habib et al. (“Approximate solutions to retirement spending problems and the optimality of ruin,” 2017\)
Harbron et al. ( Withdrawal order: making the most of retirement assets , 2019\)
Horneff et al. (“Do Required Minimum Distribution 401(K) Rules Matter, and for Whom? Insights from a
Lifecycle Model,” 2021\)
Johnston et al. (“An empirical evaluation of dynamic vs static withdrawal strategies,” 2019\)
Kintzel (“Income Sustainability in Retirement: A Case Study of the Life\-Cycle Account,” 2020\)
Larson (“Strategy: Assessing the Impact of Required Minimum Distributions on the 4 Percent Rule,” 2018\)
Larson (“Required Minimum Distributions as a Retirement Strategy: The Tradeoff Between RMD Volatility
and the Expected Number of Dollars Paid Out,” 2022\)
Lobel et al. ( The replacement ratio: Making it personal , 2019\)
Lozada ( Financing Retirement using U.S. Treasury Bonds: Safe Withdrawal Rates, Mean/Standard\-Deviation
Frontiers,and Endpoint\-Dependence of the Safest Maturity , 2018\)
Lozada ( Fixed income for retirement saving: TIAA traditional lessons on quality, duration, risk, and gradual
withdrawals , 2018\)
Laster et al. (“Strategies for Managing Retirement Risks,” 2016\)
Laster et al. (“Systematic Withdrawal Strategies for Retirees,” 2012\)
Lozada ( Financing Retirement using U.S. Treasury Bonds: Safe Withdrawal Rates, Mean/Standard\-Deviation
Frontiers,and Endpoint\-Dependence of the Safest Maturity , 2018\)
MacDonald et al. (“Research and Reality: A Literature Review on Drawing Down Retirement Financial Savings,”
2013\)
Martin and Kintzel (“A Comparison of Free Online Tools for Individuals Deciding When to Claim Social Security
Benefits,” 2016\)
Milevsky (“Intelligent Drawdown Rates,” 2020\)
Miller (“Improving Withdrawal Rates in a Low Yield World,” 2015\) Mitchell (“A Mean\-Variance Approach to
Withdrawal Rate Management: Theory and Simulation,” 2009\)
Mitchell and Felton (“Same\-Sex Couples and Sustainable Retirement Withdrawal Rates,” 2015\)
Novotny and Mansson (“Finding the Optimal Withdrawal Rate on a Retirement Portfolio,” 2020\)
Pakula (Guiding your clients through stormy weather: Sustainable withdrawal rates in times of crisis , 2020\)
Pepperell et al. (“Death or Bust? The Risk with Post\-Retirement Income Models,” 2020\)
Pfau (“How to Link Retirement Strategies to Sustainable\-Spending Rates,” 2015\)
Pfau and Dokken (“Rethinking Retirement: Sustainable Withdrawal Rates for New Retirees in 2015,” 2015\)
Larson (“Required Minimum Distributions as a Retirement Strategy: The Tradeoff Between RMD Volatility
and the Expected Number of Dollars Paid Out,” 2022\)
Rietz et al. (“Analyzing Retirement Withdrawal Strategies,” 2018\)
Rook (“Minimizing the Probability of Ruin in Retirement,” 2015\)
Rosenthal (“Joint effect of random years of longevity and mean reversion in equity returns on the safe withdrawal
rate in retirement,” 2018\)
Roux and de Villiers (“A simplified approach to estimate the sustainable lifestyle level for retirement planning,”
2020\)
Sato (“Optimal Withdrawal Rate Under Longevity Risks: A Criterion for Life Planning after Retirement,” 2016\)
Scruggs (“Asset Allocation and Withdrawal Strategies: Three Levers for Managing Retirement Outcomes,”
2019\)
Suarez (“The perfect withdrawal amount over the historical record,” 2020\)
Suarez et al. (“The Perfect Withdrawal Amount: A Methodology for Creating Retirement Account Distribution
Strategies,” 2015\)
Tergersen (“Forget the 4% Rule: Rethinking Common Retirement Beliefs,” 2018\)
Vanguard Research ( Dynamic spending: A better way to budget in retirement , 2020\)
Van Harlow ( Optimal Asset Allocation in Retirement: A Downside Risk Perspective , 2014\)
19Van Harlow and Brown (“Improving the Outlook for a Successful Retirement: A Case for Using Downside
Hedging,” 2016\)
Van Harlow and Brown (“Market Risk, Mortality Risk, And Sustainable Retirement Asset Allocation: A Down\-
side Risk Perspective,” 2016\)
Vaughan (“RMD Arbitrage: Strategies for Legally Delaying and Reducing RMDs,” 2017\)
Warshawsky (“Reforming Retirement Income: Annuitization, Combination Strategies, and Required Minimum
Distributions,” 2018\)
Woerheide and Nanigian (“Sustainable Withdrawal Rates from Retirement Portfolios: The Historical Evidence
on Buffer Zone Strategies,” 2011\)
2\.2\.12 Retirement income
References:
Biggs (“The life cycle model, replacement rates, and retirement income adequacy,” 2017\)
Blanchett and Finke (“Guaranteed Income: A License to Spend,” 2021\)
Collins et al. (“How Risky is Your Retirement Income Risk Model?” 2015\)
Collins (“Annuities and retirement income planning,” 2016\)
DeLibero and Pfau (“Life Insurance as a Retirement Income Tool,” 2017\)
Fan et al. (“Optimizing retirement income: an adaptive approach based on assets and liabilities,” 2013\)
Finke and Blanchett (“An Overview of Retirement Income Strategies,” 2016\)
Finke (Bill Sharpe Seeks a Better Retirement Income Solution , 2019\)
Goodman and Richardson (“Achieving Retirement Income Security: A Comparison of Guaranteed Lifetime
Withdrawal Benefit, Systematic Withdrawal and Partial Variable Annuity Strategies,” 2019\)
Grennon (“A Dynamic Approach to Retirement Income,” 2016\)
Harbron et al. ( Withdrawal order: making the most of retirement assets , 2019\)
Hopkins et al. (“Ethical issues in retirement income planning: an advisor perspective,” 2016\)
Horneff et al. (“How Persistent Low Expected Returns Alter Optimal Life Cycle Saving, Investment, and Re\-
tirement Behavior,” 2018\)
Huang and Milevsky (“Longevity risk and retirement income tax efficiency: A location spending rate puzzle,”
2016\)
Irlam and Tomlinson (“Retirement Income Research: What Can We Learn from Economics?” 2014\)
Israelsen (“Retirement Portfolio Realities: The Mathematics of Survival,” 2017\)
Jaconetti et al. ( From assets to income: A goals\-based approach to retirement spending , 2020\)
Kintzel (“Income Sustainability in Retirement: A Case Study of the Life\-Cycle Account,” 2020\)
Lozada ( Fixed income for retirement saving: TIAA traditional lessons on quality, duration, risk, and gradual
withdrawals , 2018\)
Martellini et al. (“Securing Replacement Income with Goal\-Based Retirement Investing Strategies,” 2020\)
Kaplan (“Asset Allocation with Annuities for Retirement Income Management,” 2006\)
Kintzel (“Income Sustainability in Retirement: A Case Study of the Life\-Cycle Account,” 2020\)
Koo et al. (“Novel Utility\-Based Life Cycle Models to Optimize Income in Retirement in the Presence of Het\-
erogeneous Preferences,” 2020\)
Malhotra (“A Framework for Finding an Appropriate Retirement Income Strategy,” 2012\)
Mantilla\-Garcia et al. (“From Defined\-Contribution Towards Target\-Income Retirement Systems,” 2020\)
Martel and Sharon ( An Untimely Retirement: The Dangers of ’Sequence Risk’ for Retirees – Introducing ”Income
to Outcome” retirement framework , 2019\)
Marwood and Minnen (“Safely Boosting Retirement Income by Harmonizing Drawdown Paths,” 2020\)
Milevsky ( Calculus of Retirement Income: Financial Models for Pension Annuities and Life Insurance , 2006\)
Milevsky ( Retirement Income Recipes in R: From Ruin Probabilities to Intelligent Drawdowns , 2020\)
Murguia and Pfau (“A Model Approach to Selecting a Personalized Retirement Income Strategy,” 2021\)
Pepperell et al. (“Death or Bust? The Risk with Post\-Retirement Income Models,” 2020\)
Pfau (“Choosing a Retirement Income Strategy: A New Evaluation Framework,” 2015\)
Pfau et al. ( Optimizing Retirement Income Solutions in Defined Contribution Retirement Plans: A Framework
for Building Retirement Income Portfolios , 2016\)
20Pfau et al. ( Optimizing Retirement Income by Integrating Retirement Plans, IRAs, and Home Equity: A Frame\-
work for Evaluating Retirement Income Decisions , 2017\)
Pfau (“An Overview of Retirement Income Planning,” 2018\)
Pfau (“The four approaches to managing retirement income risk,” 2019\)
Pittman (“Is a Portfolio Built to Produce Yield a Sensible Retirement Income Portfolio?” 2014\)
Sexauer et al. (“Making Retirement Income Last a Lifetime,” 2015\)
Sharpe ( Retirement Income Analysis with scenario matrices , 2019\)
Wallick et al. (“Getting More from Less in Defined Benefit Plans,” 2018\)
Warshawsky (“Reforming Retirement Income: Annuitization, Combination Strategies, and Required Minimum
Distributions,” 2018\)
2\.2\.13 Sequence of returns
References:
Clare et al. (“Reducing Sequence Risk Using Trend Following and the CAPE Ratio,” 2017\)
Clare et al. (“Absolute Momentum, Sustainable Withdrawal Rates and Glidepath Investing in US Retirement
Portfolios from 1925,” 2019\)
Clare et al. (“Measuring sequence of returns risk,” 2020\)
Collins and Stampfli (“Sequence of Returns Risk Reconsidered,” 2019\)
DeJong and Robinson (“A Case Study in Sequence Risk: A 20\-Year Retrospective on the Impact of the 2000\-2002
and 2007\-2009 Bear Markets on Retirement Nest Egg Sustainability,” 2022\)
Drew et al. (“Conditional Allocations to Real Estate: An Antidote to Sequencing Risk in Defined Contribution
Retirement Plans,” 2015\)
Estrada (“Sequence Risk: Is It Really a Big Deal?” 2020\)
Frank et al. (“An Age\-Based, Three\-Dimensional Distribution Model Incorporating Sequence and Longevity
Risks,” 2012\)
Ge (“Utilizing Low\-Volatility Assets To Mitigate Sequence Risk In Retirement Investing,” 2019\)
Kenigsberg et al. (“Return Sequence and Volatility: Their Impact on Sustainable Withdrawal Rates,” 2014\)
Kitces (“Sequence of return risk and safe withdrawal rates,” 2015\)
Laster et al. (“Strategies for Managing Retirement Risks,” 2016\)
Martel and Sharon ( An Untimely Retirement: The Dangers of ’Sequence Risk’ for Retirees – Introducing ”Income
to Outcome” retirement framework , 2019\)
Milevsky and Posner (“Can collars reduce retirement sequencing risk? analysis of portfolio longevity extension
overlays (leo),” 2014\)
Milevsky (“Modeling the Risk of Sequence\-of\-Returns,” 2020\)
Tretiakova and Yamada (“Autonomous portfolio:a decumulation investment strategy that will get you there,”
2017\)
Vrdoljak et al. (“The Role of Variable Annuities in Addressing Retirement Risks,” 2014\)
2\.2\.14 Incorporating Social Security
References:
Alderson and Betker (“Does the Benefit of Deferring Social Security Offset the Opportunity Cost to Do So?”
2017\)
Ali et al. (“Social Security Benefit Valuation, Risk, and Optimal Retirement,” 2019\)
Alleva (“Minimizing the Risk of Opportunity Loss in the Social Security Claiming Decision,” 2015\)
Alleva (“Discount Rate Specification and the Social Security Claiming Decision,” 2016\)
Alleva (“Social Security Retirement Benefit Claiming\-Age Combinations Available to Married Couples,” 2017\)
Armour and Hung (“Drawing down Retirement Wealth: Interactions between Social Security Wealth and Private
Retirement Savings,” 2017\)
Armour and Knapp ( The Consequences of Claiming Social Security Benefits at Age 62 , 2021\)
Armour and Knapp ( The Changing Picture of Who Claims Social Security Early , 2021\)
Armour and Knapp (“The consequences of claiming Social Security benefits at age 62,” 2022\)
Atkins and Caliendo (“Strategies for maximizing social security benefits,” 2009\)
Bairoliya and McKiernan (“Revisiting Retirement and Social Security Claiming Decisions,” 2021\)
21Benz (When Is the ’Right’ Time to File for Social Security Benefits? 2021\)
Biggs et al. (“The Consequences of Current Benefit Adjustments for Early and Delayed Claiming,” 2021\)
Bronshtein et al. (“Leaving big money on the table: Arbitrage opportunities in delaying social security,” 2020\)
Clark et al. (“Annuity options in public pension plans: the curious case of social security leveling,” 2018\)
del Carmen Valls Martı́nez et al. (“Pensions, Ageing and Social Security Research: Literature Review and Global
Trends,” 2021\)
Diamond et al. (“Optimal Claiming of Social Security Benefits,” 2021\)
Ding et al. (“Statistical Learning for Individualized Asset Allocation,” 2022\)
Duffy et al. (“The Value of Delayed Social Security Claiming for Higher\-Earning Women,” 2021\)
Eschenbach and Lewis (“Risk, standard deviation, and expected value: when should an individual start social
security?” 2019\)
Fellowes et al. ( The Retirement Solution Hiding in Plain Sight: How Much Retirees Would Gain by Improving
Social Security Decisions , 2019\)
Franklin ( Maximizing Social Security Retirement Benefits , 2021\)
Geisler and Hulse (“The Taxation of Social Security Benefits and Planning Implications,” 2016\)
Glickman and Hermes (“Why Retirees Claim Social Security at 62 and How It Affects Their Retirement Income:
Evidence from the Health and Retirement Study,” 2015\)
Harris (“Should a Retiree File for Social Security at 62 or 70?” 2019\)
Huang et al. ( Housing Wealth Shocks, Home Equity Withdrawal, and the Claiming of Social Security Retirement
Benefits , 2020\)
Jennings and Reichenstein (“Estimating the Value of Social Security Retirement Benefits,” 2001\)
Kuselias et al. (“The Financial and Tax Considerations of Social Security and Early Retirement,” 2021\)
Lalive et al. ( The Impact of Social Security on Pension Claiming and Retirement: Active vs. Passive Decisions ,
2020\)
Laster et al. (“Strategies for Managing Retirement Risks,” 2016\)
Mahaney ( Innovative Strategies to Help Maximize Social Security Benefits , 2020\)
Munnell et al. (“Are Early Claimers Making a Mistake?” 2016\)
Pfau et al. (“A Portfolio Approach to Retirement Income Security,” 2016\)
Reichenstein and Meyer (“Social security claiming strategies for widows and widowers,” 2016\)
Reichenstein and Meyer (“Redo Strategies: When Can You Redo a Prior Social Security Claiming Decision?”
2016\)
Reichenstein and Meyer (“Optimizing Social Security Benefits Is Still Complicated,” 2019\)
Reichenstein and Meyer (“Advice for Married Couples When One Spouse Will Die Year(s) Before the Other
Spouse,” 2021\)
Reichenstein and Meyer (“How Social Security Coordination Can Add Value to a Tax\-Efficient Withdrawal
Strategy,” 2021\)
Reichenstein and Meyer (“Social Security Claiming Strategies for Singles and Their Implications for Couples,”
2021\)
Reznik et al. ( Analysis of Benefit Estimates Shown in the Social Security Statement , 2020\)
Rundle (“A Social Security Purchase: Is Delaying Social Security More Effective than Purchasing a Deferred
Income Annuity?” 2018\)
Shoven and Slavov (“The Decision to Delay Social Security Benefits: Theory and Evidence,” 2012\)
Siskos (“What’s Your Strategy for Maximizing Your Social Security Benefits?” 2021\)
Smith (The Best Age for Social Security Retirement Benefits , 2021\)
Society of Actuaries Research ( Deciding When to Claim Social Security , 2017\)
Templin (“When to Tap Social Security: The Sometimes Surprising Answer From Online Calculators,” 2021\)
2\.2\.15 Glidepath considerations
References:
Arnott et al. (“The Glidepath Illusion ... and Potential Solutions,” 2013\)
Blanchett and Kaplan (“Beyond the Glide Path:The Drivers of Target\-Date Fund Returns,” 2018\)
Clare et al. (“Absolute Momentum, Sustainable Withdrawal Rates and Glidepath Investing in US Retirement
Portfolios from 1925,” 2019\)
22Cosares (“Generating a Family of Optimal Glide Paths for Investment Planning with Target Dates,” 2013\)
Crook (“Liabilities Matter: Improving Target Date Glidepath Construction through Liability Adaptive Asset
Allocation,” 2019\)
Drew and West (“Retirement Income Sufficiency through Personalised Glidepaths,” 2021\)
Estrada (“The Glidepath Illusion: An International Perspective,” 2014\)
Estrada (“The Retirement Glidepath: An International Perspective,” 2016\)
Estrada (“Target\-Date Funds, Glidepaths, and Risk Aversion,” 2020\)
Faria (“An Examination of Target Date Fund Glidepath Construction,” 2021\)
Fraser and Payne (“Bond Tents: Reshaping the Equity Glide Slope at the End of Wealth Accumulation,” 2018\)
Fullmer and Tzitzouris (“Evaluation of Target\-Date Glide Paths withinDefined Contribution Plans,” 2014\)
Ge (“Optimal Glide Path Selection for Low\-Volatility Assets,” 2019\)
Goldstein (“The glide path less traveled: A critical examination of assumptions, outcomes, and glide path
specification,” 2018\)
Idzorek et al. (“Bait and Switch: Glide Path Instability,” 2013\)
Kitces and Pfau (“Retirement Risk, Rising Equity Glidepaths, and Valuation\-Based Asset Allocation,” 2014\)
Krasnopolsky and Ashton (“Why Pairing LDI with De\-Risking Glide Paths Produces Inferior Pension Fund
Outcomes,” 2018\)
Jang et al. (“Glide paths for a retirement plan with deferred annuities,” 2022\)
Milevsky et al. (“A Glide Path for Target Date Fund Annuitization,” 2015\)
Mladina (“Dynamic Asset Allocation with Horizon Risk: Revisiting Glide Path Construction,” 2014\)
Mladina (“Optimal Lifetime Asset Allocation with Goals\-Based, Lifecycle Glide Paths,” 2016\)
Mladina and Grant (“Glide Paths Based on a Retirement Goal and Depleting Human Capital,” 2019\)
Pae and Atra (“Rules of Thumb versus Industry Glide Paths; Some Bootstrapping Evidence,” 2020\)
Rook (“Optimal Equity Glidepaths in Retirement,” 2015\)
Root et al. (“Strategic Liability Management: Building a Glide Path Strategy to Manage Interest Rate and
Longevity Risks,” 2013\)
Wiafe et al. (“Asset Allocation in Retirement: Does Glide Path Matter?” 2016\)
Yoon (“Glide path and dynamic asset allocation of target date funds,” 2010\)
2\.2\.16 Target date strategies
References:
An and Sachdeva (“Missing the Target? Retirement Expectations and Target Date Funds,” 2021\)
Bai and Wallbaum (“Optimizing Pension Outcomes Using Target\-Driven Investment Strategies: Evidence from
Three Asian Countries with the Highest Old\-Age Dependency Ratio,” 2020\)
Basu et al. (“Dynamic Lifecycle Strategies for Target Date Retirement Funds,” 2011\)
Cosares (“Generating a Family of Optimal Glide Paths for Investment Planning with Target Dates,” 2013\)
Crook (“Liabilities Matter: Improving Target Date Glidepath Construction through Liability Adaptive Asset
Allocation,” 2019\)
Faria (“An Examination of Target Date Fund Glidepath Construction,” 2021\)
Fisch and Turner (“Making a Complex Investment Problem Less Difficult:Robo Target\-Date Funds,” 2018\)
Forsyth et al. (“Are target date funds dinosaurs? Failure to adapt can lead to extinction,” 2017\)
Forsyth et al. (“Target Wealth: The Evolution of Target Date Funds,” 2017\)
Gabudean and Weiss (“How to Evaluate Target\-Date Funds: A Practical Guide,” 2019\)
Gabudean et al. (“On Optimal Allocations of Target\-Date Funds,” 2021\)
Janssen et al. (“Life Cycle Investing: From Target\-Date to Goal\-Based Investing,” 2013\)
Kritzman (“Target\-Date Funds: A Regime\-Based Approach,” 2017\)
Massa et al. (“To Target a Date or Not to Target a Date? That is the Question: The Unintended Consequences
of Investing for the Long Run,” 2021\)
Milevsky et al. (“A Glide Path for Target Date Fund Annuitization,” 2015\)
Mitchell and Utkus (“Target\-date funds and portfolio choice in 401(k) plans,” 2021\)
Shoven and Walton (“An Analysis of the Performance of Target Date Funds,” 2021\)
232\.2\.17 Risk management for retirement portfolios and strategies
References:
Bateman et al. (“Risk Information and Retirement Investment Choice Mistakes Under Prospect Theory,” 2015\)
Bhansali (“Tail\-Risk Management for Retirement Investments,” 2015\)
Blanchett (“Addressing Key Retirement Risks,” 2014\)
Bravo (“Funding for longer lives. Retirement wallet and risk\-sharing annuities,” 2019\)
Buetow and Hanke (“How Long is Long Enough?” 2020\)
Campbell and Sigalov (“Portfolio choice with sustainable spending: A model of reaching for yield,” 2022\)
Chen et al. (“Tail index\-linked annuity: A longevity risk sharing retirement plan,” 2022\)
Clare et al. (“Perfect Withdrawal in a Noisy World: Investing Lessons with and without Annuities while in
Drawdown between 2000 and 2019,” 2021\)
Collins et al. (“How Risky is Your Retirement Income Risk Model?” 2015\)
Dadashi (“Optimal investment strategy post retirement without ruin possibility: A numerical algorithm,” 2020\)
DeJong and Robinson (“A Case Study in Sequence Risk: A 20\-Year Retrospective on the Impact of the 2000\-2002
and 2007\-2009 Bear Markets on Retirement Nest Egg Sustainability,” 2022\)
Ding and Marazzina (“Sensitivity of Optimal Retirement Problem to Liquidity Constraints,” 2021\)
Drew et al. (“Conditional Allocations to Real Estate: An Antidote to Sequencing Risk in Defined Contribution
Retirement Plans,” 2015\)
Estrada and Kritzman (“Evaluating Retirement Strategies: A Utility\-Based Approach,” 2018\)
Estrada (“The Gain\-Pain Index: Asset Allocation for Individual (And Other?) Investors,” 2021\)
Fellowes et al. ( The Retirement Solution Hiding in Plain Sight: How Much Retirees Would Gain by Improving
Social Security Decisions , 2019\)
Fox (“Linking metrics to objectives: retirement saving, spending, and active management,” 2020\)
Frank and Brayman (“Combining Stochastic Simulations and Actuarial Withdrawals into One Model,” 2016\)
Ge (“Utilizing Low\-Volatility Assets To Mitigate Sequence Risk In Retirement Investing,” 2019\)
Gemmo et al. (“Optimal portfolio choice with tontines under systematic longevity risk,” 2020\)
Hou (How Accurate Are Retirees’ Assessments of Their Retirement Risk? 2020\)
Huang and Milevsky (“Longevity risk and retirement income tax efficiency: A location spending rate puzzle,”
2016\)
Hunt and Blake (“Basis Risk and Pensions Schemes: A Relative Modelling Approach.,” 2020\)
Khang and Clarke ( Safeguarding retirement in a bear market , 2020\)
Kitces and Pfau (“Retirement Risk, Rising Equity Glidepaths, and Valuation\-Based Asset Allocation,” 2014\)
Laster et al. (“Strategies for Managing Retirement Risks,” 2016\)
Lozada (“Fixed income for retirement saving: TIAA traditional lessons on quality, duration, risk, and gradual
withdrawals,” 2020\)
Lozada ( Financing Retirement using U.S. Treasury Bonds: Safe Withdrawal Rates, Mean/Standard\-Deviation
Frontiers,and Endpoint\-Dependence of the Safest Maturity , 2018\)
Lumby (“Three Essays on Managing Risk in Retirement,” 2017\)
McQuarrie (“Will Required Minimum Distributions Exhaust My Savings and Leave Me in Penury?” 2022\)
Merton and Muralidhar (“Selfies: A new pension bond and currency for retirement,” 2020\)
Milevsky ( Retirement Income Recipes in R: From Ruin Probabilities to Intelligent Drawdowns , 2020\)
Milevsky and Posner (“Can collars reduce retirement sequencing risk? analysis of portfolio longevity extension
overlays (leo),” 2014\)
Mislinski (“How to Illustrate Planning Risks to Clients,” 2021\)
Mitchell (“Withdrawal Rate Strategies for Retirement Portfolios: Preventive Reductions and Risk Management,”
2009\)
Mitchell (“Migrating with Black Swans: Climate Risk and Retirement Planning,” 2016\)
Park (“Influence of risk tolerance on long\-term investments: a Malliavin calculus approach,” 2022\)
Pfau (“The four approaches to managing retirement income risk,” 2019\)
Pepperell et al. (“Death or Bust? The Risk with Post\-Retirement Income Models,” 2020\)
Rietz et al. (“A Simulation for Minimizing both the Probability and the Length of Financial Ruin in Retirement,”
2020\)
Sato (“Optimal Withdrawal Rate Under Longevity Risks: A Criterion for Life Planning after Retirement,” 2016\)
Sharpe ( Retirement Income Analysis with scenario matrices , 2019\)
24Sherwood (“Risk Capacity Portfolio Construction,” 2021\)
Smith and Gould (“Measuring and controlling shortfall risk in retirement,” 2007\)
Simsek et al. (“Optimal Longevity Risk Management in the Retirement Stage of the Life Cycle,” 2018\)
Tian and Zhu (“Optimal Investing after Retirement Under Time\-Varying Risk Capacity Constraint,” 2020\)
Tomlinson (“Coping with Sequence Risk: How Variable Withdrawal and Annuitization Improve Retirement
Outcomes,” 2017\)
Van Harlow ( Optimal Asset Allocation in Retirement: A Downside Risk Perspective , 2014\)
Van Harlow and Brown (“Market Risk, Mortality Risk, And Sustainable Retirement Asset Allocation: A Down\-
side Risk Perspective,” 2016\)
Vrdoljak et al. (“The Role of Variable Annuities in Addressing Retirement Risks,” 2014\)
Walker et al. (“To Reduce the Risk of Retirement Portfolio Exhaustion, Include Home Equity as a Non\-Correlated
Asset in the Portfolio,” 2021\)
Waring and Siegel (“What Investment Risk Means to You, Illustrated Strategic Asset Allocation, the Budget
Constraint, and the Volatility of Spending During Retirement,” 2018\)
Ziemba (“An Approach to Financial Planning of Retirement Pensions with Scenario\-Dependent Correlation
Matrixes and Convex Risk Measures,” 2016\)
2\.2\.18 Presentation and visualization of retirement portfolios and strategies
References:
Bateman et al. (“Risk Information and Retirement Investment Choice Mistakes Under Prospect Theory,” 2015\)
Bengen (“The Planner’s Toolkit for Managing Retirement Withdrawal Plans,” 2021\)
Consigli and Di Tria (“Asset\-liability management and goal\-based investing for retail business,” 2018\)
Costa et al. ( Fuel for the F.I.R.E.: Updating the 4% rule for early retirees , 2021\)
Estrada (“Retirement Planning: From Z to A,” 2020\)
Finke and Blanchett (“An Overview of Retirement Income Strategies,” 2016\)
Frank et al. (“An Age\-Based, Three\-Dimensional Distribution Model Incorporating Sequence and Longevity
Risks,” 2012\)
Iannarone (“Rethinking automated investment adviser disclosure,” 2018\)
Jeon et al. (“Horizon effect on optimal retirement decision,” 2021\)
JP Morgan Asset Management Research ( Guide to Retirement , 2021\)
Lefrancois et al. (“Expectation Risk: A Novel Short\-Term Risk Measure for Long\-Term Financial Projections,”
2020\)
McLean (“Rebalancing Frequency and Safe Withdrawal Rates,” 2021\)
Mislinski (“How to Illustrate Planning Risks to Clients,” 2021\)
Pfau (“Making Sense Out of Variable Spending Strategies for Retirees,” 2015\)
Pfau (“Choosing a Retirement Income Strategy: A New Evaluation Framework,” 2015\)
Thorp et al. (“Flicking the switch: Simplifying disclosure to improve retirement plan choices,” 2020\)
Tomlinson (“Retirement Strategies in Pictures,” 2018\)
Waring and Siegel (“What Investment Risk Means to You, Illustrated Strategic Asset Allocation, the Budget
Constraint, and the Volatility of Spending During Retirement,” 2018\)
Warren (“Design of Investment Options using Utility Functions: A Demonstration for Products,” 2019\)
Zuss (Participants Will Need Support to Understand Lifetime Income Projections , 2022\)
2\.2\.19 Investor risk profile
References:
Alsabah et al. (“Robo\-Advising: Learning Investors Risk Preferences via Portfolio Choices,” 2021\)
Bachmann et al. (“Designing A Risk Profiler: Which Measures Predict Risk Taking?” 2014\)
Blanchett et al. (“Who Exhibits Time Varying Risk Aversion?” 2016\)
Bollen and Posavac (“Gender, risk tolerance, and false consensus in asset allocation recommendations,” 2018\)
Boreiko and Massarotti (“How Risk Profiles of Investors Affect Robo\-Advised Portfolios,” 2020\)
Capponi et al. (“Personalized Robo\-Advising: Enhancing Investment through Client Interaction,” 2020\)
Capponi and Zhang (“Risk Preferences and Efficiency of Household Portfolios,” 2020\)
Dong et al. (“Robo\-advisor using closed\-form solutions for investors’ risk preferences,” 2022\)
25Erdemlioglu and Joliet (“Long\-term asset allocation, risk tolerance and market sentiment,” 2019\)
Estrada (“Target\-Date Funds, Glidepaths, and Risk Aversion,” 2020\)
Estrada (“The Gain\-Pain Index: Asset Allocation for Individual (And Other?) Investors,” 2021\)
Fan et al. (“Optimal estimation of functionals of high\-dimensional mean and covariance matrix,” 2021\)
Gard and Gremm (“Two Measures of Financial Risk Tolerance from Questionnaire Data,” 2018\)
Grable et al. (“A test of traditional and psychometric relative risk tolerance measures on household financial
risk taking,” 2019\)
Hubble and Grable (“The efficient frontuzzle: what investment risk profiling still fails to solve,” 2019\)
Khanna and Chauhan (“A study of risk profiling and investment choices of retail investor,” 2017\)
Klement (“Investor Risk Profiling: An Overview,” 2015\)
Klement (“Risk Profiling and Tolerance: Insights for the Private Wealth Manager,” 2018\)
Lurtz et al. (“A deeper dive: A mixed methods approach to risk tolerance,” 2021\)
Momen et al. (“A robust behavioral portfolio selection: model with investor attitudes and biases,” 2020\)
Park (“Influence of risk tolerance on long\-term investments: a Malliavin calculus approach,” 2022\)
Ryack (“Incorporating Financial Risk Tolerance Research into the Financial Planning Process,” 2016\)
Sahm (“How Much Does Risk Tolerance Change?” 2017\)
Sivarajan and De Bruijn (“Risk Tolerance, Return Expectations and Other Factors Impacting Investment De\-
cisions,” 2021\)
Swedroe (“The Role of Financial Risk Tolerance in Investment Policy,” 2021\)
Tertilt and Scholz (“To Advise, or Not to Advise Robo\-Advisors Evaluate the Risk Preferences of Private
Investors,” 2018\)
Thanki et al. (“Psychological antecedents of financial risk tolerance,” 2020\)
Vandenbroucke and Fortuna (“Loss Aversion Implied by a Risk\-Based Questionnaire,” 2019\)
Veres (“A Comparison of Risk Tolerance Products,” 2020\)
Weber and Klement (“Risk tolerance and circumstances,” 2018\)
Xu (“The risk profiles of 401(k) accounts,” 2015\)
Yu et al. (“Learning Time Varying Risk Preferences from Investment Portfolios using Inverse Optimization with
Applications on Mutual Funds,” 2021\)
Yu et al. (“Learning Risk Preferences from Investment Portfolios Using Inverse Optimization,” 2021\)
2\.2\.20 Testing, evaluating and comparison procedures for retirement portfolios and strategies
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
Elkins (Stanford analyzed 292 retirement strategies to determine the best one – here’s how it works , 2019\)
Estrada and Kritzman (“Evaluating Retirement Strategies: A Utility\-Based Approach,” 2018\)
Fabozzi and Lopez de Prado (“Being Honest in Backtest Reporting: A Template for Disclosing Multiple Tests,”
2018\)
26Greiner and Stoyanov (“Portfolio scoring by expected risk premium,” 2019\)
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
Pfau et al. ( Optimizing Retirement Income by Integrating Retirement Plans, IRAs, and Home Equity: A Frame\-
work for Evaluating Retirement Income Decisions , 2017\)
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
Zhang et al. (“DoubleEnsemble: A New Ensemble Method Based on Sample Reweighting and Feature Selection
for Financial Data Analysis,” 2020\)
Zhang et al. (“Information Coefficient as a Performance Measure of Stock Selection Models,” 2020\)
Zhang et al. (“Deep Learning for Portfolio Optimization,” 2020\)
273 Practical details for the project
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
283\.4 Deliverables
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
294 Project tasks and timelines
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
30•For each article focus primarily on Abstract, Conclusion, and Numerical Results
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
31•Visual Paradigm ( online )
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
325 Design and implementation for the project codes
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
33Figure 2: Examples of architecture of coding framework: Greykite
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
34Figure 4: Examples of major components of coding framework (top) and UML diagrams (bottom)
35Figure 5: Financial Machine Learning in Portfolio Construction
Source: Machine Learning in Asset Management365\.2 Representative examples of Python libraries with well designed folder structure
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
376 Practical Info
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
38I can provide you with a bibliography file which contains all refeernces mentioned in the project description, This
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
39•to be as liquid as possible
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
40Table 3: Monthly data sets
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
417 Potentially useful Python and R software implementations: pack\-
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
427\.3 Anomaly detection and data outliers
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
43•dsos: Dataset Shift with Outlier Scores
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
44R software implementations
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
45•DEBBI: Differential Evolution\-Based Bayesian Inference
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
46R software implementations
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
47•LightGBM: fast, distributed, high performance gradient boosting (GBT, GBDT, GBRT, GBM or MART)
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
48•mixSPE: Mixtures of Power Exponential and Skew Power Exponential Distributions for Use in Model\-Based
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
49•genieclust: Fast and Robust Hierarchical Clustering with Noise Point Detection
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
50•evclust: Evidential Clustering
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
51•pytorch\_cluster: PyTorch Extension Library of Optimized Graph Cluster Algorithms
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
52•flake8: glues together pycodestyle, pyflakes, mccabe, and third\-party plugins to check the style and quality of
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
53•pydantic: Data parsing and validation using Python type hints
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
54R software implementations
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
55•rstudio.prefs: Set ’RStudio’ Preferences
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
56•scalene: high\-performance, high\-precision CPU, GPU, and memory profiler for Python
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
57R software implementations
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
58•MatrixCorrelation: Matrix Correlation Coefficients
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
59R software implementations
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
60•rigr: Regression, Inference, and General Data Analysis Tools in R
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
61•pythae: Unifying Generative Autoencoder implementations in Python
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
62•MSCMT: Multivariate Synthetic Control Method Using Time Series
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
63•Voluptuous: data validation library.
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
64R software implementations
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
657\.16 Data regimes, states and changepoints: analysis and modeling
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
66R software implementations
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
67•robcp: Robust Change\-Point Tests
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
68•PyMongo \- the Python driver for MongoDB
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
69•qs: Quick Serialization of R Objects
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
707\.19 Dimensionality reduction
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
71•Rdimtools: Dimension Reduction and Estimation Methods
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
72•stumpy: variety of time series data mining tasks
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
73R software implementations
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
74•pdp: Partial Dependence Plots
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
75•theft: Tools for Handling Extraction of Features from Time Series
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
76•psd: Adaptive, Sine\-Multitaper Power Spectral Density and Cross Spectrum Estimation
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
77•glum: Generalized linear models
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
78•sktime: unified framework for machine learning with time series by UK national institute for data science and
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
79•ForecastComb: Forecast Combination Methods
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
80•robets: Forecasting Time Series with Robust Exponential Smoothing
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
817\.26 Graphs and graphical modeling
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
82R software implementations
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
83•Catalyst: PyTorch framework for Deep Learning Research and Development
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
84•NannyM: estimate post\-deployment model performance (without access to targets), detect data drift, and
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
85•distillML: Model Distillation and Interpretability Methods for Machine Learning Models
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
867\.29 Machine Learning frameworks (includes Automated ML and hyperparameters
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
87•Optuna: hyperparameter optimization framework
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
88•netrd: etwork {reconstruction, distances, dynamics}
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
89•statnet: Software Tools for the Statistical Analysis of Network Data
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
90•nlopt: nonlinear optimization
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
91•graDiEnt: derivative\-free, optim\-style Stochastic Quasi\-Gradient Differential Evolution optimization
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
92•NGBoost: Natural Gradient Boosting for Probabilistic Prediction
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
93•hmmr: ”Mixture and Hidden Markov Models with R” Datasets and Example Code
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
94•RMixtComp: Mixture Models with Heterogeneous and (Partially) Missing Data
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
95•Gym: ttolkit by openAI for toolkit for developing and comparing reinforcement learning algorithms
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
96R software implementations
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
97•RobustANOVA: Robust One\-Way ANOVA Tests under Heteroscedasticity and Nonnormality
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
98•scikit\-learn: machine learning in Python
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
99•NonpModelCheck: Model Checking and Variable Selection in Nonparametric Regression
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
1007\.36 Sensitivity analysis and numerical derivatives
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
101•PyProbables: Probabilistic data structures in python
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
102•mlquantify: Algorithms for Class Distribution Estimation
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
103•ExtremalDep: Extremal Dependence Models
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
104•SR Bench: benchmark framework for symbolic regression
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
105R software implementations
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
106•fdrci: Permutation\-Based FDR Point and Confidence Interval Estimation
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
107•OutliersO3: Draws Overview of Outliers (O3\) Plots
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
1087\.41 Testing software codes
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
109R software implementations
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
110•hcrystalball: unifies the API for most commonly used libraries and modeling techniques for time\-series fore\-
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
111R software implementations
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
112•shrink: Global, Parameterwise and Joint Shrinkage Factor Estimation
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
113•nlpaug: Data augmentation for NLP
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
114•text2sdg: Detecting UN Sustainable Development Goals in Text
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
1157\.45 Visualization and reporting
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
116•tourr: Tour Methods for Multivariate Data Visualisation
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
117•ggfocus: Scales that Focus Specific Levels in your ggplot
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
118•gtsummary: Presentation\-Ready Data Summary and Analytic Result Tables
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
119•shinydlplot: Add a Download Button to a ’shiny’ Plot or ’plotly’
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
1208\.2 Research studies with code
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
121Snow (“Machine Learning in Asset Management Part 1: Portfolio Construction Trading Strategies,” 2020\)
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
122•lrsm\_portfolio: Portfolio Construction using Stratified Models
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
1238\.4 R software implementations
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
124•qrmtools: Tools for Quantitative Risk Management
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
125References
Abeliansky, A. and Strulik, H. (2021\). “Health and Aging Before and after Retirement .” In:SSRN e\-Print .
Ackerley, A., Nefouse, N., and Nikles, D. (2022\). To spend or not to spend? Tech. rep. BlackRock.
Adcock, C., Areal, N., Armada, M. R., Cortez, M. C., Oliveira, B., and Silva, F. (2017\). “Portfolio Performance
Measurement: Monotonicity with Respect to the Sharpe Ratio and Multivariate Tests of Correlation .” In:SSRN
e\-Print .
Alderson, M. J. and Betker, B. L. (2017\). “Does the Benefit of Deferring Social Security Offset the Opportunity
Cost to Do So? ” In:Journal of Financial Planning .
Alexandrova, M. and Gatzert, N. (2019\). “What Do We Know About Annuitization Decisions? ” In:Risk Manage\-
ment and Insurance Review 22(1\), pp. 57–100\.
Ali, Y., Fang, M., Sota, P. A. A., Taylor, S., and Wang, X. (2019\). “Social Security Benefit Valuation, Risk, and
Optimal Retirement .” In:Risks 7(4\), p. 124\.
Aliaga\-Diaz, R., Ahluwalia, H., Zhu, V., Donaldson, S., Daga, A., and Pakula, D. (2021\). Vanguard’s Life\-Cycle
Investing Model (VLCM): A general portfolio framework for goals\-based investing . Tech. rep. Vanguard.
Alleva, B. (2016\). “Discount Rate Specification and the Social Security Claiming Decision .” In:SSRN e\-Print .
Alleva, B. (2017\). “Social Security Retirement Benefit Claiming\-Age Combinations Available to Married Couples .”
In:SSRN e\-Print .
Alleva, B. J. (2015\). “Minimizing the Risk of Opportunity Loss in the Social Security Claiming Decision .” In:The
Journal of Retirement 3(1\), pp. 67–86\.
Alsabah, H., Capponi, A., Ruiz Lacedelli, O., and Stern, M. (2021\). “Robo\-Advising: Learning Investors Risk
Preferences via Portfolio Choices .” In:Journal of Financial Econometrics 19(2\), pp. 369–292\.
An, B.\-J. and Sachdeva, K. (2021\). “Missing the Target? Retirement Expectations and Target Date Funds .” In:
SSRN e\-Print .
Anantharaman, D. and Henderson, D. (2016\). “Understanding Pension Liabilities: A Closer Examination of Discount
Rates.” In:SSRN e\-Print .
Ardia, D., Boudt, K., and Gagnon\-Fleury, J.\-P. (2017\). “RiskPortfolios: Computation of Risk\-Based Portfolios in
R.” In:The Journal of Open Source Software 2(10\), pp. 171\+.
Armour, P. and Hung, A. (2017\). “Drawing down Retirement Wealth: Interactions between Social Security Wealth
and Private Retirement Savings .” In:SSRN e\-Print .
Armour, P. and Knapp, D. (2021a). The Changing Picture of Who Claims Social Security Early . Tech. rep. AARP
Public Policy Institute.
Armour, P. and Knapp, D. (2021b). The Consequences of Claiming Social Security Benefits at Age 62 . Tech. rep.
AARP Public Policy Institute.
Armour, P. and Knapp, D. (2022\). “The consequences of claiming Social Security benefits at age 62 .” In:Journal
of Pension Economics and Finance , pp. 1–27\.
Arnold, T., Earl, J. H., Marshall, C. D., and Schwartz, A. (2017\). “Excel Calculators for Determining Retirement
Accumulation and Disbursement Information .” In:The Journal of Wealth Management 20(2\), pp. 94–101\.
Arnold, T., Earl, J. H., Marshall, C. D., and Schwartz, A. (2018\). “Using ”Equivalent Tax Rates” to Determine
Tax\-Efficient Retirement Investment and Withdrawal .” In:The Journal of Wealth Management 21(2\), pp. 55–69\.
Arnott, R. D., Harvey, C. R., and Markowitz, H. (2019\). “A backtesting protocol in the era of machine learning .”
In:The Journal of Financial Data Science 1(1\), pp. 64–74\.
Arnott, R. D., Sherrerd, K. F., and Wu, L. (2013\). “The Glidepath Illusion ... and Potential Solutions .” In:The
Journal of Retirement 1(2\), pp. 13–28\.
Arshanapalli, B. and Nelson, W. (2012\). “Asset Allocation Options for Wealth Accumulation .” In:The Journal of
Wealth Management 14(4\), pp. 22–27\.
Assabil, S. E. and Mcleish, D. L. (2021\). “Assessing the Impact of Longevity Risk for Countries with Limited Data .”
In:The Journal of Retirement 8(3\), pp. 62–75\.
Atkins, A. B. and Caliendo, F. N. (2009\). “Strategies for maximizing social security benefits .” In:The Journal of
Wealth Management 12(1\), pp. 25–31\.
Azman, S. and Pathmanathan, D. (2022\). “The GLM framework of the Lee\-Carter model: a multi\-country study .”
In:Journal of Applied Statistics 49(3\), pp. 1752\-763–12\.
Bachmann, K., Hens, T., and Stossel, R. (2014\). “Designing A Risk Profiler: Which Measures Predict Risk Taking? ”
In:SSRN e\-Print .
126Bacon, C. R. (2019\). “Performance Attribution: History and Progress .” In:CFA Institute Research Foundation
Publications .
Bai, Z. and Wallbaum, K. (2020\). “Optimizing Pension Outcomes Using Target\-Driven Investment Strategies:
Evidence from Three Asian Countries with the Highest Old\-Age Dependency Ratio .” In:Asia\-Pacific Journal
of Financial Studies 49(4\), pp. 652–682\.
Bailey, D. H., Borwein, J. M., and Lopez de Prado, M. (2017\). “Stock Portfolio Design and Backtest Overfitting .”
In:Journal of Investment Management 15(1\), pp. 75–87\.
Bailey, R., DeShetler, A., Leming, J., Weber, S. M., Youssef, J., and Young, J. A. (2021\). Planning for health care
costs in retirement . Tech. rep. Vanguard.
Bairoliya, N. and McKiernan, K. (2021\). “Revisiting Retirement and Social Security Claiming Decisions .” In:SSRN
e\-Print .
Banerjee, S. (2019\). Asset Decumulation or Asset Preservation? What Guides Retirement Spending? Tech. rep.
Employee Benefit Research Institute EBRI.
Basu, A. K., Byrne, A., and Drew, M. E. (2011\). “Dynamic Lifecycle Strategies for Target Date Retirement Funds .”
In:The Journal of Portfolio Management 37(2\), pp. 83–96\.
Basu, A. K. and Wiafe, O. K. (2017\). “Impact of persistent bad returns and volatility on retirement outcomes .” In:
Finance Research Letters 21, pp. 201–205\.
Bateman, H., Stevens, R., and Lai, A. (2015\). “Risk Information and Retirement Investment Choice Mistakes Under
Prospect Theory .” In:Journal of Behavioral Finance 16(4\), pp. 279–296\.
Bell, D. N. F., Comerford, D. A., and Douglas, E. (2020\). “How do subjective life expectancies compare with
mortality tables? Similarities and differences in three national samples .” In:The Journal of the Economics of
Ageing 16 (100241\).
Bengen, W. P. (2021\). “The Planner’s Toolkit for Managing Retirement Withdrawal Plans .” In:Journal of Financial
Planning 34(4\), pp. 74–80\.
Benz, C. (2021\). When Is the ’Right’ Time to File for Social Security Benefits? Tech. rep. Morningstar.
Beracha, E., Downs, D. H., and MacKinnon, G. (2017\). “The 4% rule: Does real estate make a difference? ” In:
Journal of Property Research 34(3\), pp. 181–210\.
Bernhardt, T. and Donnelly, C. (2018\). Pension Decumulation Strategies: A State\-of\-the\-Art Report . Tech. rep. Risk
Insight Lab, Heriot\-Watt University.
Bessler, W., Opfer, H., and Wolff, D. (2017\). “Multi\-asset portfolio optimization and out\-of\-sample performance: an
evaluation of Black Litterman, mean\-variance, and naive diversification approaches .” In:The European Journal
of Finance 23(1\), pp. 1–30\.
Bessler, W. and Wolff, D. (2017\). “Portfolio Optimization with Industry Return Prediction Models .” In:SSRN
e\-Print .
Bhansali, V. (2015\). “Tail\-Risk Management for Retirement Investments .” In:The Journal of Retirement 2(3\),
pp. 78–86\.
Bianchi, M. and Briere, M. (2021a). “Robo\-Advising for Small Investors .” In:SSRN e\-Print .
Bianchi, M. and Briere, M. (2021b). “Robo\-Advising: Less AI and More XAI? ” In:SSRN e\-Print .
Biggs, A. G., Chen, A., and Munnell, A. (2021\). “The Consequences of Current Benefit Adjustments for Early and
Delayed Claiming .” In:SSRN e\-Print .
Biggs, A. G. (2017\). “The life cycle model, replacement rates, and retirement income adequacy .” In:The Journal
of Retirement 4(3\), pp. 96–110\.
Bjerring, T., Ross, O., and Weissensteiner, A. (2017\). “Feature selection for portfolio optimization .” In:Annals of
Operations Research 256, pp. 21–40\.
Blake, D. and Cairns, A. J. G. (2020\). “Longevity risk and capital markets: the 2018\-19 update .” In:Annals of
Actuarial Science 14(2\), pp. 219–261\.
Blanchett, D. (2014\). “Addressing Key Retirement Risks .” In:The Journal of Retirement 2(2\), pp. 67–80\.
Blanchett, D. (2018\). “Health shocks and subsequent retiree spending .” In:The Journal of Retirement 6(1\), pp. 55–
69\.
Blanchett, D. (2020a). “The Benefit of Diversified Guaranteed Income for Retirees: Combining Immediate Fixed
and Variable Annuities .” In:Retirement Management Journal 2(3\).
Blanchett, D. (2020b). “The value of allocating to annuities .” In:The Journal of Retirement 8(1\), pp. 40–52\.
Blanchett, D. (2021a). “Do Advisors Improve 401(k) Plans? ” In:The Journal of Retirement 8(4\), pp. 26–42\.
127Blanchett, D. (2021b). “Minding the Gap in Subjective Mortality Estimates .” In:The Journal of Retirement 9(2\),
pp. 8–20\.
Blanchett, D. and Cormier, W. (2021\). “Right\-Sizing Retirement: Exploring the Retirement Consumption Gap in
Early Retirement .” In:Journal of Financial Planning 34(2\), pp. 68–81\.
Blanchett, D., Finke, M., and Pfau, W. (2018\). “Low Returns and Optimal Retirement Savings .” In:How Persistent
Low Returns Will Shape Saving and Retirement . Oxford University Press.
Blanchett, D. and Finke, M. S. (2019\). “Should Annuities be Purchased from Tax\-Sheltered Assets? ” In:SSRN
e\-Print .
Blanchett, D. and Finke, M. S. (2021\). “Guaranteed Income: A License to Spend .” In:SSRN e\-Print .
Blanchett, D., Finke, M. S., and Guillemette, M. A. (2016a). “Who Exhibits Time Varying Risk Aversion? ” In:
SSRN e\-Print .
Blanchett, D., Finke, M. S., and Pfau, W. D. (2016b). “Required Retirement Savings Rates Today .” In:SSRN
e\-Print .
Blanchett, D. and Kaplan, P. D. (2018\). “Beyond the Glide Path:The Drivers of Target\-Date Fund Returns .” In:
The Journal of Retirement 5(4\), pp. 25–39\.
Blanchett, D. M. (2017\). “The Impact of Guaranteed Income and Dynamic Withdrawals on Safe Initial Withdrawal
Rates.” In:Journal of Financial Planning 30(4\), pp. 42–52\.
Blanchett, D. M., Finke, M., and Pfau, W. D. (2013\). “Low Bond Yields and Safe Portfolio Withdrawal Rates .” In:
The Journal of Wealth Management 16(2\), pp. 55–62\.
Bogan, V. L., Geczy, C. C., and Grable, J. E. (2020\). “Financial planning: A research agenda for the next decade .”
In:Financial Planning Review 3(2\).
Boileau, P., Hejazi, N., Collica, B., Laan, M. van der, and Dudoit, S. (2021\). “cvCovEst: Cross\-validated covariance
matrix estimator selection and evaluation in R .” In:Journal of Open Source Software 6(63\), p. 3273\.
Bollen, N. P. B. and Posavac, S. (2018\). “Gender, risk tolerance, and false consensus in asset allocation recommen\-
dations .” In:Journal of Banking \& Finance 87, pp. 304–317\.
Boon, L.\-N., Briere, M., and Werker, B. J. M. (2020\). “Systematic longevity risk: to bear or to insure? ” In:Journal
of Pension Economics and Finance 19(3\), pp. 409–441\.
Boreiko, D. and Massarotti, F. (2020\). “How Risk Profiles of Investors Affect Robo\-Advised Portfolios .” In:Frontiers
in Artificial Intelligence 3\.
Branning, J. and Grubbs, M. (2019\). “Crafting Retirement Income that is Stable, Secure, and Sustainable .” In:
SSRN e\-Print .
Brauer, K. (2021\). “Nudged into Better Portfolios and Lower Risk: Robo\-Advice and Savings Decisions .” In:SSRN
e\-Print .
Bravo, J. M. (2019\). “Funding for longer lives. Retirement wallet and risk\-sharing annuities .” In:Ekonomiaz: Revista
vasca de economia .
Bravo, J. M. V. (2020\). “Addressing the Pension Decumulation Phase of Employee Retirement Planning .” In:Who
Wants to Retire and Who Can Afford to Retire? IntechOpen.
Breach, T., D’Amico, S., and Orphanides, A. (2020\). “The term structure and inflation uncertainty .” In:Journal of
Financial Economics 138(2\), pp. 388–414\.
Bronshtein, G., Scott, J., Shoven, J. B., and Slavov, S. N. (2020\). “Leaving big money on the table: Arbitrage
opportunities in delaying social security .” In:The Quarterly Review of Economics and Finance 78, pp. 261–272\.
Browning, C., Guo, T., Cheng, Y., and Finke, M. S. (2020\). “Spending in Retirement .” In:SSRN e\-Print .
Brugiere, P. (2020\). Quantitative Portfolio Management with Applications in Python . Springer International Pub\-
lishing. 189 pp.
Bruni, R., Cesarone, F., Scozzari, A., and Tardella, F. (2016\). “Real\-world datasets for portfolio selection and
solutions of some stochastic dominance portfolio models .” In:Data in Brief 8, pp. 858–862\.
Bruni, R., Cesarone, F., Scozzari, A., and Tardella, F. (2017\). “On exact and approximate stochastic dominance
strategies for portfolio selection .” In:European Journal of Operational Research 259(1\), pp. 322–329\.
Bryzgalova, S., Huang, J., and Julliard, C. (2021a). “Bayesian solutions for the factor zoo: we just ran two quadrillion
models .” In:SSRN e\-Print .
Bryzgalova, S., Pelger, M., and Zhu, J. (2021b). “Forest Through the Trees: Building Cross\-Sections of Stock
Returns .” In:SSRN e\-Print .
Buetow, G. W. and Hanke, B. (2020\). “How Long is Long Enough? ” In:The Journal of Retirement 88(22\), pp. 39–
48\.
128Buetow, G. W., Hanke, B., and Zagonov, M. (2020\). “Active management in defined contribution plans .” In:The
Journal of Retirement 7(4\), pp. 61–79\.
Butt, A., Khemka, G., and Warren, G. J. (2021\). “Principles and Rules for Translating Retirement Objectives into
Strategies .” In:SSRN e\-Print .
Cairns, A. J. G., Blake, D., Dowd, K., and Coughlan, G. (2020\). “A Two\-Factor Model for Stochastic Mortality
with Parameter Uncertainty: Theory and Calibration .” In:SSRN e\-Print (s).
Cajas, D. (2021a). “Entropic Portfolio Optimization: a Disciplined Convex Programming Framework .” In:SSRN
e\-Print .
Cajas, D. (2021b). “OWA Portfolio Optimization: a Disciplined Convex Programming Framework .” In:SSRN e\-
Print.
Campbell, J. Y. and Sigalov, R. (2022\). “Portfolio choice with sustainable spending: A model of reaching for yield .”
In:Journal of Financial Economics 143(1\), pp. 188–206\.
Canarella, G., Gil\-Alana, L. A., Gupta, R., and Miller, S. M. (2020\). “Modeling US historical time\-series prices and
inflation using alternative long\-memory approaches .” In:Empirical economics 58, pp. 1491–1511\.
Capolongo, A. and Pacella, C. (2021\). “Forecasting inflation in the euro area: countries matter! ” In:Empirical
Economics 61, pp. 2477–2499\.
Capponi, A., Olafsson, S., and Zariphopoulou, T. (2020\). “Personalized Robo\-Advising: Enhancing Investment
through Client Interaction .” In:arXiv e\-Print .
Capponi, A. and Zhang, Z. (2020\). “Risk Preferences and Efficiency of Household Portfolios .” In:arXiv e\-Print .
Cassidy, D. P., Peskin, M. W., Siegel, L. B., and Sexauer, S. (2013\). “Be Kind to Your Retirement Plan \- Give It a
Benchmark .” In:The Journal of Retirement 1(1\), pp. 81–90\.
Cesarone, F., Moretti, J., and Tardella, F. (2018\). “Why Small Portfolios Are Preferable and How to Choose Them .”
In:SSRN e\-Print .
Cesarone, F., Mottura, C., Ricci, J. M., and Tardella, F. (2019\). “On the stability of portfolio selection models .” In:
SSRN e\-Print .
Chalmers, J. and Reuter, J. (2020\). “Is conflicted investment advice better than no advice? ” In:Journal of Financial
Economics 138(2\), pp. 366–387\.
Chang, H.\-Y., Sheu, D.\-F., and Chen, S.\-Y. (2010\). “A Framework for Assessing Individual Retirement Planning
Investment Policy Performance .” In:The Journal of Wealth Management 13(3\), pp. 38–49\.
Changwony, F. K., Campbell, K., and Tabner, I. T. (2021\). “Savings goals and wealth allocation in household
financial portfolios .” In:Journal of Banking \& Finance 124 (106028\).
Chaudhuri, S. E. and Lo, A. W. (2019\). “Dynamic Alpha: A Spectral Decomposition of Investment Performance
Across Time Horizons .” In:Management Science 65(9\), pp. 4440–4450\.
Chen, A., Fuino, M., Sehner, T., and Wagner, J. (2022a). “Valuation of long\-term care options embedded in life
annuities .” In:Annals of Actuarial Science , pp. 1–27\.
Chen, A., Hieber, P., and Rach, M. (2021a). “Optimal retirement products under subjective mortality beliefs .” In:
Insurance: Mathematics and Economics 101(A), pp. 55–69\.
Chen, A., Li, H., and Schultze, M. B. (2022b). “Tail index\-linked annuity: A longevity risk sharing retirement plan .”
In:Scandinavian Actuarial Journal , pp. 1–26\.
Chen, A., Rach, M., and Sehner, T. (2019\). “On the Optimal Combination of Annuities and Tontines .” In:SSRN
e\-Print .
Chen, A. Y. and Zimmermann, T. (2022\). “Open Source Cross\-Sectional Asset Pricing .” In:American Finance
Association Annual Meeting .
Chen, A. and Munnell, A. H. (2021\). How Much Taxes Will Retirees Owe on Their Retirement Income? Tech. rep.
Center for Retirement Research at Boston College.
Chen, A., Haberman, S., and Thomas, S. (2020\). “The implication of the hyperbolic discount model for the an\-
nuitisation decisions .” In:Journal of Pension Economics and Finance 19(3\), pp. 372–391\.
Chen, A., Haberman, S., and Thomas, S. H. (2021b). “Combining Flexible Asset Allocation, Sustainable With\-
drawals, and Deferred Annuities to provide an Adaptive Lifelong Investing Solution .” In:SSRN e\-Print .
Chen, A., Haberman, S., and Thomas, S. (2017\). “Optimal Decumulation Strategies During Retirement with De\-
ferred Annuities .” In:SSRN e\-Print .
Chen, W. and Langrene, N. (2020\). “Deep neural network for optimal retirement consumption in defined contribution
pension system .” In:arXiv e\-Print .
129Chen, W., Minney, A., Toscas, P., Koo, B., Zhu, Z., and Pantelous, A. A. (2021c). “Personalised drawdown strategies
and partial annuitisation to mitigate longevity risk .” In:Finance Research Letters 39 (101644\).
Cheng, Y., Gibson, P., and Guo, T. (2017\). “Life Quality and Health Costs in Late Retirement .” In:SSRN e\-Print .
Chib, S. (2020\). R package czfactor . Tech. rep. Washington University.
Chib, S. and Zhao, L. (2020\). R package czzg . Tech. rep. Washington University.
Chien, C.\-L. (2019\). Enhancing Retirement Success Rates in the United States . Springer International Publishing.
113 pp.
Chiu, Y.\-F., Hsieh, M.\-H., and Tsai, C. (2019\). “Valuation and analysis on complex equity indexed annuities .” In:
Pacific\-Basin Finance Journal 57 (101175\).
Clare, A., Glover, S., Seaton, J., Smith, P. N., and Thomas, S. (2020\). “Measuring sequence of returns risk .” In:
The Journal of Retirement 8(1\), pp. 65–79\.
Clare, A., Seaton, J., Smith, P. N., and Thomas, S. (2017\). “Reducing Sequence Risk Using Trend Following and
the CAPE Ratio .” In:Financial Analysts Journal 73(4\), pp. 91–103\.
Clare, A., Seaton, J., Smith, P. N., and Thomas, S. (2021a). “Perfect Withdrawal in a Noisy World: Investing
Lessons with and without Annuities while in Drawdown between 2000 and 2019 .” In:The Journal of Retirement
9(1\), pp. 9–39\.
Clare, A. D., Seaton, J., Smith, P. N., and Thomas, S. H. (2019\). “Absolute Momentum, Sustainable Withdrawal
Rates and Glidepath Investing in US Retirement Portfolios from 1925 .” In:SSRN e\-Print .
Clare, A. D., Seaton, J., Smith, P. N., and Thomas, S. H. (2021b). “Can sustainable withdrawal rates be enhanced
by trend following? ” In:International Journal of Finance \& Economics 26(1\), pp. 27–41\.
Clark, R., Maurer, R., and Mitchell, O. S. (2018a). “How Persistent Low Returns Will Shape Saving and Retirement .”
In:How Persistent Low Returns Will Shape Saving and Retirement . Oxford University Press.
Clark, R. L., Hammond, R. G., Morrill, M. S., and Vanderweide, D. (2018b). “Annuity options in public pension
plans: the curious case of social security leveling .” In:The Journal of Retirement 6(1\), pp. 33–44\.
Collins, P. J. (2016\). “Annuities and retirement income planning .” In:CFA Foundation Research Foundation Briefs .
Collins, P. J., Lam, H. D., and Stampfli, J. (2015\). “How Risky is Your Retirement Income Risk Model? ” In:
Financial Services Review 24(3\).
Collins, P. J. and Stampfli, J. (2019\). “Sequence of Returns Risk Reconsidered .” In:Retirement Management Journal
8(1\).
Consigli, G. and Di Tria, M. (2018\). “Asset\-liability management and goal\-based investing for retail business .” In:
International Journal of Financial Engineering and Risk Management 2(4\), p. 308\.
Consigli, G., Iaquinta, G., Moriggia, V., di Tria, M., and Musitelli, D. (2012\). “Retirement planning in individual
asset liability management .” In:IMA Journal of Management Mathematics 23(4\), pp. 365–396\.
Consiglio, A., Cocco, F., and Zenios, S. (2006\). “Scenario optimization asset and liability modelling for individual
investors .” In:Annals of Operations Research 152(1\), pp. 167–191\.
Coppola, M., Russolillo, M., and Simone, R. (2020\). “On the management of retirement age indexed to life ex\-
pectancy: a scenario analysis of the Italian longevity experience .” In:The Journal of Risk Finance 21(3\), pp. 217–
231\.
Coqueret, G. (2022\). Perspectives in sustainable equity investing (website version) .
Coqueret, G. and Guida, T. (2020\). Machine Learning for Factor Investing: R Version . Chapman and Hall/CRC.
341 pp.
Correia, C. L., Sayre, R., and Allen, J. C. (2017\). “Avoiding the Medicaid Trap: A Step\-by\-Step Guide to Estate
Planning .” In:The Journal of Retirement 5(2\), pp. 96–103\.
Cosares, S. (2013\). “Generating a Family of Optimal Glide Paths for Investment Planning with Target Dates .” In:
The Journal of Wealth Management 16(3\), pp. 43–53\.
Costa, P., Pakula, D., and Clarke, A. S. (2021\). Fuel for the F.I.R.E.: Updating the 4% rule for early retirees .
Tech. rep. Vanguard.
Crook, M. and Baredes, M. (2015\). “Total Wealth Allocation: Liquidity, Longevity, and Legacy .” In:The Journal
of Wealth Management 18(3\), pp. 18–26\.
Crook, M. and Sutedja, R. (2017\). “Will Long\-Term Care Ruin Retirement Plans? ” In:The Journal of Retirement
4(3\), pp. 42–50\.
Crook, M. W. (2019\). “Liabilities Matter: Improving Target Date Glidepath Construction through Liability Adaptive
Asset Allocation .” In:The Journal of Retirement 7(1\), pp. 44–57\.
130Cvitanic, J., Kou, S., Wan, X., and Williams, K. L. (2020\). “Pi portfolio management: reaching goals while avoiding
drawdowns .” In:SSRN e\-Print .
D’Acunto, F. and Rossi, A. G. (2021\). “New Frontiers of Robo\-Advising: Consumption, Saving, Debt Management,
and Taxes .” In:SSRN e\-Print .
Dadashi, H. (2020a). “Optimal investment strategy post retirement without ruin possibility: A numerical algorithm .”
In:Journal of Computational and Applied Mathematics 363, pp. 325–336\.
Dadashi, H. (2020b). “Optimal investment–consumption problem: Post\-retirement with minimum guarantee .” In:
Insurance: Mathematics and Economics 94, pp. 160–181\.
Daher, M., Dahling, D., Pritchard, R., and Tseng, B. (2020\). From Accumulation to Decumulation – Why It Matters
and What Plan Sponsors Should Know . Tech. rep. Fidelity Investments.
Dai, W. and Medhat, M. (2021\). “US Inflation and Global Asset Returns .” In:SSRN e\-Print .
Dang, D.\-M., Forsyth, P. A., and Vetzal, K. R. (2017\). “The 4 percent strategy revisited: a pre\-commitment mean\-
variance optimal approach to wealth management .” In:Quantitative Finance 17(3\), pp. 335–351\.
Das, S. and Varma, S. (2020\). “Dynamic Goals\-Based Wealth Management using Reinforcement Learning .” In:
Journal of Investment Management 18 (2\), pp. 1–20\.
Das, S. R., Ostrov, D., Radhakrishnan, A., and Srivastav, D. (2020a). “Dynamic portfolio allocation in goals\-based
wealth management .” In:Computational Management Science 17, pp. 613–640\.
Das, S. R., Ostrov, D., Radhakrishnan, A., and Srivastav, D. (2022a). “Dynamic optimization for multi\-goals wealth
management .” In:Journal of Banking \& Finance 140 (106192\).
Das, S. R., Ostrov, D. N., Casanova, A., Radhakrishnan, A., and Srivastav, D. (2020b). “Combining Investment and
Tax Strategies for Optimizing Lifetime Solvency under Uncertain Returns and Mortality .” In:SSRN e\-Print .
Das, S. R., Ostrov, D. N., Casanova, A., Radhakrishnan, A., and Srivastav, D. (2022b). “Optimal Goals\-Based
Investment Strategies For Switching Between Bull and Bear Markets .” In:The Journal of Wealth Management
24(4\), pp. 8–36\.
Das, S. R. and Ross, G. (2021\). “The Role of Options in Goals\-Based Wealth Management .” In:SSRN e\-Print .
de Carvalho, M. and Rua, A. (2017\). “Real\-time nowcasting the US output gap: Singular spectrum analysis at
work.” In:International Journal of Forecasting 33(1\), pp. 185–198\.
De La Pena, J. I., Fernandez\-Ramos, M. C., and Garayeta, A. (2021\). “Cost\-Free LTC Model Incorporated into
Private Pension Schemes .” In:International Journal of Environmental Research and Public Health 18(5\) (2268\).
de Mendonça, H. F., Garcia, P. M., and Vicente, J. V. M. (2021\). “Rationality and anchoring of inflation expecta\-
tions: An assessment from survey\-based and market\-based measures .” In:Journal of Forecasting 40(6\), pp. 1027–
1053\.
de Villiers, J. U. and Roux, E.\-M. (2019\). “Reframing the Retirement Saving Challenge: Getting to a Sustainable
Lifestyle Level .” In:Journal of Financial Counseling and Planning 30(2\), pp. 277–288\.
Deelstra, G., Devolder, P., and Melis, R. (2021\). “Optimal annuitisation in a deterministic financial environment .”
In:Decisions in Economics and Finance 44(1\), pp. 161–175\.
Dehm, C. (2020\). “Stochastic mortality : modelling and optimal investment .” PhD thesis. University of Ulm.
DeJong, J. C. and Robinson, J. H. (2022\). “A Case Study in Sequence Risk: A 20\-Year Retrospective on the Impact
of the 2000\-2002 and 2007\-2009 Bear Markets on Retirement Nest Egg Sustainability .” In:The Journal of Wealth
Management 24(4\), pp. 37–68\.
del Carmen Valls Martı́nez, M., Santos\-Jaén, J. M., Amin, F.\-u., and Martı́n\-Cervantes, P. A. (2021\). “Pensions,
Ageing and Social Security Research: Literature Review and Global Trends .” In:Mathematics 9(24\), p. 3258\.
DeLibero, R. and Pfau, W. D. (2017\). “Life Insurance as a Retirement Income Tool .” In:SSRN e\-Print .
Delong, L. and Chen, A. (2016\). “Asset allocation, sustainable withdrawal, longevity risk and non\-exponential
discounting .” In:Insurance: Mathematics and Economics 71, pp. 342–352\.
Dempster, M. A. H., Kloppers, D., Medova, E., Osmolovsky, I., and Ustinov, P. (2016\). “Lifecycle Goal Achievement
or Portfolio Volatility Reduction? ” In:The Journal of Portfolio Management 42(2\), pp. 99–117\.
Dempster, M. A. H. and Medova, E. A. (2011\). “Asset Liability Management for Individual Households .” In:British
Actuarial Journal 16(2\).
Diamond, S., Boyd, S., Greenberg, D., Kochenderfer, M., and Ang, A. (2021\). “Optimal Claiming of Social Security
Benefits .” In:SSRN e\-Print .
Dickson, J. M., Bruno, M. A., and Wong, B. C. (2018\). A ”BETR” approach to Roth conversions . Tech. rep.
Vanguard.
DiJoseph, M. A. (2020\). Spending guidelines to help ease retirees’ market worries . Tech. rep. Vanguard.
131DiLellio, J. and Ostrov, D. N. (2019\). “Constructing Tax Efficient Withdrawal Strategies for Retirees with Tradi\-
tional 401(k)/IRAs, Roth 401(k)/IRAs, and Taxable Accounts .” In:SSRN e\-Print .
Dillschneider, Y., Maurer, R., and Schober, P. (2020\). “Dynamic Portfolio Choice with Annuities When the Interest
Rate Is Stochastic .” In:SSRN e\-Print .
Ding, G. and Marazzina, D. (2021\). “Sensitivity of Optimal Retirement Problem to Liquidity Constraints .” In:arXiv
e\-Print .
Ding, L., Ahmed, S., and Shapiro, A. (2020\). “A Python package for multi\-stage stochastic programming .” In:
Optimization Online e\-Print .
Ding, Y., Li, Y., and Song, R. (2022\). “Statistical Learning for Individualized Asset Allocation.” In: arXiv e\-Print .
Diris, B., Palm, F., and Schotman, P. (2015\). “Long\-Term Strategic Asset Allocation: An Out\-of\-Sample Evaluation .”
In:Management Science 61(9\), pp. 2185–2202\.
Dixon, M. and Polson, N. (2020\). “Deep Fundamental Factor Models .” In:SIAM Journal on Financial Mathematics
11(3\), SC–26–SC–37\.
Dixon, M. F., Halperin, I., and Bilokon, P. (2020\). Machine Learning in Finance: from theory to practice . Springer
International Publishing. 548 pp.
Dixon, M. F. and Halperin, I. (2021\). “Goal\-based wealth management with generative reinforcement learning .” In:
Risk (Cutting edge) .
Dong, B., Xu, W., Sevic, A., and Sevic, Z. (2020\). “Efficient willow tree method for variable annuities valuation
and risk management .” In:International Review of Financial Analysis 68, p. 101429\.
Dong, X., Li, Y., Rapach, D., and Zhou, G. (2022a). “Anomalies and the expected market return .” In:Journal of
Finance 27(1\), pp. 639–681\.
Dong, Z.\-L., Zhu, M.\-X., and Xu, F.\-M. (2022b). “Robo\-advisor using closed\-form solutions for investors’ risk
preferences .” In:Applied Economics Letters .
Donnelly, C. and Bernhardt, T. (2018\). Pension decumulation strategies: a state\-of\-the\-art report . Tech. rep. Heriot
Watt University.
Donnelly, C., Khemka, G., and Lim, W. (2022\). “Investing for retirement: Terminal wealth constraints or a desired
wealth target? ” In:European Financial Management .
Drew, M. E., Walk, A. N., West, J., and Cameron, J. (2014\). “Improving retirement adequacy through asset class
prioritization .” In:Journal of Financial Services Marketing 19(4\), pp. 291–303\.
Drew, M. E., Walk, A. N., and West, J. (2015\). “Conditional Allocations to Real Estate: An Antidote to Sequencing
Risk in Defined Contribution Retirement Plans .” In:The Journal of Portfolio Management 41(6\), pp. 82–95\.
Drew, M. E., Walk, A. N., and West, J. M. (2016\). “Withdrawal Capacity in the Face of Expected and Unexpected
Health and Aged\-Care Expenses During Retirement .” In:The Journal of Retirement 3(3\), pp. 77–94\.
Drew, M. E. and West, J. M. (2021\). “Retirement Income Sufficiency through Personalised Glidepaths .” In:Financial
Analysts Journal 77(2\), pp. 5–20\.
Dreyer, A. and Pogorelova, L. (2018\). “The Effect of Income\-Dependent Mortality on Withdrawal Strategies .” In:
The Journal of Retirement 6(1\), pp. 70–81\.
Du, Y. (2021\). “Essays on Portfolio Choice and Health over the Life Cycle .” PhD thesis. Temple University.
Duffy, S., Finke, M. S., and Blanchett, D. (2021\). “The Value of Delayed Social Security Claiming for Higher\-Earning
Women .” In:SSRN e\-Print .
Dunham, L. M. and Washer, K. M. (2020\). “Using Life Tables for Retirement Planning .” In:The Journal of Wealth
Management 23(3\), pp. 28–36\.
Dziwisch, A., Krahnhof, P., and Zureck, A. (2021\). “Empirical determination of sustainable withdrawal rates consid\-
ering historical yields and inflation rates in Germany .” In:Zeitschrift fur die gesamte Versicherungswissenschaft
110, pp. 117–132\.
Elkins, K. (2019\). Stanford analyzed 292 retirement strategies to determine the best one – here’s how it works .
Tech. rep. CNBC.
Elnekave, R. (2007\). “The mathematics of savings and retirement planning .” In:The Journal of Wealth Management
10(3\), pp. 87–92\.
Envestnet Research (2020\). Capital Sigma: The Advisor Advantage . Tech. rep. Envestnet.
Erdemlioglu, D. and Joliet, R. (2019\). “Long\-term asset allocation, risk tolerance and market sentiment .” In:Journal
of International Financial Markets, Institutions and Money 62, pp. 1–19\.
Eschenbach, T. G. and Lewis, N. A. (2019\). “Risk, standard deviation, and expected value: when should an individual
start social security? ” In:The Engineering Economist 64(1\), pp. 24–39\.
132Estrada, J. (2014\). “The Glidepath Illusion: An International Perspective .” In:The Journal of Portfolio Management
40(2\), pp. 52–64\.
Estrada, J. (2016\). “The Retirement Glidepath: An International Perspective .” In:The Journal of Investing 25(2\),
pp. 28–54\.
Estrada, J. (2017a). “Maximum Withdrawal Rates: A Novel and Useful Tool .” In:Journal of Applied Corporate
Finance 29(4\), pp. 134–137\.
Estrada, J. (2017b). “Refining the Failure Rate .” In:The Journal of Retirement 4(3\), pp. 63–76\.
Estrada, J. (2017c). “Replacing the Failure Rate: A Downside Risk Perspective .” In:SSRN e\-Print .
Estrada, J. (2018a). “From Failure to Success: Replacing the Failure Rate .” In:The Journal of Wealth Management
20(4\), pp. 9–21\.
Estrada, J. (2018b). “Maximum withdrawal rates: an empirical and global perspective .” In:The Journal of Retire\-
ment 5(3\), pp. 57–71\.
Estrada, J. (2019\). “Managing to target: dynamic adjustments for accumulation strategies .” In:SSRN e\-Print .
Estrada, J. (2020a). “Retirement Planning: From Z to A .” In:The Journal of Retirement 88(22\), pp. 8–22\.
Estrada, J. (2020b). “Sequence Risk: Is It Really a Big Deal? ” In:SSRN e\-Print .
Estrada, J. (2020c). “Target\-Date Funds, Glidepaths, and Risk Aversion .” In:SSRN e\-Print .
Estrada, J. (2020d). “Target\-Date Funds, Glidepaths, and Risk Aversion .” In:The Journal of Wealth Management
23(3\), pp. 50–60\.
Estrada, J. (2021a). “Sequence Risk: Is It Really a Big Deal? ” In:The Journal of Investing 30(6\), pp. 47–69\.
Estrada, J. (2021b). “The Gain\-Pain Index: Asset Allocation for Individual (And Other?) Investors .” In:SSRN
e\-Print .
Estrada, J. (2021c). “The Sustainability of (Global) Withdrawal Strategies .” In:Journal of Financial Planning
34(11\), pp. 82–98\.
Estrada, J. and Kritzman, M. (2018\). “Evaluating Retirement Strategies: A Utility\-Based Approach .” In:SSRN
e\-Print .
Estrada, J. and Kritzman, M. (2019\). “Toward Determining the Optimal Investment Strategy for Retirement .” In:
The Journal of Retirement 7(1\), pp. 35–42\.
Fabozzi, F. J., Fabozzi, F. A., Lopez de Prado, M., and Stoyanov, S. (2021\). Asset Management: Tools and Issues .
World Scientific. 516 pp.
Fabozzi, F. J. and Lopez de Prado, M. (2018\). “Being Honest in Backtest Reporting: A Template for Disclosing
Multiple Tests .” In:The Journal of Portfolio Management 45(1\), pp. 141–147\.
Fan, J., Weng, H., and Zhou, Y. (2021\). “Optimal estimation of functionals of high\-dimensional mean and covariance
matrix .” In:arXiv e\-Print .
Fan, Y.\-A., Murray, S., and Pittman, S. (2013\). “Optimizing retirement income: an adaptive approach based on
assets and liabilities .” In:The Journal of Retirement 1(1\), pp. 124–135\.
Faria, M. C. (2021\). “An Examination of Target Date Fund Glidepath Construction .” In:SSRN e\-Print .
Fellowes, M., Fichtner, J. J., Plews, L., and Whitman, K. (2019\). The Retirement Solution Hiding in Plain Sight:
How Much Retirees Would Gain by Improving Social Security Decisions . Tech. rep. Capital One Investing.
Feng, R. and Jing, X. (2017\). “Analytical valuation and hedging of variable annuity guaranteed lifetime withdrawal
benefits .” In:Insurance: Mathematics and Economics 72, pp. 36–48\.
Fichtner, J. J. and Seligman, J. S. (2018\). “Retirement Saving and Decumulation in a Persistent Low\-Return
Environment .” In:How Persistent Low Returns Will Shape Saving and Retirement . Oxford University Press.
Fidelity Research (2019\). Why work with a financial advisor . Tech. rep. Fidelity.
Finefrock, C. J., Gradisher, S. M., and Nitz, C. M. (2015\). “Long\-Term Care Insurance: Comparisons for Determining
the Best Options for Clients .” In:Journal of Financial Planning 38(2\), pp. 36–43\.
Finke, M. (2019\). Bill Sharpe Seeks a Better Retirement Income Solution . Tech. rep. ThinkAdvisor.
Finke, M. and Pfau, W. (2015\). “Reduce Retirement Costs with Deferred Income Annuities Purchased before
Retirement .” In:Journal of Financial Planning 28(7\), pp. 40–49\.
Finke, M. S. and Blanchett, D. (2016\). “An Overview of Retirement Income Strategies .” In:Journal of Investment
Consulting 17(1\), pp. 22–30\.
Fisch, J. E. and Turner, J. A. (2018\). “Making a Complex Investment Problem Less Difficult:Robo Target\-Date
Funds .” In:The Journal of Retirement 5(4\), pp. 40–45\.
Fonseca, R., Michaud, P.\-C., Galama, T., and Kapteyn, A. (2021\). “Accounting for the Rise of Health Spending
and Longevity .” In:Journal of the European Economic Association 19(1\), pp. 536–579\.
133Forsyth, P. (2021\). “Two stage decumulation strategies for DC plan investors .” In:International Journal of Theo\-
retical and Applied Finance 24(01\) (2150007\).
Forsyth, P., Vetzal, K. R., and Westmacott, G. (2017a). “Target Wealth: The Evolution of Target Date Funds .” In:
SSRN e\-Print .
Forsyth, P., Vetzal, K. R., and Westmacott, G. (2018\). “Management of Withdrawal Risk Through Optimal Life
Cycle Asset Allocation .” In:SSRN e\-Print .
Forsyth, P. A. (2022a). “A Stochastic Control Approach to Defined Contribution Plan Decumulation: ”The Nastiest,
Hardest Problem in Finance” .” In:North American Actuarial Journal 26(2\), pp. 227–251\.
Forsyth, P. A. (2022b). “Short term decumulation strategies for underspending retirees .” In:Insurance: Mathematics
and Economics 102, pp. 56–74\.
Forsyth, P. A., Li, Y., and Vetzal, K. R. (2017b). “Are target date funds dinosaurs? Failure to adapt can lead to
extinction .” In:arXiv e\-Print .
Forsyth, P. A. and Vetzal, K. R. (2019\). “Optimal asset allocation for retirement saving: deterministic vs. time
consistent adaptive strategies .” In:Applied Mathematical Finance 26(1\), pp. 1–37\.
Forsyth, P. A., Vetzal, K. R., and Westmacott, G. (2019\). “Management of Portfolio Depletion Risk through Optimal
Life Cycle Asset Allocation .” In:North American Actuarial Journal 23(3\), pp. 447–468\.
Forsyth, P. A., Vetzal, K. R., and Westmacott, G. (2020\). “Optimal Asset Allocation for DC Pension Decumulation
with a Variable Spending Rule .” In:ASTIN Bulletin 50(2\), pp. 419–447\.
Forsyth, P. A., Vetzal, K. R., and Westmacott, G. (2021\). “Optimal control of the decumulation of a retirement
portfolio with variable spending and dynamic asset allocation .” In:ASTIN Bulletin 51(3\), pp. 905–938\.
Fox, S. (2020\). “Linking metrics to objectives: retirement saving, spending, and active management .” In:The Journal
of Retirement 7(3\), pp. 6–29\.
Frank, L. R. and Brayman, S. (2016\). “Combining Stochastic Simulations and Actuarial Withdrawals into One
Model .” In:Journal of Financial Planning 29(11\), pp. 44–53\.
Frank, L. R., Mitchell, J. B., and Blanchett, D. M. (2012\). “An Age\-Based, Three\-Dimensional Distribution Model
Incorporating Sequence and Longevity Risks .” In:Journal of Financial Planning 25(3\).
Franklin, M. B. (2021\). Maximizing Social Security Retirement Benefits . Tech. rep. InvestmentNews.
Fraser, S. P. and Payne, B. C. (2018\). “Bond Tents: Reshaping the Equity Glide Slope at the End of Wealth
Accumulation .” In:The Journal of Wealth Management 21(2\), pp. 27–38\.
French, E. and Jones, J. B. (2017\). “Health, Health Insurance, and Retirement: A Survey .” In:Annual Review of
Economics 9(1\), pp. 383–409\.
Friedenthal, M. (2020\). “The Third Generation of Financial Planning .” In:Advisor Perspectives .
Fuino, M. and Wagner, J. (2018\). “Long\-term care models and dependence probability tables by acuity level: New
empirical evidence from Switzerland .” In:Insurance: Mathematics and Economics 81, pp. 51–70\.
Fullmer, R. K. (2009\). “A Framework for Portfolio Decumulation .” In:Journal of Investment Consulting 10(1\),
pp. 63–71\.
Fullmer, R. K. (2012\). “Modern Portfolio Decumulation A New Strategy for Managing Retirement Income .” In:
Someday Rich: Planning for Sustainable Tomorrows Today . Wiley, pp. 249–271\.
Fullmer, R. K. and Tzitzouris, J. A. (2014\). “Evaluation of Target\-Date Glide Paths withinDefined Contribution
Plans.” In:The Journal of Retirement 1(4\), pp. 75–94\.
Fulton, C. and Hubrich, K. (2021\). “Forecasting US Inflation in Real Time .” In:Econometrics 9(4\), p. 36\.
Gabudean, R., Gomes, F., Michaelides, A., and Zhang, Y. (2021\). “On Optimal Allocations of Target\-Date Funds .”
In:The Journal of Retirement 9(2\), pp. 58–79\.
Gabudean, R. C. and Weiss, R. A. (2019\). “How to Evaluate Target\-Date Funds: A Practical Guide .” In:The
Journal of Retirement 6(4\), pp. 68–81\.
Gan, G. (2013\). “Application of data clustering and machine learning in variable annuity valuation .” In:Insurance:
Mathematics and Economics 53(3\), pp. 795–801\.
Gao, X. and Sun, L. (2021\). “Modeling retirees’ investment behaviors in the presence of health expenditure risk
and financial crisis risk .” In:Economic Modelling 94, pp. 442–454\.
Gard, R. and Gremm, M. (2018\). “Two Measures of Financial Risk Tolerance from Questionnaire Data .” In:SSRN
e\-Print .
Ge, W. (2019a). “Optimal Glide Path Selection for Low\-Volatility Assets .” In:The Journal of Index Investing 10(3\),
pp. 70–84\.
134Ge, W. (2019b). “Utilizing Low\-Volatility Assets To Mitigate Sequence Risk In Retirement Investing .” In:The
Journal of Investing 28(5\), pp. 85–100\.
Geisler, G., Harden, B., and Hulse, D. (2021\). “A Comparison of the Tax Efficiency of Decumulation Strategies .”
In:Journal of Financial Planning 34(3\), pp. 72–89\.
Geisler, G. and Hulse, D. (2016\). “The Taxation of Social Security Benefits and Planning Implications .” In:Journal
of Financial Planning 29(5\), pp. 52–63\.
Gemmo, I., Rogalla, R., and Weinert, J.\-H. (2020\). “Optimal portfolio choice with tontines under systematic
longevity risk .” In:Annals of Actuarial Science 14(2\), pp. 302–315\.
Ghilarducci, T., Radpour, S., and Webb, A. (2019\). “New evidence on the effect of economic shocks on retirement
plan withdrawals .” In:The Journal of Retirement 6(4\), pp. 7–19\.
Glickman, M. M. and Hermes, S. (2015\). “Why Retirees Claim Social Security at 62 and How It Affects Their
Retirement Income: Evidence from the Health and Retirement Study .” In:The Journal of Retirement 2(3\),
pp. 25–39\.
Goldberg, L. R., Cai, T., and Hand, P. (2021\). “Tax\-Rate Arbitrage: Realization of Long\-Term Gains to Enable
Short\-Term Loss Harvesting .” In:SSRN e\-Print .
Goldman Sachs Asset Management Research (2021\). Retirement Realities: Time For Change: Retirement Survey \&
Insights Report 2021 . Tech. rep. Goldman Sachs Asset Management.
Goldstein, B. (2018\). “The glide path less traveled: A critical examination of assumptions, outcomes, and glide path
specification .” In:SSRN e\-Print .
Goodman, B. and Richardson, D. P. (2019\). “Achieving Retirement Income Security: A Comparison of Guaranteed
Lifetime Withdrawal Benefit, Systematic Withdrawal and Partial Variable Annuity Strategies .” In:SSRN e\-
Print.
Grable, J. E., Lyons, A. C., and Heo, W. (2019\). “A test of traditional and psychometric relative risk tolerance
measures on household financial risk taking .” In:Finance Research Letters 30, pp. 8–13\.
Grealish, A. and Kolm, P. N. (2021a). “Robo\-Advisors Today and Tomorrow: Investment Advice Is Just an App
Away.” In:The Journal of Wealth Management 24(3\), pp. 144–155\.
Grealish, A. and Kolm, P. N. (2021b). “Robo\-Advisory: From Investing Principles and Algorithms to Future De\-
velopments .” In:SSRN e\-Print .
Greiner, S. P. and Stoyanov, S. V. (2019\). “Portfolio scoring by expected risk premium .” In:The Journal of Portfolio
Management 45(4\), pp. 83–90\.
Grennon, T. (2015\). “A Dynamic Asset Allocation Approach for Selecting a 401K QDIA .” In:SSRN e\-Print .
Grennon, T. (2016\). “A Dynamic Approach to Retirement Income .” In:SSRN e\-Print .
Gudkov, N., Ignatieva, K., and Ziveyi, J. (2019\). “Pricing of guaranteed minimum withdrawal benefits in variable
annuities under stochastic volatility, stochastic interest rates and stochastic mortality via the componentwise
splitting method .” In:Quantitative Finance 19(3\), pp. 501–518\.
Guidolin, M., Hansen, E., and Lozano\-Banda, M. (2018\). “Portfolio performance of linear SDF models: an out\-of\-
sample assessment .” In:Quantitative Finance 18(8\), pp. 1425–1436\.
Guijarro\-Ordonez, J., Pelger, M., and Zanotti, G. (2021\). “Deep Learning Statistical Arbitrage .” In:SSRN e\-Print .
Guo, D. (2019\). “A Statistical Response to Challenges in Vast Portfolio Selection .” PhD thesis. University of
Waterloo.
Guo, D., Boyle, P. P., Weng, C., and Wirjanto, T. S. (2019\). “When Does The 1/N Rule Work? ” In:SSRN e\-Print .
Gupta, K. (2020\). “Optimal investment and consumption strategy for a retiree under stochastic force of mortality .”
MA thesis. Simon Fraser University.
Gurdogan, H. and Kercheval, A. (2021\). “Multi Anchor Point Shrinkage for the Sample Covariance Matrix (Extended
Version).” In: arXiv e\-Print .
Habib, F., Huaxiong, H., Mauskopf, A., Nikolic, B., and Salisbury, T. S. (2018\). “Optimal allocation to deferred
income annuities .” In:SSRN e\-Print .
Habib, F., Huaxiong, H., and Milevsky, M. A. (2017\). “Approximate solutions to retirement spending problems and
the optimality of ruin .” In:SSRN e\-Print .
Hagelstein, P., Lackner, I., Otto, J., Perona, A., and Piziak, R. (2019a). “Fixed and Dynamic Asset Allocation in
the Accumulation Phase .” In:Journal of Finance and Investment Analysis 8(1\), pp. 1–12\.
Hagelstein, P., Lackner, I., Otto, J., Perona, A., and Piziak, R. (2019b). “Markowitz Portfolios with Graham Bands
in the Accumulation Phase .” In:The Journal of Wealth Management 22(3\), pp. 41–48\.
135Halen, N., Faust, K., and Taylor, T. (2020\). “Understanding the True Cost of Health Care in Retirement .” In:
Retirement Management Journal .
Haley, M. R. (2017\). “K\-fold cross validation performance comparisons of six naive portfolio selection rules: how
naive can you be and still have successful out\-of\-sample portfolio performance? ” In:Annals of Finance 13,
pp. 341–353\.
Han, N.\-w. and Hung, M.\-w. (2012\). “Optimal asset allocation for DC pension plans under inflation .” In:Insurance:
Mathematics and Economics 51(1\), pp. 172–181\.
Hanna, S. and Kim, K. T. (2017\). “Treatment of Inflation in Retirement Planning Calculations: An Improved
Method .” In:Journal of Financial Planning 30(1\), pp. 44–53\.
Hao, H. (2019\). “A Regime\-Aware Agent\-Based Framework for Financial Planning .” PhD thesis. Princeton Univer\-
sity.
Harbron, G. L., Bloore, W., and Zorn, J. (2019\). Withdrawal order: making the most of retirement assets . Tech. rep.
Vanguard.
Harris, M. (2019\). “Should a Retiree File for Social Security at 62 or 70? ” In:The Journal of Retirement 7(2\),
pp. 51–59\.
Harvey, C. R., Liu, Y., and Saretto, A. (2020\). “An Evaluation of Alternative Multiple Testing Methods for Finance
Applications .” In:The Review of Asset Pricing Studies 10(2\), pp. 199–248\.
Hejazi, S. A., Jackson, K. R., and Gan, G. (2017\). “A Spatial Interpolation Framework for Efficient Valuation of
Large Portfolios of Variable Annuities .” In:arXiv e\-Print .
Hens, T., Schenk\-Hoppe, K. R., and Woesthoff, M.\-H. (2020\). “Escaping the backtesting illusion .” In:The Journal
of Portfolio Management 46(4\), pp. 81–93\.
Hicks, W. (2019\). How Much Is An Adviser Worth? Tech. rep. Sapling Wealth Management.
Ho, J., Tumkaya, T., Aryal, S., Choi, H., and Claridge\-Chang, A. (2019\). “Moving beyond P values: data analysis
with estimation graphics .” In:Nature Methods 16(7\), pp. 565–566\.
Hofmann, P. (2021a). “Quantifying the Tax Benefit of Retirement Accounts for Better Client Decisions (Part 1\) .”
In:Advisor Perspectives .
Hofmann, P. (2021b). “Quantifying the Tax Benefit of Retirement Accounts for Better Client Decisions (Part 2\) .”
In:Advisor Perspectives .
Homescu, C. (2014\). “Many risks, one (optimal) portfolio .” In:SSRN e\-Print .
Homescu, C. (2015\). “Better Investing Through Factors, Regimes and Sensitivity Analysis .” In:SSRN e\-Print .
Hopkins, J. P., Ragatz, J. A., and Galli, C. (2016\). “Ethical issues in retirement income planning: an advisor
perspective .” In:The Journal of Retirement 4(1\), pp. 112–130\.
Horan, S. (2005\). Tax\-Advantaged Savings Accounts and Tax\-Efficient Wealth Accumulation . Tech. rep. CFA Insti\-
tute Research Foundation.
Horneff, V., Maurer, R., and Mitchell, O. (2017\). “How Persistent Low Expected Returns Alter Optimal Life Cycle
Saving, Investment, and Retirement Behavior .” In:SSRN e\-Print .
Horneff, V., Maurer, R., and Mitchell, O. S. (2018a). “How Persistent Low Expected Returns Alter Optimal Life
Cycle Saving, Investment, and Retirement Behavior .” In:How Persistent Low Returns Will Shape Saving and
Retirement . Oxford University Press.
Horneff, V., Maurer, R., and Mitchell, O. S. (2018b). “Putting the Pension Back in 401(k) Retirement Plans:
Optimal versus Default Longevity Income Annuities .” In:SSRN e\-Print .
Horneff, V., Maurer, R., and Mitchell, O. S. (2021\). “Do Required Minimum Distribution 401(K) Rules Matter,
and for Whom? Insights from a Lifecycle Model .” In:SSRN e\-Print .
Horneff, W. J., Maurer, R. H., Mitchell, O. S., and Dus, I. (2008\). “Following the rules: Integrating asset allocation
and annuitization in retirement portfolios .” In:Insurance: Mathematics and Economics 42(1\), pp. 396–408\.
Hosseini, R., Kopecky, K. A., and Zhao, K. (2022\). “The evolution of health over the life cycle .” In:Review of
Economic Dynamics 45, pp. 237–253\.
Hou, W. (2020\). HowAccurateAreRetirees’AssessmentsofTheirRetirementRisk? Tech. rep. Center for Retirement
Research at Boston College.
Hsu, Y.\-C., Lin, H.\-W., and Vincent, K. (2017\). Do Cross\-Sectional Stock Return Predictors Pass the Test without
Data\-Snooping Bias? Tech. rep. Institute of Economics Academia Sinica.
Hsu, P.\-H., Han, Q., Wu, W., and Cao, Z. (2018\). “Asset allocation strategies, data snooping, and the 1 / N rule .”
In:Journal of Banking \& Finance 97, pp. 257–269\.
136Hu, W. (2021\). “A Comprehensive Study of Guaranteed Minimum Maturity Benefit and Guaranteed Minimum
Death Benefit under Regime\-switching Models .” PhD thesis. North Carolina State University.
Huang, H. and Milevsky, M. A. (2016\). “Longevity risk and retirement income tax efficiency: A location spending
rate puzzle .” In:Insurance: Mathematics and Economics 71, pp. 50–62\.
Huang, M. and Yu, S. (2020\). “A new procedure for resampled portfolio with shrinkaged covariance matrix .” In:
Journal of Applied Statistics 47(44\), pp. 642–652\.
Huang, N., Li, J., and Ross, A. (2020\). Housing Wealth Shocks, Home Equity Withdrawal, and the Claiming of Social
Security Retirement Benefits . Tech. rep. Centre For Research On Successful Ageing, Singapore Management
University.
Huaxiong, H., Milevsky, M. A., and Salisbury, T. S. (2017\). “Retirement Spending and Biological Age .” In:SSRN
e\-Print .
Hubble, A. and Grable, J. E. (2019\). “The efficient frontuzzle: what investment risk profiling still fails to solve .” In:
The Journal of Investing 28(6\), pp. 55–72\.
Hugonnier, J., Pelgrin, F., and St\-Amour, P. (2017\). “Closing down the shop: optimal health and wealth dynamics
near the end of life .” In:SSRN e\-Print .
Hunt, A. and Blake, D. P. (2020\). “Basis Risk and Pensions Schemes: A Relative Modelling Approach. ” In:SSRN
e\-Print .
Hwang, I., Xu, S., and In, F. (2018\). “Naive versus optimal diversification: Tail risk and performance .” In:European
Journal of Operational Research 265(1\), pp. 372–388\.
Hyams, S. D., Smith, A. E., Squirrell, C. M., Warren, G. J., Warren, O. H., and Willetts, P. J. (2020\). “Saving for
retirement: rules of thumb .” In:British Actuarial Journal 25 (e7\).
Iannarone, N. G. (2018\). “Rethinking automated investment adviser disclosure .” In:SSRN e\-Print .
Idzorek, T., Stempien, J., and Voris, N. (2013\). “Bait and Switch: Glide Path Instability .” In:The Journal of
Investing 22(1\), pp. 74–82\.
Ielpo, F., Merhy, C., and Simon, G. (2017\). Engineering Investment Process: Making Value Creation Repeatable .
Elsevier. 430 pp.
Ilmanen, A. and Rauseo, M. (2018\). “Intelligent Risk Taking .” In:How Persistent Low Returns Will Shape Saving
and Retirement . Oxford University Press.
Irlam, G. (2020a). AI Planner .url:https://www.aiplanner.com/ .
Irlam, G. (2020b). “Lifetime Portfolio Selection: Using Machine Learning .” In:SSRN e\-Print .
Irlam, G. (2020c). “Machine learning for retirement planning .” In:The Journal of Retirement 8(1\), pp. 32–29\.
Irlam, G. (2020d). “Multi Scenario Financial Planning via Deep Reinforcement Learning AI .” In:SSRN e\-Print .
Irlam, G. and Tomlinson, J. (2014\). “Retirement Income Research: What Can We Learn from Economics? ” In:The
Journal of Retirement 1(4\), pp. 118–128\.
Iskhakov, F., Thorp, S., and Bateman, H. (2015\). “Optimal Annuity Purchases for Australian Retirees .” In:Economic
Record 91(293\), pp. 139–154\.
Israelsen, C. L. (2017\). “Retirement Portfolio Realities: The Mathematics of Survival .” In:International Journal of
Trade, Economics and Finance 8(4\), pp. 194–197\.
Jaconetti, C. M., DiJoseph, M. A., Jr., F. M. K., Pakula, D., and Lobel, H. (2020\). From assets to income: A
goals\-based approach to retirement spending . Tech. rep. Vanguard.
Jaeger, M., Krugel, S., Marinelli, D., Papenbrock, J., and Schwendner, P. (2020\). “Understanding machine learning
for diversified portfolio construction by explainable AI .” In:SSRN e\-Print .
Jang, C., Clare, A., and Owadally, I. (2022\). “Glide paths for a retirement plan with deferred annuities .” In:Journal
of Pension Economics and Finance , pp. 1–17\.
Jansen, S. (2020\). Machine Learning for Algorithmic Trading (Second Edition) . Packt Publishing. 820 pp.
Janssen, R., Kramer, B., and Boender, G. (2013\). “Life Cycle Investing: From Target\-Date to Goal\-Based Investing .”
In:The Journal of Wealth Management 16(1\), pp. 23–32\.
Jennings, W. W. and Reichenstein, W. R. (2001\). “Estimating the Value of Social Security Retirement Benefits .”
In:The Journal of Wealth Management 4(3\), pp. 14–29\.
Jeon, J., Kwak, M., and Park, K. (2021\). “Horizon effect on optimal retirement decision .” In:SSRN e\-Print .
Johnston, K., Hatem, J., Carnes, T., and Kosedag, A. (2019\). “An empirical evaluation of dynamic vs static
withdrawal strategies .” In:Managerial Finance 45(12\), pp. 1509–1525\.
JP Morgan Asset Management Research (2021\). Guide to Retirement . Tech. rep. JP Morgan Asset Management.
Jung, B. (2017\). Your advisor...worth more than 1%? Tech. rep. Russell Investments.
137Jung, J. (2020\). Estimating Markov Transition Probabilities Between Health States Using U.S. Longitudinal Survey
Data. Tech. rep. Towson University.
Jung, J. (2021\). “Estimating Markov Transition Probabilities Between Health States Using U.S. Longitudinal Survey
Data.” In:SSRN e\-Print .
Jurczenko et al. (2020\). Machine Learning for Asset Management . Ed. by E. Jurczenko. Wiley. 445 pp.
Kahler, J. R., Clarke, A., and Bruno, M. A. (2020\). HSAs: An off\-label prescription for retirement saving . Tech. rep.
Vanguard.
Kakushadze, Z. and Yu, W. (2016\). “Statistical Risk Models .” In:SSRN e\-Print .
Kakushadze, Z. and Yu, W. (2017\). “Open Source Fundamental Industry Classification .” In:MDPI Data 22 (2\).
Kakushadze, Z. and Yu, W. (2018a). “Betas, Benchmarks, and Beating the Market .” In:The Journal of Trading .
Kakushadze, Z. and Yu, W. (2018b). “Decoding stock market with quant alphas .” In:Journal of Asset Management ,
pp. 1–11\.
Kakushadze, Z. and Yu, W. (2019\). “Machine learning risk models .” In:SSRN e\-Print .
Kakushadze, Z. and Yu, W. (2020\). “Machine learning treasury yields .” In:SSRN e\-Print .
Kaplan, P. D. (2006\). “Asset Allocation with Annuities for Retirement Income Management .” In:The Journal of
Wealth Management 8(4\), pp. 27–40\.
Kazak, E. and Pohlmeier, W. (2019\). “Testing out\-of\-sample portfolio performance .” In:International Journal of
Forecasting 35(2\), pp. 540–554\.
Kazak, E. and Pohlmeier, W. (2020\). Portfolio Pretesting with Machine Learning . Tech. rep. University of Lancaster.
Kelly, D. P. and Roy, K. (2021\). Annuities: An essential slice of the retirement pie . Tech. rep. J.P. Morgan Asset
Management.
Kenigsberg, M. B., Mazumdar, P. D., and Feinschreiber, S. (2014\). “Return Sequence and Volatility: Their Impact
on Sustainable Withdrawal Rates .” In:The Journal of Retirement 2(2\), pp. 81–98\.
Khang, K. and Clarke, A. S. (2020\). Safeguarding retirement in a bear market . Tech. rep. Vanguard.
Khanna, K. and Chauhan, V. (2017\). “A study of risk profiling and investment choices of retail investor .” In:SSRN
e\-Print .
Kieren, P. and Weber, M. (2022\). “When saving is not enough – wealth decumulation in retirement .” In:Journal
of Pension Economics and Finance 21(3\), pp. 446–473\.
Kim, W. C., Kwon, D.\-G., Lee, Y., Kim, J. H., and Lin, C. (2020\). “Personalized goal\-based investing via multi\-stage
stochastic goal programming .” In:Quantitative Finance 20(3\) (3\), pp. 515–526\.
Kinniry Jr., F. M., Jaconetti, C. M., DiJoseph, M. A., Zilbering, Y., and Bennyhoff, D. G. (2016\). Putting a value
on your value: quantifying Vanguard Advisor’s Alpha . Tech. rep. Vanguard.
Kintzel, D. (2020\). “Income Sustainability in Retirement: A Case Study of the Life\-Cycle Account .” In:The Journal
of Retirement 7(3\), pp. 31–45\.
Kitces, M. (2015\). “Sequence of return risk and safe withdrawal rates .” In:Retirement Income Conference .
Kitces, M. and Richards, C. (2019\). Kitces \& Carl Ep 01: How To Value The Value Of Financial Planning .
url:https://www.kitces.com/blog/kitces\-carl\-richards\-talk\-value\-of\-financial\-planning\-
intangible/ .
Kitces, M. E. and Pfau, W. D. (2014\). “Retirement Risk, Rising Equity Glidepaths, and Valuation\-Based Asset
Allocation .” In:SSRN e\-Print .
Klement, J. (2015\). “Investor Risk Profiling: An Overview .” In:SSRN e\-Print .
Klement, J. (2018\). “Risk Profiling and Tolerance: Insights for the Private Wealth Manager .” In:ResearchFoundation
Publications of CFA Institute .
Kobor, A. and Muralidhar, A. (2020\). “Targeting Retirement Security with a Dynamic Asset Allocation Strategy .”
In:Financial Analysts Journal 76(3\), pp. 38–55\.
Kohlscheen, E. (2021\). “What does machine learning say about the drivers of inflation? ” In:SSRN e\-Print .
Koijen, R. S. J., Nijman, T. E., and Werker, B. J. M. (2011\). “Optimal Annuity Risk Management .” In:Review of
Finance 15(4\), pp. 799–833\.
Konicz, A. K., Pisinger, D., and Weissensteiner, A. (2016\). “Optimal retirement planning with a focus on single
and joint life annuities .” In:Quantitative Finance 16(2\), pp. 275–295\.
Konicz, A. K., Pisinger, D., and Weissensteiner, A. (2015\). “Optimal annuity portfolio under inflation risk .” In:
Computational Management Science 12(3\), pp. 461–488\.
Koo, B., Pantelous, A. A., and Wang, Y. (2020\). “Novel Utility\-Based Life Cycle Models to Optimize Income in
Retirement in the Presence of Heterogeneous Preferences .” In:SSRN e\-Print .
138Kopa, M., Moriggia, V., and Vitali, S. (2018\). “Individual optimal pension allocation under stochastic dominance
constraints .” In:Annals of Operations Research 260(1\-2\), pp. 255–291\.
Krasnopolsky, M. and Ashton, M. (2018\). “Why Pairing LDI with De\-Risking Glide Paths Produces Inferior Pension
Fund Outcomes .” In:The Journal of Investing 27(supplement), pp. 58–64\.
Kritzman, M. (2017\). “Target\-Date Funds: A Regime\-Based Approach .” In:The Journal of Retirement 5(1\), pp. 96–
105\.
Kritzman, M., Kinlaw, W., and Turkington, D. (2017\). A Practitioner’s Guide to Asset Allocation . Wiley. 256 pp.
Kuntz, L.\-C. (2018\). “Portfolio Strategies with Classical and Alternative Benchmarks .” PhD thesis. Georg August
University of Gottingen.
Kuselias, S., Perreault, S. J., and Shafer, M. (2021\). “The Financial and Tax Considerations of Social Security and
Early Retirement .” In:The Journal of Wealth Management .
Lai, K.\-H., Zha, D., Wang, G., Xu, J., Zhao, Y., Kumar, D., Chen, Y., Zumkhawaka, P., Wan, M., Martinez, D.,
and Hu, X. (2021\). “TODS: An Automated Time Series Outlier Detection System.” In: arXiv e\-Print .
Lalive, R., Magesan, A., and Staubli, S. (2020\). The Impact of Social Security on Pension Claiming and Retirement:
Active vs. Passive Decisions . Tech. rep. NBER.
Larson, S. (2022\). “Required Minimum Distributions as a Retirement Strategy: The Tradeoff Between RMD Volatil\-
ity and the Expected Number of Dollars Paid Out .” In:Journal of Financial Planning 35(1\), pp. 60–67\.
Larson, S. J. (2018\). “Strategy: Assessing the Impact of Required Minimum Distributions on the 4 Percent Rule .”
In:Journal of Financial Service Professionals 72(1\), pp. 55–63\.
Laster, D., Suri, A., and Vrdoljak, N. (2012\). “Systematic Withdrawal Strategies for Retirees .” In:The Journal of
Wealth Management 15(3\), pp. 36–49\.
Laster, D., Vrdoljak, N., and Suri, A. (2014\). “Pitfalls in Retirement .” In:The Journal of Retirement 1(1\), pp. 91–99\.
Laster, D., Vrdoljak, N., and Suri, A. (2016\). “Strategies for Managing Retirement Risks .” In:The Journal of
Retirement 4(1\), pp. 11–18\.
Latham, L. (2021\). Bridging the Gap Between Accumulation and Decumulation for Participants . Tech. rep. T. Rowe
Price.
Le Guenedal, T. and Roncalli, T. (2022\). Portfolio Construction with Climate Risk Measures . Tech. rep. Amundi
Asset Management.
Lefrancois, R., Mamidipudi, P., and Li, J. (2020\). “Expectation Risk: A Novel Short\-Term Risk Measure for Long\-
Term Financial Projections .” In:SSRN e\-Print .
Lettau, M. and Pelger, M. (2020\). “Factors That Fit the Time Series and Cross\-Section of Stock Returns .” In:The
Review of Financial Studies 33(5\), pp. 2274–2325\.
Levine, J. (2021\). “No Investment Fee Is Small, Long Term .” In:arXiv e\-Print .
Lewis, N. D. (2009\). “Is There a Role for Commodities in Long\-Term Wealth Accumulation? ” In:The Journal of
Wealth Management 12(2\), pp. 130–137\.
Lewis, W. C. and Caliendo, F. N. (2006\). “Tax\-Deferred Retirement Saving .” In:The Journal of Wealth Management
8(4\), pp. 12–16\.
Li, H. and Hyndman, R. J. (2021\). “Assessing mortality inequality in the U.S.: What can be said about the future? ”
In:Insurance: Mathematics and Economics 99, pp. 152–162\.
Li, H. and Shi, Y. (2021\). “Mortality Forecasting with an Age\-Coherent Sparse VAR Model .” In:Risks 9(2\), p. 35\.
Li, Y. and Forsyth, P. A. (2019\). “A data\-driven neural network approach to optimal asset allocation for target
based defined contribution pension plans .” In:Insurance: Mathematics and Economics 86, pp. 189–204\.
Li, Z., Liu, X.\-Y., Zheng, J., Wang, Z., Walid, A., and Guo, J. (2021\). “FinRL\-Podracer: High Performance and
Scalable Deep Reinforcement Learning for Quantitative Finance .” In:ACM International Conference on AI in
Finance .
Linnainmaa, J. T., Melzer, B., and Previtero, A. (2021\). “The Misguided Beliefs of Financial Advisors .” In:SSRN
e\-Print .
Liu, X.\-Y., Rui, J., Gao, J., Yang, L., Yang, H., Wang, Z., Wang, C. D., and Guo, J. (2022\). “FinRL\-Meta: A
Universe of Near\-Real Market Environments for Data\-Driven Deep Reinforcement Learning in Quantitative
Finance.” In: arXiv e\-Print .
Liu, X.\-Y., Yang, H., Gao, J., and Wang, C. (2021\). “FinRL: Deep Reinforcement Learning Framework to Automate
Trading in Quantitative Finance .” In:SSRN e\-Print .
Lobel, H., Jaconetti, C. M., and Cuff, R. (2019\). The replacement ratio: Making it personal . Tech. rep. Vanguard.
139Lohre, H., Rother, C., and Schafer, K. A. (2020\). “Hierarchical Risk Parity: Accounting for Tail Dependencies
in Multi\-asset Multi\-factor Allocations .” In:Machine Learning for Asset Management: New Developments and
Financial Applications . Ed. by E. Jurczenko. Wiley, pp. 329–368\.
Lopez de Prado, M. (2019\). “A Data Science Solution to the Multiple\-Testing Crisis in Financial Research .” In:The
Journal of Financial Data Science 1(1\), pp. 99–110\.
Lopez de Prado, M. (2020\). Machine learning for asset managers . Cambridge University Press. 190 pp.
Lopez de Prado, M. and Lewis, M. J. (2019\). “Detection of false investment strategies using unsupervised learning
methods .” In:Quantitative Finance 19(9\), pp. 1555–1565\.
Love, D. and Phelan, G. (2015\). “Hyperbolic discounting and life\-cycle portfolio choice .” In:Journal of Pension
Economics and Finance 14, pp. 492–524\.
Lozada, G. A. (2018a). Financing Retirement using U.S. Treasury Bonds: Safe Withdrawal Rates, Mean/Standard\-
Deviation Frontiers,and Endpoint\-Dependence of the Safest Maturity . Tech. rep. University of Utah.
Lozada, G. A. (2018b). Fixed income for retirement saving: TIAA traditional lessons on quality, duration, risk, and
gradual withdrawals . Tech. rep. University of Utah.
Lozada, G. A. (2020\). “Fixed income for retirement saving: TIAA traditional lessons on quality, duration, risk, and
gradual withdrawals .” In:The Journal of Retirement 7(4\), pp. 39–59\.
Lumby, J. (2017\). “Three Essays on Managing Risk in Retirement .” PhD thesis. Texas Tech University.
Lung, E., Roodt, C., Ryan, L., Warren, G. J., and Wymer, K. (2021\). “A Framework for Designing Investment
Strategies for Default Retirement Plans .” In:The Journal of Retirement 8(3\), pp. 40–60\.
Lurtz, M. R., Archuleta, K., Kothakota, M., and Jorgensen, T. J. (2021\). “A deeper dive: A mixed methods approach
to risk tolerance .” In:Financial Planning Review 4(2\) (e112\).
Lussier, J. (2019\). “Secure retirement: connecting financial theory and human behavior .” In:CFA Institute Research
Foundation .
MacDonald, B.\-J., Jones, B., Morrison, R. J., Brown, R. L., and Hardy, M. (2013\). “Research and Reality: A
Literature Review on Drawing Down Retirement Financial Savings .” In:North American Actuarial Journal
17(3\), pp. 181–215\.
MacDonald, B.\-J., Morrison, R. J., Avery, M., and Osberg, L. (2018\). “Drawing Down Retirement Savings \- Do
Pensions, Taxes and Government Transfers Matter Much for Optimal Decisions? ” In:ASTIN Bulletin 48(3\),
pp. 1277–1306\.
MacLean, L. and Zhao, Y. (2017\). “Asset Price Dynamics: Shocks and Regimes .” In:Optimal Financial Decision
Making under Uncertainty . Ed. by G. Consigli, D. Kuhn, and P. Brandimarte. Vol. 245\. Springer International
Publishing, pp. 35–53\.
Maclean, Ziemba, W. T., and Li, Y. (2005\). “Time to wealth goals in capital accumulation .” In:Quantitative Finance
5(4\), pp. 343–355\.
Mahaney, J. (2020\). Innovative Strategies to Help Maximize Social Security Benefits . Tech. rep. Prudential.
Mahayni, A. and Schneider, J. C. (2012\). “Variable annuities and the option to seek risk: Why should you diversify? ”
In:Journal of Banking and Finance 36(9\), pp. 2417–2428\.
Malavasi, M., Lozza, S. O., and Truck, S. (2021\). “Second order of stochastic dominance efficiency vs mean variance
efficiency .” In:European Journal of Operational Research 290(3\), pp. 1192–1206\.
Malhotra, M. (2012\). “A Framework for Finding an Appropriate Retirement Income Strategy .” In:Journal of
Financial Planning .
Mantilla\-Garcia, D., Martinez\-Carrasco, M., Garcia Huitron, M. E., and Muralidhar, A. (2020\). “From Defined\-
Contribution Towards Target\-Income Retirement Systems .” In:SSRN e\-Print .
Marekwica, M., Schaefer, A., and Sebastian, S. (2013\). “Life cycle asset allocation in the presence of housing and
tax\-deferred investing .” In:Journal of Economic Dynamics and Control 37(6\), pp. 1110–1125\.
Marinescu, M. (2022\). “Risk\-Based Optimal Portfolio Strategies: A Compendium .” In:SSRN e\-Print .
Markwat, T., Molenaar, R., and Rodriguez, J. C. (2016\). “Purchasing an Annuity: Now or Later? The Role of
Interest Rates .” In:Bankers, Markets and Investors (142\), pp. 4–17\.
Martel, R. and Sharon, A. (2019a). An Untimely Retirement: The Dangers of ’Sequence Risk’ for Retirees – Intro\-
ducing ”Income to Outcome” retirement framework . Tech. rep. PIMCO.
Martel, R. and Sharon, A. (2019b). Financial Advisors and Retirement: The Decumulation Dilemma . Tech. rep.
PIMCO.
Martellini, L. and Milhau, V. (2020\). Advances in Retirement Investing . Cambridge University Press. 167 pp.
140Martellini, L., Milhau, V., and Mulvey, J. (2019\). “’Flexicure’ Retirement Solutions: A Part of the Answer to the
Pension Crisis? ” In:The Journal of Portfolio Management 45(5\), pp. 136–151\.
Martellini, L., Milhau, V., and Mulvey, J. (2020\). “Securing Replacement Income with Goal\-Based Retirement
Investing Strategies .” In:The Journal of Retirement 7(4\), pp. 8–26\.
Martin, P. P. and Kintzel, D. (2016\). “A Comparison of Free Online Tools for Individuals Deciding When to Claim
Social Security Benefits .” In:SSRN e\-Print .
Martin, R. (2021\). “PyPortfolioOpt: portfolio optimization in Python .” In:Journal of Open Source Software 6(61\),
p. 3066\.
Marwood, D. and Minnen, D. (2020\). “Safely Boosting Retirement Income by Harmonizing Drawdown Paths .” In:
Journal of Financial Planning 33(11\), pp. 46–60\.
Maschner, C., Moritz, B., and Schmitz, M. (2021\). “Modern Asset Management .” In:SSRN e\-Print .
Massa, M., Moussawi, R., and Simonov, A. (2021\). “To Target a Date or Not to Target a Date? That is the Question:
The Unintended Consequences of Investing for the Long Run .” In:SSRN e\-Print .
McIndoe, C. (2020\). “A Data Driven Approach to Market Regime Classification .” MA thesis. Imperial College.
McLean, R. (2021\). “Rebalancing Frequency and Safe Withdrawal Rates .” In:Advisor Perspectives .
McQuarrie, E. F. (2022a). “When and for Whom are Roth Conversions Most Beneficial? A New Set of Guidelines,
Cautions and Caveats .” In:SSRN e\-Print .
McQuarrie, E. F. (2022b). “Will Required Minimum Distributions Exhaust My Savings and Leave Me in Penury? ”
In:SSRN e\-Print .
Medeiros, M. C., Vasconcelos, G. F. R., Veiga, A., and Zilberman, E. (2021\). “Forecasting Inflation in a Data\-Rich
Environment: The Benefits of Machine Learning Methods .” In:Journal of Business \& Economic Statistics 39,
pp. 98–119\.
Mendu, H. (2021\). “A critical review of ’optimal’ annuitization strategies .” MA thesis. University of Waterloo.
Merton, R. C. (2014\). “The Crisis in Retirement Planning .” In:Harvard Business Review .
Merton, R. C. and Muralidhar, A. (2020a). “A Six\-Component Integrated Approach to Addressing the Retirement
Funding Challenge .” In:Journal Of Investment Management 18(4\), pp. 28–54\.
Merton, R. C. and Muralidhar, A. (2020b). “Selfies: A new pension bond and currency for retirement .” In:Journal
of Financial Transformation 51\.
Meyer, W. and Reichenstein, W. (2013\). “Adding Longevity through Tax\-Efficient Withdrawal Strategies .” In:The
Journal of Wealth Management 16(1\), pp. 57–64\.
Micheli, A. and Neuman, E. (2022\). “Evidence of Crowding on Russell 3000 Reconstitution Events.” In: arXiv
e\-Print .
Milevsky, M. A. (2006\). Calculus of Retirement Income: Financial Models for Pension Annuities and Life Insurance .
Cambridge University Press.
Milevsky, M. A. (2020a). “Calibrating Gompertz in reverse: What is your longevity\-risk\-adjusted global age? ” In:
Insurance: Mathematics and Economics 92, pp. 147–161\.
Milevsky, M. A., Huang, H., and Young, V. R. (2015\). “A Glide Path for Target Date Fund Annuitization .” In:The
Journal of Retirement 3(1\), pp. 27–37\.
Milevsky, M. A. and Posner, S. E. (2014\). “Can collars reduce retirement sequencing risk? analysis of portfolio
longevity extension overlays (leo) .” In:The Journal of Retirement 1(4\), pp. 46–56\.
Milevsky, M. A., Salisbury, T. S., and Chigodaev, A. (2018\). “The implied longevity curve: How long does the
market think you are going to live? ” In:arXiv e\-Print .
Milevsky, M. A. (2018\). “Swimming with Wealthy Sharks: Longevity, Volatility and the Value of Risk Pooling .” In:
SSRN e\-Print .
Milevsky, M. A. (2020b). “Biological (and Other) Ages .” In:Retirement Income Recipes in R . Springer International
Publishing, pp. 259–279\.
Milevsky, M. A. (2020c). “Intelligent Drawdown Rates .” In:Retirement Income Recipes in R . Springer International
Publishing, pp. 209–232\.
Milevsky, M. A. (2020d). “Life Annuities: From Immediate to Deferred .” In:Retirement Income Recipes in R .
Springer International Publishing, pp. 181–208\.
Milevsky, M. A. (2020e). “Modeling Human Longevity and Life Tables .” In:Retirement Income Recipes in R .
Springer International Publishing, pp. 111–130\.
Milevsky, M. A. (2020f). “Modeling the Risk of Sequence\-of\-Returns .” In:Retirement Income Recipes in R . Springer
International Publishing, pp. 85–109\.
141Milevsky, M. A. (2020g). Retirement Income Recipes in R: From Ruin Probabilities to Intelligent Drawdowns .
Springer International Publishing. 302 pp.
Miller, A. K. (2015\). “Improving Withdrawal Rates in a Low Yield World .” In:SSRN e\-Print .
Millossovich, P., Bacinello, A. R., Olivieri, A., and Pitacco, E. (2011\). “Variable Annuities: A Unifying Valuation
Approach .” In:SSRN e\-Print .
Mislinski, J. (2021\). “How to Illustrate Planning Risks to Clients .” In:Advisor Perspectives .
Mitchell, J. B. (2009a). “A Mean\-Variance Approach to Withdrawal Rate Management: Theory and Simulation .”
In:SSRN e\-Print .
Mitchell, J. B. (2009b). “Withdrawal Rate Strategies for Retirement Portfolios: Preventive Reductions and Risk
Management .” In:SSRN e\-Print .
Mitchell, J. B. (2016\). “Migrating with Black Swans: Climate Risk and Retirement Planning .” In:The Journal of
Retirement 4(2\), pp. 24–36\.
Mitchell, J. B. and Felton, Z. S. (2015\). “Same\-Sex Couples and Sustainable Retirement Withdrawal Rates .” In:
SSRN e\-Print .
Mitchell, O. S., Clark, R., and Maurer, R. (2018\). “How Persistent Low Returns Will Shape Saving and Retirement .”
In:How Persistent Low Returns Will Shape Saving and Retirement . Oxford University Press.
Mitchell, O. S. and Utkus, S. P. (2021\). “Target\-date funds and portfolio choice in 401(k) plans .” In:Journal of
Pension Economics and Finance , pp. 1–18\.
Mitra, G. and Medova, E. (2010\). “Asset and liability management/liability\-driven investment for pension funds .”
In:Journal of Asset Management 11(2\-3\), pp. 71–72\.
Mladina, P. (2014\). “Dynamic Asset Allocation with Horizon Risk: Revisiting Glide Path Construction .” In:The
Journal of Wealth Management 16(4\), pp. 18–26\.
Mladina, P. (2016\). “Optimal Lifetime Asset Allocation with Goals\-Based, Lifecycle Glide Paths .” In:The Journal
of Wealth Management 19(1\), pp. 10–22\.
Mladina, P. (2020\). “Refining After\-Tax Return and Risk Parameters .” In:The Journal of Wealth Management
23(2\), pp. 8–17\.
Mladina, P. and Grant, C. (2019\). “Glide Paths Based on a Retirement Goal and Depleting Human Capital .” In:
The Journal of Investing 28(1\), pp. 8–16\.
Moehle, N., Kochenderfer, M. J., Boyd, S., and Ang, A. (2021\). “Tax\-Aware Portfolio Construction via Convex
Optimization .” In:arXiv e\-Print .
Moenig, T. (2021\). “It’s RILA Time: An Introduction to Registered Index\-Linked Annuities .” In:SSRN e\-Print .
Momen, O., Esfahanipour, A., and Seifi, A. (2020\). “A robust behavioral portfolio selection: model with investor
attitudes and biases .” In:Operational Research 20(1\), pp. 427–446\.
Mooney, T., Rapaka, R., and Vera, T. (2020\). “Dynamic Regime Strategy for Stress Testing and Optimizing
Institutional Investor Portfolios .” In:SSRN e\-Print .
Mulvey, J. M. and Hao, H. (2020\). “Setting Realistic Goals for Personal Retirement Planning via Micro\-Macro
Analyses .” In:The Journal of Retirement 8(2\), pp. 23–38\.
Munnell, A. H., Sanzenbacher, G., Webb, A., and Gillis, C. M. (2016\). “Are Early Claimers Making a Mistake? ”
In:SSRN e\-Print .
Munnell, A. H. and Webb, A. (2021\). “The Impact of Leakages from 401(k)s and IRAs .” In:The Journal of
Retirement 9(3\), pp. 32–54\.
Munnell, A. H., Wettstein, G., and Hou, W. (2019\). “How Best to Annuitize Defined Contribution Assets? ” In:
SSRN e\-Print .
Muralidhar, A., Shin, S. H., and Ohashi, K. (2016\). “The Most Basic Missing Instrument in Financial Markets: The
Case for Forward Starting Bonds .” In:The Journal of Investment Consulting 17(2\).
Murguia, A. and Pfau, W. D. (2021a). “A Model Approach to Selecting a Personalized Retirement Income Strategy .”
In:SSRN e\-Print .
Murguia, A. and Pfau, W. D. (2021b). “Retirement Income Beliefs and Financial Advice Seeking Behaviors .” In:
SSRN e\-Print .
Murphy, R. O., Lamas, S., and Sin, R. (2020\). “Identifying What Investors Value in a Financial Adviser: Uncovering
Opportunities and Pitfalls .” In:Journal of Financial Planning 33(7\), pp. 44–52\.
Neville, H., Draaisma, T., Funnell, B., Harvey, C. R., and Hemert, O. van (2021\). “The Best Strategies for Infla\-
tionary Times .” In:SSRN e\-Print .
142Ngai, A. and Sherris, M. (2011\). “Longevity risk management for life and variable annuities: The effectiveness of
static hedging using longevity bonds and derivatives .” In:Insurance: Mathematics and Economics 49(1\), pp. 100–
114\.
Nicolas, F. (2019\). Investment Strategies for Retirement . World Scientific. 416 pp.
Novotny, L. E. and Mansson, A. (2020\). “Finding the Optimal Withdrawal Rate on a Retirement Portfolio .” MA
thesis. Copenhagen Business School.
Owadally, I., Jang, C., and Clare, A. (2021a). “Optimal investment for a retirement plan with deferred annuities .”
In:Insurance: Mathematics and Economics 98, pp. 51–62\.
Owadally, I., Mwizere, J.\-R., Kalidas, N., Murugesu, K., and Kashif, M. (2021b). “Long\-Term Sustainable Invest\-
ment for Retirement .” In:Sustainability 13(9\), p. 5000\.
Pae, Y. and Atra, R. (2020\). “Rules of Thumb versus Industry Glide Paths; Some Bootstrapping Evidence .” In:The
Journal of Investing 29(3\), pp. 23–27\.
Pakula, D. (2020\). Guiding your clients through stormy weather: Sustainable withdrawal rates in times of crisis .
Tech. rep. Vanguard.
Paradise, T. and Kahler, J. R. (2020\). What to do with your next dollar: A quantitative framework . Tech. rep.
Vanguard.
Park, H. (2022\). “Influence of risk tolerance on long\-term investments: a Malliavin calculus approach .” In:Stochastics ,
pp. 1–32\.
Parker, F. J. (2016a). “Goal\-Based Portfolio Optimization .” In:The Journal of Wealth Management 19(3\), pp. 22–
30\.
Parker, F. J. (2016b). “Portfolio Selection in a Goal\-Based Setting .” In:The Journal of Wealth Management 19(2\),
pp. 41–46\.
Parker, F. J. (2020\). “Allocation of wealth both within and across goals: a practitioner guide .” In:The Journal of
Wealth Management 23(1\), pp. 8–21\.
Parker, F. J. (2021a). “Achieving Goals While Making an Impact: Balancing Financial Goals with Impact Investing .”
In:The Journal of Impact and ESG Investing 1(3\), pp. 27–38\.
Parker, F. J. (2021b). “Multi\-Period Goals\-Based Portfolio Optimization .” In:SSRN e\-Print .
Peijnenburg, K., Nijman, T., and Werker, B. J. M. (2017\). “Health Cost Risk: A Potential Solution To the Annuity
Puzzle .” In:The Economic Journal 127(603\), pp. 1598–1625\.
Pellerin, M. (2021\). “Investing for Retirement Income: A Comparison of Asset Allocations and Spending Strategies .”
In:SSRN e\-Print .
Pepperell, R., Greenwood, D., and Alsharman, M. (2020\). “Death or Bust? The Risk with Post\-Retirement Income
Models .” In:SSRN e\-Print .
Perrin, S. and Roncalli, T. (2020\). “Machine Learning Optimization Algorithms \& Portfolio Allocation .” In:Machine
Learning for Asset Management: New Developments and Financial Applications . Ed. by E. Jurczenko. Wiley,
pp. 261–328\.
Pfau, W. (2021\). Retirement Planning Guidebook: Navigating the Important Decisions for Retirement Success .
Retirement Researcher Media. 476 pp.
Pfau, W. D. (2015a). “Choosing a Retirement Income Strategy: A New Evaluation Framework .” In:SSRN e\-Print .
Pfau, W. D. (2015b). “How to Link Retirement Strategies to Sustainable\-Spending Rates .” In:Advisor Perspectives .
Pfau, W. D. (2015c). “Making Sense Out of Variable Spending Strategies for Retirees .” In:SSRN e\-Print .
Pfau, W. D. (2018\). “An Overview of Retirement Income Planning .” In:Journal of Financial Counseling and
Planning 29(1\), pp. 114–120\.
Pfau, W. D. (2019\). “The four approaches to managing retirement income risk .” In:SSRN e\-Print .
Pfau, W. D. and Dokken, W. (2015\). “Rethinking Retirement: Sustainable Withdrawal Rates for New Retirees in
2015\.” In:Financial Advisor Magazine .
Pfau, W. D., Tomlinson, J., and Vernon, S. (2016a). “A Portfolio Approach to Retirement Income Security .” In:
The Journal of Retirement 4(2\), pp. 11–22\.
Pfau, W. D., Tomlinson, J., and Vernon, S. (2016b). Optimizing Retirement Income Solutions in Defined Contribu\-
tion Retirement Plans: A Framework for Building Retirement Income Portfolios . Tech. rep. Stanford Center on
Longevity.
Pfau, W. D., Tomlinson, J., and Vernon, S. (2017\). Optimizing Retirement Income by Integrating Retirement Plans,
IRAs, and Home Equity: A Framework for Evaluating Retirement Income Decisions . Tech. rep. Stanford Center
on Longevity.
143Pittman, S. (2014\). “Is a Portfolio Built to Produce Yield a Sensible Retirement Income Portfolio? ” In:Journal of
Financial Planning 27(8\), pp. 52–60\.
Pittman, S. (2015\). “Use Your Client’s Funded Ratio to Simplify and Improve Retirement Planning Decisions .” In:
The Journal of Retirement 3(2\), pp. 93–104\.
Platanakis, E., Sutcliffe, C. M., and Ye, X. (2021\). “Horses for Courses: Mean\-Variance for Asset Allocation and
1/N for Stock Selection .” In:European Journal of Operational Research 288(1\), pp. 302–317\.
Podkaminer, E., Tollette, W., and Siegel, L. (2022\). “Protecting Portfolios Against Inflation .” In:The Journal of
Investing 31(2\), pp. 23–44\.
Prendergast, J. R. (2021\). “Replicating Maximum\-Yield Annuities with US Treasury Funds .” In:The Journal of
Fixed Income 30(4\), pp. 81–99\.
Pruser, J. (2021\). “Forecasting US inflation using Markov dimension switching .” In:Journal of Forecasting 40(3\),
pp. 481–499\.
Qian, W., Rolling, C. A., Cheng, G., and Yang, Y. (2022\). “Combining forecasts for universally optimal perfor\-
mance .” In:International Journal of Forecasting .
Quinn, J. F. and Cahill, K. E. (2018\). “Challenges and Opportunities of Living and Working Longer .” In:How
Persistent Low Returns Will Shape Saving and Retirement . Oxford University Press.
Rabitti, G. and Borgonovo, E. (2020\). “Is mortality or interest rate the most important risk in annuity models? A
comparison of sensitivity analysis methods .” In:Insurance: Mathematics and Economics 95, pp. 48–58\.
Radovanov, B. and Marcikic, A. (2014\). “Testing The Performance Of The Investment Portfolio Using Block Boot\-
strap Method .” In:Economic Themes 52(2\).
Rao, A. and Jelvis, T. (2022\). Foundations of Reinforcement Learning with Applications in Finance .
Raskie, S. (2017\). “Navigating Uncertainties in Accumulation and Decumulation of Retirement Portfolios .” In:
Journal of Economics and Public Finance 3(3\), p. 470\.
Rebonato, R. (2019\). “A financially justifiable and practically implementable approach to coherent stress testing .”
In:Quantitative Finance 19(5\), pp. 827–842\.
Reichenstein, W. (2006\). “After\-Tax Asset Allocation .” In:Financial Analysts Journal 62(4\), pp. 14–19\.
Reichenstein, W. (2020\). “Saving in Roth Accounts and Making Roth Conversions before Retirement in Today’s
Low Tax Rates .” In:Journal of Financial Planning .
Reichenstein, W. and Meyer, W. (2016a). “Redo Strategies: When Can You Redo a Prior Social Security Claiming
Decision? ” In:Journal of Financial Planning .
Reichenstein, W. and Meyer, W. (2016b). “Social security claiming strategies for widows and widowers .” In:The
Journal of Retirement 3(4\), pp. 77–86\.
Reichenstein, W. and Meyer, W. (2017\). “Valuing Roth Conversion and Recharacterization Options .” In:Journal
of Financial Planning 30(11\), pp. 48–56\.
Reichenstein, W. and Meyer, W. (2018\). “Understanding the Tax Torpedo and Its Implications for Various Retirees .”
In:Journal of Financial Planning 31(7\), pp. 38–45\.
Reichenstein, W. and Meyer, W. (2019a). “Medicare and Tax Planning for Higher\-Income Households .” In:The
Journal of Wealth Management 22(3\), pp. 28–40\.
Reichenstein, W. and Meyer, W. (2019b). “Optimizing Social Security Benefits Is Still Complicated .” In:The Journal
of Retirement 6(3\), pp. 69–79\.
Reichenstein, W. and Meyer, W. (2020\). “Investment implications of the rising and falling pattern of marginal tax
rates for retirees .” In:The Journal of Retirement 8(1\), pp. 53–64\.
Reichenstein, W. and Meyer, W. (2021a). “Advice for Married Couples When One Spouse Will Die Year(s) Before
the Other Spouse .” In:Journal of Financial Planning 34(1\).
Reichenstein, W. and Meyer, W. (2021b). “How Social Security Coordination Can Add Value to a Tax\-Efficient
Withdrawal Strategy .” In:The Journal of Retirement 9(2\), pp. 37–57\.
Reichenstein, W. and Meyer, W. (2021c). “Social Security Claiming Strategies for Singles and Their Implications
for Couples .” In:Journal of Financial Planning 34(5\).
Reichenstein, W. R. (2007\). “Note on Applying After\-Tax Asset Allocation .” In:The Journal of Wealth Management
10(2\), pp. 94–97\.
Reilly, C. and Byrne, A. (2018\). “Investing for Retirement in a Low Returns Environment .” In:How Persistent Low
Returns Will Shape Saving and Retirement . Oxford University Press.
Reznik, G., Alleva, B., Song, J., Sarney, M., and Olsen, A. (2020\). Analysis of Benefit Estimates Shown in the Social
Security Statement . Tech. rep. Social Security Administration.
144Rietz, R., Blumenschein, T., Crough, S., and Cohen, A. (2018\). “Analyzing Retirement Withdrawal Strategies .” In:
Preprints .
Rietz, R. J., Blumenschein, T., Crough, S., Cohen, A., and Coleman, J. (2020\). “A Simulation for Minimizing both
the Probability and the Length of Financial Ruin in Retirement .” In:SSRN e\-Print .
Rogalla, R. (2021\). “Optimal Portfolio Choice in Retirement With Participating Life Annuities .” In:North American
Actuarial Journal 25(sup1\), S182–S195\.
Roncalli, T. (2021\). “Advanced Course in Asset Management .” In:SSRN e\-Print .
Rook, C. J. (2015a). “Minimizing the Probability of Ruin in Retirement .” In:arXiv e\-Print .
Rook, C. J. (2015b). “Optimal Equity Glidepaths in Retirement .” In:SSRN e\-Print .
Rook, C. J. (2017\). “Multivariate Density Modeling for Retirement Finance .” In:arXiv e\-Print .
Root, E., Mallett, C., Zwerling, N., and Toale, T. (2013\). “Strategic Liability Management: Building a Glide Path
Strategy to Manage Interest Rate and Longevity Risks .” In:Institutional Investor Guides: Special Issues , pp. 56–
60\.
Rosenthal, D. (2018\). “Joint effect of random years of longevity and mean reversion in equity returns on the safe
withdrawal rate in retirement .” In:SSRN e\-Print .
Rossi, A. G. and Utkus, S. P. (2021\). “The Needs and Wants in Financial Advice: Human versus Robo\-advising .”
In:SSRN e\-Print .
Roux, E.\-M. and de Villiers, J. (2020\). “A simplified approach to estimate the sustainable lifestyle level for retirement
planning .” In:Investment Analysts Journal 49, pp. 232–242\.
Roy, K. and Kim\-Steiner, Y. (2019\). Three retirement spending surprises . Tech. rep. J.P. Morgan Asset Management.
Rundle, J. (2018\). “A Social Security Purchase: Is Delaying Social Security More Effective than Purchasing a
Deferred Income Annuity? ” In:The Journal of Retirement 6(1\), pp. 8–21\.
Ruthbah, U. (2020\). “The Retirement Puzzle .” In:SSRN e\-Print .
Ryack, K. (2016\). “Incorporating Financial Risk Tolerance Research into the Financial Planning Process .” In:
Journal of Financial Planning 29(10\), pp. 54–61\.
Sahm, C. (2017\). “How Much Does Risk Tolerance Change? ” In:SSRN e\-Print .
Salampasis, D., Mention, A.\-L., and Kaiser, A. O. (2019\). “Wealth Management in Times of Robo: Towards Hybrid
Human\-Machine Interactions .” In:SSRN e\-Print .
Sapra, S. and Pedersen, N. (2017\). “The Role of Long\-Maturity TIPS in Retirement Portfolios .” In:The Journal of
Retirement 4(4\), pp. 95–106\.
Sarmas, E., Xidonas, P., and Doukas, H. (2020\). Multicriteria Portfolio Construction with Python . Springer Inter\-
national Publishing.
Sato, M. (2016\). “Optimal Withdrawal Rate Under Longevity Risks: A Criterion for Life Planning after Retirement .”
In:SSRN e\-Print .
Scherer, B. and Lehner, S. (2021\). “What Drives Robo\-Advice? ” In:SSRN e\-Print .
Schumann, E. (2019\). “Backtesting .” In:SSRN e\-Print .
Scruggs, J. T. (2019\). “Asset Allocation and Withdrawal Strategies: Three Levers for Managing Retirement Out\-
comes .” In:Journal of Financial Planning .
Šestanović, T. and Arnerić, J. (2021\). “Neural network structure identification in inflation forecasting .” In:Journal
of Forecasting 40(1\), pp. 62–79\.
Sestok, B. (2021\). “Implementing Advice based on ”A Comparison of the Tax Efficiency of Decumulation Strate\-
gies”.” In:Journal of Financial Planning 34(11\).
Sexauer, S. C., Peskin, M. W., and Cassidy, D. (2015\). “Making Retirement Income Last a Lifetime .” In:Financial
Analysts Journal 71(1\), pp. 79–89\.
Seymour, A., Flint, E. J., and Chikurunhe, F. (2018\). “Dynamic portfolio management strategies: A framework for
historical analysis .” In:SSRN e\-Print .
Shang, H. L. and Haberman, S. (2020\). “Forecasting age distribution of death counts: an application to annuity
pricing .” In:Annals of Actuarial Science 14(1\), pp. 150–169\.
Sharma, A., Syrgkanis, V., Zhang, C., and Kiciman, E. (2021\). “DoWhy: Addressing Challenges in Expressing and
Validating Causal Assumptions.” In: arXiv e\-Print .
Sharpe, W. (2019\). Retirement Income Analysis with scenario matrices . Stanford University. 200 pp.
Sherwood, M. W. (2021\). “Risk Capacity Portfolio Construction .” In:The Journal of Investing 30(2\), pp. 31–52\.
Shi, X., Xu, D., and Zhang, Z. (2022\). “Deep Learning Algorithms for Hedging with Frictions.” In: arXiv e\-Print .
145Shi, Y. (2021\). “Forecasting Mortality Rates with the Adaptive Spatial Temporal Autoregressive Model .” In:Journal
of Forecasting 40(3\), pp. 528–546\.
Shoven, J. and Slavov, S. (2012\). “The Decision to Delay Social Security Benefits: Theory and Evidence .” In:SSRN
e\-Print , pp. 121–144\.
Shoven, J. B. and Sialm, C. (2004\). “Asset location in tax\-deferred and conventional savings accounts .” In:Journal
of Public Economics 88(1\-2\), pp. 23–38\.
Shoven, J. B. and Walton, D. B. (2021\). “An Analysis of the Performance of Target Date Funds .” In:The Journal
of Retirement 8(4\), pp. 43–65\.
Siebert, J., Gross, J., and Schroth, C. (2021\). “A systematic review of Python packages for time series analysis .”
In:Engineering Proceedings 5(1\) (22\).
Simos, T. E., Mourtas, S. D., and Katsikis, V. N. (2021\). “Time\-varying Black–Litterman portfolio optimization
using a bio\-inspired approach and neuronets .” In:Applied Soft Computing 112, p. 107767\.
Simsek, K. D., Jeong Kim, M., Chang Kim, W., and Mulvey, J. M. (2018\). “Optimal Longevity Risk Management
in the Retirement Stage of the Life Cycle .” In:The Journal of Retirement 5(3\), pp. 73–92\.
Siskos, C. (2021\). “What’s Your Strategy for Maximizing Your Social Security Benefits? ” In:Kiplinger .
Sivarajan, S. and De Bruijn, O. (2021\). “Risk Tolerance, Return Expectations and Other Factors Impacting Invest\-
ment Decisions .” In:The Journal of Wealth Management 23(4\).
Smith, G. and Gould, D. P. (2007\). “Measuring and controlling shortfall risk in retirement .” In:The Journal of
Investing 16(1\), pp. 82–95\.
Smith, L. (2021\). The Best Age for Social Security Retirement Benefits . Tech. rep. SmartAsset.
Sneddon, T., Bao, C., and Zhu, Z. (2015\). “Optimal Asset Liability Management for Post\-retirement stage with
Income Protection Product .” In:21st International Congress on Modelling and Simulation .
Sneddon, T., Zhu, Z., and O’Hare, C. (2016\). “Modelling defined contribution retirement outcomes: A stochastic
approach using Australia as a case study .” In:Australian Journal of Actuarial Practice 4, pp. 5–19\.
Snow, D. (2019\). “Machine learning in asset management .” In:SSRN e\-Print .
Snow, D. (2020a). “Machine Learning in Asset Management \- Part 2: Portfolio Construction \- Weight Optimization .”
In:The Journal of Financial Data Science 2 (2\), pp. 17–24\.
Snow, D. (2020b). “Machine Learning in Asset Management Part 1: Portfolio Construction Trading Strategies .” In:
The Journal of Financial Data Science 2(1\) (1\), pp. 10–23\.
Society of Actuaries Research (2017\). Deciding When to Claim Social Security . Tech. rep. Society of Actuaries.
Sornwanee, M. (2020\). “Multi\-Regime, Goal\-Based Retirement Solutions: Sensitivity Analysis and Post\-Retirement
Performance Comparison of Dynamic Strategies .” MA thesis. Princeton University.
Sosner, N., Liberman, J., and Liu, S. (2021\). “Integration of Income and Estate Tax Planning .” In:The Journal of
Wealth Management 24(1\), pp. 78–104\.
Steinorth, P. and Mitchell, O. S. (2015\). “Valuing variable annuities with guaranteed minimum lifetime withdrawal
benefits .” In:Insurance: Mathematics and Economics 64, pp. 246–258\.
Suarez, E. D. (2020\). “The perfect withdrawal amount over the historical record .” In:Financial Services Review
28(2\), pp. 96–132\.
Suarez, E. D., Suarez, A., and Walz, D. T. (2015\). “The Perfect Withdrawal Amount: A Methodology for Creating
Retirement Account Distribution Strategies .” In:Financial Services Review 24(4\).
Suhonen, A., Lennkh, M., and Perez, F. (2017\). “Quantifying Backtest Overfitting in Alternative Beta Strategies .”
In:The Journal of Portfolio Management 43 (2\), pp. 90–104\.
Sun, Q. (2019\). “Dynamic Retirement Financial Planning Model .” PhD thesis. University of Connecticut.
Sun, W., Triest, R. K., and Webb, A. (2008\). “Optimal Retirement Asset Decumulation Strategies: The Impact of
Housing Wealth .” In:Asia\-Pacific Journal of Risk and Insurance 3(1\).
Sutcliffe, C. (2015\). “Trading death: The implications of annuity replication for the annuity puzzle, arbitrage,
speculation and portfolios .” In:International Review of Financial Analysis 38, pp. 163–174\.
Swedroe, L. (2021\). “The Role of Financial Risk Tolerance in Investment Policy .” In:Advisor Perspectives .
Taljaard, B. H. and Maré, E. (2021\). “Why has the equal weight portfolio underperformed and what can we do
about it? ” In:Quantitative Finance 21(11\), pp. 1855–1868\.
Tatsat, H., Puri, S., and Lookabaugh, B. (2020\). Machine Learning and Data Science Blueprints for Finance: From
Building Trading Strategies to Robo\-Advisors Using Python . O’Reilly. 400 pp.
Tayali, S. T. (2020\). “A novel backtesting methodology for clustering in mean–variance portfolio optimization .” In:
Knowledge\-Based Systems 209, p. 106454\.
146Templin, N. (2021\). “When to Tap Social Security: The Sometimes Surprising Answer From Online Calculators .”
In:Wall Street Journal .
Tergersen, A. (2018\). “Forget the 4% Rule: Rethinking Common Retirement Beliefs .” In:Wall Street Journal .
Tertilt, M. and Scholz, P. (2018\). “To Advise, or Not to Advise Robo\-Advisors Evaluate the Risk Preferences of
Private Investors .” In:The Journal of Wealth Management 21(2\), pp. 70–84\.
Thanki, H., Karani, A., and Goyal, A. K. (2020\). “Psychological antecedents of financial risk tolerance .” In:The
Journal of Wealth Management 23(2\), pp. 36–51\.
Tharp, D. T. and Kitces, M. E. (2018\). “Life\-Cycle Earnings Curves and Safe Savings Rates .” In:The Journal of
Retirement 5(3\), pp. 109–120\.
Thompson, J. R., Feng, L., Reesor, R. M., Grace, C., and Metzler, A. (2021\). “Measuring Financial Advice: Aligning
Client Elicited and Revealed Risk .” In:SSRN e\-Print .
Thorp, S., Bateman, H., Dobrescu, L., Newell, B., and Ortmann, A. (2020\). “Flicking the switch: Simplifying
disclosure to improve retirement plan choices .” In:Journal of Banking \& Finance 121, p. 105955\.
Tian, W. and Zhu, Z. (2020\). “Optimal Investing after Retirement Under Time\-Varying Risk Capacity Constraint .”
In:arXiv e\-Print .
Tomlinson, J. (2017\). “Coping with Sequence Risk: How Variable Withdrawal and Annuitization Improve Retirement
Outcomes .” In:Advisor Perspectives .
Tomlinson, J. (2018\). “Retirement Strategies in Pictures .” In:Advisor Perspectives .
Tomlinson, J. (2020a). “New Estimates of the Need for Long\-Term Care .” In:Advisor Perspectives .
Tomlinson, J. (2020b). “The Unimportance of Asset Allocation in Retirement Planning .” In:Advisor Perspectives .
Traccucci, P., Dumontier, L., Garchery, G., and Jacot, B. (2019\). “A Triptych Approach for Reverse Stress Testing
of Complex Portfolios .” In:Risk (Cutting Edge) .
Tretiakova, I. and Yamada, M. S. (2017\). “Autonomous portfolio:a decumulation investment strategy that will get
you there .” In:The Journal of Retirement 5(2\), pp. 83–95\.
Tsai, C. C.\-L. and Cheng, E. S. (2021\). “Incorporating statistical clustering methods into mortality models to
improve forecasting performances .” In:Insurance: Mathematics and Economics 99, pp. 42–62\.
Tuck, J., Barratt, S., and Boyd, S. (2022\). “Portfolio Construction Using Stratified Models .” In:Machine Learning
in Financial Markets: A guide to contemporary practices . Ed. by A. Capponi and C.\-A. Lehalle. Cambridge
University Press.
Turvey, P. A., Basu, A. K., and Verhoeven, P. (2013\). “Embedded Tax Liabilities and Portfolio Choice .” In:The
Journal of Portfolio Management 39(3\), pp. 93–101\.
Ungolo, F., Sherris, M., and Zhou, Y. (2021\). “affine\_mortality: A Github repository for estimation, analysis, and
projection of affine mortality models .” In:SSRN e\-Print .
Valentine, K. D., Buchanan, E. M., Scofield, J. E., and Beauchamp, M. T. (2019\). “Beyond p values: utilizing
multiple methods to evaluate evidence .” In:Behaviormetrika 46(1\), pp. 121–144\.
Vamossy, D. and Skog, R. (2021\). “EmTract: Investor Emotions and Market Behavior.” In: arXiv e\-Print .
van Bilsen, S. and Bovenberg, A. L. (2020\). “The decumulation period of a personal pension with risk sharing:
investment approach versus consumption approach .” In:Journal of Pension Economics and Finance 19(2\),
pp. 262–291\.
van Bilsen, S. and Linders, D. (2019\). “Affordable and adequate annuities with stable payouts: Fantasy or reality? ”
In:Insurance: Mathematics and Economics 86, pp. 19–42\.
Van Harlow, H. V. and Brown, P. (2016a). “Market Risk, Mortality Risk, And Sustainable Retirement Asset
Allocation: A Downside Risk Perspective .” In:Journal of Investment Management 14(2\).
Van Harlow, W. (2014\). Optimal Asset Allocation in Retirement: A Downside Risk Perspective . Tech. rep. Putnam
Institute.
Van Harlow, W. and Brown, K. C. (2016b). “Improving the Outlook for a Successful Retirement: A Case for Using
Downside Hedging .” In:The Journal of Retirement 3(3\), pp. 35–50\.
Van Harlow, W. and Brown, K. C. (2017\). “Health State and the Savings Required for a Sustainable Retirement .”
In:The Journal of Retirement 4(4\), pp. 25–38\.
Van Harlow, W., Brown, K. C., and Jenks, S. E. (2020\). “The Use and Value of Financial Advice for Retirement
Planning .” In:The Journal of Retirement 7(3\), pp. 46–79\.
Vandenbroucke, J. and Fortuna, G. (2019\). “Loss Aversion Implied by a Risk\-Based Questionnaire .” In:The Journal
of Wealth Management 22(1\), pp. 39–48\.
Vanguard Research (2020\). Dynamic spending: A better way to budget in retirement . Tech. rep. Vanguard.
147Vanini, P. (2020\). “Asset Management .” In:SSRN e\-Print .
Vaughan, C. (2017\). “RMD Arbitrage: Strategies for Legally Delaying and Reducing RMDs .” In:JournalofFinancial
Planning 30(6\), pp. 49–57\.
Veres, B. (2020\). “A Comparison of Risk Tolerance Products .” In:Advisor Perspectives .
Vincent, K., Hsu, Y.\-C., and Lin, H.\-W. (2018\). “Analyzing the Performance of Multifactor Investment Strategies
under a Multiple Testing Framework .” In:The Journal of Portfolio Management 44(4\), pp. 113–126\.
Vinod, H. D. (2021\). “R Package GeneralCorr Functions for Portfolio Choice .” In:SSRN e\-Print .
Vovk, V. and Wang, R. (2020\). “True and false discoveries with e\-values .” In:arXiv e\-Print .
Vovk, V. and Wang, R. (2021\). “E\-values: Calibration, combination, and applications .” In:Annals of Statistics
49(3\), pp. 1736–1753\.
Vrdoljak, N., Laster, D., and Suri, A. (2014\). “The Role of Variable Annuities in Addressing Retirement Risks .” In:
The Journal of Retirement 2(2\), pp. 55–66\.
Walker, P., Sacks, B. H., and Sacks, S. R. (2021\). “To Reduce the Risk of Retirement Portfolio Exhaustion, Include
Home Equity as a Non\-Correlated Asset in the Portfolio .” In:Journal of Financial Planning 34(12\), pp. 82–97\.
Wallick, D. W., Berkowitz, D. B., Clarke, A. S., DiCiurcio, K. J., and Stockton, K. A. (2018\). “Getting More from
Less in Defined Benefit Plans .” In:How Persistent Low Returns Will Shape Saving and Retirement . Oxford
University Press.
Wang, J., Meric, G., Liu, Z., and Meric, I. (2011\). “The Determinants of Stock Returns in the October 9, 2007
March 9, 2009 Bear Market .” In:The Journal of Investing 20(3\), pp. 18–24\.
Waring, M. B. and Siegel, L. B. (2018\). “What Investment Risk Means to You, Illustrated Strategic Asset Allocation,
the Budget Constraint, and the Volatility of Spending During Retirement .” In:The Journal of Retirement 6(2\),
pp. 7–26\.
Warren, G. J. (2019\). “Design of Investment Options using Utility Functions: A Demonstration for Products .” In:
SSRN e\-Print .
Warshawsky, M. (2018\). “Reforming Retirement Income: Annuitization, Combination Strategies, and Required
Minimum Distributions .” In:SSRN e\-Print .
Weber, E. U. and Klement, J. (2018\). “Risk tolerance and circumstances .” In:CFA Institute Research Foundation
Briefs 4(2\).
Wiafe, O. (2015\). “Investment strategies in retirees’ decumulation phase .” PhD thesis. Queensland University of
Technology.
Wiafe, O. K., Basu, A. K., and Chen, E. T. (2020\). “Portfolio choice after retirement: Should self\-annuitisation
strategies hold more equities? ” In:Economic Analysis and Policy 65, pp. 241–255\.
Wiafe, O. K., Basu, A. K., and Chen, E.\-T. ( (2016\). “Asset Allocation in Retirement: Does Glide Path Matter? ”
In:SSRN e\-Print .
Wiafe, O. K., Basu, A. K., and Chen, E.\-T. J. (2014\). “Portfolio Strategies in Decumulation Phase: Does Lifecycling
Fail?” In:SSRN e\-Print .
Wiecki, T., Campbell, A., Lent, J., and Stauth, J. (2016\). “All That Glitters Is Not Gold: Comparing Backtest
and Out\-of\-Sample Performance on a Large Cohort of Trading Algorithms .” In:The Journal of Investing 25(3\),
pp. 69–80\.
Williams, P. D. (2021\). “Inflation Expectations in the U.S.: Linking Markets, Households, and Businesses .” In:SSRN
e\-Print .
Winter, P. and Planchet, F. (2022\). “Modern tontines as a pension solution: a practical overview .” In:European
Actuarial Journal 11\.
Woerheide, W. J. and Nanigian, D. (2011\). “Sustainable Withdrawal Rates from Retirement Portfolios: The His\-
torical Evidence on Buffer Zone Strategies .” In:SSRN e\-Print .
Wolfe, B. and Brazier, R. (2018\). Spending retirement assets ... or not? Tech. rep. BlackRock.
Wolfe, B. and Ferraro, M. (2022\). Decumulation challenges and potential solutions – Helping build a pathway towards
retirement spending and income confidence . Tech. rep. BlackRock.
Wu, H., Wang, X., Liu, Y., and Zeng, L. (2020\). “Multi\-period optimal investment choice post\-retirement with
inter\-temporal restrictions in a defined contribution pension plan .” In:Journal of Industrial \& Management
Optimization 16(6\), pp. 2857–2890\.
Wu, S. (2021\). “Assessing the relationship between health and household portfolio allocation .” In:Financial Planning
Review 4(4\).
Xu, G. (2015\). “The risk profiles of 401(k) accounts .” In:The Journal of Retirement 2(3\), pp. 67–77\.
148Xu, G. (2018\). “Static and Dynamic Tax Diversification of Withdrawals from Multiple Individual Retirement
Accounts .” In:The Journal of Retirement 6(2\), pp. 75–87\.
Xu, G. and Anichini, T. (2016\). “Mean\-Variance Analysis in Post\-Retirement Planning .” In:The Journal of Retire\-
ment 3(3\), pp. 62–76\.
Xu, G., Markowitz, H., and Guerard, J. B. (2019\). “Shortfall risk and shortfall duration for portfolio choice in
decumulation .” In:The Journal of Retirement 7(1\), pp. 24–34\.
Xu, J. and Hoesch, A. (2018\). “Predicting longevity: an analysis of potential alternatives to life expectancy reports .”
In:The Journal of Retirement 5(4\), pp. 9–24\.
Yang, B. (2017\). “Longevity and statistical modelling .” PhD thesis. Nanyang Technological University Singapore.
Yang, Y., UY, M. C. S., and Huang, A. (2020\). “FinBERT: A Pretrained Language Model for Financial Commu\-
nications.” In: arXiv e\-Print .
Yoon, Y. (2010\). “Glide path and dynamic asset allocation of target date funds .” In:Journal of Asset Management
11(5\), pp. 346–360\.
Young, R. (2020a). Tax\-Efficient Withdrawal Strategies . Tech. rep. T. Rowe Price.
Young, R. (2020b). “The Roth/Pretax Decision in Late Career Years: The Increasing Importance of Accumulated
Assets in Light of the SECURE Act .” In:Journal of Financial Planning 33(12\), pp. 59–68\.
Yu, L. (2021\). “Comparing Classical Portfolio Optimization and Robust Portfolio Optimization on Black Swan
Events .” MA thesis. University of Waterloo.
Yu, L., Hardle, W. K., Borke, L., and Benschop, T. (2020\). “An AI approach to measuring financial risk .” In:SSRN
e\-Print .
Yu, S., Chen, Y., and Dong, C. (2021a). “Learning Time Varying Risk Preferences from Investment Portfolios using
Inverse Optimization with Applications on Mutual Funds .” In:arXiv e\-Print .
Yu, S., Wang, H., and Dong, C. (2021b). “Learning Risk Preferences from Investment Portfolios Using Inverse
Optimization .” In:arXiv e\-Print .
Zhang, C., Li, Y., Chen, X., Jin, Y., Tang, P., and Li, J. (2020a). “DoubleEnsemble: A New Ensemble Method Based
on Sample Reweighting and Feature Selection for Financial Data Analysis .” In:IEEE International Conference
on Data Mining (ICDM) . IEEE.
Zhang, F., Guo, R., and Cao, H. (2020b). “Information Coefficient as a Performance Measure of Stock Selection
Models .” In:arXiv e\-Print .
Zhang, S. (2018\). “Optimal Retirement Planning: Scenario Generation, Preferences, and Objectives .” PhD thesis.
University of Waterloo.
Zhang, Z., Zohren, S., and Roberts, S. (2020c). “Deep Learning for Portfolio Optimization .” In:The Journal of
Financial Data Science 22(4\), pp. 8–20\.
Ziemba, W. T. (2016\). “An Approach to Financial Planning of Retirement Pensions with Scenario\-Dependent
Correlation Matrixes and Convex Risk Measures .” In:The Journal of Retirement 4(1\), pp. 99–111\.
Zuss, N. (2022\). Participants Will Need Support to Understand Lifetime Income Projections . Tech. rep. PlanSponsor.
149Appendix A: Overviews of investment processes and models in QWIM
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
150Appendix C: Incorporating comparison of portfolio metrics using bench\-
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
151Python and R packages/codes for portfolio optimization
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
152Python and R packages/codes for portfolio metrics and performance evaluation
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
153•expected covariance matrix is calculated based on forecasted values available at June 20, 2019 and obtained
using the forecasted model trained on given training dataset (which is from 1990 to 2017\)
Then one would compare various portfolio metrics among the two portfolios. These metrics can be calculated on
following time periods:
•from date of portfolio construction (June 20, 2019\) to last date for which you have data (August 1, 2020\)
•from starting date of dataset (January 1st, 1990\) to last date for which you have data (August 1, 2020\)
•from starting date of dataset (January 1st, 1990\) to date of portfolio construction (June 20, 2019\)
So you would have side\-by\-side comparisons of portfolio metrics for each of the above 3 time periods.
Portfolio metrics can be calculated using various Python and/or R packages mentioned above.
154