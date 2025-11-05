from dataclasses import dataclass
from typing import Optional, Dict, Self


@dataclass
class LoanApplication:
    applicant_name: str
    amount: float
    term_years: int
    loan_type: Optional[str] = None
    interest_rate: Optional[float] = None
    collateral: Optional[Dict] = None
    employer_name: Optional[str] = None
    annual_income: Optional[float] = None
    existing_debts: Optional[float] = None

    def __str__(self) -> str:
        return (
            f"Loan application for {self.applicant_name}: "
            f"${self.amount:,.2f} over {self.term_years} years"
        )

    def amortization_schedule(self):
        pass


class LoanApplicationBuilder:
    def __init__(self, applicant_name: str, amount: float, term_years: int):
        if not applicant_name or amount <= 0 or term_years <= 0:
            raise ValueError("Invalid required parameters")

        self._application = LoanApplication(
            applicant_name=applicant_name, amount=amount, term_years=term_years
        )

    def set_loan_type(self, loan_type: str) -> Self:
        self._application.loan_type = loan_type
        return self

    def set_interest_rate(self, interest_rate: float) -> Self:
        if interest_rate < 0:
            raise ValueError("Interest rate cannot be negative")
        self._application.interest_rate = interest_rate
        return self

    def set_collateral(self, collateral: Dict) -> Self:
        self._application.collateral = collateral
        return self

    def set_employer_name(self, employer_name: str) -> Self:
        self._application.employer_name = employer_name
        return self

    def set_annual_income(self, annual_income: float) -> Self:
        if annual_income < 0:
            raise ValueError("Annual income cannot be negative")
        self._application.annual_income = annual_income
        return self

    def set_existing_debts(self, existing_debts: float) -> Self:
        if existing_debts < 0:
            raise ValueError("Existing debts cannot be negative")
        self._application.existing_debts = existing_debts
        return self

    def build(self) -> LoanApplication:
        return self._application


if __name__ == "__main__":
    builder = LoanApplicationBuilder("John Doe", 250000, 30)
    loan_application = (
        builder.set_loan_type("Mortgage")
        .set_interest_rate(3.5)
        .set_employer_name("Tech Corp")
        .set_annual_income(85000)
        .set_existing_debts(15000)
        .build()
    )
    print(loan_application)
