class CoinTotalEvaluator:
    def __init__(self, cmc_evaluator: CoinMarketCapEvaluator,
                 website_evaluator: CoinWebsiteEvaluator,
                 community_evaluator: CoinCommunityEvaluator,
                 team_evaluator: TeamEvaluator,
                 github_evaluator: GithubEvaluator,
                 collaboration_evaluator: CollaborationEvaluator,
                 white_paper_evaluator: WhitePaperEvaluator,
                 roadmap_evaluator: RoadmapEvaluator):
        self.cmc_evaluator = cmc_evaluator
        self.website_evaluator = website_evaluator
        self.community_evaluator = community_evaluator
        self.team_evaluator = team_evaluator
        self.github_evaluator = github_evaluator
        self.collaboration_evaluator = collaboration_evaluator
        self.white_paper_evaluator = white_paper_evaluator
        self.roadmap_evaluator = roadmap_evaluator
