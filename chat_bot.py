from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"[hH]ello|[hH]i|[aA]fternoon", ["Hello! Welcome to SoftUni! In order to provide better service,"
                                            "could you please tell us your name?"]
    ],
    [
        r"My name is (.*)", [f"Hello %1! How can we help you?"]
    ],
    [
        r"(.*) (python|java|javascript|perl)", ["If you need information about those courses you"
                    " can go at our site and in the search bar type on of the language you looking for!",
                    "For more information about courses you can always call us!"]
    ],
    [
        r"quit", ["Have a nice day!"]
    ],
    [
        r"No", ["Bye!"]
    ],
    [
        r"([oO]k)? [tT]hank you", ["Thank you too! Is there anything else I can help you with?",
                            "I am glad that I helped you! Something more I can assist you with?"]
    ],
    [
        r"(\w+)", ["Sorry, but I am not so smart yet! Please make yourself more clear or call us!", "Can you please ask something else?"
                   , "I need more information", "Sorry I can not answer this question!"]
    ]
]


def chatbot():
    print("Hello! This is RoboArti! How can I help you?")
    chat = Chat(pairs, reflections)
    return chat.converse()

if __name__ == "__main__":
    chatbot()
