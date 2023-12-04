from Bot import Bot
from info import In_out_commands
from flask import Flask


if __name__ == "__main__":
    bot = Bot(In_out_commands())
    in_out = In_out_commands()
    in_out.print_command(
        'Hello. I am your contact-assistant. What should I do with your contacts?')
    bot.book.load("auto_save")
    commands = ['Add', 'Search', 'Edit', 'Load',
                'Remove', 'Save', 'Congratulate', 'View', 'Exit']
    while True:
        action = in_out.input_command(
            'Type help for list of commands or enter your command\n').strip().lower()
        if action == 'help':
            format_str = str('{:%s%d}' % ('^', 20))
            for command in commands:
                in_out.print_command(format_str.format(command))
            action = in_out.input_command().strip().lower()
            bot.handle(action)
            if action in ['add', 'remove', 'edit']:
                bot.book.save("auto_save")
        else:
            bot.handle(action)
            if action in ['add', 'remove', 'edit']:
                bot.book.save("auto_save")
        if action == 'exit':
            break
