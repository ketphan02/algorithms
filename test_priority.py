from algorithm_sandbox.encoder import DATA_FILE_PATH
from algorithm_sandbox.logger import Logger
from algorithm_sandbox.mock_team_generation import mock_generation
from team_formation.app.team_generator.algorithm.algorithms import AlgorithmOptions
from team_formation.app.team_generator.algorithm.priority_algorithm.priority import Priority
from team_formation.app.team_generator.algorithm.priority_algorithm.priority_algorithm import PriorityAlgorithm

if __name__ == '__main__':
    logger = Logger(real=True)
    algorithm_options = AlgorithmOptions(
        priorities=[
            {
                'order': 1,
                'constraint': Priority.TYPE_DIVERSIFY,
                'skill_id': 73,
                'limit_option': Priority.MIN_OF,
                'limit': 2,
                'value': 3,
            }
        ],
        diversify_options=[{'id': 73}]
    )
    teams = mock_generation(PriorityAlgorithm, algorithm_options, logger, 56, DATA_FILE_PATH)
    logger.end()
    logger.print_teams(teams, with_relationships=True, only_unmet=True)
