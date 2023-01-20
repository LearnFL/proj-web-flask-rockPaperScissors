# Simple Flask App Rock Paper Scissors

#### License
Feel free to use the code but please keep Authorship Attribution.
"This app was made by Dennis Rotnov https://github.com/LearnFL"

#### Purpose
Built very fast, built for fun with a kiddo.

#### Process
Built with Flask. A great example of why JavaScript is suted better for this type of applications. Not only would it simplify the design but also it would run on a client side without making constant requests, and that is a deal breaker. 

#### Coded by 
Dennis Rotnov
#### See Live application 
https://aqueous-ocean-49788.herokuapp.com/index

#### HEROKU
1. Create Procfile with and add this line:   web: gunicorn YourAppName:app
2. requirements.txt, make sure to include gunicorn==YourVersion
3. Create runtime.txt and add: python-3.10.0 (your version)
4. Command line: brew tap heroku/brew && brew install heroku
5. Command line: Heroku login (heroku login -i  if IP is not recognized)
6. Command line: git init
7. Change branch name to main.
8. Command line: git .add 
9. Command line: git commit
10. Command line: heroku create
11. Command line: git push heroku main
12. Command line: heroku open

#### Screenshot
<img width="1441" alt="Screen Shot 2022-08-20 at 4 52 29 PM" src="https://user-images.githubusercontent.com/86169204/185765624-34caf3fc-f135-45ea-8cbb-35669f2759ba.png">
<img width="1441" alt="Screen Shot 2022-08-20 at 4 52 47 PM" src="https://user-images.githubusercontent.com/86169204/185765632-651a99cf-0144-4a2f-8ab8-c19e5e34df4f.png">
<img width="1442" alt="Screen Shot 2022-08-20 at 4 53 02 PM" src="https://user-images.githubusercontent.com/86169204/185765644-021e330a-3623-4ac5-919f-79619e875f0d.png">

