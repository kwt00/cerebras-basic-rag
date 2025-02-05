import os
import PyPDF2
import docx
import generator

class Retriever:
    def __init__(self, data_source):
        self.data_source = data_source

    def retrieve(self, query):
        results = [doc for doc in self.data_source if query.lower() in doc.lower()]
        return results

    def process_pdf(self, file_path):
        with open(file_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = ''
            for page in reader.pages:
                text += page.extract_text() + '\n'
        return text

    def process_docx(self, file_path):
        doc = docx.Document(file_path)
        text = '\n'.join([para.text for para in doc.paragraphs])
        return text

    def process_txt(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
        return text

    def load_files(self, file_paths):
        all_texts = []
        for file_path in file_paths:
            if file_path.endswith('.pdf'):
                all_texts.append(self.process_pdf(file_path))
            elif file_path.endswith('.docx'):
                all_texts.append(self.process_docx(file_path))
            elif file_path.endswith('.txt'):
                all_texts.append(self.process_txt(file_path))
        self.data_source = all_texts
        g = generator.Generator()
        print(g.generate(self.data_source, input("Enter the prompt: ")))
        
    def __init__(self, data_source):
        self.data_source = data_source

    def retrieve(self, query):
        results = [doc for doc in self.data_source if query.lower() in doc.lower()]
        return results
