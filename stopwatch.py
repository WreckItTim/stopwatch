from time import time
# simple stopwatch to time whatevs, in (float) seconds
# keeps track of laps along with final time
class Stopwatch:
  def __init__(self):
    self.start_time = time.time()
    self.last_time = self.start_time
    self.laps = []
  def lap(self):
    this_time = time.time()
    delta_time = this_time - self.last_time
    self.laps.append(delta_time)
    self.last_time = this_time
    return delta_time
  def stop(self):
    self.stop_time = time.time()
    self.delta_time = self.stop_time - self.start_time
    return self.delta_time