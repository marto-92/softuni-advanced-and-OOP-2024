from typing import Dict


class Player:

    def __init__(self, name: str, hp: int, mp: int):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills: Dict[str: int] = {}
        self.guild = "Unaffiliated"

    def add_skill(self, skill, mana) -> str:
        if skill in self.skills:
            return "Skill already added"

        self.skills[skill] = self.skills.get(skill, 0) + mana

        return f"Skill {skill} added to the collection of the player {self.name}"

    def player_info(self) -> str:
        skills = '\n'.join(f'==={s} - {m}' for s, m in self.skills.items())

        return f"Name: {self.name}\n" \
               f"Guild: {self.guild}\n" \
               f"HP: {self.hp}\n" \
               f"MP: {self.mp}\n" \
               f"{skills}"
