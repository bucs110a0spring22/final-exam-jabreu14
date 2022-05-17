import requests

class Randomfact_api:
  def __init__(self):
    '''
    Uses self to save the API url as an instance variable
    Args: None
    Return: None
    
    
    '''
    self.api_url = 'https://uselessfacts.jsph.pl/random.json?language=en'

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
    Return: (str), returns the dictionary of random facts
    
    
    '''
    return self.result

  # def displayfact(self):
  #   api = self.randomfact()
  #   api.get()
  #   data = api.randomfact()
  #   return data['text']