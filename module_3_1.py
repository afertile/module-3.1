calls = 0
def string_info(string):
    global calls
    calls += 1
    def count_calls(calls):
        calls += 1
        return calls
    info = []
    info.append(len(string))
    info.append(string.upper())
    info.append(string.lower())
    return tuple(info)
def is_contains(string, list_to_search):
    global calls
    calls += 1
    string = string.lower()
    new_list_to_search = []
    for i in list_to_search:
        i = i.lower()
        new_list_to_search.append(i)
    if string in new_list_to_search:
        return True
    else:
        return False
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)