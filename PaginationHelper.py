import math
class PaginationHelper:

  # The constructor takes in an array of items and a integer indicating
  # how many items fit within a single page
  def __init__(self, collection, items_per_page):
      self.collection=collection
      self.items_per_page=items_per_page
  
  # returns the number of items within the entire collection
  def item_count(self):
      return len(self.collection)
  
  # returns the number of pages
  def page_count(self):
      x=self.item_count()
      count=0
      while  x>self.items_per_page:
          x=x-self.items_per_page
          count+=1
      if x!=0:
          count+=1
      return count          
  # returns the number of items on the current page. page_index is zero based
  # this method should return -1 for page_index values that are out of range
  def les(self):
      lis= [self.collection[i:i + self.items_per_page] for i in range(0, len(self.collection), self.items_per_page)]
      return lis

  def page_item_count(self,page_index):
      v=self.page_count()
      index=range(v)
      if page_index not in index:
          return -1
      lis=self.les()
      return len(lis[page_index]) 
           
  # determines what page an item is on. Zero based indexes.
  # this method should return -1 for item_index values that are out of range
  def page_index(self,item_index):
      if item_index not in range(len(self.collection)):
          return -1
      else: return math.ceil((item_index + 1)/self.items_per_page) - 1
      
    
        