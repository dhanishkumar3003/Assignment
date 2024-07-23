def contains_special_character(s: str) -> bool:
    special_characters = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
    
    for char in s:
        if char in special_characters:
            print("contains special character")
            return 
    print("doesn'tcontains  special character")


if __name__=="__main__":
    
    contains_special_character("test")
    contains_special_character("test123")
    contains_special_character("test@")
