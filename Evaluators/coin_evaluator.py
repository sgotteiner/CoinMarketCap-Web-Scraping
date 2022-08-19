class Coin_Total_Evaluator:
    def __init__(self, cmc_evaluator: Coin_Market_Cap_Evaluator,
                 website_evaluator: Coin_Website_Evaluator,
                 community_evaluator: Coin_Community_Evaluator,
                 team_evaluator: Team_Evaluator,
                 github_evaluator: Github_Evaluator,
                 collaboration_evaluator: Collaboration_Evaluator,
                 white_paper_evaluator: White_Paper_Evaluator,
                 roadmap_evaluator: Roadmap_Evaluator):
        self.cmc_evaluator = cmc_evaluator
        self.website_evaluator = website_evaluator
        self.community_evaluator = community_evaluator
        self.team_evaluator = team_evaluator
        self.github_evaluator = github_evaluator
        self.collaboration_evaluator = collaboration_evaluator
        self.white_paper_evaluator = white_paper_evaluator
        self.roadmap_evaluator = roadmap_evaluator
