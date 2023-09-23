from policyengine_us.model_api import *


class ct_social_security_benefit_adjustment_eligible(Variable):
    value_type = float
    entity = TaxUnit
    unit = USD
    label = "Connecticut social security benefit adjustment eligible"
    definition_period = YEAR
    defined_for = StateCode.CT

    def formula(tax_unit, period, parameters):
        p = parameters(
            period
        ).gov.states.ct.tax.income.subtractions.social_security
        filing_status = tax_unit("filing_status", period)
        agi = add(tax_unit, period, ["adjusted_gross_income"])
        max_amount = p.max_amount[filing_status]
        return agi < max_amount