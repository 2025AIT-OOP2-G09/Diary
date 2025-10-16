from diaries.AbstractDiary import AbstractDiary
class IshigamiDiary(AbstractDiary):
    def get_date(self): # type: ignore
        return "2025-10-16"
    def get_summary(self): # type: ignore
        return "Gitは複雑"
    def get_author(self): # type: ignore
        return "Ishigami"