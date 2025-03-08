class Comment:
    def __init__(self, author, text):
        self.text = text
        self.author = author
        self.replies = []  # Список відповідей
        self.is_deleted = False  # Прапорець видалення

    def reply(self, reply):
        self.replies.append(reply)

    def remove(self):
        self.text = "Цей коментар було видалено."
        self.author = None
        self.is_deleted = True

    def display(self, level=0):
        indent = "    " * level
        author = f"{self.author}: " if self.author else ""
        print(indent + author + self.text)
        for reply in self.replies:
            reply.display(level + 1)  # Рекурсивно виводимо вкладені коментарі

# Приклад використання
comment = Comment("Бодя", "Яка чудова книга!")

reply_1 = Comment("Андрій", "Книга повне розчарування :(")
comment.reply(reply_1)
reply_1.reply(Comment("Сергій", "Не книжка, а перевели купу паперу ні нащо..."))
reply_1.remove()

comment.reply(Comment("Марина", "Що в ній чудового?"))

comment.display()
