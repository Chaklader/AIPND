#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/calculates_results_stats.py
#
# PROGRAMMER: Chaklader Asfak Arefe
# DATE CREATED: August 3, 2024
# REVISED DATE: August 3, 2024
# PURPOSE: Create a function calculates_results_stats that calculates the
#          statistics of the results of the program run using the classifier's model
#          architecture to classify the images.

def calculates_results_stats(results_dic):
    """
    Calculates statistics of the results of the program run using classifier's model
    architecture to classifying pet images.
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
     results_stats_dic - Dictionary that contains the results statistics
    """
    # Creates empty dictionary for results_stats_dic
    results_stats_dic = dict()

    # Initialize counters
    results_stats_dic['n_dogs_img'] = 0
    results_stats_dic['n_match'] = 0
    results_stats_dic['n_correct_dogs'] = 0
    results_stats_dic['n_correct_notdogs'] = 0
    results_stats_dic['n_correct_breed'] = 0

    # Process through the results dictionary
    for key in results_dic:
        # Labels Match Exactly
        if results_dic[key][2] == 1:
            results_stats_dic['n_match'] += 1

        # Pet Image Label is a Dog AND Labels match- counts Correct Breed
        if results_dic[key][3] == 1 and results_dic[key][2] == 1:
            results_stats_dic['n_correct_breed'] += 1

        # Pet Image Label is a Dog - counts number of dog images
        if results_dic[key][3] == 1:
            results_stats_dic['n_dogs_img'] += 1

            # Classifier classifies image as Dog (& pet image is a dog)
            # counts number of correct dog classifications
            if results_dic[key][4] == 1:
                results_stats_dic['n_correct_dogs'] += 1

        # Pet Image Label is NOT a Dog
        else:
            # Classifier classifies image as NOT a Dog(& pet image isn't a dog)
            # counts number of correct NOT dog clasifications.
            if results_dic[key][4] == 0:
                results_stats_dic['n_correct_notdogs'] += 1

    # Calculates run statistics (counts & percentages)
    results_stats_dic['n_images'] = len(results_dic)
    results_stats_dic['n_notdogs_img'] = (results_stats_dic['n_images'] -
                                          results_stats_dic['n_dogs_img'])

    # Calculates % correct for matches
    results_stats_dic['pct_match'] = (results_stats_dic['n_match'] / results_stats_dic['n_images']) * 100.0

    # Calculates % correct dogs
    results_stats_dic['pct_correct_dogs'] = (results_stats_dic['n_correct_dogs'] / results_stats_dic[
        'n_dogs_img']) * 100.0

    # Calculates % correct breed of dog
    results_stats_dic['pct_correct_breed'] = (results_stats_dic['n_correct_breed'] / results_stats_dic[
        'n_dogs_img']) * 100.0

    # Calculates % correct not-a-dog images
    # Uses conditional statement for when no 'not a dog' images were submitted
    if results_stats_dic['n_notdogs_img'] > 0:
        results_stats_dic['pct_correct_notdogs'] = (results_stats_dic['n_correct_notdogs'] /
                                                    results_stats_dic['n_notdogs_img']) * 100.0
    else:
        results_stats_dic['pct_correct_notdogs'] = 0.0

    return results_stats_dic