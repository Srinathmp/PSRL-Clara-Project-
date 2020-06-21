#Wrapper function which decides whether the feedback is provided for python or C program

import sys
import re
import keyword
from New_functions.built_in_functions import Interaction_module
from New_functions.ift_analysis import ift_feedback
from New_functions.operator_analysis import feedback_comp_operator, feedback_arth_operator, feedback_logic_operator
from New_functions.operator_analysis import feedback_incorrect_value

def check_equal(feedback):
	sections = feedback.split(" to ")
	sections[0] = sections[0].split("Change ")[1]

	#at index 1 and 3 the required set of strings are present which is to be compared 
	if sections[0] in sections[1]:
		return 1
	return 0

def feedback_channelizer(clara_feedback, inputs, arguements, lang):
	if(check_equal(clara_feedback)):   #function to check if feedback generated by clara is with no change suggestions 
		#print("Feedback Claimed to be Unnecessary :",clara_feedback)
		print("Unnecessary feedback!!!")
		return
	else:
		#print("Starting\n\n\n")
		builtin_checked = 0
		python_builtins = ['range', 'sum', 'return','reduced', 'slice','next', 'list','set', 'dict']
		keywords = keyword.kwlist

		if 'line' in clara_feedback:
			clara_split = clara_feedback.split('line ')
		elif 'at' in clara_feedback:
			clara_split = clara_feedback.split('at ')

		line_num = 0
		if (clara_split[1].split(' ')[0]).isdigit():
			line_num = clara_split[1].split(' ')[0]

		bltins_error = [] #To store the builtins where the user has gone wrong
		for blt in python_builtins:
			if (blt+"(") in clara_feedback:
				bltins_error.append(blt)

		if bltins_error != []:
			builtin_checked = 1
			print("Looks like you have made a logical mistake in usage of one of the builtin method or function",end = " ")
			if line_num:
				print("at line number : ",line_num)
			print("Would you like to know name of builtin?")
			print("yes/no\n")
			reply = input()
			if(reply == 'no' or reply == 'No' or reply == 'NO'):
				sys.exit("Nice!!! You don't want to giveup so easily. Happy coding!")
			else:
				Interaction_module(clara_feedback,bltins_error[0])

		#check for if it is a keyword
		'''
		keyword_error = []
		for key in keyword.kwlist:
			if key in clara_feedback:
				keyword_error.append(key)

		if keyword_error != []:
			print("Looks there are one or more keywords, where you have used it illogically with respect to given problem statement")
			print("This is at line number :",line_num)
			print("Do you ")
		'''
		ite_checked = 0
		if 'ite(' in clara_feedback:
			ite_checked = 1
			print("Looks like you have implemented if-then-else illogically with respect to the given problem statement.", end = " ")
			if line_num:
				print("This wrong implementation is at line number : ", line_num)
			print("It is recommended that you read through the problem statement again, before proceeding to debug")
			#implementation of effective feedback for ift
			print("Or you can choose to be given with a detailed explanation by pressing 1, orelse press 0 to exit\n")
			reply_1 = int(input())
			if(reply_1 == 0):
				sys.exit("Nice!!! You choose to debug on own. Happy coding!")
			else:
				ift_feedback(clara_feedback, inputs)

		#incorrect use of operators
		if not(builtin_checked) and not(ite_checked):
			arithmetic_operators = ['+','-','*','/','%']
			comparison_operators = ['==','!=','<','<=','>','>=']
			logical_operators = ['and', 'or', '&&', '||', '&', '|']

			segments = clara_feedback.split(" to ")
			segments[0] = segments[0].split("Change ")[1]
			segments[1] = segments[1].split(" at")[0]
			for op in arithmetic_operators+comparison_operators:
				if op in segments[0] and op not in segments[1]: #This is feasible for single operator error
					if op in arithmetic_operators:
						feedback_arth_operator(segments,op,line_num,clara_feedback)
					elif op in comparison_operators:
						feedback_comp_operator(segments, op, line_num, clara_feedback)
					elif op in logical_operators:
						feedback_logic_operator(segments, op, line_num, clara_feedback)

			#incorrect use of values
			# using re.findall() 
			# getting numbers from string  
			num1 = re.findall(r'\d+', segments[0]) 
			num2 = re.findall(r'\d+', segments[1]) 
			if num1 != [] and num2 != []: 
				if(num1[0] != num2[0]):
					feedback_incorrect_value(num1[0], num2[0], line_num, clara_feedback)
			elif num1 != [] or num2 != []:
				print("There might be an incorrect initialization", end = " ")
				if line_num:
					print("at line number :",line_num)
				print("It is recommended that you dry run through code look for right initialization")
				print("Repair to this has been generated, press 1 to see repair or 0 to exit")
				reply2 = int(input())
				if(reply2 == 1):
					print(clara_feedback, "\n\n")

		#incorrect return statements($ret)
		#incorrect conditional statements($cond)
		#incorrect initializations(tell that wrong answer is due to incorrect initialization of x, change it from this to this)
		#incorrect use of  operators
		#FOR most of feedbacks can compare between incorrect and correction expression given in feedback 




