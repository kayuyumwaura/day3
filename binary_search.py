#ceate a function to return a list of numbers
class Binary_Search(object):
  if len (object) == 0:
    return false
  
  def __init__(self, length, step):
    self.list = range(0+step, + 1  , step) 
    self.length = len(self.list) - 1

#a function that returns the count, index and length
  def search(self, number):
    total = 0
    start = 0
    count = 0
    end = len(self.list) - 1
    output_dict = {'count':count, 'index':0, 'len':length }

    #uses divide and conquer to search for the number
    if number not in self.list:
      output_dict['index'] = -1
      return false
    else:
      midpoint = (start + end)/2
      if self.list[start] == number:
        output_dict['index'] = start
        return output_dict
      elif self.list[end] == number:
        output_dict['index'] = end
        return output_dict
      else:
        False