# import mrjob
from mrjob.job import MRJob
# create  a class to inherit or take properties from the mrjob class
class Bacon_count(MRJob):
    # create a mapper() function that take (self, _, line) as parameters
   def mapper(self, _, line):
       # loop through each word
       for word in line.split():
           if word.lower() == "bacon":
               yield "bacon", 1
    # reducer function
   def reducer(self, key, values):
       yield key, sum(values)
if __name__ == "__main__":
   Bacon_count.run()
