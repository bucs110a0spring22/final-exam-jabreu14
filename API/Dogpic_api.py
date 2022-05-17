import requests

class Dogpic_api:
  def __init__(self):
    '''
    Uses self to save the API url as an instance variable
    Args: None
    Return: None
    
    
    '''
    self.api_url = 'https://random.dog/woof.json'

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
    Return: (str), returns the dictionary of dog image urls.
    
    
    '''
    return self.result