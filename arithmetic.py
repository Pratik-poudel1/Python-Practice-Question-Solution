def add(a, b):
    return 'Addition of Two Numbers:',a + b

def subtract(a, b):
    return 'Subtraction of Two Numbers:',a - b

def multiply(a, b):
    return 'Multiple of Two Numbers:',a * b

def divide(a, b):
    if b != 0:
        return 'Division of Two Number:',a / b 
    else:
        "Cannot divide by zero"