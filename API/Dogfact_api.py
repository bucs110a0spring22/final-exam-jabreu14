import requests

class Dogfact_api:
  def __init__(self):
    '''
    Uses self to save the API url as an instance variable
    Args: None
    Return: None
    
    
    '''
    self.api_url = 'http://dog-api.kinduff.com/api/facts'

  def get(self):
    '''
   Gets the returned json data from the object, and converts that data to a dictionary that is saved to a variable.
    Args: None
    Return: None
    
    
    '''
    r = requests.get(self.api_url)
    self.result = r.json()
    
  def __str__(self):
    '''
    Returns the result of the data that was taken from the API
    Args: None
    Return: (str), returns the dictionary of dog facts
    
    
    '''
    return self.result