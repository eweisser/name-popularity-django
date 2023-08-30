# name-popularity-django
A Django project for visualizing the relative frequency of first names in the US and conducting additional analysis
This is a successor to a previous project on the same topic (see https://github.com/eweisser/namepopularity); before that, I kept track of similar calculations on Excel. In this work, I wanted first to see if my and others' impressions of regional popularity trends for first names aligned with actual data, but with time, the scope grew dramatically.
This repository consists of the basic files comprising the Django app. Currently, the app facilitates three kinds of analysis:
1. A US map or maps color-coded to indicated relative frequency of a given first name, in a given year
2. A list of first names ordered by frequency relative to other states, for a given US state in a given year
3. The same function as #1 above, featuring a given number of the most popular names in a given year

In the future, I'd like to implement a few more methods of analysis as well as performance improvement.
