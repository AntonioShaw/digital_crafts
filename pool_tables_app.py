pool_tables=[] #global array

sys.path.append(".")

from pool_table_class.py import PoolTable

from datetime import datetime
time=datetime.now()


  
# create 12 pool tables and put them in the array
for index in range (1,13):
  pool_table = from pool_table_class import PoolTable
  pool_tables.append(pool_table)



while True:
  question = input("------------------WELCOME! ARE YOU READY TO BREAK?-----------------------")

  print("----------------------------Choose an Option----------------------------")
  print("1 = Check Out a Pool Table: ")
  print("2 = Check In a Pool Table: ")
  print("3 = View Pool Tables: ")
  print("q = Quit: ")

  choice =input("Make your selection: ")
  if question == "q":
    break
  
  if choice == "1":
    # display all tables
    print(f"Table #{pool_table.number}")
    print(f"Check Out Time{pool_table.start_time}")
  
  
  #  with open("date.txt", "a") as file:
  
  
  
  
  
  #     file.write(question)  
  #     file.write("\n")
  
  # else:
  #   with open ("date.txt") as file_content:
  #     content = file_content.read()
  #     print(content)
  #     break
