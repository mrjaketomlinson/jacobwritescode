class LoanApplication:
    def __init__(
        self,
        applicant_name,
        amount,
        term_years,
        loan_type=None,
        interest_rate=None,
        collateral=None,
        employer_name=None,
        annual_income=None,
        existing_debts=None,
    ):
        self.applicant_name = applicant_name
        self.amount = amount
        self.term_years = term_years
        self.loan_type = loan_type
        self.interest_rate = interest_rate
        self.collateral = collateral
        self.employer_name = employer_name
        self.annual_income = annual_income
        self.existing_debts = existing_debts

    def __str__(self):
        return (
            f"Loan application for {self.applicant_name}: "
            f"{self.amount} over {self.term_years} years"
        )

    def ammortization_schedule(self):
        pass
