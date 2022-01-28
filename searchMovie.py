import json

with open('oscar.json') as f:
    data=json.load(f)

# pass in par and an array of dictionaries containing movie info
# returns array of dictionaries 
# the dictionaries hold info about a particular movie
# the movie category field are in upper case
def searchByName(par, d):
    resultsDict={}
    arr=[]
    for i in range(0,len(d)):
        val = d[i]['film']
        if par.upper() in val.upper():
            if not val in resultsDict:
                if type(d[i]['category']) is list:
                    resultsDict[val]={
                        "year":d[i]['year'],
                        "category":d[i]['category'],
                        "name":d[i]['name'],
                        "film":d[i]['film'],
                        "winner":d[i]['winner']
                    }
                    arr.append(resultsDict[val])
                else:
                    resultsDict[val]={
                        "year":d[i]['year'],
                        "category":[d[i]['category']],
                        "name":d[i]['name'],
                        "film":d[i]['film'],
                        "winner":d[i]['winner']
                    }
                    arr.append(resultsDict[val])
            else:
                if not type(d[i]['category']) is list:
                    resultsDict[val]['category'].append(d[i]['category'])
    return arr
    
def searchByCategory(par, d):
    resultsDict={}
    arr=[]
    par=par.upper()
    for i in range(0,len(d)):
        val = d[i]['category']
        nVal = d[i]['film']
        
        if not nVal in resultsDict:
            if type(val) is list:
                for j in range(0,len(val)):
                    if par in val[j]:
                        resultsDict[nVal]={
                            "year":d[i]['year'],
                            "category":d[i]['category'],
                            "name":d[i]['name'],
                            "film":d[i]['film'],
                            "winner":d[i]['winner']
                        }
                        arr.append(resultsDict[nVal])
                        break
            else:
                if par in val:
                    resultsDict[nVal]={
                        "year":d[i]['year'],
                        "category":[d[i]['category']],
                        "name":d[i]['name'],
                        "film":d[i]['film'],
                        "winner":d[i]['winner']
                    }
                    arr.append(resultsDict[nVal])
        elif nVal in resultsDict:
            #add other categories to movie
            if not type(val) is list:
                resultsDict[nVal]['category'].append(val)
                
    return arr

#may need to get rid of name field (we dosent relly have any relevance now)   
def searchByYear(par, d):
    resultsDict={}
    arr=[]
    for i in range(0,len(d)):
        val = d[i]['year']
        nVal = d[i]['film']
        if par == val:
            if not nVal in resultsDict:
                if type(d[i]['category']) is list:
                    resultsDict[nVal]={
                        "year":d[i]['year'],
                        "category":d[i]['category'],
                        "name":d[i]['name'],
                        "film":d[i]['film'],
                        "winner":d[i]['winner']
                    }
                    arr.append(resultsDict[nVal])
                    
                else:
                    resultsDict[nVal]={
                        "year":d[i]['year'],
                        "category":[d[i]['category']],
                        "name":d[i]['name'],
                        "film":d[i]['film'],
                        "winner":d[i]['winner']
                    }
                    arr.append(resultsDict[nVal])
            elif nVal in resultsDict:
                if not type(d[i]['category']) is list:
                    resultsDict[nVal]['category'].append(d[i]['category'])
                
    return arr

def searchByWinner(par, d):
    if type(par) != bool:
        print("error, value passed to searchByWinner must be a bool")
    resultsDict={}
    arr=[]
    for i in range(0,len(d)):
        val = d[i]['winner']
        nVal = d[i]['film']
        if par == val:
            if not nVal in resultsDict:
                if type(d[i]['category']) is list:
                    resultsDict[nVal]={
                        "year":d[i]['year'],
                        "category":d[i]['category'],
                        "name":d[i]['name'],
                        "film":d[i]['film'],
                        "winner":d[i]['winner']
                    }
                    arr.append(resultsDict[nVal])
                    
                else:
                    resultsDict[nVal]={
                        "year":d[i]['year'],
                        "category":[d[i]['category']],
                        "name":d[i]['name'],
                        "film":d[i]['film'],
                        "winner":d[i]['winner']
                    }
                    arr.append(resultsDict[nVal])
            elif nVal in resultsDict:
                if not type(d[i]['category']) is list:
                    resultsDict[nVal]['category'].append(d[i]['category'])
                  
    return arr

if __name__ == '__main__':

    #manual tests   
    #print(searchByCategory("BEST PICTURE", data))
    #print(searchByYear(1934, data))
    #print(searchByWinner(True, data))
    #print(searchByCategoryAndYear("BEST PICTURE", 1989, data))
    #print(searchByName("Iron", data))
    #print(searchByName("Iron", data))
    #print( json.dumps(searchByCategory("BEST PICTURE", searchByYear(1997, data))) )  
    
    print("printing from searchMovie.py")
    