---
title: "Plan for modeling in the Bay Area"
author: "Lucy M. Li"
date: "April 3, 2020"
output:
  html_document:
    keep_md: yes
  pdf_document: default
---



# Executive summary

Ever since the SARS epidemic in 2003, mathematical modeling has been used to infer 
epidemiological quantities, uncover the natural history of disease, and evaluate 
effectiveness of interventions. In more recent years, modeling has been using in real
time to help policymakers to make decisions on interventions and resource allocation 
by forecasting the number of morbidities and mortalities as well as resource requirements.

During the current pandemic, models used for past outbreaks have been adapted for 
capturing COVID-19 transmission. This document provides:

1) an overview of the process of modeling for infectious diseases;
2) broad categories of models that are generally used for infectious diseases and their application to COVID-19;
3) sources of bias and uncertainty, and approaches to address these issues;
4) computational setup and requirements for modeling;

A proposed strategy for modeling the transmission of COVID-19 in the San Francisco Bay Area 
is laid out in the last section.

# Process of modeling for infectious diseases


### 1. Decide on question(s) to address

- What are key epidemiological parameter values?
- How many hospitalizations and deaths will occur in the next week?
- Who are more likely to infect others?
- Where are hotspots of transmission?
- What is the impact of social distancing?
- What is the fatality rate per infection?

### 2. Pick model(s) based on what we find out about the disease and pathogen.

- Routes of transmission
- Natural history of infection ( [CDC resource](https://www.cdc.gov/csels/dsepd/ss1978/lesson1/section9.html))
- Risk factors for infection and transmission?
- Animal and environmental reservoirs
- Immunity after infection (is re-infection possible?)
- Strains or serotypes of the pathogen
- Availability of treatments or vaccines
- Seasonality

### 3. Constraining or estimating parameters and initial model state values.

- Demography data to estimate population sizes
- Contact tracing data from the current outbreak can provide direct measurements of model parameters
- Serological surveys can provide information about who has already been infected
- Statistical distributions of generation times and incubation periods from similar infectious diseases could be used as priors to constrain parameter search space
- The ability to estimate parameters from data decreases with the number of parameters relative to the number of data points ( [paper](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6332839/) on the identifiability of parameters in infectious disease epi models)
- Sometimes it's better to fix more parameters, and perform sensitivity analyses to assess dependence of results on assumptions

### 4. Model fitting

- ODE solvers for deterministic models
- General purpose optimization algorithms for simple models
- Approximate Bayesian computation
- MCMC is the main workhorse for more complex models and for Bayesian analyses. There are many flavors that are used: Metropolis-Hastings, Gibbs, Hamiltonian, particle marginal Metropolis Hastings)

### 5. Model selection / ensemble modeling

- Reversible jump MCMC
- AIC/BIC/DIC/Bayes factor
- Bayesian model averaging
- [Ensemble modelig](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1007486)

### 6. Summarizing results

- Forecast of epidemic trajectory with credible intervals
- Parameter estimates with credible or confidence intervals
- Sensitivity analysis results
- Probabilities of events or outcomes
- Spatial visualizations


# Categories of models

This [paper](https://academic.oup.com/cid/article/60/suppl_1/S11/356440) in CID from 2015 provides a fairly comprehensive categorization of models, the epidemiological questions they address, and the types of data they need. Although the paper was written to provide guidance on modeling for the next flu pandemic, the principles are the same for modeling coronavirus.

Instead of regurgitating what was written in that paper, I will highlight a few papers that capture a range of options for modeling COVID-19.

### SEIR models with spatial spread

[Nowcasting and forecasting the potential domestic and international spread of the 2019-nCoV outbreak originating in Wuhan, China: a modelling study (Feb 29)](https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(20)30260-9/fulltext):

  - Fixed incubation and infectious periods
  - Fixed zoonotic infections
  - Used Tencent mobility data to fix the number of people moving between provinces in China, and between China and neighboring countries
  - Estimated R0 from Wuhan data using a deterministic SEIR model
  - Gibbs sampling
  - Predicted infections in China and surrounding countries using forward simulation of a deterministic metapopulation SEIR model
  - Showed how quickly the epidemic would die out assuming different reduction in transmission

[Early dynamics of transmission and control of COVID-19: a mathematical modelling study](https://www.sciencedirect.com/science/article/pii/S1473309920301444)

  - Fixed the number of travellers to different countries
  - Fixed the incubation period and delay in from onset to isolation
  - Estimated time-varying R using stochastic SEIR model
  - Estimated the relative rate of detection among exported cases compared to in Wuhan
  - Used Sequential Monte Carlo to fit model to data


[The effect of travel restrictions on the spread of the 2019 novel coronavirus (COVID-19) outbreak](https://science.sciencemag.org/content/sci/early/2020/03/05/science.aba9757.full.pdf?casa_token=r_FNP9kDFRIAAAAA:RVQLw6WOjB2-Xj210e8rnv7g16naIgAHeLRV_aQ2Uwn-gPxSgpc2DvmOuvPn3NSQV8MiUSGOKRZhMX0)
  
  - 
  - Used the [GLEAM](http://www.gleamviz.org/model/) model to estimate R0
  - Approximate Bayesian Computation
  - Sensitivity analysis assuming different combinations of average latent and infectious periods, detection rates, initial conditions, and generation times

###  Branching processes

[Feasibility of controlling COVID-19 outbreaks by isolation of cases and contacts](https://www.sciencedirect.com/science/article/pii/S2214109X20300747)



### Individual-based models

[https://spiral.imperial.ac.uk/bitstream/10044/1/77482/5/Imperial%20College%20COVID19%20NPI%20modelling%2016-03-2020.pdf](Impact of non-pharmaceutical interventions (NPIs) to reduce COVID19 mortality and healthcare demand)


### Statistical models

[Forecasting COVID-19 impact on hospital bed-days, ICU-days, ventilatordays and deaths by US state in the next 4 months](http://www.healthdata.org/sites/default/files/files/research_articles/2020/COVID-forecasting-03252020_4.pdf)

# Biases and uncertainty

### Common types of sampling issues

  - Fraction of infections that are asymptomatic/mild symptomatic infections --> time-invariant
  - Time-varying in type of tests being used
  - Time-varying in testing criteria
  - Uneven distribution geographically and according to human demographics
  - False negatives --> people who were mis-diagnosed
  - Potentially conflicting information from different data sources

### Sensitivity to assumptions

Models tend to be sensitive to these assumptions

  - Generation time distribution
  - Mixing patterns if there is significant heterogeneity in transmission across different demographic groups in the population
  - Rate of ascertainment
  

# Computational

## R/Python

Usually data cleaning, data transformation, and visualizations are done in R and Python, with the model and MCMC algorithm written in C or C++ for performance.

Most frequently used R packages: https://www.repidemicsconsortium.org/projects/

[RStan](https://mc-stan.org/users/interfaces/rstan)

[PyStan](https://pystan.readthedocs.io/en/latest/)

## C/C++

Stan

[BUGS](https://www.mrc-bsu.cam.ac.uk/software/bugs/)

[JAGS](http://mcmc-jags.sourceforge.net/)


## Containers

Not used that much for infectious disease outbreak modeling, even though Docker containers are widely used for pathogen genomics research. This would be an area of great technological contribution.

# Plan for predictive modeling of COVID-19 in the Bay Area

## Data

- Case counts by county: Webscraper, JHU data
- Number of tests by county: Webscraper, JHU data
- Deaths by county: Webscraper, JHU data
- Recovered by county: Webscraper, JHU data
- Hospitalizations: 
- Number of healthcare facilities, beds, and ventilators: Esri
- Mobility data between counties: Descartes Labs/Bay Area Council, Esri
- Transport data into and out of the bay area: SFgov

Data sources:

- [Web scraper](https://github.com/czbiohub/realtime-covid19-tracking/tree/scraping_experiment)
- [Descartes Labs/Bay Area Council](https://github.com/BACEI/Bay-Area-Mobility-Data/blob/master/MASTER_mobility_index_bayarea.csv)
- [Johns Hopkins Data](https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_time_series)
- [ESRI's data](https://disasterresponse.maps.arcgis.com/home/group.html?id=e0140dbc514b48b5b90c351740c14639&view=list#content): Unacast Social Distancing Score, ASTHO Restaurants and Bars Restrictions, ASTHO Stay at Home Orders and Advisories, ASTHO Travel and Quarantine Orders, ASTHO Testing Prioritization Guidance, ASTJHO State of Emergency Declarations, ASTHO Testing Prioritization Guidance, CDC Social Vulnerability Index 2018 - USA, Definitive Healthcare: USA Hospital Beds, World Population Density Estimate 2016
- [SF Gov data](https://data.sfgov.org/browse)
- [Data.gov](http://www.data.gov/)


## Models

### Compartmental models

Variations on the SEIR metapopulation model to include the following feature(s):

- geographic structure
- multiple strains
- age structure
- movement in and out of the area
- hospitalizations
- household transmission

### Agent-based models

- 

### Genomic

## Computational setup



## Questions to address

- Predictions about COVID-19 infections and hospitalizations
- Predictions about how long shelter-in-place needs to be in place
- Estimate real-time reproductive number before and after shelter-in-place
- Cross-jurisdictional transmissions based on mobility and genomic data
- Estimate ratio of introduced vs local transmission over time

- Side project on impact for healthcare by reducing load not just by COVID:
  - Impact on influenza
  - Impact on RSV infections
  - Food-borne outbreaks



