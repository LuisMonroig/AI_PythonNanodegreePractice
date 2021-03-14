#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/calculates_results_stats.py
#                                                                             
# PROGRAMMER:
# DATE CREATED:                                  
# REVISED DATE: 
# PURPOSE: Create a function calculates_results_stats that calculates the 
#          statistics of the results of the programrun using the classifier's model 
#          architecture to classify the images. This function will use the 
#          results in the results dictionary to calculate these statistics. 
#          This function will then put the results statistics in a dictionary
#          (results_stats_dic) that's created and returned by this function.
#          This will allow the user of the program to determine the 'best' 
#          model for classifying the images. The statistics that are calculated
#          will be counts and percentages. Please see "Intro to Python - Project
#          classifying Images - xx Calculating Results" for details on the 
#          how to calculate the counts and percentages for this function.    
#         This function inputs:
#            -The results dictionary as results_dic within calculates_results_stats 
#             function and results for the function call within main.
#         This function creates and returns the Results Statistics Dictionary -
#          results_stats_dic. This dictionary contains the results statistics 
#          (either a percentage or a count) where the key is the statistic's 
#           name (starting with 'pct' for percentage or 'n' for count) and value 
#          is the statistic's value.  This dictionary should contain the 
#          following keys:
#            n_images - number of images
#            n_dogs_img - number of dog images
#            n_notdogs_img - number of NON-dog images
#            n_match - number of matches between pet & classifier labels
#            n_correct_dogs - number of correctly classified dog images
#            n_correct_notdogs - number of correctly classified NON-dog images
#            n_correct_breed - number of correctly classified dog breeds
#            pct_match - percentage of correct matches
#            pct_correct_dogs - percentage of correctly classified dogs
#            pct_correct_breed - percentage of correctly classified dog breeds
#            pct_correct_notdogs - percentage of correctly classified NON-dogs
#
##
# TODO 5: Define calculates_results_stats function below, please be certain to replace None
#       in the return statement with the results_stats_dic dictionary that you create 
#       with this function
# 
def calculates_results_stats(results_dic):
    """
    Calculates statistics of the results of the program run using classifier's model 
    architecture to classifying pet images. Then puts the results statistics in a 
    dictionary (results_stats_dic) so that it's returned for printing as to help
    the user to determine the 'best' model for classifying images. Note that 
    the statistics calculated as the results are either percentages or counts.
    Parameters:
      results_dic - Dictionary with key as image filename and value as a List 
             (index)idx 0 = pet image label (string)
                    idx 1 = classifier label (string)
                    idx 2 = 1/0 (int)  where 1 = match between pet image and 
                            classifer labels and 0 = no match between labels
                    idx 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and 
                            0 = pet Image 'is-NOT-a' dog. 
                    idx 4 = 1/0 (int)  where 1 = Classifier classifies image 
                            'as-a' dog and 0 = Classifier classifies image  
                            'as-NOT-a' dog.
    Returns:
     results_stats_dic - Dictionary that contains the results statistics (either
                    a percentage or a count) where the key is the statistic's 
                     name (starting with 'pct' for percentage or 'n' for count)
                     and the value is the statistic's value. See comments above
                     and the previous topic Calculating Results in the class for details
                     on how to calculate the counts and statistics.
    """        

    results_stats_dic = {"n_dogs_img":int(0), "n_notdogs_img":int(0), "n_match":int(0),
                         "n_correct_dogs":int(0), "n_correct_notdogs":int(0), "n_correct_breed":int(0)}

    results_stats_dic["n_images"] = len(results_dic) 

    for value in list(results_dic.values()):
        if value[3] == 1:
            results_stats_dic["n_dogs_img"] += 1 
        elif value[3] == 0:
            results_stats_dic["n_notdogs_img"] += 1

        if value[2] == 1:
            results_stats_dic["n_match"] += 1 

        if value[3] == 1 and value[4] == 1:
            results_stats_dic["n_correct_dogs"] += 1 
        if value[3] == 0 and value[4] == 0:
            results_stats_dic["n_correct_notdogs"] += 1 

        if  value[3] == 1 and value[2] == 1:
            results_stats_dic["n_correct_breed"] += 1 
    results_stats_dic["pct_match"] = (results_stats_dic["n_match"]/results_stats_dic["n_images"])*100

    results_stats_dic["pct_correct_dogs"] = (results_stats_dic["n_correct_dogs"]/results_stats_dic["n_dogs_img"])*100

    results_stats_dic["pct_correct_breed"] = (results_stats_dic["n_correct_breed"]/results_stats_dic["n_dogs_img"])*100

    results_stats_dic["pct_correct_notdogs"] = (results_stats_dic["n_correct_notdogs"]/results_stats_dic["n_notdogs_img"])*100   

    return results_stats_dic

"""
results_dic = {'Dalmatian_04037.jpg': ['dalmatian', 'dalmatian, coach dog, carriage dog', 1, 1, 1], 'Basset_hound_01034.jpg': ['basset hound', 'basset, basset hound', 1, 1, 1], 'polar_bear_04.jpg': ['polar bear', 'ice bear, polar bear, ursus maritimus, thalarctos maritimus', 1, 0, 0], 'Poodle_07927.jpg': ['poodle', 'standard poodle, poodle', 1, 1, 1], 'Golden_retriever_05182.jpg': ['golden retriever', 'golden retriever', 1, 1, 1], 'Golden_retriever_05223.jpg': ['golden retriever', 'golden retriever', 1, 1, 1], 'Great_pyrenees_05367.jpg': ['great pyrenees', 'kuvasz', 0, 1, 1], 'Great_dane_05320.jpg': ['great dane', 'great dane', 1, 1, 1], 'Saint_bernard_08010.jpg': ['saint bernard', 'saint bernard, st bernard', 1, 1, 1], 'Golden_retriever_05195.jpg': ['golden retriever', 'golden retriever', 1, 1, 1], 'Boxer_02426.jpg': ['boxer', 'boxer', 1, 1, 1], 'gecko_02.jpg': ['gecko', 'banded gecko, gecko', 1, 0, 0], 'cat_01.jpg': ['cat', 'lynx', 0, 0, 0], 'Basenji_00974.jpg': ['basenji', 'basenji', 1, 1, 1], 'Boston_terrier_02285.jpg': ['boston terrier', 'boston bull, boston terrier', 1, 1, 1], 'Rabbit_002.jpg': ['rabbit', 'wood rabbit, cottontail, cottontail rabbit, rabbit', 1, 0, 0], 'Beagle_01170.jpg': ['beagle', 'walker hound, walker foxhound', 0, 1, 1], 'German_shepherd_dog_04890.jpg': ['german shepherd dog', 'german shepherd, german shepherd dog, german police dog, alsatian', 1, 1, 1], 'Dalmatian_04017.jpg': ['dalmatian', 'dalmatian, coach dog, carriage dog', 1, 1, 1], 'German_shepherd_dog_04931.jpg': ['german shepherd dog', 'german shepherd, german shepherd dog, german police dog, alsatian', 1, 1, 1], 'Boston_terrier_02303.jpg': ['boston terrier', 'boston bull, boston terrier', 1, 1, 1], 'fox_squirrel_01.jpg': ['fox squirrel', 'fox squirrel, eastern fox squirrel, sciurus niger', 1, 0, 0], 'German_shorthaired_pointer_04986.jpg': ['german shorthaired pointer', 'german shorthaired pointer', 1, 1, 1], 'great_horned_owl_02.jpg': ['great horned owl', 'ruffed grouse, partridge, bonasa umbellus', 0, 0, 0], 'Beagle_01125.jpg': ['beagle', 'beagle', 1, 1, 1], 'Saint_bernard_08036.jpg': ['saint bernard', 'saint bernard, st bernard', 1, 1, 1], 'Beagle_01141.jpg': ['beagle', 'beagle', 1, 1, 1], 'Great_pyrenees_05435.jpg': ['great pyrenees', 'great pyrenees', 1, 1, 1], 'Cocker_spaniel_03750.jpg': ['cocker spaniel', 'cocker spaniel, english cocker spaniel, cocker', 1, 1, 1], 'Basenji_00963.jpg': ['basenji', 'basenji', 1, 1, 1], 'skunk_029.jpg': ['skunk', 'skunk, polecat, wood pussy', 1, 0, 0], 'Dalmatian_04068.jpg': ['dalmatian', 'dalmatian, coach dog, carriage dog', 1, 1, 1], 'Golden_retriever_05257.jpg': ['golden retriever', 'golden retriever', 1, 1, 1], 'cat_02.jpg': ['cat', 'tabby, tabby cat, cat', 1, 0, 0], 'Miniature_schnauzer_06884.jpg': ['miniature schnauzer', 'miniature schnauzer', 1, 1, 1], 'gecko_80.jpg': ['gecko', 'tailed frog, bell toad, ribbed toad, tailed toad, ascaphus trui', 0, 0, 0], 'Poodle_07956.jpg': ['poodle', 'standard poodle, poodle', 1, 1, 1], 'Boston_terrier_02259.jpg': ['boston terrier', 'boston bull, boston terrier', 1, 1, 1], 'cat_07.jpg': ['cat', 'egyptian cat, cat', 1, 0, 0], 'Collie_03797.jpg': ['collie', 'collie', 1, 1, 1]} 

print(calculates_results_stats(results_dic))
"""