#!/usr/bin/python

from __future__ import division
""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
print len(enron_data)
print len(enron_data["SKILLING JEFFREY K"])

print sum([enron_data[i]['poi'] for i in enron_data])

print enron_data['PRENTICE JAMES']['total_stock_value']
print enron_data['COLWELL WESLEY']['from_this_person_to_poi']
print enron_data['SKILLING JEFFREY K']['exercised_stock_options']

print enron_data['SKILLING JEFFREY K']['total_payments']
print enron_data['FASTOW ANDREW S']['total_payments']
print enron_data['LAY KENNETH L']['total_payments']

print len([i for i in enron_data if enron_data[i]['salary'] != 'NaN'])
print len([i for i in enron_data if enron_data[i]['email_address'] != 'NaN'])
print len([i for i in enron_data if enron_data[i]['total_payments'] == 'NaN'])/len(enron_data)

print sum([enron_data[i]['poi'] for i in enron_data if enron_data[i]['total_payments'] == 'NaN'])/len(enron_data)