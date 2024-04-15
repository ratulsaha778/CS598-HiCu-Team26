# HiCu-ICD
This Github repository contains codes for training the ICD model mentioned in the research paper [HiCu: Leveraging Hierarchy for Curriculum Learning in Automated ICD Coding](https://github.com/wren93/HiCu-ICD/tree/main).

Setup
-----
The text file `requirements.txt` contains all the Python packages needed for the environment. Google Colab usually comes with the packages preinstalled. We need to vigilant about the code and version dependencies. 

Data Preprocessing
-----
MIMIC-III v1.4 dataset was used for model training and evaluation.
Detailed data download process is mentioned: https://piazza.com/class/lr91rjy3b7616o/post/338.

Training
-----
With a powerful (20GB+ RAM, 20GB+ GPU memory) personal computer, model can be train locally through: 
1. MultiResCNN and RAC models can be run with appropriate .py files under "/runs" folder.
2. For LAAT (Bi-LSTM) models, artifacts are present in "LAAT" branch of GitHub repo.

Alternatively, model training can be done on the cloud in Google Colab through:
1. Load the complete folder structure with files in it, into Google Drive.
3. Local Preprocessed data would be loaded in subfolder "/data".
4. There are executable code sections in "Team26_HiCu_Colab_Notebook_Draft.ipynb" that first mounts the Google Drive into Google Colab. Then the contents are copied into Colab. Then the model performance checking programs are run inside Colab on the data present in Colab. That way the models run bit faster.
"Options.py" contains the hyperparamter settings. RAC models need multiple high-end GPUs.

Acknowledgement
-----
We reused authors' original repo codes [wren93/HiCu-ICD] (https://github.com/wren93/HiCu-ICD), with some updates to improve reproducibility & facilitate model training on Google Colab.