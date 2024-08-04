#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/adjust_results4_isadog.py
#                                                                             
# PROGRAMMER: Chaklader Asfak Arefe
# DATE CREATED: August 3, 2024
# REVISED DATE: August 3, 2024
# PURPOSE: Create a function adjust_results4_isadog that adjusts the results
#          dictionary to indicate whether or not the pet image label is of-a-dog,
#          and to indicate whether or not the classifier image label is of-a-dog.

def adjust_results4_isadog(results_dic, dogfile):
    """
    Adjusts the results dictionary to determine if classifier correctly
    classified images 'as a dog' or 'not a dog' especially when not a match.
    Demonstrates if model architecture correctly classifies dog images even if
    it gets dog breed wrong (not a match).
    Parameters:
      results_dic - Dictionary with key as image filename and value as a list
      dogfile - A text file with names of all dogs from the classifier function
                and dog names from the pet image files.
    Returns:
           None - results_dic is mutable data type so no return needed.
    """
    # Creates dognames dictionary for quick matching to results_dic labels
    dognames_dic = dict()

    # Reads in dognames from file, 1 name per line & automatically closes file
    with open(dogfile, "r") as infile:
        # Reads in dognames from first line in file
        line = infile.readline()

        while line != "":
            # Process line by striping newline from line
            line = line.strip()

            # Add dogname to dogsnames_dic if it doesn't already exist
            if line not in dognames_dic:
                dognames_dic[line] = 1

            # Reads in next line in file to be processed
            line = infile.readline()

    # Adjust results dictionary adding two new keys at the end of the list
    for key in results_dic:
        # Pet Image Label IS of Dog (e.g. found in dognames_dic)
        if results_dic[key][0] in dognames_dic:
            # Classifier Label IS image of Dog (e.g. found in dognames_dic)
            if results_dic[key][1] in dognames_dic:
                results_dic[key].extend((1, 1))
            # Classifier Label IS NOT image of dog
            else:
                results_dic[key].extend((1, 0))

        # Pet Image Label IS NOT a Dog image (e.g. NOT found in dognames_dic)
        else:
            # Classifier Label IS image of Dog
            if results_dic[key][1] in dognames_dic:
                results_dic[key].extend((0, 1))
            # Classifier Label IS NOT image of Dog
            else:
                results_dic[key].extend((0, 0))