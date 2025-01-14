from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import List
from schema import Schema, SchemaError
from models.enums import Relationship, RelationshipBehaviour


class AlgorithmOptions(ABC):
    def __post_init__(self):
        self.validate()

    @abstractmethod
    def validate(self):
        pass


@dataclass
class RandomAlgorithmOptions(AlgorithmOptions):
    def validate(self):
        super().validate()


@dataclass
class WeightAlgorithmOptions(AlgorithmOptions):
    requirement_weight: int
    social_weight: int
    diversity_weight: int
    preference_weight: int
    max_project_preferences: int
    friend_behaviour: RelationshipBehaviour
    enemy_behaviour: RelationshipBehaviour
    diversify_options: List[int] = field(default_factory=list)
    concentrate_options: List[int] = field(default_factory=list)

    def validate(self):
        super().validate()
        try:
            Schema(int).validate(self.requirement_weight)
            Schema(int).validate(self.social_weight)
            Schema(int).validate(self.diversity_weight)
            Schema(int).validate(self.preference_weight)
            Schema(int).validate(self.max_project_preferences)
            Schema(RelationshipBehaviour).validate(self.friend_behaviour)
            Schema(RelationshipBehaviour).validate(self.enemy_behaviour)
            Schema([int]).validate(self.diversify_options)
            Schema([int]).validate(self.concentrate_options)
        except SchemaError as error:
            raise ValueError(f"Error while validating WeightAlgorithmOptions \n{error}")


@dataclass
class PriorityAlgorithmOptions(WeightAlgorithmOptions):
    priorities: List[dict] = field(default_factory=list)

    # TODO: Decide what to do here.
    def validate(self):
        super().validate()


@dataclass
class SocialAlgorithmOptions(WeightAlgorithmOptions):
    def validate(self):
        super().validate()
