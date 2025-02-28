from transformers import pipeline

toxigen_hatebert = pipeline("text-classification", model="tomh/toxigen_hatebert", tokenizer="bert-base-uncased")

#returns true if it is racist, false if it is not
def is_racist(sentence):
    output = toxigen_hatebert(sentence)
    return output[0]['label'] == 'LABEL_1'
