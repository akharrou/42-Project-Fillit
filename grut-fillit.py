# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    grut-fillit.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: akharrou <akharrou@student.42.us.org>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/05/15 17:19:55 by akharrou          #+#    #+#              #
#    Updated: 2019/05/15 17:46:23 by akharrou         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

try:

	import os
	import sys

	# COLORIZATION — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — #

	RED        = '\033[31m'
	GREEN      = '\033[32m'
	YELLOW     = '\033[38;2;247;249;94m'
	GOLD       = '\033[38;2;218;171;119m'

	DEFAULT    = '\033[0m'
	ITALTIC    = '\033[3m'
	UNDELRINED = '\033[4m'
	BACKGROUND = '\033[0m'
	STRIPS     = GOLD

	RED_BACKGROUND    = '\033[41m'

	# TITLES — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — #

	FILENAME = 'grut-fillit.py'

	TITLE    = 'GENERALIZED RAMBO UNIT-TESTER ™️'
	EDITION  = 'Fillit Edition'

	# FORMAT CONSTANTS — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — #

	BAR_LEN  = 105

	COL1_LEN = 38
	COL2_LEN = 20
	COL3_LEN = 20
	COL4_LEN = 11

	# USAGE & MANUAL — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — #

	def usage():
		print(f'usage: python3 {FILENAME} [-f {UNDELRINED}file{DEFAULT} ... | {UNDELRINED}input_argument{DEFAULT} ...]')
		sys.exit(1)

	def manual():
		print(f'{UNDELRINED}Coming soon...{DEFAULT}')
		sys.exit(1)

	# FLAG HANDLING — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — #

	if (len(sys.argv) < 2        or
		sys.argv[1] == '-h'      or
		sys.argv[1] == '--help'  or
		sys.argv[1] == ''):

		usage()

	elif (sys.argv[1] == '-m'        or
		sys.argv[1] == '-man'      or
		sys.argv[1] == '-manual'   or
		sys.argv[1] == '--manual'):

		manual()

	elif (sys.argv[1] == '-f'):

		if (len(sys.argv[2:]) < 1):
			usage()

		try:

			arguments = []
			sys.argv = sys.argv[2:]
			for argsFile in sys.argv:

				try:

					with open(argsFile, 'r') as fd:
						arguments.extend(fd.readlines())

				except Exception:
					print('Invalid Input File')

		except Exception as e:
			usage()

	else:
		arguments = sys.argv[1:]

	# # DYNAMIC INPUT — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — #

	try:
		launch_command_programA = os.environ["LAUNCH_PROGRAM_A"]
	except Exception:
		launch_command_programA = str(input("[LAUNCH COMMAND -- Program_A] (w/out arguments): "))
		print(f"\nSet variable:\nexport LAUNCH_PROGRAM_A='{launch_command_programA}'")
		print('\n')

	try:
		launch_command_programB = os.environ["LAUNCH_PROGRAM_B"]
	except Exception:
		launch_command_programB = str(input("[LAUNCH COMMAND -- Program_B] (w/out arguments): "))
		print(f"\nSet variable:\nexport LAUNCH_PROGRAM_B='{launch_command_programB}'")
		print('\n')

	# # HEADER — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — #

	print(f'{STRIPS}{f"=" * (BAR_LEN + 2)}')
	print(f'|{DEFAULT}{BACKGROUND}{f" " * (BAR_LEN)}{DEFAULT}{STRIPS}|')
	print(f'|{DEFAULT}{BACKGROUND}{f" " * (int((BAR_LEN - 3) / 2) - int(len(TITLE) / 2))}⚜️  {DEFAULT}{TITLE}{DEFAULT}{BACKGROUND}  ⚜️{f" " * (int((BAR_LEN - 3) / 2) - int(len(TITLE) / 2) - 2)}{DEFAULT}{STRIPS}|')
	print(f'|{DEFAULT}{BACKGROUND}{f" " * int((BAR_LEN - 3) / 2 - int(len(EDITION) / 2))}~ {ITALTIC}{EDITION}{DEFAULT}{BACKGROUND} ~{f" " * (int((BAR_LEN - 3) / 2 - int(len(EDITION) / 2)) - 1 - (len(EDITION) % 2))}{DEFAULT}{STRIPS}|')
	print(f'|{DEFAULT}{BACKGROUND}{f" " * (BAR_LEN)}{DEFAULT}{STRIPS}|')
	print(f'{STRIPS}{f"=" * (BAR_LEN + 2)}{DEFAULT}')

	# BODY — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — #

	print(f'\nProgram A Launch Command: {launch_command_programA}')
	print(f'Program B Launch Command: {launch_command_programB}')
	print('')

	FILE_A = '__output_A__'
	FILE_B = '__output_B__'

	def GRUTBody__fillit(program_A, program_B):

		i = 0
		total_trues = 0
		total_args = len(arguments)
		width = len(str(total_args))

		print(f' {f"—" * (BAR_LEN + width)}')
		print(f'| {"":{width}} |  {"INPUT:":{COL1_LEN}}|   {"PROGRAM A:":{COL2_LEN}}|   {"PROGRAM B:":{COL3_LEN}}|  {"IDENTICAL":{COL4_LEN}}|')
		print(f'|-{"-" * width}-|{"-" * (COL1_LEN + 2)}|{"-" * (COL2_LEN + 3)}|{"-" * (COL2_LEN + 3)}|{"-" * 13}|')

		with open(f"{FILE_A}", 'w+') as fd_A:
			with open(f"{FILE_B}", 'w+') as fd_B:

					for arg in arguments:

						arg = arg.strip('\n').replace('\t', '    ')

						with open(arg, 'r') as fd_input:

							test_trues = 0

							i += 1
							os.system(f'{program_A} "{arg}" > {FILE_A}')
							os.system(f'{program_B} "{arg}" > {FILE_B}')

							fd_A.seek(0)
							fd_B.seek(0)

							inputFile = fd_input.readlines()
							inputFile.insert(0, '')
							inputFile.insert(0, arg)

							outputs = list(zip(fd_A.readlines(), fd_B.readlines(), inputFile))

							programA_output = outputs[0][0].rstrip('\n')
							programB_output = outputs[0][1].rstrip('\n')
							arg_input = outputs[0][2].rstrip('\n')

							print(f"""| {i:0{width}} |  FILE: {f'{UNDELRINED}{arg_input}{DEFAULT}':{COL1_LEN + 2}}|   {programA_output:{COL2_LEN}}|   {programB_output:{COL3_LEN}}| """, end="")

							outputs = outputs[1:]

							if (programA_output == programB_output):
								print(f'  {f"[{GREEN}TRUE{DEFAULT}]":{COL4_LEN + 8}}|')
								test_trues += 1
							else:
								print(f'  {f"[{RED}FALSE{DEFAULT}]":{COL4_LEN + 8}}|')

							lines_read = 1
							for lineA, lineB, lineInput in outputs:

								lines_read += 1

								programA_output = lineA.rstrip('\n')
								programB_output = lineB.rstrip('\n')
								arg_input = lineInput.rstrip('\n')

								print(f"""| {'':{width}} |  {f'{arg_input}':{COL1_LEN}}|   {programA_output:{COL2_LEN}}|   {programB_output:{COL3_LEN}}| """, end="")

								if (programA_output == programB_output):
									print(f'  {f"[{GREEN}TRUE{DEFAULT}]":{COL4_LEN + 8}}|')
									test_trues += 1
								else:
									print(f'  {f"[{RED}FALSE{DEFAULT}]":{COL4_LEN + 8}}|')

							if (test_trues == len(outputs) + 1):
								total_trues += 1

							arg_input = inputFile[lines_read:]
							for line in arg_input:
								print(f"""| {'':{width}} |  {f'{line}':{COL1_LEN}}|   {'':{COL2_LEN}}|   {'':{COL3_LEN}}| """, end="")

							print(f' {f"—" * (BAR_LEN + width)}')


			print(f'\n[{total_trues} / {i}] IDENTICAL RESULTS ')

			os.remove(f'{FILE_A}')
			os.remove(f'{FILE_B}')

	GRUTBody__fillit(launch_command_programA, launch_command_programB)

# 	# FOOTER — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — #

	print(f'️\n{UNDELRINED}Share if you found it useful !{DEFAULT} :: G.R.U.T -- © 2019 {UNDELRINED}kmira{DEFAULT} & {UNDELRINED}akharrou{DEFAULT} 🤩')
	print('')

except Exception as e:
	print(f' {f"—" * (BAR_LEN)}\n')
	print(f'{RED_BACKGROUND}{YELLOW}💣  G.R.U.T CRASHED 💣{DEFAULT}\n')
	print(f'{UNDELRINED}\n🚨  Please Report the Issue ! 🚨{DEFAULT}  :: G.R.U.T -- © 2019 {UNDELRINED}kmira{DEFAULT} & {UNDELRINED}akharrou{DEFAULT} 😓')
	print(f'{DEFAULT}Copy paste the following and {YELLOW}report or dm{DEFAULT} us @akharrou / @kmira the issue\n\n')
	print(f'{UNDELRINED}GRUT ISSUE:\n{DEFAULT}{RED_BACKGROUND}{ITALTIC}')
	raise e
