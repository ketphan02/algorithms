import copy
from dataclasses import dataclass, field
from typing import List, Dict

from old.team_formation.app.team_generator.algorithm.priority_algorithm.priority import (
    Priority,
)
from old.team_formation.app.team_generator.algorithm.priority_algorithm.scoring import (
    get_priority_satisfaction_array,
    get_multipliers,
)
from old.team_formation.app.team_generator.student import Student
from old.team_formation.app.team_generator.team import Team

"""
These dataclasses are used only in the priority algorithm.
We could simply use the normal Team and TeamSet classes, but then all of their metadata would be deeply cloned.
Because the priority algorithm deals with mutating teams, deep-cloning team sets is a frequent occurrence and these
    classes enable a more lightweight representation of the data actually needed by the priority algorithm
"""


@dataclass
class PriorityTeam:
    team: Team  # just a reference to the team so team requirements can be found easily without duplicating them
    student_ids: List[int]


@dataclass
class PriorityTeamSet:
    priority_teams: List[PriorityTeam] = field(default_factory=list)

    def __init__(self, *args, **kwargs):
        self.score = None  # not calculated yet

    def clone(self):
        # TODO: keep an eye on this copying properly
        cloned_priority_teams = copy.deepcopy(self.priority_teams)
        return PriorityTeamSet(priority_teams=cloned_priority_teams)

    def calculate_score(
        self, priorities: List[Priority], student_dict: Dict[int, Student]
    ) -> float:
        if self.score:
            return self.score

        priority_satisfaction_array = get_priority_satisfaction_array(
            self.priority_teams, priorities, student_dict
        )
        multipliers = get_multipliers(priorities)
        score = sum(
            [
                satisfaction * multiplier
                for satisfaction, multiplier in zip(
                    priority_satisfaction_array, multipliers
                )
            ]
        )
        self.score = score
        return self.score