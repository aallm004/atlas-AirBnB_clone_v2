#!/usr/bin/python3
""" Consol
e Module """
import cmd
import sys
from datetime import datetime
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import shlex
from sqlalchemy import Column, ForeignKey
classes = {'BaseModel': BaseModel, 'User': User, 'Place': Place,
               'State': State, 'City': City, 'Amenity': Amenity,
               'Review': Review
              }

class HBNBCommand(cmd.Cmd):
    """ Contains the functionality for the HBNB console"""

    # determines prompt for interactive/non-interactive modes
    prompt = '(hbnb) ' if sys.__stdin__.isatty() else ''

    classes = {
               'BaseModel': BaseModel, 'User': User, 'Place': Place,
               'State': State, 'City': City, 'Amenity': Amenity,
               'Review': Review
              }
    dot_cmds = ['all', 'count', 'show', 'destroy', 'update']
    types = {
             'number_rooms': int, 'number_bathrooms': int,
             'max_guest': int, 'price_by_night': int,
             'latitude': float, 'longitude': float
            }

    def preloop(self):
        """Prints if isatty is false"""
        if not sys.__stdin__.isatty():
            print('(hbnb)')

    def precmd(self, line):
        """Reformat command line for advanced command syntax.

        Usage: <class name>.<command>([<id> [<*args> or <**kwargs>]])
        (Brackets denote optional fields in usage example.)
        """
        _cmd = _cls = _id = _args = ''  # initialize line elements

        # scan for general formating - i.e '.', '(', ')'
        if not ('.' in line and '(' in line and ')' in line):
            return line

        try:  # parse line left to right
            pline = line[:]  # parsed line

            # isolate <class name>
            _cls = pline[:pline.find('.')]

            # isolate and validate <command>
            _cmd = pline[pline.find('.') + 1:pline.find('(')]
            if _cmd not in HBNBCommand.dot_cmds:
                raise Exception

            # if parantheses contain arguments, parse them
            pline = pline[pline.find('(') + 1:pline.find(')')]
            if pline:
                # partition args: (<id>, [<delim>], [<*args>])
                pline = pline.partition(', ')  # pline convert to tuple

                # isolate _id, stripping quotes
                _id = pline[0].replace('\"', '')
                # possible bug here:
                # empty quotes register as empty _id when replaced

                # if arguments exist beyond _id
                pline = pline[2].strip()  # pline is now str
                if pline:
                    # check for *args or **kwargs
                    if pline[0] == '{' and pline[-1] == '}' \
                            and type(eval(pline)) is dict:
                        _args = pline
                    else:
                        _args = pline.replace(',', '')
                        # _args = _args.replace('\"', '')
            line = ' '.join([_cmd, _cls, _id, _args])

        except Exception as mess:
            pass
        finally:
            return line

    def postcmd(self, stop, line):
        """Prints if isatty is false"""
        if not sys.__stdin__.isatty():
            print('(hbnb) ', end='')
        return stop

    def do_quit(self, command):
        """ Method to exit the HBNB console"""
        exit()

    def help_quit(self):
        """ Prints the help documentation for quit  """
        print("Exits the program with formatting\n")

    def do_EOF(self, arg):
        """ Handles EOF to exit program """
        print()
        exit()

    def help_EOF(self):
        """ Prints the help documentation for EOF """
        print("Exits the program without formatting\n")

    def emptyline(self):
        """ Overrides the emptyline method of CMD """
        pass

    def do_create(self, args):
        """ Create an object of any class"""
        if not args:
            print("** class name missing **")
            return
        args_list = args.split()
        class_name = args_list[0]
        if class_name not in self.classes:
            print("** class '{class_name}' doesn't exist**")
            return
        kwargs = {}
        # Parse Parameters
        try:
            for param in args_list[1:]:
                key, value = param.split('=')
                key = key.strip()
                value = value.strip()
                # Handle value types
                if value.startswith('"') and value.endswith('"'):
                    value = value[1:-1].replace('_', ' ')
                elif '.' in value:
                    value = float(value)
                else:
                    value = int(value)
                kwargs[key] = value
        except ValueError:
            print("** Invalid parameter value **")
            return
        except Exception as e:
            print(f"** Error parsing parameters: {e} **")
            return
        # Create instance and set attributes
        try:
            print("print before new_instance")
            new_instance = self.classes[class_name](**kwargs)
            print("print after new_instance")
            new_instance.save()
            print("print after save")
            print(new_instance.id)
        except Exception as e:
            print(f"** Error creating instance: {e} **")

    def help_create(self):
        """ Help information for the create method """
        print("Creates a class of any type")
        print("[Usage]: create <className>\n")

    def do_show(self, args):
        """ Method to show an individual object """
        new = args.partition(" ")
        c_name = new[0]
        c_id = new[2]
        
        instance_key = f"{c_name}.{c_id}"
        # guard against trailing args
        if c_id and ' ' in c_id:
            c_id = c_id.partition(' ')[0]
            instance_key = f"{c_name}.{c_id}"
            print(instance_key)
        if not c_name:
            print("** class name missing **")
            return

        if c_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if not c_id:
            print("** instance id missing **")
            return

        try:
            print(storage.all()[instance_key])
        except KeyError:
            print("** no instance found **")

    def help_show(self):
        """ Help information for the show command """
        print("Shows an individual instance of a class")
        print("[Usage]: show <className> <objectId>\n")

    def do_destroy(self, args):
        """ Destroys a specified object """
        new = args.partition(" ")
        c_name = new[0]
        c_id = new[2]
        if c_id and ' ' in c_id:
            c_id = c_id.partition(' ')[0]

        if not c_name:
            print("** class name missing **")
            return

        if c_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if not c_id:
            print("** instance id missing **")
            return

        key = c_name + "." + c_id
        
        try:
            for k, v in storage.all().items():
                if k == key:
                    print("Deleting")
                    storage.delete(v)
                    storage.save()
        except KeyError:
            print("** no instance found **")

    def help_destroy(self):
        """ Help information for the destroy command """
        print("Destroys an individual instance of a class")
        print("[Usage]: destroy <className> <objectId>\n")

    def do_all(self, args):
        """ Shows all objects, or all objects of a class"""
        print_list = []

        if args:
            args = args.split(' ')[0]  # remove possible trailing args
            if args not in HBNBCommand.classes:
                print("** class doesn't exist **")
                return
            for k, v in storage.all(args).items():
                if k.split('.')[0] == args:
                    print_list.append(str(v))
        else:
            for k, v in storage.all().items():
                print_list.append(str(v))

        print(print_list)

    def help_all(self):
        """ Help information for the all command """
        print("Shows all objects, or all of a class")
        print("[Usage]: all <className>\n")

    def do_count(self, args):
        """Count current number of class instances"""
        count = 0
        for k, v in storage.__objects.items():
            if args == k.split('.')[0]:
                count += 1
        print(count)

    def help_count(self):
        """ """
        print("Usage: count <class_name>")

    def do_update(self, arg):
        """
        Update an instance based on the class name, id, attribute & value.
        Example: update State 123 name "California"
        """
        args = shlex.split(arg)
        att_val = ''
        att_name = ''
        instance_key = ''

        # Check if there are enough arguments
        if len(args) < 4:
            print(f"** Missing arguments ({len(args)}) **")
            return

        # Extract relevant arguments
        class_name, instance_id, attr_name, attr_value = args[:4]

        # Generate instance_key and class_name_str
        class_name_str = list(self.classes.keys())[list(self.classes.values()).index(self.classes[class_name])]
        instance_key = f"{class_name}.{instance_id}"


        # Check if the instance exists
        if instance_key not in storage.all(class_name).keys():
            print (storage.all(class_name).keys())
            print("** No instance found **")
            return

        # Convert attribute value to int or float if needed
            try:
                attr_value = int(attr_value)
            except ValueError:
                attr_value = 0
        elif att_name in ["latitude", "longitude"]:
            try:
                attr_value = float(attr_value)
            except ValueError:
                attr_value = 0.0

        setattr(storage.all()[instance_key], att_name, attr_value)
        storage.all()[instance_key].save()

        print(args)
        if len(args) == 4:
            att_name = args[2]
            att_val = args[3]
            if att_name and att_val:
                print ("updating value")
                setattr(storage.all()[instance_key], att_name, att_val)
                storage.all()[instance_key].save()
            elif att_name:
                print("** 327 value missing **")
            else:
                print("** 331 attribute name missing **")

            # generate key from class and id
        #class_name_str = list(self.classes.keys())[list(self.classes.values()).index(self.classes[class_name])]
    
        #instance_key = f"{class_name}.{instance_key}"
    

            # determine if key is present
        if instance_key not in storage.all():
            print(instance_key)
            print(storage.all().keys())
            print("** no instance found **")
            return

            # first determine if kwargs or args
        if '{' in args[2] and '}' in args[2] and type(eval(args[2])) is dict:
            kwargs = eval(args[2])
            args = []  # reformat kwargs into list, ex: [<name>, <value>, ...]
            for k, v in kwargs.items():
                args.append(k)
                args.append(v)
        else:  # isolate args
            args = args[2]
            if args and args[0] == '\"':  # check for quoted arg
                second_quote = args.find('\"', 1)
                att_name = args[1:second_quote]
                args = args[second_quote + 1:]

            args = args.partition(' ')

                # if att_name was not quoted arg
            if not att_name and args[0] != ' ':
                att_name = args[0]
                # check for quoted val arg
            if args[2] and args[2][0] == '\"':
                    att_val = args[2][1:args[2].find('\"', 1)]

                # if att_val was not quoted arg
            if not att_val and args[2]:
                att_val = args[2].partition(' ')[0]

            args = [att_name, att_val]

            # retrieve dictionary of current objects
            new_dict = storage.all()[instance_key]

            # iterate through attr names and values
            for i, att_name in enumerate(args):
                # block only runs on even iterations
                if (i % 2 == 0):
                    att_val = args[i + 1]  # following item is value
                    if not att_name:  # check for att_name
                        print("** attribute name missing **")
                        return
                    if not att_val:  # check for att_value
                        print(f"** 385 value missing{args}**")
                        return
                    # type cast as necessary
                    if att_name in HBNBCommand.types:
                        att_val = HBNBCommand.types[att_name](att_val)

                    # update dictionary with name, value pair
                    new_dict.__dict__.update({att_name: att_val})

            new_dict.save()  # save updates to file

    def help_update(self):
        """ Help information for the update class """
        print("Updates an object with new information")
        print("Usage: update <className> <id> <attName> <attVal>\n")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
