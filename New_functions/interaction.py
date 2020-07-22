#Importing module which performs casual interaction with the user(can add more interactions)
from New_functions.bot_conversation import RecognizeSpeech_during_interaction
from gtts import gTTS
import os
import sys
from playsound import playsound

def conversation(entities, lang):
	try:
		language = 'en'
		rate = False
		if lang == 'c':
			prog_lang = "C language"
			#from Documentation.doc_testing import *
			from Documentation.doc_testing import if_statement_func, else_statement_func,array_doc_func,for_loop_func, operator_function
			from Documentation.doc_testing import while_loop_func, break_and_continue_func,return_func, available_documentation
			entity_func_dict = {'else': else_statement_func,'if':if_statement_func,'array':array_doc_func, 
				'for':for_loop_func, 'while':while_loop_func, 'break_and_continue_statements_and_else_clauses_on_loops':break_and_continue_func,
				'return':return_func, 'operator':operator_function}

			### Include entities return, variable, operator
		elif lang == 'py':
			prog_lang = "Python"
			#from Documentation.python_doc_testing import *
			from Documentation.python_doc_testing import if_statement_func, else_statement_func, elif_statement_func, python_nested_if_statements_func, for_loop_func,available_documentation
			from Documentation.python_doc_testing import range_function_func,break_and_continue_statements_and_else_clauses_on_loops_func, while_loop_func, list_doc_func, return_func, operator_function
			entity_func_dict = {'elif':elif_statement_func, 'else': else_statement_func,
							 'for':for_loop_func, 'if':if_statement_func, 'nested_if':python_nested_if_statements_func,
							 'range':range_function_func,'break_and_continue_statements_and_else_clauses_on_loops':break_and_continue_statements_and_else_clauses_on_loops_func,
							 'while':while_loop_func, 'list':list_doc_func,'return':return_func, 'operator':operator_function}
		status = 0
		for entity in entities:
			#say : Would you like to read about the 'entity' keyword
			#print("\nTo continue reading about,",entity,"Press 1, else press any key to continue :\n")
			print("Would you like to read about",entity,"keyword")
			speak = "Would you like to read about..." + entity + "keyword"
			speech_obj = gTTS(text = speak, lang = language, slow=rate)
			speech_obj.save('wit_bot.mp3')
			#os.system("mpg123 wit_bot.mp3")
			playsound('wit_bot.mp3', True)
			print("\n***Please speak now...\n")
			response =  RecognizeSpeech_during_interaction('myspeech.wav', 6)
			if response:
				if (response[0] == 'Agree' or response[1] == 'on') and (response[0] != 'Disagree'):
					if entity in list(entity_func_dict.keys()):
						speak = "Great!, we have got some explanation for you"
						speech_obj = gTTS(text = speak, lang = language, slow=rate)
						speech_obj.save('wit_bot.mp3')
						#os.system("mpg123 wit_bot.mp3")
						playsound('wit_bot.mp3', True)
						
						print("\n****************************************************\n")
						entity_func_dict[entity]()
						print("\n****************************************************\n")
					else:
						# print("Sorry!...We don't have related documentation for,",entity,"keyterm\n")
						# engine.say("Sorry...")
						# engine.runAndWait()
						print("Sorry we don't have related documentation for",entity,"keyword")
						speak = "Sorry!...We don't have related documentation for," + entity + "keyword."
						speak += ".It would be great if you could refer to the official" + prog_lang + "documentation and search for this programming keyterm"	
						speech_obj = gTTS(text = speak, lang = language, slow=rate)
						speech_obj.save('wit_bot.mp3')
						#os.system("mpg123 wit_bot.mp3")
						playsound('wit_bot.mp3', True)
						print("\n***The list of all the available documentations are : ")
						available_documentation()

				else:
					speak = "Exiting the bot, have a good day and happy coding"
					speech_obj = gTTS(text = speak, lang = language, slow=rate)
					speech_obj.save('wit_bot.mp3')
					#os.system("mpg123 wit_bot.mp3")
					playsound('wit_bot.mp3', True)
					sys.exit("\n***Happy Coding***\n")

			print("\nIf you would like to revisit the keywords recognised, to read further,press 1, else press 0 to exit\n")
			speak = "To revisit the keywords recognised for explanation,press 1, else press 0 to exit"
			speech_obj = gTTS(text = speak, lang = language, slow=rate)
			speech_obj.save('wit_bot.mp3')
			#os.system("mpg123 wit_bot.mp3")
			playsound('wit_bot.mp3', True)
			status = int(input())
			# if status == 0:
			# 	speak = "Have a Good day. Happy learning and coding!"
			# 	speech_obj = gTTS(text = speak, lang = 'en', slow=False)
			# 	speech_obj.save('wit_bot.mp3')
			# 	#os.system("mpg123 wit_bot.mp3")
			#playsound('wit_bot.mp3', True)
			# 	sys.exit("*** Happy Coding!!! ***\n")
		#----------------------------------------------------
		return status
	except Exception as err:
		print("Exception arose is ", err)