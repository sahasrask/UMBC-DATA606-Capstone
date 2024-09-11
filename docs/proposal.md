
# Sanskrit to English Translation System
- Prepared for: UMBC Data Science Master Degree Capstone by Dr Chaoji (Jay) Wang - FALL 2024 Semester
- Author: Sahasra Kamatam
- GitHub: https://github.com/sahasrask
- Linkedin: https://www.linkedin.com/in/sahasra-kamatam-851763197/


## BACKGROUND
### Problem Statement
Forest Fire Prediction System gives the most accurate predictions of when fire can take place using data-driven techniques and machine learning models.
Why does it matter ?

1. **Early Warning and Prevention:** By accurately predicting the likelihood of forest fires, these systems enable authorities to take proactive measures to prevent fires from occurring or to mitigate their impact. 
2. **Resource Allocation:** Forest fire prediction systems help in allocating firefighting resources effectively. By identifying areas at high risk of fire, authorities can strategically deploy firefighting crews, equipment, and aircraft to those locations, improving response times and minimizing damage.


* Research Questions :

1. How can machine learning algorithms be optimized to improve the accuracy and reliability of forest fire prediction models?
2. How do different environmental factors, such as weather conditions, vegetation type, and topography, influence the spread and intensity of forest fires?
3.  What role can remote sensing technologies, such as satellite imagery and unmanned aerial vehicles (UAVs), play in enhancing forest fire prediction and monitoring?



## DATA

- **Data sources:** [Algerian Forest Fires from UCI](https://archive.ics.uci.edu/dataset/547/algerian+forest+fires+dataset)
- **Data size:** 12.9 KB
- **Data shape:** 
  - `Algerian_forest_fires_dataset_UPDATE.csv` - 244 rows, 12 columns
- **Time period:** The datasets cover a time span of (from 06/01/2012 to 09/30/2012).
- **What does each row represent?**
  - The dataset includes 244 instances that regroup a data of two regions of Algeria,namely the Bejaia region located in the northeast of Algeria and the Sidi Bel-abbes region located in the northwest of Algeria.

### Data Dictionary

| day | month | year | Temperature | RH | Ws | Rain | FFMC | DMC | DC | ISI | BUI | FWI | Classes | Region |
|-----|-------|------|-------------|----|----|------|------|-----|----|-----|-----|-----|---------|--------|
| 1   | 6     | 2012 | 29          | 57 | 18 | 0.0  | 65.7 | 3.4 | 7.6 | 1.3 | 3.4 | 0.5 | 0       | 1      |
| 2   | 6     | 2012 | 29          | 61 | 13 | 1.3  | 64.4 | 4.1 | 7.6 | 1.0 | 3.9 | 0.4 | 0       | 1      |
| 3   | 6     | 2012 | 26          | 82 | 22 | 13.1 | 47.1 | 2.5 | 7.1 | 0.3 | 2.7 | 0.1 | 0       | 1      |
| 4   | 6     | 2012 | 25          | 89 | 13 | 2.5  | 28.6 | 1.3 | 6.9 | 0.0 | 1.7 | 0.0 | 0       | 1      |
| 5   | 6     | 2012 | 27          | 77 | 16 | 0.0  | 64.8 | 3.0 | 14.2| 1.2 | 3.9 | 0.5 | 0       | 1      |
| ... | ...   | ...  | ...         | ...| ...| ...  | ...  | ... | ... | ... | ... | ... | ...     | ...    |

  
  
### Target/Label in ML Model
The primary target for the machine learning models in this project is the class. 

### Features/Predictors for ML Models
Temperature, relative humidity (RH), wind speed (Ws), rainfall (Rain), Fire Weather Index (FWI), FFMC, DMC, DC, ISI, BUI, Region
