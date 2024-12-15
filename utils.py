import csv
import re
import random

class QuestionGenerator:
    def __init__(self, csv_file_path):
        self.csv_file_path = csv_file_path
        self.questions = self.generate_questions()
    
# define a template method
    def generate_questions(self):
        raise NotImplementedError("generate_questions() method must be implemented")
    

class QuestionGenerator_MOS(QuestionGenerator):
    def __init__(self, csv_file_path):
        self.csv_file_path = csv_file_path
        self.questions = self.generate_questions()

    def generate_questions(self):
        questions = []
        with open(self.csv_file_path, mode='r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for idx, row in enumerate(csv_reader, start=1):
                filename = row['filename']
                question = {
                    "id": idx,
                    "title": f"Question {idx}",  # Dynamically generate title
                    "audio_path": f"{filename}",  # Assume all files are in 'wavs/' directory
                    "name": f"q{idx}"  # Unique identifier for the question
                }
                questions.append(question)
        return questions
    

class QuestionGenerator_PMOS(QuestionGenerator):
    def __init__(self, csv_file_path):
        self.emodict = {'hap':'Happy', 'sad':'Sad', 'ang':'Angry', 'sur':'Surprised'}
        super().__init__(csv_file_path)
    def generate_questions(self):
        questions = []
        with open(self.csv_file_path, mode='r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for idx, row in enumerate(csv_reader, start=1):
                f1 = row['filename1']
                f2 = row['filename2']
                # get emotion label from filename
                emotion = self.emodict[f1.split('_')[-3][0:3]]

                question = {
                    "id": idx,
                    "title": f"Question {idx}:   {emotion} Speech",  # Dynamically generate title
                    "audio_paths": [f"{f1}", f"{f2}"],  # Assume all files are in 'wavs/' directory
                    "name": f"q{idx}"  # Unique identifier for the question
                }
                questions.append(question)
        return questions

# MOS with special function for filename processing
class QuestionGenerator_FMOS(QuestionGenerator):
    def __init__(self, csv_file_path, random_p=3):
        self.random_p = random_p
        self.regexpattern = r'dia(\d+)_utt(\d+)_R\[(\w+)\]_GT\[(\w+)\]'
        self.csv_file_path = csv_file_path
        self.questions = self.generate_questions()

    def generate_questions(self):
        questions = []
        filepath_list = []
        with open(self.csv_file_path, mode='r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                filepath_list.append(row['filepath'])

            for idx, filepath in enumerate(filepath_list, start=1):
                filename = filepath.split('/')[-1]
                match = re.match(self.regexpattern, filename)
                if match:
                    dia = match.group(1)
                    utt = match.group(2)
                    R = match.group(3)
                    GT = match.group(4)
                    mark = f"d{dia}_u{utt}_R{R[:2]}_G{GT[:2]}"
                else:
                    print("No match found")
                keywords = [R, GT]
                random.shuffle(keywords)
                question = {
                    "id": idx,
                    "title": f"Question {idx}",  # Dynamically generate title
                    "media_path": f"{filepath}",  # Assume all files are in 'wavs/' directory
                    "name": f"v{idx}-{mark}",  # Unique identifier for the question
                    "keywords": keywords
                }
                questions.append(question)
        return questions