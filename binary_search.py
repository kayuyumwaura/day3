class Binary_Search(object):
  
  def __init__(self, length, step):
    self.list = range(0+step, list*step + 1  , step)
    object.__init__(self, self.list)
    self.length = len(self.list) - 1

  def search(self, number):
    total = 0
    start = 0
    count = 0
    end = len(self.list) - 1
    output_dict = {'count':count, 'index':0, 'len':length }

    if number not in self.list:
      output_dict['index'] = -1
      return output_dict
    else:
      midpoint = (start + end)/2
      if self.list[start] == number:
        output_dict['index'] = start
        return output_dict
      elif self.list[end] == number:
        output_dict['index'] = end
        return output_dict
      elif self.list[midpoint] == number:
        output_dict['index'] == midpoint
        output_dict['count'] +=1
      else:
        