#Q15 = Create a nested function make_greeting that returns a greeting function customized with a given greeting message.

def make_greeting(greeting):
    def greet(name):
        return f"{greeting}, {name}!"
    return greet
greeting = input("Enter the greeting message: ")
name = input("Enter the name: ")
greeting_function = make_greeting(greeting)
message = greeting_function(name)
print(message)
