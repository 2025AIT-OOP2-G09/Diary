from diaries.AbstractDiary import AbstractDiary
class DiarySample(AbstractDiary):
    def get_date(self): # type: ignore
        return "2021-12-01"
    def get_summary(self): # type: ignore
        return "なにもない一日だった"
    def get_author(self): # type: ignore
        return "Sample"