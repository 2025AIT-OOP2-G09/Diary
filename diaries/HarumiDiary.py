from diaries.AbstractDiary import AbstractDiary
class HarumiDiary(AbstractDiary):
    def get_date(self): # type: ignore
        return "2025-10-16"
    def get_summary(self): # type: ignore
        return "リーダー仕事多くないか"
    def get_author(self): # type: ignore
        return "Sample"