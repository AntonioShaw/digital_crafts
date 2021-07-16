class PoolTable:
  def __init__(self, number, current_time):
    self.number=number
    self.is_occupied=False
    #self.current_time=current_time
    self.start_time=start_time
    #self.end_time=end_time
    #self.time_played=end_time - start_time

  def check_out(self):
    self.is_occupied = True
    self.start_time = datetime.now()
    self.save_to_file()

  def save_to_file(self):
    with open("pool_tables.txt", "w") as file:
      file.write(str(self.number))
      # Convert date to string 
      file.write("07/15/2021 9:45 AM")
