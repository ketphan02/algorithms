from old.algorithm_sandbox.metrics.project_metric import satisfied_requirements
from models.team_set import TeamSet
from benchmarking.evaluations.interfaces import TeamSetMetric


class NumRequirementsSatisfied(TeamSetMetric):
    """
    Across all teams, the number of requirements that have been satisfied.
    """

    def calculate(self, team_set: TeamSet) -> float:
        return sum([satisfied_requirements(team) for team in team_set.teams])
