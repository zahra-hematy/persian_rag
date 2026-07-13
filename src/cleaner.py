import re


class TextCleaner:

    def clean(self, text):

        text = text.replace('ي', 'ی')
        text = text.replace('ك', 'ک')
        # delete extra spaces
        text = re.sub(r'[ \t]+', ' ', text)
        text = re.sub(r'\n\s*\n+', '\n\n', text)

        return text.strip()