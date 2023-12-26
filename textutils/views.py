#SHAIL
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse('''
                        <head>
    <link href="https://fonts.googleapis.com/css?family=Abel" rel="stylesheet">
    <style>
        .h1, .h2, .h3, .h4, .h5, .h6, h1, h2, h3, h4, h5, h6 {
            margin-bottom: .5rem;
            font-family: 'abel', sans-serif;
            font-weight: 700;
            line-height: 1.2;
        }

        body {
            font-size: 1rem;
            background-color: Cyan
        }

        table {
            background-color: #ffffff; /* Set the background color for the table */
        }

        .button {
            display: inline-block;
            padding: 10px;
            text-align: center;
            text-decoration: none;
            background-color: #e0e0e0; /* Set the button background color */
            border: 1px solid #ccc;
            border-radius: 5px;
        }
    </style>
</head>
<body>
    <h1 style="font-family: 'Arial', sans-serif; color: #4CAF50; text-align: left; margin-left: 20px; margin-bottom: 20px; text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5); font-size: 36px; font-weight: bold;">Shail</h1>
    <br>College:</h1><a href="https://www.gecg28.ac.in/">GEC g28</a></h1>
    <h1>Tech learnt From:</h1><a href="https://www.youtube.com/playlist?list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9">Django & playlist</a>
    <h1>Fav Web Series:</h1><a href="https://www.jiocinema.com/tv-shows/asur/3500240">ASUR</a>
    <center>
        <h1><b>Social Media Handles</b></h1>
        <table border="2" style="border-collapse: collapse; width: 400px; text-align: center;">
            <tr>
                <td style="padding: 10px; font-weight: bold; font-style: italic;">Linkedin</td>
                <td style="padding: 10px;"><a href="https://www.linkedin.com/in/shail-shah-11236b248/" target="_blank" class="button"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/81/LinkedIn_icon.svg/2048px-LinkedIn_icon.svg.png" alt="LinkedIn Logo" width="20" height="20"></a></td>
            </tr>
            <tr>
                <td style="padding: 10px; font-weight: bold; font-style: italic;">Instagram</td>
                <td style="padding: 10px;"><a href="https://www.instagram.com/shail_s03_/" target="_blank" class="button"><img src="https://upload.wikimedia.org/wikipedia/commons/9/95/Instagram_logo_2022.svg" alt="Instagram Logo" width="20" height="20"></a></td>
            </tr>
        </table>
    </center>
</body>

''')

def home(request):
    #params={'username':'Alien','place':'Mars'}
    return render(request,'home.html')#,params

def about(request):
        return HttpResponse('''
    <!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>About Us - TextUtilsS</title>
  <style>
    body {
      font-family: 'Arial', sans-serif;
      background-color: #f4f4f4;
      margin: 0;
      padding: 0;
    }

    header {
      background-color: #333;
      color: #fff;
      text-align: center;
      padding: 1rem;
    }

    section {
      max-width: 800px;
      margin: 2rem auto;
      padding: 1.5rem;
      background-color: #fff;
      box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    }

    h2 {
      color: #333;
    }

    p {
      line-height: 1.6;
      color: #555;
    }

    .statistics {
      background-color: #f8f8f8;
      padding: 1.5rem;
      margin-top: 2rem;
      border-radius: 8px;
    }

    .statistics h2 {
      color: #333;
      margin-bottom: 1rem;
    }

    .statistics dl {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 1rem;
    }

    .statistics dt, .statistics dd {
      padding: 0.5rem;
      border: 1px solid #ddd;
      border-radius: 4px;
    }

    .rights-box {
      background-color: #333;
      color: #fff;
      text-align: center;
      padding: 1rem;
      position: fixed;
      bottom: 0;
      width: 100%;
      animation: highlight 5s infinite alternate;
    }

    .created-by {
      margin-top: 1rem;
      transition: color 0.3s ease-in-out;
    }

    .rights-box:hover .created-by {
      color: #1e90ff;
    }

    @keyframes highlight {
      0% {
        background-color: #333;
      }
      25% {
        background-color: #87CEEB; /* Sky Blue */
      }
      50% {
        background-color: #FF6347; /* Tomato Red */
      }
      75% {
        background-color: #DA70D6; /* Orchid */
      }
      100% {
        background-color: #333;
      }
    }

  </style>
</head>
<body>
  <header>
    <h1>TextUtils</h1>
    <p>Your Text Utility App</p>
  </header>

  <section>
    <h2>About Us</h2>
    <p>Welcome to TextUtils, your go-to platform for text-related tools and utilities. Our mission is to make working with text easier, faster, and more efficient. Whether you need to analyze, format, or manipulate text, TextUtils has you covered.</p>

    <h2>Our Mission</h2>
    <p>Welcome to our text utilities page, where we provide a range of text processing services to enhance your content. Our team is dedicated to delivering high-quality and efficient solutions to make your text stand out.</p>

    <h2>Our Achievements</h2>
    <ul>
      <li>Leading in text processing technology</li>
      <li>Over 1 million satisfied users</li>
      <li>99% accuracy in text analysis</li>
    </ul>

    <!-- Statistics Box -->
    <div class="statistics">
      <h2>Statistics</h2>
      <dl>
        <dt>Users Served</dt>
        <dd>1,000,000</dd>
        <dt>Years in Operation</dt>
        <dd>5</dd>
        <dt>Accuracy Rate</dt>
        <dd>99%</dd>
      </dl>
    </div>
  </section>

  <!-- Founding date line -->
  <div class="founding-date">
    <p>TextUtils has been empowering users since December 26, 2023.</p>
  </div>

  <!-- Rights Box with Created By -->
  <div class="rights-box">
    <div class="created-by">
      <p>Created By: <strong>SHAIL SHAH</strong>©</p>
    </div>
    <p>&copy; 2023 TextUtilsS. All rights reserved.</p>
  </div>

</body>
</html>
                            ''')

def analyze(request ):
    #get text
        djtext=request.POST.get('text','default')
        #checkbox
        removepunc=request.POST.get('removepunc','off')
        fullcaps=request.POST.get('fullcaps','off')
        nlr=request.POST.get('nlr','off')
        esr=request.POST.get('esr','off')
        charc=request.POST.get('charc','off')
        
        #print(removepunc)
        #print(djtext)
        if removepunc == "on":
            #analyzed=djtext
            punctuations='''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
            analyzed=""
            for char in djtext:
                if char not in punctuations:
                    analyzed=analyzed+char
            params={'purpose':'Removed Punctuations','analyzed_Text':analyzed}
            djtext=analyzed
            #return render(request,'analyze.html',params)
        #elif
        if (fullcaps=="on"):
            analyzed=""
            for char in djtext:
                analyzed =  analyzed+char.upper()
            params={'purpose':' Changed to Uppercase','analyzed_Text':analyzed}
            djtext=analyzed
            #return render(request,'analyze.html',params)
        if (nlr=="on"):
            analyzed=""
            for char in djtext:
                if char != "\n" and char != "\r":
                    analyzed =  analyzed+char
                else:
                    print("No")
            print("pre",analyzed)
            params={'purpose':' Removed NewLines','analyzed_Text':analyzed}
            #print(params)
            djtext=analyzed
            #return render(request,'analyze.html',params)
        if (esr=="on"):
            analyzed=""
            for index,char in enumerate(djtext):
                #if djtext[index]== " " and djtext[index+1]==" " :
                #   pass
                #else: 
                if not(djtext[index]== " " and djtext[index+1]==" " ):
                    analyzed =  analyzed+char
            params={'purpose':' Removed NewLines','analyzed_Text':analyzed}
            djtext=analyzed
            #return render(request,'analyze.html',params)
        if (charc=="on"):
            analyzed=len(djtext)
            params={'purpose':' Counting length','analyzed_Text':analyzed}
            #djtext=analyzed
            #return render(request,'analyze.html',params)
        #else:
        #    return HttpResponse("Error")
        
        if (removepunc !="on" and fullcaps!="on" and nlr!="on" and esr!="on"
            and charc!="on" ):
            return HttpResponse("Select atleast one to get OUTPUT")
        
        return render(request,'analyze.html',params)

def contact(request):
    #params={'username':'Alien','place':'Mars'}
    return render(request,'ContactUsTUS.html')#,param

#def capfirst(request):
 #       return HttpResponse("capitalize first")

#def newlineremove(request):
 #       return HttpResponse("Newline remover")

#def spaceremove(request):
#        return HttpResponse("space remover")

#def charcount(request):
 #       return HttpResponse("char count")