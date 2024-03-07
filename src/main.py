from textnode import TextNode

def main():
    tn_1 = TextNode("testnode 1", "bold", "https://www.meatspin.co")
    tn_2 = TextNode("testnode 1", "bold", "https://www.meatspin.co")
    tn_3 = TextNode("not the same", "italic", "https://www.lol.com")

    print(tn_1.__repr__())
    print(tn_3.__repr__())
    print(tn_1.__eq__(tn_2))
    print(tn_3.__eq__(tn_1))
    print(tn_1)
    print(tn_1 == tn_2)
    
main()