# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
men = open("mendeley.txt", encoding='utf8')
menText = men.read()
menLines = menText.splitlines()


# %%
word = open("wordReferences.txt", encoding='utf8')
wordText = word.read()
wordLines = wordText.splitlines()


# %%
def findDOI(wordLine):
    'Extract a doi from a citation in string format'
    doiIndex = wordLine.find('doi:')

    if(doiIndex!= -1):
        doi = wordLine[doiIndex+5:-1]
    else:
        doi =''
    return doi


wordDois=[]                         #List of wordDois from Word  
for citation in wordLines:
    doi = findDOI(citation)
    if(len(doi)>0):             #only counts citations where DOI is present
        wordDois.append(doi)
# print(len(wordDois))
# print (len(menLines))


# %%
removeCount=0
for i in range(len(wordDois)-1,-1,-1):      #iterate backwards through wordDois
    doi = wordDois[i]                       #Set a local variable to deal with duplicates?
    changed = False                         #Becomes true if a mendeley citation is removed

    for j in range(len(menLines)-1,-1,-1):  #iterate backwards through wordDois
        
        if (menLines[j].find(doi)!=-1):
            menLines.pop(j)                 #if doi is found in menLines
            changed = True                  #signifies that a Mendeley Citation has been removed
            removeCount+=1
            
    if changed:
        wordDois.pop(i)
noDOI=[]
notCited=[]
for citation in menLines:
    if citation.find("doi:")==-1:
        noDOI.append(citation)
    else:
        notCited.append(citation)

# print(len(wordDois))
# print (len(menLines))
# print (removeCount+len(menLines))   
#Menlines now only has DOIS that haven't been read, or citations without dois


# %%
wordDoiString = '\n'.join(wordDois)
wordDoiString = "These are the DOIs of papers that have been double cited in your paper:\n\n"+ wordDoiString

noDoiString = '\n'.join(noDOI)
noDoiString = "These are the formatted citations of papers in Mendeley that either don't have DOIs. They may or may not be cited in your research paper.\n\n" + noDoiString

notCitedString = '\n'.join(notCited)
notCitedString = "\n\n/////////////////////////////////////////////\n\nThese are the formatted citations of papers in Mendeley that haven't been cited in your research paper.\n\n" + notCitedString

menCitationString = noDoiString + notCitedString
duplicates = open("DUPLICATES.txt",'w+',encoding='utf8')
duplicates.write(wordDoiString)
duplicates.close()

remainingCitations = open("MISSING DOI AND REMAINING CITATIONS.txt",'w+', encoding='utf8')
remainingCitations.write(menCitationString)
remainingCitations.close()


