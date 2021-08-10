class Player(object):
    def __init__(self, name, health, status):
        self.name = name
        self.health = health
        self.status = []
        self.encounter = 1
        self.heal_token = 1

    def get_name(self):
        return self.name

    def get_health(self):
        return self.health

    def get_status(self):
        return self.status

    def get_encounter(self):
        return self.encounter

    def reset_status(self):
        self.status = []

    def set_name(self, name):
        self.name = name

    def set_health(self, health):
        self.health = health

    def set_heal_token(self, heal_token):
        self.heal_token = heal_token

    def change_status(self, status, change):
        if change == "r":
          self.status.remove(status)
        elif change == "a":
          self.status.append(status)
    
    def update_status(self, status):
      if status in self.status:
        self.change_status(status, "r")
        self.change_status(status, "a")
      else:
        self.change_status(status, "a")