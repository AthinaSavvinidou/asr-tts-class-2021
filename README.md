# asr-tts-class-2021


## AUTOMATIC SPEECH RECOGNITION
  ### 1. Project Description
 In this project, was attempted to create an  automatic recognition system, which recognizes voice commands for the AMONG US game in the German language. 
 
 ### 2.Data Preparation
The grammar and dictionary were originally created, as well the list of voice commands. The run.sh file runs german_data_prep.sh to prepare the train and dev dataset.
In turn german_data_prep.sh runs prep_tsv.py, which searches for files in the dataset subfolders and creates a pandas dataframe with speaker ids, utterance ids, wav file paths, utterances. Then the pandas dataframe is divided into two dataframes, one for train and one for development, which are sorted based on utterance id. From these two dataframes two train / dev directories are created in which the .tsv, wav.scp, utt2spk, spk2utt and text files are stored. Then the german_data_prep.sh runs validation on the files of these two directories.


  
## SYNTHESIS PART <a name="introduction"></a>
In order to test the competence of the project in this part, 5 phrases have been generated using slt_arctic_demo and slt_arctic_full_voice through merlin engine.


### Phrases <a name="paragraph1"></a>
List of phrases: 1.Use button. 
                 2.Move right shields. 
                 3.Select author.
                 4. Game instructions Polus. 
                 5.Play Mira for free.

### Evaluation Results <a name="paragraph2"></a>

  
    

 1. Intelligibility

|     SLT_ARCTIC_DEMO               |     Evaluator 1    |     Evaluator 2    |
|-----------------------------------|--------------------|--------------------|
|     1.Use button                  | 1                  | 1                  |
|     2.Move right shields          | 1                  | 1                  |
|     3.Select author               | 1                  | 1                  |
|     4. Game instructions Polus    | 1                  | 1                  |
|     5.Play Mira   for free        | 1                  | 1                  |

2. Naturalness

|     SLT_ARCTIC_DEMO               |     Evaluator 1    |     Evaluator 2    |
|-----------------------------------|--------------------|--------------------|
|     1.Use button                  | 1                  | 1                  |
|     2.Move right shields          | 1                  | 1                  |
|     3.Select author               | 1                  | 1                  |
|     4. Game instructions Polus    | 1                  | 1                  |
|     5.Play Mira   for free        | 1                  | 1                  |

1.Intelligibilty

|     SLT_ARCTIC_FULL_VOICE         |     Evaluator 1    |     Evaluator 2    |
|-----------------------------------|--------------------|--------------------|
|     1.Use button                  | 4                  | 5                  |
|     2.Move right shields          | 4                  | 5                  |
|     3.Select author               | 4                  | 4                  |
|     4. Game instructions Polus    | 5                  | 5                  |
|     5.Play Mira   for free        | 5                  | 5                  |

2.Naturalness

|     SLT_ARCTIC_FULL_VOICE         |     Evaluator 1    |     Evaluator 2    |
|-----------------------------------|--------------------|--------------------|
|     1.Use button                  | 4                  | 5                  |
|     2.Move right shields          | 4                  | 5                  |
|     3.Select author               | 4                  | 3                  |
|     4. Game instructions Polus    | 5                  | 5                  |
|     5.Play Mira   for free        | 5                  | 5                  |

MEAN OPINION SCORES
| MEAN OPINION SCORE |     SLT_ARCTIC_DEMO    |     SLT_ARCTIC_FULL_VOICE    |
|--------------------|------------------------|------------------------------|
| Intelligibilty     | 1                      | 4.6                          |
| Naturalness        | 1                      | 4.5                          |

### MOS Improvement suggestions
In order to have a more accurate and objective mean opinion scores, it is useful to create models, which are trained based on actual human MOS ratings. Otherwise, you have to  to hire sufficient amount of evaluators, in order to have representative results. 
