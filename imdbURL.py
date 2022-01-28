import requests
import json


def giveURL(movie, year):
  #use string replace to format movie title for url
  strpmvie = movie.replace(' ', '+')
  strpmvie = movie.replace("//'", "'")
  
  #query omdb api for the imdb id of movie
  respString = 'http://www.omdbapi.com/?s='+ strpmvie + '&type=movie' +'&apikey=18325552'
  r = requests.get(respString)
  #put api response into json format
  dictionary = r.json()
  
  upperBound=5
  imdbURL="NA"
  if ('Search' in dictionary) and len(dictionary['Search']) >= 1:
      for i in range(0, len(dictionary['Search'])):
          movieYear=dictionary['Search'][i]['Year']
          if  movieYear <= year and (int(year)-int(movieYear) <= upperBound):
            imdbURL = "https://www.imdb.com/title/" + dictionary['Search'][i]['imdbID']
            break
  
  #put imdb id into the imdb movie url to get their webpage for the given movie and return the result
  return(imdbURL)



if __name__ == '__main__':
   
    
    '''
    Possible errors: 
    The movie title input must be formatted to not have spaces at the end or beginning or have any other errors

    No error checking has been done yet for anything

    Should provide a "Movie not found" error as default
    '''
