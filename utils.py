import csv

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