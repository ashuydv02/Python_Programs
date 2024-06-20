from typing import List, Dict, Tuple, Any, Optional


# Variables
name: str = "Ashish"
age: int = 20
salary: float = 5.505
# print(name, age, salary)


def demofunc() -> str:
    return "Hello"


print(demofunc())


# Dictinary
def words_count(text: str) -> Dict[str, int]:
    words = text.split()
    return {word: words.count(word) for word in set(words)}


print(words_count("Ashish Yadav Ashish"))


# List as Alias
number = List[int]
def even_numbers(num: int) -> number:
    return [n for n in range(num + 1) if n % 2 == 0]


print(even_numbers(50))


# Tuple
def odd_numbers(num: int) -> Tuple[int, ...]:
    return tuple([n for n in range(num + 1) if n % 2 == 1])


print(odd_numbers(50))


# Any
def demo(var: Any) -> Any:
    return var


print(demo("ashish"))


# Optional
def find_user(username: str) -> Optional[dict]:
    user_database = {'Ashish': {'age': 21}, 'Anil': {'age': 22}}
    return user_database.get(username)


print(find_user('Ashish'))
