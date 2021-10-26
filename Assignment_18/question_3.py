class PlayerCharacter:
    def __init__(self, max_hp = 10, level = 1) -> None:
        if max_hp < 0:
            max_hp = 10
        else:
            self.max_hp = max_hp


        if level < 1:
            level = 1
        else:
            self.level = level

        self.hp = max_hp

    def __str__(self) -> str:
        return f"Player with {self.hp} HP out of {self.max_hp} HP at level {self.level}"

    def take_damage(self, damage):
        self.hp -= damage
    
    def heal(self, heal_amount):
        self.hp += heal_amount
        
        if self.hp > self.max_hp:
            self.hp = self.max_hp
    
    def level_up(self):
        self.level += 1
        self.max_hp += 3 * self.level
        self.hp = self.max_hp

    def is_dead(self):
        if self.hp < 1:
            return True
        else:
            return False 

player = PlayerCharacter()
print(player)
player.take_damage(5)
print(player)
player.heal(3)
print(player)
player.level_up()
print(player)
player.take_damage(15)
print(player.is_dead())
player.take_damage(2)
print(player)
print(player.is_dead())
player.heal(50)
print(player)