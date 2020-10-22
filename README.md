# Mendeley Citations
Simple code to find which references you haven't yet used in Mendeley.

Say you have a folder in Mendeley with 200 documents. This folder was created for a research paper. You're nearing the end of the paper, and you realize you've only used 150 documents. There's no easy way to find which 50 documents you missed! I made some python code to solve that problem, and I have also created a .exe file to run on any Windows system.

Please feel free to use this tool to help with your research!

### How to use: 
1. If you have python on your computer, download Citations.py, otherwise download Citations.exe
1. Create a file named "Mendeley.txt" in the same file as the downloaded file
2. Copy the formatted citations from Mendeley into the text file. You can select all the files, right-click, and click copy formatted citations. You need to set the citation format to something that shows the DOI, such as IEEE.
3. Create another text file named "wordReferences.txt" and copy your Mendeley bibliography from word into the text file. You should now have the Citations.exe or Citations.py file, Mendeley.txt, and wordReferences.txt in one folder. 
4. Run the code. 
5. You will be left with 2 text files:  DUPLICATES.txt which tells you which papers have been cited as two or more separate papers, and
                                        MISSING DOI AND REMAINING CITATIONS.txt which is a list of unused papers and documents with missing DOIs from Mendeley.
                                        
I hope this helps you on your research journey!
