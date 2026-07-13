import fitz

class PDFLoader:

  def Load(self, file_path):
      doc = fitz.open(file_path)

      text = ""

      for page in doc:
          text += page.get_text()

      return text