'''
Author : Artur Assis Alves
Date   : 09/06/2020
Title  : State Machine
'''
class User ():
    def __init__(self, user_type):
        self.user_type = user_type.lower()

class Document ():
    def __init__(self):
        self.state = Draft()

    def approve_publication(self, user):
        if (user.user_type == "admin"):
            self.state.admin_approval = True
        else:
            print("DENIED")

    def expire_publication(self):
        if (isinstance(self.state, Published)):
            self.state.publication_expired = True
            self.change_state(Draft())

    def fail_review(self):
        if (isinstance(self.state, Moderation)):
            self.state.review_failed = True

    def change_state(self, next_state):
        self.state = next_state

    def render(self, user):
        self.state.render(user, self)

    def publish(self, user):
        self.state.publish(user, self)

    def print_state(self):
        print("Document status : {}.".format(self.state.__class__.__name__.lower()))


class StateInterface:
    def publish(self,  user, document):
        pass
    def render(self, user, document):
        pass

class Draft(StateInterface):
    def publish(self,  user, document):
        if (user.user_type == "admin"):
            document.change_state(Published())
        elif (user.user_type == "author"):
            document.change_state(Moderation())
        else:
            print("DENIED")


class Moderation(StateInterface):
    def __init__(self):
        self.admin_approval = False
        self.review_failed  = False
    def publish(self,  user, document):
        if ( (user.user_type == "admin")or((user.user_type == "author")and(self.admin_approval)) ):
            document.change_state(Published())
        else:
            print("DENIED")

    def render(self, user, document):
        if (self.review_failed and (not(self.admin_approval))):
            document.change_state(Draft())


class Published (StateInterface):
    def __init__(self):
        self.publication_expired = False
    def publish(self,  user, document):
        pass
    def render(self, user, document):
        if (self.publication_expired):
            document.change_state(Draft())


if __name__=="__main__":
    administrador  = User("admin")
    autor          = User ("author")
    outro          = User("outro")
    documento      = Document()
    print("(1)-Autor publica :")
    documento.publish(autor)
    documento.print_state()
    print("(2)-Autor publica :")
    documento.publish(autor)
    documento.print_state()
    print("(3)-Documento falha na revisao :")
    documento.fail_review()
    documento.print_state()
    print("(4)-Autor processa o documento :")
    documento.render(autor)
    documento.print_state()
    print("(5)-Admin publica :")
    documento.publish(administrador)
    documento.print_state()
    print("(6)-Publicacao expira :")
    documento.expire_publication()
    documento.print_state()
    print("(7)-Autor publica :")
    documento.publish(autor)
    documento.print_state()
    print("(8)-Admin aprova o documento :")
    documento.approve_publication(administrador)
    documento.print_state()
    print("(9)-Autor publica :")
    documento.publish(autor)
    documento.print_state()
