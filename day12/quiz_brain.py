class QuizBrain:
	def __init__(self,que_list):
		self.que_num=0
		self.que_list=que_list

	def next_question(self):
		question = self.que_list[self.que_num]
		self.que_num+=1
		print(f'{self.que_num+1}. {question.question} [True/False] : ')

	def more_question(self):
		return self.que_num < len(self.que_list)