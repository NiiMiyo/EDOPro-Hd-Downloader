from command_handler import CommandHandler
from commands.cmd_allcards import COMMAND_ALLCARDS
from commands.cmd_all import COMMAND_ALL
from commands.cmd_allfields import COMMAND_ALLFIELDS
from commands.cmd_alltokens import COMMAND_ALLTOKENS
from commands.cmd_exit import COMMAND_EXIT
from commands.cmd_force import COMMAND_FORCE
from commands.cmd_help import COMMAND_HELP
from constants import SETUP_CREATION_FILES, SETUP_CREATION_FOLDERS

from os.path import exists
from os import makedirs

def setup_commands():
	CommandHandler.add_command(COMMAND_ALL)
	CommandHandler.add_command(COMMAND_ALLCARDS)
	CommandHandler.add_command(COMMAND_ALLFIELDS)
	CommandHandler.add_command(COMMAND_EXIT)
	CommandHandler.add_command(COMMAND_FORCE)
	CommandHandler.add_command(COMMAND_HELP)
	CommandHandler.add_command(COMMAND_ALLTOKENS)

def setup_files():
	for f in SETUP_CREATION_FILES:
		if not exists(f):
			with open(f, "w+"):
				# I only need that the files exist
				pass

def setup_folders():
	for f in SETUP_CREATION_FOLDERS:
		if not exists(f):
			makedirs(f)
