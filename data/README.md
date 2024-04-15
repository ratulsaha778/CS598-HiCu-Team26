1. MIMIC-III dataset is accessed from [PhysioNet](https://physionet.org/content/mimiciii/1.4/).

2. MIMIC-III files data structure:
```
data
|   D_ICD_DIAGNOSES.csv
|   D_ICD_PROCEDURES.csv
|	mimic3/
|   |   NOTEEVENTS.csv
|   |   DIAGNOSES_ICD.csv
|   |   PROCEDURES_ICD.csv
|   |   train_full_hadm_ids.csv
|   |   train_50_hadm_ids.csv
|   |   dev_full_hadm_ids.csv
|   |   dev_50_hadm_ids.csv
|   |   test_full_hadm_ids.csv
|   |   test_50_hadm_ids.csv
```

3. The `*_hadm_ids.csv` files are downloaded from [CAML repository](https://github.com/jamesmullenbach/caml-mimic)

4. "python preprocess_mimic3.py" need to run to preprocess the data.

5. Preprocess creates new files for the model:
```
data
|	mimic3/
|	|	dev_50.csv, test_50.csv, train_50.csv
|	|	dev_full.csv, test_full.csv, train_full.csv
|	|	vocab.csv, vocab_rac.csv
|	|	processed_full_100.embed/.w2v/.w2v.syn1neg.npy/.w2v.wv.vectors.npy, processed_full_300.embed/.w2v/.w2v.syn1neg.npy/.w2v.wv.vectors.npy
|	|	disch_full.csv, disch_dev_split.csv, disch_train_split.csv, disch_test_split.csv
|	|	ALL_CODES.csv, ALL_CODES_filtered.csv
```

6. Final data files are loaded in Google Drive: https://drive.google.com/drive/folders/1wb8_7s_7mVQpuYbco3Em38hf8mxTk7kX?usp=drive_link. These files used to train the model and performance check in Google Colab.

