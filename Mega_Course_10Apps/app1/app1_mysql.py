import mysql.connector

con = mysql.connector.connect(
    user = "ardit700_student",
    password = "ardit700_student",
    host = "108.167.140.122",
    database = "ardit700_pm1database"
)

def translate(word) :

    word = word.lower().strip()
    
    cursor = con.cursor()
    query = cursor.execute(f"SELECT Definition FROM Dictionary WHERE Expression = '{word}' ")
    results = cursor.fetchall()

    if results:
        return(results)
    
    else:
        # get all words in order to find similar ones
        query = cursor.execute("SELECT Expression FROM Dictionary")
        results = cursor.fetchall()




    

word = input("What would you like to know? ")

output = translate(word)

for res in output:
    print(res[0])




