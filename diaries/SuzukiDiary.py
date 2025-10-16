from diaries.AbstractDiary import AbstractDiary
class SuzukiDiary(AbstractDiary):
    def get_date(self): # type: ignore
        return "2025-10-16"
    def get_summary(self): # type: ignore
        return "github難しい"
    def get_author(self): # type: ignore
        return "Suzuki"