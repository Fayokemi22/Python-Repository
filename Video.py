class Video:
    def __init__(self, title, duration, current_position):
        self.title = title
        self.duration = duration
        self.current_position = current_position

    def play(self):
        return f"{self.title} is now playing"

    #fix
    def advance_minutes(self):
        return f"{self.duration} minutes"

    def is_finished(self):
        if self.current_position == self.duration:
            return True
        else:
            return False

    def restart(self):
      if self.is_finished():
           return self.play()
      return not self.is_finished()

    def time_remaining(self):
      return self.duration - self.current_position



