# Text Suggestion System

## Introduction
This api provides text suggestion based on the given input text using **Markvo Chain**.
The Markov Chain used here  constructed using n-gram size 2 using **Wikipidea articles and Conversation** dataset.
---
## Modules and Routes
This project contains following module
<br>
### generate(model,ngram_size,start_text,max)
<br>
This module generate the text that need to be suggested using the Markov model passed as an arugment ,default ngram size is 2 and if you wish to use another model with different n-gram size construct the Markov Chain using python notebook present in core folder and pass the n-gram size to the generate function.If no start text is passed as an input then **None** will be taken as start text and empty string will be given as response.
<br><br>
This project contain following routes
<br>
### /suggest_text
By passing the text in request params with **GET** method to this route you can get  text suggestion as json in response.
Pass input string with **data** as key.
---
## Resources
Articles from Wikipedia and Chat dataset from Kaggle was used for generating the Markov chain