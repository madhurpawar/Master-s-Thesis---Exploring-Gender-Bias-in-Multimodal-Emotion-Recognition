from collections import defaultdict
import os
import pandas as pd

# Define the list of classes for CREMA-D dataset
sentences_list = [
    "IEO", "TIE", "IOM", "IWW", "TAI", "MTI", "IWL", "ITH", 
    "DFA", "ITS", "TSI", "WSI"
]
emotions_list = ["ANG", "DIS", "FEA", "HAP", "NEU", "SAD"]
intensity_list = ["LO", "MD", "HI", "XX"]

def getListOfFiles(dirName):
    listOfFile = os.listdir(dirName)
    allFiles = defaultdict(list)
    for entry in listOfFile:
        file = os.listdir(dirName + '/' + entry)
        allFiles[entry] = file
                
    return allFiles

def load_CREMA_D_info(data_dir, X=None, Y=None):
    """
    This function will return audio file PATH and labels separately when data directory(`data_dir`) 
    is passed to it.
    """
    audio_dataset = list()

    if not (X or Y):
        X = list()
        Y = list()

    for wav in os.listdir(data_dir):
        # Getting labels from the encoded file names
        parts = wav.split('_')
        actor_id = parts[0]
        sentence = parts[1]
        emotion = parts[2]
        intensity = parts[3].split('.')[0]  # Removing file extension

        # Collect labels in a list
        l_text = [actor_id, sentence, emotion, intensity]

        X.append(os.path.join(data_dir, wav)) 
        Y.append(l_text)
  
    return X, Y

def getdata(video_folder: str):
    video_info = load_CREMA_D_info(video_folder)
    label_headers = ['Audio_file', 'actor_id', 'sentence', 'emotion', 'emotional_intensity']
    df_ = defaultdict(list)
    df_[label_headers[0]] = video_info[0]
    for j, label in enumerate(label_headers[1:], 0):
        df_[label] = [i[j] for i in video_info[1]]

    return pd.DataFrame(df_)