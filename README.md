# CSE-576-NR-2
CSE 576 Synthetic dataset creation
Group 5 Natural Language QA with numericals

# Novelty Chalenge

1. Novelty detection
2. Novelty handling


# Challenge description

This challenge is aimed at testing models’ capability to detect novelty and handle it. <br><br>
Novelty detection : Identifying if an input is different from the data distribution on which the model was trained; OOD detection. Model should detect OOD samples and ask for some similar examples. <br><br>
Novelty handling : handling novel inputs from a limited set of OOD examples; Low resource learning; Zero-shot / few shot learning. 

# Challenge Breakdown
This challenge has been broken down into multiple stages.<br>
The challenge starts with Stage 1 : the simplest of all <br>
The complexity of the challenge increases with the stage.<br>
In every stage, a model is evaluated on a test set that consists of both In-domain and Out-of-domain questions. Models are given more credit for detecting OOD questions as compared to correctly solving them. Hence, achieving the novelty detection objective.<br>
Final score is computed by aggregating the weighted scores of all the stages.


# Scoring criteria for a stage
| Answer \ Question Category | In-Domain | Out-of-domain |
| --- | --- | --- |
| Correct |  10 | -6 | 
| Incorrect | 0 | -5 | 
| OOD detected | -7.5 | 10 |


# Fetch script Sample

```
python fetch.py --stage stage1 --data_percentage 50 train_data_file_name any_file_name.json
```

# Evaluate script sample
```
python evaluate.py --stage stage1 --test_data_file your_custom_file.json
```

## Format of your_custom_file.json
each sample in a separate row in json format<br>
```
{"Answer": "100", "Id": "f4552671f8909587cf485ea990207f3b"}
```

Created by:
Pratyusha Kodali
Gayathri Alloju
Vamshi Krishna Kangala
Chandrahaas Chintabogutta: 1218686443
Sabyasachi Bisoyi 1218272029

Dataset attached : data.json
Group project GitHub link  : https://github.com/swarooprm/CSE-576-NR-2  (our mentor Swaroop’s GitHub account)

Overview:
We have created our synthetic dataset using template based QA generation and using some from existing dataset such as Aquarata and DROP.
Our dataset has three columns, namely “question”,”answer” and “options” and it is in JSON format. Question column has the generated question using the template, answer
has the answer for the question and options is an array of available options.

Members Contribution:
Sabyasachi Bisoyi:
We have created templates with commonsense knowledge, verb physics and numerical math. We have followed these papers for the same.
NumerSense: Probing Numerical Commonsense Knowledge of Pre-trained Language Models and Verb Physics : Relative Physical Knowledge 
of Actions and Objects . Also We have taken some maths questions from NCERT sample books. In a template we try to change verbs(actions), 
and numerical. In the code to generate templates , we define relationship between numbers and answer. So we can eliminate options and reach 
to the final answer. For verb physics we need extra data to compare between objects/mediums. This is being provided in a dictionary. Depending 
on the question, we have changed the duplicity value and at the end merged all questions generated and shuffled them to Make the model train/learn with less spurious bias.

Chandrahaas Chintalaboguda:

Our main task is to create synthetic data for Natural Language QA with numericals which involved common sense and some numerical analysis. For this I followed papers of Numersense for using some commonsense knowledge datasets and AquaRat for some simple math problems. I also followed some math questions from Manhattan 5 lb book and ICSE books. I have tried to change the verbs, objects and numericals by masking them and randomly assigning sets for every question template. For each question I have given a different duplicity value depending on the number of different objects and numericals. I have inserted each output from each template into a dictionary with Questions, Answers and Options as keys and then inserted them into a list. Later in the end,I shuffled them in the end to reduce any spurious biases and saved it into a JSON file.
I have three columns in my dataset Question, Options and Answer.

Vamsi Krishna Kanagala:

As the main goal of this task is to create synthetic data for our project, I've chosen the approach of using templates that includes commonsense knowledge along with numericals. For creating these questions, I have taken the questions for NCERT textbook and GRE sample papers as reference. At first, I built the structure of the questions by keeping the subjects, objects, and action verbs as variables(parameters). I also have maintained set of nouns and action verbs, and with these I generated sample questions by selecting random names and verbs. Thus, in every iteration a random variable is selected and replaced at its corresponding position in the templates. And depending on the number of parameters present in the template and the gravity of the structure, I have selected the duplicity(numbers of iterations). I have also generated the options and answers for the questions in each iteration, and saved all these in a list of dictionaries initially, which I later saved in a JSON file after shuffling the entire saved list to avoid unwanted biases.

Prathyusha Kodali:

For this initial phase of the project, it is required to build a synthetic dataset for training a model that can perform discrete reasoning over the content in the given question to obtain an answer. For the implementation of this task, I have gone through AQuA-RAT datasets, NCERT questions and dicussed with the project guide on the template creation approach. I have created 22 templates, each with a duplicity of 200. Templates 1 to template 13 are numerical questions involving common and real world knowledge. Most of them are based on keywords, comparisions between objects, prices etc. The rest of the templates requires mathematical operations on the parameters to obtain a numerical answer. To generate different type of questions, I have created an excel workbook having multiple sheets named "inputs.xlsx" with different values possible for parameters mentioned in each template. The values in excel sheet are read into pandas dataframes/lists and the parameter values are randomly chosen. For a few questions, I have also generated different sets of options (set containing no correct answers, set with one correct answer and a set with more than one correct answers). I have added unrealistic options so that the model cannot answer by choosing maximizing or minimizing the given parameters. I have also added linguistic variations in the options and shuffled the options to avoid any bias. After generation of set of questions with corresponding answers and options, I have shuffled them to avoid spurious biases if any and copied the data samples to the JSON file. 

Gayathri Alloju:

The main task being Sythetic Dataset creation, I have created templates based on numerical common sense questions where primary focus being comparison of objects with respect to weight, volume, etc. I have also created tenplates based on numerical calculations taking into account real life examples. I put my main effort on creating a source for the above tenplates, more the number of source records gives variety of Dataset samples which is saved in an Excel file. I set the duplicity factor to generate different samples based on my excel file data and Lists for some of the templates. I have given multiple options based on the type of question which will be shuffled for every loop to avoid repeated orders. Finally I have generated the output as per the logic I have written in the code. The output has been saved into a json file which will be shuffled to lessen the spurious bias if any.     

Code:
Our code is written in Jupyter notebook. So each cell is individually runnable and can be run from any machine having Jupyter notebook.
