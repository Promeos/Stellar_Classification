# Star Light, Star Bright
#### Classifying Stars

## Background

### About Riiid Labs
“Riiid Labs, an AI solutions provider delivering creative disruption to the education market, empowers global education players to rethink traditional ways of learning leveraging AI. With a strong belief in equal opportunity in education, Riiid launched an AI tutor based on deep-learning algorithms in 2017 that attracted more than one million South Korean students. This year, the company released EdNet, the world’s largest open database for AI education containing more than 100 million student interactions.” [Source](https://www.kaggle.com/c/riiid-test-answer-prediction/overview)

### TOEIC (Test of English for International Communication)
The TOEIC Listening & Reading test is an objective test that features 200 questions with a two hour time limit. Listening (approximately 45 minutes, 100 questions) and Reading (75 minutes, 100 questions). [Source](https://www.iibc-global.org/english/toeic/test/lr/about/format.html)

### Riiid's TOEIC Platform
“Santa TOEIC is the AI-based web/mobile learning platform for the TOEIC. AI tutor provides a one-on-one curriculum, effectively increasing scores based on the essential questions and lectures for each user.” [Source](https://www.riiid.co/en/product)

## Data Dictionary
 
**`stars.csv`**
| Feature Name                                  | Description                                                                   |
| :-------------------------------------------- | :---------------------------------------------------------------------------- |
| Temperature                                   | Temperature in degrees Kelvin                                                 |
| Relative Luminosity                           | Luminosity $\div$ Average Luminosity of the Sun                               |
| Relative Radius                               | Radius $\div$ Average Radius of the Sun                                       |
| A_M                                           | Absolute Magnitude                                                            |
| Color                                         | General Color of Spectrum                                                     |
| Spectral Class                                | O,B,A,F,G,K,M / SMASS - https://en.wikipedia.org/wiki/Asteroid_spectral_types |


| Spectral Class                                | Spectral Features                                                             |
| :-------------------------------------------- | :---------------------------------------------------------------------------- |
| A                                             | Very steep red slope shortward of 0.75 μm; moderately deep absorption feature longward of 0.75 μm. |
| B, F	                                        | Linear, generally featureless spectra. Differences in UV absorption features and presence/absence of narrow absorption feature near 0.7 μm. |
| G                                             | Linear, generally featureless spectra. Differences in UV absorption features and presence/absence of narrow absorption feature near 0.7 μm. |
| K                                             | Moderately steep red slope shortward of 0.75 μm; smoothly angled maximum and flat to blueish longward of 0.75 μm, with little or no curvature. |
| M                                             | Generally featureless spectrum with reddish slope; differences in subtle absorption features and/or spectral curvature and/or peak relative reflectance. |
| O                                            	| Peculiar trend, known so far for very few asteroids.                              |

| Target Name: __Type__ | Description             |
| :-------------------- | :---------------------- |
| 0                     | Red Dwarf               | 
| 1                     | Brown Dwarf             | 
| 2                     | White Dwarf             | 
| 3                     | Main Sequence           | 
| 4                     | Super Giants            | 
| 5                     | Hyper Giants            | 

MATH:

    Lo = 3.828 x 10^26 Watts
    (Avg Luminosity of Sun)

    Ro = 6.9551 x 10^8 m
    (Avg Radius of Sun)

### Feature Engineering
| Feature Name                | Description                                                                                 |
|-----------------------------|---------------------------------------------------------------------------------------------|
|||


## Initial Thoughts


## Project Steps
### 1. Acquire


### 2. Prepare
**Missing Values**

**Feature Engineering**

**Preprocessing**


### 3. Explore


#### Hypotheses
**Hypothesis**
> 


**Hypothesis**
>

**Hypothesis**
> 

**Hypothesis**
> 

**Hypothesis**
> 

### 4. Model


### Final Model


### 5. Conclusion

#### Key Findings
- 

#### What was the best model?


## How to Reproduce
All files are reproducible and available for download and use.
- [x] Read this README.md
- [ ] Download the aquire.py, prepare.py, and Final-Report.ipynb files
- [ ] Run Final-Report.ipynb
