class form:
    questions=[]
    answers=[]
    def __init__(self):
        pass
    def add(self,question):
        self.questions.append(str(question))
    def ask(self,showNumber=True,showRemaining=False):
        self.answers=[]
        for ind,val in enumerate(self.questions):
            question=''
            if showNumber:
                question+=str(ind+1)
                if showRemaining:
                    question+="/"+str(len(self.questions))+": "
                else:
                    question+=": "
            question+=val+" "
            self.answers.append(input(question))
        return self.answers
