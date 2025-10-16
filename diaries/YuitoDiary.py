from diaries.AbstractDiary import AbstractDiary
class YuitoDiary(AbstractDiary):
    def get_date(self): # type: ignore
        return "2025-10-16"
    def get_summary(self): # type: ignore
        return "GitHub難しい"
    def get_author(self): # type: ignore
        return "Yuito"