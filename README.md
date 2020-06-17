open cmd-
cd Desktop
git clone (paste the clone link from github)
cd Retail-Banking
venv\Scripts\activate
pip install -r requirements.txt
mongoimport --jsonArray --db banking --collection user --file user.json
flask run


login demo user-

1.user_id":"DT20195490747","password":"subhankar@1234","work":"executive"
2.user_id":"CT20192697557","password":"priyansha@1234","work":"executive"
3.user_id":"CT20182443036","password":"snehalatha@1234","work":"executive"
4.user_id":"DT20195554899","password":"aniruddha@1234","work":"cashier"

