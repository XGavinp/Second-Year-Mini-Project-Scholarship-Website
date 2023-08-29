import pickle

def function_b():
    return "Hello, world!"

def function_a():
    result = function_b()
    return result.upper()


with open('functions.pkl', 'wb') as f:
    pickle.dump(function_a, f)
    pickle.dump(function_b, f)


with open('functions.pkl', 'rb') as f:
    function_a = pickle.load(f)
    function_b = pickle.load(f)

result = function_a()
print(result)
