import random
from API import Randomfact_api
from API import Catfact_api
from API import Dogfact_api
from API import Dogpic_api
from API import Stoic_api
from API import Kanye_api

def main():
  
    
    answer = str(input("Do you want a random fun fact?\n"))
    if answer == "yes" or answer == "Yes":
      api = Randomfact_api.Randomfact_api()
      api.get()
      data = api.__str__()
      print(data['text'])
    elif answer =="no" or answer == "No":
      answer2 = str(input("How about a random cat fact?\n"))
      
      if answer2 == "yes" or answer2 == "Yes":
          api = Catfact_api.Catfact_api()
          api.get()
          data = api.__str__()
          print(data[random.randint(0,4)]['text'])
      elif answer2 =="no" or answer2 == "No":
          answer3 = str(input("Yeah, I'm more of a dog person myself. How about a random dog fact?\n"))
      
          if answer3 == "yes" or answer3 == "Yes":
            api = Dogfact_api.Dogfact_api()
            api.get()
            data = api.__str__()
            image = Dogpic_api.Dogpic_api()
            image.get()
            images = image.__str__()
            print(data['facts'])
            print("Here is a cool dog picture: ",images['url'], " click on it...")
          elif answer3 == "no" or answer3 == "No":   
            answer4 = str(input("Huh... not a big animal guy I see. What about a random Kanye quote?\n"))
        
            if answer4 == "yes" or answer4 == "Yes":
              api = Kanye_api.Kanye_api()
              api.get()
              data = api.__str__()
              print(data['quote'], '\n...yes, yes truly inspirational')
            elif answer4 == "no" or answer4 == "No":
              answer5 = str(input("I see... not your style I get it, how about a powerful stoic quote?\n"))
            
              if answer5 == "yes" or answer5 == "Yes":
                    api = Stoic_api.Stoic_api()
                    api.get()
                    data = api.__str__()
                    print(data['data']['quote'])
              elif answer5 == "no" or answer5 == "No":
                print("You know what? I'm leaving!\n")
            
            
   




                    
main()

  
  # try:
  #   fact = API1.API1()
  # except: 
  #   return None
  # else: 
  #   print(fact.animefact())















  
    # #r is a request oject
    # r = requests.get('https://anime-facts-rest-api.herokuapp.com/api/v1')
    # #r.json() to get the returned json data from the object
    # trivia = r.json() #converts the data to a dictionary
    # #returns the top level of the object
    # print(type(trivia), trivia)
    
    # #get the first result from trivia and print
    

