# Sanskrit to English Translation
 ### Sahasra Kamatam- 4th Semester
- Sanskrit to English Translation
- Prepared for UMBC Data Science Master Degree Capstone by Sahasra Kamatam under the guidance of Dr Chaojie (Jay) Wang
- Author Name: Sahasra Kamatam
- LinkedIn: [Sahasra Kamatam](https://www.linkedin.com/in/sahasra-kamatam/)
- GitHub: [Sahasra Kamatam](https://github.com/sahasrask)
- PowerPoint presentation:docs/SanToEng Presentation.pptx
- Youtube Link: 
    
## 1. Introduction
Sanskrit is one of the oldest languages and is known for its precision basically Its words changes based on grammar rules like cases, gender, and number by giving each word a variety of meanings depending on its form. 
English, on the other hand, has a simpler structure and relies more on word order to convey meaning, this creates a gap in how sentences are understood in each language.
#### Research Questions
- How can modern NLP techniques, particularly Transformer-based models, be adapted to accurately capture the complex grammatical structures of Sanskrit in order to improve translation quality into English?
- What are the limitations of existing multilingual models when applied to low-resource languages like Sanskrit, and how can fine-tuning or transfer learning be leveraged to enhance translation accuracy?
- How does the scarcity of parallel Sanskrit-English datasets impact the performance of machine translation models, and what strategies can be employed to mitigate data limitations?
-  How effective are attention mechanisms and context-handling techniques in disambiguating multiple meanings of Sanskrit words during translation?
- What evaluation metrics are best suited for assessing the grammatical and semantic accuracy of Sanskrit-to-English translations, and how can these be applied to optimize the model?
  
## 2. Data 

- The dataset taken from the dataset library: "rahular/itihasa"
- Dataset contains Train and Test Data of Sanskrit to English translated sentences.
- Sanskrit and Enlish translations has its seperate text file like ---------------
- Train dataset contains 75162 sentences and 1 feature of Sanskrit text and Enlish translation of Sanskrit sentences. 
- Test dataset contains 24217 sentences and 1 feature of Sanskrit text and Enlish translation of Sanskrit sentences. 
- Dataset is downloaded in the project file. 

## 3. Data Prepocessing
- Data is downloaded from dataset library: "rahular/itihasa" and extracted the translations from the train dataset.
- Extracted Sanskrit and English sentences from each entry and stored in different lists.
- Data Cleaning is done by performing the below steps
     - Lowercasing all the characters
     - Removing Quotes
     - Removing all Special characters
     - Removing numbers.
     - Removing Extra Spaces.
     - Added "START_" and "_END" tokens marking the start and end of target language sequences.
- Processed English and Sanskrit sentences (or phrases) stored in a lists and extracted unique words from those sentences, and counts the total number of unique words.
- From the data we got 72422 and 18402 unique words from Sanskrit and English sentences respectively.
- Created dictionaries to map words to unique indices.
- Create reverse dictionaries to map indices back to words.

<img src="Images/Data_Cleaning.png" alt="yolov4arch" style="display: block; margin-left: auto; margin-right: auto; width: 400px; height: 120px;">

## 4. Model Training
- **Encoder-Decoder Long Short-Term Memory Algorithm**
  - Partition a dataset comprising Sanskrit (san) and English (eng) sentences into training and testing subsets, structure the data into organized DataFrames, and save the resulting datasets for future use.
  - LSTM algorithm is a data generator for training sequence-to-sequence models, typically used in machine translation tasks.
  - The model is used to prepare batches of data for the encoder and decoder during training, ensuring that data is processed efficiently in chunks (batches).
  - Built a sequence-to-sequence (seq2seq) model using the Keras library, suitable for tasks like machine translation or text generation. It consists of an encoder-decoder architecture with LSTM (Long Short-Term Memory) layers for handling sequential data.

  <img src="Images/Keras_Model.png" alt="yolov4arch" style="display: block; margin-left: auto; margin-right: auto; width: 400px; height: 200px;">

  - The output shows a summary of the model architecture, listing each layer, its type, the shape of the output, the number of parameters (trainable values), and how the layers are connected.
  - The Input layers receive sequences of unspecified length (indicated by (None, None)).
  - Embedding layers convert input words into 50-dimensional vectors. One embedding layer handles the source language, and the other handles the target language.
  - LSTM layers process these embeddings to capture the sequence information and output hidden states and cell states of size 50.
  - The final Dense layer outputs a probability distribution over 18,403 possible target tokens (words).
  - The model has about 5.5 million trainable parameters, meaning that the model will learn by adjusting these values during training.

- **Plotting Training and Validation:**
  - Saved the trained model's weights to a file named "nmt_model.weights.h5." which allows reloading the weights later without re-training.
    <img src="Images/Keras_Model.png" alt="yolov4arch" style="display: block; margin-left: auto; margin-right: auto; width: 400px; height: 200px;">
    ![image](https://github.com/sahasrask/UMBC-DATA606-Capstone/docs/Images/Keras_Model.png)
docs/Images
  - The plot displays the model's performance over epochs(training vs. validation accuracy) to detect overfitting or underfitting.


    1. Custom cfg file
    2. `coco.data` and `coco.names`
    3. `train.txt` file and `test.txt` file (optional)
  - Change the `coco.names` file to include the name of the custom object: vehicle registration plate.

  <img src="images/coconame.png" alt="yolov4arch" style="display: block; margin-left: auto; margin-right: auto; width: 200px; height: 100px;">

  - Modify `coco.data`, which is used to train the model. Inside `coco.data`, set the locations of `train.txt`, `test.txt`, `coco.names`, the number of classes, and a backup location for weights.

  <img src="images/cocodata.png" alt="yolov4arch" style="display: block; margin-left: auto; margin-right: auto; width: 200px; height: 100px;">

  - `yolov4-custom.cfg` is the configuration file where the architecture and parameters for training object detection are specified.
  - The cfg file contains specific sections to be modified for custom object detection:
    1. Network architecture
    2. Input dimensions
    3. Batch size and subdivisions
    4. Training parameters
    5. Anchor boxes
    6. Classes
    7. Filters
    8. Augmentation and preprocessing
  - I suggest setting **batch = 64** and **subdivisions = 16** for optimal results. If you encounter any issues, increase subdivisions to 32.

  Adjust the rest of the cfg file based on the number of classes your detector will be training on.

  **Note:** 
  I set **max_batches = 6000** and **steps = 4800, 5400**. I changed **classes = 1** in the three YOLO layers and **filters = 18** in the three convolutional layers preceding the YOLO layers.

  **Configuring Your Variables:**

  - **width = 416**
  - **height = 416**  
  *(These should be multiples of 32. The standard is 416, but increasing this to values like 608 can sometimes improve results, though it will slow down training.)*

  - **max_batches = (number of classes) * 2000**  
  *(But no fewer than 6000, so for 1, 2, or 3 classes, max_batches should be 6000. For 5 classes, max_batches would be 10000.)*

  - **steps = (80% of max_batches), (90% of max_batches)**  
  *(For example, if max_batches = 10000, then steps = 8000, 9000.)*

  - **filters = (number of classes + 5) * 3**  
  *(So if you are training for one class, filters = 18. For four classes, filters would be 27.)*

  **Optional:** If you experience memory issues or prolonged training times, change **random = 1** to **random = 0** in each of the three YOLO layers in the cfg file. This will speed up training and save memory, though it may slightly reduce model accuracy.

**All files are uploaded inside the [GitHub repo folder docs and notebooks](https://github.com/Hemanth-Akkenapally/UMBC-DATA606-Capstone). Change it according to your project requirements.**
## 6. Results
- Trained model generetes a set of weights like first 1000, 2000, 3000 and best. we will use best weights for testing the images we took in real time. 
- After training YOLO model, it will generate a graph which shows us the error rate for every iterations which Loss graph and mAP plot in a single graph.
- Loss graph explains us the loss values over time. If the loss plateaus or increases, it indicates overfitting or need a further tuning of the parameters in cfg file.
- Our model is good to use since the graph shows less than 0.1% loss.
- Mean average precision measures the precision of the model in detection the objects across different classes. High mean average precision indicates better performance model.
 
<img src="images/Errorvsiterations.png" alt="Graph" style="display: block; margin-left: auto; margin-right: auto; width: 300px; height: 250px;">

- We will use custom.weights file which is generated after training the model to test the object detection. 

<img src="images/outputcolab.png" alt="output colab" style="display: block; margin-left: auto; margin-right: auto; width: 250px; height:250px;"> 

- Output shows 98 percent accuracy that the license plate is detected.

## 7. Application of the Trained Models

- **Streamlit Application :** For machine learning and data science projects, Streamlit is an open-source Python toolkit that makes it easier to create and distribute eye-catching, unique web applications. Because of its intuitive and user-friendly design, developers may create interactive applications with little to no code.

- Streamlit has many benefits, including simple deployment, real-time engagement, connectivity with data science libraries, and ease of use. It also offers choices for altering the arrangement to meet various project specifications.

<img src="images/streamlitwebpage.png" alt="Web Page" style="display: block; margin-left: auto; margin-right: auto; width: 250px; height:250px;">


- This is the webpage we developed using streamlit application. We can directly upload an image and run the detection button then it runs the detection in the background colab and gives us the output along with accuracy.

<img src="images/outputstreamlit.png" alt="Outout Streamlit" style="display: block; margin-left: auto; margin-right: auto; width: 250px; height:250px;">


## 8. Conclusion
- Summary: This project explored the challenges and approaches for Sanskrit-to-English translation using Encoder-Decoder LSTM models, highlighting the unique complexities of Sanskrit’s syntax, morphology, and context-dependent meanings.
- Achievements: Successfully developed a model that translates basic Sanskrit sentences, paving the way for enhanced accessibility of Sanskrit texts in academia and beyond.
- Challenges and Limitations: Handling complex sentence structures, compounded words, and data scarcity remains a challenge, impacting translation accuracy.
- Future Potential: With advancements like Transformer models, attention mechanisms, and domain-specific fine-tuning, the model can be improved for better accuracy and wider application.
- Final Thought: This work contributes to bridging the gap between ancient and modern languages, making Sanskrit's rich cultural and intellectual heritage more accessible in the digital age.

## 9. References 

1. https://www.mdpi.com/2075-1680/12/5/424
2. https://roboflow.com/model/yolov4
3. https://github.com/kiyoshiiriemon/yolov4_darknet
4. https://blog.51cto.com/u_15067242/3553533
5. https://arxiv.org/abs/2004.10934 
6. https://developer.nvidia.com/cuda-toolkit 
7. https://pjreddie.com/darknet/yolo/
