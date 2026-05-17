from project.formula_teams.formula_team import \
    FormulaTeam


class MercedesTeam(FormulaTeam):
    @property
    def get_sponsors(self):
        sponsors = {"Petronas":{1:1_000_000,3:500_000},"Teamviewer": {5:100_000, 7:50_000}}
        return sponsors

    @property
    def get_expenses(self):
        return 200_000