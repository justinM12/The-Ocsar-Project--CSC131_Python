from imdbURL import giveURL
import json
import unittest

#print (giveURL("The Devil's Holiday", "1930"))

class MyTest(unittest.TestCase):
    # only test for movies
    def test_giveURL(self):
        x = giveURL("300", "2006")
        y = giveURL("Scooby Doo", "2002")
        z = giveURL("titanic", "1997")
        a = giveURL("Before Night Falls", "2000")
        
        
        self.assertEqual(x, "https://www.imdb.com/title/tt0416449")
        self.assertEqual(y, "https://www.imdb.com/title/tt0267913")
        self.assertEqual(z, "https://www.imdb.com/title/tt0120338")
        self.assertEqual(a, "https://www.imdb.com/title/tt0247196")
        
unittest.main() 