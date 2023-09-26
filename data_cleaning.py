import pandas as pd
import re
from get_model_tokenizer import get_model_tokenizer

_, tokenizer = get_model_tokenizer()
def clean_data(dataframe):
    # Convert to lower
    dataframe["questions"] = dataframe["questions"].apply(lambda x: x.lower())
    dataframe["answers"] = dataframe["answers"].apply(lambda x: x.lower())
    # Remove Special Characters
    dataframe["questions"] = dataframe["questions"].apply(lambda x: x.replace("'", ""))
    dataframe["answers"] = dataframe["answers"].apply(lambda x: x.replace("'", ""))
    
    dataframe["questions"] = dataframe["questions"].apply(lambda x: re.sub('[^A-Za-z0-9]+', ' ', x))
    dataframe["answers"] = dataframe["answers"].apply(lambda x: re.sub('[^A-Za-z0-9]+', ' ', x))
    
    return dataframe
