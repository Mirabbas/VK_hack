from chat.chatter import Chatter, Two, One, Any, Compare, Join

chatter = Chatter()

hello = "привет", "приветики", "привет!", "ку", "привет"

only_hello = Any(hello, Compare.equals, 0)
has_hello = Any(hello, Compare.inside, 0)
has_hello_last = Any(hello, Compare.inside, 2)

chatter.add(Two(has_hello_last, has_hello, Join.everything), "ты уже здоровался!")
chatter.add(only_hello, "я приветствую тебя!")
chatter.add(has_hello, "я приветствую тебя, но я не понял остальной части предложения!")

chatter.add(One("", Compare.inside, 0), "Я не понял!", "Не понимаю!", "Что?")

