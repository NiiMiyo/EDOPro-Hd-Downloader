from command_handler import CommandHandler
from commands.cmd_allcards import COMMAND_ALLCARDS
from commands.cmd_all import COMMAND_ALL
from commands.cmd_allfields import COMMAND_ALLFIELDS
from commands.cmd_exit import COMMAND_EXIT
from commands.cmd_force import COMMAND_FORCE
from commands.cmd_help import COMMAND_HELP


def setup_commands():
	CommandHandler.add_command(COMMAND_ALL)
	CommandHandler.add_command(COMMAND_ALLCARDS)
	CommandHandler.add_command(COMMAND_ALLFIELDS)
	CommandHandler.add_command(COMMAND_EXIT)
	CommandHandler.add_command(COMMAND_FORCE)
	CommandHandler.add_command(COMMAND_HELP)
