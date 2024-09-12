
# Sanskrit to English Translation System
- Prepared for: UMBC Data Science Master Degree Capstone by Dr Chaoji (Jay) Wang - FALL 2024 Semester
- Author: Sahasra Kamatam
- GitHub: https://github.com/sahasrask
- Linkedin: https://www.linkedin.com/in/sahasra-kamatam-851763197/


## BACKGROUND
### Problem Statement
The challenge is to develop an accurate and automated Sanskrit-to-English translation system that addresses the complexities of Sanskrit grammar, contextual meaning, and the scarcity of annotated parallel datasets.

Why does it matter ?

1. **Early Warning and Prevention:** By accurately predicting the likelihood of forest fires, these systems enable authorities to take proactive measures to prevent fires from occurring or to mitigate their impact. 
2. **Resource Allocation:** Forest fire prediction systems help in allocating firefighting resources effectively. By identifying areas at high risk of fire, authorities can strategically deploy firefighting crews, equipment, and aircraft to those locations, improving response times and minimizing damage.


* Research Questions :

1. How can modern NLP techniques, particularly Transformer-based models, be adapted to accurately capture the complex grammatical structures of Sanskrit in order to improve translation quality into English?
2. What are the limitations of existing multilingual models when applied to low-resource languages like Sanskrit, and how can fine-tuning or transfer learning be leveraged to enhance translation accuracy?
3. How does the scarcity of parallel Sanskrit-English datasets impact the performance of machine translation models, and what strategies can be employed to mitigate data limitations?
4. How effective are attention mechanisms and context-handling techniques in disambiguating multiple meanings of Sanskrit words during translation?
5. What evaluation metrics are best suited for assessing the grammatical and semantic accuracy of Sanskrit-to-English translations, and how can these be applied to optimize the model?
 

## DATA

- **Data sources:** https://www.kaggle.com/datasets/deveshparmar01/sanskrit2/data
- **Data size:** 4 MB
- **Data shape:** 
  - `dict.xlsx` - 1255 rows, 2 columns
  - `output_file.xlsx` - 69714 rows, 2 columns

### Data Dictionary

| Sanskrit | English | Meaning                               |
|----------|-------- |---------------------------------------|
| अब्       | 6       | now                                   | 
| अबभसे     | 6       | spoke , began to say , said , replied | 
| अबद्धह्     | 6       | being too attached to Her             |
| अबद्धम्     | 6       | nonsensical                           |
| अबधत     | 6       | irregularly composed                  |
| ...      | ...     | ..................................... | 


| English | Sanskrit |
|---------|--------  |
| I       | 6        | 
| walk    | चर       | 
| doing   | करोति     | 
| deep    | गम्भीरम्    | 
| quiet   | निःशब्दम्   | 
| ...     | ...     |

  
  
### Target/Label in ML Model
The primary target for the machine learning models in this project is the class. 

### Features/Predictors for ML Models
Temperature, relative humidity (RH), wind speed (Ws), rainfall (Rain), Fire Weather Index (FWI), FFMC, DMC, DC, ISI, BUI, Region
