from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request , 'index.html')

def removepunc(request):
   djText = request.POST.get('text','defaultt')
   
   print(djText) 
   print(request.POST.get('removepunc','off'))
   removepuncutaion = request.POST.get('removepunc','off')
   allCaps = request.POST.get('allCaps','off')
   removeLine = request.POST.get('newLineRemover','off')
   extraSpaceRemover = request.POST.get('extraSpaceRemover','off')
   countCharacter = request.POST.get('CharacterCount','off')
  
   analyzedd = djText
  
   if removepuncutaion == "on" : 
      analyzedd = ''
      punctuation = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
      
      for char in djText :
        if char not in punctuation :
            analyzedd += char
      
      params = {'purpose' : 'Remove Punctuations' , 'analyzedText' : analyzedd}
      djText = analyzedd
   
   if allCaps == "on" :
      analyzedd = djText.upper() 
      params = {'purpose' : 'Captize the String ' , 'analyzedText' : analyzedd}
      djText = analyzedd

   if removeLine == "on" :
      analyzedd = ''
      for n in djText :
         if n != "\n" and n!='\r' :
           analyzedd = analyzedd + n 
      
      params = {'purpose' : 'Remove Line' , 'analyzedText' : analyzedd}
      djText = analyzedd

   if extraSpaceRemover == 'on':
      analyzedd =''
      for index ,char in enumerate(djText) :
          if not(djText[index] == ' ' and djText[index+1] == ' '):
            analyzedd = analyzedd + char
      params = {'purpose' : 'Rremove Extra Spaces ' , 'analyzedText' : analyzedd}
      djText = analyzedd

   if countCharacter == 'on': 
      counter = 0
      for char in djText:
        counter +=1

      temp = djText+"\ncharacter count = "+ str(counter)  
      params = {'purpose' : 'Counting Characters ' , 'analyzedText' : temp}
    
   else :

      params = {'purpose' : 'No Operation is Performed' , 'analyzedText' : djText} 
   
   return render(request ,'removepunc.html',params)

