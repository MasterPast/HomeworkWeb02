from AddressBook import *
# from info import In_out_commands

class Bot:
    def __init__(self, in_out: In_out_commands):
        self.in_out = in_out
        self.book = AddressBook(in_out)

    def handle(self, action):
        if action == 'add':
            name = Name(self.in_out.input_command("Name: ")).value.strip()
            phones = Phone().value
            birth = Birthday().value
            email = Email().value.strip()
            status = Status().value.strip()
            note = Note(self.in_out.input_command("Note: ")).value
            record = Record(name, phones, birth, email, status, note)
            return self.book.add(record)
        elif action == 'search':
            self.in_out.print_command(
                "There are following categories: \nName \nPhones \nBirthday \nEmail \nStatus \nNote")
            category = self.in_out.input_command('Search category: ')
            pattern = self.in_out.input_command('Search pattern: ')
            result = (self.book.search(pattern, category))
            for account in result:
                if account['birthday']:
                    birth = account['birthday'].strftime("%d/%m/%Y")
                    result = "_" * 50 + "\n" + f"Name: {account['name']} \nPhones: {', '.join(account['phones'])} \nBirthday: {birth} \nEmail: {account['email']} \nStatus: {account['status']} \nNote: {account['note']}\n" + "_" * 50
                    self.in_out.print_command(result)
        elif action == 'edit':
            contact_name = self.in_out.input_command('Contact name: ')
            parameter = self.in_out.input_command(
                'Which parameter to edit(name, phones, birthday, status, email, note): ').strip()
            new_value = self.in_out.input_command("New Value: ")
            return self.book.edit(contact_name, parameter, new_value)
        elif action == 'remove':
            pattern = self.in_out.input_command(
                "Remove (contact name or phone): ")
            return self.book.remove(pattern)
        elif action == 'save':
            file_name = self.in_out.input_command("File name: ")
            return self.book.save(file_name)
        elif action == 'load':
            file_name = self.in_out.input_command("File name: ")
            return self.book.load(file_name)
        elif action == 'congratulate':
            self.in_out.print_command(self.book.congratulate())
        elif action == 'view':
            self.in_out.print_command(self.book)
        elif action == 'exit':
            pass
        else:
            self.in_out.print_command("There is no such command!")
