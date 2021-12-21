import contact
import contact_list

test_1=contact.Contact("john brown","brown@onet.pl","555234000")
test_2=contact.Contact("Anna May",   "am@o2.pl", "232000199")
test_3=contact.Contact("George Small",   "George Small", "222999100")
test_4=contact.Contact("Paola Big","bigpaola@poczta.pl","100200300")
lista=contact_list.Contact_List()
lista.add_cont(test_1)
lista.add_cont(test_2)
lista.add_cont(test_3)
lista.add_cont(test_4)
lista.display()
