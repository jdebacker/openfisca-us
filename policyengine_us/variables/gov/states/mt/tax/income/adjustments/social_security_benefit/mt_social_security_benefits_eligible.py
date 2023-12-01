from policyengine_us.model_api import *


class mt_social_security_benefits_eligible(Variable):
    value_type = float
    entity = TaxUnit
    label = "Eligible for Montana taxable social security benefit"
    unit = USD
    definition_period = YEAR
    reference = (
        "https://www.leg.mt.gov/bills/mca/title_0150/chapter_0300/part_0210/section_0010/0150-0300-0210-0010.html",
        "https://mtrevenue.gov/wp-content/uploads/mdocs/form%202%202021.pdf#page=6",
        "https://mtrevenue.gov/wp-content/uploads/dlm_uploads/2023/05/Montana-Idividiual-Income-Tax-Return-Form-2-2022v6.2.pdf#page=6",
    )
    defined_for = StateCode.MT

    def formula(tax_unit, period, parameters):
        exceeding_income = tax_unit(
            "mt_social_security_benefits_exceeding_income", period
        )
        modified_income = tax_unit("mt_modified_income", period)
        return (exceeding_income >= 0) & (modified_income >= 0)
