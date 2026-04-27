from basic_programs.myexception import AgeException


class AgeCalculation():
    def voting_age_check(self, age):
        if age < 18:
            raise AgeException('Not Eligible to vote')
        else:
            return True

    def pension_age_check(self, age):
        if age < 60:
            raise AgeException('Not eligible for pension...')
        else:
            return True
